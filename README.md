# Work Kit

A personal Cursor plugin for **every** project: plan first, debug from evidence, review the real diff, ship a clean commit, and save repeated workflows as skills.

Public GitHub home: **[github.com/Ses2905/cursor-skills](https://github.com/Ses2905/cursor-skills)**.

Install it once at **user** scope. Do not copy these files into each repo.

## Install from GitHub (desktop skill library)

```bash
git clone https://github.com/Ses2905/cursor-skills.git
cd cursor-skills
chmod +x scripts/*.sh
./scripts/install-local.sh
./scripts/sync-user-skills.sh
```

That copies the plugin to `~/.cursor/plugins/local/work-kit` and every `skills/*/SKILL.md` folder into `~/.cursor/skills/` (Cursor's skill library). Then:

1. Command Palette → **Developer: Reload Window**
2. Open **Customize**, filter **User**, confirm **Work Kit**
3. **Settings → Agents → Context and Tools → Sync Skills for Cloud Agents**

Or copy only the skill folders with the skills CLI:

```bash
npx skills add https://github.com/Ses2905/cursor-skills
```

## Install from this directory

If you already have the repo checked out:

```bash
chmod +x scripts/*.sh
./scripts/install-local.sh
```

That copies a real folder to `~/.cursor/plugins/local/work-kit` (Cursor ignores symlinks that point outside that directory). Then:

1. Command Palette → **Developer: Reload Window**
2. Open **Customize**, filter **User**, confirm **Work Kit**
3. Invoke skills with `/plan-the-work`, `/debug-from-evidence`, `/review-the-diff`, `/ship-the-change`, `/capture-a-skill`, `/handoff`, `/install-impeccable`, `/install-github-skills`, `/install-open-design`, `/web-design-guidelines`, `/react-bits`, `/high-end-visual-design`, `/lark-slides`, `/slides`, `/frontend-slides-editable`, `/html-ppt`, `/product-strategy-session`, `/html-diagram`, `/hyperframes-animation`, `/remotion-best-practices`, `/review-animations`, `/improve-animations`, `/find-animation-opportunities`
4. Slash commands: `/plan`, `/debug`, `/review-diff`, `/ship`, `/new-skill`, `/handoff`, `/install-impeccable`, `/install-github-skills`, `/install-open-design`, `/web-design-guidelines`, `/react-bits`, `/high-end-visual-design`, `/lark-slides`, `/slides`, `/frontend-slides-editable`, `/html-ppt`, `/product-strategy-session`, `/html-diagram`, `/hyperframes-animation`, `/remotion-best-practices`, `/review-animations`, `/improve-animations`, `/find-animation-opportunities`

On Teams/Enterprise, admins must allow **Dashboard → Settings → Security & Identity → Marketplace and Plugins → Allow Local Plugin Imports**.

After you edit this repo, run `./scripts/install-local.sh` again and reload.

## Publish to GitHub

```bash
./scripts/publish-to-github.sh
```

Pushes `main` to [Ses2905/cursor-skills](https://github.com/Ses2905/cursor-skills). Needs write access: Cursor **Dashboard → Integrations → Connect GitHub** (grant `Ses2905/cursor-skills`), or a `GH_TOKEN` / `GITHUB_TOKEN` with `repo` scope.

## GitHub skill catalogs

[awesome-cursor-skills](https://github.com/spencerpauly/awesome-cursor-skills) is a list, not a plugin. This repo pulls a curated preset into `~/.cursor/skills/`:

```bash
./scripts/install-catalog-skills.sh --preset design-product
```

That installs design-system, visual QA, motion, presentation, copy, and product-shaping skills. Details: `skills/install-github-skills/SKILL.md`. List first with `--list`.

## Cloud Agents

Cloud VMs do not see `~/.cursor/plugins/local`. To reuse the skills there:

```bash
./scripts/sync-user-skills.sh
```

Then **Settings → Agents → Context and Tools → Sync Skills for Cloud Agents**.

Keep repo-specific knowledge in that repo (`AGENTS.md`, `.cursor/rules`, `.cursor/skills`).

## What you get

| Kind | Name | When |
| --- | --- | --- |
| Rule | `verify-before-done` | Always — prove it works before claiming done |
| Rule | `tight-diffs` | Always — change only what the task needs |
| Rule | `apple-design` | UI/motion files only — Apple-style fluid interfaces |
| Skill | `apple-design` | Gesture UI, springs, sheets, materials, type |
| Skill | `taste-skill` | Anti-slop landing pages, portfolios, demos, redesigns |
| Rule | `taste-skill` | Agent-decides — marketing/frontend taste, not dashboards |
| Skill | `high-end-visual-design` | Agency-tier Double-Bezel UI, premium type, custom motion |
| Rule | `high-end-visual-design` | Agent-decides — expensive marketing UI, not dashboards |
| Skill | `frontend-design` | Distinctive UI, type, and visual direction (not templates) |
| Rule | `frontend-design` | Agent-decides — new or reshaped product UI |
| Skill | `canvas-design` | Posters, PNG/PDF art from a design philosophy |
| Rule | `canvas-design` | Agent-decides — static visual art, not product UI |
| Skill | `web-design-guidelines` | Review UI for guidelines, UX, a11y, interaction |
| Rule | `web-design-guidelines` | Agent-decides — UI review, not backend |
| Skill | `react-bits` | Animated React components from reactbits.dev |
| Rule | `react-bits` | Agent-decides — React UI flourishes only |
| Skill | `plan-the-work` | Before non-trivial implementation |
| Skill | `debug-from-evidence` | Something is broken |
| Skill | `review-the-diff` | After a sizable change, or before merge |
| Skill | `ship-the-change` | Commit and push |
| Skill | `capture-a-skill` | Save a repeated workflow |
| Skill | `handoff` | Compact the conversation into a portable PM handoff document |
| Rule | `handoff` | Agent-decides — session handoff to another agent; not a durable skill |
| Skill | `install-work-kit` | Reinstall or explain setup |
| Skill | `install-impeccable` | Install Impeccable globally for Cursor |
| Skill | `install-github-skills` | Pull the design-product preset from GitHub catalogs |
| Skill | `install-open-design` | Install Open Design from GitHub Releases + Cursor MCP |
| Skill | `lark-slides` | Create/edit Lark Feishu slides via lark-cli XML |
| Rule | `lark-slides` | Agent-decides — Feishu slides only, needs lark-cli |
| Skill | `slides` | HTML pitch decks with Chart.js, tokens, copy formulas (ckmslides) |
| Rule | `slides` | Agent-decides — HTML presentations, not Feishu or PPTX |
| Skill | `design-system` | Token CSVs and `search-slides.py` sibling for `/slides` |
| Skill | `frontend-slides-editable` | Single-file HTML decks with a built-in browser editor |
| Rule | `frontend-slides-editable` | Agent-decides — editable HTML decks, not Feishu or Chart.js slides |
| Skill | `html-ppt` | Themed static HTML presentations (36 themes, keyboard runtime) |
| Rule | `html-ppt` | Agent-decides — html-ppt templates, not Chart.js or Feishu |
| Skill | `product-strategy-session` | End-to-end PM strategy: positioning → discovery → roadmap |
| Rule | `product-strategy-session` | Agent-decides — product strategy sessions, not implementation |
| Skill | `html-diagram` | Self-contained HTML diagrams (topology, sequence, state, hierarchy) |
| Rule | `html-diagram` | Agent-decides — explicit diagram requests, not general UI |
| Skill | `design-artifact` | Visual register sibling for Effective HTML artifacts |
| Skill | `hyperframes-animation` | GSAP motion rules, blueprints, and HyperFrames adapters |
| Rule | `hyperframes-animation` | Agent-decides — HyperFrames/GSAP motion, not generic UI |
| Skill | `hyperframes-core` | Composition contract sibling for `/hyperframes-animation` |
| Skill | `remotion-best-practices` | Router for Remotion React video skills |
| Rule | `remotion-best-practices` | Agent-decides — Remotion video, not HyperFrames or web UI |
| Skill | `review-animations` | Review motion code against Emil Kowalski's craft bar |
| Rule | `review-animations` | Agent-decides — animation review only, not general diffs |
| Skill | `improve-animations` | Audit motion across a codebase, then write execution plans |
| Rule | `improve-animations` | Agent-decides — animation audit/plans; does not implement |
| Skill | `find-animation-opportunities` | Find missing motion; reject what should stay still |
| Rule | `find-animation-opportunities` | Agent-decides — opportunity search only; does not implement |
| Agent | `reviewer` / `debugger` | Dedicated review or debug pass |

## Marketplace plugins (user scope)

Install these from **Customize → Install → user**, not project. See [STARTER_PLUGINS.md](STARTER_PLUGINS.md).

Start with:

1. [Continual Learning](https://cursor.com/marketplace/cursor/continual-learning) — writes durable facts into `AGENTS.md`
2. [Create Plugin](https://cursor.com/marketplace/cursor/create-plugin) — scaffold and validate more plugins
3. Product plugins you already use (Linear, Figma, Notion, GitHub, Playwright)

## User Rules vs this plugin

Put short communication preferences in **Customize → Rules** (account-level, syncs with your login). Put workflows here. Put codebase facts in the repo.

## Layout

```text
work-kit/
├── .cursor-plugin/plugin.json
├── catalog/presets.json
├── rules/
├── skills/
├── agents/
├── commands/
├── scripts/
└── assets/logo.svg
```
