---
name: install-github-skills
description: Pulls selected Agent Skills from GitHub catalogs (default spencerpauly/awesome-cursor-skills plus Anthropic, Vercel, and Matt Pocock sources) into ~/.cursor/skills. Use when the user asks to install awesome-cursor-skills, copy SKILL.md folders from GitHub, or add design, motion, presentation, or product-management skills.
disable-model-invocation: true
---

# Install skills from GitHub

Catalogs like [awesome-cursor-skills](https://github.com/spencerpauly/awesome-cursor-skills) are **lists**, not a Cursor marketplace plugin. Cursor does not auto-import them. This repo's installer clones the sources and copies each skill folder (the directory that contains `SKILL.md`) into `~/.cursor/skills/`.

Do not copy the whole awesome-list repo into the skills directory. Do not write into `~/.cursor/skills-cursor/`.

## Default: design / visuals / product

From this work-kit repo:

```bash
./scripts/install-catalog-skills.sh --preset design-product
```

Then **Developer: Reload Window**. Confirm in **Customize → Skills**.

That preset installs:

| Area | Skills |
| --- | --- |
| Design system & UI | `using-ui-stack`, `frontend-design`, `web-design-guidelines`, `converting-css-to-tailwind`, `taste-skill`, `high-end-visual-design` |
| Visual QA | `visual-qa-testing`, `verifying-in-browser`, `responsive-testing`, `dark-mode-testing`, `accessibility-auditing`, `screenshotting-changelog`, `comparing-branches-visually` |
| Motion | `react-view-transitions`, `hyperframes-animation`, `remotion-best-practices`, `review-animations`, `improve-animations`, `find-animation-opportunities` |
| Images & art | `generating-images`, `exporting-to-png`, `canvas-design`, `theme-factory`, `brand-guidelines`, `html-diagram` |
| Presentation / docs | `pptx`, `pdf`, `docx`, `verifying-markdown-formatting`, `writing-guidelines`, `slides`, `design-system`, `frontend-slides-editable`, `html-ppt` |
| Product | `writing-copy`, `grill-me`, `grilling`, `to-tickets`, `product-strategy-session`, `pm-handoff` |

Sources and the full mapping live in [catalog/presets.json](../../catalog/presets.json).

## Other invocations

```bash
# list what a preset would install
./scripts/install-catalog-skills.sh --preset design-product --list

# one or more names from that preset
./scripts/install-catalog-skills.sh --preset design-product --only writing-copy,frontend-design,pptx

# every local skill under awesome-cursor-skills/resources (noisy)
./scripts/install-catalog-skills.sh --preset all-awesome

# Lark/Feishu slides (needs @larksuite/cli + login)
./scripts/install-catalog-skills.sh --preset lark

# HTML Chart.js decks (skills.sh ckmslides → --skill slides)
./scripts/install-catalog-skills.sh --preset slides

# Editable single-file HTML decks (skills.sh frontend-slides-editable)
./scripts/install-catalog-skills.sh --preset frontend-slides-editable

# Themed static HTML PPT (skills.sh html-ppt)
./scripts/install-catalog-skills.sh --preset html-ppt

# Product strategy session + orchestrated Dean Peters siblings (CC BY-NC-SA 4.0)
./scripts/install-catalog-skills.sh --preset product-strategy-session

# Self-contained HTML diagrams (plannotator/effective-html html-diagram)
./scripts/install-catalog-skills.sh --preset html-diagram

# HyperFrames GSAP motion (heygen-com/hyperframes hyperframes-animation)
./scripts/install-catalog-skills.sh --preset hyperframes-animation

# Remotion React video best-practices router
./scripts/install-catalog-skills.sh --preset remotion-best-practices

# Emil Kowalski animation review
./scripts/install-catalog-skills.sh --preset review-animations

# Emil Kowalski animation audit-then-plan (includes review-animations sibling)
./scripts/install-catalog-skills.sh --preset improve-animations

# Emil Kowalski missing-motion finder
./scripts/install-catalog-skills.sh --preset find-animation-opportunities

# Matt Pocock conversation handoff (upstream skill name: handoff)
./scripts/install-catalog-skills.sh --preset pm-handoff
```

Installs go to `~/.cursor/skills/<skill-name>/` unless `--dest` is set.

## After install

- Desktop: Reload Window, then use `/using-ui-stack`, `/frontend-design`, `/writing-copy`, `/pptx`, `/grill-me`, and the rest.
- Cloud Agents: **Settings → Agents → Sync Skills for Cloud Agents** (only `~/.cursor/skills/` syncs).
- Polished Cursor UI kit: still run `/install-impeccable` (`npx impeccable install --providers=cursor --scope=global`). That is a different installer, not a folder copy from the awesome list.

## Manual copy (no script)

```bash
git clone --depth 1 https://github.com/spencerpauly/awesome-cursor-skills.git /tmp/awesome-cursor-skills
mkdir -p ~/.cursor/skills
cp -R /tmp/awesome-cursor-skills/resources/<skill-name> ~/.cursor/skills/<skill-name>
```

The destination folder name must match the `name` frontmatter in `SKILL.md`.

## Project-only

Copy into that repo's `.cursor/skills/<skill-name>/` and commit it. Do not vendor catalog skills into work-kit unless the user asked to pin them here.

## Do not commit Playground dumps

`npx skills add` from [AI UX Playground](https://aiuxplayground.com) copies into `.agents/skills/` and writes `skills-lock.json`. That is a local leftover, not the plugin catalog. Work Kit vendors chosen skills under `skills/<name>/`. `.agents/` and `skills-lock.json` are gitignored. Do not keep a second copy of taste (`gpt-taste`) next to `skills/taste-skill`.
