#!/usr/bin/env python3
"""library-add — the single add-path for this repo's library (`/add-to-library`).

Classifies pasted text or a file and routes it to the correct place:

- **skill**    → `skills/<name>/SKILL.md`            (Work Kit — a reusable capability)
- **prompt**   → `prompts/commands/<name>.md`        (Prompt Kit — a slash-command)
- **workflow** → `workflows/<name>/WORKFLOW.md`
- **reference**→ `references/<category>/<name>.md`
- **template** → `templates/<category>/<name>.md`

Classification/normalization reuse the `ai-lib` engine (`tools/ai-lib`). For
installing whole external repos/zips, use `tools/ai-lib/ai-lib install` instead;
this script is the lightweight "add one thing I pasted" path.

Usage:
  ./scripts/library-add.py --file NOTES.md
  ./scripts/library-add.py --kind prompt --name deck-review --stdin < body.md
  ./scripts/library-add.py "## Use For\\nreview a deck\\n## Prompt\\n..."
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "ai-lib"))
import ai_lib  # noqa: E402  (shared classifier / normalizer)

# where each type lands in THIS repo (Work Kit + Prompt Kit)
DEST = {
    "skill": lambda name, cat: ROOT / "skills" / name / "SKILL.md",
    "prompt": lambda name, cat: ROOT / "prompts" / "commands" / f"{name}.md",
    "workflow": lambda name, cat: ROOT / "workflows" / name / "WORKFLOW.md",
    "reference": lambda name, cat: ROOT / "references" / (cat or "misc") / f"{name}.md",
    "template": lambda name, cat: ROOT / "templates" / (cat or "misc") / f"{name}.md",
}
KIT = {"skill": "Work Kit", "prompt": "Prompt Kit", "workflow": "Work Kit",
       "reference": "references", "template": "templates"}


def _read_input(args) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8", errors="replace")
    if args.stdin or not args.text:
        data = sys.stdin.read()
        if data.strip():
            return data
    if args.text:
        return "\n".join(args.text).replace("\\n", "\n")
    raise SystemExit("No content: pass --file, --stdin, or text.")


def classify(text: str, kind: str | None, name: str | None) -> tuple[str, str, str]:
    fm = ai_lib.parse_frontmatter(text)
    typ = kind or ai_lib.classify_type(Path((name or "item") + ".md"), text, fm)[0]
    if typ not in DEST:
        # fold asset/global/tool into the closest supported add-path
        typ = "reference"
    cat, _ = ai_lib.classify_category(text, name or "")
    resolved_name = ai_lib.kebab(name or fm.get("name") or _title(text) or "item")
    return typ, cat, resolved_name


def _title(text: str) -> str:
    import re
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def ensure_frontmatter(text: str, typ: str, cat: str, name: str) -> str:
    fm = ai_lib.parse_frontmatter(text)
    if fm:
        return text  # respect existing front-matter
    title = _title(text) or name.replace("-", " ").title()
    header = [f"---", f"name: {name}", f"type: {typ}"]
    if cat:
        header.append(f"category: {cat}")
    header.append(f"description: {title}")
    header.append("---")
    body = text if text.startswith("#") else f"# {title}\n\n{text}"
    return "\n".join(header) + "\n\n" + body


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Add one pasted item to the library (the /add-to-library path).")
    p.add_argument("text", nargs="*", help="inline content (or use --file/--stdin)")
    p.add_argument("--kind", choices=list(DEST) + ["auto"], default="auto", help="artifact type (default: auto-classify)")
    p.add_argument("--name", default=None, help="explicit kebab-case name")
    p.add_argument("--category", default=None, help="override the detected category")
    p.add_argument("--file", default=None, help="read content from a file")
    p.add_argument("--stdin", action="store_true", help="read content from stdin")
    p.add_argument("--dry-run", action="store_true", help="show where it would land; write nothing")
    args = p.parse_args(argv)

    text = _read_input(args)
    kind = None if args.kind == "auto" else args.kind
    typ, cat, name = classify(text, kind, args.name)
    cat = args.category or cat
    dest = DEST[typ](name, cat)

    print(f"Type: {typ}  ({KIT[typ]})")
    print(f"Category: {cat or '—'}")
    print(f"Name: {name}")
    print(f"Destination: {dest.relative_to(ROOT)}")

    if args.dry_run:
        print("\n[dry-run] nothing written.")
        return 0
    if dest.exists():
        print(f"\nRefusing to overwrite existing {dest.relative_to(ROOT)}. "
              f"Pick a different --name or edit it directly.")
        return 2

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(ensure_frontmatter(text, typ, cat, name), encoding="utf-8")
    print(f"\nAdded → {dest.relative_to(ROOT)}")
    if typ == "skill":
        print("Next: ./scripts/skills-db.sh build   (refresh the skills catalog)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
