# Insight statements: Work Kit first delivery

**Study:** Why install can succeed while Plan to Ship never runs, and whether install copy leads to `/plan`.
**Evidence date:** 16 September 2026 (product inspection plus planning session). Not an interview study.
**Participants:** Zero of the planned 5 to 8 Avery-like ICs. Owner diary n=1 (Sarah Scherer). One Cloud Agent working session. No recorded usability.
**Decision this informs:** 15 October 2026 go/no-go (G1 to G4), and whether the next session edits `install-local.sh` or writes another plan.
**Team constraints:** One owner. $0 paid GTM. Cursor chrome is not ours to redesign. Avery is primary. Cloud phase is 14 Nov. Do not invent NPS or Mixpanel. Do not mix owner rows into a fake n=8.
**Related:** [Recruitment](first-delivery-recruitment.md), [Beta survey](first-delivery-beta-survey.md), [Problem statement](../problem-statements/work-kit-first-delivery.md), [Feature priority](../okrs/q4-2026-feature-priority.md)
**Source prompt:** [Research insight statement writer](https://aiuxplayground.com/prompts/research-insight-statement-writer) (AI UX Playground)

The Playground prompt asked for themes from a recent study. Those brackets were empty. These statements use what is in the repo and the 16 Sep session log. They are not quotes from external testers. Rewrite this file after 5 interview completes or after G3 usability, whichever comes first.

**What is unknown.** Whether skippers exist outside this repo. Whether good copy produces `/plan` without a researcher. How often Teams hides the plugin card. How often Cloud Agent runs miss synced skills in live work.

---

## Insight 1. Install copy names the wrong finish line

**Headline.** Success is still "plugin visible," not `/plan`.

**Observation.** After a successful `./scripts/install-local.sh`, the terminal prints three next steps: Reload Window, confirm Work Kit under Customize, then "Optional for Cloud Agents: ./scripts/sync-user-skills.sh." The GitHub README clone path ends on Reload, Customize, then the Cloud Agents sync toggle. The checkout path ends on Reload, Customize, then a long inventory of slash names and catalog skills. `/plan` is not step 3 in the script. The README job line still says "plan first."

**Pattern.** This is the live install path for every desktop install, not a one-off branch note. It showed up in both the script echo and two README install lists on the same day we wrote a launch pack that requires step 3 to be `/plan`. n of external users on this copy: 0. n of install surfaces that omit `/plan` as the third beat: 3 (script, clone README, checkout README).

**Implication.** A person who does what the product tells them will stop at a plugin card, or go do cloud sync, or pick from a catalog list. They will not be told that first delivery is an accepted plan (or a tiny skip) in a product repo. The mental model the copy teaches is "installed = done." That is the failure named in the problem statement, produced by our own next-steps, not by a missing plugin file.

**Recommendation.** Change the three numbered beats so they match: Reload, Customize shows Work Kit, open a product repo and `/plan` (or `/debug` if something is already broken). Move cloud sync to the Cloud Agents section. Do not add a first-run UI. This is G3. It is F1 on the priority matrix. Do it before 8 Oct.

---

## Insight 2. We cannot tell if the loop runs because the log has no rows

**Headline.** The 80% target has no denominator.

**Observation.** `docs/okrs/session-log.md` has column headers and one blank placeholder row. There is no date, repo, `entry`, or `ship` filled for a product-repo sitting. Q4 OKRs still target 80% plan-or-tiny and 8 named-file ships.

**Pattern.** 0 of 1 operators has a completed row. The planned 5 to 8 interview sample is also 0. Every launch metric that uses the log is currently unmeasurable.

**Implication.** "First delivery is the default path" is a claim without a count. An empty log hides skip-to-chat the same way a plugin card hides it. The need is a written start for each sitting (`plan`, `tiny`, `debug`, or `neither`), not a richer analytics product.

**Recommendation.** Log the next real sitting in a product repo the same day G3 lands. Missing weeks count as 0 for O1 KR2. Do not impute. Do not wait for Mixpanel.

---

## Insight 3. Planning volume is up. Executable copy is unchanged.

**Headline.** More docs did not move step 3.

**Observation.** On 16 Sep the owner ran a chain of Playground templates (user flow, OKRs, launch pack, recruitment, survey, priority matrix). Those files state G3 is a no-go and F1 is rank 1. `install-local.sh` line 30 still says optional cloud sync. README install lists still do not make `/plan` the third beat.

**Pattern.** One working session, many artifacts, zero copy edits to the install echo. The same miss was written into the runbook, post-launch readout, recruitment plan, beta survey, and priority matrix.

**Implication.** The team already knows the UX problem. Extra synthesis does not change what Avery sees. Time spent on templates competes with the two files users actually follow (script, README).

**Recommendation.** Next session that touches this repo edits `install-local.sh` and README only, then reloads and tries `/plan` in a product repo. Stop adding Playground templates until G3 passes.

---

## Insight 4. Desktop install and Cloud Agents are different jobs sharing one numbered list

**Headline.** Optional sync as step 3 serves neither Avery nor Casey.

**Observation.** The kit copies to `~/.cursor/plugins/local/work-kit`. Cloud Agent VMs do not mount that directory. Skills for cloud work have to live under `~/.cursor/skills/` plus a Settings toggle. The Avery install list currently puts that cloud path in slot 3, labeled optional.

**Pattern.** This is how the product is built, not a survey theme. It is true for every Cloud Agent run. We have not watched Casey complete E7. We have not counted missed loads.

**Implication.** Avery is told a step that is not their first delivery. Casey is told the same step is optional, which matches the silent-miss path. One list cannot mark success for both surfaces.

**Recommendation.** Keep two lists. Avery: Reload, Customize, `/plan`. Casey: `sync-user-skills.sh`, checker fails if a core folder is missing, toggle on. Ship Casey copy after G3, in time for 14 Nov, not as Avery's third line.

---

## Insight 5. The skipper hypothesis is still untested with other ICs

**Headline.** We have a recruitment plan, not findings.

**Observation.** Recruitment and a beta survey exist as markdown. Screening questions, consent, and a 17 Sep to 14 Oct timeline are written. No screener responses, no interview notes, no usability videos, no survey completes.

**Pattern.** Sample size completed: 0. Planned completes: 5 to 8. Owner self-study is excluded from that n on purpose.

**Implication.** We do not know how other Cursor ICs start agent sessions after they install skills. We do not know if they would follow a `/plan` third step. Treating the hypothesis as validated would treat one operator as a panel.

**Recommendation.** Run problem interviews in leftover hours (they do not need G3). Run usability and the survey only after G3. Stop at 8. Do not delay the copy fix to wait for n=5. If 2 of 5 later say install-then-`/plan` is not ready to tell another IC, slip 15 Oct.

---

## So what (60 seconds)

Work Kit's stated job is plan first, then ship named files. The install path still congratulates a Customize card and offers optional cloud sync or a catalog of slash names. That is a UX defect in our copy, observed in the script and README on 16 Sep, not a missing feature and not a quote from a panel. We also have no session rows, so we cannot grade the 80% loop target. A stack of planning docs already names this as G3 and rank 1. None of them changed what the next installer will read. Other ICs have not been interviewed, so skippers in the wild are still a hypothesis. The decision is not "redesign onboarding." The decision is: edit the three next-steps before 8 Oct, log the next product-repo sitting, and keep cloud sync off Avery's list. If that copy is not shipped, 15 Oct is a no-go.

---

## Which insight most challenges the current roadmap

**Insight 1, backed by Insight 3.** The Q4 plan treats 15 Oct as a dated go-live for first delivery, with cloud on 14 Nov. Launch docs, OKRs, and the priority matrix already assume the product's next step is `/plan`. The live product still teaches a different next step. The challenged assumption is "specification equals shipped UX." Cloud work, fixtures, captures, and more research do not fix what the installer reads. Reassess the roadmap the hour F1 lands, not after another template.
