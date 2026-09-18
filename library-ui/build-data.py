#!/usr/bin/env python3
"""Build library-ui/data.js for the Library UI prototype.

Real skills + prompts come from catalog/skills-index.json. Workflows, references,
templates, tools, projects, integrations, inbox, updates, health and activity are
synthesized (clearly placeholder) so the wireframes use realistic content while
those tiers are still sparse. Regenerate: python3 library-ui/build-data.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "skills-index.json"
OUT = ROOT / "library-ui" / "data.js"


def title_of(name: str) -> str:
    return name.replace("-", " ").replace("_", " ").title()


def main() -> int:
    cat = json.loads(CATALOG.read_text())
    items: list[dict] = []
    by_name: dict[str, dict] = {}

    for s in cat["skills"]:
        it = {
            "id": f"{s['kind']}:{s['name']}",
            "name": s["name"],
            "title": title_of(s["name"]),
            "kind": s.get("kind", "skill"),
            "category": s.get("category") or "Uncategorized",
            "description": s.get("description", ""),
            "summary": s.get("summary", "") or s.get("description", ""),
            "best_use": s.get("best_use", ""),
            "watch_outs": s.get("watch_outs", ""),
            "command": s.get("command", ""),
            "date_added": s.get("date_added", ""),
            "date_updated": s.get("date_updated", ""),
            "source": {"type": "local", "label": "this repo"},
            "status": "installed",
            "depends_on": [], "used_by": [], "references": [], "enabled_in": [],
        }
        items.append(it)
        by_name[s["name"]] = it

    def pick(cat_name: str, n: int) -> list[str]:
        names = [i["name"] for i in items if i["kind"] == "skill" and i["category"] == cat_name]
        return names[:n]

    pres = pick("Presentations & Diagrams", 4)
    prod = pick("Product & Discovery", 4)
    design = pick("Design & Frontend", 3)

    # --- Synthesized workflows (reference real skills where possible) ---
    workflows = [
        {"id": "workflow:build-executive-presentation", "name": "build-executive-presentation",
         "title": "Build Executive Presentation", "kind": "workflow", "category": "Presentations & Diagrams",
         "summary": "From a messy executive ask to a decision-ready board deck.",
         "source": {"type": "local", "label": "this repo"}, "status": "installed",
         "date_added": "2026-09-18", "date_updated": "2026-09-18",
         "steps": [
             {"name": "Research & Inputs", "uses": prod[:2]},
             {"name": "Narrative Architecture", "uses": prod[2:4] or prod[:1]},
             {"name": "Visual Development", "uses": pres[:3]},
             {"name": "Build", "uses": pres[3:4] or pres[:1]},
             {"name": "QA", "uses": design[:1]},
         ]},
        {"id": "workflow:redesign-page", "name": "redesign-page", "title": "Redesign a Page",
         "kind": "workflow", "category": "Design & Frontend",
         "summary": "Audit an existing page and rebuild it to the design standards.",
         "source": {"type": "local", "label": "this repo"}, "status": "installed",
         "date_added": "2026-09-18", "date_updated": "2026-09-18",
         "steps": [
             {"name": "Audit", "uses": design[:1]},
             {"name": "Direction", "uses": design[1:3]},
             {"name": "Build & QA", "uses": design[:2]},
         ]},
    ]
    for w in workflows:
        w.setdefault("description", w["summary"]); w.setdefault("best_use", ""); w.setdefault("watch_outs", "")
        w.setdefault("command", ""); w.setdefault("depends_on", []); w.setdefault("references", []); w.setdefault("enabled_in", [])
        used = []
        for st in w["steps"]:
            for nm in st["uses"]:
                used.append(nm)
                if nm in by_name and w["title"] not in by_name[nm]["used_by"]:
                    by_name[nm]["used_by"].append(w["title"])
        w["uses_list"] = sorted(set(used))
        items.append(w)

    # --- References / templates / tools ---
    refs = [
        ("slide-layout-patterns", "Slide Layout Patterns", "Presentations & Diagrams", "Approved slide layouts and when to use each."),
        ("chart-patterns", "Chart Patterns", "Data Visualization", "Chart types mapped to the insight they communicate best."),
        ("design-tokens", "Design Tokens", "Design & Frontend", "The canonical palette, type, spacing and motion (see DESIGN.md)."),
        ("persona-library", "Persona Library", "Research", "Reusable proto-personas for discovery and messaging."),
    ]
    for nm, tt, c, d in refs:
        items.append({"id": f"reference:{nm}", "name": nm, "title": tt, "kind": "reference", "category": c,
                      "summary": d, "description": d, "best_use": "", "watch_outs": "", "command": "",
                      "source": {"type": "local", "label": "this repo"}, "status": "installed",
                      "date_added": "2026-09-18", "date_updated": "2026-09-18",
                      "depends_on": [], "used_by": [], "references": [], "enabled_in": []})
    tools = [
        ("ai-lib", "ai-lib Installer", "agent-tools", "Classifies and routes external sources into the library."),
        ("skills-db", "Skills Catalog", "agent-tools", "Generates the searchable Library index."),
        ("library-add", "Add to Library", "agent-tools", "The single add-path (/add-to-library)."),
    ]
    for nm, tt, c, d in tools:
        items.append({"id": f"tool:{nm}", "name": nm, "title": tt, "kind": "tool", "category": c,
                      "summary": d, "description": d, "best_use": "", "watch_outs": "", "command": "",
                      "source": {"type": "local", "label": "this repo"}, "status": "installed",
                      "date_added": "2026-09-18", "date_updated": "2026-09-18",
                      "depends_on": [], "used_by": [], "references": [], "enabled_in": []})

    # A couple of illustrative dependencies/references/enabled-in on hero skills
    hero = pres[0] if pres else (items[0]["name"])
    if hero in by_name:
        by_name[hero]["depends_on"] = design[:2]
        by_name[hero]["references"] = ["Slide Layout Patterns", "Design Tokens"]
        by_name[hero]["enabled_in"] = ["Advertiser Experience Deck", "Q4 Launch"]

    projects = [
        {"id": "advertiser-deck", "name": "Advertiser Experience Deck",
         "skills": pres + design[:1], "workflows": ["Build Executive Presentation"],
         "references": ["Slide Layout Patterns", "Chart Patterns"],
         "integrations": {"Cursor": "synced", "Claude Code": "synced", "Codex": "not synced"}},
        {"id": "q4-launch", "name": "Q4 Launch",
         "skills": prod, "workflows": ["Build Executive Presentation"],
         "references": ["Persona Library"],
         "integrations": {"Cursor": "synced", "Claude Code": "not synced", "Codex": "not synced"}},
    ]
    for p in projects:
        for nm in p["skills"]:
            if nm in by_name and p["name"] not in by_name[nm]["enabled_in"]:
                by_name[nm]["enabled_in"].append(p["name"])

    integrations = [
        {"id": "cursor", "name": "Cursor", "status": "connected", "count": sum(1 for i in items if i["kind"] == "skill"), "last_synced": "12 min ago"},
        {"id": "claude-code", "name": "Claude Code", "status": "connected", "count": 28, "last_synced": "yesterday"},
        {"id": "codex", "name": "Codex", "status": "not configured", "count": 0, "last_synced": None},
    ]
    inbox = [
        {"name": "animation-patterns", "detected": "reference", "category": "Presentations & Diagrams",
         "reason": "Could also be classified as a Skill", "source": "github.com/example/motion"},
        {"name": "deck-linting", "detected": "prompt", "category": "Presentations & Diagrams",
         "reason": "Low category confidence", "source": "pasted"},
    ]
    updates = [
        {"name": pres[0] if pres else "presentation-design", "kind": "skill", "note": "Source has changed", "has_local": True},
        {"name": "chart-patterns", "kind": "reference", "note": "2 files updated upstream", "has_local": False},
    ]
    health = {
        "ok": ["Registry healthy", "Integrations connected", "References resolved"],
        "issues": [
            {"type": "Broken reference", "detail": f"{title_of(pres[0]) if pres else 'A skill'} → old-layout-patterns"},
            {"type": "Duplicate candidate", "detail": "Visual QA / Presentation QA"},
        ],
    }
    activity = [
        {"action": "Installed", "target": "Add to Library", "when": "just now"},
        {"action": "Updated", "target": workflows[0]["title"], "when": "15 min ago"},
        {"action": "Enabled", "target": f"{title_of(prod[0]) if prod else 'a skill'} · Q4 Launch", "when": "1 h ago"},
        {"action": "Classification changed", "target": "deck-linting → Prompt", "when": "2 h ago"},
    ]

    counts = {}
    for i in items:
        counts[i["kind"]] = counts.get(i["kind"], 0) + 1
    collections = {}
    for i in items:
        collections[i["category"]] = collections.get(i["category"], 0) + 1
    collections = [{"name": k, "count": v} for k, v in sorted(collections.items(), key=lambda x: -x[1]) if k != "Uncategorized"]

    data = {
        "generated": "library-ui/build-data.py",
        "items": items, "counts": counts, "collections": collections,
        "projects": projects, "integrations": integrations, "inbox": inbox,
        "updates": updates, "health": health, "activity": activity,
    }
    OUT.write_text("window.LIBRARY_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} — {len(items)} items ({counts})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
