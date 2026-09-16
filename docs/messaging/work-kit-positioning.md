# Competitive positioning: Work Kit

**Product:** Work Kit (`work-kit`), personal MIT Cursor plugin
**Job:** After one user-scope install, the next sitting is `/plan` (or a marked tiny skip) through named-file `/ship`.
**Not a GTM category play.** No TAM. No share. No sales team. No press desk. This file tells Avery (and anyone who clones the repo) which job to pick. It does not fund a launch campaign.
**Related:** [Messaging](work-kit.md), [Competitive UX](work-kit-competitive-ux.md), [GTM](../launches/q4-2026-first-delivery-gtm.md), [STARTER_PLUGINS.md](../../STARTER_PLUGINS.md)
**Source prompt:** [Competitive positioning](https://aiuxplayground.com/prompts/competitive-positioning) (AI UX Playground)
**Desk date:** 16 Sep 2026. Interviews 0. Survey 0. Log rows 0. Do not paste this as SEO.

Live proof gap: stated position is loop then ship. Shipped install copy still routes to chat (card) or catalogs (step 3). Positioning **fails in the first minute** until WK-1 / G3 lands. See [WK-1](../tickets/wk-1-g3-install-copy.md).

---

## 1. Market context

**Category and size.** We do not sell into "AI coding platforms" or "developer tools SaaS." The real category is **how a Cursor sitting starts and finishes**. Size is one primary operator today (Avery) plus clone visitors who follow the GitHub README. Cursor's user base is not our TAM. We have no right to that number and no plan to capture it this quarter.

**Target customers.** Avery: solo IC on desktop Cursor, ships with git weekly, will run a shell script. Secondary: Casey (same person on Cloud Agents, phase 2). Clone visitor on GitHub. Riley on Teams is recovery copy only, not a buyer.

**Trends we actually see (desk, not a report).**

- Default chat implements before a plan exists.
- Skill catalogs and `npx skills add` grow inventory without a delivery bar.
- Continual Learning writes durable facts into `AGENTS.md`. That is a complement.
- Cloud Agent VMs do not mount `~/.cursor/plugins/local`.
- Playground / catalog dumps feel like product progress. They are not first delivery.

**How sittings start today.** Minute one goes to C1 (chat), C3 (browse a list), or C4 (remember facts). Work Kit is the only option in this set that **claims** plan-then-named-ship. Live copy does not yet send people there.

**Current position.** Owned channel is README plus `install-local.sh`. Paid and earned: none, on purpose ([GTM](../launches/q4-2026-first-delivery-gtm.md)). Competitive position vs jobs: **stated** unique on the loop, **shipped** overlapping C1/C3 at install. That is the strategy problem. Not "we need a bigger catalog."

---

## 2. Competitive set

Jobs Avery already has. Not companies to beat on a landing page. Market share for each: not measured. Do not invent percentages.

### Direct (same sitting, different default)

These steal minute one from `/plan`.

**C1. Cursor default chat**

- Who: Anyone already in Cursor. Zero install.
- Strengths: Fast. Always there. No ceremony.
- Weaknesses: No accept gate. Easy `git add .` culture. No session log.
- Share: Unknown. Functionally 100% of Avery's fallback.
- Overlap: Total. Avery is already in this product. Work Kit is a plugin inside it.

**C3. GitHub skill lists (example: awesome-cursor-skills)**

- Who: People shopping for SKILL.md files.
- Strengths: Breadth. Discovery. Badges and tables.
- Weaknesses: No default delivery bar. Infinite install, no ship.
- Share: Unknown. Not a billed competitor.
- Overlap: Clone visitors who landed on a list and our README checkout catalog dump.

**C2. `npx skills add` / skills CLI**

- Who: People who want one SKILL.md on disk fast.
- Strengths: One command.
- Weaknesses: May not install this plugin's slashes. Users think they installed Work Kit (E3 in the user flow).
- Share: Unknown.
- Overlap: Same IC, different finish line (files on disk vs `/plan`).

### Indirect

**Manual process we replace.** Re-explain "plan then ship named files" in chat every sitting. `git add .` on a dirty tree. Copy kit folders into each app repo. Hand-copy skills onto a cloud VM.

**Do nothing.** Stay on C1. Customize may show a plugin card. The sitting still starts in chat. Cost: leftover junk in commits, agents that edit before accept, 15 Oct no-go if we also "do nothing" on copy. Do nothing is the default and it is free.

**Other alternatives.** Repo-local `.cursor/` kits (C6). Marketplace GitHub plugin for PRs (C5). Continual Learning for facts (C4). None of these are "Work Kit, but billed."

### Adjacent (might expand, or we might leak into them)

**C4. Continual Learning (Marketplace).** Writes workspace facts into `AGENTS.md`. Might look like "memory is the loop." It is not. Emerging threat only if we try to eat `AGENTS.md` or if Avery thinks Work Kit replaces it.

**C5. Marketplace GitHub / Create Plugin.** Orthogonal. Threat if we position `/ship` as a PR tool, or if Create Plugin becomes "the" plugin story and first delivery stays invisible.

**C6. Copy `.cursor/` / kit files into each app repo.** Teams that "just vendor it." Fights user-scope. README forbids this for Work Kit. Threat is drift and support, not a rival brand.

**C7. Playground / catalog dumps into this kit.** Internal adjacent. Feels like growth. Does not start `/plan`. This session's template chain is C7 applied to docs.

**Cursor platform changes.** If Cursor ships a native plan-accept-ship bar, our category shrinks to "named files plus log." Watch. Do not pre-build a Marketplace listing to "keep up."

---

## 3. Positioning framework

**Target customer.** Avery, solo IC, desktop Cursor. Job title is whatever pays the git history. Pain: install can succeed while the next sitting has no plan and `/ship` is skipped. Why switch: one install at user scope, every project inherits the loop, product repos keep their own `AGENTS.md`. They do not "switch companies." They switch the first command of the sitting.

**Market category.** User-scope Cursor **delivery loop**, not "AI assistant," not "skill marketplace," not "agent memory." Framing helps because lists win shopping and Continual Learning wins facts. If we enter those frames we lose on breadth and on memory. We can win "what happens after Customize shows the card."

**Category leadership claim.** None. Do not claim we lead a market. Claim: for Avery, Work Kit is the default path from install to a named-file commit. Leadership is a log rate (80% plan-or-tiny, 8 ships by 31 Dec), not a press sentence.

**Unique value (the one thing only we can claim, when copy matches).** Named `/plan`, `/debug`, `/review-diff`, `/ship` after one real-directory install at `~/.cursor/plugins/local/work-kit`, with `/ship` refusing junk staging. Why it matters: the sitting has a start and a finish that git can audit. Proof: skill files and `install-local.sh` (copy dest, excludes, no symlink). Not a testimonial. Not NPS. Honest gap: Q4 log is still empty; do not claim habit.

**Differentiators**

1. **Plan gate, then edits.** Skill waits for accept on non-tiny work. Matters because C1 will implement if you let it.
2. **Named-file `/ship`.** Forbids `git add .` on unrelated files and `--no-verify` unless asked. Matters because chat culture ships leftovers, including `.env`.
3. **Once, user scope.** Real directory install. Not a checkout symlink (Cursor ignores those). Not C6 vendoring. Matters because the loop should not fork into every app repo.
4. **Complements, not a catalog.** Lists stay behind `install-catalog-skills.sh --preset`. Continual Learning stays in `STARTER_PLUGINS.md`. Matters because first-run IA must stay three beats.
5. **Cloud is a different file root.** Local plugin does not mount on Cloud VMs. Sync is Casey, not Avery step 3. Matters because pretending otherwise burns runs.

Differentiators 1-5 are **undiscoverable** while step 3 is optional cloud sync or a 20-name slash list.

---

## 4. Positioning statement

Use this. Do not decorate it.

For a solo IC on desktop Cursor who can install a plugin and still start the next sitting in chat with no plan,

Work Kit is a user-scope delivery loop that makes the next change planned, reviewed on the real diff, and shipped as named files, without copying kit files into each repo.

Unlike default chat, skill lists, or `npx skills add` alone, Work Kit names `/plan` through `/ship` after one install, and `/ship` refuses junk staging.

**Do not use.** "For teams drowning in AI sprawl, Work Kit is the enterprise copilot that promises aligned delivery." That sentence is false on audience, category, and proof.

**False until G3.** If README or script step 3 is not `/plan`, do not say the statement out loud as if install already teaches it.

---

## 5. Competitive comparison matrix

Not price vs features. We are MIT and $0. Axes that decide the sitting:

### Matrix 1. Time-to-first-edit vs delivery bar

High bar = accept a plan (or log tiny), review `git diff`, named-file ship.

```text
delivery bar
high |  Work Kit (stated)
     |  Work Kit (copy today) sits down and right, with C1
     |
low  |  C3 lists     C1 chat / C2 CLI
     +-------------------------------
       slow first edit          instant
```

**Where we sit.** Stated: high bar, slower first edit than C1 (on purpose). Shipped copy: low bar, because step 3 does not start `/plan`. C1 owns instant. C3 owns slow shopping with a low bar.

**Why this frame.** Price/feature 2x2 would put us in a fake SaaS quadrant. This frame says: do not out-speed chat. Win the finish.

### Matrix 2. Catalog breadth vs default loop

```text
default loop (plan to named ship)
strong |  Work Kit (stated)
       |
weak   |  C4 facts     C3 / C7 catalogs
       |  C5 GitHub    C1 chat (no loop)
       +-------------------------------
         narrow kit                 wide inventory
```

**Where we sit.** Narrow kit, strong loop (stated). C3/C7 are wide and loop-weak. C4 is narrow on a different job (facts).

**Insight.** Adding catalog names as install step 3 moves us right (wide) and down (weak loop). That is a loss. Keep presets optional.

### Visual send-to table (print)

| If Avery's job is | Position us as | Not as |
| --- | --- | --- |
| Start the next change with a plan, then named-file ship | Work Kit E1, then `/plan` | A catalog README as step 3 |
| Edit immediately | C1 chat, log `neither` | Optional flavor on the same sitting |
| Find a community skill | C3 list or skills CLI | First delivery |
| Remember repo facts | C4 Continual Learning | Work Kit capture of playground installs |
| PRs and issues in chat | C5 GitHub plugin | `/ship` of the working tree |
| Kit in every app's git | Do not. User scope | C6 |

---

## 6. Win / loss analysis

There is no deal. A "win" is the next sitting. A "loss" is C1/C3 at minute one.

**We win when**

- Need is a repeatable bar across personal repos, not a new skill to try.
- Sitting is non-tiny (or tiny and they will log the skip).
- They will run `./scripts/install-local.sh` and reload.
- Competitive scene is "chat vs a loop," not "which list has more badges."
- How to repeat: three numbered beats. Same words in script and README. Then a log row.

**We lose when**

- Need is instant implement, shopping, or `AGENTS.md` memory.
- They only run `npx skills add` and expect `/plan`.
- Teams block local plugin imports and they refuse `~/.cursor/skills`.
- Step 3 is vague, so C1 wins by default.
- How to address: do not contest C1 on speed, C3 on breadth, C4 on memory. Fix G3. Send them to the right job. Riley: say the admin toggle early. E3: say slashes need the plugin.

**If we do not do G3.** We lose every new clone, including future-Avery. Positioning docs cannot recover that.

---

## 7. Battle cards

Use in a 1:1 paste, not a sales deck. Proof is files. Not quotes from testers (n=0).

### C1. Default chat

**Overview.** The empty Composer/chat box. Avery's default. Work Kit lives inside the same app.

**Their pitch.** Ask, then it edits.

**Strengths.** Zero friction. Always available. Wins impatient sittings.

**Weaknesses.** No plan you can reject. No named-file ship. No log.

**Our advantage.** Accept gate and `/ship` constraints. Tiny skip so we do not moralize obvious one-liners.

**Trap questions (ask them).** "How do you refuse a plan that was never written?" "What staged besides the files you meant?"

**Landmines (they ask).** "Will this make the agent slower or more preachy?" Answer: `/plan` waits on non-tiny work. That is the product. Tiny obvious changes skip the long plan. If you want chat to edit immediately every time, do not use Work Kit.

**Proof.** `skills/plan-the-work/SKILL.md`, `skills/ship-the-change/SKILL.md`. Not a case study.

### C3. Skill lists

**Overview.** Discovery catalogs. awesome-cursor-skills is a list, not a plugin.

**Their pitch.** Browse everything. Copy a URL.

**Strengths.** Breadth. Good for shopping.

**Weaknesses.** No ship bar. First-run as a table of names hides `/plan`.

**Our advantage.** Curated preset behind a script, not E1. One loop.

**Trap.** "When did the last catalog install produce a named-file commit?"

**Landmine.** "Is this an alternative to awesome-cursor-skills?" Answer: that repo is a list. This repo is a plugin plus an opt-in preset. Lists are better for browsing. Work Kit is better for a default loop.

**Proof.** README GitHub skill catalogs section. `install-catalog-skills.sh --preset`. Messaging snapshot table.

### C2. skills CLI

**Overview.** Drops SKILL.md onto disk.

**Pitch.** One command to add a skill.

**Strengths.** Fast add.

**Weaknesses.** Plugin slashes may be missing.

**Our advantage.** Real plugin install plus matching slash names.

**Trap.** "If I type `/plan` after `npx skills add` only, what happens?"

**Landmine.** "I already installed it." Answer: Customize, User, Work Kit card, then `/plan`. CLI alone is E3, not E1.

**Proof.** `scripts/install-local.sh` dest. Slash list in checkout README (after G3: three beats, catalog not numbered step 3).

### C4. Continual Learning

**Overview.** Marketplace plugin. Durable facts in `AGENTS.md`.

**Pitch.** The agent remembers workspace facts.

**Strengths.** Memory across sittings. User scope.

**Weaknesses.** Not a delivery loop. Does not stage git.

**Our advantage.** We do not steal `AGENTS.md`. Complementary.

**Trap.** "Does remembering a fact review the diff or stage `.env`?"

**Landmine.** "Why don't you write facts too?" Answer: product repos keep their own `AGENTS.md`. Work Kit is the cross-project loop. Use both.

**Proof.** `STARTER_PLUGINS.md` install-first row. Messaging "who we are not."

### C6. Copy kit into each repo

**Overview.** Vendor `.cursor/` or plugin files per app.

**Pitch.** The kit travels in that repo's git.

**Strengths.** Follows the repo for a team clone.

**Weaknesses.** Drift. Conflicts. Fights user-scope local plugins.

**Our advantage.** One dest. App repos stay app repos.

**Trap.** "Who owns merges when the kit and the app both change `SKILL.md`?"

**Landmine.** "Our team needs it in git." Answer: README forbids copying this plugin into each application repo. Repo-specific knowledge stays in that repo. We cannot override a Teams block on local imports.

**Proof.** README "Install it once at user scope." Script copies a real directory, does not instruct `ln -s`.

### C5 and C7 (short)

**C5 GitHub plugin.** Pitch: issues/PRs in chat. We do not replace it. `/ship` is working-tree git, not GitHub API. Keep in starter list.

**C7 Catalog dumps.** Pitch: more skills, more ready. Weakness: C3 inside our repo. Trap: "Did stdout change?" Landmine: "We should finish the Playground queue first." Answer: F1/G3 is rank 1. Templates are not scope.

---

## 8. Messaging framework

Canonical lines live in [work-kit.md](work-kit.md). This section is the competitive cut. If the two disagree, the one-liner in that file wins.

**Value propositions**

- Primary: Once-per-machine plugin that makes the next change planned, verified, and shipped as named files, without copying kit files into each repo.
- Secondary: You can reject a plan before code moves. You review `git diff`, not intent. `/ship` should not scoop `.env`.
- Tertiary: Cloud can follow the same loop if you sync skills. Local plugins do not reach cloud VMs. MIT. No paid tier.

**Key messages (statement + proof)**

1. Success is an accepted plan and a named-file commit, not the plugin card. Proof: launch message and (after G3) identical three beats in script and README.
2. Lists for browsing, Continual Learning for facts, Work Kit for `/plan` through `/ship`. Proof: snapshot table in messaging. `STARTER_PLUGINS.md`.
3. Install is a real directory at user scope, not a symlink, not a per-repo copy. Proof: `install-local.sh` dest and excludes.
4. We will not claim habit until the session log shows it. Proof: empty log today. Target 80% plan-or-tiny and 8 ships by 31 Dec. Not ARR. Not NPS.

**Proof points we do not have.** Customer stories (n=0). Statistics of users. Awards. Expert endorsements. Do not invent them for a battle card.

**Proof points we do have.** Scripts, skill text, MIT license, dest path behavior, `/ship` forbids. After 15 Oct: log rows, timed E1, G3 grep.

---

## 9. Positioning by audience

### Customers (Avery, clone visitor)

**30 seconds.** Work Kit is not done when Customize shows the card. After reload, open a product repo and run `/plan`. Review the real diff. `/ship` named files. Install once at user scope. Do not copy this into each app.

**Talking points.** Three beats. Tiny skip is honest. Cloud sync is a different section. Catalogs are optional.

**Story to tell.** Owner pasting templates while line 30 still says optional cloud sync. That is the live miss. After G3, tell the sitting: plan, review, named files. Do not tell a fake user quote.

### Sales

There is no sales org. If a human asks why use this:

**Elevator.** Use Work Kit when you want the same plan-then-ship bar in every Cursor project and you refuse to copy a plugin into each repo. Use a catalog when you want to browse. Use Continual Learning when you want durable repo facts. Use all three if you want. They do different jobs.

**Demo narrative.** Run install. Show stdout (must be three beats after G3). Reload. Customize User. `/plan` in a product repo. `/review-diff`. `/ship` named files. Show the log row. Do not demo a 20-skill inventory as first delivery.

**Objections.** See messaging FAQ. Short versions: empty Customize (filter User, Teams toggle). Why not `npx` only (slashes). Why not copy into the app (user scope). Proof is thin (true until the log exists).

### Partners

No partner program. No integration marketplace pitch. If Cursor or a plugin author asks: we complement user-scope Marketplace plugins. We do not wrap them. Integration story is "install both at user scope." Nothing to co-sell.

### Press / analysts

Skip this quarter. GTM cut comparison SEO, Product Hunt, and embargo. If someone asks anyway: one-liner only. No "we launched." No category creation story. Market POV: Cursor sittings already have chat, lists, and memory. Work Kit is the delivery loop. Do not send the PR/FAQ while G3 is false.

---

## 10. Evolution strategy

**This quarter.** Position as the loop. Ship G3 so the position is true in stdout. Do not evolve into a catalog, a memory product, or a billed assistant.

**When to re-evaluate.** After G3 plus a week of log rows (earliest useful: 22 Oct metrics pass). After 31 Dec disappointment question. If Cursor ships a native plan-to-ship bar. If a teammate appears and needs Riley-path as a real segment. If 80% plan rate exists and Avery actually wants distribution (GTM gate).

**Signals the position is wrong**

- Log shows `neither` as the majority because people hate the gate (product), not because copy was vague (G3).
- Clone visitors still follow catalog step 3 after G3 (copy drifted again).
- Avery uses C4 or C5 as the "real" kit and Work Kit as unused chrome.
- We start answering "how many skills" as the success metric.

**Long-term leadership.** Not category ownership. Be the default sitting bar on Avery's machine, then Casey's cloud path, without becoming a list. If we ever publish a comparison page, reuse the send-to table. Until the loop is logged, that page is theater.

**Immediate strategy (same as competitive UX).**

1. Ship US-1 / WK-1 copy so we stop losing to C1 at minute one.
2. Keep C4/C5 as complements. Do not re-implement them.
3. Keep C3 behind a preset. Do not paste the catalog into install step 3.
4. Do not write comparison SEO.
5. Re-run this file only after G3 and log rows. Positioning without first-run copy is C7.

---

## How to use this file

- README, script echo, teammate paste: [messaging](work-kit.md) one-liner and three beats.
- Desk "vs X" questions: battle cards here, snapshot table there.
- Launch channels: [GTM](../launches/q4-2026-first-delivery-gtm.md). Still $0. Still no press.
- Next product work: [WK-1](../tickets/wk-1-g3-install-copy.md), not a positioning microsite.
