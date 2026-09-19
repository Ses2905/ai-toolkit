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
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

try:
    import yaml  # optional; a minimal fallback parser is used when absent
except ImportError:  # pragma: no cover - exercised only without PyYAML
    yaml = None


# Directories (repo-relative) scanned for `*/SKILL.md`. The kit vendors its
# skills under skills/; `.agents/` is a `npx skills add` dump and is gitignored,
# so it is intentionally not scanned. Add new first-class roots here as needed.
SKILL_ROOTS: list[str] = ["skills"]


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
    # Prompt Kit themes (prompts carry a coarse `theme` in front-matter).
    "product": "Product & Discovery",
    "strategy": "Product & Discovery",
    "research": "Product & Discovery",
    "engineering": "Engineering Workflow",
}

# Explicit overrides for skills whose category is unambiguous by name.
CATEGORY_BY_NAME: dict[str, str] = {
    # Design & Frontend
    "apple-design": "Design & Frontend",
    "emil-design-eng": "Design & Frontend",
    "canvas-design": "Design & Frontend",
    "design-artifact": "Design & Frontend",
    "design-system": "Design & Frontend",
    "frontend-design": "Design & Frontend",
    "high-end-visual-design": "Design & Frontend",
    "taste-skill": "Design & Frontend",
    "web-design-guidelines": "Design & Frontend",
    "react-bits": "Design & Frontend",
    "ui-ux-pro-max": "Design & Frontend",
    "rad-spacing": "Design & Frontend",
    "huashu-design": "Design & Frontend",
    "walmart-ads-terminology": "Product & Discovery",
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
    "codex-ppt": "Presentations & Diagrams",
    "ppt-master": "Presentations & Diagrams",
    "guizang-ppt-skill": "Presentations & Diagrams",
    "gpt-taste": "Design & Frontend",
    "action-title-writing": "Presentations & Diagrams",
    "data-callout-design": "Presentations & Diagrams",
    "executive-summary-slide": "Presentations & Diagrams",
    "visual-hierarchy-cleanup": "Presentations & Diagrams",
    # Product & Discovery — Board Room Strategy pack
    "board-room-strategy": "Product & Discovery",
    "define-governing-question": "Product & Discovery",
    "audience-stakeholder-map": "Product & Discovery",
    "scqa-situation-frame": "Product & Discovery",
    "working-hypothesis-answer": "Product & Discovery",
    "storyline-skeleton-map": "Product & Discovery",
    "issue-tree-decomposition": "Product & Discovery",
    "root-cause-driver-tree": "Product & Discovery",
    "quantify-the-gap": "Product & Discovery",
    "benchmark-and-compare": "Product & Discovery",
    "synthesize-so-whats": "Product & Discovery",
    "generate-strategic-options": "Product & Discovery",
    "prioritization-matrix": "Product & Discovery",
    "scenario-stress-test": "Product & Discovery",
    "tradeoff-analysis": "Product & Discovery",
    "recommendation-statement": "Product & Discovery",
    "implementation-roadmap": "Product & Discovery",
    "resource-and-investment-plan": "Product & Discovery",
    "risk-and-mitigation-register": "Product & Discovery",
    "operating-model-and-owners": "Product & Discovery",
    "metrics-and-milestones": "Product & Discovery",
    "objection-and-qa-prep": "Product & Discovery",
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
    (
        "Engineering Workflow",
        r"debug|plan|review|ship|commit|diff|test|refactor|handoff|hand-off|"
        r"pickup|pick-up|session|workflow",
    ),
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


def present_categories(skills: list["Skill"]) -> list[str]:
    """Categories that actually occur, in canonical order with extras appended.

    Keeps the display robust when a new skill lands in an unexpected category
    (e.g. Uncategorized) so it is never silently dropped from the UI/catalog.
    """
    have = {s.category for s in skills}
    ordered = [c for c in CATEGORIES if c in have]
    extras = sorted(c for c in have if c not in CATEGORIES)
    return ordered + extras


@dataclass
class Skill:
    name: str
    source_root: str
    category: str
    type: str
    theme: str
    description: str
    argument_hint: str
    best_for: list[str]
    summary: str
    best_use: str
    watch_outs: str
    date_added: str
    date_updated: str
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
    kind: str = "skill"   # skill | prompt | workflow

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

_USE_RE = re.compile(r"\b(use (?:when|for|to|this)\b.*)", re.IGNORECASE)
# High-precision boundary cues: a skill explicitly saying where it does NOT fit
# or what it won't do. Kept strict to avoid mis-extracting descriptive prose.
_WATCH_RE = re.compile(
    r"(?<![A-Za-z])("
    r"do not use\b[^.;]*|do not apply\b[^.;]*|do not activate\b[^.;]*|"
    r"not for\b[^.;]*|not meant (?:for|to)\b[^.;]*|"
    r"does not (?:implement|apply|handle|cover|change|edit|modify|touch|support|build)\b[^.;]*|"
    r"distinct from\b[^.;]*|instead of\b[^.;]*|read-only\b[^.;]*)",
    re.IGNORECASE,
)


def _sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def derive_summary(description: str) -> str:
    """The 'what it is' — sentences before the first 'Use when/for/to' cue."""
    sents = _sentences(description)
    kept: list[str] = []
    for s in sents:
        if re.match(r"^use (when|for|to|this)\b", s, re.IGNORECASE):
            break
        kept.append(s)
    summary = " ".join(kept) if kept else (sents[0] if sents else description)
    return summary.strip()


def derive_best_use(description: str, best_for: list[str]) -> str:
    """Best use case — explicit best_for, else the skill's own 'Use when…' cue."""
    if best_for:
        return "; ".join(best_for[:3])
    m = _USE_RE.search(description)
    return m.group(1).strip() if m else ""


def derive_watch_outs(description: str) -> str:
    """When it doesn't fit — boundary/caveat clauses pulled from the skill text."""
    found: list[str] = []
    for m in _WATCH_RE.finditer(description):
        clause = m.group(1).strip().rstrip(".,;")
        clause = clause[0].upper() + clause[1:] if clause else clause
        if clause and clause not in found:
            found.append(clause)
    return "; ".join(found[:3])


def _git_dates(root: Path, skill_md: Path, skill_dir: Path) -> tuple[str, str]:
    """(date_added, date_updated) as YYYY-MM-DD from git history.

    Falls back to filesystem mtime when git history is unavailable (e.g. a
    freshly created skill that is not committed yet, or a non-git checkout).
    """
    def _mtime(p: Path) -> str:
        try:
            return datetime.fromtimestamp(p.stat().st_mtime, timezone.utc).strftime("%Y-%m-%d")
        except OSError:
            return ""

    added = updated = ""
    try:
        rel_md = skill_md.relative_to(root)
        rel_dir = skill_dir.relative_to(root)
        add_out = subprocess.run(
            ["git", "-C", str(root), "log", "--diff-filter=A", "--format=%as", "--", str(rel_md)],
            capture_output=True, text=True, timeout=15,
        )
        add_lines = [ln for ln in add_out.stdout.splitlines() if ln.strip()]
        if add_lines:
            added = add_lines[-1].strip()  # oldest add
        upd_out = subprocess.run(
            ["git", "-C", str(root), "log", "-1", "--format=%as", "--", str(rel_dir)],
            capture_output=True, text=True, timeout=15,
        )
        if upd_out.stdout.strip():
            updated = upd_out.stdout.strip().splitlines()[0].strip()
    except (subprocess.SubprocessError, OSError, ValueError):
        pass

    return added or _mtime(skill_md), updated or _mtime(skill_md)


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
    skill_names = {md.parent.name for _, md in _iter_skill_dirs(root)}
    mapping: dict[str, str] = {}
    for cmd in sorted(commands_dir.glob("*.md")):
        body = cmd.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"skills/([a-z0-9-]+)/", body)
        if m and m.group(1) in skill_names:
            mapping.setdefault(m.group(1), cmd.stem)
        elif cmd.stem in skill_names:
            mapping.setdefault(cmd.stem, cmd.stem)
    return mapping


def _iter_skill_dirs(root: Path) -> list[tuple[str, Path]]:
    """Return (source_root, skill_md_path) for every SKILL.md across roots."""
    found: list[tuple[str, Path]] = []
    for rel in SKILL_ROOTS:
        base = root / rel
        if not base.is_dir():
            continue
        for skill_md in sorted(base.glob("*/SKILL.md")):
            found.append((rel, skill_md))
    return found


def scan_skills(root: Path) -> list[Skill]:
    skill_dirs = _iter_skill_dirs(root)
    if not skill_dirs:
        raise SystemExit(f"No SKILL.md found under {', '.join(SKILL_ROOTS)} in {root}")

    command_by_skill = _command_by_skill(root)
    rules = {p.stem for p in (root / "rules").glob("*.mdc")} if (root / "rules").is_dir() else set()
    preset_keys = _preset_keys(root)
    readme_text = (root / "README.md").read_text() if (root / "README.md").is_file() else ""

    skills: list[Skill] = []
    for source_root, skill_md in skill_dirs:
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
        date_added, date_updated = _git_dates(root, skill_md, d)
        skill = Skill(
            name=name,
            source_root=source_root,
            category=categorize(name, theme, description),
            type=str(fm.get("type", "") or ""),
            theme=theme,
            description=description,
            argument_hint=str(fm.get("argument-hint", "") or ""),
            best_for=best_for,
            summary=derive_summary(description),
            best_use=derive_best_use(description, best_for),
            watch_outs=derive_watch_outs(description),
            date_added=date_added,
            date_updated=date_updated,
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


def _first_paragraph(text: str) -> str:
    for line in text.splitlines():
        s = line.strip()
        if s and not s.startswith(("#", "---", "-", "|", "```", ">")) and ":" not in s[:14]:
            return s
    return ""


def _doc_item(root: Path, path: Path, kind: str, source_root: str, command: str = "") -> Skill:
    """Build a library item (prompt/workflow) from a single markdown doc."""
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    description = str(fm.get("description", "") or "").strip() or _first_paragraph(text)
    theme = str(fm.get("theme", "") or "")
    name = path.stem
    added, updated = _git_dates(root, path, path)
    item = Skill(
        name=name, source_root=source_root, category=categorize(name, theme, description),
        type=str(fm.get("type", "") or kind), theme=theme, description=description,
        argument_hint=str(fm.get("argument-hint", "") or ""), best_for=[],
        summary=derive_summary(description), best_use=derive_best_use(description, []),
        watch_outs=derive_watch_outs(description), date_added=added, date_updated=updated,
        command=command, has_command=bool(command), has_rule=False, has_scripts=False,
        has_tests=False, has_examples=False, has_docs=False, file_count=1,
        skill_md_bytes=path.stat().st_size, in_catalog=False, in_readme=False, kind=kind,
    )
    item.score, item.score_breakdown = score_skill(item)
    return item


def scan_prompts(root: Path) -> list[Skill]:
    base = root / "prompts" / "commands"
    if not base.is_dir():
        return []
    return [_doc_item(root, p, "prompt", "prompts/commands", command=p.stem)
            for p in sorted(base.glob("*.md"))]


def scan_workflows(root: Path) -> list[Skill]:
    base = root / "workflows"
    if not base.is_dir():
        return []
    items: list[Skill] = []
    for p in sorted(base.rglob("*.md")):
        if p.name.upper() == "README.MD":
            continue
        items.append(_doc_item(root, p, "workflow", "workflows"))
    return items


def scan_library(root: Path) -> list[Skill]:
    """All library items — skills + prompts + workflows — ranked together."""
    items = scan_skills(root) + scan_prompts(root) + scan_workflows(root)
    _assign_ranks(items)
    return items


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
    cats = present_categories(skills)
    skills_out: list[dict] = []
    for s in sorted(skills, key=lambda s: s.rank_overall):
        d = asdict(s)
        d["tags"] = s.tags  # computed property; asdict() omits it
        skills_out.append(d)
    kinds = ["skill", "prompt", "workflow"]
    return {
        "generated_by": "scripts/skills_db.py",
        "categories": cats,
        "kinds": [k for k in kinds if any(s.kind == k for s in skills)],
        "score_weights": SCORE_WEIGHTS,
        "score_max_raw": MAX_RAW,
        "total": len(skills),
        "counts_by_category": {
            c: sum(1 for s in skills if s.category == c) for c in cats
        },
        "counts_by_kind": {
            k: sum(1 for s in skills if s.kind == k) for k in kinds
            if any(s.kind == k for s in skills)
        },
        "skills": skills_out,
    }


def render_markdown(skills: list[Skill]) -> str:
    cats = present_categories(skills)
    lines: list[str] = []
    lines.append("# Work Kit Skills Database")
    lines.append("")
    lines.append(
        "Auto-generated by `scripts/skills_db.py build`. Do not edit by hand — "
        "run the builder to refresh, or use the live app "
        "(`./scripts/skills-db.sh serve`) and its Refresh button. Search from the "
        "terminal with `./scripts/skills-db.sh find <query>`."
    )
    lines.append("")
    lines.append(f"**{len(skills)} skills** across **{len(cats)} categories**. "
                 "Score (0-100) rewards invocability (command/rule), bundled tooling "
                 "(scripts/tests/examples/docs), doc depth, metadata completeness, and "
                 "catalog/README integration.")
    lines.append("")

    lines.append("## Categories")
    lines.append("")
    lines.append("| Category | Skills | Blurb |")
    lines.append("| --- | --- | --- |")
    for c in cats:
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

    for c in cats:
        group = sorted(
            [s for s in skills if s.category == c], key=lambda s: s.rank_in_category
        )
        if not group:
            continue
        lines.append(f"## {c}")
        lines.append("")
        lines.append(f"_{CATEGORY_BLURB.get(c, '')}_")
        lines.append("")
        lines.append("| Rank | Skill | Score | Type | Invoke | Added | Updated | What it is |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
        for s in group:
            invoke = []
            if s.command:
                invoke.append(f"`/{s.command}`")
            if s.has_rule:
                invoke.append("rule")
            invoke_str = ", ".join(invoke) if invoke else "—"
            summary = (s.summary or s.description).replace("|", "\\|")
            if len(summary) > 150:
                summary = summary[:147] + "…"
            lines.append(
                f"| {s.rank_in_category} | `{s.name}` | {s.score} | "
                f"{s.type or '—'} | {invoke_str} | {s.date_added or '—'} | "
                f"{s.date_updated or '—'} | {summary} |"
            )
        lines.append("")

    return "\n".join(lines) + "\n"


def render_html(skills: list[Skill]) -> str:
    payload = build_index(skills)
    data_json = json.dumps(payload, ensure_ascii=False)
    # The JSON is embedded; escape the closing script sequence defensively.
    data_json = data_json.replace("</", "<\\/")
    total = len(skills)
    ncats = len(present_categories(skills))
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
<title>Skills Field Guide</title>
<style>
  /* Design tokens — a "field guide / catalog" register: cool paper, pine accent,
     serif display + humanist UI sans. Deliberately avoids the cream+serif and
     near-black+neon AI-default looks; one accent, structure carries meaning. */
  /* Verdant brand faces — open-licensed (OFL), committed under
     design-system/fonts and served at /fonts/*. Space Grotesk + Plus Jakarta Sans. */
  @font-face { font-family:"Space Grotesk"; src:url("fonts/SpaceGrotesk-400.woff2") format("woff2"); font-weight:400; font-display:swap; }
  @font-face { font-family:"Space Grotesk"; src:url("fonts/SpaceGrotesk-500.woff2") format("woff2"); font-weight:500; font-display:swap; }
  @font-face { font-family:"Space Grotesk"; src:url("fonts/SpaceGrotesk-700.woff2") format("woff2"); font-weight:700; font-display:swap; }
  @font-face { font-family:"Plus Jakarta Sans"; src:url("fonts/PlusJakartaSans-400.woff2") format("woff2"); font-weight:400; font-display:swap; }
  @font-face { font-family:"Plus Jakarta Sans"; src:url("fonts/PlusJakartaSans-500.woff2") format("woff2"); font-weight:500; font-display:swap; }
  @font-face { font-family:"Plus Jakarta Sans"; src:url("fonts/PlusJakartaSans-600.woff2") format("woff2"); font-weight:600; font-display:swap; }
  @font-face { font-family:"Plus Jakarta Sans"; src:url("fonts/PlusJakartaSans-700.woff2") format("woff2"); font-weight:700; font-display:swap; }

  /* Semantic tokens. One palette, baked in — no theme switcher. Teal/emerald on
     botanical paper, Space Grotesk display + Plus Jakarta Sans UI (OFL fonts).
     --pine* alias --accent* so the many component rules stay palette-agnostic. */
  :root {
    color-scheme: light;
    --paper: #f4faf8; --surface: #ffffff; --surface-2: #ecfbf4;
    --ink: #083344; --muted: #3f6b6b; --faint: #7fa3a3;
    --line: #d7ebe6; --line-strong: #bfe0d8;
    --accent: #0e7490; --accent-ink: #06323d; --accent-wash: #d7eef0; --on-accent: #ffffff;
    --pine: var(--accent); --pine-ink: var(--accent-ink); --pine-wash: var(--accent-wash);
    --shadow: 0 1px 2px rgba(8,51,68,.05), 0 10px 30px rgba(8,51,68,.08);
    --display: "Space Grotesk", "Archivo", ui-sans-serif, system-ui, sans-serif;
    --ui: "Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
    --ease: cubic-bezier(.32,.72,0,1);
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body { margin: 0; background: var(--paper); color: var(--ink); font-family: var(--ui);
    font-size: 14px; line-height: 1.5; -webkit-font-smoothing: antialiased; }
  :focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 6px; }
  button, select, input, .th-sort, .disclosure { touch-action: manipulation; }
  code { font-size: .85em; background: var(--surface); border: 1px solid var(--line); padding: 1px 6px; border-radius: 6px; }
  .wrap { max-width: 1180px; margin: 0 auto; padding: 0 28px; }

  .topnav { border-bottom: 1px solid var(--line); background: var(--surface); }
  .topnav .wrap { display: flex; align-items: center; gap: 18px; padding-top: 14px; padding-bottom: 14px; }
  .topnav .brand { display: inline-flex; align-items: center; gap: 10px; font-family: var(--display); font-weight: 700; font-size: 17px; color: var(--ink); letter-spacing: -0.01em; }
  .topnav .brand .logo { width: 26px; height: 26px; border-radius: 8px; background: linear-gradient(135deg, var(--accent), #34d399); flex: none; }
  .topnav .links { display: flex; gap: 4px; margin-left: auto; align-items: center; }
  .topnav .links a { color: var(--muted); font-weight: 600; padding: 7px 11px; border-radius: 8px; text-decoration: none; }
  .topnav .links a:hover { color: var(--ink); background: var(--surface-2); }
  .topnav .links a.active { color: var(--accent-ink); background: var(--accent-wash); }

  header { padding: 40px 0 18px; }
  h1 { font-family: var(--display); font-weight: 600; font-size: 40px; line-height: 1.05; letter-spacing: -0.015em; margin: 0 0 12px; text-wrap: balance; }
  .lede { color: var(--muted); font-size: 16px; max-width: 66ch; margin: 0; text-wrap: pretty; }
  .counts { margin-top: 16px; display: flex; gap: 22px; flex-wrap: wrap; color: var(--faint); font-size: 13px; }
  .counts b { color: var(--ink); font-weight: 600; }

  .toolbar { position: sticky; top: 0; z-index: 20; background: color-mix(in srgb, var(--paper) 90%, transparent);
    backdrop-filter: blur(10px); border-bottom: 1px solid var(--line); }
  .toolbar .wrap { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; padding-top: 13px; padding-bottom: 13px; }
  .field { display: flex; align-items: center; gap: 9px; background: var(--surface);
    border: 1px solid var(--line-strong); border-radius: 10px; padding: 9px 12px; }
  .field svg { flex: none; color: var(--faint); }
  .field.search { flex: 1 1 300px; }
  .field input { flex: 1; border: 0; outline: 0; background: transparent; color: var(--ink); font: inherit; }
  .field.sel { padding: 0; }
  select { font: inherit; color: var(--ink); background: var(--surface); border: 0; border-radius: 10px; padding: 10px 12px; cursor: pointer; outline: 0; }
  .btn { font: inherit; font-weight: 600; cursor: pointer; border-radius: 10px; padding: 9px 15px; border: 1px solid var(--accent-ink);
    background: var(--accent); color: var(--on-accent); display: inline-flex; align-items: center; gap: 8px; transition: background .2s var(--ease); }
  .btn:hover { background: var(--pine-ink); }
  .btn:disabled { opacity: .55; cursor: default; }
  .btn svg { transition: transform .5s var(--ease); }
  .btn.spin svg { transform: rotate(360deg); }
  .updated { color: var(--faint); font-size: 12.5px; }
  .admin { position: relative; margin-left: auto; }
  .admin > summary { list-style: none; cursor: pointer; display: inline-flex; align-items: center; gap: 7px;
    font: inherit; font-weight: 600; color: var(--muted); background: var(--surface);
    border: 1px solid var(--line-strong); border-radius: 10px; padding: 9px 13px; }
  .admin > summary::-webkit-details-marker { display: none; }
  .admin > summary:hover { color: var(--ink); }
  .admin[open] > summary { color: var(--ink); border-color: var(--accent); }
  .admin-panel { position: absolute; right: 0; top: calc(100% + 8px); z-index: 30; width: 260px;
    background: var(--surface); border: 1px solid var(--line-strong); border-radius: 12px;
    box-shadow: var(--shadow); padding: 14px; }
  .admin-title { margin: 0 0 10px; font-size: 11px; letter-spacing: .08em; text-transform: uppercase; color: var(--faint); font-weight: 600; }
  .admin-row { display: flex; align-items: center; justify-content: space-between; gap: 10px; font-size: 13px; font-weight: 600; color: var(--muted); }
  .admin-row select { font: inherit; color: var(--ink); background: var(--surface); border: 1px solid var(--line-strong); border-radius: 8px; padding: 7px 10px; }
  .admin-note { margin: 12px 0 0; font-size: 12px; line-height: 1.5; color: var(--faint); }

  .board { padding: 22px 0 40px; }
  .tablewrap { overflow-x: auto; border: 1px solid var(--line); border-radius: 14px; background: var(--surface); box-shadow: var(--shadow); }
  table { width: 100%; border-collapse: collapse; min-width: 720px; }
  thead th { position: sticky; top: 0; z-index: 2; background: var(--surface-2); text-align: left; font-weight: 600; font-size: 12px;
    color: var(--muted); padding: 12px 14px; border-bottom: 1px solid var(--line-strong); white-space: nowrap; }
  .th-sort { font: inherit; font-weight: 600; color: var(--muted); background: none; border: 0; padding: 0;
    cursor: pointer; display: inline-flex; align-items: center; gap: 6px; }
  .th-sort:hover { color: var(--ink); }
  th[aria-sort="ascending"] .th-sort, th[aria-sort="descending"] .th-sort { color: var(--ink); }
  th .arrow { color: var(--accent); font-size: 11px; }
  tbody td { padding: 13px 14px; border-bottom: 1px solid var(--line); vertical-align: top; }
  tbody tr.row:hover td { background: var(--surface-2); }
  .disclosure { font: inherit; text-align: left; background: none; border: 0; padding: 0; cursor: pointer;
    display: flex; align-items: center; gap: 8px; color: var(--ink); }
  .skill-name { font-weight: 600; font-size: 14.5px; }
  .chev { color: var(--faint); transition: transform .18s var(--ease); font-size: 10px; }
  tr.row.open .chev { transform: rotate(90deg); }
  .skill-sum { color: var(--muted); font-size: 12.5px; margin-top: 3px; max-width: 60ch;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
  .catcell { display: inline-flex; align-items: center; gap: 7px; white-space: nowrap; font-size: 13px; }
  .dot { width: 9px; height: 9px; border-radius: 3px; flex: none; }
  .type-pill { font-size: 13px; color: var(--muted); text-transform: capitalize; }
  .kind-pill { margin-left: 8px; font-size: 10.5px; font-weight: 700; letter-spacing: .04em; text-transform: uppercase;
    padding: 1px 7px; border-radius: 999px; border: 1px solid var(--line-strong); color: var(--muted); vertical-align: middle; }
  .kind-pill.k-prompt { color: var(--accent-ink); border-color: var(--accent); background: var(--accent-wash); }
  .kind-pill.k-workflow { color: #7a4e07; border-color: #e6b566; background: #fdecc8; }
  .prose { color: var(--muted); font-size: 12.5px; max-width: 32ch;
    display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
  .prose.none { color: var(--faint); }
  .cmd { color: var(--pine-ink); font-weight: 600; }
  .model { color: var(--faint); }
  .score { display: flex; align-items: center; gap: 9px; white-space: nowrap; }
  .bar { width: 60px; height: 6px; border-radius: 999px; background: var(--line); overflow: hidden; }
  .bar > span { display: block; height: 100%; background: var(--pine); }
  .num { font-variant-numeric: tabular-nums; color: var(--ink); font-size: 13px; min-width: 24px; }
  .date { font-variant-numeric: tabular-nums; color: var(--muted); white-space: nowrap; font-size: 12.5px; }

  tr.detail td { background: var(--surface-2); border-bottom: 1px solid var(--line-strong); padding: 0; }
  tr.detail .inner { padding: 6px 18px 20px 42px; display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 14px 30px; }
  .fb h4 { margin: 12px 0 5px; font-size: 11px; letter-spacing: .03em; color: var(--faint); font-weight: 600; }
  .fb p { margin: 0; color: var(--ink); font-size: 13px; line-height: 1.55; }
  .badges { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 5px; }
  .badge { font-size: 11.5px; padding: 2px 9px; border-radius: 999px; border: 1px solid var(--line-strong); color: var(--muted); background: var(--surface); }
  .badge.on { color: var(--pine-ink); border-color: var(--pine); background: var(--pine-wash); }

  .empty { text-align: center; color: var(--faint); padding: 70px 0; }
  footer { color: var(--faint); font-size: 12.5px; padding: 14px 0 60px; }
  @media (prefers-reduced-motion: reduce) { *, html { transition: none !important; scroll-behavior: auto !important; } }
</style>
</head>
<body>
<nav class="topnav"><div class="wrap">
  <a class="brand" href="./" aria-label="Library home"><span class="logo" aria-hidden="true"></span>Library</a>
  <div class="links">
    <a href="./" class="active">Library</a>
    <a href="design-system/">Design system</a>
    <a href="https://github.com/Ses2905/cursor-skills" rel="noopener">GitHub</a>
  </div>
</div></nav>

<header><div class="wrap">
  <h1>Your AI Library</h1>
  <p class="lede">Every capability in the kit — <strong>skills</strong>, <strong>prompts</strong>, and <strong>workflows</strong> — with what each does, where it fits, and how it's invoked. Search, filter, and sort any column, or open a row for the full brief.</p>
  <div class="counts"><span><b id="c-total">0</b> items</span><span id="c-kinds"></span><span><b id="c-cats">0</b> categories</span><span>generated by <code>__GENERATED__</code></span></div>
</div></header>

<div class="toolbar"><div class="wrap">
  <label class="field search">
    <svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
    <input id="q" name="q" type="search" aria-label="Search the library" placeholder="Search the library — name, what it does, best use…" autocomplete="off" spellcheck="false" autofocus />
  </label>
  <div class="field sel"><select id="fkind" aria-label="Filter by kind"></select></div>
  <div class="field sel"><select id="fcat" aria-label="Filter by category"></select></div>
  <div class="field sel"><select id="ftype" aria-label="Filter by type"></select></div>
  <button id="refresh" class="btn" hidden><svg aria-hidden="true" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12a9 9 0 1 1-2.6-6.4"/><path d="M21 3v6h-6"/></svg><span class="lbl">Refresh</span></button>
  <span id="updated" class="updated" role="status" aria-live="polite"></span>
  <details class="admin" id="admin">
    <summary aria-label="About this library"><svg aria-hidden="true" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg><span>About</span></summary>
    <div class="admin-panel">
      <p class="admin-title">About this library</p>
      <p class="admin-note">A living catalog of every <strong>skill</strong>, <strong>prompt</strong>, and <strong>workflow</strong> in the kit. Search or filter to find one, then open a row for the full brief — what it does, when to use it, and how to invoke it.</p>
      <p class="admin-note" id="about-counts"></p>
      <p class="admin-note">Add new items with the <code>/add-to-library</code> command; the catalog re-indexes and ranks them automatically.</p>
    </div>
  </details>
</div></div>

<main class="board"><div class="wrap">
  <div class="tablewrap">
    <table>
      <thead><tr>
        <th aria-sort="none"><button type="button" class="th-sort" data-sort="name">Skill <span class="arrow" aria-hidden="true"></span></button></th>
        <th aria-sort="none"><button type="button" class="th-sort" data-sort="category">Category <span class="arrow" aria-hidden="true"></span></button></th>
        <th aria-sort="none"><button type="button" class="th-sort" data-sort="type">Type <span class="arrow" aria-hidden="true"></span></button></th>
        <th>Invoke</th>
        <th aria-sort="none"><button type="button" class="th-sort" data-sort="score">Score <span class="arrow" aria-hidden="true"></span></button></th>
        <th aria-sort="none"><button type="button" class="th-sort" data-sort="date_updated">Updated <span class="arrow" aria-hidden="true"></span></button></th>
      </tr></thead>
      <tbody id="tbody"></tbody>
    </table>
  </div>
  <div class="empty" id="empty" hidden>No skills match your filters.</div>
  <footer id="foot"></footer>
</div></main>

<script>
let DB = __DATA__;
const LIVE = location.protocol !== "file:";
const CAT_COLORS = ["#0f766e","#7c3aed","#c2410c","#2563eb","#5f7a33","#a1348a","#0e7490","#9a6b00"];
const state = { q:"", kind:"All", cat:"All", type:"All", sort:"name", dir:1 };
const $ = id => document.getElementById(id);
function esc(s){ return (s||"").replace(/[&<>"]/g, c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }
function catColor(cat){ const i = DB.categories.indexOf(cat); return CAT_COLORS[(i<0?DB.categories.length:i)%CAT_COLORS.length]; }
function tokenize(s){ return s.toLowerCase().split(/\s+/).filter(Boolean); }
function relevance(sk, toks){
  if(!toks.length) return 0; let r = 0;
  const hay = [sk.name, sk.summary, sk.description, sk.best_use, sk.category, (sk.tags||[]).join(" ")].join(" \u0001 ").toLowerCase();
  const name = sk.name.toLowerCase();
  for(const t of toks){ if(t===name) r+=100; else if(name.includes(t)) r+=40; if(hay.includes(t)) r+=8; }
  return r;
}
function types(){ return Array.from(new Set(DB.skills.map(s=>s.type).filter(Boolean))).sort(); }
function kinds(){ return (DB.kinds && DB.kinds.length) ? DB.kinds : ["skill"]; }
function fillFilters(){
  const kd = $("fkind");
  kd.innerHTML = ['<option value="All">All kinds</option>']
    .concat(kinds().map(k=>`<option value="${esc(k)}">${esc(k)}s (${(DB.counts_by_kind||{})[k]||0})</option>`)).join("");
  kd.value = kinds().includes(state.kind) ? state.kind : "All";
  const cat = $("fcat");
  cat.innerHTML = ['<option value="All">All categories</option>']
    .concat(DB.categories.map(c=>`<option value="${esc(c)}">${esc(c)} (${DB.counts_by_category[c]||0})</option>`)).join("");
  cat.value = DB.categories.includes(state.cat) ? state.cat : "All";
  const ty = $("ftype");
  ty.innerHTML = ['<option value="All">All types</option>']
    .concat(types().map(t=>`<option value="${esc(t)}">${esc(t)}</option>`)).join("");
  ty.value = types().includes(state.type) ? state.type : "All";
}
function sortVal(sk){
  switch(state.sort){
    case "name": return sk.name.toLowerCase();
    case "category": return String(DB.categories.indexOf(sk.category)).padStart(3,"0") + sk.name;
    case "type": return (sk.type||"~") + sk.name;
    case "date_added": return sk.date_added || "";
    case "date_updated": return sk.date_updated || "";
    default: return sk.score;
  }
}
function apply(){
  const toks = tokenize(state.q);
  let rows = DB.skills.map(sk=>({sk, rel:relevance(sk,toks)}));
  if(toks.length) rows = rows.filter(r=>r.rel>0);
  if(state.kind!=="All") rows = rows.filter(r=>(r.sk.kind||"skill")===state.kind);
  if(state.cat!=="All") rows = rows.filter(r=>r.sk.category===state.cat);
  if(state.type!=="All") rows = rows.filter(r=>r.sk.type===state.type);
  rows.sort((a,b)=>{
    if(toks.length && b.rel!==a.rel) return b.rel-a.rel;
    const va=sortVal(a.sk), vb=sortVal(b.sk);
    let c = va<vb?-1:va>vb?1:0;
    if(c===0) c = b.sk.score-a.sk.score;
    return c*state.dir;
  });
  return rows.map(r=>r.sk);
}
function invokeCell(sk){ return sk.command ? `<span class="cmd">/${esc(sk.command)}</span>` : `<span class="model">model-invoked</span>`; }
function proseCell(t){ return t ? `<div class="prose">${esc(t)}</div>` : `<div class="prose none">—</div>`; }
function rowHTML(sk, idx){
  const color = catColor(sk.category);
  const main = `<tr class="row" data-idx="${idx}">
    <td><button type="button" class="disclosure" aria-expanded="false" aria-controls="d-${idx}"><span class="chev" aria-hidden="true">▶</span><span class="skill-name">${esc(sk.name)}</span><span class="kind-pill k-${esc(sk.kind||'skill')}">${esc(sk.kind||'skill')}</span></button><div class="skill-sum">${esc(sk.summary)}</div></td>
    <td><span class="catcell"><span class="dot" style="background:${color}"></span>${esc(sk.category)}</span></td>
    <td><span class="type-pill">${esc(sk.type||"—")}</span></td>
    <td>${invokeCell(sk)}</td>
    <td><div class="score"><span class="bar"><span style="width:${sk.score}%"></span></span><span class="num">${sk.score}</span></div></td>
    <td class="date">${esc(sk.date_updated||"—")}</td>
  </tr>`;
  const badges = [];
  badges.push(`<span class="badge${sk.command?" on":""}">${sk.command?"/"+esc(sk.command):"no command"}</span>`);
  badges.push(`<span class="badge${sk.has_rule?" on":""}">rule</span>`);
  ["scripts","tests","examples","docs"].forEach(k=>{ if(sk["has_"+k]) badges.push(`<span class="badge on">${k}</span>`); });
  if(sk.theme) badges.push(`<span class="badge">${esc(sk.theme)}</span>`);
  const detail = `<tr class="detail" id="d-${idx}" data-for="${idx}" hidden><td colspan="6"><div class="inner">
    <div class="fb" style="grid-column:1/-1"><h4>WHAT IT IS</h4><p>${esc(sk.description)}</p></div>
    <div class="fb"><h4>BEST USED FOR</h4><p>${sk.best_use?esc(sk.best_use):"—"}</p></div>
    <div class="fb"><h4>WATCH-OUTS</h4><p>${sk.watch_outs?esc(sk.watch_outs):"No limits stated in the skill — check its SKILL.md."}</p></div>
    <div class="fb"><h4>RANK</h4><p>#${sk.rank_overall} overall · #${sk.rank_in_category} in ${esc(sk.category)} · ${sk.score}/100</p></div>
    <div class="fb"><h4>ADDED / UPDATED</h4><p>${esc(sk.date_added||"—")} → ${esc(sk.date_updated||"—")}</p></div>
    <div class="fb"><h4>INVOKE</h4><p>${sk.command?"/"+esc(sk.command):"model-invoked"}${sk.argument_hint?" · "+esc(sk.argument_hint):""}</p></div>
    <div class="fb" style="grid-column:1/-1"><h4>SIGNALS</h4><div class="badges">${badges.join("")}</div></div>
  </div></td></tr>`;
  return main + detail;
}
function render(){
  const rows = apply();
  $("tbody").innerHTML = rows.map((sk,i)=>rowHTML(sk,i)).join("");
  $("empty").hidden = rows.length>0;
  $("foot").textContent = `Showing ${rows.length} of ${DB.total} items. Score (0–100) rewards invocability, bundled tooling, doc depth, metadata, and catalog/README integration.`;
  document.querySelectorAll("thead th").forEach(th=>{
    const btn = th.querySelector(".th-sort"); if(!btn) return;
    const active = btn.dataset.sort===state.sort;
    th.setAttribute("aria-sort", active ? (state.dir<0?"descending":"ascending") : "none");
    btn.querySelector(".arrow").textContent = active ? (state.dir<0?"▼":"▲") : "";
  });
  syncURL();
}
function toggleRow(tr){
  if(!tr) return;
  const d = document.getElementById("d-"+tr.dataset.idx);
  const open = d.hasAttribute("hidden");
  if(open){ d.removeAttribute("hidden"); tr.classList.add("open"); }
  else { d.setAttribute("hidden",""); tr.classList.remove("open"); }
  const btn = tr.querySelector(".disclosure");
  if(btn) btn.setAttribute("aria-expanded", String(open));
}
function setSort(key){
  if(state.sort===key) state.dir *= -1;
  else { state.sort = key; state.dir = (key==="name"||key==="category"||key==="type") ? 1 : -1; }
  render();
}
function stamp(label){ $("updated").textContent = `${label} ${new Date().toLocaleTimeString()} · ${DB.total} skills`; }
function counts(){
  $("c-total").textContent = DB.total;
  $("c-cats").textContent = DB.categories.length;
  const ck = DB.counts_by_kind || {};
  $("c-kinds").textContent = kinds().map(k=>`${ck[k]||0} ${k}s`).join(" · ");
  const about = $("about-counts");
  if(about) about.textContent = `${DB.total} items across ${DB.categories.length} categories — ` + kinds().map(k=>`${ck[k]||0} ${k}s`).join(", ") + ".";
}
async function fetchData(path){
  const r = await fetch(path, { method: path.indexOf("refresh")>=0?"POST":"GET", cache:"no-store" });
  if(!r.ok) throw new Error("HTTP "+r.status); return await r.json();
}
async function refresh(){
  const btn = $("refresh"); btn.disabled = true; btn.classList.add("spin");
  const lbl = btn.querySelector(".lbl"); lbl.textContent = "Refreshing…";
  try { DB = await fetchData("/api/refresh"); if(!DB.categories.includes(state.cat)) state.cat="All"; fillFilters(); counts(); render(); stamp("Refreshed"); }
  catch(e){ stamp("Refresh failed —"); }
  finally { btn.disabled = false; btn.classList.remove("spin"); lbl.textContent = "Refresh"; }
}
$("q").addEventListener("input", e=>{ state.q=e.target.value; render(); });
$("fkind").addEventListener("change", e=>{ state.kind=e.target.value; render(); });
$("fcat").addEventListener("change", e=>{ state.cat=e.target.value; render(); });
$("ftype").addEventListener("change", e=>{ state.type=e.target.value; render(); });
document.querySelector("thead").addEventListener("click", e=>{
  const btn = e.target.closest(".th-sort"); if(btn) setSort(btn.dataset.sort);
});
$("tbody").addEventListener("click", e=> toggleRow(e.target.closest("tr.row")));

function syncURL(){
  const p = new URLSearchParams();
  if(state.q) p.set("q", state.q);
  if(state.kind!=="All") p.set("kind", state.kind);
  if(state.cat!=="All") p.set("cat", state.cat);
  if(state.type!=="All") p.set("type", state.type);
  if(state.sort!=="name" || state.dir!==1){ p.set("sort", state.sort); p.set("dir", state.dir<0?"desc":"asc"); }
  const qs = p.toString();
  history.replaceState(null, "", qs ? "?"+qs : location.pathname);
}
function readURL(){
  const p = new URLSearchParams(location.search);
  if(p.has("q")) state.q = p.get("q");
  if(p.has("kind")) state.kind = p.get("kind");
  if(p.has("cat")) state.cat = p.get("cat");
  if(p.has("type")) state.type = p.get("type");
  if(p.has("sort")){ state.sort = p.get("sort"); state.dir = p.get("dir")==="asc" ? 1 : -1; }
}
// Refresh only makes sense against a live backend (the serve command). On a
// static host (GitHub Pages, file://) there is no /api, so probe it first and
// only reveal Refresh when the backend actually answers — otherwise the button
// would always fail. The embedded snapshot renders regardless.
async function enableLiveIfAvailable(){
  if(!LIVE) return false;
  try {
    const data = await fetchData("/api/skills");
    DB = data;
    const b = $("refresh");
    b.hidden = false;
    b.addEventListener("click", refresh);
    return true;
  } catch(e) { return false; }
}
async function init(){
  readURL();
  const live = await enableLiveIfAvailable();
  fillFilters();
  $("q").value = state.q;
  counts(); render(); stamp(live ? "Loaded" : "Snapshot");
}
init();
</script>
</body>
</html>
"""


# --- Live server ----------------------------------------------------------

class _DBHandler(BaseHTTPRequestHandler):
    """Serves the interactive page plus a live/rescanning JSON API.

    ``root`` and ``build_paths`` are bound per-server via functools.partial.
    """

    root: Path = Path(".")
    build_paths: dict[str, str] = {}

    def log_message(self, *args) -> None:  # quiet by default
        pass

    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _json(self, payload: dict) -> None:
        self._send(200, json.dumps(payload).encode("utf-8"), "application/json; charset=utf-8")

    _FONT_TYPES = {".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf", ".otf": "font/otf"}

    def _rescan(self) -> list[Skill]:
        return scan_library(self.root)

    def _serve_font(self, name: str) -> None:
        """Serve a licensed brand font from design-system/fonts (if present).

        Returns 404 when the file is absent (unlicensed setups) so the CSS
        fallback stacks take over. Only bare filenames are allowed.
        """
        ext = Path(name).suffix.lower()
        if "/" in name or ".." in name or ext not in self._FONT_TYPES:
            self._send(404, b"Not found", "text/plain; charset=utf-8")
            return
        font_path = self.root / "design-system" / "fonts" / name
        if not font_path.is_file():
            self._send(404, b"font not installed", "text/plain; charset=utf-8")
            return
        self._send(200, font_path.read_bytes(), self._FONT_TYPES[ext])

    def _handle(self) -> None:
        path = self.path.split("?", 1)[0].rstrip("/") or "/"
        if path == "/":
            html_doc = render_html(self._rescan())
            self._send(200, html_doc.encode("utf-8"), "text/html; charset=utf-8")
        elif path.startswith("/fonts/"):
            self._serve_font(path[len("/fonts/"):])
        elif path == "/api/skills":
            self._json(build_index(self._rescan()))
        elif path == "/api/refresh":
            # Rescan AND rewrite the committed artifacts so disk stays current.
            skills = self._rescan()
            _write_artifacts(self.root, skills, self.build_paths)
            payload = build_index(skills)
            payload["refreshed"] = True
            self._json(payload)
        else:
            self._send(404, b"Not found", "text/plain; charset=utf-8")

    def do_GET(self) -> None:
        self._handle()

    def do_HEAD(self) -> None:
        self._handle()

    def do_POST(self) -> None:
        self._handle()


def serve(root: Path, host: str, port: int, build_paths: dict[str, str]) -> None:
    class Bound(_DBHandler):
        pass

    Bound.root = root
    Bound.build_paths = build_paths
    httpd = ThreadingHTTPServer((host, port), Bound)
    actual = httpd.server_address[1]
    print(f"Skills database live at http://{host or 'localhost'}:{actual}/")
    print("  GET  /               interactive page (rescans on load)")
    print("  GET  /api/skills     live JSON index")
    print("  POST /api/refresh    rescan + rewrite SKILLS.md/html/json, return index")
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        httpd.server_close()


# --- CLI ------------------------------------------------------------------

def _write_artifacts(root: Path, skills: list[Skill], paths: dict[str, str]) -> None:
    json_path = root / paths.get("json", "catalog/skills-index.json")
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(build_index(skills), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (root / paths.get("md", "SKILLS.md")).write_text(render_markdown(skills), encoding="utf-8")
    (root / paths.get("html", "skills-database.html")).write_text(render_html(skills), encoding="utf-8")


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

    p_serve = sub.add_parser("serve", help="Run the interactive skills database app with a live Refresh")
    p_serve.add_argument("--host", default="127.0.0.1", help="bind host (default 127.0.0.1)")
    p_serve.add_argument("--port", type=int, default=8765, help="bind port (default 8765; 0 = pick a free port)")

    args = parser.parse_args(argv)
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    skills = scan_library(root)

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
        paths = {"json": args.json, "md": args.md, "html": args.html}
        _write_artifacts(root, skills, paths)
        print(f"Wrote {args.json}, {args.md}, {args.html} ({len(skills)} skills).")
        return 0

    if cmd == "serve":
        serve(root, args.host, args.port, {})
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
