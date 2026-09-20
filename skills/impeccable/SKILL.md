---
name: install-impeccable
description: Installs the Impeccable frontend-design skill for Cursor (npx impeccable install, ZIP from impeccable.style, or copy from pbakaus/impeccable). Use when the user wants Impeccable, impeccable.style, /impeccable, frontend design skills, or to remove AI UI slop.
---

# Install Impeccable

Do not vendor Impeccable into work-kit. Use the official installer so Cursor gets the Cursor-specific build, commands, and design hook.

Requires Node.js 22.18+. Docs: [impeccable.style](https://impeccable.style) · [getting started](https://impeccable.style/tutorials/getting-started) · [GitHub](https://github.com/pbakaus/impeccable)

## Cursor, all projects (preferred)

From any directory on the user's machine:

```bash
npx impeccable install --providers=cursor --scope=global
```

Interactive equivalent: `npx impeccable install`, keep **Cursor**, choose **global**.

That writes the Cursor build into the user skill dir (`~/.cursor/skills/`). Then:

1. Command Palette → **Developer: Reload Window**
2. Type `/impeccable` in Agent chat. Autocomplete should list commands.
3. In each product repo, run `/impeccable init` once (writes `PRODUCT.md`; may offer `DESIGN.md`).

Update later: `npx impeccable update`

## Cursor, this project only

From the app repo root (not this work-kit repo unless it is a UI app):

```bash
npx impeccable install --providers=cursor --scope=project
```

Writes `.cursor/skills/impeccable/` and, when accepted, `.cursor/hooks.json` for the design detector. Reload Cursor. Allow the hook if the harness prompts.

## Website ZIP ([#downloads](https://impeccable.style/#downloads))

1. On impeccable.style, choose the **Cursor** / impeccable tab (not Claude marketplace, not `skills.sh`).
2. Download the Cursor ZIP.
3. Extract at the project root so `.cursor/skills/` appears:

```bash
cd your-project
unzip ~/Downloads/impeccable-cursor.zip -d .
ls .cursor/skills/
```

4. Reload Cursor. Confirm `/impeccable`.

## Other official methods (usually worse for Cursor)

| Method | When |
| --- | --- |
| `npx skills add pbakaus/impeccable` | Shared generic skill, not the Cursor-tuned build. Prefer `npx impeccable install`. |
| `/plugin marketplace add pbakaus/impeccable` | Claude Code only |
| `cp -r dist/cursor/.cursor your-project/` | After cloning [pbakaus/impeccable](https://github.com/pbakaus/impeccable); last resort |
| Git submodule + `npx impeccable link --source=... --providers=cursor` | Teams that vendor a pinned copy |

## After install

```
/impeccable init
/impeccable polish <page>
/impeccable critique <page>
/impeccable audit <page>
```

Pin a shortcut with `/impeccable pin audit` if they want `/audit`.

If `/impeccable` is missing: reload, confirm files exist under `~/.cursor/skills/impeccable` (global) or `.cursor/skills/impeccable` (project), rerun the installer with `--providers=cursor`. Nightly / "Agent Skills" toggles from older docs are obsolete on current Cursor.

## Guardrails

- Do not copy Impeccable's skill tree into work-kit.
- Do not install into work-kit unless this repo is the UI they want designed.
- Do not run `npx impeccable install` without `--providers` / `--scope` if the user already said they want Cursor + global.
