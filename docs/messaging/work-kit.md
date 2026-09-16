# Messaging framework: Work Kit

**Product:** Work Kit (`work-kit`), personal Cursor plugin
**Job:** Plan first, debug from evidence, review the real diff, ship named files. One install, every project.
**Primary audience:** Avery, solo IC on desktop Cursor
**Secondary audience:** Casey on Cloud Agents. Clone visitors on GitHub.
**Not for:** Teams that need a billed product, a waitlist, or an unscoped skill dump
**Related:** [Comms plan](../launches/q4-2026-first-delivery-comms.md), [Problem statement](../problem-statements/work-kit-first-delivery.md), [PR/FAQ](../launches/q4-2026-first-delivery-prfaq.md), [Positioning](work-kit-positioning.md)
**Source prompt:** [Product messaging framework](https://aiuxplayground.com/prompts/product-messaging-framework) (AI UX Playground)

Use this file as the single source for README, script echo, and teammate paste. If a line disagrees with the one-liner, cut the line.

---

## 1. Core message

**Primary value proposition (1 sentence).** Work Kit is a once-per-machine Cursor plugin that makes the next change planned, verified, and shipped as named files, without copying kit files into each repo.

**Supporting points (benefits, not features).**

- You get a plan you can accept or reject before code moves.
- You get a review of `git diff`, not of intent.
- You get a commit that did not scoop `.env` or leftover notes.
- You install at user scope once. Product repos keep their own `AGENTS.md`.
- Cloud Agents can follow the same loop if you sync skills. Local plugins do not reach cloud VMs.

**Proof points (why believe this).**

- `scripts/install-local.sh` copies a real directory to `~/.cursor/plugins/local/work-kit`. Cursor ignores a symlink into the checkout. That claim is in the script, not a slogan.
- Core skills are named for the job: `plan-the-work`, `debug-from-evidence`, `review-the-diff`, `ship-the-change`, `capture-a-skill`. Slash commands match: `/plan`, `/debug`, `/review-diff`, `/ship`.
- `ship-the-change` forbids `git add .` when unrelated files are present and forbids `--no-verify` unless you ask.
- MIT license. No paid tier to explain.
- Honest gap: Q4 still has to prove the loop in a session log. Until 80% of logged sessions plan or tiny-skip, do not claim habit. Claim the path.

**Who we are not.** We are not Continual Learning (facts into `AGENTS.md`). We are not a GitHub skills list. We are not `npx skills add` without plugin slash commands.

---

## 2. Audience-specific messages

**Avery (primary).** After Reload Window, Customize, User should show Work Kit. Then open a product repo and `/plan`. Tiny obvious change: write tiny skip in the log and implement. Review the real diff. `/ship` named files.

**Casey (secondary, phase 2).** Desktop install does not follow you to a Cloud Agent. Run `./scripts/sync-user-skills.sh`. Turn on Sync Skills for Cloud Agents. If the checker fails, do not start the cloud run.

**Clone visitor (secondary).** Clone [Ses2905/cursor-skills](https://github.com/Ses2905/cursor-skills). Run `./scripts/install-local.sh`. Do not copy this plugin into each application repo. Marketplace plugins you already use stay at user scope. See `STARTER_PLUGINS.md`.

**Riley (recovery only).** If Customize stays empty on Teams, local plugin imports may be blocked. Ask admin for Allow Local Plugin Imports, or fall back to `~/.cursor/skills`.

**Do not tailor.** Press, partners, a sales org. No message for them this quarter.

---

## 3. Channel-specific messaging

**Website / homepage (README).**

Work Kit: install once at user scope. Plan, debug, review, ship. Success is an accepted plan and a named-file commit, not the plugin card.

Next:

1. Command Palette, Developer: Reload Window
2. Customize, filter User, confirm Work Kit
3. Open a product repo and run `/plan` (or `/debug` if something is already broken)

**Social media.** Skip this launch. If you ever post, use the one-liner only. No "we launched" thread. No Product Hunt.

**Email (teammate paste only).**

Work Kit is not done when Customize shows the card. After reload, open a product repo and run `/plan`. Cloud Agents cannot see local plugins. Sync skills first.

**Sales (if a human asks why use this).**

Use Work Kit when you want the same plan-then-ship bar in every Cursor project and you refuse to copy a plugin into each repo. Use a catalog list when you want to browse skills. Use Continual Learning when you want durable repo facts in `AGENTS.md`. Use all three together if you want. They do different jobs.

---

## 4. Messaging pillars

**Pillar 1. Once, user scope.** Install to `~/.cursor/plugins/local/work-kit`. Every project inherits the loop. Repo-specific knowledge stays in that repo.

**Pillar 2. First delivery is the job.** The loop is Plan, Debug, Review, Ship. A visible plugin with no `/plan` is an incomplete install.

**Pillar 3. Same loop on Cloud Agents, different files.** Sync `SKILL.md` folders to `~/.cursor/skills/`. Say this before someone burns a cloud run.

Keep these three. Do not add a fourth pillar about slides, motion, or Remotion. Those are optional catalogs with their own rules.

---

## 5. FAQ and objections

**What is Work Kit?** A personal Cursor plugin for plan, debug, review, ship, and capturing repeated workflows. Public home: github.com/Ses2905/cursor-skills.

**Is it installed?** Customize, User, shows Work Kit after reload. Then you still have to `/plan` on the next real change.

**Customize is empty.** Filter User, not Project. Reload. On Teams, local imports may be blocked. Fallback: copy skills to `~/.cursor/skills`.

**Why not copy the folder into my app repo?** The README forbids it. User-scope is the point. App repos keep `AGENTS.md` and `.cursor/rules` for that codebase.

**Why not `npx skills add` only?** That can install SKILL.md files without this plugin's slash commands. Use E1 or E2 if you want `/plan` and `/ship`.

**Is this an alternative to awesome-cursor-skills?** That repo is a list. This repo is a plugin plus a curated preset you opt into. Lists are better for browsing. Work Kit is better for a default loop. Say that on any comparison page.

**Is this an alternative to Cursor Marketplace plugins?** Marketplace plugins (GitHub, Continual Learning, Create Plugin) are complements at user scope. Work Kit does not replace them.

**Will this make the agent slower or more preachy?** `/plan` waits on non-tiny work. That is the product. Tiny obvious changes skip the long plan. If you want chat to edit immediately every time, do not use Work Kit.

**Does it work on Cloud Agents?** Not as a local plugin. Sync skills and the Settings toggle, or the kit is invisible.

**Is it done when the script prints "Installed"?** No. Next steps include `/plan`.

**Can I add every AI UX Playground skill as the launch?** No. Catalog sprawl is out of scope for first delivery.

**How do you measure this?** Session log: plan/tiny/debug, ship, cloud. Not ARR. Not NPS. End of Q4: would you be very disappointed if `/plan` through `/ship` vanished.

**Objection: I already have a README and AGENTS.md.** Keep them. Work Kit is the cross-project loop. Your repo docs stay the source for that repo.

**Objection: Skills I install from GitHub already do planning.** Some do. Work Kit's bar is one short loop with named slash commands and a ship path that refuses junk staging. If another skill is your loop, do not run both as always-on.

**Objection: Teams will not allow local plugins.** True. We cannot change that. Fallback is `~/.cursor/skills`. Say it early.

**Objection: Proof is thin.** True until the session log exists. Do not inflate with fake customer counts. Point at the scripts and the skill files.

---

## Differentiation snapshot (honest)

| Option | Best for | Not best for |
| --- | --- | --- |
| Work Kit | One loop, every desktop project, named `/plan` to `/ship` | Billed SaaS, public launch days, unscoped catalogs |
| awesome-cursor-skills | Discovering community skills | A default delivery bar |
| `npx skills add` only | Dropping SKILL.md files into a project | Plugin slash commands from this repo |
| Continual Learning | Durable facts in `AGENTS.md` | Plan-gate and ship staging |
| Copying kit files into each repo | Never. Conflicts with this product. | n/a |

Help them decide. If they want a list, send them to the list. If they want first delivery, send them to E1 and the one-liner. Longer desk analysis: [Competitive UX](work-kit-competitive-ux.md). Jobs-vs-jobs positioning (no TAM): [Positioning](work-kit-positioning.md).

---

## Voice

- Clarity over cleverness. Say `/plan`, not "a delightful planning ritual."
- Sentence case. Straight quotes.
- Tell the next step. "Reload, then `/plan`."
- No "you're all set" after the script.
- Same words in README and `install-local.sh`. If they drift, README is wrong or the script is wrong. Fix both.
