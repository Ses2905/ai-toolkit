---
name: capture-a-skill
description: Turn a repeated workflow into a Cursor skill, rule, or command. Use when the user wants to save a workflow, says this should be a skill, or notices the same instructions repeating across projects.
---

# Capture a skill

Prefer `/add-to-library` (or `skills/library-add/SKILL.md`) for anything new. This skill is the skill-only path.

Save durable workflow as files the agent can reuse, not as chat memory.

## Choose the component

| Need | Put it here |
| --- | --- |
| Multi-step workflow the agent should follow when relevant | `skills/<name>/SKILL.md` via `./scripts/library-add.py skill …` |
| One-shot reusable ask, rewrite, or template fill | **Prompt Kit** via `./scripts/library-add.py prompt …` |
| Short always-on constraint | `rules/<name>.mdc` via `./scripts/library-add.py rule …` |
| Explicit slash action that launches a skill here | `commands/<name>.md` (use `--with-command` / `--slash-only`) |
| Repo-only knowledge | that repo's `.cursor/skills` or `AGENTS.md` |

If the user pastes something they would send as a chat message, stop and save it as a **prompt**. Do not wrap it as a `SKILL.md`.

## Skill file

```markdown
---
name: kebab-case-name
description: What it does and when to use it. Include trigger phrases.
---

# Title

## When to use
## Workflow
## Guardrails
```

`name` must match the folder name. Keep `SKILL.md` short; move long reference material to `references/`.

## Where to write

- Editing **work-kit**: use `./scripts/library-add.py` so indexes and both plugins stay in sync, then re-run `scripts/install-local.sh`.
- One-off personal skill (no plugin bump): `~/.cursor/skills/<name>/SKILL.md` — avoid unless temporary.
- Cloud Agents: `./scripts/sync-user-skills.sh` then **Settings → Agents → Sync Skills for Cloud Agents**.

## After writing

Tell the user to **Developer: Reload Window**, then confirm the skill in **Customize → Skills**.
