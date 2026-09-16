# SWOT: Work Kit first delivery (Q4 2026)

**Product / company.** Work Kit (`work-kit`). Personal MIT Cursor plugin. One operator: Sarah Scherer. Not a company. Not a billed product.
**Market.** How a Cursor sitting starts and finishes. Not "AI coding platforms." No TAM. No share.
**Key competitors.** Jobs, not brands: C1 default chat, C2 skills CLI, C3 GitHub skill lists, C4 Continual Learning, C5 Marketplace GitHub / Create Plugin, C6 copy kit into each repo, C7 catalog dumps into this kit. Desk analysis 16 Sep 2026. Interviews 0.
**Strategic goal.** Make Plan to Ship the default path: G3 copy by 8 Oct, 15 Oct go-live if G1-G4 pass, 80% plan-or-tiny and 8 named-file ships by 31 Dec. Decide: next sitting edits install copy, not another template.
**Time horizon.** Near-term: 16 Sep to 31 Dec 2026. Longer only if the 31 Dec disappointment question is yes. Do not use this SWOT to justify 2027 platform work.
**Related:** [Positioning](work-kit-positioning.md), [Competitive UX](work-kit-competitive-ux.md), [Priority](../okrs/q4-2026-feature-priority.md), [WK-1](../tickets/wk-1-g3-install-copy.md)
**Source prompt:** [SWOT analysis](https://aiuxplayground.com/prompts/swot-analysis-framework) (AI UX Playground)

"How to use" replaces the prompt's "leverage." We are not squeezing a market. We are pointing numbered step 3 at `/plan`.

---

## Analysis context (filled)

| Field | Value |
| --- | --- |
| Internal vs external line | Internal: this repo, copy, skills, owner time, log. External: Cursor chrome, chat default, Marketplace, Teams policy, Cloud VM file roots, clone visitors |
| What SWOT will not do | Invent ARR, NPS, share, or tester quotes. Rank a marketplace listing. Fund ads |
| Live fact that binds the matrix | G3 fails. `install-local.sh` line 30 still prints optional cloud sync as step 3 |

---

## 1. Strengths (internal, positive)

### S1. Named delivery loop already exists (Product)

- **Strength.** `/plan`, `/debug`, `/review-diff`, `/ship` match skill names. Tiny skip is a first-class log state in the spec.
- **Evidence.** Skill folders and slash commands in the plugin. `ship-the-change` forbids `git add .` on unrelated files and `--no-verify` unless asked.
- **Advantage vs jobs.** C1 has no accept gate. C3 has no ship bar. C4 does not stage git. C2 may install SKILL.md without these slashes.
- **How to use.** Point install step 3 at `/plan`. Do not rebuild the loop. Do not add a 21st slash to "complete" first delivery.

### S2. Real-directory user-scope install (Technology)

- **Strength.** `install-local.sh` copies to `~/.cursor/plugins/local/work-kit`. Cursor ignores a checkout symlink. Dest is once per machine.
- **Evidence.** Script dest, rsync/tar copy, README "do not copy into each repo."
- **Advantage.** Beats C6 vendoring (drift, merge fights). Beats "hope a symlink works."
- **How to use.** Keep dest unchanged in WK-1. Sell "once, user scope" in README. Do not spend the sitting rewriting copy mechanics.

### S3. Honest complements, not a fake platform (Positioning)

- **Strength.** Messaging already sends shopping to lists, facts to Continual Learning, PRs to GitHub plugin. `STARTER_PLUGINS.md` exists.
- **Evidence.** Messaging snapshot table. Positioning send-to table. GTM cut press and ads.
- **Advantage.** We do not have to out-catalog C3 or out-remember C4.
- **How to use.** Keep catalogs behind `install-catalog-skills.sh --preset`. Keep C4/C5 in the starter list. Refuse comparison SEO this quarter.

### S4. Strict ship text (Product / risk)

- **Strength.** Named-file `/ship` is written as a refuse-junk skill, not a slogan.
- **Evidence.** Skill file. US-5 AC. Secrets in a push = P0 in launch docs.
- **Advantage.** C1 culture is `git add .`. We can be the sitting that does not scoop `.env`.
- **How to use.** After G3, prove it with one logged `/ship` and a `/review-diff`. Do not claim a clean-commit rate before the log has rows.

### S5. One owner can change stdout in under 2 hours (Team / process)

- **Strength.** No design-system queue. No legal. MIT. $0 GTM. WK-1 is copy in two files.
- **Evidence.** [WK-1](../tickets/wk-1-g3-install-copy.md) estimate. Scope freeze already names F1.
- **Advantage.** C3 lists cannot rewrite Cursor chat. We can rewrite our echo today.
- **How to use.** Spend the next sitting on F1, not on SWOT follow-ups. Bus factor is also W4. Do not hire a narrative. Patch the echo.

### Top 3 strengths to use

1. **S1 loop skills.** They are the only unique claim. Useless if undiscoverable.
2. **S2 real install.** Already works. WK-1 must not "fix" dest.
3. **S3 complements.** Stops us from fighting the wrong job.

S4 and S5 support those three. S5 is how F1 actually happens. S4 is how O3 stays true after copy lands.

---

## 2. Weaknesses (internal, negative)

### W1. Install copy names the wrong finish line (Product / copy)

- **Weakness.** Success echo and README numbered lists do not make `/plan` step 3.
- **Evidence.** Script L30 optional cloud sync. Clone README item 3 is the Cloud Agents toggle. Checkout README items 3-4 are catalogs. `install-work-kit` skill matches the miss.
- **Impact.** We lose to C1 at minute one. Stated positioning is false in stdout. 15 Oct G3 is no-go.
- **Mitigation.** WK-1 this sitting. Same three beats in script and both README lists. Move sync to Cloud Agents.

### W2. Empty measurement (Process)

- **Weakness.** Session log has no filled row. Survey 0. Interviews 0.
- **Evidence.** `docs/okrs/session-log.md` placeholder. Research gate files.
- **Impact.** Cannot grade 80% or 8 ships. Easy to confuse "we wrote OKRs" with "the loop runs."
- **Mitigation.** Log the next product-repo sitting the day G3 lands. Do not buy Mixpanel. Do not impute.

### W3. Headline and numbered steps disagree (Copy / IA)

- **Weakness.** README says plan first, then numbers a different finish.
- **Evidence.** Same file: job sentence vs clone/checkout lists. Messaging three beats vs live echo.
- **Impact.** Diligent clone visitors follow the list, not the slogan. Looks like C3 on first-run.
- **Mitigation.** Same as W1. Do not add a fourth explanatory paragraph instead of editing the list.

### W4. Single operator, Playground queue as competing work (Team)

- **Weakness.** Sarah is eng, QA, PM, and research. Template chain consumes the hours that could patch G3.
- **Evidence.** 16 Sep affinity Theme E: many artifacts, line 30 unchanged. This SWOT is another artifact.
- **Impact.** C7 inside the company. Spec piles up. Avery still sees old step 3.
- **Mitigation.** Treat Playground fills as leftover hours only after G3. Scope freeze: templates are not F1.

### W5. Local plugin invisible on Cloud Agent VMs (Architecture, owned constraint)

- **Weakness.** `~/.cursor/plugins/local` does not mount on cloud VMs. Sync is required and easy to skip.
- **Evidence.** Cursor platform behavior. README Cloud Agents section. Script currently mislabels that as desktop step 3.
- **Impact.** Casey silent miss. Putting sync on Avery's list does not fix Casey and harms Avery.
- **Mitigation.** Split lists (F8) after G3. Checker (F7) before 14 Nov. Do not pretend the plugin card exists on the VM.

### W6. Teams can block local imports (Policy we do not own)

- **Weakness.** Customize can stay empty on Teams/Enterprise.
- **Evidence.** README recovery note. Riley is recovery-only this quarter. 0 Riley completes watched.
- **Impact.** Install "succeeds" in the terminal and fails in the UI. Out of Avery spine. Support trap if we market to teams.
- **Mitigation.** Keep Riley as a paragraph. Fallback `~/.cursor/skills`. Do not make Teams the ICP.

### W7. Unvalidated skipper hypothesis (Research)

- **Weakness.** We have not heard other ICs. Owner "I already `/plan`" can hide copy bugs.
- **Evidence.** Recruitment plan, 0 of 8. Affinity Theme G.
- **Impact.** Risk of overfit to one operator. Risk of delaying F1 for a panel we do not have.
- **Mitigation.** F1 without interviews. Problem interviews in leftover hours. Usability after G3 only.

### Top 3 weaknesses to address

1. **W1 copy.** Blocks G3. Fixes W3 at the same time. Under 2 hours.
2. **W2 log.** Blocks O1 grade. First row after F1, same day if possible.
3. **W4 process.** If templates keep winning, W1 never closes.

W5 is real but dated 14 Nov, and the wrong fix (Avery step 3 = sync) is how W1 happened. W6 is recovery copy, not this week's patch. W7 must not become a gate.

---

## 3. Opportunities (external, positive)

External means Cursor, clone visitors, and adjacent jobs. Not "we should write more docs."

### O1. Nobody numbers `/plan` after install (Job to be done)

- **Opportunity.** C1 says chat. C3 says browse. C4 says remember. The "I installed something, what is the next sitting?" job is open.
- **Evidence.** Competitive UX feature table: install next-step is `/plan` is N today for us and N for them. Desk, not a survey.
- **Impact.** Every future clone, including future-Avery. Not a market dollar figure.
- **How to capture.** Three beats. WK-1. That is the whole capture plan.
- **Timing.** Now through 8 Oct. After 15 Oct the miss is a launched miss.

### O2. Cloud Agents need a skills root, not a plugin card (Platform)

- **Opportunity.** Platform split is a reason Casey needs a clear list and a checker. Complements desktop rather than replacing it.
- **Evidence.** Local plugins do not mount. Sync script already exists.
- **Impact.** Six logged cloud runs is O2. Only after F7 is green.
- **How to capture.** F7 F8 F10 in November. Keep sync off Avery step 3.
- **Timing.** Window opens after G3. Closes if we teach optional sync as desktop success and Casey still skips.

### O3. Tiny work can keep C1 speed without giving up the bar (Behavior)

- **Opportunity.** Impatient sittings are real. US-4 tiny skip logs honesty instead of a fake six-section plan.
- **Evidence.** Spec and stories. Not measured in the log yet.
- **Impact.** Reduces "preachy" objection. Protects plan gate for non-tiny work.
- **How to capture.** After G3, log tiny vs plan. Do not make chat the default in copy.
- **Timing.** Same quarter as O1. Do not ship tiny as numbered install step 4.

### O4. Owned GitHub README is the only channel that matters (Distribution)

- **Opportunity.** Clone visitors already land on README. GTM is $0 by choice, not by lack of ads.
- **Evidence.** GTM owned-channel table. No email list.
- **Impact.** One page change is the go-to-market.
- **How to capture.** Identical three beats in README and echo. Optional GitHub release notes after G3, Template B, no social.
- **Timing.** 8 to 15 Oct message freeze.

### O5. Complements stay installable at user scope (Ecosystem)

- **Opportunity.** Marketplace plugins Avery already uses do not conflict with a user-scope loop. We can tell people to use both.
- **Evidence.** `STARTER_PLUGINS.md`. Positioning battle cards C4/C5.
- **Impact.** Avoids a lose-lose "replace Continual Learning" fight.
- **How to capture.** Keep the starter table. Do not re-implement `AGENTS.md` memory.
- **Timing.** Ongoing. No extra build this week.

### Top 3 opportunities to pursue

1. **O1 numbered `/plan`.** Only capture that moves 15 Oct.
2. **O4 README as GTM.** Same sitting as O1.
3. **O2 Casey path.** After G3, before 14 Nov.

O3 and O5 are rules, not projects. Do not open a "tiny skip platform" or a "partner Marketplace" workstream.

---

## 4. Threats (external, negative)

### T1. Default chat always available (Competition / C1)

- **Threat.** Zero-friction implement wins any sitting where step 3 is vague or `/plan` feels slow.
- **Evidence.** Chat is the host app. Positioning: functionally 100% of Avery's fallback. Testers watched: 0, still true as architecture.
- **Impact.** High. First delivery never starts.
- **Likelihood.** High until G3. Medium after G3 if copy is right and Avery still prefers speed (untested).
- **Mitigation.** Copy. Tiny skip for obvious work. Do not contest C1 on time-to-first-edit for non-tiny work.

### T2. Catalog and CLI confuse "installed" (Competition / C2 C3 C7)

- **Threat.** `npx skills add` or a list README feels like Work Kit. Checkout catalog dump teaches shopping as E1.
- **Evidence.** User flow E3. Live README checkout items 3-4. Playground queue as C7.
- **Impact.** High for clone visitors. Medium internal (hours).
- **Likelihood.** High today (our own copy). Medium after G3 if we dump catalogs again.
- **Mitigation.** VF-2 forbidden strings. Preset behind a script. Stop template-as-progress until G3.

### T3. Cursor changes plugin or cloud paths (Platform)

- **Threat.** Dest ignored, local imports deprecated, or a native plan-to-ship bar ships in Cursor.
- **Evidence.** Cloud VM already ignores local plugins. Teams toggle already exists. Native bar is hypothetical.
- **Impact.** High if dest breaks. Medium if Cursor owns the loop (our category shrinks to named files plus log).
- **Likelihood.** Cloud miss: high (already true). Dest break: unknown, treat as slip-cloud not rewrite-F1. Native bar: low this quarter, watch.
- **Mitigation.** Fail closed on cloud checker. Rollback is re-run install from a known-good SHA. Do not pre-build a Marketplace listing.

### T4. Secrets or dirty-tree ship (Habit / C1 culture)

- **Threat.** Even with skill text, a sitting can still stage `.env` if someone ignores `/ship`.
- **Evidence.** Skill forbids it. Log has 0 ships to prove compliance. P0 in runbook.
- **Impact.** High if it happens (trust, not TAM).
- **Likelihood.** Medium until a logged named-file ship exists. Lower after US-5 sitting.
- **Mitigation.** `/review-diff` on every push. Do not `--no-verify` unless asked. Dirty-tree fixtures later (F11), not instead of G3.

### T5. Teams policy and Riley support creep (Regulation-like / seat policy)

- **Threat.** Empty Customize on a company seat. Pressure to vendor C6 "so it works for the team."
- **Evidence.** README Teams note. Scope: Riley recovery only.
- **Impact.** Medium if we chase it. Low if we keep Avery as spine.
- **Likelihood.** Low for this operator. Higher if we pitch internally at a company.
- **Mitigation.** Say the admin toggle early. Do not take a Teams pilot this quarter (see later Playground LOI: refuse).

### T6. Platform memory looks like the loop (Adjacent / C4)

- **Threat.** Avery treats Continual Learning as Work Kit and never `/plan`.
- **Evidence.** Both are user-scope Customize plugins. Different jobs.
- **Impact.** Medium. Silent substitution.
- **Likelihood.** Medium if copy stays "confirm Work Kit" without `/plan`.
- **Mitigation.** Same as T1/W1. Messaging: facts vs loop. Use both.

### Top 3 threats to monitor

1. **T1 chat at minute one.** Defense is G3 copy, not a speed feature.
2. **T2 catalog/CLI confusion.** Defense is our own lists, today.
3. **T3 Cursor path change.** Defense is checker plus rollback SHA, not a rewrite of dest during WK-1.

T4 is operational after F1. T5/T6 are copy and ICP discipline.

---

## 5. SWOT matrix and strategic implications

| | Strengths | Weaknesses |
| --- | --- | --- |
| **Opportunities** | **SO.** Use S1 (loop exists) and S2 (install works) to take O1/O4: three beats in echo and README this sitting. Use S3 so O5 stays "use both," not a build. | **WO.** Fix W1/W3 so O1 is true in stdout. Fix W4 so O1 gets hours. Do not use W7 (no testers) as a reason to skip O1. Split W5 after G3 to take O2. |
| **Threats** | **ST.** S1 accept gate and S4 ship text are the defense against T1/T4, but only if discoverable. S3 send-to table defends T2/T6 ("that job is a list / Continual Learning"). S5 speed of copy defends T1 this week. | **WT.** Do not mitigate T1 by adding catalog names (feeds T2). Do not mitigate T3 by putting sync on Avery step 3 (feeds W1). Do not mitigate T5 by C6 vendoring. If hours are scarce (W4), drop SWOT-like templates and patch W1. |

**Read of the matrix.** SO is a two-file change. WT is the failure mode we are already in: fighting cloud and catalogs with Avery's third beat, and fighting uncertainty with more docs.

---

## 6. Strategic recommendations

**Invest in.** WK-1 / F1 / G3 copy. Then one product-repo `/plan` and named-file `/ship`, logged (W2). That is the SO play. Hours, not dollars. $0.

**Defend against.** T1 by making step 3 `/plan`. T2 by removing catalog dumps from numbered install. T3 by recording a rollback SHA at T-24, not by delaying copy.

**Address urgently.** W1 (and W3 with it). Then W4: stop treating this SWOT as progress. W2 the same day if the sitting has time.

**Monitor.** Cursor Cloud file roots and any native plan-to-ship UI (T3). Log `neither` rate after G3 (T1 product vs copy). Checkout README regressions (catalog as step 3). Do not monitor NPS, ARR, or Marketplace rank.

**Do not invest in.** Comparison SEO. Product Hunt. Eating `AGENTS.md`. First-run UI. Marketplace listing. A 2027 platform. Another Playground synthesis before G3.

**Decision this SWOT supports.** Next coding sitting opens `scripts/install-local.sh` and README. It does not open a new strategy file. Re-run SWOT only after G3 plus a week of log rows, or if Cursor ships a native loop.

---

## One-line strategy

Use the loop we already wrote. Stop losing the first minute to chat and catalogs because our own step 3 says so.
