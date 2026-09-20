---
name: install-work-kit
description: Install this personal Cursor plugin at user scope, copy skills for Cloud Agent sync, and recommend marketplace plugins. Use when the user asks how to install work-kit, set up plugins globally, or leverage skills across all projects.
---

# Install work-kit

Public GitHub home: [github.com/Ses2905/cursor-skills](https://github.com/Ses2905/cursor-skills).

## From GitHub (desktop skill library)

```bash
git clone https://github.com/Ses2905/cursor-skills.git
cd cursor-skills
./scripts/install-global.sh
```

That one command installs the local plugin, copies every vendored skill into `~/.cursor/skills/`, installs the Owl-Listener `designer-skills` pack, and deletes the project-local `npx skills add` leftover (`.agents/`, `skills-lock.json`).

The same steps, split out:

```bash
./scripts/install-local.sh
./scripts/sync-user-skills.sh
./scripts/install-catalog-skills.sh --preset designer-skills
rm -rf .agents skills-lock.json
```

Then **Developer: Reload Window**, confirm **Work Kit** under **Customize → User**, and enable **Settings → Agents → Context and Tools → Sync Skills for Cloud Agents**.

Skill folders only:

```bash
npx skills add https://github.com/Ses2905/cursor-skills
```

## Local plugin (every desktop project)

From a checkout of this repo:

```bash
./scripts/install-local.sh
```

That copies this plugin to `~/.cursor/plugins/local/work-kit` as a real directory (not a symlink). Then:

1. Command Palette → **Developer: Reload Window**
2. Open **Customize**, filter **User**, confirm **Work Kit**
3. Skills appear under **Agent Decides**; invoke with `/plan-the-work`, `/debug-from-evidence`, `/review-the-diff`, `/ship-the-change`, `/capture-a-skill`, `/install-impeccable`, `/install-github-skills`, `/install-open-design`, `/react-bits`, `/high-end-visual-design`, `/lark-slides`, `/slides`, `/frontend-slides-editable`, `/html-ppt`, `/product-strategy-session`, `/board-room-strategy`, `/html-diagram`, `/hyperframes-animation`, `/remotion-best-practices`, `/emil-design-eng`, `/review-animations`, `/improve-animations`, `/find-animation-opportunities`, `/pm-handoff`, `/codex-ppt`, `/ppt-master`, `/guizang-ppt-skill`, `/ppt-visual`, `/presentation-art-director`, `/frontend-designer`, `/motion-design`, `/huashu-design`, `/ui-ux-pro-max`, `/rad-spacing`, `/walmart-ads-terminology`

On Teams/Enterprise, local plugins require **Allow Local Plugin Imports**.

## Cloud Agents

`~/.cursor/plugins/local` is not available on cloud VMs. To reuse the skills there:

```bash
./scripts/sync-user-skills.sh
```

Then **Settings → Agents → Context and Tools → Sync Skills for Cloud Agents**.

Repo-specific knowledge still belongs in that repo (`AGENTS.md`, `.cursor/rules`, `.cursor/skills`).

Do not commit `.agents/skills/` or `skills-lock.json`. Playground `npx skills add` dumps there for local use; this plugin's catalog is `skills/`.

## GitHub catalogs

```bash
./scripts/install-catalog-skills.sh --preset design-product
```

See `skills/install-github-skills/SKILL.md`.

## Marketplace plugins

Install these at **user** scope from **Customize → Install**, not project scope. See `STARTER_PLUGINS.md`.
