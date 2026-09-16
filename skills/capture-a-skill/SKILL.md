---
name: capture-a-skill
description: Turn a repeated workflow into a Cursor skill, rule, or command. Use when the user wants to save a workflow, says this should be a skill, or notices the same instructions repeating across projects.
---

# Capture a skill

Save durable workflow as files the agent can reuse, not as chat memory.

## Choose the component

| Need | Put it here |
| --- | --- |
| Multi-step workflow the agent should follow when relevant | `skills/<name>/SKILL.md` |
| Short always-on constraint | `rules/<name>.mdc` with `alwaysApply: true` |
| Explicit slash action | `commands/<name>.md` |
| Repo-only knowledge | that repo's `.cursor/skills` or `AGENTS.md` |

Default for personal, cross-project workflows: this plugin under `skills/`.

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

- Editing **work-kit**: add the file here, then re-run `scripts/install-local.sh` so `~/.cursor/plugins/local/work-kit` stays in sync.
- One-off personal skill (no plugin bump): `~/.cursor/skills/<name>/SKILL.md`
- Cloud Agents: copy or keep skills in `~/.cursor/skills/` and enable **Settings → Agents → Sync Skills for Cloud Agents**. Local plugin folders do not sync to cloud VMs.

## After writing

Tell the user to **Developer: Reload Window**, then confirm the skill in **Customize → Skills**.
