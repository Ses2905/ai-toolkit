# Project tenets: Work Kit first delivery

**Project.** Work Kit first delivery (Plan to Ship as the default path).
**Problem.** Install can succeed while the next sitting starts in chat with no plan. Live install step 3 still teaches optional cloud sync, so clone visitors never reach `/plan`. Cloud sync is easy to skip. `/ship` can still meet a dirty tree.
**Primary users.** Avery: Sarah Scherer on desktop Cursor, ships with git weekly. Clone visitors who follow the README get the same copy. Casey (Cloud Agents) is phase 2. Riley (Teams) is recovery copy, not a buyer.
**Stage.** Build. The kit already exists at user scope. First delivery is unproven. Not explore (we are not searching for a job). Not scale. Not sunset.
**Constraints.** One owner. $0 paid. MIT. Cursor chrome not owned. Cloud VMs do not mount `~/.cursor/plugins/local`. G3 copy fails today (`scripts/install-local.sh` line 30). Go-live 15 Oct 2026 or slip. Cloud checker 14 Nov. Grade 31 Dec.
**Will not optimize for.** Lowest cost (already $0). Every Casey/Riley edge. Marketplace rank. Catalog size. Interview n. ARR. NPS. Playground templates completed.
**Related:** [Messaging](work-kit.md), [Positioning](work-kit-positioning.md), [Scope](../launches/q4-2026-first-delivery-scope.md), [Focus metrics](../okrs/q4-2026-focus-metrics.md), [Priority](../okrs/q4-2026-feature-priority.md), [WK-1](../tickets/wk-1-g3-install-copy.md)
**Source prompt:** [Project tenets](https://aiuxplayground.com/prompts/project-tenets-creation) (AI UX Playground)

Context is not thin. One set of tenets, not an ambitious vs pragmatic pair. The uncomfortable version is the only version. If a sitting cannot pass these questions, it is C7 (catalog dump), not first delivery.

Tenets are not a feature list. F1 through F18 live in [scope](../launches/q4-2026-first-delivery-scope.md). This file is how we choose when two good ideas fight.

---

## 1. North star

Logged product-repo sittings start with an accepted `/plan` or an honest tiny skip, and end in a named-file `/ship`.

That is plan-or-tiny rate (target 80%) with named-file ships as the input (target 8 by 31 Dec). G3 copy match is the gate in front of the star, not the star. Do not print a percentage while the log has 0 rows. Show n=0.

---

## 2. Seven tenets

### 1. Echo is the product

Stdout and README numbered lists are the shipped UX. Planning docs are not.

**Implication.** We edit `install-local.sh` and both README install lists in the same change. We do not treat a filled template, a ticket, or an OKR file as progress while line 30 still says optional cloud sync. We do not add a shareout, tenets file, or synthesis that postpones that patch.

**Example tradeoff.** When another Playground template vs WK-1 copy, we choose the copy because clone visitors follow the echo, not the planning folder.

### 2. Plan or tiny

Every logged product-repo sitting starts as `/plan` or a marked tiny skip. Chat-then-code is a miss, even if the commit is clean.

**Implication.** We teach `/plan` (or `/debug` if something is already broken) as install item 3. We log `tiny` when the change is one line. We refuse fake six-section plans that inflate the rate. We do not count a sitting that started in default chat as first delivery.

**Example tradeoff.** When a polished `/plan` on a one-line rename vs marking `tiny`, we choose `tiny` because a fake plan teaches the wrong habit and games Objective 2 KR1.

### 3. Avery's third beat

Avery's install has three beats: Reload, Customize, `/plan`. Cloud is not beat three.

**Implication.** Until 14 Nov, Casey's sync script, Settings toggle, and checker stay out of Avery's numbered list. We do not "help" clone visitors by making optional cloud sync the finish line. Riley recovery copy waits. We do not green a dashboard that shows both "cloud mentioned" and "G3 pass."

**Example tradeoff.** When Casey's missing skills vs Avery's step 3, we choose Avery's step 3 because a cloud footnote as item 3 is how G3 failed, and Casey has a dated phase (14 Nov) of his own.

### 4. Named files or it missed

A sitting that does not `/ship` named files did not finish the job. `git add .` on a dirty tree is a miss even if `/plan` ran.

**Implication.** We stage paths we can name. We forbid `--no-verify` unless asked. We count named-file ships (8 by 31 Dec), not "we merged something." Chat-then-ship rows do not rescue first delivery.

**Example tradeoff.** When shipping the whole dirty tree vs a named-path commit that leaves notes behind, we choose named paths because last-mile safety is the job, not a clean working tree for its own sake.

### 5. One spine until proven

Avery on desktop is the product until the loop is logged. Other surfaces are recovery or a later phase.

**Implication.** We do not split copy, GTM, or research across Casey, Riley, Marketplace, or "the Cursor user base." We do not recruit design partners or paid pilots. We do not write B2B ICP. Reach is one operator's sittings.

**Example tradeoff.** When a Teams/Enterprise install path vs a desktop `/plan` echo, we choose the desktop echo because Riley's blocker is policy we do not own, and spreading thin is how step 3 became a cloud footnote.

### 6. Empty stays empty

We do not invent users, quotes, rates, or money. An empty instrument prints n=0, not 0%.

**Implication.** Interviews 0, survey 0, log 0 stay 0 until they are not. We do not field the beta survey before G3. We do not triangulate skippers from mixed sources that are all empty. We do not put ARR, NPS, DAU, GitHub stars, or template counts on the weekly board. Customize-visible is not success.

**Example tradeoff.** When a research readout vs patching the echo, we choose the echo because talking to people about a skippable step 3 wastes their hour and does not change stdout.

### 7. Secrets stop the line

A secret in a `/ship` push beats the north star for that sitting. Stop. Rotate. Then continue.

**Implication.** `/review-diff` on copy and ship diffs. Skill text that forbids `.env` and `git add .` on unrelated files. A hit is P0 even if plan-or-tiny is 80%. We do not "note it and ship anyway."

**Example tradeoff.** When an 80% week vs holding a commit that staged `.env`, we choose to hold because a logged rate cannot excuse a leaked secret.

---

## 3. Anti-goals

Things this project is explicitly not trying to be.

1. **A skill catalog or Marketplace listing.** Folder count and GitHub stars are vanity. Capture (O4) stays parked until the log has repeats.
2. **A billed product.** No ARR, no MSA, no paid design partners, no LOI that implies a check. MIT or nothing this quarter.
3. **Continual Learning.** Durable facts belong in the product repo's `AGENTS.md`. Work Kit is the sitting loop, not the memory store.
4. **A cloud-first installer.** Local plugins do not mount on Cloud Agent VMs. Teaching sync as Avery's finish line is the live bug, not the strategy.
5. **A research program.** Five-to-eight interviews and a beta survey are leftover hours after G3. They are not the 15 Oct trophy.

---

## 4. Review questions

Ask these in critiques, weekly review, and before starting a sitting. A no on 1, or a yes on 3 or 5, means stop.

1. Does this change Avery's next sitting this week, in stdout or in a logged product-repo row?
2. If the docs and the install echo disagree, which one did we actually edit?
3. Would this make Avery's numbered step 3 anything other than `/plan` (or `/debug` if broken)?
4. Are we about to print a percentage, quote, or n that the instruments do not have?
5. Is this C7: another template, skill dump, or catalog page that feels like progress while line 30 is unchanged?

If the sitting cannot answer question 1 with a yes, it is not first delivery. Next sitting is still WK-1: make the echo match these tenets.
