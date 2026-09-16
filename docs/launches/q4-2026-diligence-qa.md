# Diligence Q&A: Work Kit (do not send to investors)

**Company.** None. Personal MIT project. Public repo [Ses2905/cursor-skills](https://github.com/Ses2905/cursor-skills). Owner Sarah Scherer.
**Product.** Work Kit (`work-kit`): a once-per-machine Cursor plugin that makes the next change planned, reviewed on the real diff, and shipped as named files, without copying kit files into each repo.
**Customers.** Avery: one solo IC on desktop Cursor (the owner). Clone visitors who follow README. Casey (Cloud Agents) is phase 2. Riley (Teams) is recovery copy only.
**Business model.** MIT license. Price $0. No seats, no usage fee, no marketplace take rate.
**Metrics.** ARR/MRR: $0 and not a goal. Growth, retention, burn, runway: not company metrics. Product metrics: session log rows 0 as of 16 Sep 2026. Q4 targets exist; actuals do not. Interviews 0. Survey 0.
**Known risks.** Concentration n=1. Cursor platform paths. Install copy still fails G3. Secrets in a push. Single-operator bus factor. Teams can block local plugins.
**Moat claim.** None that a fund would buy. Anyone can fork MIT skill text. What is defensible for Avery is habit plus `/ship` refusing junk, and only after the loop actually runs. Live copy does not yet teach `/plan` as step 3.
**Source prompt:** [Diligence Q&A prep](https://aiuxplayground.com/prompts/diligence-qa-prep) (AI UX Playground)
**Related:** [OKRs](../okrs/q4-2026-work-kit.md), [GTM](q4-2026-first-delivery-gtm.md), [Positioning](../messaging/work-kit-positioning.md), [SWOT](../messaging/work-kit-swot.md), [WK-1](../tickets/wk-1-g3-install-copy.md), [Pilot LOI](q4-2026-pilot-loi.md)

If a partner, employer, or friend asks "is this a company," use this file. Do not invent MRR. The prompt said to mark invented metrics as needing founder input. Here those cells are **N/A or 0**, not blanks to fill with a story.

---

## 0. Opening (ask this first)

**Q.** Are you raising?

**A.** No. There is no entity, no priced round, and no use of funds. Work Kit is a personal plugin. If you want diligence on a startup, this is the wrong packet.

**Attach.** LICENSE (MIT). `.cursor-plugin/plugin.json` (1.20.0).

**Trap.** Softening into "pre-seed, exploring." That is spin. Stop the meeting.

---

## 1. Product and roadmap

**Q.** What does the product do, in one minute?

**A.** After one user-scope install, Avery reloads Cursor, confirms Work Kit under Customize, then in a product repo runs `/plan` (or `/debug` if something is already broken), reviews `git diff`, and `/ship` of named files. Cloud Agents do not see the local plugin. They need synced `SKILL.md` files. Success is an accepted plan and a clean commit, not a plugin card.

**Attach.** [Messaging one-liner](../messaging/work-kit.md). `scripts/install-local.sh`. Core skills under `skills/plan-the-work` and `skills/ship-the-change`.

**Trap.** Demo a 20-name slash catalog as the product. That is C3, not first delivery.

**Q.** What is live vs specified?

**A.** The loop skills and real-directory install are live. Named-file `/ship` rules are in the skill text. Install next-steps are specified as Reload, Customize, `/plan`. Live stdout still prints optional cloud sync as step 3. README clone and checkout lists still do not match that spec. G3 is a 15 Oct no-go until WK-1 lands.

**Attach.** Script lines 27-30. [WK-1](../tickets/wk-1-g3-install-copy.md). [US-1 AC](../user-flows/us-1-g3-acceptance-criteria.md).

**Trap.** "Onboarding is in progress" without showing line 30. Specification is not shipped UX.

**Q.** What is the roadmap?

**A.** Q4 only. 8 Oct G3 copy match. 15 Oct internal go-live if G1-G4 pass. 14 Nov cloud path with a sync checker. 31 Dec grade: 80% plan-or-tiny and 8 named-file ships. No 2027 platform unless the disappointment question is yes.

**Attach.** [Roadmap](../okrs/q4-2026-roadmap.md). [Scope freeze](q4-2026-first-delivery-scope.md). [Priority](../okrs/q4-2026-feature-priority.md).

**Trap.** A year of bars, Marketplace listing, or first-run UI as committed roadmap.

**Q.** How do you know it works?

**A.** Product inspection of install copy, scripts, and skills on 16 Sep. We have not run usability. The session log has no filled row, so we cannot show a sitting that planned and shipped. Plugin dest copy is the part that already works.

**Attach.** [Affinity map](../research/first-delivery-affinity.md). [Session log](../okrs/session-log.md). MT-1 in WK-1 after the copy patch.

**Trap.** Fake n, NPS, or the PR/FAQ Avery quote as a customer.

---

## 2. Market and competition

**Q.** How big is the market?

**A.** We do not claim Cursor's user base as TAM. The category is how one IC's sitting starts and finishes. Customer count today is one. Clone visitors are uncounted GitHub traffic. A TAM slide would be fiction.

**Attach.** [Positioning](../messaging/work-kit-positioning.md) section 1. GTM non-goals.

**Trap.** "AI coding is a $X billion market and we take 1%."

**Q.** Who do you compete with?

**A.** Jobs, not companies. Default Cursor chat (C1) wins minute one. Skill lists and `npx skills add` (C3, C2) win shopping. Continual Learning (C4) wins `AGENTS.md` facts. Marketplace GitHub (C5) wins PRs in chat. Copying kit files into each repo (C6) fights user-scope. Catalog dumps into this repo (C7) feel like progress and are not.

**Attach.** [Competitive UX](../messaging/work-kit-competitive-ux.md). [SWOT](../messaging/work-kit-swot.md). `STARTER_PLUGINS.md`.

**Trap.** A 2x2 vs "Copilot and Cursor" as if we were a platform vendor.

**Q.** What is the moat?

**A.** MIT text is not a moat. Cursor owns the runtime. What we can defend for Avery is a named loop plus `/ship` that refuses junk, if it becomes habit. Until the log has rows, even that is a claim. Fork risk is accepted.

**Attach.** LICENSE. `skills/ship-the-change/SKILL.md`. Session log (empty).

**Trap.** "Data network effects" or "switching costs" on n=1.

**Q.** Why will you win?

**A.** We win a sitting when Avery wants a repeatable bar across personal repos and will run the install script. We lose when they want instant implement, a catalog, or memory. Live we lose at install because step 3 does not say `/plan`. Winning is a copy change this week, not a category war.

**Attach.** Positioning win/loss. WK-1.

**Trap.** "Category leader in agent delivery."

---

## 3. Go-to-market

**Q.** How do you acquire users?

**A.** We do not. Owned channel is GitHub README and `install-local.sh` echo. Paid $0. Earned none. No Product Hunt, ads, or waitlist. If a human asks, paste the teammate template. Clone visitors follow README. That is the motion.

**Attach.** [GTM](q4-2026-first-delivery-gtm.md). [Comms](q4-2026-first-delivery-comms.md).

**Trap.** A funnel with CAC, or "PLG viral loops."

**Q.** What is pricing?

**A.** $0. MIT. There is no conversion to paid. There is no expansion revenue. If we ever charged, that would be a different product and a different diligence file.

**Attach.** LICENSE. GTM paid table (all skip).

**Trap.** "Freemium now, enterprise later" without a buyer or a seat.

**Q.** When is launch?

**A.** Internal phase 1 on 15 Oct 2026 if G1-G4 pass. G3 is currently fail. We will slip the day rather than launch on yellow copy. Phase 2 cloud 14 Nov. We will not post GA.

**Attach.** [Runbook](q4-2026-first-delivery-runbook.md) go/no-go table.

**Trap.** "We launched" while step 3 is still optional sync.

---

## 4. Metrics and unit economics

**Q.** What is ARR / MRR?

**A.** $0. Not a lagging KPI we are waiting to instrument. There is no revenue.

**Attach.** This section. Bank statements are irrelevant to the kit.

**Trap.** A placeholder ARR "to be confirmed." Do not put a number in a cell to look diligent.

**Q.** What are the product KPIs?

**A.** Targets, not actuals: 80% of logged sittings plan or tiny-skip; 8 named-file ships; E1 timed twice under 10 minutes; 6 cloud runs that load plan or debug after a checker exists. As of 16 Sep: log rows 0, so every rate is undefined. Do not report 0% as if n were large.

**Attach.** [OKRs](../okrs/q4-2026-work-kit.md). [Metrics](q4-2026-first-delivery-metrics.md). Session log.

**Trap.** Mixpanel screenshots, NPS, DAU, or percentages of empty tables.

**Q.** What is retention / churn?

**A.** Not measured. The user is the operator. Churn would mean she stops using `/plan`. We will know that from `neither` rows after the log exists. There is no cancel survey.

**Attach.** Session log schema (`entry`: plan / tiny / debug / neither).

**Trap.** "Net revenue retention 120%."

**Q.** What is burn and runway?

**A.** Company burn $0. Paid GTM $0. Constraint is Sarah's hours, not cash. Runway as a finance term does not apply. Opportunity cost is sittings spent on Playground templates instead of WK-1.

**Attach.** GTM budget rows. SWOT W4.

**Trap.** Personal salary as "burn" to imply a seed round.

**Q.** Unit economics?

**A.** No unit. No COGS of note beyond Cursor (which the user already pays) and git. Gross margin on $0 is a nonsense slide.

**Attach.** None. Refuse the slide.

**Trap.** "Software margins 90%."

---

## 5. Team and hiring plan

**Q.** Who is on the team?

**A.** Sarah Scherer. Eng, QA, PM, support, and the only user that matters this quarter (Avery). No contractors. No advisors with a kit equity story, because there is no equity.

**Attach.** Git history. Plugin author field if present.

**Trap.** A fake org chart with unfilled roles.

**Q.** What is the hiring plan?

**A.** None this quarter. Scope is one-operator. If a teammate clones the repo, they follow README. We are not recruiting a sales hire, a researcher, or a designer.

**Attach.** Scope resources line. Recruitment plan is for 5 to 8 problem interviews in leftover hours, not headcount.

**Trap.** "We will hire after the round."

**Q.** Key-person risk?

**A.** Total. If Sarah stops, the kit freezes. MIT means someone else can fork. That is the mitigation, not a backup employee.

**Attach.** LICENSE. Rollback: re-run `install-local.sh` from a known-good SHA.

**Trap.** "Process is documented so anyone can run it" as if that were a team.

---

## 6. Risks and mitigations

**Q.** What is the biggest product risk right now?

**A.** Install copy teaches the wrong finish line. Diligent people will stop at Customize, optional sync, or a catalog. 15 Oct is no-go until script and README step 3 are `/plan`. Mitigation is WK-1, under 2 hours, this sitting.

**Attach.** Live `install-local.sh` line 30. WK-1. Affinity Theme A.

**Trap.** Calling this "a messaging tweak" while still ranking catalogs as launch work.

**Q.** Platform / tech risk?

**A.** Cloud VMs do not mount `~/.cursor/plugins/local`. Teams can block local plugin imports. Cursor could change dest behavior. Mitigation: sync plus checker for Casey (phase 2), Riley paragraph plus `~/.cursor/skills` fallback, rollback SHA at T-24. We do not own Cursor chrome.

**Attach.** README Cloud Agents and Teams notes. Runbook rollback.

**Trap.** "We have an API partnership with Cursor."

**Q.** Concentration?

**A.** One user, one owner, one runtime (Cursor). If Avery prefers chat, the kit has no other logo to show. Mitigation is not a second segment this quarter. It is making the loop true for this operator and logging it.

**Attach.** OKR primary user. Positioning ICP.

**Trap.** "Design partners at ten companies" when n=0 interviews.

**Q.** Security / secrets?

**A.** `/ship` forbids `.env` and `git add .` on unrelated files, and forbids `--no-verify` unless asked. That is text, not a proof from production. A secrets commit is P0. Mitigation: `/review-diff` on every push this repo. Dirty-tree fixtures later, not instead of G3.

**Attach.** `skills/ship-the-change/SKILL.md`. US-5 AC.

**Trap.** SOC2, pentest, or "enterprise-ready."

**Q.** Regulatory?

**A.** None specific. Not a medical or banking product. Teams admin policy is the closest "rule," and it is Cursor's.

**Attach.** Riley recovery copy.

**Trap.** Inventing a compliance roadmap.

---

## 7. Use of funds

**Q.** How much are you raising and why?

**A.** $0. There is no raise. Do not issue a SAFE. Do not put a valuation on MIT markdown.

**Attach.** This answer. LICENSE.

**Trap.** A $500k seed "to hire and GTM" for a plugin the owner can patch in two hours.

**Q.** If you had extra hours, not dollars, where do they go?

**A.** 1) WK-1 copy until G3 passes. 2) One logged product-repo `/plan` and named-file `/ship`. 3) Timed E1. 4) Cloud checker before 14 Nov. 5) Leftover: problem interviews, not more strategy PDFs.

**Attach.** Priority matrix F1-F2. SMART goals A/B/C.

**Trap.** Allocating hours to Marketplace, SEO, or the remaining Playground queue before G3.

**Q.** What would make you take money later?

**A.** Not this quarter. A different product (billed, multi-seat, supported) would need a different license, a buyer, and metrics that do not exist. Until 31 Dec disappointment is yes and someone other than Avery depends on the loop, taking money would buy a company we have not chosen to be.

**Attach.** Scope anti-goals. GTM gate on distribution (80% plan rate first).

**Trap.** "We are keeping options open" as a substitute for the no.

---

## Data room (what actually exists)

| Ask | Exists | Path |
| --- | --- | --- |
| Pitch deck | No. Do not make one | Use messaging one-liner |
| Financials | N/A | $0 |
| Cap table | N/A | No entity |
| Customer list | Avery = owner | Do not list fake logos |
| Cohort dashboard | No | Session log, 0 rows |
| Security review | Skill text only | `ship-the-change` |
| Roadmap | Yes | `docs/okrs/q4-2026-roadmap.md` |
| Product demo | Terminal install plus `/plan` | After G3, not a catalog tour |

---

## How to use this file

If you are Sarah talking to yourself: skip to section 6 and WK-1. Diligence theater is C7.

If someone asks to invest: section 0, then 7. Then stop.

If someone asks whether to use the kit: sections 1 and 3. Send them to E1, not to this Q&A.
