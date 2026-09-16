# Work Kit

A personal Cursor plugin for **every** project: plan first, debug from evidence, review the real diff, ship a clean commit, and save repeated workflows as skills.

Install it once at **user** scope. Do not copy these files into each repo.

## Install (desktop)

From this directory:

```bash
chmod +x scripts/*.sh
./scripts/install-local.sh
```

That copies a real folder to `~/.cursor/plugins/local/work-kit` (Cursor ignores symlinks that point outside that directory). Then:

1. Command Palette → **Developer: Reload Window**
2. Open **Customize**, filter **User**, confirm **Work Kit**
3. Invoke skills with `/plan-the-work`, `/debug-from-evidence`, `/review-the-diff`, `/ship-the-change`, `/capture-a-skill`
4. Slash commands: `/plan`, `/debug`, `/review-diff`, `/ship`, `/new-skill`

On Teams/Enterprise, admins must allow **Dashboard → Settings → Security & Identity → Marketplace and Plugins → Allow Local Plugin Imports**.

After you edit this repo, run `./scripts/install-local.sh` again and reload.

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
| Skill | `plan-the-work` | Before non-trivial implementation |
| Skill | `debug-from-evidence` | Something is broken |
| Skill | `review-the-diff` | After a sizable change, or before merge |
| Skill | `ship-the-change` | Commit and push |
| Skill | `capture-a-skill` | Save a repeated workflow |
| Skill | `install-work-kit` | Reinstall or explain setup |
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
├── rules/
├── skills/
├── agents/
├── commands/
├── scripts/
└── assets/logo.svg
```
