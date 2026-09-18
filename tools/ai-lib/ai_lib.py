#!/usr/bin/env python3
"""ai-lib — a package manager + librarian for an AI capability library.

Inspects an incoming source (local dir/file, .zip, or GitHub URL), classifies
each artifact (skill / prompt / workflow / reference / template / asset /
global instruction / tool), proposes a routing plan, and installs it into a
canonical global library ($AI_LIBRARY_HOME) with a machine-readable registry,
provenance, and duplicate detection.

Pure standard library (optional PyYAML fast-path for manifests/front-matter).
V1 scope: inspect, install (with --dry-run + approval), list, search, info,
remove, doctor. Agent adapters / upstream updates / promotion are V2.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml  # optional
except ImportError:  # pragma: no cover
    yaml = None


# --- Library shape --------------------------------------------------------

DEFAULT_HOME = Path(os.environ.get("AI_LIBRARY_HOME", str(Path.home() / ".ai-library")))

# artifact type -> library subdirectory
TYPE_DIR = {
    "skill": "skills",
    "prompt": "prompts",
    "workflow": "workflows",
    "reference": "references",
    "template": "templates",
    "asset": "assets",
    "global": "global",
    "tool": "tools",
    "integration": "integrations",
}
LIBRARY_DIRS = list(dict.fromkeys(TYPE_DIR.values())) + ["registry", "config", "inbox"]

# Preferred domain taxonomy — do not invent new categories casually.
CATEGORIES = [
    "presentation", "design", "visual-storytelling", "data-visualization",
    "research", "strategy", "product", "frontend", "development", "writing",
    "content", "ux", "accessibility", "automation", "agent-tools",
    "documentation", "productivity",
]
CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "presentation": ["slide", "deck", "presentation", "keynote", "ppt", "pitch"],
    "data-visualization": ["chart", "graph", "kpi", "visualization", "dashboard", "plot"],
    "visual-storytelling": ["storytell", "narrative", "story arc"],
    "design": ["design", "typograph", "color", "spacing", "layout", "brand", "visual", "figma", "css"],
    "accessibility": ["accessib", "a11y", "aria", "wcag", "contrast"],
    "research": ["research", "interview", "persona", "survey", "discovery", "jobs-to-be-done", "jtbd"],
    "strategy": ["strategy", "positioning", "roadmap", "okr", "prioriti", "market", "competitive"],
    "product": ["product", "prd", "epic", "user story", "press release", "backlog", "sprint"],
    "frontend": ["frontend", "react", "component", "ui ", "tailwind", "animation", "motion"],
    "development": ["debug", "refactor", "compile", "test", "lint", "git", "ci"],
    "writing": ["copywrit", "writing", "microcopy", "tone", "editorial"],
    "content": ["content", "changelog", "seo", "blog"],
    "ux": ["ux", "user flow", "journey", "usability"],
    "automation": ["automation", "workflow", "pipeline", "zapier"],
    "agent-tools": ["agent", "mcp", "cursor", "claude", "codex", "prompt library"],
    "documentation": ["documentation", "readme", "docs"],
    "productivity": ["plan", "review", "ship", "handoff", "retro"],
}

ASSET_EXT = {".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ttf", ".otf", ".woff", ".woff2", ".pdf", ".mp4"}
TOOL_EXT = {".py", ".js", ".mjs", ".cjs", ".ts", ".sh", ".rb", ".go"}
GLOBAL_NAMES = {"agents.md", "design.md", "claude.md", "readme.md", "contributing.md"}


# --- Small helpers --------------------------------------------------------

def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def kebab(name: str) -> str:
    name = re.sub(r"\.md$", "", name.strip(), flags=re.IGNORECASE)
    name = re.sub(r"[_\s]+", "-", name)
    name = re.sub(r"[^a-zA-Z0-9-]", "", name)
    name = re.sub(r"-+", "-", name).strip("-").lower()
    return name or "item"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[text.find("\n", 3) + 1 : end + 1]
    if yaml is not None:
        try:
            data = yaml.safe_load(block)
            return data if isinstance(data, dict) else {}
        except yaml.YAMLError:
            return {}
    out: dict[str, str] = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and m.group(2).strip():
            out[m.group(1)] = m.group(2).strip().strip("\"'")
    return out


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]{3,}", text.lower()))


# --- Classification -------------------------------------------------------

def classify_category(text: str, name: str = "") -> tuple[str, float]:
    hay = f"{name} {text}".lower()
    best, score = "", 0
    for cat in CATEGORIES:  # deterministic order
        n = sum(hay.count(kw) for kw in CATEGORY_KEYWORDS[cat])
        if n > score:
            best, score = cat, n
    if not best:
        return "", 0.0
    # confidence: crude — matched-keyword volume normalized
    return best, min(1.0, score / 3)


def classify_type(path: Path, text: str, fm: dict) -> tuple[str, float]:
    """Return (type, confidence). Content first, filename second."""
    declared = str(fm.get("type", "")).strip().lower()
    if declared in TYPE_DIR:
        return declared, 1.0

    name = path.name.lower()
    ext = path.suffix.lower()

    if ext in ASSET_EXT:
        return "asset", 1.0
    if name == "skill.md" or re.search(r"^#+\s", text) and re.search(r"##\s*(activate when|definition of done)", text, re.I):
        return "skill", 0.9
    if name in GLOBAL_NAMES:
        return "global", 0.9
    if ext in TOOL_EXT:
        return "tool", 0.8
    if re.search(r"##\s*(steps|review gates)\b", text, re.I) and re.search(r"step\s*\d|###\s*step", text, re.I):
        return "workflow", 0.8
    if re.search(r"##\s*(use for|prompt|inputs)\b", text, re.I) or "[input" in text.lower():
        return "prompt", 0.7
    if ".template" in name or "/templates/" in str(path).lower().replace("\\", "/"):
        return "template", 0.7
    if re.search(r"/(references|patterns|examples|frameworks)/", str(path).lower().replace("\\", "/")):
        return "reference", 0.7
    if ext == ".md":
        # bare markdown with no strong signal → reference (knowledge) but low confidence
        return "reference", 0.35
    return "reference", 0.2


# --- Artifacts + source resolution ---------------------------------------

@dataclass
class Artifact:
    name: str            # kebab id
    title: str           # human title
    type: str
    category: str
    confidence: float
    src: str             # path relative to source root (or the dir for skills)
    is_dir: bool
    description: str = ""
    needs_review: bool = False


def _find_manifest(root: Path) -> dict | None:
    for cand in ("ai-library.yaml", "ai-library.yml", "package.yaml"):
        p = root / cand
        if p.is_file() and yaml is not None:
            try:
                data = yaml.safe_load(p.read_text())
                if isinstance(data, dict) and data.get("items"):
                    return data
            except yaml.YAMLError:
                return None
    return None


def _title_of(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    if m:
        return m.group(1).strip()
    fm = parse_frontmatter(text)
    return str(fm.get("name") or fm.get("title") or fallback)


def _description_of(text: str, fm: dict) -> str:
    if fm.get("description"):
        return str(fm["description"])[:300]
    # first non-heading, non-empty line
    for line in text.splitlines():
        s = line.strip()
        if s and not s.startswith(("#", "---", "-", "|", "```")):
            return s[:300]
    return ""


def inspect_dir(root: Path) -> list[Artifact]:
    """Classify a resolved source directory into artifacts."""
    manifest = _find_manifest(root)
    arts: list[Artifact] = []

    if manifest:
        for item in manifest.get("items", []):
            p = root / item.get("path", "")
            typ = str(item.get("type", "")).lower()
            if typ not in TYPE_DIR:
                continue
            text = read_text(p) if p.is_file() else ""
            title = _title_of(text, p.name) if p.is_file() else p.name
            cat = str(item.get("category", "")) or classify_category(text, p.name)[0]
            arts.append(Artifact(
                name=kebab(item.get("name") or p.stem or p.name), title=title, type=typ,
                category=cat or "", confidence=1.0, src=str(p.relative_to(root)),
                is_dir=p.is_dir(), description=_description_of(text, parse_frontmatter(text)),
                needs_review=not bool(cat)))
        if arts:
            return arts

    # 1) Skill packages: any directory containing SKILL.md
    skill_dirs: set[Path] = set()
    for skill_md in root.rglob("SKILL.md"):
        d = skill_md.parent
        skill_dirs.add(d)
        text = read_text(skill_md)
        fm = parse_frontmatter(text)
        cat, cconf = classify_category(text, d.name)
        arts.append(Artifact(
            name=kebab(str(fm.get("name") or d.name)), title=_title_of(text, d.name),
            type="skill", category=cat, confidence=0.9,
            src=str(d.relative_to(root)), is_dir=True,
            description=_description_of(text, fm), needs_review=cconf < 0.2))

    # 2) Loose files (not inside a skill package)
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.name == "SKILL.md":
            continue
        if any(str(p).startswith(str(sd) + os.sep) for sd in skill_dirs):
            continue  # belongs to a skill package
        if any(part in {".git", "__MACOSX", "node_modules", "__pycache__"} for part in p.parts):
            continue
        text = read_text(p) if p.suffix.lower() not in ASSET_EXT else ""
        fm = parse_frontmatter(text)
        typ, tconf = classify_type(p, text, fm)
        cat, cconf = classify_category(text or p.name, p.name)
        arts.append(Artifact(
            name=kebab(p.stem), title=_title_of(text, p.name) if text else p.name,
            type=typ, category=cat, confidence=round(min(tconf, cconf or tconf), 2),
            src=str(p.relative_to(root)), is_dir=False,
            description=_description_of(text, fm),
            needs_review=(tconf < 0.5 or cconf < 0.2)))
    return arts


def resolve_source(source: str, workdir: Path) -> tuple[Path, dict]:
    """Return (resolved_dir, provenance)."""
    prov: dict = {}
    p = Path(source).expanduser()
    if source.startswith(("http://", "https://", "git@")) or source.endswith(".git"):
        dest = workdir / "src"
        subprocess.run(["git", "clone", "--depth", "1", source, str(dest)],
                       check=True, capture_output=True, text=True, timeout=180)
        commit = subprocess.run(["git", "-C", str(dest), "rev-parse", "HEAD"],
                                 capture_output=True, text=True).stdout.strip()
        shutil.rmtree(dest / ".git", ignore_errors=True)
        prov = {"type": "github", "url": source, "commit": commit}
        return dest, prov
    if p.is_dir():
        return p, {"type": "local", "original_path": str(p.resolve())}
    if p.suffix.lower() == ".zip" and p.is_file():
        dest = workdir / "src"
        dest.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(p) as z:
            z.extractall(dest)
        inner = [c for c in dest.iterdir() if c.is_dir() and c.name != "__MACOSX"]
        root = inner[0] if len(inner) == 1 and not any(f.is_file() for f in dest.iterdir()) else dest
        return root, {"type": "zip", "original_path": str(p.resolve())}
    if p.is_file():
        dest = workdir / "src"
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest / p.name)
        return dest, {"type": "local", "original_path": str(p.resolve())}
    raise SystemExit(f"Cannot resolve source: {source}")


# --- Registry -------------------------------------------------------------

def registry_path(home: Path) -> Path:
    return home / "registry" / "packages.json"


def load_registry(home: Path) -> dict:
    p = registry_path(home)
    if p.is_file():
        try:
            return json.loads(p.read_text())
        except json.JSONDecodeError:
            pass
    return {"version": 1, "items": []}


def save_registry(home: Path, reg: dict) -> None:
    p = registry_path(home)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(reg, indent=2) + "\n", encoding="utf-8")


def ensure_home(home: Path) -> None:
    for d in LIBRARY_DIRS:
        (home / d).mkdir(parents=True, exist_ok=True)


# --- Overlap detection ----------------------------------------------------

def find_overlap(art: Artifact, reg: dict) -> dict | None:
    incoming = tokens(art.description) | tokens(art.title)
    best = None
    for it in reg["items"]:
        if it["type"] != art.type:
            continue
        if it["name"] == art.name:
            return {"id": it["id"], "reason": "same name", "score": 1.0}
        existing = tokens(it.get("description", "")) | tokens(it.get("title", ""))
        if incoming and existing:
            jac = len(incoming & existing) / len(incoming | existing)
            if jac >= 0.5 and (best is None or jac > best["score"]):
                best = {"id": it["id"], "reason": "similar description", "score": round(jac, 2)}
    return best


# --- Routing + install ----------------------------------------------------

def destination(home: Path, art: Artifact) -> Path:
    if art.needs_review or (not art.category and art.type not in ("global", "tool", "asset")):
        base = home / "inbox" / art.type
    else:
        sub = TYPE_DIR[art.type]
        base = home / sub / art.category if art.category else home / sub
    if art.is_dir:
        return base / art.name
    ext = Path(art.src).suffix or ".md"
    return base / f"{art.name}{ext}"


def plan(home: Path, source_root: Path, arts: list[Artifact], reg: dict) -> list[dict]:
    rows = []
    for a in arts:
        dest = destination(home, a)
        rows.append({
            "artifact": a, "dest": dest,
            "overlap": find_overlap(a, reg),
        })
    return rows


def render_plan(source: str, rows: list[dict], home: Path) -> str:
    out = [f"Source: {source}", f"Library: {home}", ""]
    by_type: dict[str, int] = {}
    for r in rows:
        by_type[r["artifact"].type] = by_type.get(r["artifact"].type, 0) + 1
    out.append("Detected: " + ", ".join(f"{n} {t}" for t, n in sorted(by_type.items())) or "nothing")
    out.append("")
    out.append(f"{'TYPE':<11}{'CATEGORY':<20}{'NAME':<30}DESTINATION")
    for r in rows:
        a = r["artifact"]
        rel = r["dest"].relative_to(home)
        flag = "  ⚠ overlap:" + r["overlap"]["id"] if r["overlap"] else ""
        review = "  [needs review]" if a.needs_review else ""
        out.append(f"{a.type:<11}{(a.category or '—'):<20}{a.name:<30}{rel}{flag}{review}")
    return "\n".join(out)


def do_install(home: Path, source: str, rows: list[dict], prov: dict,
               source_root: Path, reg: dict) -> list[dict]:
    installed = []
    for r in rows:
        a: Artifact = r["artifact"]
        dest: Path = r["dest"]
        src = source_root / a.src
        dest.parent.mkdir(parents=True, exist_ok=True)
        if a.is_dir:
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest, ignore=shutil.ignore_patterns(".git", "__pycache__", "node_modules", "__MACOSX"))
        else:
            shutil.copy2(src, dest)
        item = {
            "id": f"{a.type}/{a.category or 'uncategorized'}/{a.name}",
            "name": a.name, "title": a.title, "type": a.type, "category": a.category,
            "description": a.description, "local_path": str(dest.relative_to(home)),
            "source": {**prov, "item": a.src}, "installed_at": now_iso(),
            "status": "installed", "needs_review": a.needs_review,
        }
        reg["items"] = [x for x in reg["items"] if x["id"] != item["id"]]
        reg["items"].append(item)
        installed.append(item)
    save_registry(home, reg)
    return installed


# --- Index regeneration ---------------------------------------------------

def regenerate_index(home: Path) -> Path:
    reg = load_registry(home)
    lines = ["# AI Library Index", "", f"_generated {now_iso()} · {len(reg['items'])} items_", ""]
    by_type: dict[str, list[dict]] = {}
    for it in reg["items"]:
        by_type.setdefault(it["type"], []).append(it)
    for typ in sorted(by_type):
        lines.append(f"## {typ.capitalize()}s ({len(by_type[typ])})")
        lines.append("")
        lines.append("| Name | Category | Description | Source |")
        lines.append("| --- | --- | --- | --- |")
        for it in sorted(by_type[typ], key=lambda x: (x.get("category") or "", x["name"])):
            src = it.get("source", {})
            srctxt = src.get("url") or src.get("original_path") or src.get("type", "")
            desc = (it.get("description") or "").replace("|", "\\|")[:80]
            lines.append(f"| `{it['name']}` | {it.get('category') or '—'} | {desc} | {srctxt} |")
        lines.append("")
    out = home / "INDEX.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


# --- doctor ---------------------------------------------------------------

def doctor(home: Path) -> list[str]:
    issues: list[str] = []
    reg = load_registry(home)
    seen_ids: set[str] = set()
    for it in reg["items"]:
        if it["id"] in seen_ids:
            issues.append(f"duplicate registry id: {it['id']}")
        seen_ids.add(it["id"])
        if not (home / it["local_path"]).exists():
            issues.append(f"registry points at missing path: {it['local_path']}")
        if not it.get("source"):
            issues.append(f"missing provenance: {it['id']}")
        if it.get("needs_review"):
            issues.append(f"needs review (in inbox): {it['id']}")
    # orphaned files under type dirs not in registry
    known = {home / it["local_path"] for it in reg["items"]}
    for sub in ("skills", "prompts", "workflows", "references", "templates"):
        base = home / sub
        if not base.is_dir():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.name != "INDEX.md" and not any(str(p).startswith(str(k)) for k in known):
                pass  # loose file; not necessarily an error in V1
    return issues


# --- CLI ------------------------------------------------------------------

def _load_source(source: str):
    workdir = Path(tempfile.mkdtemp(prefix="ai-lib-"))
    root, prov = resolve_source(source, workdir)
    arts = inspect_dir(root)
    return workdir, root, prov, arts


def cmd_inspect(args) -> int:
    home = Path(args.home).expanduser()
    workdir, root, prov, arts = _load_source(args.source)
    try:
        reg = load_registry(home)
        rows = plan(home, root, arts, reg)
        print(render_plan(args.source, rows, home))
    finally:
        shutil.rmtree(workdir, ignore_errors=True)
    return 0


def cmd_install(args) -> int:
    home = Path(args.home).expanduser()
    ensure_home(home)
    workdir, root, prov, arts = _load_source(args.source)
    try:
        reg = load_registry(home)
        rows = plan(home, root, arts, reg)
        print(render_plan(args.source, rows, home))
        if not arts:
            print("\nNothing to install.")
            return 0
        overlaps = [r for r in rows if r["overlap"]]
        if args.dry_run:
            print("\n[dry-run] no changes made.")
            return 0
        if overlaps and not args.yes:
            print("\nOverlap(s) detected; re-run with --yes to install anyway, or resolve first:")
            for r in overlaps:
                print(f"  {r['artifact'].name} ~ {r['overlap']['id']} ({r['overlap']['reason']}, {r['overlap']['score']})")
            return 2
        if not args.yes:
            print("\nRe-run with --yes to apply this plan (or --dry-run to preview).")
            return 3
        installed = do_install(home, args.source, rows, prov, root, reg)
        regenerate_index(home)
        print(f"\nInstalled {len(installed)} item(s). Registry + INDEX.md updated.")
    finally:
        shutil.rmtree(workdir, ignore_errors=True)
    return 0


def cmd_list(args) -> int:
    home = Path(args.home).expanduser()
    reg = load_registry(home)
    items = reg["items"]
    if args.type:
        items = [i for i in items if i["type"] == args.type.rstrip("s")]
    if args.category:
        items = [i for i in items if i.get("category") == args.category]
    for it in sorted(items, key=lambda x: (x["type"], x.get("category") or "", x["name"])):
        print(f"{it['type']:<10} {it.get('category') or '—':<18} {it['name']}")
    print(f"\n{len(items)} item(s).")
    return 0


def cmd_search(args) -> int:
    home = Path(args.home).expanduser()
    q = args.query.lower()
    reg = load_registry(home)
    hits = [i for i in reg["items"]
            if q in i["name"].lower() or q in (i.get("description") or "").lower()
            or q in (i.get("category") or "").lower() or q in (i.get("title") or "").lower()]
    for it in hits:
        print(f"{it['type']:<10} {it.get('category') or '—':<16} {it['name']} — {(it.get('description') or '')[:70]}")
    print(f"\n{len(hits)} match(es).")
    return 0


def cmd_info(args) -> int:
    home = Path(args.home).expanduser()
    reg = load_registry(home)
    for it in reg["items"]:
        if it["id"] == args.item or it["name"] == args.item:
            print(json.dumps(it, indent=2))
            return 0
    print(f"Not found: {args.item}")
    return 1


def cmd_remove(args) -> int:
    home = Path(args.home).expanduser()
    reg = load_registry(home)
    kept, removed = [], []
    for it in reg["items"]:
        if it["id"] == args.item or it["name"] == args.item:
            removed.append(it)
        else:
            kept.append(it)
    if not removed:
        print(f"Not found: {args.item}")
        return 1
    for it in removed:
        target = home / it["local_path"]
        if args.purge and target.exists():
            if target.is_dir():
                shutil.rmtree(target)
            else:
                target.unlink()
    reg["items"] = kept
    save_registry(home, reg)
    regenerate_index(home)
    print(f"Removed {len(removed)} item(s) from registry" + (" and disk" if args.purge else ""))
    return 0


def cmd_doctor(args) -> int:
    home = Path(args.home).expanduser()
    issues = doctor(home)
    if not issues:
        print("doctor: no issues found.")
        return 0
    print(f"doctor: {len(issues)} issue(s):")
    for i in issues:
        print(f"  - {i}")
    return 1


def cmd_reindex(args) -> int:
    home = Path(args.home).expanduser()
    out = regenerate_index(home)
    print(f"Wrote {out}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ai-lib", description="Package manager + librarian for an AI capability library.")
    p.add_argument("--home", default=str(DEFAULT_HOME), help="library home (default $AI_LIBRARY_HOME or ~/.ai-library)")
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("inspect", help="Classify a source and print the routing plan")
    pi.add_argument("source"); pi.set_defaults(func=cmd_inspect)

    pin = sub.add_parser("install", help="Install a source into the library")
    pin.add_argument("source")
    pin.add_argument("--dry-run", action="store_true", help="show the plan; make no changes")
    pin.add_argument("--yes", "-y", action="store_true", help="apply without prompting")
    pin.set_defaults(func=cmd_install)

    pl = sub.add_parser("list", help="List installed items")
    pl.add_argument("type", nargs="?", default=None)
    pl.add_argument("--category", default=None)
    pl.set_defaults(func=cmd_list)

    ps = sub.add_parser("search", help="Search the library")
    ps.add_argument("query"); ps.set_defaults(func=cmd_search)

    pf = sub.add_parser("info", help="Show a registry item")
    pf.add_argument("item"); pf.set_defaults(func=cmd_info)

    pr = sub.add_parser("remove", help="Remove an item from the registry")
    pr.add_argument("item")
    pr.add_argument("--purge", action="store_true", help="also delete files on disk")
    pr.set_defaults(func=cmd_remove)

    sub.add_parser("doctor", help="Validate the library").set_defaults(func=cmd_doctor)
    sub.add_parser("reindex", help="Regenerate INDEX.md").set_defaults(func=cmd_reindex)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
