# Beta feedback survey: Work Kit first delivery

**Product in beta:** Work Kit (`work-kit`) first delivery. Install once, then Plan to Ship in a product repo.
**Owner / researcher:** Sarah Scherer
**Related:** [Recruitment](first-delivery-recruitment.md), [Metrics](../launches/q4-2026-first-delivery-metrics.md), [Problem statement](../problem-statements/work-kit-first-delivery.md), [User flow](../user-flows/work-kit-first-delivery.md)
**Source prompt:** [Beta feedback survey](https://aiuxplayground.com/prompts/beta-feedback-survey) (AI UX Playground)

This is not a public SaaS beta. There is no waitlist and no NPS dashboard. Send this only to people who tried install after G3, not as a stand-in for the 5 to 8 problem interviews.

---

## Beta context (filled)

| Field | Value |
| --- | --- |
| What they are testing | Work Kit 1.20.0 path: clone or existing checkout, `./scripts/install-local.sh`, Reload Window, Customize shows Work Kit, then `/plan` (or a marked tiny skip) on a throwaway or real product repo. Optional: `/review-diff`, `/ship`, cloud sync. |
| What we want to learn | Whether README and script next-steps lead to `/plan` without a researcher telling them. What they skip. What blocks ship of named files. Whether Cloud Agents still look like the kit is missing. |
| How long they have had access | Target: G3 copy lands 8 Oct 2026. Testers get 3 to 7 days of use before they see this form. Do not send it against the current script echo that still treats cloud sync as the third step. |
| Cohort size | Same as recruitment: 5 to 8 Avery-like ICs. Owner diary is not a survey response. Do not mix Sarah's answers into the n. |
| Key concerns | Install copy. First `/plan`. Loop skip (chat implements with no plan). `/ship` staging extra files or secrets. Cloud sync skip. Teams/Enterprise empty Customize card. |

**When to send.** After a usability session in 8 to 14 Oct, or 24 hours after they install if they skipped the call. Close the form on 14 Oct. Do not collect on 15 Oct.

**How to send.** Email or the same form tool as the screener. One link. No intercept in Cursor. No Mixpanel.

**Playground items we will not run as KPIs.** The prompt asked for NPS (0-10) and "likelihood to use after launch." Those are cut as launch metrics in the OKRs and metrics spec. This form uses a recommend-to-an-IC item and a next-session `/plan` item instead. Sean Ellis disappointment stays the Q4 personal grade (O4 KR3), asked once at year end, not here.

---

## Survey structure

**Order.** Gate, context, overall, install and loop, per-command, issues, comparison, launch call, open, follow-up.

**Time.** 8 to 10 minutes if they installed. Under 2 minutes if the gate is no (then stop).

**Required vs optional.** Required: G1, Q2, Q6, Q8, Q10, Q15, Q18, Q21. Everything else optional. Do not make open text required.

**Skip logic.**

- Gate = no: thank them, stop. Point them back to the interview, not this form.
- Q2 does not include `/plan`: skip F1. Still ask Q10 (how the session started).
- Q2 does not include `/ship`: skip F3.
- Q3 = no: skip Q12 and F4.
- Q15 = no: skip Q16 and Q17.

**Analysis rule.** n=5 to 8. Report counts, not percentages. Do not chart NPS. Do not average a 1-5 into a fake CSAT target. Quote open text only if they consented on the interview form or tick Q27b.

---

## Paste-ready survey

Title: Work Kit first-delivery feedback (8 to 10 min)

**Intro (paste).**

You tried Work Kit after the install copy was updated. This form is about that try, not about Cursor as a product. Unpaid unless we already offered a gift card for the call. Stop anytime. Do not paste secrets, `.env` files, or private code.

We will not add you to a marketing list. There is no marketing list.

### Gate

**G1.** Did you run `./scripts/install-local.sh` (or an existing checkout of that script) this week and reload Cursor? (yes / no) **Required.**

If no: "Thanks. This form is only for people who installed. If you still want a 45-minute workflow call, reply to Sarah." End.

If yes: continue.

### Use cases and context

Asked first so later answers have a frame. Playground section 5.

**Q1.** What repo did you try this on? (throwaway / a real product repo / both / I do not remember) Optional.

**Q2.** Which of these did you actually run? Check all that apply. **Required.**

- Reload Window, then Customize, User, Work Kit visible
- `/plan`
- `/debug`
- `/review-diff`
- `/ship`
- `/new-skill`
- `./scripts/sync-user-skills.sh`
- I installed and then used chat with no slash command

**Q3.** Did you start a Cursor Cloud Agent on this try? (yes / no / not sure) Optional.

**Q4.** How many separate coding sittings did you use Work Kit in after install? (1 / 2-3 / 4+) Optional.

**Q5.** Cursor seat while you tried it. (personal / Teams / Enterprise / not sure) Optional.

### Overall experience

Scale for Q6 to Q8: 1 = strongly disagree, 2 = disagree, 3 = mixed, 4 = agree, 5 = strongly agree. Include "did not try" where noted.

**Q6.** After install, I knew the next step was `/plan` (or a tiny skip), not "plugin visible." **Required.** 1-5.

**Q7.** I would tell another IC who already uses Cursor to run this install this week. 1-5. Optional. This is not an NPS score and will not be tracked as one.

**Q8.** My next real change in a product repo will start with `/plan` or a marked tiny skip. 1-5. **Required.** This is the survey stand-in for plan-or-tiny intent. The live KPI stays the session log after 8 Oct.

**Q9.** Compared with what the README led me to expect, first delivery was: much worse / worse / as expected / better / much better / I did not read the README. Optional.

### Usability and functionality

**Q10.** How did your first session after install actually start? **Required.**

- I ran `/plan` because the script or README said to
- I ran `/plan` because I already work that way
- I asked the agent to implement with no plan
- I ran `/debug` because something was already broken
- I marked the change tiny and skipped `/plan`
- Other (one line)

**Q11.** Ease of getting from clone-or-checkout to Customize showing Work Kit. 1 = very hard, 5 = very easy, or did not finish install. Optional.

**Q12.** (Show if Q3 = yes.) After install, my Cloud Agent run loaded `plan-the-work` or `debug-from-evidence` from `~/.cursor/skills/`. (yes / no / I did not check / not sure) Optional.

**Q13.** Which piece was most useful on this try? Pick one. Optional.

- Install script
- `/plan`
- `/debug`
- `/review-diff`
- `/ship`
- `/new-skill`
- None of these. Chat without the kit was enough

**Q14.** What was missing that you needed before you would use this on a real repo? Open. Optional, but leave the box. If nothing, type "nothing."

### Specific feature feedback

Rate only what they checked in Q2. Skip the rest. Each feature uses the same four fields:

- Usefulness: 1 = not useful, 5 = essential, or skipped
- Ease: 1 = very hard, 5 = very easy, or skipped
- Worked: one line, optional
- Fix: one line, optional

**F1 `/plan`.** Show if Q2 includes `/plan`.

**F2 Install copy (script echo plus README next-steps).** Show for everyone who passed the gate. This is the G3 check.

**F3 `/ship`.** Show if Q2 includes `/ship`. Hint on Fix: extra files staged, secrets, commit message.

**F4 Cloud sync.** Show if Q3 = yes.

Do not add a block for every catalog skill. This beta is first delivery, not the Remotion pack.

### Issues and bugs

**Q15.** Did you hit a problem that stopped or slowed first delivery? (yes / no) **Required.**

**Q16.** (If yes.) What happened, in one short paragraph. No pastes of `.env` or tokens. Optional-but-shown.

**Q17.** (If yes.) Was it blocking (could not finish `/plan` or `/ship`) or annoying (you finished, with extra work)? (blocking / annoying / not sure)

Severity 1-3 only if they want it: 1 = workaround exists, 2 = lost a session, 3 = would not try again until fixed.

### Comparison

Compare to the workaround in the problem statement, not to a competitor landing page.

**Q18.** Versus starting in chat with no plan, this path was: much worse / worse / same / better / much better / I only used chat. **Required.**

**Q19.** Versus `git add .` on a dirty tree, `/ship` was: much worse / worse / same / better / much better / I did not run `/ship`. Optional.

**Q20.** What would stop you from using Work Kit on the next real change? Check all that apply. Optional.

- Install copy still does not say `/plan`
- Customize does not show the plugin (Teams/Enterprise)
- Agent edits before I accept a plan
- `/ship` is easy to skip
- Cloud run does not see the skills
- I do not want a plugin. I will keep pasting prompts
- Other (one line)

### Launch readiness

Launch here means 15 Oct internal go-live for this kit, not public GA.

**Q21.** For another IC on a personal Cursor seat, is install-then-`/plan` ready to tell them to run this week? (yes / yes with changes / no) **Required.**

**Q22.** What must be fixed before 15 Oct? Open. Optional.

**Q23.** What can wait until after 15 Oct (cloud phase is 14 Nov)? Open. Optional.

Do not ask a second recommend score. Q7 already covers it.

### Open-ended

**Q24.** What should stay as-is? Optional.

**Q25.** What frustrated you most? Optional.

**Q26.** If you could change one sentence in the README or script echo, what would it say? Optional.

**Q27.** Anything else? Optional.

**Q27b.** I am OK with an anonymized quote from this form in `docs/`. (yes / no) Default no.

### Follow-up

**Q28.** OK to schedule a 45-minute follow-up if something in this form is unclear? (yes / no)

**Q29.** Want another week of the same build after you send this, through 14 Oct? (yes / no / already done)

**Q30.** Email if different from the one we used to invite you. Optional.

---

## Scoring (research only)

| Item | How to read | Do not do |
| --- | --- | --- |
| Q6, Q8, Q21 | Launch-relevant. If Q6 median is disagree, G3 is still failing. If Q8 is not agree for most completes, do not claim first delivery. If Q21 is "no" from 2 or more of 5, slip 15 Oct. | Do not convert to NPS. |
| Q10 | Count how many started from copy vs habit vs skip. Copy-led `/plan` is the G3 win. | Do not treat "I already `/plan`" as proof the README works. |
| F2 | Open "fix" lines are G3 bugs. | Do not close G3 on Customize-visible alone. |
| Q15-Q17 | Blocking issues are P0 if they involve secrets or `git add .`. | Do not wait for n=100. |
| Q7, Q9, Q18 | Context for the 22 Oct synthesis. | Do not put on the metrics dashboard. |

Owner fills O4 KR3 on 31 Dec in the OKR doc, not in this form.

---

## Fielding checklist

1. G3 copy matches README and `install-local.sh` (next step is `/plan`, not optional cloud sync).
2. At least one tester has finished install. Do not mail a ghost cohort.
3. Same consent rule as [recruitment](first-delivery-recruitment.md): notes, no marketing list, no secrets.
4. Cap at the 5 to 8 people already recruited. Do not post this on Product Hunt.
5. On 14 Oct, export answers into the 22 Oct synthesis. Leave raw forms off git if they contain emails. Put counts and anonymized quotes in `docs/` only.

**Completion time check.** Read the form out loud. If it takes more than 10 minutes to answer honestly after a real install, cut optional scales before cutting Q6, Q8, Q10, Q21.
