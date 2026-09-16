# Retention diagnosis: Work Kit (not SaaS churn)

**Product.** Work Kit (`work-kit`). $0 MIT Cursor plugin. Not a subscription. There is no cancel button, no dunning, no winback coupon.
**Retention curves.** None. Mixpanel: none. Session log: 0 filled rows on 16 Sep 2026. Day-1 / day-7 / day-30: undefined (denominator 0).
**Churn reasons pasted.** Interviews 0. Support tickets 0. Cancel surveys 0. What we have: product inspection of install copy, empty log, owner process (Playground chain vs line 30).
**Segments.** Avery (desktop IC, primary). Casey (Cloud Agents, same human, phase 2). Riley (Teams, recovery). Clone visitor (README). Owner-as-C7 (templates instead of the loop).
**Pricing changes.** None. Price stays $0. A discount cannot save a sitting that never started `/plan`.
**Related:** [Metrics](q4-2026-first-delivery-metrics.md), [Session log](../okrs/session-log.md), [ICP](../messaging/work-kit-icp.md), [WK-1](../tickets/wk-1-g3-install-copy.md), [Affinity](../research/first-delivery-affinity.md)
**Source prompt:** [Retention churn diagnosis](https://aiuxplayground.com/prompts/retention-churn-diagnosis) (AI UX Playground)

Blunt line: value decays at **numbered step 3**, before habit, before cloud, before any email. Messaging that does not change `install-local.sh` cannot fix it.

---

## Filled inputs (no empty paste)

| Field | Value |
| --- | --- |
| Curve | Blank. Do not draw a fake slope |
| Churn quotes | None. Do not use the PR/FAQ composite Avery line |
| Segment diffs | Architecture plus copy, not observed behavior counts |
| Price | $0, unchanged |

**What "retained" means here.** A later sitting in a product repo still uses `entry` = `plan`, `tiny`, or `debug`, then named-file `/ship`. Plugin files sitting in `~/.cursor/plugins/local/work-kit` is not retention. That is shelfware.

**What "churned" means here.** `entry` = `neither`, or no row when a sitting happened, or Customize empty and they stop, or cloud run with skills missing. Not "cancelled Pro."

---

## 1. Retention diagnosis (where value decays)

Value is the loop: accept a plan (or log tiny), review the real diff, ship named files. Decay is earlier than SaaS onboarding usually admits.

```text
minute 0   clone / install          copy can already send them to C1 or C3
minute 5   Reload, Customize        card visible = false success
sitting 1  first real change        chat implements; /plan never asked
sitting n  habit                    empty log hides skip
cloud      Casey                    local plugin absent; optional sync skipped
teams      Riley                    card never appears; kit looks dead
```

**Decay 1. Never activated (blocking).** 3 of 3 desktop install surfaces omit `/plan` as step 3. Script: optional cloud sync. Clone README: Cloud Agents toggle. Checkout README: catalog dump. A diligent new installer who follows instructions never reaches the loop. This is not churn after value. This is no value event.

**Decay 2. False activation.** Customize shows Work Kit. Owner (and copy) treat that as done. Same as C1 finish line. Messaging "success is a named-file commit" in a headline does not override a numbered list. Headline vs list is already a contradiction in one README.

**Decay 3. Sitting-start skip (hypothesized, uncounted).** Default chat is faster. After G3, if `neither` dominates, that is product (gate feels preachy), not copy. Today we cannot tell skip from unlogged. Empty log is not 0% churn. It is no instrument.

**Decay 4. Ship skip.** `/ship` exists and is strict. If sittings end in `git add .`, O3 fails even when `/plan` ran. Unobserved. Do not invent a secrets incident.

**Decay 5. Cloud silent miss.** VMs do not mount local plugins. Optional sync as Avery step 3 does not retain Casey. It trains Avery to skip `/plan`. Architecture cannot be emailed away.

**Decay 6. Teams policy.** Empty Customize. Recovery copy only. A save-play email to an admin is out of ICP and out of our control.

**Decay 7. Owner process churn.** 16 Sep: many docs, same echo. The operator "churns" from using the loop into writing about the loop. That is C7. A retention campaign that adds another report makes this worse.

**Messaging cannot fix:** Cursor chat being instant (C1). Cloud file roots. Teams Allow Local Plugin Imports. An empty log. Step 3 in stdout (only an edit to the script fixes that, which is copy-as-product, not a slogan).

---

## 2. Churn taxonomy with frequency

Frequencies are **surfaces and instruments**, not testers. Testers: 0 of 8.

| Code | Name | What it looks like | Frequency now | Severity |
| --- | --- | --- | --- | --- |
| CH-NA | Never activated | Follows install list, never `/plan` | 3/3 install surfaces teach it. Users observed: 0 | Blocking G3 / 15 Oct |
| CH-FA | False activation | Card visible, sitting in chat | Taught by copy. Log cannot confirm | Blocking first delivery |
| CH-NL | Not logged | Sitting happened, row blank | 1 placeholder row, 0 filled | Blocks O1 measurement |
| CH-NE | `neither` | Logged skip to implement | 0 rows | Unknown until log exists |
| CH-NS | No `/ship` | Plan ran, commit is junk or unlogged | 0 | P0 if `.env`. Unobserved |
| CH-CL | Cloud miss | Run without core skills | 0 cloud notes | Phase 2. High if we count O2 early |
| CH-TM | Teams empty | Script ok, Customize empty | 0 Riley completes | Recovery only |
| CH-C7 | Template substitute | Docs instead of echo | 1/1 owner session this chain | High for hours, not for clone visitors |
| CH-CA | Subscription cancel | Billing churn | n/a | Do not track |

**Do not report.** "32% churned in week 1." There is no cohort.

**Leading indicator after G3.** CH-NE rate among filled rows. If week +1 (22 Oct) is mostly `neither`, copy worked and the gate did not. Then the fix is tiny-skip honesty or accepting C1 for some sittings, not a longer README.

---

## 3. Segment-specific insights

**Avery (primary).** Risk is CH-NA and CH-FA from our copy, then CH-NL because she is the only logger. "I already know to `/plan`" does not retain clone-Avery and does not fill the log. Insight: owner skill is not product retention.

**Clone visitor.** Only sees README and stdout. CH-NA is almost certain until G3. Insight: they will not read the messaging framework. They will do item 3.

**Casey.** Same human, different root. CH-CL is structural. Putting sync on desktop step 3 is a retain-Casey tactic that churns Avery. Insight: two lists. Checker in November. Not a save email.

**Riley.** CH-TM is policy. Insight: do not spend retention hours here. FAQ paragraph. Hard disqualify as ICP.

**Catalog / CLI (A5/A6).** Never in the funnel. `npx skills add` without the plugin is not churn. It is a different job. Do not winback with "come back and `/plan`."

**Owner-as-C7.** Retained as a writer, churned as an operator. Insight: this diagnosis file is a CH-C7 risk. Next sitting must be WK-1 or the pattern continues.

---

## 4. Quick saves vs structural fixes

| Kind | Move | Fixes | Does not fix |
| --- | --- | --- | --- |
| Structural (now) | WK-1: step 3 = `/plan` | CH-NA, CH-FA for new installs | C1 speed. Teams policy |
| Structural (now) | Fill a log row the same day | CH-NL | Whether she actually planned |
| Structural (soon) | Tiny skip as honest state | Preachy-gate after G3 | People who want chat always |
| Structural (14 Nov) | Sync checker fail-closed | CH-CL | Local plugin on VMs |
| Structural (later) | `/ship` audit sitting | CH-NS | Someone ignoring the skill |
| Quick (allowed) | Calendar block for the copy edit | CH-C7 this week | Clone visitors |
| Quick (allowed) | Identical three beats, no extra FAQ novel | Drift | Architecture |
| Fake save (forbid) | Discount, pause plan, "we'd love you back" email | Nothing | Everything |
| Fake save (forbid) | In-app modal we do not own | Nothing | Cursor chrome is not ours |
| Fake save (forbid) | NPS survey as winback | Nothing | Survey blocked until G3 |

**Rule.** If the save does not change stdout or a log row, it is theater.

---

## 5. 30-60-90 day plan

Clock starts 16 Sep 2026. Aligns with existing dates, not a SaaS onboard sequence.

**Days 0-30 (through ~16 Oct, includes 8 Oct SLC and 15 Oct go-live).**

- Ship G3. Without this, there is no retention to plan.
- One go-live log row: plan or tiny plus named-file ship. Day 1 target: that row exists.
- Time E1 twice if not done.
- If G3 yellow on 8 Oct: slip 15 Oct. Do not "retain" a launch that taught skip.
- Do not field the beta survey. Do not start a 30-day email drip.

**Days 31-60 (through ~16 Nov, includes 22 Oct check and 14 Nov cloud).**

- Week +1 (22 Oct): denominator not zero. At least 3 logged sittings. Watch CH-NE vs plan/tiny.
- If KR2 still 0: do not add channels. Habit, not GTM.
- Casey: checker + split lists. Fail closed. Do not count cloud as retained Avery.
- Interviews only leftover hours. Usability only on new copy.

**Days 61-90 (through ~16 Dec, toward 31 Dec grade).**

- 8 named-file ships and 80% plan-or-tiny are the retention grade.
- Disappointment question: would you miss `/plan` through `/ship`?
- If `neither` is the majority: structural gate work, not copy polish.
- Still no cancel-save program. Still $0.

**After 90.** Re-read this file only if the log has rows. A second retention memo with zeros is CH-C7.

---

## 6. Email / in-app save plays

There is no in-app. Cursor does not give us a modal. "In-app" for us is **stdout and README numbered lists**.

**Play 1. Install echo (the only in-product save).** After successful copy, three beats ending in `/plan`. This is WK-1. It is not a winback. It is first value.

**Play 2. Calendar note to Avery (email A, already in pilot LOI).** Subject: next sitting is WK-1. Not "we miss you."

**Play 3. Clone visitor (only if they write).** One paragraph: Reload, Customize, `/plan` in a product repo. If they wanted a catalog, send them to the list. Do not sequence-mail them.

**Play 4. After G3, if she logs `neither` twice.** Note in the log, then try tiny skip on the next obvious change. If she wants chat every time, do not guilt. The kit is optional. That is honest churn.

**Do not send.**

- "Your trial ends in 3 days."
- "Here's 20% off."
- "A quick NPS would help us improve."
- "New skills this week" catalog dump (feeds CH-NA).
- Save-play that mentions cloud sync as desktop step 3.

---

## 7. Metrics to watch weekly

Read [metrics](q4-2026-first-delivery-metrics.md). Until 8 Oct the weekly read is almost only G3.

| Weekly | Metric | Decision if bad |
| --- | --- | --- |
| Now | G3 grep: `Optional for Cloud Agents` absent from script success echo | Do WK-1. Do not discuss retention |
| Now | Session log filled rows this week | 0 means CH-NL. Log the sitting, do not impute |
| After first row | Plan-or-tiny rate | Below 80% with n small: watch, do not panic. n=0: ignore the rate |
| After first row | Count of `neither` | Rising after G3: gate problem, not copy |
| After first row | Named-file ships (cumulative toward 8) | 0 by 22 Oct: process miss |
| After G3 | Secrets in a push | P0. Stop. Not a retention KPI |
| 14 Nov+ | Cloud `skills_loaded` fail | Checker. Do not count as Avery churn |
| Never | MAU, NPS, MRR, email open rate | Kill. No decision uses them |

**Failure mode.** Treating Customize-visible as retained. That is CH-FA, the current default.

---

## So what

Retention is not a drip. Clone visitors churn at item 3 because we tell them to. Avery's loop is unmeasured because the log is empty. Cloud and Teams are different jobs. Price is not the lever.

Structural save this week: edit the echo. Then write a row. Messaging cannot substitute. If this file is used to delay WK-1, it has become CH-C7.
