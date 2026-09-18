# Shareout: Work Kit first delivery (16 Sep 2026)

**Project type.** Feature-launch planning plus product inspection. Not a 5-day design sprint. Not a usability study. Not a prototype week with testers.
**Duration.** One Cloud Agent working session on 16 Sep 2026, on top of a kit that has existed since earlier 2026. First delivery is still unproven. Launch target 15 Oct 2026 has not happened.
**Team.** Sarah Scherer only. She is owner, Avery (primary user), copy, and eng. Casey (Cloud Agents) and Riley (Teams) are recovery paths, not the room.
**Audience.** Sarah. There is no exec staff, research org, or design critique panel. If this deck is read later by a clone visitor, it is a status note, not a pitch.
**Time limit.** 20 minutes spoken. Appendix is skippable. Stop at 12 minutes if the only decision left is "open the script."
**Related:** [Stakeholder presentation](q4-2026-stakeholder-presentation.md) (12-min decision cut), [Insights](../research/first-delivery-insights.md), [Affinity](../research/first-delivery-affinity.md), [Focus metrics](../okrs/q4-2026-focus-metrics.md), [WK-1](../tickets/wk-1-g3-install-copy.md), [Roadmap](../okrs/q4-2026-roadmap.md)
**Source prompt:** [Design sprint shareout](https://aiuxplayground.com/prompts/design-sprint-shareout-template) (AI UX Playground)

Do not present this as "what testers said." Interviews 0. Survey 0. Log rows 0. Do not invent quotes, CSAT, or Mixpanel. Do not show ARR. The 12-minute stakeholder deck is the decision version. This file is the longer "what we inspected" version of the same facts.

**Ask at the end.** Next sitting is F1 / G3: `install-local.sh` echo and both README lists, item 3 = `/plan` (or `/debug` if broken). Not another Playground template.

---

## Timing map (20 minutes)

| Min | Section | Slides | If short on time |
| --- | --- | --- | --- |
| 0-4 | Opening | S1-S3 | Keep S1 and S3. Skip team slide. |
| 4-7 | Approach | S4-S6 | Keep constraints. Skip method tour. |
| 7-13 | Built / learned | S7-S11 | Keep S8 (line 30) and S10 (paper vs echo). |
| 13-16 | Results | S12-S14 | Keep the empty-instrument table. |
| 16-18 | Insights | S15-S16 | Keep "docs are not stdout." |
| 18-20 | Recommend | S17-S19 | Keep the no-go and the ask. |
| skip | Appendix | A1-A4 | Only if someone asks "where is the evidence." |

Success for this talk: a calendar block for the copy edit. Failure: another template.

---

## 1. Opening (S1-S3): 4 minutes

### S1. Work Kit is a loop, not a catalog (1 min)

**Talking points**

- Work Kit is a once-per-machine Cursor plugin. Install at user scope. Next change is planned, reviewed, and shipped as named files. Kit files stay out of each application repo.
- Primary user is Avery: Sarah on desktop Cursor. Casey and Riley wait.
- Tonight is a shareout of inspection and planning, not a shipped launch.
- If 15 Oct were tomorrow, we would no-go. Install still finishes on optional cloud sync.

**Visual.** One sentence on a blank slide. No product screenshot yet. Subtitle: "Personal MIT plugin. Team of 1. 16 Sep 2026."

**Timing.** 60 seconds. Do not tour the skill list.

### S2. The problem is skippable first delivery (1.5 min)

**Talking points**

- Install can succeed while Plan to Ship never runs. That is the job failure.
- Live step 3 on the script is `Optional for Cloud Agents: ./scripts/sync-user-skills.sh` (`scripts/install-local.sh` line 30).
- Clone README item 3 points at the Cloud Agents toggle. Checkout README dumps catalog lists as items 3-4.
- Default chat (C1) and skill lists (C3) win minute one if copy is vague. Continual Learning (C4) wins durable facts. We only win `/plan` to `/ship` if copy says so.

**Visual.** Three-column jobs sketch: Chat | Lists | Work Kit. Work Kit column has a red X on "shipped copy" and a green check on "stated job."

**Timing.** 90 seconds. Point, do not debate TAM. There is no TAM.

### S3. Goals, team, dates (1.5 min)

**Talking points**

- Success this quarter is not Customize-visible. It is G3 pass, then 80% plan-or-tiny, then 8 named-file ships. North star is the rate. G3 is the gate.
- Team: Sarah. Hats: operator, PM, eng, copy. No budget ask. $0 MIT.
- Dates that matter: 8 Oct SLC for copy. 15 Oct go-live or slip. 14 Nov cloud checker. 31 Dec grade.
- This session's success criterion: next sitting edits the echo. Filling this deck is not a KR.

**Visual.** Horizontal date bar: 16 Sep (today, G3 fail) → 8 Oct (copy) → 15 Oct (go-live) → 14 Nov (cloud) → 31 Dec (grade). Mark 15 Oct as "no-go until G3."

**Timing.** 90 seconds. Skip OKR recitation. Point at the bar.

---

## 2. Approach (S4-S6): 3 minutes

### S4. Method: inspect the product, do not invent users (1 min)

**Talking points**

- We did not run a Google-style design sprint. No How Might We wall. No five testers on Friday.
- Method: open the install surfaces, the session log, and the planning docs. Compare what we wrote to what stdout prints.
- Unit of analysis: three install texts (script echo, clone README, checkout README), one empty log, one owner.
- Questions we can answer: what does step 3 say. Do instruments have a complete. Did today's docs change the echo.
- Questions we cannot: why other ICs skip `/plan`. How often Teams hides the card.

**Visual.** Two boxes. Left: "Did" (file inspect, copy diff, OKR cut). Right: "Did not" (interviews, survey fielding, prototype test, Mixpanel).

**Timing.** 60 seconds. If the room wants "n=8," say n=0 and move.

### S5. What the sitting actually produced (1 min)

**Talking points**

- User flow, OKRs, SMART, scope, stories, AC, roadmap, GTM, metrics, affinity, SWOT, ICP, LOI (refused paid pilots), retention, focus metrics.
- Ticket WK-1 exists. It names F1 / G3. It has not been implemented.
- Zero of those files changed `install-local.sh` line 30.
- That gap is the finding, not a side note.

**Visual.** Two piles. Left: "docs committed." Right: "stdout." Right pile is empty except the old echo. Caption: "Paper is not the product."

**Timing.** 60 seconds. Do not list every filename.

### S6. Constraints we accepted (1 min)

**Talking points**

- One operator. No design partners. No MSA. No paid pilot (Option C refused).
- Cursor chrome is not ours. Cloud VMs do not mount `~/.cursor/plugins/local`.
- Unslop: no fake NPS, no invented quotes, no percentages of empty tables.
- Scope freeze: marketplace, first-run UI, comparison SEO, and catalog dumps are out until G3.
- Playground templates are a known trap (C7). This shareout is one of them. Treat it as a map, then stop.

**Visual.** In / out table. In: copy match, log row, named-file ship. Out: Marketplace, NPS, cloud as Avery step 3, another synthesis.

**Timing.** 60 seconds.

---

## 3. What we built / learned (S7-S11): 6 minutes

### S7. Stated product (the kit that already exists) (1 min)

**Talking points**

- `scripts/install-local.sh` copies a real directory to `~/.cursor/plugins/local/work-kit`. It does not symlink the checkout.
- Slash commands: `/plan` `/debug` `/review-diff` `/ship` `/new-skill`.
- Core skills: `plan-the-work`, `debug-from-evidence`, `review-the-diff`, `ship-the-change`, `capture-a-skill`, `install-work-kit`.
- Cloud path is `scripts/sync-user-skills.sh`. Local plugins do not mount on cloud VMs. That is phase 2 (14 Nov), not Avery step 3.
- First delivery is not "more skills." It is one sitting that starts planned and ends shipped.

**Visual.** Simple loop diagram: Plan → Debug → Review → Ship. Capture sits off the loop until the log has repeats.

**Timing.** 60 seconds. This is context, not a demo of every skill.

### S8. Live demo: open the echo (1.5 min)

**Talking points**

- This is the walkthrough. Not a Figma. Open `scripts/install-local.sh` lines 25-31.
- Line 28: Reload Window. Line 29: Customize, User, Work Kit. Line 30: optional cloud sync.
- Clone README item 3: Cloud Agents toggle. Checkout README items 3-4: catalog dumps.
- US-1 / G3 wants item 3 to contain `/plan` and `/debug` if broken, on the script and both README lists, identical.
- `git grep` for `Optional for Cloud Agents` on the script echo should be empty after F1. Today it is not.

**Visual.** Screenshot or terminal paste of lines 25-31. Red underline on line 30. Adjacent "should be" text: `3. In chat: /plan (or /debug if something is already broken)`.

**Timing.** 90 seconds. If presenting to yourself, actually open the file. Do not describe it from memory.

### S9. Adjacent jobs (1 min)

**Talking points**

- C1 default chat: implements before a plan exists. Wins if step 3 is skippable.
- C2 skills CLI: inventory without a delivery bar.
- C3 lists: shopping. Checkout README currently behaves like this.
- C4 Continual Learning: durable facts in `AGENTS.md`. Complement, not a rival for ship.
- C5 Marketplace / Create Plugin, C6 copy-into-repo, C7 catalog dumps / Playground templates: noise this quarter.

**Visual.** Job map from [positioning](../messaging/work-kit-positioning.md). Highlight C1 and C3 as the live overlap. Work Kit unique only on stated loop+ship.

**Timing.** 60 seconds. No TAM slide.

### S10. Paper vs echo (1.5 min)

**Talking points**

- Every Q4 doc already ranks F1 / G3 first. Feature priority, SMART A, US-1, WK-1, stakeholder CTA, focus metrics Objective 1 KR1.
- The echo is unchanged. That is insight 3 from the inspection set: specification is not shipped UX.
- Filling more templates raises a vanity count (docs pages) and does not move G3.
- Affinity theme: "install tells a different story than the OKRs." Stickies are inspection notes, not tester quotes.

**Visual.** Two-column: "Docs say" (`/plan`) vs "Install says" (sync script). One arrow labeled "not a commit."

**Timing.** 90 seconds. This is the emotional peak. Then sit in it.

### S11. Decisions already made (1 min)

**Talking points**

- Avery only for 15 Oct. Casey 14 Nov. Riley recovery copy, not a buyer.
- North star: plan-or-tiny rate, 80%. Named-file ships are an input (8). G3 is a gate.
- Paid design partners: refuse. Pilot LOI Option C is a no.
- O4 capture parked until the log has a denominator.
- Rollback: `install-local.sh` from a known-good SHA. Not a feature flag.

**Visual.** Decision log, five rows, one line each. No process photo.

**Timing.** 60 seconds.

---

## 4. Results and validation (S12-S14): 3 minutes

### S12. How we validated (and what we refused to fake) (1 min)

**Talking points**

- Validation today is product inspection: three install surfaces vs US-1 AC. Pass/fail. Fail.
- We did not field the beta survey. Survey analysis is written with n=0 on purpose.
- We did not run E1 timing. Ten-minute clone-to-visible is untimed. Do not invent 7 minutes.
- Mixed-source synthesis stays gated: interviews 0, survey 0, log 0. Do not triangulate skippers.
- The honest test of copy is a sitting after F1, logged. That sitting has not happened.

**Visual.** Checklist with three red fails (G3, log, E1) and no green user-research row.

**Timing.** 60 seconds.

### S13. Scoreboard as of 16 Sep (1 min)

**Talking points**

- G3: fail.
- Session log rows: 0. Plan-or-tiny: n=0 (do not print 0%). Named-file ships: 0.
- Cloud checker: absent. Interviews: 0. ARR: $0 and not a metric.
- Customize-visible is true for the owner and is not success.
- Star, DAU, NPS, template count: off the board ([focus metrics](../okrs/q4-2026-focus-metrics.md) section 4).

**Visual.** Six tiles only: G3, log rows, plan-or-tiny, ships, secrets, E1 minutes. Four of six are fail/empty/untimed. Secrets: unobserved. Do not add a seventh vanity tile.

**Timing.** 60 seconds. If someone asks for a trend line, say there is no series.

### S14. What worked vs what did not (1 min)

**Talking points**

- Worked: kit stays a real copy, not a checkout symlink. Named skills still match the job. Scope freeze named C7 as a trap. Paid-pilot path refused in writing.
- Did not: install copy still teaches skip. Planning volume did not move stdout. Session log still has no denominator.
- Feedback: none from other ICs. Owner feedback is "I already know to `/plan`," which is why clone visitors still need the echo.
- Quotes: none. Do not read the PR/FAQ Avery line as a finding.

**Visual.** Two lists, equal weight. No smile chart.

**Timing.** 60 seconds.

---

## 5. Insights and learnings (S15-S16): 2 minutes

### S15. What surprised us (1 min)

**Talking points**

- The surprise is not that copy drifted. The surprise is that a full planning chain can agree on F1 and still leave line 30 intact.
- Retention here is not billing churn. Value decays at item 3. Empty log means we cannot draw a curve ([retention](q4-2026-retention-churn.md)).
- Cloud-as-step-3 feels helpful and fights the north star. A dashboard that greens both is wrong.
- Playground shareouts feel like a sprint finish. They are C7 unless they end in a patch.

**Visual.** One sentence: "We documented the loop harder than we taught it."

**Timing.** 60 seconds.

### S16. What we would do differently (1 min)

**Talking points**

- Open `install-local.sh` in sitting one. Write the echo. Then write OKRs that describe the new echo.
- Cap planning templates until G3 is green. One more deck after this one is a process smell.
- Do not schedule interviews until copy matches. Talking to people about a skippable step 3 wastes their hour and ours.
- Implication: for a one-person kit, "research complete" is the wrong trophy. "Stdout matches the ticket" is the trophy.

**Visual.** Sequence rewrite: Copy → Log row → Then docs. Cross out: Docs → Docs → Docs → Copy.

**Timing.** 60 seconds.

---

## 6. Recommendations and next steps (S17-S19): 2 minutes

### S17. Recommendation: no-go 15 Oct until G3. Iterate copy this sitting. (45 sec)

**Talking points**

- Go/no-go: **no-go** on 15 Oct if line 30 still says optional cloud sync. Slip the date rather than ship a skippable loop.
- Ship/iterate: **iterate the copy now.** The kit exists. The missing piece is three matching beats, not a new feature.
- Invest/deprioritize: **deprioritize** catalog growth, Marketplace, paid pilots, cloud-as-Avery-step-3, O4 capture, and further Playground fills.
- Do not ask the room for budget. There is no room and no budget.

**Visual.** Big word: "No-go." Subline: "until item 3 is `/plan`."

**Timing.** 45 seconds. Do not soften into "we should consider."

### S18. Next steps, owner, dates (45 sec)

**Talking points**

- Sarah: patch `install-local.sh` success echo and both README numbered lists in one change. WK-1 / US-1 / F1. Target sitting: the next one. SLC 8 Oct.
- Sarah: `/review-diff` on that change. Then one product-repo `/plan` and named-file `/ship`. Log the row. That is day-1 of 15 Oct, or the slip date.
- Sarah: E1 or E2 timed twice after copy. Ten minutes clone-or-checkout to Customize visible.
- Not next: sync checker (14 Nov), six cloud runs, four captures, survey fielding.

**Visual.** Three boxes: Copy (now) → Log row (go-live week) → Cloud checker (14 Nov). Owner on every box: Sarah.

**Timing.** 45 seconds.

### S19. Open questions and what the audience owes (30 sec)

**Talking points**

- Open: exact `/plan` wording on the echo. US-1 AC is the bar. Do not bikeshed past that in this meeting.
- Open: whether 15 Oct slips. Decide after 8 Oct SLC, not tonight.
- Open: E1 timing unknown. Measure after copy, not before.
- From the audience (Sarah): a calendar block, the file open, and a commit. Not approval theater.
- Q&A is a pre-mortem: "If I leave this talk to write another template, the talk failed."

**Visual.** CTA line, same as the stakeholder deck: "Open `scripts/install-local.sh`. Change item 3. Stop."

**Timing.** 30 seconds. End. Do not take the appendix unless asked.

---

## 7. Appendix (skippable)

### A1. Evidence index

- Script: `scripts/install-local.sh` lines 25-31.
- Ticket: [WK-1](../tickets/wk-1-g3-install-copy.md).
- AC: [US-1](../user-flows/us-1-g3-acceptance-criteria.md).
- Empty log: [session-log](../okrs/session-log.md).
- Inspection stickies: [affinity](../research/first-delivery-affinity.md).
- Scoreboard: [focus metrics](../okrs/q4-2026-focus-metrics.md).
- 12-min cut: [stakeholder presentation](q4-2026-stakeholder-presentation.md).

### A2. What we will not put on a slide

- Fake tester quotes, survey n, CSAT, NPS, Mixpanel funnels.
- ARR, TAM, GitHub star charts.
- PR/FAQ Avery quote as a finding.
- Percentages of empty tables.

### A3. Adjacent-job one-liners

- Chat implements first. Lists shop. Continual Learning remembers. Work Kit claims plan-then-named-ship. Live copy still shops and optional-syncs.

### A4. Backup if someone asks "what about cloud?"

- Cloud VMs do not mount local plugins. Checker and six runs are Objective 3 KR2 after 14 Nov. Putting cloud on Avery step 3 is the live bug. Do not "fix" it by making the bug the lesson.

---

## How to use

Present from S1 to S19 without the appendix. If only 12 minutes exist, use the [stakeholder presentation](q4-2026-stakeholder-presentation.md) instead of this file.

Next sitting still does not need a shareout. It needs the echo to match the slides.
