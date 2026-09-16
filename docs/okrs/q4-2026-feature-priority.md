# Feature priority: Work Kit first delivery, Q4 2026

**Product:** Work Kit (`work-kit`), personal Cursor plugin
**Owner:** Sarah Scherer
**Primary user:** Avery
**Horizon:** now through 31 December 2026. Phase dates: 15 Oct internal, 14 Nov cloud, 31 Dec grade.
**Related:** [OKRs](q4-2026-work-kit.md), [Checklist](../launches/q4-2026-first-delivery-checklist.md), [Problem statement](../problem-statements/work-kit-first-delivery.md), [Runbook](../launches/q4-2026-first-delivery-runbook.md)
**Source prompt:** [Feature prioritization matrix](https://aiuxplayground.com/prompts/feature-prioritization-matrix) (AI UX Playground)

The Playground prompt left the feature list blank. Candidates are the OKR initiatives plus the live G3 copy miss. This is a one-operator kit. Rank work that makes Plan to Ship the default path. Do not rank a marketplace, a dashboard, or catalog dumps.

---

## Context (filled)

**Business goals.** O1: first delivery is the default path (80% plan-or-tiny, 8 named-file ships). O2: Cloud Agents load the same five skills. O3: no secrets or `git add .` junk. O4: repeated workflows become skills. Not ARR. Not NPS.

**User needs.** After install, Avery starts the next real change with `/plan` or a marked tiny skip, then `/ship` of named files. Casey needs sync, not a plugin card on a VM. Riley needs recovery copy if Teams blocks local imports. Avery is the spine.

**Technical constraints.** One owner. Surfaces are Cursor chrome, terminal, git. Local plugins do not exist on Cloud Agent VMs. Teams policy is not owned by this repo. `/ship` must not `--no-verify` unless asked. Session log is markdown. No Mixpanel.

**Timeline.** G3 due 8 Oct. Go-live 15 Oct if G1 to G4 pass. Cloud 14 Nov. Grade 31 Dec. Appetite is this quarter, not a six-month platform bet.

**Live fact.** G3 fails today. `install-local.sh` still prints optional cloud sync as step 3. README still does not make `/plan` the third install beat. Ranking that does not put this first is fiction.

---

## 1. Framework selection

**Recommended.** Value vs effort, with a date gate in front. Call it **gate then V/E**.

**Not RICE.** Reach is one operator (sessions, not users). A Reach score of 1 makes RICE a dressed-up value/effort ratio and implies a funnel we do not have.

**Not Kano this week.** Kano needs testers who have used the loop. The beta survey and 5 to 8 interviews can feed a Kano pass in November on leftover items (plan-gate hardening vs dirty-tree fixtures). Too late to order 15 Oct work.

**Why this aligns.** 15 Oct is a go/no-go, not a backlog grooming. Blockers are not traded against a "nice" capture skill. After blockers, high value and low hours win because the constraint is Sarah's time.

**Methodology.**

1. Put every candidate in one of: 15 Oct gate, 14 Nov cloud, 31 Dec grade, or cut.
2. Score Value 1-5 and Effort 1-5. Score Risk 1-3 as a warning, not a multiplier that hides a blocker.
3. Inside a gate, rank by `P = Value / Effort` (one decimal). Tie-break: lower effort, then lower risk, then O1 before O2-O4.
4. Sequence by dependencies. Do not start cloud copy as Avery's step 3. That is how G3 failed.

---

## 2. Scoring criteria

| Criterion | What it means here | Scale |
| --- | --- | --- |
| Gate | When the work must land or the dated event is a miss | 15 Oct / 14 Nov / 31 Dec / cut |
| Value | Moves O1-O4 or removes the install-succeeds-loop-never-runs failure | 5 = G3 or empty log (no denominator). 4 = a named KR. 3 = honest logging or recovery copy. 2 = research context. 1 = nice |
| Effort | Owner hours to a usable result | 1 = under 2 hours. 2 = half day. 3 = 1-2 days. 4 = 3-5 days. 5 = more than a week of calendar or coding |
| Risk | Chance the change trains the wrong habit or ships secrets | 1 = copy or log. 2 = script behavior. 3 = skill changes how agents edit |

**Weighting.** Gate is a filter, not a weight. No 40/30/30 blend. `P = Value / Effort` only among items that share a gate.

**How to read P.** 5.0 is a 5-value, 1-effort move. Below 1.0 is a grind. A 15 Oct item with P=1.0 still beats a 31 Dec item with P=5.0.

**Assumptions for every row.** Avery is primary. One owner. Cursor plugin paths stay as `install-work-kit` documents them. Playground skill installs are not features.

---

## 3. Feature scoring

Candidate list (in-scope). Cuts are in section 4.

| ID | Feature | Gate | V | E | R | P | KR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | G3 copy. README and `install-local.sh` identical. Step 3 is `/plan` or `/debug` if broken. Cloud sync leaves the Avery list. | 15 Oct | 5 | 1 | 1 | 5.0 | G3, O1 |
| F2 | Session log in use. One row per product-repo sitting. Empty table is not a log. | 15 Oct | 5 | 1 | 1 | 5.0 | G2, O1 KR2 |
| F3 | Timed E1 twice. Clone to Customize visible. Patch where the clock dies. | 15 Oct | 4 | 2 | 1 | 2.0 | O1 KR1 |
| F4 | Tiny-skip rule in the log. No fake six-section plan for a one-file change. | 15 Oct | 3 | 1 | 1 | 3.0 | O1 KR2 |
| F5 | `/ship` skill text plus monthly `git log` audit: no `.env`, no ignored junk. | 15 Oct | 4 | 2 | 2 | 2.0 | O3 KR3, G4 |
| F6 | Review verdict footer on each `/ship` branch: ship / fix / needs verification. | 15 Oct | 3 | 1 | 1 | 3.0 | O3 KR2 |
| F7 | Sync checker. After `sync-user-skills.sh`, fail if any of the five core folders is missing. | 14 Nov | 4 | 3 | 2 | 1.3 | O2 KR1 |
| F8 | Casey README: plugin card missing, skills still required. Pass/fail boxes. Sync is required for cloud work, not Avery step 3. | 14 Nov | 4 | 2 | 1 | 2.0 | O2 KR3 |
| F9 | Stranger checklist run on a second environment. | 14 Nov | 3 | 2 | 1 | 1.5 | O2 KR3 |
| F10 | Six Cloud Agent runs that load `plan-the-work` or `debug-from-evidence`. | 14 Nov | 4 | 4 | 1 | 1.0 | O2 KR2 |
| F11 | Ten dirty-tree fixtures for `/ship` named-path staging. | 31 Dec | 4 | 4 | 2 | 1.0 | O3 KR1 |
| F12 | Tag a workflow the third time it appears. Capture 4 as `skills/<name>/SKILL.md`. | 31 Dec | 3 | 3 | 1 | 1.0 | O4 KR1 |
| F13 | Same-day `install-local.sh` after every skill-add commit. | 15 Oct | 3 | 1 | 1 | 3.0 | O4 KR2 |
| F14 | Hook-fail drill. Confirm the skill forbids `--no-verify` unless asked. | 31 Dec | 3 | 2 | 2 | 1.5 | O3 KR1 |
| F15 | Riley recovery paragraph: Teams may block local imports. Fall back to E3 plus `~/.cursor/skills`. | 31 Dec | 2 | 2 | 1 | 1.0 | O1 recovery |
| F16 | Harden `plan-the-work` so agents wait for accept more often. | 31 Dec | 4 | 4 | 3 | 1.0 | O1 KR2 |
| F17 | Problem interviews n=5 to 8. Current workflow. Can run before G3. | 15 Oct | 3 | 3 | 1 | 1.0 | Research |
| F18 | Usability plus beta survey. Only after G3. | 15 Oct | 3 | 2 | 1 | 1.5 | Research |

### Rationale and assumptions by feature

**F1.** Highest value because live copy trains skip. Effort 1 if the session only edits echo and README. Assumption: no product change is required for G3. Risk 1: words only. Do not "fix" G3 by making cloud sync Avery's third step.

**F2.** File exists. Value is rows, not the header. Effort 1 is starting this week's sittings. Assumption: owner will log. If that fails, O1 KR2 is ungradable. Do not impute.

**F3.** Value 4, not 5: a slow install still delivers if `/plan` is the next step. Effort 2 is two timed runs plus README patches. Assumption: a machine with Cursor already installed is enough. Do not wait for a wipe.

**F4, F6, F13.** Habits. Low effort, they keep the denominator honest. They do not replace F1.

**F5.** Secrets in a push are P0. Effort 2 is reading `ship-the-change` and one audit command. Fixtures (F11) can wait. Assumption: skill text already forbids secrets. Confirm, do not invent a scanner product.

**F7.** Script work. Effort 3 includes wiring into `sync-user-skills.sh` and a miss case. Do not block 15 Oct. Cloud phase is 14 Nov.

**F8 vs F1.** Same files, different audience. F1 is Avery's numbered list. F8 is the Cloud Agents section. Mixing them is the current bug.

**F10.** Effort 4 is calendar (six real runs), not a weekend of code. Starts after F7 passes.

**F11.** Blocks O3 grade, not 15 Oct. Checklist already allows slip to 15 Dec.

**F12.** O4 follows O1. Capturing playground installs does not count.

**F16.** High risk. Changing when agents edit can break tiny skips. Do it only if the log shows skip-to-implement after G3 copy is correct.

**F17 vs F18.** Interviews find skippers. Usability tests copy. Copy is not done, so F18 waits. F17 must not eat the F1 session.

---

## 4. Prioritized feature list

Rank inside each gate by P, then effort, then O1.

### 15 Oct (do in this order)

| Rank | ID | P | Kind | Why this rank |
| --- | --- | --- | --- | --- |
| 1 | F1 | 5.0 | Blocker | Go/no-go G3. Everything else is paper if this stays wrong. |
| 2 | F2 | 5.0 | Blocker | G2 is a header today. KR2 needs a row. |
| 3 | F4 | 3.0 | Quick win | Honest tiny skips. Same day as F2. |
| 4 | F6 | 3.0 | Quick win | Verdict on the branches you already ship. |
| 5 | F13 | 3.0 | Quick win | Reinstall after skill-add. Protects F1 from drifting kit files. |
| 6 | F3 | 2.0 | Drill | Clock E1. Patch only where time dies. |
| 7 | F5 | 2.0 | Safety | Confirm `/ship` text and one audit. G4 adjacent. |
| 8 | F18 | 1.5 | Research | After F1. Usability of the new echo. |
| 9 | F17 | 1.0 | Research | Can overlap F1 week for problem interviews. Do not swap for F1. |

**Quick wins.** F4, F6, F13. Hours, not design.

**Strategic this quarter, not this week.** F7, F11, F16. They are strategic only after the loop is logged.

**Dependencies.** F18 depends on F1. F3 can run the same day as F1 if copy is already patched. F10 depends on F7. F12 depends on F2 (need repeats to tag). F16 depends on F2 showing skip-to-implement after F1.

### 14 Nov

| Rank | ID | P |
| --- | --- | --- |
| 1 | F8 | 2.0 |
| 2 | F9 | 1.5 |
| 3 | F7 | 1.3 |
| 4 | F10 | 1.0 |

Do F8 copy with F7 in one change set so the checklist and the checker agree. Then F9 on a second environment. Then F10 runs.

### 31 Dec

| Rank | ID | P |
| --- | --- | --- |
| 1 | F14 | 1.5 |
| 2 | F11 | 1.0 |
| 3 | F12 | 1.0 |
| 4 | F15 | 1.0 |
| 5 | F16 | 1.0 |

F11 before F16. Safe ship is owned. Agent-hardening is a guess until the log speaks.

### Cut this quarter

| Item | Why |
| --- | --- |
| Marketplace listing, first-run UI, metrics dashboard app | SLC: not simple. Surfaces we do not own. |
| Product Hunt, ads, comparison SEO, NPS/Mixpanel | $0 GTM. Cut in the session summary. |
| Dumping Playground catalogs into the kit | Not first delivery. Not O4. |
| Riley as happy path | Teams admin is not owned. Recovery copy only (F15). |
| Paid waitlist, public GA | One operator. Internal go-live only. |

---

## 5. Roadmap recommendations

Playground phase labels mapped to this kit's dates. There is no separate "next sprint" team. A phase is a dated gate.

### Phase 1. Immediate (now to 15 Oct)

Ship F1 in the next coding session that touches this repo. Same week: F2 first rows, F4, F6, F13. Before 15 Oct: F3 twice, F5 once. Problem interviews (F17) only in leftover hours. Usability (F18) after F1.

Exit: G1 to G4 pass or slip the day. Do not add F7 into phase 1 to look complete.

### Phase 2. Short-term (16 Oct to 14 Nov, then runs through December)

F8, F7, F9. Start F10 after the checker is green. Continue logging. Do not open F16 yet.

If phase 1 slipped, finish F1-F5 before any cloud work. A cloud phase on wrong Avery copy repeats G3.

### Phase 3. Close Q4 and after (14 Nov to 31 Dec; 2027 only if disappointment is yes)

F11, F14, F12, F15. F16 only if plan-or-tiny is below 80% with good copy. After 31 Dec: no six-month roadmap unless O4 KR3 is yes. If it is "somewhat," fix the loop again. Do not start a platform.

**Sequencing one-liner.** Copy, log, clock, ship-safety, then checker, then cloud runs, then fixtures, then capture.

---

## 6. Risk assessment

| Risk | Features | Mitigation | Alternative | Reassess |
| --- | --- | --- | --- | --- |
| Copy still trains skip | F1 | Treat G3 as binary. Slip 15 Oct. | Do not launch on yellow. Last good `install-local.sh` SHA. | Every README or script edit |
| Docs instead of rows | F2 | Missing week = 0 for O1 KR2. No imputed sessions. | Drop research templates until a row exists | Weekly 15-minute OKR check |
| Cloud copy lands in Avery step 3 | F1, F8 | Split lists. Avery: reload, Customize, `/plan`. Casey: sync script plus toggle | F8 lives only under Cloud Agents | When editing `install-local.sh` |
| Checker false green | F7 | Fail closed on a missing folder. One miss-case in the change | Manual `ls` until the script exists | Each sync |
| Fixtures slip | F11 | Keep F5 audit. O3 KR3 still grades | Scored dry-run of skill text vs 10 trees | 15 Dec |
| F16 breaks tiny skip | F16 | Wait for log evidence | Leave skill as-is. Remind in F4 | After 3 weeks of log |
| Interviews eat F1 time | F17 | Cap at leftover hours. n stop at 8 | Skip F17. Owner diary still counts | 8 Oct SLC gate |
| Teams block | F15 | E3 plus skills path. Do not make Riley the spine | Grade O1 KR1 on fallback | If owner uses a Teams seat |
| Cursor changes plugin paths | All | Re-read `install-work-kit` in November | Patch scripts before December grade | November monthly |

**High-risk features.** F16 (behavior change). F7 (script can lie). F11 (false confidence if fixtures are toy). F1 is high impact, low implementation risk, high *miss* risk if skipped.

---

## 7. Success metrics

Use the session log and git. Do not add a survey KPI to the dashboard.

| Feature | Impact measure | Cadence |
| --- | --- | --- |
| F1 | Script echo and README step 3 are `/plan`. Usability: they try `/plan` without being told. | Once at G3, again if copy changes |
| F2 | Rows with date, repo, entry, ship. Denominator > 0 | Weekly |
| F3 | Two times, each 10 minutes or less, written in the log | Twice in Q4 |
| F4 | Tiny rows exist. Plan rate not inflated | Weekly |
| F5 / F14 | Zero secret or gitignore junk commits from `/ship`. Hook drill notes `--no-verify` not used | Monthly audit. Drill once |
| F6 | Every `/ship` branch has a verdict | Each branch |
| F7 | Sync script exit non-zero on a missing folder | Each sync |
| F8 / F9 | Second environment completes the Casey checklist | Once before 14 Nov |
| F10 | 6 cloud runs load a core skill | Weekly after 14 Nov |
| F11 | 10 of 10 dirty trees stage named paths only | After each `ship-the-change` edit |
| F12 | 4 new skills from Q4 repeats, reinstalled | Monthly |
| F13 | 90% of skill-add commits followed by same-day install | Each skill add |
| F15 | One recovery note if Teams is tried. Not a user count | If it happens |
| F16 | Plan-or-tiny rate vs 80% after change | Weekly, only if shipped |
| F17 / F18 | Counts from interviews and survey. Not NPS | 14 Oct close, 22 Oct synthesis |
| O4 KR3 | Very disappointed: yes / somewhat / no | 31 Dec only |

**Review cadence.** Weekly: log plus P-rank if a new candidate appears. Monthly: forecast 0.0-1.0 per KR. 8 Oct: SLC. 15 Oct: G1-G4. 14 Nov: F7 green before counting cloud runs. 31 Dec: grade.

**When to re-score this matrix.** After F1 lands. After week 1 of the log. If Cursor changes plugin or sync behavior. Do not re-score to justify a catalog dump.

---

## Matrix (print this)

| Rank | ID | Feature | Gate | V | E | R | P | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | F1 | G3 copy `/plan` as step 3 | 15 Oct | 5 | 1 | 1 | 5.0 | Edit `install-local.sh` and README. Stop. |
| 2 | F2 | Session log rows | 15 Oct | 5 | 1 | 1 | 5.0 | Log the next product-repo sitting. |
| 3 | F4 | Tiny-skip in log | 15 Oct | 3 | 1 | 1 | 3.0 | Add the word "tiny" when it is tiny. |
| 4 | F6 | Review verdict footer | 15 Oct | 3 | 1 | 1 | 3.0 | Paste verdict on the next `/ship`. |
| 5 | F13 | Same-day reinstall | 15 Oct | 3 | 1 | 1 | 3.0 | Run `install-local.sh` after skill-add. |
| 6 | F3 | Timed E1 | 15 Oct | 4 | 2 | 1 | 2.0 | Stopwatch twice. |
| 7 | F5 | Ship secrets audit | 15 Oct | 4 | 2 | 2 | 2.0 | Read skill. `git log --stat`. |
| 8 | F18 | Usability + survey | 15 Oct | 3 | 2 | 1 | 1.5 | After F1 only. |
| 9 | F17 | Problem interviews | 15 Oct | 3 | 3 | 1 | 1.0 | Leftover hours. Stop at 8. |
| 10 | F8 | Casey README checklist | 14 Nov | 4 | 2 | 1 | 2.0 | Cloud section, not Avery step 3. |
| 11 | F9 | Second-environment Casey | 14 Nov | 3 | 2 | 1 | 1.5 | After F8. |
| 12 | F7 | Sync checker | 14 Nov | 4 | 3 | 2 | 1.3 | Fail closed. |
| 13 | F10 | Six cloud runs | 14 Nov | 4 | 4 | 1 | 1.0 | After F7 green. |
| 14 | F14 | Hook-fail drill | 31 Dec | 3 | 2 | 2 | 1.5 | Once. |
| 15 | F11 | Dirty-tree fixtures | 31 Dec | 4 | 4 | 2 | 1.0 | By 15 Dec. |
| 16 | F12 | Four captures | 31 Dec | 3 | 3 | 1 | 1.0 | From log repeats. |
| 17 | F15 | Riley recovery copy | 31 Dec | 2 | 2 | 1 | 1.0 | Paragraph, not a path rewrite. |
| 18 | F16 | Plan-gate hardening | 31 Dec | 4 | 4 | 3 | 1.0 | Only if log still shows skip. |

Next session does F1, not another Playground template.
