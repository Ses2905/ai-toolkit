# Post-launch analysis: Work Kit first delivery

**Feature / product:** Work Kit first delivery (Plan to Ship as the default path)
**Planned launch date:** 15 October 2026
**This document's as-of date:** 16 September 2026
**Time since launch:** Launch has not happened. 29 days remain.
**Launch scope (planned):** Soft, phased internal. Phase 1 desktop Avery. Phase 2 Cloud Agents on 14 Nov. Not public GA.
**Source prompt:** [Post-launch analysis framework](https://aiuxplayground.com/prompts/post-launch-analysis-framework) (AI UX Playground)
**Related:** [Metrics](q4-2026-first-delivery-metrics.md), [Runbook](q4-2026-first-delivery-runbook.md), [OKRs](../okrs/q4-2026-work-kit.md), [Session log](../okrs/session-log.md)

This is a **pre-launch readout** using the post-launch template. Inventing usage, interviews, or sentiment would fake a grade. Quantitative cells are **no data** unless the source is the repo today.

Re-run this file on **22 October 2026** (week +1). Replace every "no data" from the session log and git. Do not keep this 16 Sep verdict after go-live.

---

## 1. Launch summary

**What was launched.** Nothing in production copy yet. What exists is planning: user flow, OKRs, problem statement, checklist, comms, messaging, GTM, runbook, metrics spec, empty session log.

**What is supposed to launch on 15 Oct.** README and `install-local.sh` next-steps include `/plan`. Avery completes one logged Plan to Ship in a product repo.

**Scope and rollout (planned, not executed).** 100% of current operators (one person). No feature flag. No percentage cohort.

**Key objectives.** O1: first delivery default. O2: cloud loop (from 14 Nov). Not signups or revenue.

**Success criteria (from metrics spec).** Day 1: Customize visible, go-live row, named-file ship. Quarter: 80% plan-or-tiny, 8 ships.

**Go/no-go today.** No-go for 15 Oct if it were tomorrow. G3 fails: script step 3 is still optional cloud sync. Session log has no completed row. README install list still ends on Customize and a long skill inventory, not `/plan` as step 3.

---

## 2. Quantitative analysis

All rates use the [session log](../okrs/session-log.md). The table has a header and an empty row. Denominator for plan-or-tiny is **0**.

| Family | Metric | Value as of 16 Sep | Target | vs target |
| --- | --- | --- | --- | --- |
| Usage | Logged product-repo sessions | 0 | n/a yet | No data |
| Usage | Customize visible after install | Not timed this cycle | Visible | No data |
| Engagement | Plan-or-tiny rate | Undefined (0/0) | 80% | No data |
| Engagement | Sessions with `ship=yes` | 0 | 8 by 31 Dec | Miss if graded now |
| Conversion | Day-1 activation (ship + named files) | 0 | 1 on 15 Oct | Not yet due |
| Conversion | Time to first `/plan` | No data | Same day as go-live | No data |
| Performance | E1 minutes | Untimed | <= 10, twice | No data |
| Quality | Secret commits from `/ship` | Not audited this cycle | 0 | No data |
| Quality | README vs script echo match | Fail. Script step 3 is cloud sync. README local install step 3 is a skill inventory | Match, step 3 is `/plan` | Miss |
| Baseline | Q3 session log | Did not exist | Start week 1 | Baseline is untracked, as planned |

**Comparison to baseline.** Q3 evidence is git history only: catalog skills shipped (HTML PPT, Remotion, animation). No plan-or-tiny rate. Do not backfill.

**Comparison to targets.** It is too early to hit 80% or 8 ships. It is not too early to fail G3. Copy drift is a live miss against the runbook.

---

## 3. Qualitative analysis

**User feedback themes.** None. No post-launch users. Owner (Avery) has not logged a session against the new success bar.

**Support tickets.** No issues filed as a result of a 15 Oct README change. That change is not on `main` as executed launch copy.

**User interviews.** None this cycle. Do not quote imaginary Avery.

**Sentiment.** No social. No app store. O4 KR3 disappointment question is scheduled 31 Dec. Asking it now would grade planning docs, not the loop.

**What we can infer without pretending it is feedback.** The problem statement already names the pre-launch pain: plugin card without `/plan`. That remains the hypothesis, not a validated post-launch theme.

---

## 4. What worked well

These are **planning** wins, not launch wins. Do not carry them into the 22 Oct "what worked" as if users adopted.

- Problem is named. Install can succeed while the loop never runs.
- One metric is named. Plan-or-tiny rate, not Cursor DAU.
- Scope was cut. Paid, PR, Product Hunt, and catalog dumps are explicit non-goals.
- Rollback is specified. `install-local.sh` already `rm -rf` dest then copies. That procedure does not wait on a new tool.
- Session log file exists. Empty, but the columns match the metrics dictionary.
- Honest GTM. $0 paid. Owned README only.

**Met or exceeded goals.** No launch KPIs are due. G5 (no social queued) holds by default.

**Unexpected wins.** None from users. Unexpected process note: G3 showed up because the runbook compared script echo to the new message. Finding the miss before 15 Oct is the point of T-24.

---

## 5. What didn't work

**Issues identified now.**

1. **G3 copy drift.** `install-local.sh` step 3 is still "Optional for Cloud Agents: ./scripts/sync-user-skills.sh". Launch message requires step 3 to be `/plan` (or `/debug` if broken). Cloud sync belongs in the Cloud Agents section, not as the third install beat for Avery.
2. **README local install still treats Customize as done.** After reload it lists a long invoke list. It does not say open a product repo and `/plan`.
3. **Empty denominator.** No session has been logged. O1 KR2 cannot be forecast from data.
4. **Launch date and analysis date were inverted in this prompt.** Writing a post-launch report 29 days early is a process miss if treated as a grade.

**Negative feedback.** None collected.

**Missed goals.** None due except the copy-match goal, which is already red.

**Unexpected problems.** Prompting a full post-launch pack before T-0. Mitigation: this file refuses fake numbers.

---

## 6. User behavior analysis

**How users are using the feature.** Unknown. The feature (first delivery as default path) is not live in install copy.

**Adoption patterns.** Discover may already be true for the owner (plugin installed in daily Cursor). Try and adopt against the new bar: no data.

**Usage frequency.** No rows.

**Segments.** Avery only. Casey not in play until 14 Nov. Riley untested.

**Do not say.** "Users love the loop." "Power users ship daily." There is no log.

---

## 7. Problem identification

**Friction (known pre-launch, still open).**

- Success used to mean plugin visible. That copy is still in the script.
- Cloud path is easy to skip. Calling it optional in step 3 trains Avery to ignore `/plan`.
- Teams can block local plugins. Unchanged.
- Dirty tree plus `git add .` remains a `/ship` risk. Fixtures are due 15 Dec, not 15 Oct.

**Confusion areas (predicted, not observed).** README step 3 as a wall of skill names vs a single next action. Predicted in comms. Not yet user-tested.

**Technical issues.** None reported from go-live. Sync checker script is not built yet (O2 KR1).

**UX issues.** No Work Kit screens. UX is Cursor chrome plus terminal echo. The echo is the UX bug (G3).

---

## 8. Improvement opportunities

### Quick wins (before 15 Oct, ordered)

1. Change `install-local.sh` next-steps so step 3 is open a product repo and `/plan`. Move cloud sync out of that list.
2. Change README local-install "Then" list to match, word for word.
3. Keep GitHub clone path's step 3 as Sync Skills for Cloud Agents **or** split: desktop three steps vs cloud extra steps. Do not mix Avery's third beat with Casey's.
4. Log the next real product-repo session even before 15 Oct, using `entry=neither` if you skipped `/plan`. That starts the denominator honestly.

### Short-term (15 Oct to 22 Oct)

- Run the runbook. Fill day-1 dashboard.
- Time E1 once.
- Do not open social or PH to "make up" for an empty log.

### Long-term (after 80% is real)

- Sync checker.
- Casey checklist on a second environment.
- Dirty-tree fixtures.
- Revisit rented channels only if O1 KR2 is in the log.

### Priority

P0 for launch: items 1 and 2. Without them, 15 Oct is a no-go. Everything else waits.

---

## 9. Business impact

**Revenue.** $0. MIT. No change.

**Cost.** Hours spent writing launch docs in mid-September. That is inventory. It pays off only if G3 is fixed and the log is used. If docs substitute for `/plan`, the cost is wasted.

**User satisfaction.** Ungraded. Do not report NPS.

**Strategic alignment.** Still aligned with the README job (plan first, ship clean). Alignment on paper is not O1. Grade alignment on 31 Dec from the log.

---

## 10. Next steps

**Immediate (this week, before any other launch doc).**

1. Patch `install-local.sh` echo and README so G3 can pass. Owner: Sarah.
2. Fill rollback SHA on T-24 (14 Oct), not now.
3. Do not schedule 15 Oct release notes until G3 is green.

**Iteration plan.** After 15 Oct, use weekly metrics view. After 22 Oct, rewrite **this** analysis with real rows. Delete or strike the 16 Sep "no data" tables so nobody cites them as Q4 results.

**Further research.** None until there are sessions. Do not run interviews about a loop nobody has been asked to follow under the new copy.

**Follow-up actions.**

| When | Action |
| --- | --- |
| Before 8 Oct | G3 copy match. SLC gate. |
| 15 Oct | Runbook. One log row. |
| 22 Oct | First real post-launch analysis. Replace this file's numbers. |
| 14 Nov | Cloud phase only if week-1 log is not empty. |
| 31 Dec | OKR grade. O4 KR3 sentence. |

---

## 22 Oct fill-in stub (use this, do not invent 16 Sep)

Paste log totals:

- n_sessions =
- n_plan =
- n_tiny =
- n_debug =
- n_neither =
- plan_or_tiny_rate =
- n_ship_named =
- E1 minutes =
- P0/P1 count =
- friction notes =

Then rewrite sections 2 to 7 from those numbers only.
