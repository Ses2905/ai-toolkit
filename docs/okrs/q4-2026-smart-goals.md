# SMART goals: Work Kit first delivery

**Role / team:** Sarah Scherer. Owner, PM, and the engineer. No other team.
**Area:** First delivery. Install copy through `/plan` and named-file `/ship`. Not catalog growth.
**Rough intent:** Stop treating a Customize card as success. The next product-repo sitting should start with a plan (or a marked tiny skip) and end in a clean ship.
**Constraints:** One person. $0 paid. Cursor chrome is not ours. G3 copy currently fails. Cloud VMs do not mount local plugins. MIT. No Mixpanel.
**How success is measured:** Session log, git, and a binary copy check. Not NPS. Not ARR.
**Related:** [OKRs](q4-2026-work-kit.md), [Scope](../launches/q4-2026-first-delivery-scope.md), [Priority](q4-2026-feature-priority.md), [Metrics](../launches/q4-2026-first-delivery-metrics.md), [Roadmap](q4-2026-roadmap.md)
**Source prompt:** [SMART goal creator](https://aiuxplayground.com/prompts/smart-goal-creator) (AI UX Playground)

These three goals are the OKRs written as SMART. They do not add a fourth objective. O4 (capture) stays in the OKR file and is not a 15 Oct goal.

**Assumption (labeled).** Avery stays the primary user. Casey is goal 3. Riley is not a goal this quarter.

---

## 1. Intent in one sentence

After one user-scope install, Avery's next real change is `/plan` or a marked tiny skip, then `/ship` of named files, and that sitting is written in the session log.

---

## 2. Three SMART goals

### Goal A. Phase 1 go-live (must)

By 15 October 2026, 09:00 owner local, Work Kit first delivery is go: copy matches, Customize shows the plugin, and one product-repo sitting is logged as plan-or-tiny plus named-file `/ship` with no secrets.

**Specific.** Outcome: G1-G4 pass and one complete log row. Scope: `install-local.sh`, README install lists, `docs/okrs/session-log.md`, owner's desktop Cursor. Who: Sarah as Avery. Not in scope: cloud checker, fixtures, interviews, marketplace.

**Measurable.**

| Signal | Baseline 16 Sep | Target 15 Oct |
| --- | --- | --- |
| Script and README step 3 | Optional cloud sync / catalog or toggle | `/plan` or `/debug` if broken. Identical on both |
| Customize, User, Work Kit | Untimed | Visible after reload |
| Session log completed rows | 0 | 1 go-live row: `entry` plan or tiny, `ship=yes`, `named_files=yes` |
| Secrets in that push | Unknown, assume 0 until a miss | 0 |

**Achievable.** F1 is under 2 hours of copy. Risk: this session (and the next) spends time on Playground docs instead. Good enough: three numbered beats match, one real sitting logged. Not good enough: header-only log, or step 3 still sync. If G3 is yellow, slip the day. That is still achieving the goal, later. Launching on yellow is not.

**Relevant.** This is the problem statement. Clone visitors follow step 3. If step 3 is wrong, the kit trains skip.

**Time-bound.** G3 due 8 Oct (SLC). Go/no-go 15 Oct 09:00. Slip with a new date the same day if no-go. Do not keep a yellow 15 Oct.

### Goal B. Loop is the default path (Q4 grade)

By 31 December 2026, at least 80% of logged product-repo sittings start with accepted `/plan` or marked tiny skip, and at least 8 sittings end in `/ship` of named files only.

**Specific.** Outcome: O1 KR2 and KR3. Scope: owner's product repos. `cursor-skills` doc-only rows excluded when marked. Who: Sarah. Not in scope: other ICs' unlogged work, Mixpanel DAU, survey CSAT.

**Measurable.**

| Signal | Baseline | Target 31 Dec |
| --- | --- | --- |
| Plan-or-tiny rate | Untracked. Denominator 0 today | >= 80% of rows with date and repo |
| Named-file ships | Count from git plus log after log starts | >= 8 |
| Weeks with zero rows | n/a | Count as 0 for that week. Do not impute |

Formula: `(n_plan + n_tiny) / n_sessions`.

**Achievable.** Assumes the log is used from go-live week (goal A). Risk: log abandoned, then this goal is a fail, not "unknown." Good enough: 0.7 on the OKR grade is success (about 70% confidence at kickoff). Hitting 80% and 8 ships is 1.0 on those KRs. Fake six-section plans to inflate the rate is not good enough (US-4).

**Relevant.** Habit is the kit's job. A one-day go-live with no later rows is a launch, not first delivery as default.

**Time-bound.** Log starts with goal A (15 Oct or slip date). Weekly rate visible by 22 Oct. Monthly forecast 31 Oct and 30 Nov. Grade 31 Dec.

### Goal C. Cloud Agents get the same loop (phase 2)

By 14 November 2026 the sync checker fails closed if a core skill folder is missing, and by 31 December at least 6 Cloud Agent runs loaded `plan-the-work` or `debug-from-evidence` from `~/.cursor/skills/`.

**Specific.** Outcome: O2 KR1 then KR2. Scope: Casey path, README Cloud section, `sync-user-skills.sh`. Who: Sarah on Cloud Agents. Not in scope: Avery's three install beats (must stay `/plan`). Not in scope: making local plugins appear on VMs (Cursor does not).

**Measurable.**

| Signal | Baseline | Target |
| --- | --- | --- |
| Checker | None | Non-zero exit on a missing core folder. Due 14 Nov |
| Cloud runs that loaded plan or debug | Unknown | 6 by 31 Dec. Do not count runs started while checker is red |
| Avery step 3 | Sync (wrong) | Still `/plan` after Casey copy lands |

**Achievable.** Script work is 1-2 days. Six runs are calendar, not a weekend of code. Risk: putting sync back as Avery step 3 while "fixing" Casey. Good enough: checker green, six noted runs, Avery list untouched. Not good enough: README that says optional sync as desktop step 3.

**Relevant.** Cloud VMs never see `~/.cursor/plugins/local`. Without this, Casey's run looks like the kit is missing.

**Time-bound.** Do not start until goal A copy is split (US-1). Checker and Casey README by 14 Nov. Six runs from 14 Nov through 31 Dec.

---

## 3. Review cadence and leading indicators

**Cadence.**

- Weekly, 15 minutes: count new log rows, plan-or-tiny so far, whether G3 is still green.
- 8 Oct: SLC. Goal A copy must be done or 15 Oct slips.
- 15 Oct 09:00: go/no-go G1-G4.
- 22 Oct: first rate (even if below 80%). Log not abandoned.
- Month end: OKR forecast 0.0-1.0.
- 14 Nov: checker green before counting cloud runs.
- 31 Dec: grade A (done or slipped-and-done), B, C. O4 KR3 disappointment in the OKR file, not here.

**Leading indicators (watch this week, not 31 Dec).**

1. G3 status: match vs mismatch. Today: mismatch. If still mismatch on 8 Oct, goal A will miss 15 Oct.
2. Log rows this week after copy lands. Zero rows for 7 days after go-live means goal B is already in trouble.
3. First sitting after install: `entry` is `plan` or `tiny`, not `neither`. `neither` twice in a row is skip trained by copy or by habit. Check US-1 before blaming Avery.

Do not watch NPS, star counts, or Playground skill install counts. Those are not leading indicators for these goals.

---

## 4. Open questions before committing

Answer in writing. Defaults in parentheses are assumptions if you stay silent.

1. Is Avery still the only person these goals grade? (Yes. A teammate needs a `who` column and a separate rate.)
2. Will the next session that touches this repo be F1 copy, not another template? (It must be, or do not commit to 15 Oct.)
3. What is the first product repo for the go-live row? (Name it. If unnamed, people will log `cursor-skills` chores and the metrics spec will argue.)
4. Is 8 Oct G3 a real hard date or a wish? (Treat as hard. Slip 15 Oct if it misses.)
5. Do unpaid problem interviews happen at all, or is owner diary enough for 15 Oct? (Diary is enough for goal A. Interviews are leftover. Do not block A.)
6. If Cursor changes local plugin paths in Q4, do we slip C or A? (Slip C. A is copy plus a desktop sitting.)
7. Is 80% still the number if the log only has 10 sittings? (Yes. Small n, still a rate. Do not switch to "feels like 80.")

If (2) is no, do not sign these goals. The OKRs already exist. Adding SMART text without F1 is more paper.
