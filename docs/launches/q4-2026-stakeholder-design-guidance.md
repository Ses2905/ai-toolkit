# Design guidance: translate stakeholder objections (17 Sep 2026)

**Paste received.** Empty. No Slack thread, no exec email, no design critique notes.
**Feedback used instead.** Five hat objections already written in the [stakeholder presentation](q4-2026-stakeholder-presentation.md). Plus the live product line that acts like a stakeholder: install step 3 is optional cloud sync. These are owner lines, not quotes from other people.
**Stakeholder.** Sarah Scherer, every hat. There is no separate design org.
**Design surface we own.** Numbered install copy: `scripts/install-local.sh` echo, clone README, checkout README. We do not own Cursor chrome, Customize, or a first-run modal.
**Related:** [Stakeholder map](q4-2026-stakeholder-map.md), [Tenets](../messaging/work-kit-tenets.md), [WK-1](../tickets/wk-1-g3-install-copy.md), [US-1 AC](../user-flows/us-1-g3-acceptance-criteria.md), [Feedback triage](../research/first-delivery-feedback-triage.md), [WK-1 agenda](q4-2026-wk1-agenda.md)
**Source prompt:** [Translate stakeholder feedback](https://aiuxplayground.com/prompts/translate-stakeholder-feedback) (AI UX Playground)

Do not treat the PR/FAQ Avery line as stakeholder input. Do not invent a VP comment. Next sitting is the copy patch, not a workshop to refine these questions.

**Raw lines (the "paste")**

1. Operator: "I already know to `/plan`."
2. PM: "We should research first."
3. Eng: "Copy is fine, the skill is the product."
4. Copy: "Catalog should be visible."
5. Exec: "Is this big enough to present?" (and the date-pride variant: ship 15 Oct anyway).
6. Shipped echo: `3. Optional for Cloud Agents: ./scripts/sync-user-skills.sh`

---

## 1. Feedback interpretation

### What they likely mean

| Line | Plain meaning | Underlying goal | Missing context |
| --- | --- | --- | --- |
| Already know `/plan` | Do not spend a sitting on copy I will not read | Keep personal speed | Clone visitors and future-Sarah on a cold machine do not have that memory |
| Research first | Do not patch without testers | Avoid shipping the wrong words | Copy never asked anyone to `/plan`. Interviews cannot explain a skippable step 3. Survey is gated on G3 |
| Copy is fine | Skills and dest path are the real work | Protect eng time | Three install surfaces omit `/plan` as beat three. Skills already exist |
| Catalog visible | Show what the kit contains at install | Reduce "what did I get?" | Checkout README already dumps lists. That is C3 (shopping), not first delivery |
| Big enough / hit the date | Do not make a fuss, or do not miss 15 Oct | Status, calendar pride | There is no board. A skippable loop is not a launch |
| Optional cloud as step 3 | Casey should not be forgotten | Cloud skills load | Local plugins do not mount on VMs. A footnote as Avery item 3 is the live bug |

Shared concern: look busy, look complete, do not "just change words." Shared miss: stdout is the product (tenet 1).

---

## 2. Actionable design guidance

**Change (copy, not chrome).**

- Script echo item 3: `/plan` (or `/debug` if something is already broken). Same sentence on clone README and checkout README numbered lists.
- Move `./scripts/sync-user-skills.sh` and the Settings toggle to the Cloud Agents section. Not beat three.
- Remove catalog / Remotion / slash inventory from numbered install items 3-4.
- If `install-work-kit` skill item 3 still dumps names, match it in the same sitting if that file ships in dest. Not a second epic.

**Canonical three beats (do not bikeshed past US-1).**

1. Command Palette, Reload Window.
2. Customize, filter User, confirm Work Kit.
3. In a product-repo chat: `/plan` (or `/debug` if something is already broken).

**Investigate later, not in this sitting.** Whether those words produce `/plan` without a researcher (survey after G3). E1 timing after copy. Casey checker after 14 Nov.

**Do not design.** First-run UI, Marketplace card, in-product banner, a modal over chat, a progress checklist in Cursor chrome.

**Clarifying questions (for Sarah, if she stalls).** See section 4. Default if unanswered: follow US-1 AC as written.

---

## 3. Prioritized recommendations

**High (address directly this sitting)**

- Patch the three numbered lists. Ticket WK-1. Agenda: 30 min copy sitting.
- Keep 15 Oct as no-go until that patch is in. Slip after 8 Oct SLC if still red.
- Push back on catalog-as-onboarding and cloud-as-step-3 in the same diff.

**Medium (after G3)**

- Log one product-repo row (plan or tiny, named-file ship).
- Time E1 twice.
- Then, leftover hours, talk to people about whether the new item 3 worked.

**Low**

- prettier README prose around the lists, once the numbers match.
- Riley recovery paragraph.
- Capture gallery. Parked.

**Accommodate vs push back (summary).** Accommodate the goal under each line (speed, truth, Casey-later, a real date). Push back on the tactic (skip copy, research first, catalog in the list, ship red, cloud as item 3).

---

## 4. Clarifying questions

Ask only if the patch is blocked by wording. Otherwise type.

1. Must item 3 name `/debug` as well as `/plan`? (US-1 says yes if something is already broken.)
2. Is one sentence enough, or do we link to the Cloud Agents heading for sync? (Link in the cloud section, not as beat three.)
3. Does checkout README lose its catalog dump entirely from the numbered list, or move it under a later "what is in the kit" heading? (Move. Do not number it as 3-4.)

**Additional context that would help, and that we will not wait for.** Interview n, Figma, Cursor product-team blessing, a second reviewer.

**How to validate.** After the commit: `sed -n '25,31p' scripts/install-local.sh` and a side-by-side of both README lists. After go-live: a logged row. Not a workshop vote.

---

## 5. Alternative interpretations

| Line | Alternate reading | How to tell | Push back or accommodate |
| --- | --- | --- | --- |
| Already know `/plan` | Real request to skip onboarding for power users | We have one operator and public README | Push back. Write for the stranger. Muscle memory is not clone UX |
| Already know `/plan` | Fear that `/plan` on a one-line change is ceremony | Check US-4 tiny skip | Accommodate tiny. Still teach `/plan` as default item 3 |
| Research first | Fear of wrong words | US-1 already picked the words | Push back until G3. Research after |
| Research first | C7 in PM clothing | If the next file is another template, this reading is correct | Push back. Open the script |
| Copy is fine | Dest/symlink work was hard and should not be relitigated | Dest copy already works | Accommodate: do not rewrite dest. Push back: echo is still wrong |
| Catalog visible | Help discovery of Remotion/slides | Those skills exist | Accommodate in a non-numbered "also in the kit" section after G3. Push back as install steps |
| Big enough | Shame about a one-person memo | There is no board | Push back. Do not present. Patch |
| Hit the date | Honest fear of slipping | 8 Oct SLC exists | Accommodate a written slip. Push back on launching red |
| Cloud as step 3 | Believe local plugins work on VMs | They do not | Push back with the architecture fact. Accommodate a 14 Nov checker |

If two readings fight, US-1 AC plus tenet 1 win. Do not split the difference by leaving sync as item 3 "and also `/plan`."

---

## 6. Implementation notes

**Design.** Copy-only. Three identical numbered lists. Sentence case. Straight quotes. No extra marketing sentence on the echo. Cursor chrome stays as Reload + Customize; we instruct, we do not restyle.

**Technical.** One change set: `install-local.sh` echo and both README files. No dest rewrite. No symlink. `/review-diff` before commit. `git grep` for `Optional for Cloud Agents` on the script echo must be empty. If the skill `install-work-kit` is in the tarball, match item 3 there too so dest does not re-teach a catalog.

**User impact.** Avery's muscle memory unchanged if she already `/plan`s. Clone visitors gain a third beat. Casey waits until 14 Nov and does not steal Avery's list. Riley unchanged this sitting.

**Risk if we "design" the feedback into a UI.** We cannot ship it. We will have spent the sitting. Line 30 stays.

---

## Next steps

1. Do not send these questions to a stakeholder thread. There is no thread.
2. Open `scripts/install-local.sh`. Change item 3. Match both README lists. [WK-1 agenda](q4-2026-wk1-agenda.md).
3. If wording stalls, use US-1 as written. Do not open another prompt.

The guidance is the patch. Item 3 is `/plan`.
