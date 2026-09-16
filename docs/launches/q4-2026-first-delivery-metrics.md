# Launch metrics dashboard: Work Kit first delivery

**Product / feature:** Work Kit first delivery (Plan to Ship as the default path)
**Operator:** Sarah Scherer (Avery). Optional teammate later.
**Measure from:** 8 Oct 2026 (log starts) through 31 Dec 2026 (Q4 grade)
**Launch day:** 15 Oct 2026
**Instrument:** markdown plus git. Not Mixpanel, Amplitude, or GA4.
**Related:** [OKRs](../okrs/q4-2026-work-kit.md), [Focus metrics](../okrs/q4-2026-focus-metrics.md), [Runbook](q4-2026-first-delivery-runbook.md), [Session log](../okrs/session-log.md), [Retention](q4-2026-retention-churn.md)
**Source prompt:** [Launch metrics dashboard](https://aiuxplayground.com/prompts/launch-metrics-dashboard) (AI UX Playground)

A session is one coding sitting in a **product repo** (not only `cursor-skills` chores) where Work Kit should have applied. One operator means "users" in this spec are **sessions** and **runs**, not a multiplayer MAU chart.

---

## 1. Success criteria

**Successful launch.** On 15 Oct, Customize shows Work Kit, the session log has a go-live row, and that row is plan-or-tiny-skip plus named-file `/ship`. Through Q4, O1 KR2 hits 80% and O1 KR3 hits 8 ships. Cloud counting starts 14 Nov.

**Primary goals.** Adoption of the loop. Engagement as repeat Plan to Ship. Quality as zero secret commits and copy match. Not revenue.

**Secondary goals.** Cloud runs load core skills (O2). Repeat workflows become skills (O4). README questions that the FAQ already answers stay at 0 after week 1.

**When to read the numbers.**

| Horizon | Date | What must be true |
| --- | --- | --- |
| Day 1 | 15 Oct | Go-live row. Customize yes. Named-file ship yes. No secrets. |
| Week 1 | 22 Oct | At least 3 logged sessions. Plan-or-tiny rate visible (even if below 80%). Log not abandoned. |
| Month 1 | 31 Oct | Monthly KR forecast. At least 1 timed E1 if not done on day 1. |
| Quarter 1 | 31 Dec | Grade O1 to O4. Disappointment question on the core loop. |

---

## 2. North star metric

**Metric.** Plan-or-tiny rate: sessions whose `entry` is `plan` or `tiny` divided by all logged product-repo sessions in the period.

**Why.** The problem statement is install succeeding while the loop never runs. DAU of Cursor would hide that. This rate is the loop.

**Target.** 80% for Q4 (O1 KR2). Day 1: 100% of that day's rows (there should be one). Week 1: no target freeze. Watch that the denominator is not zero.

**How to measure.** `docs/okrs/session-log.md`. Count rows with `entry` in `plan`, `tiny`. Divide by rows with a non-empty `date` and `repo`. Exclude `cursor-skills` doc-only rows if `repo` is this kit and no product change shipped. When unsure, include the row and mark `notes`.

Formula: `plan_or_tiny_rate = (n_plan + n_tiny) / n_sessions`.

---

## 3. Adoption metrics

Map "users" to sessions for one operator. If a teammate appears, add a `who` column. Until then `who` is Sarah.

| Funnel step | Definition | Target | Source |
| --- | --- | --- | --- |
| Discover | Customize shows Work Kit after reload, or README next-steps read | Day 1: yes | Customize check, README |
| Try | First logged session with `entry` plan, tiny, or debug | Day 1: 1 session | Session log |
| Adopt (3+ times) | 3+ sessions with `entry` plan or tiny in Q4 | 3 by 31 Oct, ongoing | Session log |
| Power user | 8+ named-file ships (O1 KR3) plus plan-or-tiny rate still >= 80% | 31 Dec | Log plus git |
| Adoption rate % | Same as north star for the operator. If teammate: their plan-or-tiny rate separately | 80% | Log |
| Time to first use | Minutes from T-0 install to first accepted `/plan` or tiny skip | Same day as 15 Oct go-live | Runbook clock |
| Activation rate | Go-live row has `ship=yes` and `named_files=yes` | 1.0 on day 1 | Log |

Discover without try is the failure mode this launch exists to kill.

---

## 4. Engagement metrics

| Metric | Definition | Target | Skip? |
| --- | --- | --- | --- |
| DAU / WAU / MAU | Count of days with at least one logged session (D), weeks (W), months (M) | No vanity target. Log the counts. | Do not treat Cursor-open days as Work Kit DAU |
| Usage frequency | Sessions per week with plan/tiny/debug | Enough to grade 80% (roughly 2+ per week) | |
| Session duration | Skip | Skip | Not collected |
| Clicks | Skip | Skip | No event stream |
| Retention D1 / D7 / D30 | Day after go-live has a row (D1). A row in day 7-8 window (D7). A row in day 28-31 (D30) | D1: yes. D7: yes. D30: yes | Binary for one person, not a cohort curve of thousands |
| Stickiness DAU/MAU | Skip as a ratio. One operator makes it noise | Skip | |

**Feature usage frequency (real).** Share of sessions that reach `ship=yes`. Secondary engagement: `/debug` when something is broken, not as a substitute for `/plan` on greenfield work.

---

## 5. Quality metrics

| Metric | Definition | Target | Source |
| --- | --- | --- | --- |
| Error rate | Customize missing, copy drift, ship scooped junk, plan skipped on non-tiny work | 0 P0. 0 P1 open at EOD 15 Oct | Runbook |
| Load time | E1 minutes clone to Customize visible | <= 10 min, twice in Q4 | Timed drill |
| Crashes | Cursor crash during loop | Log if it happens. Not a kit KPI | Notes |
| Support tickets | GitHub issues on `cursor-skills` about install/copy/ship | Rising after README change means copy failed | GitHub |
| CSAT | Skip numeric CSAT | Skip | No survey tool |
| NPS | Skip | Skip | Use O4 KR3 disappointment question instead |

**O4 KR3.** 31 Dec: "If `/plan`, `/debug`, `/review-diff`, `/ship` disappeared, I would be very disappointed." Yes = 1.0. Somewhat = 0.3. No = 0.0.

---

## 6. Business impact metrics

| Metric | This product |
| --- | --- |
| Revenue | N/A. MIT. $0. |
| Conversion rate | Plan-or-tiny rate and ship rate, not checkout |
| Upgrades / upsells | N/A |
| Churn | Abandoned log (weeks with 0 rows while coding still happened). Mark in monthly review |
| LTV | N/A |
| Time saved | Optional note in `notes` if a session would have been a long chat without `/plan`. Do not invent hours |

Efficiency is "named files only" and "no speculative debug." Count P0 secrets at 0.

---

## 7. User sentiment metrics

| Metric | How | Target |
| --- | --- | --- |
| Feedback pos/neg | `notes` column plus GitHub issues | Qualitative. Tag `friction:` or `worked:` |
| Social mentions | Skip. Target 0 posts | 0 |
| App store reviews | Skip | Skip |
| Survey | O4 KR3 only, 31 Dec | Very disappointed = yes |
| Feature requests | Issues or notes. Do not let them add catalog skills before O1 | Backlog |
| Pre vs post | Q3 had no log. Post is Q4 rate. Pre is "untracked" | Do not fake a baseline |

---

## 8. Competitive metrics

Skip as a launch dashboard. No market share, win rate, or migration tracker.

Differentiation is documented in [messaging](../messaging/work-kit.md). Do not put competitor SEO traffic on this board.

---

## 9. Dashboard structure

The dashboard is three markdown views over the same log. No BI tool.

### Real-time (launch day 15 Oct)

Fill at 10:00, 12:00, 16:00.

| Field | 10:00 | 12:00 | 16:00 |
| --- | --- | --- | --- |
| Discovered (Customize) | | | |
| Tried (`entry` set) | | | |
| Activated (`ship=yes`) | | | |
| Error (P0/P1) | | | |
| GitHub issues opened | | | |
| Social posts | 0 | 0 | 0 |

### Weekly view (Fridays)

- Plan-or-tiny rate this week
- Ships this week (`named_files=yes`)
- Sessions this week (denominator)
- P1/P0 count
- Top `friction:` notes
- Cloud runs this week (0 until 14 Nov)

### Monthly view

- Running Q4 plan-or-tiny rate vs 80%
- Running ships vs 8
- E1 timings recorded (0, 1, or 2)
- O2 checker pass/fail (from Nov)
- Forecast 0.0 to 1.0 per KR
- Churn: weeks with coding but no log row

---

## 10. Data sources and tools

| Source | What it holds | Access | Refresh |
| --- | --- | --- | --- |
| [Session log](../okrs/session-log.md) | Funnel, north star, sentiment tags | This repo | Each session |
| git | Ships, secrets, named files | `git log`, `git show --stat` | Each `/ship` and monthly audit |
| Cursor Customize | Discover | Desktop UI | Launch day and after reinstall |
| `install-local.sh` vs README | Copy drift | Diff the two texts | Each copy change |
| GitHub issues | Support | github.com/Ses2905/cursor-skills/issues | When filed |
| Cloud transcripts | O2 KR2 | Cursor Cloud run UI | Each cloud run after 14 Nov |
| Sync checker (to add) | Five core folders | Shell exit code | Each sync |
| Mixpanel / Amplitude / GA4 | Unused | n/a | n/a |
| Social listening | Unused | n/a | n/a |
| Survey SaaS | Unused | n/a | O4 KR3 is a sentence in the OKR file |

How to access the log: open the markdown table. Add a row before you close the session. If you forget, add it the same day from git history. Do not backfill a week of guessed `entry` values.

---

## 11. Alerts and thresholds

No PagerDuty. The operator is the alert route. Thresholds from the runbook.

| Metric | Threshold | Severity | Who | Response |
| --- | --- | --- | --- | --- |
| Secrets in a pushed commit | Any 1 | P0 | Sarah | Stop comms. Rotate. Rollback kit if `/ship` caused it. Decision in 15 min |
| Customize empty after install | After reload + User filter | P1 | Sarah | Recover or rollback |
| Copy drift README vs script | Any mismatch after T-0 | P1 | Sarah | Hotfix same day |
| `ship` scooped unrelated files | Any 1 | P1 | Sarah | Do not push if not yet pushed. Log. Fix skill text |
| Plan skipped on non-tiny work | Any 1 | P1 for the session | Sarah | Note. Do not count as plan-or-tiny |
| Week with coding and 0 log rows | 1 week | P2 | Sarah | Treat that week's O1 KR2 as 0. Resume log |
| GitHub issues on copy | Spike after README change | P2 | Sarah | Fix FAQ |
| Social GA post | Any 1 | P1 process | Sarah | Delete/retract if possible. Do not amplify |
| Cloud checker fail | Non-zero exit | P1 for phase 2 | Sarah | Do not start counted cloud runs |

---

## 12. Reporting cadence

| Meeting | When | Metrics | Who |
| --- | --- | --- | --- |
| Daily (first week after 15 Oct) | 16:00 local, 15-16 Oct through 22 Oct | Day's rows, P0/P1, Customize | Sarah, 10 min. Not a standup theater |
| Weekly | Fridays 15 min | Weekly view | Sarah |
| Monthly | 31 Oct, 30 Nov | Monthly view plus KR forecast | Sarah. Optional GitHub issue as paper trail |
| Quarterly | First week of Jan 2027 | Full O1-O4 grade, O4 KR3 | Sarah |

**Who reviews what.** Sarah reviews all. There is no analytics team. Do not assign Marketing to sentiment or Sales to pipeline.

---

## Metric dictionary (log columns)

See [session-log.md](../okrs/session-log.md).

| Column | Values | Rules |
| --- | --- | --- |
| date | ISO date | Required |
| repo | Product repo name | Required. Kit-only chores: mark `kit` in notes |
| who | Sarah (default) | Add names if a teammate appears |
| entry | `plan` / `tiny` / `debug` / `neither` | `neither` hurts the north star |
| review | `ship` / `fix` / `verify` / `-` | From `/review-diff` |
| ship | `yes` / `no` | |
| named_files | `yes` / `no` / `-` | `no` if `git add .` on a dirty tree |
| cloud | `yes` / `no` | `yes` only if a Cloud Agent ran |
| skills_loaded | `plan` / `debug` / `none` / `-` | Required when cloud=yes after 14 Nov |
| minutes_install | number or `-` | Only on timed E1/E2 |
| notes | text | Prefix `friction:` or `worked:` when useful |

If `entry=neither` and you still shipped, keep both facts. Do not relabel as `tiny` after the fact.
