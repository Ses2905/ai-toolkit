#!/usr/bin/env python3
"""Skills database for Work Kit: scan, categorize, rank, and find skills.

Scans every ``skills/*/SKILL.md`` in the repo, parses its YAML frontmatter,
assigns each skill a category, computes a transparent 0-100 ranking score, and
can either search skills from the terminal (``find``) or regenerate the
committed database artifacts (``build``): a machine-readable JSON index, a
categorized+ranked ``SKILLS.md`` catalog, and a self-contained
``skills-database.html`` page with search/filter/sort built in.

Pure standard library, with an optional PyYAML fast path for frontmatter.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

try:
    import yaml  # optional; a minimal fallback parser is used when absent
except ImportError:  # pragma: no cover - exercised only without PyYAML
    yaml = None


# --- Taxonomy -------------------------------------------------------------

# Category display order. Every skill resolves to exactly one of these.
CATEGORIES: list[str] = [
    "Product & Discovery",
    "Design & Frontend",
    "Motion & Animation",
    "Presentations & Diagrams",
    "Engineering Workflow",
    "Setup & Install",
]

UNCATEGORIZED = "Uncategorized"

# PM skills carry a `theme` in frontmatter; map each theme to its category.
CATEGORY_BY_THEME: dict[str, str] = {
    "pm-artifacts": "Product & Discovery",
    "discovery-research": "Product & Discovery",
    "strategy-positioning": "Product & Discovery",
    "validation-experiments": "Product & Discovery",
    "market-intelligence": "Product & Discovery",
    "workshops-facilitation": "Product & Discovery",
}

# Explicit overrides for skills whose category is unambiguous by name.
CATEGORY_BY_NAME: dict[str, str] = {
    # Design & Frontend
    "apple-design": "Design & Frontend",
    "canvas-design": "Design & Frontend",
    "design-artifact": "Design & Frontend",
    "design-system": "Design & Frontend",
    "frontend-design": "Design & Frontend",
    "high-end-visual-design": "Design & Frontend",
    "taste-skill": "Design & Frontend",
    "web-design-guidelines": "Design & Frontend",
    "react-bits": "Design & Frontend",
    # Motion & Animation
    "find-animation-opportunities": "Motion & Animation",
    "improve-animations": "Motion & Animation",
    "review-animations": "Motion & Animation",
    "hyperframes-animation": "Motion & Animation",
    "hyperframes-core": "Motion & Animation",
    "remotion-best-practices": "Motion & Animation",
    # Presentations & Diagrams
    "slides": "Presentations & Diagrams",
    "frontend-slides-editable": "Presentations & Diagrams",
    "html-ppt": "Presentations & Diagrams",
    "html-diagram": "Presentations & Diagrams",
    "lark-slides": "Presentations & Diagrams",
    "lark-shared": "Presentations & Diagrams",
    # Engineering Workflow
    "plan-the-work": "Engineering Workflow",
    "debug-from-evidence": "Engineering Workflow",
    "review-the-diff": "Engineering Workflow",
    "ship-the-change": "Engineering Workflow",
    "capture-a-skill": "Engineering Workflow",
    "pm-handoff": "Engineering Workflow",
    # Setup & Install
    "install-github-skills": "Setup & Install",
    "install-impeccable": "Setup & Install",
    "install-open-design": "Setup & Install",
    "install-work-kit": "Setup & Install",
}

# Keyword fallback so future skills auto-classify without code edits.
# Ordered: first category whose pattern matches name+description wins.
KEYWORD_RULES: list[tuple[str, str]] = [
    ("Setup & Install", r"\binstall|setup|scaffold\b"),
    ("Motion & Animation", r"animat|motion|gsap|remotion|hyperframe|spring|easing"),
    ("Presentations & Diagrams", r"slide|deck|presentation|ppt|keynote|diagram|feishu|lark"),
    ("Design & Frontend", r"design|frontend|ui|ux|typograph|visual|css|component|token"),
    (
        "Product & Discovery",
        r"product|discovery|persona|roadmap|user story|epic|positioning|jtbd|"
        r"jobs.to.be.done|opportunity|workshop|hypothesis|prioriti|press release|"
        r"canvas|interview|market",
    ),
    ("Engineering Workflow", r"debug|plan|review|ship|commit|diff|test|refactor"),
]

# Category → short blurb for the catalog / HTML headers.
CATEGORY_BLURB: dict[str, str] = {
    "Product & Discovery": "Frame problems, run discovery, and shape product strategy before building.",
    "Design & Frontend": "Distinctive UI, design systems, typography, and visual direction.",
    "Motion & Animation": "Add, audit, and review motion with a craft bar for animation.",
    "Presentations & Diagrams": "Build editable decks, HTML presentations, and self-contained diagrams.",
    "Engineering Workflow": "Plan, debug from evidence, review the diff, ship a clean commit, and hand off a session.",
    "Setup & Install": "Install this kit and pull in external skill catalogs and tools.",
}


# --- Scoring rubric -------------------------------------------------------
# Transparent, capped contributions. Reported score is normalized to 0-100.

SCORE_WEIGHTS: dict[str, int] = {
    "command": 12,   # has a /command entry point
    "rule": 8,       # has an auto-applying rule
    "scripts": 8,    # ships executable tooling
    "tests": 6,      # ships automated tests
    "examples": 4,   # ships worked examples
    "docs": 3,       # ships extra docs
    "doc_depth": 20,  # SKILL.md richness (scaled by size)
    "breadth": 12,   # number of bundled files (scaled)
    "metadata": 10,  # description + best_for + theme/type completeness
    "catalog": 5,    # referenced by a catalog preset
    "readme": 5,     # referenced in README
}
MAX_RAW = sum(SCORE_WEIGHTS.values())


@dataclass
class Skill:
    name: str
    category: str
    type: str
    theme: str
    description: str
    argument_hint: str
    best_for: list[str]
    command: str
    has_command: bool
    has_rule: bool
    has_scripts: bool
    has_tests: bool
    has_examples: bool
    has_docs: bool
    file_count: int
    skill_md_bytes: int
    in_catalog: bool
    in_readme: bool
    score: int = 0
    score_breakdown: dict[str, int] = field(default_factory=dict)
    rank_overall: int = 0
    rank_in_category: int = 0

    @property
    def tags(self) -> list[str]:
        tags: list[str] = []
        if self.type:
            tags.append(self.type)
        if self.theme:
            tags.append(self.theme)
        return tags


# --- Frontmatter parsing --------------------------------------------------

def _split_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    if end == -1:
        return ""
    return text[text.find("\n", 3) + 1 : end + 1]


def _minimal_yaml(block: str) -> dict:
    """Tiny frontmatter parser for the fields this tool needs.

    Handles ``key: value``, quoted scalars, block scalars (``>-``/``|``), and
    simple ``- item`` lists. Used only when PyYAML is unavailable.
    """
    data: dict[str, object] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        if not raw.strip() or raw.lstrip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", raw)
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).strip()
        if val in (">-", ">", "|", "|-", ">+"):
            collected: list[str] = []
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith((" ", "\t"))):
                collected.append(lines[i].strip())
                i += 1
            data[key] = " ".join(c for c in collected if c).strip()
            continue
        if val == "":
            items: list[str] = []
            j = i + 1
            while j < len(lines) and re.match(r"^\s*-\s+", lines[j]):
                items.append(re.sub(r'^\s*-\s+', "", lines[j]).strip().strip('"\''))
                j += 1
            if items:
                data[key] = items
                i = j
                continue
            data[key] = ""
            i += 1
            continue
        data[key] = val.strip().strip('"\'')
        i += 1
    return data


def parse_frontmatter(text: str) -> dict:
    block = _split_frontmatter(text)
    if not block:
        return {}
    if yaml is not None:
        try:
            loaded = yaml.safe_load(block)
            if isinstance(loaded, dict):
                return loaded
        except yaml.YAMLError:
            pass
    return _minimal_yaml(block)


# --- Categorization + scoring ---------------------------------------------

def categorize(name: str, theme: str, description: str) -> str:
    if name in CATEGORY_BY_NAME:
        return CATEGORY_BY_NAME[name]
    if theme in CATEGORY_BY_THEME:
        return CATEGORY_BY_THEME[theme]
    haystack = f"{name} {description}".lower()
    for category, pattern in KEYWORD_RULES:
        if re.search(pattern, haystack):
            return category
    return UNCATEGORIZED


def score_skill(skill: Skill) -> tuple[int, dict[str, int]]:
    b: dict[str, int] = {}
    b["command"] = SCORE_WEIGHTS["command"] if skill.has_command else 0
    b["rule"] = SCORE_WEIGHTS["rule"] if skill.has_rule else 0
    b["scripts"] = SCORE_WEIGHTS["scripts"] if skill.has_scripts else 0
    b["tests"] = SCORE_WEIGHTS["tests"] if skill.has_tests else 0
    b["examples"] = SCORE_WEIGHTS["examples"] if skill.has_examples else 0
    b["docs"] = SCORE_WEIGHTS["docs"] if skill.has_docs else 0
    b["doc_depth"] = min(
        SCORE_WEIGHTS["doc_depth"], round(skill.skill_md_bytes / 1024 * 2)
    )
    b["breadth"] = min(SCORE_WEIGHTS["breadth"], skill.file_count)
    meta = 0
    if skill.description:
        meta += 5
    if skill.best_for:
        meta += 3
    if skill.theme and skill.type:
        meta += 2
    b["metadata"] = min(SCORE_WEIGHTS["metadata"], meta)
    b["catalog"] = SCORE_WEIGHTS["catalog"] if skill.in_catalog else 0
    b["readme"] = SCORE_WEIGHTS["readme"] if skill.in_readme else 0
    raw = sum(b.values())
    return round(raw / MAX_RAW * 100), b


# --- Scanning -------------------------------------------------------------

def _preset_keys(root: Path) -> set[str]:
    presets_path = root / "catalog" / "presets.json"
    if not presets_path.is_file():
        return set()
    try:
        data = json.loads(presets_path.read_text())
    except json.JSONDecodeError:
        return set()
    return set(data.get("presets", {}).keys())


def _command_by_skill(root: Path) -> dict[str, str]:
    """Map skill name -> command stem.

    Command files are often named differently from the skill (e.g. ``plan.md``
    -> ``plan-the-work``), so link them by the ``skills/<name>/`` reference in
    the command body, falling back to a stem that matches a skill directory.
    """
    commands_dir = root / "commands"
    if not commands_dir.is_dir():
        return {}
    skill_names = {p.name for p in (root / "skills").glob("*") if (p / "SKILL.md").is_file()}
    mapping: dict[str, str] = {}
    for cmd in sorted(commands_dir.glob("*.md")):
        body = cmd.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"skills/([a-z0-9-]+)/", body)
        if m and m.group(1) in skill_names:
            mapping.setdefault(m.group(1), cmd.stem)
        elif cmd.stem in skill_names:
            mapping.setdefault(cmd.stem, cmd.stem)
    return mapping


def scan_skills(root: Path) -> list[Skill]:
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        raise SystemExit(f"No skills/ directory at {skills_dir}")

    command_by_skill = _command_by_skill(root)
    rules = {p.stem for p in (root / "rules").glob("*.mdc")} if (root / "rules").is_dir() else set()
    preset_keys = _preset_keys(root)
    readme_text = (root / "README.md").read_text() if (root / "README.md").is_file() else ""

    skills: list[Skill] = []
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        d = skill_md.parent
        name = d.name
        fm = parse_frontmatter(skill_md.read_text(encoding="utf-8", errors="replace"))
        theme = str(fm.get("theme", "") or "")
        description = str(fm.get("description", "") or "").strip()
        best_for = fm.get("best_for") or []
        if not isinstance(best_for, list):
            best_for = [str(best_for)]
        best_for = [str(x) for x in best_for]

        files = [p for p in d.rglob("*") if p.is_file()]
        skill = Skill(
            name=name,
            category=categorize(name, theme, description),
            type=str(fm.get("type", "") or ""),
            theme=theme,
            description=description,
            argument_hint=str(fm.get("argument-hint", "") or ""),
            best_for=best_for,
            command=command_by_skill.get(name, ""),
            has_command=name in command_by_skill,
            has_rule=name in rules,
            has_scripts=(d / "scripts").is_dir(),
            has_tests=bool(list(d.rglob("*_test.py")) + list(d.rglob("test_*.py"))),
            has_examples=(d / "examples").is_dir(),
            has_docs=(d / "docs").is_dir(),
            file_count=len(files),
            skill_md_bytes=skill_md.stat().st_size,
            in_catalog=name in preset_keys,
            in_readme=bool(re.search(rf"`{re.escape(name)}`", readme_text)),
        )
        skill.score, skill.score_breakdown = score_skill(skill)
        skills.append(skill)

    _assign_ranks(skills)
    return skills


def _assign_ranks(skills: list[Skill]) -> None:
    for i, s in enumerate(sorted(skills, key=lambda s: (-s.score, s.name)), start=1):
        s.rank_overall = i
    by_cat: dict[str, list[Skill]] = {}
    for s in skills:
        by_cat.setdefault(s.category, []).append(s)
    for group in by_cat.values():
        for i, s in enumerate(sorted(group, key=lambda s: (-s.score, s.name)), start=1):
            s.rank_in_category = i


# --- Find (search) --------------------------------------------------------

def search(skills: list[Skill], query: str) -> list[tuple[Skill, int]]:
    """Return (skill, relevance) sorted by relevance then score."""
    tokens = [t for t in re.split(r"\s+", query.lower().strip()) if t]
    scored: list[tuple[Skill, int]] = []
    for s in skills:
        rel = 0
        name = s.name.lower()
        desc = s.description.lower()
        cat = s.category.lower()
        best = " ".join(s.best_for).lower()
        tags = " ".join(s.tags).lower()
        for tok in tokens:
            if tok == name:
                rel += 100
            elif tok in name:
                rel += 40
            if tok in desc:
                rel += 12
            if tok in cat:
                rel += 8
            if tok in best:
                rel += 6
            if tok in tags:
                rel += 4
        if rel > 0 or not tokens:
            scored.append((s, rel))
    scored.sort(key=lambda pair: (-pair[1], -pair[0].score, pair[0].name))
    return scored


# --- Output generators ----------------------------------------------------

def build_index(skills: list[Skill]) -> dict:
    return {
        "generated_by": "scripts/skills_db.py",
        "categories": CATEGORIES,
        "score_weights": SCORE_WEIGHTS,
        "score_max_raw": MAX_RAW,
        "total": len(skills),
        "counts_by_category": {
            c: sum(1 for s in skills if s.category == c) for c in CATEGORIES
        },
        "skills": [asdict(s) for s in sorted(skills, key=lambda s: s.rank_overall)],
    }


def render_markdown(skills: list[Skill]) -> str:
    lines: list[str] = []
    lines.append("# Work Kit Skills Database")
    lines.append("")
    lines.append(
        "Auto-generated by `scripts/skills_db.py build`. Do not edit by hand — "
        "run the builder to refresh. Search from the terminal with "
        "`./scripts/skills-db.sh find <query>` or open `skills-database.html`."
    )
    lines.append("")
    lines.append(f"**{len(skills)} skills** across **{len(CATEGORIES)} categories**. "
                 "Score (0-100) rewards invocability (command/rule), bundled tooling "
                 "(scripts/tests/examples/docs), doc depth, metadata completeness, and "
                 "catalog/README integration.")
    lines.append("")

    lines.append("## Categories")
    lines.append("")
    lines.append("| Category | Skills | Blurb |")
    lines.append("| --- | --- | --- |")
    for c in CATEGORIES:
        n = sum(1 for s in skills if s.category == c)
        lines.append(f"| {c} | {n} | {CATEGORY_BLURB.get(c, '')} |")
    lines.append("")

    lines.append("## Top skills (overall rank)")
    lines.append("")
    lines.append("| # | Skill | Category | Score |")
    lines.append("| --- | --- | --- | --- |")
    for s in sorted(skills, key=lambda s: s.rank_overall)[:10]:
        lines.append(f"| {s.rank_overall} | `{s.name}` | {s.category} | {s.score} |")
    lines.append("")

    for c in CATEGORIES:
        group = sorted(
            [s for s in skills if s.category == c], key=lambda s: s.rank_in_category
        )
        if not group:
            continue
        lines.append(f"## {c}")
        lines.append("")
        lines.append(f"_{CATEGORY_BLURB.get(c, '')}_")
        lines.append("")
        lines.append("| Rank | Skill | Score | Type | Invoke | Description |")
        lines.append("| --- | --- | --- | --- | --- | --- |")
        for s in group:
            invoke = []
            if s.command:
                invoke.append(f"`/{s.command}`")
            if s.has_rule:
                invoke.append("rule")
            invoke_str = ", ".join(invoke) if invoke else "—"
            desc = s.description.replace("|", "\\|")
            if len(desc) > 160:
                desc = desc[:157] + "…"
            lines.append(
                f"| {s.rank_in_category} | `{s.name}` | {s.score} | "
                f"{s.type or '—'} | {invoke_str} | {desc} |"
            )
        lines.append("")

    return "\n".join(lines) + "\n"


def render_html(skills: list[Skill]) -> str:
    payload = build_index(skills)
    data_json = json.dumps(payload, ensure_ascii=False)
    # The JSON is embedded; escape the closing script sequence defensively.
    data_json = data_json.replace("</", "<\\/")
    total = len(skills)
    ncats = len([c for c in CATEGORIES if any(s.category == c for s in skills)])
    return _HTML_TEMPLATE.replace("__DATA__", data_json).replace(
        "__TOTAL__", str(total)
    ).replace("__NCATS__", str(ncats)).replace(
        "__GENERATED__", html.escape("scripts/skills_db.py")
    )


_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Work Kit — Skills Database</title>
<style>
  :root {
    --bg: #0f1115; --panel: #171a21; --panel-2: #1e2230; --line: #2a2f3d;
    --ink: #e7e9ee; --muted: #9aa3b2; --accent: #6ea8fe; --accent-2: #8b7bff;
    --good: #4ade80; --chip: #232838;
    --radius: 14px; --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif;
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: radial-gradient(1200px 600px at 80% -10%, #1a2033 0%, var(--bg) 55%); color: var(--ink); font-family: var(--font); }
  header { padding: 40px 24px 8px; max-width: 1180px; margin: 0 auto; }
  h1 { font-size: 30px; letter-spacing: -0.02em; margin: 0 0 6px; }
  .sub { color: var(--muted); font-size: 15px; }
  .toolbar { position: sticky; top: 0; z-index: 5; backdrop-filter: blur(8px);
    background: rgba(15,17,21,0.82); border-bottom: 1px solid var(--line); }
  .toolbar-inner { max-width: 1180px; margin: 0 auto; padding: 14px 24px; display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }
  .search { flex: 1 1 320px; display: flex; align-items: center; gap: 10px; background: var(--panel);
    border: 1px solid var(--line); border-radius: 12px; padding: 10px 14px; }
  .search input { flex: 1; background: transparent; border: 0; outline: 0; color: var(--ink); font-size: 15px; }
  .search svg { flex: none; opacity: 0.6; }
  select { background: var(--panel); color: var(--ink); border: 1px solid var(--line); border-radius: 10px; padding: 9px 12px; font-size: 14px; }
  .chips { max-width: 1180px; margin: 0 auto; padding: 14px 24px 0; display: flex; gap: 8px; flex-wrap: wrap; }
  .chip { cursor: pointer; user-select: none; border: 1px solid var(--line); background: var(--chip);
    color: var(--muted); padding: 7px 13px; border-radius: 999px; font-size: 13px; transition: 0.15s; }
  .chip:hover { color: var(--ink); }
  .chip.active { background: linear-gradient(135deg, var(--accent), var(--accent-2)); color: #0b0d12; border-color: transparent; font-weight: 600; }
  .count { max-width: 1180px; margin: 16px auto 0; padding: 0 24px; color: var(--muted); font-size: 13px; }
  main { max-width: 1180px; margin: 0 auto; padding: 12px 24px 60px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 16px; }
  .card { background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
    border: 1px solid var(--line); border-radius: var(--radius); padding: 18px; display: flex; flex-direction: column; gap: 10px; }
  .card-top { display: flex; align-items: baseline; justify-content: space-between; gap: 10px; }
  .name { font-size: 17px; font-weight: 650; letter-spacing: -0.01em; }
  .rank { font-size: 12px; color: var(--muted); }
  .cat { font-size: 12px; color: var(--accent); font-weight: 600; }
  .desc { color: var(--muted); font-size: 13.5px; line-height: 1.5; }
  .tags { display: flex; gap: 6px; flex-wrap: wrap; }
  .tag { font-size: 11.5px; padding: 3px 9px; border-radius: 999px; border: 1px solid var(--line); color: var(--muted); }
  .tag.cmd { color: var(--good); border-color: rgba(74,222,128,0.4); }
  .tag.rule { color: var(--accent); border-color: rgba(110,168,254,0.4); }
  .scorebar { height: 7px; background: #0c0e13; border-radius: 999px; overflow: hidden; border: 1px solid var(--line); }
  .scorefill { height: 100%; background: linear-gradient(90deg, var(--accent), var(--accent-2)); }
  .score-line { display: flex; justify-content: space-between; font-size: 12px; color: var(--muted); }
  .empty { text-align: center; color: var(--muted); padding: 60px 0; }
  footer { max-width: 1180px; margin: 0 auto; padding: 0 24px 40px; color: var(--muted); font-size: 12px; }
  code { background: #0c0e13; border: 1px solid var(--line); padding: 1px 6px; border-radius: 6px; font-size: 12px; }
</style>
</head>
<body>
<header>
  <h1>Work Kit — Skills Database</h1>
  <div class="sub"><strong>__TOTAL__</strong> skills · <strong>__NCATS__</strong> categories · search, filter, and rank built in · generated by <code>__GENERATED__</code></div>
</header>
<div class="toolbar">
  <div class="toolbar-inner">
    <label class="search">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
      <input id="q" type="search" placeholder="Find a skill… (name, description, category, tag)" autofocus />
    </label>
    <select id="sort">
      <option value="rank">Sort: Rank (score)</option>
      <option value="name">Sort: Name (A–Z)</option>
      <option value="category">Sort: Category</option>
    </select>
  </div>
  <div class="chips" id="chips"></div>
</div>
<div class="count" id="count"></div>
<main><div class="grid" id="grid"></div><div class="empty" id="empty" hidden>No skills match your search.</div></main>
<footer>Regenerate with <code>./scripts/skills-db.sh build</code>. Score rewards invocability, bundled tooling, doc depth, metadata, and catalog/README integration.</footer>
<script>
const DB = __DATA__;
const state = { q: "", cat: "All", sort: "rank" };
const grid = document.getElementById("grid");
const empty = document.getElementById("empty");
const countEl = document.getElementById("count");

function tokenize(s){ return s.toLowerCase().split(/\s+/).filter(Boolean); }
function relevance(sk, toks){
  if(!toks.length) return 0;
  let rel = 0;
  const name = sk.name.toLowerCase(), desc = (sk.description||"").toLowerCase();
  const cat = sk.category.toLowerCase(), best = (sk.best_for||[]).join(" ").toLowerCase();
  const tags = (sk.tags||[]).join(" ").toLowerCase();
  for(const t of toks){
    if(t===name) rel+=100; else if(name.includes(t)) rel+=40;
    if(desc.includes(t)) rel+=12;
    if(cat.includes(t)) rel+=8;
    if(best.includes(t)) rel+=6;
    if(tags.includes(t)) rel+=4;
  }
  return rel;
}
function esc(s){ return (s||"").replace(/[&<>"]/g, c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }

function render(){
  const toks = tokenize(state.q);
  let rows = DB.skills.map(sk => ({ sk, rel: relevance(sk, toks) }));
  if(toks.length) rows = rows.filter(r => r.rel > 0);
  if(state.cat !== "All") rows = rows.filter(r => r.sk.category === state.cat);
  rows.sort((a,b)=>{
    if(toks.length && b.rel !== a.rel) return b.rel - a.rel;
    if(state.sort === "name") return a.sk.name.localeCompare(b.sk.name);
    if(state.sort === "category"){
      if(a.sk.category !== b.sk.category) return DB.categories.indexOf(a.sk.category) - DB.categories.indexOf(b.sk.category);
      return b.sk.score - a.sk.score;
    }
    return b.sk.score - a.sk.score || a.sk.name.localeCompare(b.sk.name);
  });
  grid.innerHTML = rows.map(({sk}) => card(sk)).join("");
  empty.hidden = rows.length > 0;
  countEl.textContent = `${rows.length} of ${DB.total} skills`;
}
function card(sk){
  const badges = [];
  if(sk.command) badges.push(`<span class="tag cmd">/${esc(sk.command)}</span>`);
  if(sk.has_rule) badges.push(`<span class="tag rule">rule</span>`);
  if(sk.has_scripts) badges.push(`<span class="tag">scripts</span>`);
  if(sk.has_tests) badges.push(`<span class="tag">tests</span>`);
  (sk.tags||[]).forEach(t => badges.push(`<span class="tag">${esc(t)}</span>`));
  return `<div class="card">
    <div class="card-top"><span class="name">${esc(sk.name)}</span><span class="rank">#${sk.rank_overall}</span></div>
    <div class="cat">${esc(sk.category)}</div>
    <div class="desc">${esc(sk.description)}</div>
    <div class="tags">${badges.join("")}</div>
    <div class="score-line"><span>Score</span><span>${sk.score}/100 · rank ${sk.rank_in_category} in category</span></div>
    <div class="scorebar"><div class="scorefill" style="width:${sk.score}%"></div></div>
  </div>`;
}
function buildChips(){
  const cats = ["All", ...DB.categories];
  const box = document.getElementById("chips");
  box.innerHTML = cats.map(c => {
    const n = c === "All" ? DB.total : (DB.counts_by_category[c]||0);
    return `<span class="chip${c===state.cat?" active":""}" data-cat="${esc(c)}">${esc(c)} <span style="opacity:.6">${n}</span></span>`;
  }).join("");
  box.querySelectorAll(".chip").forEach(el => el.onclick = () => {
    state.cat = el.dataset.cat;
    box.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
    el.classList.add("active"); render();
  });
}
document.getElementById("q").addEventListener("input", e => { state.q = e.target.value; render(); });
document.getElementById("sort").addEventListener("change", e => { state.sort = e.target.value; render(); });
buildChips(); render();
</script>
</body>
</html>
"""


# --- CLI ------------------------------------------------------------------

def _fmt_find(results: list[tuple[Skill, int]], limit: int) -> str:
    if not results:
        return "No skills matched."
    out: list[str] = []
    for s, rel in results[:limit]:
        invoke = f"/{s.command}" if s.command else "(model-invoked)"
        out.append(
            f"{s.score:>3}  {s.name:<32} {s.category:<26} {invoke}"
        )
        desc = s.description
        if len(desc) > 100:
            desc = desc[:97] + "…"
        out.append(f"     {desc}")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Work Kit skills database: categorize, rank, and find skills.")
    parser.add_argument("--root", default=None, help="work-kit repo root (default: parent of scripts/)")
    sub = parser.add_subparsers(dest="cmd")

    p_find = sub.add_parser("find", help="Search skills by name/description/category/tag")
    p_find.add_argument("query", nargs="*", help="search terms")
    p_find.add_argument("--category", default=None, help="restrict to a category")
    p_find.add_argument("--limit", type=int, default=10, help="max results")

    p_list = sub.add_parser("list", help="List skills, categorized and ranked")
    p_list.add_argument("--category", default=None, help="only this category")

    sub.add_parser("stats", help="Show category counts and top skills")

    p_build = sub.add_parser("build", help="Write JSON index, SKILLS.md, and skills-database.html")
    p_build.add_argument("--json", default="catalog/skills-index.json", help="JSON index output path (repo-relative)")
    p_build.add_argument("--md", default="SKILLS.md", help="Markdown catalog output path (repo-relative)")
    p_build.add_argument("--html", default="skills-database.html", help="HTML output path (repo-relative)")

    args = parser.parse_args(argv)
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    skills = scan_skills(root)

    cmd = args.cmd or "stats"

    if cmd == "find":
        pool = skills
        if getattr(args, "category", None):
            pool = [s for s in skills if s.category.lower() == args.category.lower()]
        results = search(pool, " ".join(args.query))
        print(_fmt_find(results, args.limit))
        return 0

    if cmd == "list":
        cats = [args.category] if args.category else CATEGORIES
        for c in cats:
            group = sorted([s for s in skills if s.category == c], key=lambda s: s.rank_in_category)
            if not group:
                continue
            print(f"\n## {c}  ({len(group)})")
            for s in group:
                print(f"  {s.rank_in_category:>2}. [{s.score:>3}] {s.name}")
        return 0

    if cmd == "stats":
        print(f"{len(skills)} skills across {len(CATEGORIES)} categories\n")
        for c in CATEGORIES:
            print(f"  {sum(1 for s in skills if s.category == c):>2}  {c}")
        unc = [s for s in skills if s.category == UNCATEGORIZED]
        if unc:
            print(f"  {len(unc):>2}  {UNCATEGORIZED}: {', '.join(s.name for s in unc)}")
        print("\nTop 10 by score:")
        for s in sorted(skills, key=lambda s: s.rank_overall)[:10]:
            print(f"  #{s.rank_overall:<2} [{s.score:>3}] {s.name}  ({s.category})")
        return 0

    if cmd == "build":
        index = build_index(skills)
        json_path = root / args.json
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        (root / args.md).write_text(render_markdown(skills), encoding="utf-8")
        (root / args.html).write_text(render_html(skills), encoding="utf-8")
        print(f"Wrote {args.json}, {args.md}, {args.html} ({len(skills)} skills).")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
