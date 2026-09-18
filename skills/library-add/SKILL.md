---
name: library-add
description: Classify and save a prompt, skill, or rule into the cursor-skills library. Use when the user wants to add something to the library, says save this as a skill or prompt, or worries about putting it in the wrong place.
disable-model-invocation: true
---

# Library add

One door into [Ses2905/cursor-skills](https://github.com/Ses2905/cursor-skills). Do not invent a second plugin or dump packs into `~/.cursor/skills` by hand.

Read `prompts/SKILL-VS-PROMPT.md` first.

## Classify

| Kind | Where | When |
| --- | --- | --- |
| **prompt** | `prompts/commands/<name>.md` | One-shot ask / template fill; user would paste it into a blank chat |
| **skill** | `skills/<name>/SKILL.md` | Multi-step playbook, tools, scripts, or "whenever this work happens" |
| **rule** | `rules/<name>.mdc` | Short always-on constraint |

If unsure, run:

```bash
./scripts/library-add.py sort --stdin <<'EOF'
…pasted text…
EOF
```

## Add

**Prompt**

```bash
./scripts/library-add.py prompt --name kebab-name --theme product --file path.md
# themes: product | writing | research | strategy | engineering | personal
```

**Skill**

```bash
./scripts/library-add.py skill --name kebab-name --file path/to/SKILL.md
# workshops / on-demand only:
./scripts/library-add.py skill --name kebab-name --file path.md --slash-only
```

**Rule**

```bash
./scripts/library-add.py rule --name kebab-name --file path.mdc --always
```

The script updates `prompts/INDEX.md` and/or the skills database, then runs `./scripts/install-local.sh` (installs **Work Kit** and **Prompt Kit**).

## Guardrails

- Never create a third plugin for a one-off pack. Prefer Prompt Kit or Work Kit.
- Never bulk-copy hundreds of `SKILL.md` files into `~/.cursor/skills`.
- Never wrap a one-shot prompt as a `SKILL.md` "to be safe."
- Keep the user's wording when they paste a prompt; only add required frontmatter.
- After install, tell the user: **Developer: Reload Window**, then invoke `/name`.

## After writing

Confirm the new path, show the invoke form (`/name`), and stop.
