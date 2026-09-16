# Mixed-source synthesis: Work Kit first delivery

**Stakeholder use.** Decision for 15 Oct go/no-go and the next coding session. Not a user-research readout to show a VP as "what testers said."
**Date:** 16 September 2026
**Related:** [Insights](first-delivery-insights.md), [Survey analysis](first-delivery-survey-analysis.md), [Recruitment](first-delivery-recruitment.md), [Session log](../okrs/session-log.md), [Priority](../okrs/q4-2026-feature-priority.md), [Planning session](../sessions/2026-09-16-first-delivery-planning.md)
**Source prompt:** [User research synthesis](https://aiuxplayground.com/prompts/user-research-synthesis) (AI UX Playground)

## Gate (why this is not the Playground's mixed study)

The prompt says use this only when interviews, survey, and analytics are already summarized or coded. If you have one transcript, debrief that session. If you have raw notes, affinity-map first.

| Source the prompt wants | Status 16 Sep | Coded artifact |
| --- | --- | --- |
| Interviews (n=5 to 8) | 0 completes. No transcripts | [Recruitment](first-delivery-recruitment.md) only |
| Survey | 0 completes. Not fielded (G3 block) | [Survey analysis](first-delivery-survey-analysis.md) zeros |
| Usability | 0 sessions. Blocked until G3 | Recruitment F18 |
| Analytics | No Mixpanel. Session log has no filled row | [session-log.md](../okrs/session-log.md) |

What we can synthesize: product inspection, the 16 Sep planning session, and the empty instruments. Those are already coded in [insights](first-delivery-insights.md). They are not three user-data streams.

Do not present the composite Avery quote in the PR/FAQ as a finding. It is imaginary launch-day copy.

Rewrite this file when: 5 interview notes are themed, or the 14 Oct survey export has completes, and the log has rows. Until then, stop asking for mixed synthesis. The 16 Sep session already has a [debrief](../sessions/2026-09-16-first-delivery-planning.md).

---

## Source map (what was combined)

| ID | Source | Type | n | Weight in this report |
| --- | --- | --- | --- | --- |
| S1 | `install-local.sh` next-steps, README install lists | Product inspection | 3 surfaces | High |
| S2 | Session log table | Analytics stand-in | 0 rows | High (empty is a finding) |
| S3 | 16 Sep planning session | Process / owner | 1 session | Medium |
| S4 | Beta survey extract | Survey | 0 | High (empty is a finding) |
| S5 | Interview program | Interviews | 0 | High (empty is a finding) |
| S6 | Priority matrix, OKRs, PR/FAQ | Planning docs | n/a | Low for "user" claims. High for "we already named F1" |

---

## 1. Key findings summary

**Top insights (impact order).** Each line names its sources.

1. **Install copy still names the wrong finish line (S1).** Script step 3 is optional cloud sync. Clone README ends on the Cloud Agents toggle. Checkout README ends on a slash catalog. `/plan` is not the third beat. Insights 1.

2. **No user-data stream has a complete (S4, S5, S2).** Survey 0. Interviews 0. Log 0. There is nothing to triangulate about skippers in the wild.

3. **Planning docs already agree, and the echo did not move (S3, S6, S1).** Runbook, insights, priority, PR/FAQ, and survey spec all require G3. Line 30 of `install-local.sh` is unchanged. Insights 3.

4. **Desktop and cloud are one numbered list (S1).** Optional sync as Avery step 3 serves neither Avery nor Casey. Insights 4. Cloud analytics (skills loaded) also 0 because no runs are logged.

5. **Fielding the beta form now would measure the old copy (S4).** Survey analysis forbids invites until G3. That is a process finding, not a UX stat.

**Patterns across sources.** Every coded source that has content points at the same miss: success is still "plugin visible." Every source that should have people in it is empty on purpose or by delay. Empty + same miss is the pattern. It is not a theme from eight testers.

**Surprising.** Not a user surprise. Process surprise: this repo now has recruitment, survey, insights, survey analysis, priority, and a PR/FAQ, and still has the original echo. Mixed-synthesis requests keep arriving while F1 is unstarted.

---

## 2. User pain points

Ranked by severity for Avery if they follow the product as shipped. Frequency from **user** mentions is 0. Impact from **surfaces** is 3/3 install lists.

| Rank | Pain | Severity | Frequency (users) | Evidence (not a tester quote) |
| --- | --- | --- | --- | --- |
| 1 | Next-steps stop at Customize or send you to optional sync / a catalog | Blocking for first delivery | 0 mentions. 3 install surfaces | S1: `echo "  3. Optional for Cloud Agents: ./scripts/sync-user-skills.sh"`. README clone item 3 is the sync toggle. |
| 2 | Cannot know if the loop ran | Blocking for O1 KR2 | 0 log rows | S2: blank `entry` / `ship` |
| 3 | Cloud miss if you believed "optional" | Blocking for Casey, not today's Avery go-live | 0 cloud notes | S1 architecture. S2 `cloud` column unused |
| 4 | Dirty-tree `/ship` / secrets | P0 if it happens. Unobserved in this extract | 0 | No git audit row this session. Do not invent a hit |
| 5 | Teams empty Customize | Recovery only | 0 | No Riley complete |

**Quotes.** None from participants. Do not substitute the PR/FAQ composite. Owner line from the PR/FAQ leader quote is Sarah stating the problem, not a panel: "I could get a plugin card and still start the next sitting in chat."

---

## 3. User needs and goals

**Primary goal (from problem statement and messaging, not from interviews).** After one user-scope install, the next real change is `/plan` or a marked tiny skip, then named-file `/ship`.

**Unmet needs (observed in product, unvalidated with other ICs).**

- A third next-step that is `/plan`, not optional sync.
- A denominator: log rows.
- A Casey list that is required for cloud, separate from Avery.

**Motivations and behaviors.** Unknown for the 5 to 8 ICs. Owner behavior in S3: pasting Playground templates, not editing the echo. That is a builder behavior, not a user segment.

**Do not claim.** "Users skip `/plan` because they are busy." We have not heard that. We have copy that never asked them to `/plan`.

---

## 4. Opportunities

| Opportunity | Kind | Impact if done | Depends on user data? |
| --- | --- | --- | --- |
| F1: script + README step 3 = `/plan` | Quick win | G3 pass. Installer is told the real job | No. S1 is enough |
| F2: first log row | Quick win | O1 KR2 can start | No |
| Split Casey copy (F8) after F1 | Phase 2 | Stops teaching optional sync as desktop success | No for the split. Yes later for "did skills load" |
| Interviews in leftover hours (F17) | Research | Can confirm skippers | Yes, but must not delay F1 |
| Usability + survey after G3 (F18) | Research | Q10 copy-led `/plan`; Q21 slip rule | Yes, after F1 |
| Dirty-tree fixtures, plan-gate hardening | Long-term Q4 | O3, maybe O1 if log still shows skip | Log first |
| Marketplace, NPS, first-run UI | Cut | None for this problem | n/a |

Potential impact of F1 is the whole 15 Oct narrative. The PR/FAQ is false until F1 lands. No survey needed to start it.

---

## 5. Recommendations

Same order as the [priority matrix](../okrs/q4-2026-feature-priority.md). Mixed research does not reorder F1.

| Priority | Action | Success metric | User-research input required |
| --- | --- | --- | --- |
| 1 | Edit `install-local.sh` and README. Step 3 is `/plan` or `/debug` if broken. Sync off Avery's list | G3 binary: echo matches README | No |
| 2 | Fill one product-repo log row | `entry` and `ship` not blank | No |
| 3 | Time E1 twice | Minutes in the log, target 10 | No |
| 4 | Problem interviews only in leftover hours. Stop at 8 | Notes in research folder, not this synthesis until themed | Yes |
| 5 | Usability + survey after G3. If 2 of 5 on Q21 = no, slip 15 Oct | Completes 5 to 8 by 14 Oct | Yes, after 1 |
| 6 | Do not run this synthesis template again until S4 or S5 has coded completes | This file replaced, not stacked | Yes |

**What not to recommend from this mix.** A new onboarding UI. An analytics pipeline. A segment strategy. Those need testers or a log. We have neither.

---

## Slide appendix (if someone demands a deck)

- Slide 1. Gate: interviews 0, survey 0, log 0. This is not a user-research synthesis.
- Slide 2. Finding: three install surfaces omit `/plan` as step 3.
- Slide 3. Finding: every planning doc already says F1. Echo unchanged.
- Slide 4. Ask: next session is G3 copy, then a log row. Not another Playground report.
- Slide 5. Re-run mixed synthesis on 14 Oct if survey and interviews exist. Otherwise keep the zeros.

**Presenter note.** If a stakeholder asks "what did users say," the accurate sentence is: "No users completed a study. The product already tells installers to stop at Customize."
