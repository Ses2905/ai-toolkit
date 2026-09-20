#!/usr/bin/env python3
"""Pull Agent Skills from GitHub catalogs into ~/.cursor/skills."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def expand_user(path: str) -> Path:
    return Path(path).expanduser().resolve()


def load_catalog(root: Path) -> dict:
    catalog_path = root / "catalog" / "presets.json"
    if not catalog_path.is_file():
        raise SystemExit(f"Missing catalog file: {catalog_path}")
    return json.loads(catalog_path.read_text())


def run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def is_commit_sha(ref: str) -> bool:
    """True when *ref* is a hex object id, not a branch/tag name."""
    return bool(ref) and 7 <= len(ref) <= 40 and all(
        c in "0123456789abcdef" for c in ref.lower()
    )


def sync_repo(cache: Path, source_id: str, spec: dict) -> Path:
    dest = cache / source_id
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = spec["git"]
    ref = spec.get("ref", "main")
    # Commit SHAs are not remote branch names. Cloning with --branch <sha>
    # prints `fatal: Remote branch ... not found` and looks like a failed
    # install even though the retry succeeds.
    if (dest / ".git").is_dir():
        run(["git", "-C", str(dest), "fetch", "--depth", "1", "origin", ref])
        run(["git", "-C", str(dest), "checkout", "-q", "FETCH_HEAD"])
        return dest

    if dest.exists():
        shutil.rmtree(dest)
    if is_commit_sha(ref):
        run(["git", "clone", "--depth", "1", url, str(dest)])
        run(["git", "-C", str(dest), "fetch", "--depth", "1", "origin", ref])
        run(["git", "-C", str(dest), "checkout", "-q", "FETCH_HEAD"])
    else:
        try:
            run(["git", "clone", "--depth", "1", "--branch", ref, url, str(dest)])
        except subprocess.CalledProcessError:
            run(["git", "clone", "--depth", "1", url, str(dest)])
            run(["git", "-C", str(dest), "fetch", "--depth", "1", "origin", ref])
            run(["git", "-C", str(dest), "checkout", "-q", "FETCH_HEAD"])
    return dest


def skill_entries(catalog: dict, preset_name: str, cache: Path) -> list[tuple[str, Path]]:
    preset = catalog["presets"].get(preset_name)
    if not preset:
        known = ", ".join(sorted(catalog["presets"]))
        raise SystemExit(f"Unknown preset {preset_name!r}. Known: {known}")

    entries: list[tuple[str, Path]] = []
    if "expand" in preset:
        source_id = preset["expand"]
        spec = catalog["sources"][source_id]
        repo = sync_repo(cache, source_id, spec)
        root = repo / spec.get("root", "")
        nested = spec.get("nested_skills")
        if nested:
            glob_pat = nested if isinstance(nested, str) else "*/skills/*"
            for skill_dir in sorted(
                p for p in root.glob(glob_pat) if p.is_dir() and (p / "SKILL.md").is_file()
            ):
                entries.append((skill_dir.name, skill_dir))
            return entries
        for skill_dir in sorted(p for p in root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()):
            entries.append((skill_dir.name, skill_dir))
        return entries

    needed_sources = {item["source"] for item in preset["skills"]}
    repos: dict[str, Path] = {}
    for source_id in needed_sources:
        repos[source_id] = sync_repo(cache, source_id, catalog["sources"][source_id])

    for item in preset["skills"]:
        source_id = item["source"]
        spec = catalog["sources"][source_id]
        src = repos[source_id] / spec.get("root", "") / item["path"]
        name = item.get("name") or Path(item["path"]).name
        entries.append((name, src))
    return entries


def copy_skill(src: Path, dest_root: Path, name: str) -> Path:
    if not (src / "SKILL.md").is_file():
        raise SystemExit(f"No SKILL.md in {src}")
    dest = dest_root / name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(
        src,
        dest,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "node_modules", ".DS_Store"),
    )
    return dest


def main() -> int:
    parser = argparse.ArgumentParser(description="Install catalog skills into ~/.cursor/skills")
    parser.add_argument("--preset", default="design-product", help="Preset name from catalog/presets.json")
    parser.add_argument("--dest", default=None, help="Install directory (default: ~/.cursor/skills)")
    parser.add_argument("--only", default="", help="Comma-separated skill names to keep from the preset")
    parser.add_argument("--list", action="store_true", help="List preset skills without installing")
    parser.add_argument("--root", default=None, help="work-kit repo root")
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    catalog = load_catalog(root)
    dest_root = expand_user(args.dest or catalog.get("default_dest", "~/.cursor/skills"))
    cache = expand_user(catalog.get("cache_dir", "~/.cache/work-kit/skill-catalogs"))

    if args.list:
        print(f"preset: {args.preset}")
        for name, path in skill_entries(catalog, args.preset, cache):
            print(f"  {name}\t{path}")
        return 0

    only = {item.strip() for item in args.only.split(",") if item.strip()}
    dest_root.mkdir(parents=True, exist_ok=True)
    installed: list[str] = []
    for name, src in skill_entries(catalog, args.preset, cache):
        if only and name not in only:
            continue
        dest = copy_skill(src, dest_root, name)
        installed.append(name)
        print(f"Installed {name} → {dest}")

    if only:
        missing = sorted(only - set(installed))
        if missing:
            raise SystemExit(f"Not in preset {args.preset}: {', '.join(missing)}")

    print()
    print(f"Installed {len(installed)} skill(s) into {dest_root}")
    print("Next: Developer: Reload Window, then Customize → Skills")
    print("Cloud Agents: Settings → Agents → Sync Skills for Cloud Agents")
    return 0


if __name__ == "__main__":
    sys.exit(main())
