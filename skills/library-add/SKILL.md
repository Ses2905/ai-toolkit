---
name: library-add
type: skill
category: agent-tools
disable-model-invocation: true
description: >-
  The single add-path for this repo's library. Use when the user pastes a
  prompt/skill/workflow (or says "add this to the library", "/add-to-library",
  "save this as a skill/prompt"). Classifies the content and routes it to Work
  Kit (skills/) or Prompt Kit (prompts/) correctly, then refreshes catalogs.
references:
  - ../../LIBRARY.md
  - ../../tools/ai-lib/README.md
---

# Library Add

## Purpose
Add one pasted item (or a file) to the library at the right level, so the
library stays modular instead of everything landing in `skills/`.

## Activate When
- The user pastes content and asks to save/add it to the library.
- The user runs `/add-to-library` or says "make this a skill/prompt/workflow".

## Do Not Activate When
- Installing a whole external repo, zip, or GitHub URL → use
  `tools/ai-lib/ai-lib install <source>` instead.
- The user only wants feedback on the content, not to save it.

## Required Context
- `LIBRARY.md` — the prompt/skill/workflow/global model.
- The pasted content itself (and, if given, a preferred name/category).

## Process
1. Read the pasted text (or `--file`).
2. Classify it (skill / prompt / workflow / reference / template). If unsure,
   ask the user which it is rather than guessing.
3. Run the router:
   ```bash
   ./scripts/library-add.py --file <path>        # or --stdin, or inline text
   ./scripts/library-add.py --dry-run --file <path>   # preview first
   ```
4. For a skill, refresh the catalog: `./scripts/skills-db.sh build`.

## Decision Rules
- IF it's a reusable capability / quality bar that should auto-apply → **skill**
  (`skills/<name>/SKILL.md`, Work Kit).
- IF it's a one-off, input-driven task → **prompt**
  (`prompts/commands/<name>.md`, Prompt Kit).
- IF it's an ordered multi-step process → **workflow** (`workflows/<name>/`).
- IF it's supporting knowledge/examples → **reference**; a starting artifact →
  **template**.
- IF a capability would duplicate an existing skill → keep the skill canonical
  and make the prompt a thin invoker (see the PM commands for the pattern).

## Output Requirements
The item written to its correct path with front-matter (`name`, `type`,
`category`, `description`), normalized to `lowercase-kebab-case`.

## Definition of Done
- File exists at the routed destination; no existing file was overwritten.
- Skills catalog rebuilt when a skill was added.
- The item is discoverable (`./scripts/skills-db.sh find` or
  `tools/ai-lib/ai-lib search`).

## References
See `LIBRARY.md` for the model and `tools/ai-lib/README.md` for installing
whole external sources.
