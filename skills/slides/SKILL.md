---
name: slides
description: Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. Use for marketing presentations, pitch decks, Chart.js slides, ckmslides, or HTML slide decks. Distinct from Lark/Feishu slides.
argument-hint: "[topic] [slide-count]"
metadata:
  author: claudekit
  version: "1.0.0"
---

# Slides

Pinned from [nextlevelbuilder/ui-ux-pro-max-skill `slides`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/15de38fb70bc80ae9276fa7703b48ae861a672e6/cli/assets/skills/slides) at `15de38fb70bc80ae9276fa7703b48ae861a672e6` (MIT). skills.sh listing: [ckmslides](https://www.skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ckmslides). Official CLI: `npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill slides`. Sibling: `skills/design-system` (`../design-system/scripts/search-slides.py`). Provenance: `skills/slides/SOURCE.txt`.

**In this repo:** `skills/slides/SKILL.md` plus `references/`. Scoped rule: `rules/slides.mdc` (`alwaysApply: false`). User install: `~/.cursor/skills/slides/` via `./scripts/install-local.sh` then `./scripts/sync-user-skills.sh`. Invoke with `/slides`. Distinct from `/lark-slides` (Feishu XML).

Do not apply to Feishu/Lark decks, generic PPTX export (use Anthropic `pptx`), product UI, or backend work. Do not scrape Pexels/Unsplash or download stock photos unless the user asked. Prefer Chart.js CDN `4.4.1` and CSS variables from project tokens; if `assets/design-tokens.css` is missing, generate from `../design-system/templates/design-tokens-starter.json` rather than hardcoding hex.

Strategic HTML presentation design with data visualization.

## When to Use

- Marketing presentations and pitch decks
- Data-driven slides with Chart.js
- Strategic slide design with layout patterns
- Copywriting-optimized presentation content

## Subcommands

| Subcommand | Description | Reference |
|------------|-------------|-----------|
| `create` | Create strategic presentation slides | `references/create.md` |

## Script Paths

Script paths in this skill and its `references/` are relative to the directory that contains this SKILL.md, not to the project: `scripts/<file>` is this skill's own `scripts/` folder, and `../<skill>/scripts/<file>` is a sibling sub-skill installed alongside it. Build the full path from that directory (Claude Code reports it as the skill's base directory when the skill loads) and keep the working directory at the project root — the scripts read and write project files such as `docs/brand-guidelines.md`, `assets/design-tokens.json` or `src/` relative to it.

In this plugin that directory is `skills/slides/` (user copy: `~/.cursor/skills/slides/`). The required sibling is `../design-system/` (`python3 ../design-system/scripts/search-slides.py`). Run those scripts with cwd at the **project** root, not the skill folder.

## References (Knowledge Base)

| Topic | File |
|-------|------|
| Layout Patterns | `references/layout-patterns.md` |
| HTML Template | `references/html-template.md` |
| Copywriting Formulas | `references/copywriting-formulas.md` |
| Slide Strategies | `references/slide-strategies.md` |

## Routing

1. Parse subcommand from `$ARGUMENTS` (first word)
2. Load corresponding `references/{subcommand}.md`
3. Execute with remaining arguments
