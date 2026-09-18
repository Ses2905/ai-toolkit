---
name: capture-a-prompt
description: Save pasted text as a Cursor slash prompt in Prompt Kit. Use when the user wants to add a prompt to the prompt library, says this should be a prompt, or pastes a reusable instruction to keep.
---

# Capture a prompt

Save a reusable **ask** as a slash command. Do not create a skill.

Read `SKILL-VS-PROMPT.md` before writing. If the dump is a workflow (steps, tools, scripts, "whenever this kind of work happens"), stop and say it belongs in Work Kit via `/new-skill`. Do not write it here.

## Workflow

1. Take the user's pasted text as the prompt body. Keep their wording unless they ask for an edit. Do not wrap it in extra headings they did not include, aside from the required title if missing.
2. Choose:
   - `name`: kebab-case, max 64 chars, matches `commands/<name>.md`
   - `theme`: `product` | `writing` | `research` | `strategy` | `engineering` | `personal`
   - `description`: one line, third person, what + when
3. Write `commands/<name>.md` from this shape:

```markdown
---
name: kebab-case-name
description: What it does and when to use it.
theme: writing
---

# Title

[prompt body]

Treat any text after the slash command as the input. If none was given, ask for it once.
```

4. Add a row to the matching theme table in `INDEX.md`. Replace the `_Empty_` placeholder line if this is the first prompt in that theme.
5. From this repo root run `./scripts/install-local.sh`.
6. Tell the user to **Developer: Reload Window**, then invoke `/<name>`.

## Guardrails

- One prompt = one `commands/<name>.md`. No `SKILL.md`, no `references/`, no scripts.
- Do not copy the prompt into `~/.cursor/skills/`.
- Do not add it to Work Kit.
- Kit commands (`new-prompt`, `sort-skill-or-prompt`) stay in the Kit section of `INDEX.md`, not a theme table.
- If a command with that name exists, ask before overwriting.
