# Problem statement: Work Kit first delivery

**Product:** Work Kit, personal Cursor plugin
**Period this must move:** Q4 2026 (1 October to 31 December)
**Primary user:** Avery, solo IC on desktop Cursor
**Related:** [First-delivery user flow](../user-flows/work-kit-first-delivery.md), [Q4 OKRs](../okrs/q4-2026-work-kit.md)
**Source prompt:** [Problem statement framework](https://aiuxplayground.com/prompts/problem-statement-framework) (AI UX Playground)

The Playground prompt left the brackets blank. This statement is the customer problem behind O1 in the Q4 OKRs. Install can succeed while the Plan to Ship loop never runs.

---

## Framework inputs

### Context

**Current situation.** Work Kit installs to `~/.cursor/plugins/local/work-kit` as a real directory. After Reload Window, Customize, User can show the plugin card. Slash commands `/plan`, `/debug`, `/review-diff`, `/ship` exist. Success in the README and in install output is still "plugin visible," not "an accepted plan and a pushed commit that staged named files only." Session behavior is unlogged. Cloud Agents do not see local plugins unless `sync-user-skills.sh` ran and Sync Skills for Cloud Agents is on.

**Problem or opportunity.** Avery needs a plan-first, evidence-based, review-then-ship path in every Cursor project without copying kit files into each repo. Today the kit can be installed and ignored. Chat starts editing with no plan. `/ship` is easy to skip. Cloud runs look like the kit is missing. The opportunity is to make first delivery the default path, which is already written as a user flow and as O1.

**Why now.** Q4 2026 OKRs grade first delivery, cloud sync, safe ship, and capture. The user flow from mid-September named the aha moment (`/plan` waits for accept) and the churn triggers (Teams block, skipped cloud sync, agent that ignores the plan gate). None of those are timed or counted yet. Catalog installs keep adding skills. That growth does not fix the loop. Waiting another quarter would grade 2026 on plugin presence again.

### Who is affected

**Primary.** Avery, the owner using Work Kit on desktop Cursor in real product repos.

**Secondary.** Casey on Cloud Agents, who inherits a silent miss if sync is skipped. Riley on Teams/Enterprise, who can complete the script and still see an empty Customize card. Future teammates who clone `cursor-skills` and copy the install steps.

**Scale.** One primary operator today. Impact is every coding session in the owner's repos this quarter, plus every Cloud Agent run. Not a multi-customer TAM. If the loop fails, it fails for all of that person's agent work.

### The need

**What they need.** After install, the next unit of work in a product repo should go through Plan (or a marked tiny skip), then verify, then review of the actual diff, then ship of named files. Cloud work should load the same five core skills.

**Current workarounds.** Type prompts with no `/plan`. Debug by guessing. `git add .` on a dirty tree. Re-explain the loop in chat every session. Copy skill files by hand onto a cloud VM. Cost is leftover junk in commits, agents that edit before accept, and cloud runs that never see the kit.

**Desired outcome.** A logged session that starts with an accepted plan (or tiny skip), ends with `/ship` on intended files, and, when the work is on Cloud Agents, loads `plan-the-work` or `debug-from-evidence` from `~/.cursor/skills/`.

### Evidence

**Data.** No product analytics. Evidence is repo history and the docs written this month. Plugin version 1.20.0. `install-local.sh` prints Customize steps, not a first `/plan`. Q3 added scoped catalog skills (HTML PPT, Remotion, animation). It did not add a session log or a timed install. O1 KR2 baseline is untracked.

**Insights.** Ian McAllister's working-backwards test: start with the customer problem, not a thing we want to build. The customer problem is "I still start coding in chat after a successful install." Uri Levine's retention test for this kit: they come back to `/plan` and `/ship`, not to a plugin card. The user flow already lists D4 (tiny vs plan), D6 (verify), D7 (review verdict), V8 (named-file stage). Those are the seams. Catalog sprawl is a false problem. Playground skill installs are not captures and are not first delivery.

**Assumptions (need validation).**

- The owner will keep a session log. Without it, the 80% plan rate has no denominator.
- Cursor will keep loading user-scope local plugins from `~/.cursor/plugins/local/` and cloud skills from `~/.cursor/skills/`.
- Avery remains the primary user. Riley's Teams block is a recovery path, not the happy path.
- "Tiny skip" will be used honestly, not as a way to hide skipped plans.
- Two timed E1 installs are enough to learn where the 10-minute clock dies.

### Success criteria (from Q4 O1, plus the cloud miss that blocks Casey)

**Goals.** First delivery is the default path for Avery. Cloud Agents are not a silent empty kit.

**Metrics.** See section 3.

**Timeline.** Results inside Q4 2026. Week 1: session log exists. October: one timed E1 install. 31 December: grade O1 and O2.

---

## 1. Problem statement

Avery, a solo IC on desktop Cursor, needs a plan-first path from a Work Kit install to a verified, named-file commit because a plugin card in Customize does not change how the next session starts. Currently install can succeed, chat can edit immediately, Cloud Agents can miss synced skills, and `/ship` can scoop a dirty tree, which results in uncounted skipped plans, unverified diffs, and a kit that looks present while the loop never runs.

---

## 2. Context and background

Work Kit is a user-scope Cursor plugin. The job in the README is plan first, debug from evidence, review the real diff, ship a clean commit, and save repeated workflows as skills. Do not copy the kit into each application repo. That job is implemented as skills and slash commands. The install script copies a real folder and tells the user to reload. It does not tell them to run `/plan` on the next real change, and nothing counts whether they did.

Q3 grew the catalog (slides, motion, Remotion) with scoped rules. That is useful later. It is the wrong center of gravity if the core loop is still optional. Mid-September produced a first-delivery user flow and Q4 OKRs. Those documents name the aha moment: `/plan` writes a six-section plan and waits. They also name the misses: no timed clean install, no session log, cloud sync treated as optional, no fixture for dirty-tree shipping. The trigger for writing this statement is that Q4 grading will otherwise score "files exist on disk" again.

What we know is local and small. There are no DAU charts. The honest evidence is scripts, README copy, git history, and the owner's upcoming session log. The hypothesis to test is simple. If first delivery is logged and timed, the share of sessions that plan then ship will rise. If we only add more playground skills, it will not.

---

## 3. Success metrics

Problem solved when these Q4 outcomes hold. Unknown baselines stay unknown.

| Signal | Target by 31 December 2026 | Source |
| --- | --- | --- |
| Clean install to Work Kit visible under Customize, User, after reload | 10 minutes or less, timed twice | Stopwatch, session log (O1 KR1) |
| Logged product-repo sessions start with accepted `/plan` or marked tiny skip | At least 80% | Session log (O1 KR2) |
| Sessions that end in `/ship` of named files only | At least 8 | Session log plus `git log` (O1 KR3) |
| Five core skill folders present after `sync-user-skills.sh` | 100% of syncs, script fails on a miss | New checker (O2 KR1) |
| Cloud Agent runs that load `plan-the-work` or `debug-from-evidence` | At least 6 | Run notes (O2 KR2) |
| `/ship` on a 10-case dirty tree stages only intended paths | 10 of 10 | Fixtures (O3 KR1) |

Leading check, not a team score: on 31 December, "If `/plan`, `/debug`, `/review-diff`, `/ship` disappeared, I would be very disappointed." Yes is 1.0 on O4 KR3. That is one person. Treat it as a disappointment test, not NPS.

---

## 4. Constraints and assumptions

**Constraints.**

- Appetite is Q4 2026, one owner, no separate product team.
- Surfaces are Cursor chrome, terminal, and git. This problem does not require a new Work Kit web app.
- Local plugins do not exist on Cloud Agent VMs. Sync to `~/.cursor/skills/` is the only supported cloud path.
- Teams/Enterprise may block local plugin imports. The kit cannot change that admin setting.
- `ship-the-change` must not `--no-verify` unless the user asks. Hooks stay on.

**Assumptions.**

- Avery is the primary user. Confirm if the owner wants Casey or Riley as the spine instead.
- The owner will write a session log in week 1. If that fails, O1 KR2 cannot be graded honestly.
- Cursor's plugin and skill-sync behavior stays as documented in `install-work-kit`.
- Tiny skip remains a real category for obvious one-file changes, not a loophole.
- Repeating a playground install is not evidence of first delivery.

---

## 5. What's out of scope

- Building a custom first-run UI, dashboard, or marketplace listing for Work Kit.
- Paid growth, ARR, public NPS, or positioning against other Cursor plugins.
- Dumping GitHub skill catalogs or AI UX Playground skills into the kit as a substitute for the loop.
- Changing Cursor itself (Customize, Cloud Agent mounting, Teams policy).
- Making Riley's Teams path the happy path in Q4.
- Capturing every repeated chat into a skill before the plan-to-ship rate is logged (O4 follows O1).
- Publishing a PRD to an issue tracker with `ready-for-agent` labels. This repo has no that triage vocabulary set up. This file is the problem statement, not a ticket dump.

Hypothesis this statement is for: first delivery can be made the default path by logging sessions, timing install, and treating cloud sync as required for cloud work. The scooter is one logged Plan to Ship in a product repo, not a larger platform.
