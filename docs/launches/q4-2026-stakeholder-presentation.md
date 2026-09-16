# Stakeholder presentation: Work Kit first delivery (16 Sep 2026)

**What this is.** A 12-minute readout of planning plus product inspection. Not a user-research shareout. Interviews 0. Survey 0. Log rows 0.
**Room.** Sarah Scherer. She wears every hat. There is no exec staff, no design org, no eng team to convince.
**Decision needed.** Next session edits `install-local.sh` and README (F1 / G3). Not another Playground template.
**Related:** [Insights](../research/first-delivery-insights.md), [Synthesis](../research/first-delivery-synthesis.md), [Roadmap](../okrs/q4-2026-roadmap.md), [Comms](q4-2026-first-delivery-comms.md), [PR/FAQ](q4-2026-first-delivery-prfaq.md), [Shareout](q4-2026-first-delivery-shareout.md), [Stakeholder map](q4-2026-stakeholder-map.md)
**Source prompt:** [Stakeholder presentation](https://aiuxplayground.com/prompts/stakeholder-presentation) (AI UX Playground)

Do not present the PR/FAQ Avery quote as a finding. Do not show NPS. Do not ask for budget.

---

## 1. Presentation goal

**Understand.** Install copy still names the wrong finish line. Planning docs already agree. 15 Oct is no-go until step 3 is `/plan`.

**Action.** Approve (which here means: do) F1 in the next coding sitting. Slip 15 Oct if 8 Oct SLC is still yellow. Do not start cloud copy as Avery's third beat.

**Key takeaway.** Specification is not shipped UX. The script still says optional cloud sync as step 3.

**Success for this talk.** Ends with a calendar block for the copy edit, not with a request for more slides. If Sarah leaves to write another template, the talk failed.

---

## 2. Audience analysis

One human. Map the prompt's roles as hats.

| Hat | Cares about | Knows | Objection | Authority |
| --- | --- | --- | --- | --- |
| Operator (Avery) | Next sitting starts clean | Uses Cursor daily | "I already know to `/plan`" | Does the sitting |
| PM | O1 80% and 8 ships, 15 Oct | Wrote the OKRs | "We should research first" | Sets the date |
| Eng | Script, dest, hooks | Owns `install-local.sh` | "Copy is fine, skill is the product" | Patches the echo |
| Design (copy) | Three numbered beats | README drift | "Catalog should be visible" | Same commit as eng |
| Exec | Time, not ROI | There is no ARR | "Is this big enough to present?" | Go/no-go 15 Oct 09:00 |

**Current knowledge.** High on intent. Low on the live echo if she has not opened `install-local.sh` line 30 today.

**Real objection.** More docs feel like progress. That is C7 (catalog dump) applied to planning.

**Decision-making.** Sarah only. A filled template is not a signature ([scope](q4-2026-first-delivery-scope.md) section 9).

---

## 3. Presentation structure (12 minutes)

Do not use the Playground's 20-minute findings block. There are no testers.

| Min | Block | Slide | Purpose |
| --- | --- | --- | --- |
| 0-1 | Hook | S1 | Why 15 Oct is already in trouble |
| 1-3 | Context | S2 | What this session produced vs what installers see |
| 3-8 | Findings | S3-S6 | Four facts. No process tour |
| 8-11 | Ask | S7-S8 | F1, then log row. Roadmap only after |
| 11-12 | Close | S9 | CTA: open the script now |

Q&A is with herself. Use section 7 as a pre-mortem, not a panel.

### Talking points by slide

**S1. Hook (1 min).** "If 15 Oct were tomorrow, we would no-go. Step 3 is still optional cloud sync. Customize is not first delivery."

**S2. Context (2 min).** "Tonight we filled Playground templates for Work Kit. User flow, OKRs, research plans, AC, roadmap. Zero of those changed stdout. That is the story."

**S3. Copy (2 min).** Before/after of the three beats. Today vs US-1 AC. Point at line 30.

**S4. Empty instruments (1 min).** Interviews 0. Survey 0 (must not field until G3). Log 0. Do not triangulate skippers.

**S5. Competition (1 min).** Default chat wins minute one if step 3 is vague. Lists win shopping. Continual Learning wins `AGENTS.md`. We win `/plan` to `/ship` only if copy says so.

**S6. Paper vs echo (1 min).** Every doc says F1 is rank 1. Echo unchanged. Insight 3.

**S7. Recommendation (2 min).** Edit script and both README lists in one change. MT-1. `/review-diff`. Then one product-repo `/plan` and `/ship`. Log the row.

**S8. What we will not do (1 min).** Marketplace, NPS, first-run UI, cloud as Avery step 3, another synthesis.

**S9. CTA.** "Open `scripts/install-local.sh`. Change item 3. Stop."

---

## 4. Content strategy

Lead with S3 and S7, not the method. So what: clone visitors will do what step 3 says, so they will skip `/plan`. Data: 3 install surfaces, 0 user completes, 0 log rows. Story: owner pasting templates while line 30 sits still. Connect to SMART A and O1. Recommendations are file paths and a date, not "align stakeholders."

Balance: one screenshot of stdout, not a gallery of mermaid from every doc.

---

## 5. Visual strategy

| Point | Visual | Do not |
| --- | --- | --- |
| Hook | Screenshot of script lines 28-30 | A stock "launch" illustration |
| Copy | Two-column before/after three beats | A 20-row feature matrix |
| Empty n | Three zeros: interviews, survey, log | A fake funnel with percentages |
| Competition | One row: job -> send them to | 2x2 with invented share |
| Roadmap | Gantt with F1 in red, rest grey | A year of 2027 bars |
| Quotes | None. Or Sarah's leader line from PR/FAQ labeled owner, not user | Composite Avery as a testimonial |
| Flow | E1 three boxes: Reload, Customize, `/plan` | Full E1-E7 map in the room |

Scannable data: counts, not charts of n=0. Before/after is the only comparison that matters.

---

## 6. Stakeholder communication (hats)

**Designer hat.** Patterns: numbered install list is the UI. Rationale: catalog IA must not be step 3. Stay on copy. No Figma.

**PM hat.** Need: next sitting planned. Tradeoff: research leftover vs F1 now. Priority matrix already ranked F1 at 5.0. High-level unless she opens the AC file.

**Eng hat.** Feasibility: echo strings. Constraint: no dest change, no symlink. Test: MT-1, VF-2 grep. Dive into the patch, not into architecture theater.

**Exec hat.** Impact: every future clone. Cost: under 2 hours. ROI: there is none. Strategic: O1 or we grade a plugin card. Stay high-level: go/no-go.

Language: `/plan`, step 3, G3, log row. Not "onboarding excellence."

---

## 7. Q&A prep (pre-mortem)

**How did you validate this?** Product inspection of script and README on 16 Sep. Not a study. Say that first.

**What about interviews?** Leftover hours. Must not delay F1. Usability of the old echo is not first-delivery UX.

**Edge: I already `/plan`.** Then you are not the clone visitor. Copy is still for them. Log `plan` vs copy-led is Q10 later.

**How much / how long?** Under 2 hours for F1. $0. If we "do not do this": 15 Oct no-go, and every installer learns skip.

**Competitor?** Chat. We lose at minute one. Lists: do not out-catalog. Continual Learning: complement. Full note: [competitive UX](../messaging/work-kit-competitive-ux.md).

**Risks?** Yellow launch. Sync as Avery step 3. `.env` in `/ship` (P0, separate US-5). Cursor path change (slip cloud, not copy).

**If you do not know.** "Not measured. Log has no rows. I will not invent n."

**Is this a big idea?** Not TAM. Big enough for every sitting this quarter. PR/FAQ already says do not send this to press.

---

## 8. Call to action

| Who | What | When |
| --- | --- | --- |
| Sarah / eng | Patch `install-local.sh` and README to US-1 AC | Next sitting. Before 8 Oct |
| Sarah / QA | MT-1, VF-2 grep, `/review-diff` | Same sitting |
| Sarah / operator | Product-repo `/plan` then `/ship`. Log the row | Same day if possible, else 15 Oct |
| Sarah / PM | 8 Oct SLC. 15 Oct 09:00 go/no-go | Calendar |

**Resources.** None to request. Refuse more templates until G3 passes.

**How decided.** She patches or she slips the date. No committee.

---

## 9. Backup plan

**Short on time (5 min).** S1, S3, S9 only. Skip competition and roadmap.

**Challenged ("docs are the work").** Open the script. Read line 30 aloud. Compare to the launch message. That is the defense.

**Off track (catalog skills, Playground, cloud).** "Cloud is 14 Nov and must not be Avery step 3. Catalog is a preset, not E1. Back to line 30."

**Tech fail.** No slides required. `sed -n '25,31p' scripts/install-local.sh` is the deck.

---

## 10. Follow-up

**Share.** This file plus the script diff. Not a Google Slides theme. No audience to mail.

**Actions.** Same table as section 8. Owner is Sarah on every row.

**Feedback.** After MT-1: did stdout match README? If no, talk failed even if slides were pretty.

**Next check-in.** 8 Oct SLC. If F1 landed tonight, next is a log row and timed E1, not a replay of this readout.

---

## Slide list (optional, 9 slides)

1. Title: 15 Oct is no-go until step 3 is `/plan`
2. Tonight: many docs, same echo
3. Before / after three beats
4. n = 0, 0, 0
5. Chat wins minute one
6. Rank 1 is F1. Still open
7. Patch these two files
8. Will not: marketplace, NPS, more PDFs
9. Open the script. Stop

Appendix (do not show unless asked): US-1 AC, roadmap gantt, session summary, PR/FAQ labeled false until G3.
