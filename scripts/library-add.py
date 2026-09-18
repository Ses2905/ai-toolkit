#!/usr/bin/env python3
"""Add prompts, skills, or rules to the cursor-skills library the right way.

Usage:
  ./scripts/library-add.py sort --text "…"
  ./scripts/library-add.py sort --file path.md
  ./scripts/library-add.py prompt --name prd --theme product --file path.md
  ./scripts/library-add.py prompt --name prd --theme product --stdin
  ./scripts/library-add.py skill --name my-flow --file path/to/dir-or-SKILL.md
  ./scripts/library-add.py skill --name my-flow --stdin --slash-only
  ./scripts/library-add.py rule --name my-rule --file path.mdc --always
  ./scripts/library-add.py install

Guarantees:
  - Prompts go under prompts/commands/ (Prompt Kit), never skills/
  - Skills go under skills/<name>/SKILL.md (Work Kit)
  - Rules go under rules/<name>.mdc
  - Rebuilds prompts/INDEX.md and (for skills) the skills database
  - Optionally runs install-local.sh
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "prompts"
PROMPT_COMMANDS = PROMPTS_DIR / "commands"
SKILLS_DIR = ROOT / "skills"
RULES_DIR = ROOT / "rules"
COMMANDS_DIR = ROOT / "commands"

THEMES = ("product", "writing", "research", "strategy", "engineering", "personal")
NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")

PROMPT_HINTS = (
    "output as",
    "treat any text after",
    "guide the user through",
    "ask the user for",
    "best_for:",
    "scenarios:",
    "estimated_time:",
    "intent:",
)
SKILL_HINTS = (
    "## workflow",
    "## when to use",
    "## guardrails",
    "run `",
    "scripts/",
    "references/",
    "disable-model-invocation",
    "use when the user",
)

THEME_HEADINGS = {
    "meta": "Kit",
    "product": "Product",
    "writing": "Writing",
    "research": "Research",
    "strategy": "Strategy",
    "engineering": "Engineering",
    "personal": "Personal",
}


def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def validate_name(name: str) -> str:
    name = name.strip().lower()
    if not NAME_RE.match(name):
        die(f"invalid name {name!r}: use kebab-case, max 64 chars")
    return name


def read_body(args: argparse.Namespace) -> str:
    if getattr(args, "stdin", False):
        return sys.stdin.read()
    if getattr(args, "text", None):
        return args.text
    if getattr(args, "file", None):
        path = Path(args.file)
        if not path.exists():
            die(f"file not found: {path}")
        if path.is_dir():
            skill = path / "SKILL.md"
            if skill.exists():
                return skill.read_text()
            die(f"directory has no SKILL.md: {path}")
        return path.read_text()
    die("provide --file, --text, or --stdin")


def strip_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    block = text[3:end]
    body = text[end + 4 :].lstrip("\n")
    meta: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body


def classify(text: str) -> tuple[str, str]:
    lower = text.lower()
    prompt_score = sum(1 for h in PROMPT_HINTS if h in lower)
    skill_score = sum(1 for h in SKILL_HINTS if h in lower)
    meta, _body = strip_frontmatter(text)
    if meta.get("type") in {"component"} and "template" in lower:
        prompt_score += 2
    if meta.get("type") in {"interactive", "workflow"}:
        skill_score += 2
    if len(text) < 1200 and prompt_score >= skill_score:
        prompt_score += 1
    if prompt_score > skill_score:
        return "prompt", f"prompt_score={prompt_score} skill_score={skill_score}"
    if skill_score > prompt_score:
        return "skill", f"prompt_score={prompt_score} skill_score={skill_score}"
    return "prompt", f"tie prompt_score={prompt_score} skill_score={skill_score}; default prompt"


def ensure_frontmatter(text: str, **fields: str) -> str:
    meta, body = strip_frontmatter(text)
    for key, value in fields.items():
        if value is None:
            continue
        if key not in meta or not meta[key]:
            meta[key] = value
        elif key == "disable-model-invocation":
            meta[key] = value
    lines = ["---"]
    order = [
        "name",
        "description",
        "argument-hint",
        "theme",
        "disable-model-invocation",
    ]
    seen = set()
    for key in order:
        if key in meta:
            lines.append(f"{key}: {meta[key]}")
            seen.add(key)
    for key, value in meta.items():
        if key not in seen:
            lines.append(f"{key}: {value}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines) + body.lstrip("\n")


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def cmd_sort(args: argparse.Namespace) -> None:
    text = read_body(args)
    kind, why = classify(text)
    print(kind)
    print(why, file=sys.stderr)


def rebuild_prompt_index() -> None:
    if not PROMPT_COMMANDS.is_dir():
        return
    buckets: dict[str, list[tuple[str, str]]] = {t: [] for t in ("meta",) + THEMES}
    for path in sorted(PROMPT_COMMANDS.glob("*.md")):
        meta, body = strip_frontmatter(path.read_text())
        name = meta.get("name") or path.stem
        theme = meta.get("theme") or ("meta" if name in {"new-prompt", "sort-skill-or-prompt"} else "personal")
        if theme not in buckets:
            theme = "personal"
        desc = meta.get("description") or first_heading(body) or name
        buckets[theme].append((name, desc))

    lines = [
        "# Prompt catalog",
        "",
        "Slash commands in this kit. Kit commands manage the library; the rest are prompts you invoke.",
        "",
        "Add a prompt by pasting it in chat and saying \"add this to the prompt library\", or `/new-prompt`.",
        "",
    ]
    for theme, heading in THEME_HEADINGS.items():
        items = buckets.get(theme) or []
        lines.append(f"## {heading}")
        lines.append("")
        if not items:
            lines.append("_Empty — send the next one._")
            lines.append("")
            continue
        if theme == "meta":
            lines.append("| Command | Theme | What it does |")
            lines.append("| --- | --- | --- |")
            for name, desc in items:
                lines.append(f"| `/{name}` | meta | {desc} |")
        else:
            lines.append("| Command | What it does |")
            lines.append("| --- | --- | --- |")
            for name, desc in items:
                lines.append(f"| `/{name}` | {desc} |")
        lines.append("")
    (PROMPTS_DIR / "INDEX.md").write_text("\n".join(lines).rstrip() + "\n")
    print(f"updated {PROMPTS_DIR / 'INDEX.md'}")


def rebuild_skills_db() -> None:
    script = ROOT / "scripts" / "skills_db.py"
    if not script.exists():
        return
    subprocess.check_call([sys.executable, str(script), "--root", str(ROOT), "build"])


def maybe_install(args: argparse.Namespace) -> None:
    if getattr(args, "no_install", False):
        return
    install()


def install() -> None:
    script = ROOT / "scripts" / "install-local.sh"
    subprocess.check_call(["bash", str(script)])


def cmd_prompt(args: argparse.Namespace) -> None:
    name = validate_name(args.name)
    theme = args.theme
    if theme not in THEMES:
        die(f"theme must be one of {', '.join(THEMES)}")
    text = read_body(args)
    meta, body = strip_frontmatter(text)
    description = meta.get("description") or first_heading(body) or name
    out = ensure_frontmatter(
        text if text.startswith("---") else f"# {name}\n\n{text}",
        name=name,
        description=description,
        theme=theme,
    )
    PROMPT_COMMANDS.mkdir(parents=True, exist_ok=True)
    dest = PROMPT_COMMANDS / f"{name}.md"
    dest.write_text(out if out.endswith("\n") else out + "\n")
    print(f"wrote {dest}")
    print(f"invoke /{name}")
    rebuild_prompt_index()
    maybe_install(args)


def write_command(name: str, description: str) -> None:
    COMMANDS_DIR.mkdir(parents=True, exist_ok=True)
    dest = COMMANDS_DIR / f"{name}.md"
    dest.write_text(
        "\n".join(
            [
                "---",
                f"name: {name}",
                f"description: {description}",
                "---",
                "",
                f"Follow `skills/{name}/SKILL.md`.",
                "",
            ]
        )
    )
    print(f"wrote {dest}")


def cmd_skill(args: argparse.Namespace) -> None:
    name = validate_name(args.name)
    dest_dir = SKILLS_DIR / name
    src = Path(args.file) if getattr(args, "file", None) else None

    if src is not None and src.is_dir():
        src_resolved = src.resolve()
        dest_resolved = dest_dir.resolve() if dest_dir.exists() else dest_dir
        if src_resolved != dest_resolved:
            if dest_dir.exists():
                shutil.rmtree(dest_dir)
            shutil.copytree(
                src,
                dest_dir,
                ignore=shutil.ignore_patterns(".git", "node_modules", ".DS_Store"),
            )
        skill_md = dest_dir / "SKILL.md"
        if not skill_md.exists():
            die(f"copied {src} but no SKILL.md at {skill_md}")
        text = skill_md.read_text()
    else:
        text = read_body(args)
        dest_dir.mkdir(parents=True, exist_ok=True)
        skill_md = dest_dir / "SKILL.md"

    meta, body = strip_frontmatter(text)
    description = meta.get("description") or first_heading(body) or name
    fields = {"name": name, "description": description}
    if args.slash_only:
        fields["disable-model-invocation"] = "true"
    out = ensure_frontmatter(text if text.startswith("---") else f"# {name}\n\n{text}", **fields)
    skill_md.write_text(out if out.endswith("\n") else out + "\n")
    print(f"wrote {skill_md}")
    if args.slash_only or args.with_command:
        write_command(name, description)
    print(f"invoke /{name}")
    rebuild_skills_db()
    maybe_install(args)


def cmd_rule(args: argparse.Namespace) -> None:
    name = validate_name(args.name)
    text = read_body(args)
    RULES_DIR.mkdir(parents=True, exist_ok=True)
    dest = RULES_DIR / f"{name}.mdc"
    always = "true" if args.always else "false"
    if text.startswith("---"):
        out = text
        if "alwaysApply:" not in text:
            meta, body = strip_frontmatter(text)
            header = ["---", f"description: {meta.get('description', name)}", f"alwaysApply: {always}", "---", ""]
            out = "\n".join(header) + body.lstrip("\n")
    else:
        out = "\n".join(["---", f"description: {name}", f"alwaysApply: {always}", "---", "", text.lstrip("\n")])
    dest.write_text(out if out.endswith("\n") else out + "\n")
    print(f"wrote {dest}")
    maybe_install(args)


def cmd_install(_args: argparse.Namespace) -> None:
    rebuild_prompt_index()
    rebuild_skills_db()
    install()


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_io(sp: argparse.ArgumentParser) -> None:
        sp.add_argument("--file")
        sp.add_argument("--text")
        sp.add_argument("--stdin", action="store_true")

    def add_install_flag(sp: argparse.ArgumentParser) -> None:
        sp.add_argument("--no-install", action="store_true", help="Skip install-local.sh")

    s = sub.add_parser("sort")
    add_io(s)
    s.set_defaults(func=cmd_sort)

    s = sub.add_parser("prompt")
    s.add_argument("--name", required=True)
    s.add_argument("--theme", required=True)
    add_io(s)
    add_install_flag(s)
    s.set_defaults(func=cmd_prompt)

    s = sub.add_parser("skill")
    s.add_argument("--name", required=True)
    s.add_argument("--file")
    s.add_argument("--text")
    s.add_argument("--stdin", action="store_true")
    s.add_argument("--slash-only", action="store_true")
    s.add_argument("--with-command", action="store_true")
    add_install_flag(s)
    s.set_defaults(func=cmd_skill)

    s = sub.add_parser("rule")
    s.add_argument("--name", required=True)
    s.add_argument("--file")
    s.add_argument("--text")
    s.add_argument("--stdin", action="store_true")
    s.add_argument("--always", action="store_true")
    add_install_flag(s)
    s.set_defaults(func=cmd_rule)

    s = sub.add_parser("install")
    s.set_defaults(func=cmd_install)
    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
