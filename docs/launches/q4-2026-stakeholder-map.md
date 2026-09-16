# Stakeholder map: Work Kit first delivery

**Project.** Work Kit first delivery (Plan to Ship as the default path).
**Goal.** After one user-scope install, Avery's next sitting is `/plan` (or `/debug` if broken) through named-file `/ship`, logged. Gate: G3 copy match by 8 Oct, or slip 15 Oct.
**My role.** Sarah Scherer. Owner, only employee, only approver. Authority is total and useless as an org chart: there is no one to escalate to. Approval means doing the sitting.
**Timeline.** 16 Sep 2026 (inspection) through 31 Dec 2026 (grade). Phase 1 go-live 15 Oct or slip. Cloud 14 Nov.
**Key decisions.** (1) Patch `install-local.sh` and both README lists this sitting, yes or no. (2) Go or no-go 15 Oct. (3) Whether cloud copy may appear as Avery step 3 (already no). (4) Whether to field interviews or a survey before G3 (already no).
**Related:** [Stakeholder presentation](q4-2026-stakeholder-presentation.md), [Tenets](../messaging/work-kit-tenets.md), [Scope](q4-2026-first-delivery-scope.md), [Comms](q4-2026-first-delivery-comms.md), [ICP](../messaging/work-kit-icp.md), [Focus metrics](../okrs/q4-2026-focus-metrics.md)
**Source prompt:** [Stakeholder mapping](https://aiuxplayground.com/prompts/stakeholder-mapping-template) (AI UX Playground)

This is not a cross-functional initiative. There is no design org, eng team, legal, sales, or exec staff. Mapping fake directors would invent a company. The useful map is hats on one person, plus a few surfaces we do not own.

Do not schedule a stakeholder workshop. Next sitting is WK-1 copy, not a RACI review.

---

## 1. Stakeholder identification

People first. Surfaces and personas second. No invented names.

### Sarah Scherer (every hat)

| Hat | Function | Relationship | Level | Authority |
| --- | --- | --- | --- | --- |
| Operator (Avery) | Uses Cursor daily | Primary user. Does the sitting the kit is for. | IC | Does the work. Cannot be delegated. |
| Eng | Owns `install-local.sh`, dest, hooks, `/ship` | Only person who can patch stdout. | IC | Patches. Same commit as copy. |
| Copy | README lists, script echo | Writes the three beats. | IC | Same commit as eng. |
| PM | OKRs, dates, WK-1 | Wrote the scoreboard. Can hide behind more docs. | IC playing PM | Sets 8 Oct / 15 Oct / slip. |
| Exec (go/no-go) | Time, not ROI | Grades 15 Oct at 09:00 and 31 Dec. There is no ARR. | IC playing exec | Approver of dates. Not of budget (there is none). |

One human. If RACI lists five names, it is lying.

### Not people, still on the map

| Name | Function | Relationship | Level | Authority |
| --- | --- | --- | --- | --- |
| Clone visitor | GitHub README | Follows numbered install lists. Has never met Sarah. | IC (unknown) | Informed only, via copy. Cannot approve. |
| Casey (future self on Cloud Agents) | Same human, different runtime | Needs sync + checker. Local plugins do not mount on VMs. | IC | Informed until 14 Nov. Must not own Avery step 3. |
| Riley (Teams/Enterprise) | Policy-blocked install | Recovery paragraph only. Not a buyer. | IC | Informed if F15 ships. Cannot unblock Teams policy. |
| Cursor (the host app) | Platform we do not own | Chrome, Customize, Cloud Agent VMs, skill loading. Does not know this kit exists. | n/a | De facto high power. Not an approver we can book. |
| GitHub (Ses2905/cursor-skills) | Public home | Hosts clone path. Stars are not a metric. | n/a | Informed by commits. Not a stakeholder meeting. |
| Playground queue / C7 | Process trap | Fills templates that feel like alignment. | n/a | Low formal power. High ability to steal the sitting. |

**Out of the map (do not add).** Investors, design-partner companies, legal, sales, marketing, a VP of Product, interview recruits (n=0), paid pilots (refused).

---

## 2. Power / interest grid

Power here means "can change 15 Oct or stdout." Interest means "will notice if first delivery fails."

### High power, high interest (manage closely)

**Who.** Sarah Scherer, all hats collapsed. There is no committee.

**Strategy.** Do not "engage deeply with regular updates." Open the script. The internal conflict to manage is PM/planner (more docs) vs eng/operator (patch line 30). Weekly 15-minute review from [focus metrics](../okrs/q4-2026-focus-metrics.md). Until G3, that review is 5 minutes: gate plus one decision.

### High power, low interest (keep satisfied)

**Who.** Cursor the platform.

**Strategy.** Do not email Cursor. Do not wait for a first-run UI we cannot ship. Keep satisfied by staying inside chrome we already have: Reload, Customize User, slash commands, git. Do not bet 15 Oct on a Marketplace listing or a host-app change.

### Low power, high interest (keep informed)

**Who.** Clone visitors (via README). Casey after 14 Nov (via Casey README + checker).

**Strategy.** Inform through install copy, not a newsletter. Do not recruit their enthusiasm as a substitute for G3. Clone visitors only see numbered lists. If item 3 is sync, they are informed of the wrong job.

### Low power, low interest (monitor)

**Who.** Riley. GitHub star-gazers. Future interview recruits. Marketplace. This Playground queue.

**Strategy.** Minimal effort. Riley gets a recovery paragraph in phase 3 if at all. Do not monitor star counts. The queue is a process risk, not a stakeholder to please. Completing it is not first delivery.

---

## 3. Stakeholder analysis (high power or high interest)

Hats, not a staff directory. Preferred communication is always: the file, the script, the log. There is no Slack org.

### Operator (Avery)

- **Cares about.** Next sitting starts clean. Plan or tiny, then named-file ship. Not a catalog.
- **Needs.** Item 3 is `/plan`. Customize shows Work Kit. `/ship` will not scoop `.env`.
- **Concerns.** "I already know to `/plan`," so copy feels optional. That is how clone visitors skip.
- **Address.** Write the echo for the stranger, including future-Sarah on a cold clone. Do not skip F1 because the owner has muscle memory.
- **Success.** A logged product-repo row: `entry` plan or tiny, `ship` named files. E1 or E2 under 10 minutes after copy.
- **Communication.** Session log plus chat commands. No status email to self.
- **Influence.** Drives the north star. If Avery skips, the rate is a miss.
- **History.** Owner installed via E2. Loop not yet logged. Interviews 0.

### Eng

- **Cares about.** Script, dest path, hooks, `/ship` staging.
- **Needs.** One change that makes stdout match US-1. Then `/review-diff`.
- **Concerns.** "Copy is fine, the skill is the product." Line 30 disproves that.
- **Address.** Tenet 1: echo is the product. WK-1 is an eng sitting, not a docs sitting.
- **Success.** `git grep` for `Optional for Cloud Agents` on the script echo is empty. G3 pass.
- **Communication.** The diff. Not a design review.
- **Influence.** Only hands that can change stdout.
- **History.** Wrote `install-local.sh` as a real copy (not a checkout symlink). Left step 3 as cloud sync.

### Copy

- **Cares about.** Three identical numbered beats on script and both README lists.
- **Needs.** Same commit as eng. No README-only patch.
- **Concerns.** Catalog should be visible (checkout README items 3-4 today). That is C3.
- **Address.** Scope freeze: catalog dumps are out. Item 3 is `/plan`.
- **Success.** Clone README, checkout README, and echo match. Step 3 contains `/plan` and `/debug` if broken.
- **Communication.** The three lists side by side in the diff.
- **Influence.** Clone visitors believe this hat.
- **History.** README drifted from the script. Both are wrong vs US-1.

### PM

- **Cares about.** 80% plan-or-tiny, 8 ships, dates held or slipped in public.
- **Needs.** A denominator in the log after go-live. G3 before 15 Oct.
- **Concerns.** "We should research first." Also: filling templates looks like PM work.
- **Address.** Tenet 6: empty stays empty. Interviews after G3. This map is not a KR.
- **Success.** Focus OKRs Objective 1 then Objective 2. Not a stack of markdown.
- **Communication.** Weekly 15-min agenda. Session log. `sed -n '25,31p' scripts/install-local.sh`.
- **Influence.** Can slip 15 Oct. Can also stall by opening another prompt.
- **History.** Wrote OKRs, SMART, scope, WK-1. Did not change stdout.

### Exec (go/no-go)

- **Cares about.** Time. Whether 15 Oct is honest. There is no ROI slide.
- **Needs.** A yes or a slip, not a yellow "we planned."
- **Concerns.** "Is this big enough to present?" Also: shipping a skippable loop to hit a date.
- **Address.** No-go until G3. Slip rather than fake a launch. Do not ask for budget.
- **Success.** 15 Oct 09:00: G1-G4 pass, or a written slip date. 31 Dec grade on the star.
- **Communication.** The runbook, not a board deck. 12-min stakeholder cut if she needs a script.
- **Influence.** Approves dates. Same person as PM. Conflict is date-pride vs tenet 1.
- **History.** Set 15 Oct / 14 Nov / 31 Dec. Has not yet applied the no-go rule to line 30.

### Clone visitor

- **Cares about.** What to type after clone. Will not read `docs/`.
- **Needs.** Numbered lists that end on `/plan`.
- **Concerns.** Cloud Agents toggle and catalog lists look official. They are the wrong job.
- **Address.** Change README item 3. Do not add a "welcome" campaign.
- **Success.** They reach Customize, then `/plan`, without writing to Sarah.
- **Communication.** README only.
- **Influence.** None on dates. Total on whether stated positioning survives minute one.
- **History.** Unknown n. Do not invent one.

### Casey (phase 2)

- **Cares about.** Core skills loaded on a VM that cannot see `~/.cursor/plugins/local`.
- **Needs.** Sync checker that fails closed. Six runs after 14 Nov.
- **Concerns.** Being forgotten. Counter-concern: being promoted into Avery step 3.
- **Address.** Dated phase. Keep out of the numbered Avery list until G3 is green.
- **Success.** Checker exit fail if a core folder is missing. Then 6 runs that loaded plan or debug.
- **Communication.** Casey README, not Avery item 3.
- **Influence.** Can steal the third beat if PM panics about cloud.
- **History.** Sync script exists. Checker does not. Optional footnote is the live bug.

---

## 4. RACI matrix

R = does the sitting. A = yes/no on the date or the merge. C = hat that must look at the diff. I = learns through an artifact, not a meeting.

Every R and A is Sarah. Split by hat so the conflict is visible.

| Decision / deliverable | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| F1 / G3 copy (script + both README lists) | Eng | Exec | Copy, Operator | Clone visitor (README) |
| 15 Oct go/no-go (or slip) | PM | Exec | Operator (can we log a row?) | Casey (wait), Riley (wait) |
| Keep cloud out of Avery step 3 | Copy | Exec | Casey hat (date only) | Clone visitor |
| Day-1 logged `/plan` + named-file `/ship` | Operator | PM | Eng (`/review-diff`) | Future log readers (Sarah) |
| Secrets in a push (stop the line) | Eng | Exec | Operator | No one else. Rotate. |
| Cloud checker + 6 runs (after 14 Nov) | Eng | PM | Casey | Operator (do not change step 3) |
| Field interviews or beta survey | PM | Exec | Operator | Recruits (none yet) |
| Capture / O4 / Marketplace | none this quarter | Exec (parked) | none | none |
| Another Playground template | C7 (do not assign R) | Exec (should refuse) | none | none |

A filled RACI row is not a signature. Scope section 9 still says: signing a doc does not replace editing `install-local.sh`.

---

## 5. Engagement plan

### Manage closely (Sarah)

- **Frequency.** Until G3: 5 min when she sits down. After go-live: weekly 15 min. Monthly forecast 31 Oct, 30 Nov.
- **Format.** Session log plus `sed -n '25,31p' scripts/install-local.sh`. No slide deck. No Slack huddle with herself.
- **Messages.** Gate red or green. Denominator this week. One decision: copy, a product-repo loop, cloud checker, or slip. Not "another template."
- **Escalate.** There is no up. Escalation is a calendar block the same day, or a written slip. If the weekly review discusses research n, it already failed.

### Keep satisfied (Cursor platform)

- **Frequency.** Never as a meeting. Re-check only when chrome behavior breaks install (Customize missing, VM still no local plugins).
- **Format.** Product inspection. Not a support ticket to Cursor about Work Kit.
- **Messages.** Stay inside Reload / Customize / slash commands.
- **Escalate.** If Cursor removes local plugins, first delivery is a different product. Do not pretend a stakeholder update will fix that.

### Keep informed (clone visitors, Casey)

- **Frequency.** Clone visitors: on each install-copy commit. Casey: when F7/F8 land, not weekly.
- **Format.** README numbered lists. Casey README with pass/fail boxes. No email list (there is none).
- **Messages.** Three beats. Cloud waits. Do not ask them to "stay tuned."
- **Escalate.** If a clone visitor files an issue that item 3 is still sync, that is G3 still red. Patch. Do not reply with a strategy doc.

### Monitor (Riley, queue, stars)

- **Frequency.** Riley: when F15 is in scope. Queue: ignore as a stakeholder. Stars: never.
- **Format.** None.
- **Messages.** None.
- **Escalate.** If the queue is still stealing sittings after G3, cut the queue. Do not add an engagement cadence.

---

## 6. Risk assessment

**Blockers (real).**

- Sarah-as-PM / C7: more templates instead of WK-1. Highest probability. Already happening this session.
- Sarah-as-operator: "I already `/plan`," so echo stays wrong for strangers.
- Sarah-as-exec: ship 15 Oct with G3 red to protect the date.
- Casey hat: optional sync kept as step 3 so cloud "isn't forgotten."
- Cursor: chrome or VM policy change. Unblockable. Monitor only.

**Mitigation.**

- Tenets 1, 3, 5, 6. Review questions in `work-kit-tenets.md`. Weekly agenda item 1 is G3, not rates.
- WK-1 is the only assigned ticket. Scope freeze: Playground templates are not scope.
- No-go rule: slip 15 Oct rather than launch a skippable loop.
- Do not put cloud on the weekly board while G3 is red.

**Champions.**

- Operator hat, if she wants the next sitting to start on `/plan` without relying on memory.
- Eng hat, if she opens the file instead of the prompt list.

**How to use champions (not a campaign).**

- Put both hats in the same sitting: open `scripts/install-local.sh`, change item 3, `/review-diff`, commit. Do not recruit external advocates. Do not "activate" clone visitors. A champion who writes another deck has switched sides.

---

## 7. Communication calendar

All rows: attendee Sarah, unless noted.

| When | What | Who | Content |
| --- | --- | --- | --- |
| 16 Sep (done) | Inspection / "kickoff" | Sarah | User flow, OKRs, G3 fail recorded. Not a kickoff with a room. |
| Next sitting (overdue) | WK-1 copy | Eng + Copy + Operator | Patch echo and both README lists. This is the real kickoff of first delivery. |
| Until G3, each sit-down | 5-min gate | PM + Eng | Line 30 pass/fail. If fail: rest of the meeting is "when is WK-1." |
| 8 Oct | SLC | Exec + Eng | G3 green or 15 Oct slips. |
| Weekly from go-live week | 15-min review | PM + Operator | Denominator, plan-or-tiny, ships, secrets. [Agenda](../okrs/q4-2026-focus-metrics.md). |
| 15 Oct 09:00 | Go/no-go | Exec | G1-G4 or written slip. Runbook, not a readout to others. |
| 14 Nov | Cloud milestone | Eng + Casey hat | Checker fails closed. Avery step 3 still `/plan`. |
| 31 Oct, 30 Nov | Monthly forecast | PM | n=0 stays n=0. No fake trend. |
| 31 Dec | Grade | Exec | 80% and 8 ships, or honest miss. |

**Weekly updates: who receives.** Nobody else. Do not create a distribution list.

**Final review: who approves.** Sarah. A merged planning PR is not approval.

---

## How to use

If this file grows a column for a VP, delete the column. The map's job is to show that engagement theater is the risk, and that the only stakeholder who can unblock 15 Oct is the one who can type in `install-local.sh`.

Next sitting still does not need a stakeholder workshop. It needs item 3 to be `/plan`.
