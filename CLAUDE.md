# CLAUDE.md — tool operating guide

Agent-facing entry points for this library. (See `AGENTS.md` for conventions and
`LIBRARY.md` for the prompt/skill/workflow model.)

## Entry points

| Area | Path |
| --- | --- |
| Global instructions | `AGENTS.md`, `DESIGN.md`, this file |
| Skills | `skills/<name>/SKILL.md` |
| Prompts | `prompts/<domain>/` |
| Workflows | `workflows/<name>/` |
| Schemas/templates | `references/schemas/` |
| Design tokens | `design-system/tokens.css` |
| Skills catalog app | `skills-database.html` (gen: `scripts/skills_db.py`) |
| Library installer | `tools/ai-lib/` |

## Commands

```bash
# Skills catalog (search / browse / rank) — interactive app + static build
./scripts/skills-db.sh serve          # http://127.0.0.1:8765
./scripts/skills-db.sh find <query>
./scripts/skills-db.sh build          # regenerate SKILLS.md + skills-database.html

# Library installer / librarian
tools/ai-lib/ai-lib inspect <source>          # classify + routing plan
tools/ai-lib/ai-lib install <source> --dry-run
tools/ai-lib/ai-lib install <source> --yes
tools/ai-lib/ai-lib list [type] [--category X]
tools/ai-lib/ai-lib search <query>
tools/ai-lib/ai-lib doctor
tools/ai-lib/ai-lib reindex

# Tests
python3 scripts/skills_db_test.py
python3 tools/ai-lib/ai_lib_test.py
```

## Notes

- Prefer semantic design tokens (see `DESIGN.md`); never hard-code colors/type.
- Regenerate derived artifacts (skills catalog, library `INDEX.md`) after edits.
- Licensed commercial fonts are git-ignored; the committed brand fonts are OFL.
