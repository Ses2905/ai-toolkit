---
name: install-work-kit
description: Install this personal Cursor plugin at user scope, copy skills for Cloud Agent sync, and recommend marketplace plugins. Use when the user asks how to install work-kit, set up plugins globally, or leverage skills across all projects.
---

# Install work-kit

## Local plugin (every desktop project)

From the work-kit repo:

```bash
./scripts/install-local.sh
```

That copies this plugin to `~/.cursor/plugins/local/work-kit` as a real directory (not a symlink). Then:

1. Command Palette → **Developer: Reload Window**
2. Open **Customize**, filter **User**, confirm **Work Kit**
3. Skills appear under **Agent Decides**; invoke with `/plan-the-work`, `/debug-from-evidence`, `/review-the-diff`, `/ship-the-change`, `/capture-a-skill`, `/install-impeccable`, `/install-github-skills`

On Teams/Enterprise, local plugins require **Allow Local Plugin Imports**.

## Cloud Agents

`~/.cursor/plugins/local` is not available on cloud VMs. To reuse the skills there:

```bash
./scripts/sync-user-skills.sh
```

Then **Settings → Agents → Context and Tools → Sync Skills for Cloud Agents**.

Repo-specific knowledge still belongs in that repo (`AGENTS.md`, `.cursor/rules`, `.cursor/skills`).

## GitHub catalogs

```bash
./scripts/install-catalog-skills.sh --preset design-product
```

See `skills/install-github-skills/SKILL.md`.

## Marketplace plugins

Install these at **user** scope from **Customize → Install**, not project scope. See `STARTER_PLUGINS.md`.
