# Focus metrics: Work Kit Q4 2026

**Company.** None. Personal MIT plugin. Owner Sarah Scherer.
**Stage.** Not seed. Not pre-seed. One-operator kit already installed. First delivery is still unproven.
**Strategy this quarter.** Make Plan to Ship the default path: install step 3 is `/plan`, then log sittings until 80% plan-or-tiny and 8 named-file ships.
**Current metrics (16 Sep).** G3 fail. Session log rows 0. Plan-or-tiny rate undefined. Named-file ships 0. Cloud checker absent. Interviews 0. ARR $0 (not a metric).
**Team size.** 1.
**Related:** [OKRs](q4-2026-work-kit.md) (full O1-O4), [SMART](q4-2026-smart-goals.md), [Metrics dashboard](../launches/q4-2026-first-delivery-metrics.md), [Retention](../launches/q4-2026-retention-churn.md), [Tenets](../messaging/work-kit-tenets.md), [QBR](../launches/q4-2026-qbr.md)
**Source prompt:** [North star OKR setup](https://aiuxplayground.com/prompts/north-star-okr-setup) (AI UX Playground)

This file is the weekly scoreboard. Full OKRs stay in `q4-2026-work-kit.md`. O4 (capture) is parked off the weekly board until the log has a denominator. Kill anything that does not change a sitting this week.

---

## 1. North-star options (3)

A north star here counts **product-repo sittings**, not users. DAU of Cursor would grade the host app, not Work Kit.

### Option A. Plan-or-tiny rate (recommended)

`(n_plan + n_tiny) / n_sessions` on filled log rows.

- **Pro.** Matches the problem: install can succeed while the loop never runs. Forces a denominator. Distinguishes tiny honesty from fake plans.
- **Con.** Undefined while rows = 0. Easy to game with fake six-section plans (forbid: US-4). Easy to look like 100% on n=1.
- **Decision it changes.** If rate is low after G3: gate or habit, not copy. If denominator is 0: log, do not forecast.

### Option B. Count of named-file `/ship`s

Cumulative sessions with `ship` of named files only. Target 8 by 31 Dec.

- **Pro.** Auditable in git. Last-mile of the job. Harder to fake than a rate on n=1.
- **Con.** Ignores how the sitting started. Eight chat-then-ship rows would "win" while first delivery failed. Does not tell you to fix step 3.
- **Use as.** Input / KR, not the star.

### Option C. G3 copy match (binary)

Script echo and both README lists: step 3 is `/plan` (or `/debug` if broken).

- **Pro.** Only metric that is live today. Blocks 15 Oct. Clone visitors follow it.
- **Con.** After it passes, it stops moving. A binary cannot be a quarter-long star. Does not prove anyone planned.
- **Use as.** Gate in front of the star. Not the star.

**Rejected.** Customize-visible count, skill-folder count, GitHub stars, NPS, MRR, Playground templates shipped.

---

## 2. Recommended north star + inputs

**North star.** Option A. Plan-or-tiny rate. Q4 target 80%. Do not compute a percentage while `n_sessions` is 0. Show "n=0" instead.

**Gate in front (until green).** Option C. G3. Until green, the weekly question is "did we edit the echo," not "what is the rate."

**Input metrics (only these on the board).**

| Input | Why | Target |
| --- | --- | --- |
| G3 pass/fail | Star is lying if copy still teaches skip | Pass by 8 Oct, or slip 15 Oct |
| Filled log rows this week | Denominator | >= 1 after go-live week; 3 by 22 Oct |
| Named-file ships (cumul) | Finish the sitting | 8 by 31 Dec |
| `neither` count | Diagnoses gate vs copy | Watch after G3. No vanity target |
| Secrets in a push | P0 stop-the-line | 0 |
| E1 minutes (twice) | O1 KR1. After copy | <= 10 min |

**Cloud inputs (after 14 Nov only).** Checker exit, then 6 runs that loaded plan or debug. Do not put them on the board while G3 is red. They fight Avery step 3.

---

## 3. Company OKRs (focus cut: 3 objectives)

Maps to SMART A/B/C. Full O2 KR3 README checklist and O4 capture stay in the long OKR file, off weekly review.

### Objective 1. Install tells the truth

Clone visitors and Avery get three beats: Reload, Customize, `/plan`.

- **KR1.** By 8 Oct (SLC), `install-local.sh` success echo and both README numbered install lists match: item 3 contains `/plan` and `/debug` if broken. `git grep` for `Optional for Cloud Agents` on the script echo is empty. Baseline: fail (line 30).
- **KR2.** By 15 Oct go-live (or slip date), E1 or E2 timed twice: clone or checkout to Customize, User, Work Kit visible in 10 minutes or less. Baseline: untimed.

### Objective 2. The sitting is the loop

Logged product-repo work starts with a plan or an honest tiny skip and ends in named-file ship.

- **KR1.** By 31 Dec, plan-or-tiny rate >= 80% on rows with date and repo. Weeks with zero rows count as 0, not skipped. Baseline: n=0.
- **KR2.** By 31 Dec, at least 8 named-file `/ship`s. Day-1 (15 Oct): 1 go-live row with `entry` plan or tiny and `ship` named files. Baseline: 0.

### Objective 3. Last mile stays clean, cloud waits its turn

No secrets. Cloud does not steal Avery's third beat.

- **KR1.** Through 31 Dec, 0 secrets in a Work Kit `/ship` push. `/review-diff` on copy and ship diffs. Baseline: unobserved, treat a hit as P0.
- **KR2.** By 14 Nov, sync checker fails closed if a core skill folder is missing. By 31 Dec, 6 cloud runs loaded plan or debug **after** checker green. Avery step 3 remains `/plan`. Baseline: no checker.

**Parked.** O4 four captures from log repeats. Start only if Objective 2 has a real denominator and repeats exist. Counting captures now would reward C7.

---

## 4. What not to measure this quarter

Kill. No dashboard tile. No weekly mention.

- ARR, MRR, CAC, LTV, NRR, runway
- NPS, CSAT, star ratings
- DAU/WAU/MAU of Cursor, session duration, click counts
- GitHub stars, traffic, Product Hunt rank
- Number of SKILL.md files, Playground templates completed, docs pages added
- Survey completes before G3 (must stay 0)
- Interview n as a substitute for G3
- Email open rates (no list)
- Customize-visible as success
- Cloud runs counted while checker is red or while step 3 is still sync
- Percentages of empty tables (do not print 0%)

If a metric cannot change this week's sitting, it is off the board.

---

## 5. Weekly review agenda (15 minutes)

Attendee: Sarah. No slide deck. Instrument: session log plus `sed -n '25,31p' scripts/install-local.sh`.

1. **Gate (2 min).** G3 pass/fail. If fail: the rest of the meeting is "when is WK-1," not rates.
2. **Denominator (3 min).** Filled rows this week. If 0 after go-live: log is abandoned. Do not discuss 80%.
3. **North star (3 min).** Plan-or-tiny on those rows. `neither` count. If `neither` rises after G3: gate, not copy.
4. **Finish (3 min).** Named-file ships this week. Secrets? If yes, stop the line.
5. **One decision (4 min).** Next sitting: copy, a product-repo loop, cloud checker, or slip a date. Not "another template."

**Cadence.** Weekly from go-live week. Until G3: this agenda can be 5 minutes (item 1 + 5). Monthly forecast 31 Oct, 30 Nov. Grade 31 Dec.

---

## 6. Failure modes

**Vanity.** Customize-visible, catalog size, docs committed, "we had a planning session." All can go up while line 30 is unchanged.

**Rate with n=0.** Printing 0% or 100% on an empty log. Show n=0.

**Rate with n=1.** 100% after one good day. Do not declare Objective 2 KR1 won.

**Fake plans.** Long `/plan` output on a one-line change to inflate Objective 2 KR1. Mark `tiny` or fail the spirit of the KR.

**Conflicting KRs.** Cloud "optional" as Avery step 3 vs Objective 1 KR1. If both are green in a dashboard, the dashboard is wrong. Avery list wins until 14 Nov.

**Conflicting KRs.** O4 capture vs Objective 2. Capturing playground skills raises O4 and wrecks focus. Park O4.

**Conflicting KRs.** Interview completes vs G3. Research leftover hours only. Completes are not a KR on this board.

**Stop-the-line not on the star.** Secrets can be 1 while plan-or-tiny is 80%. Objective 3 KR1 overrides the star for that sitting.

**Channel expansion while KR2 denominator is 0.** GTM already forbids this. Weekly review must not "add a launch post" to look busy.

---

## How to use

Until G3: only Objective 1 KR1. Then Objective 2 day-1 row. Then the star. Full OKR file is the backlog of KRs. This file is what we actually look at.

Next sitting still does not need a new metric. It needs the echo to match the star's story.
