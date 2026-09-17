# Agenda: WK-1 copy sitting (first-delivery kickoff)

**Meeting type.** Working session. Not a kickoff with a room, not a brainstorm, not a weekly status sync.
**Duration.** 30 minutes. Stop at 20 if the commit exists. Do not fill leftover time with another template.
**Attendees.** Sarah Scherer only. Hats: eng (types), copy (three lists match), operator (will `/plan` later), exec (no-go until this lands).
**Purpose.** Land install step 3 as `/plan` (or `/debug` if broken) on the script echo and both README numbered lists. Ticket [WK-1](../tickets/wk-1-g3-install-copy.md).
**Calendar title.** WK-1: install step 3 is /plan
**Related:** [Exec summary](q4-2026-exec-summary.md), [Focus metrics](../okrs/q4-2026-focus-metrics.md) (recurring 15-min after go-live), [US-1 AC](../user-flows/us-1-g3-acceptance-criteria.md), [Stakeholder map](q4-2026-stakeholder-map.md)
**Source prompt:** [Meeting agenda](https://aiuxplayground.com/prompts/meeting-agenda-generator) (AI UX Playground)

Paste the box below into the calendar invite. There is no video link to include.

```
WK-1: install step 3 is /plan
30 min | Sarah Scherer (required)
Goal: commit that makes install-local.sh echo + both README lists use /plan as item 3.
Success: git grep for "Optional for Cloud Agents" on the script echo is empty.
Not this meeting: cloud checker, survey, another Playground fill, 15 Oct date debate.
Prep: open scripts/install-local.sh lines 25-31. Bring US-1 AC.
```

If this block is used for a meeting that produces minutes and no diff, the sitting failed.

---

## 1. Meeting objective

**Primary goal.** Change stdout and both README numbered install lists so item 3 is `/plan` (or `/debug` if something is already broken). Cloud sync is not Avery's third beat.

**Desired outcomes.** One commit covering `scripts/install-local.sh` and both README files. `/review-diff` run. G3 can be re-checked with `sed -n '25,31p' scripts/install-local.sh`.

**Success.** Live product no longer prints `Optional for Cloud Agents` as step 3. The three lists match. Calendar does not end in "we aligned." Failure: time spent, line 30 unchanged.

---

## 2. Attendees and roles

Required: Sarah. Optional: nobody. Do not add Casey, Riley, clone visitors, or Cursor to the invite.

| Hat | Why here | Role |
| --- | --- | --- |
| Eng | Only person who can patch the echo | Presenter and doer |
| Copy | README lists must match the echo | Contributor (same commit) |
| Operator (Avery) | Will use item 3 on the next product-repo sitting | Informed by the new echo, not by slides |
| Exec | Holds 15 Oct no-go until G3 is green | Decision-maker: merge or keep no-go |
| Note-taker | The diff and `git log -1` | Not a minutes doc |

Informed-only, not invited: clone visitors (they read README after the commit). Casey (14 Nov). Riley (recovery, later).

---

## 3. Agenda items

| Min | Topic | Owner | Purpose | Expected outcome |
| --- | --- | --- | --- | --- |
| 0-2 | Gate | Eng | Inform | Read lines 25-31 aloud. Confirm still fail. If already pass, cancel and go log a product-repo row instead. |
| 2-18 | Patch | Eng + Copy | Decide by typing | Edit echo item 3. Edit clone README numbered list. Edit checkout README numbered list. Same wording. No dest rewrite. No catalog as items 3-4. |
| 18-25 | Review | Eng | Decide | `/review-diff`. Check secrets. Confirm `git grep` for `Optional for Cloud Agents` on the echo is empty. |
| 25-30 | Ship | Exec + Eng | Decide | Named-file commit. Push if that is the usual path. Do not open a new prompt. |

**Out of order / do not add.** Brainstorm alternate step-3 copy. Cloud checker design. 15 Oct comms. Interview plan. This agenda as a discussion of agendas.

If patch overruns, cut Ship into a second 15-min block the same day. Do not slip to "next week after one more doc."

---

## 4. Preparation required

**Review beforehand (5 min, before the block).**

- `scripts/install-local.sh` lines 25-31.
- [US-1 acceptance criteria](../user-flows/us-1-g3-acceptance-criteria.md).
- [WK-1](../tickets/wk-1-g3-install-copy.md) (one change, under 2 hours, no dest rewrite).
- [Exec summary](q4-2026-exec-summary.md) only if the no-go is in doubt. It is not.

**Bring.** Editor, repo checkout, terminal. Not a slide deck. Not Mixpanel. Not the QBR.

**Questions to think about (only these).**

1. Does item 3 contain `/plan` and `/debug` if broken?
2. Do script echo, clone README, and checkout README match?
3. Did I put cloud sync back as beat three?

Do not think about Marketplace, NPS, or who else should have been invited.

---

## 5. Meeting logistics

| Field | Value |
| --- | --- |
| Date / time | Next 30-min block on Sarah's calendar. Target: 17 Sep 2026, the first sitting after this file. Do not wait for 8 Oct to start. 8 Oct is the SLC, not the start. |
| Timezone | Sarah's local. Do not invent a Zoom timezone for a room of one. |
| Location | Local machine. Editor + terminal. No video link. |
| Note-taker | The commit message and the diff. Optional: one line in the session log after go-live, not during this patch. |
| Recurring? | No. This sitting is one-shot. After G3 is green, use the 15-min weekly in [focus metrics](../okrs/q4-2026-focus-metrics.md), not this agenda. |

---

## 6. Action items template

Fill at minute 30. If the commit exists, most rows are already done.

**Decisions made**

- [ ] Item 3 is `/plan` (or `/debug` if broken) on all three lists.
- [ ] 15 Oct remains no-go until the box above is checked. Slip conversation waits for 8 Oct SLC.
- [ ] Cloud stays off Avery's numbered list.

**Action items**

| Action | Owner | Deadline |
| --- | --- | --- |
| Patch echo + both README lists, `/review-diff`, commit | Sarah (eng + copy) | This sitting |
| Re-run `sed -n '25,31p' scripts/install-local.sh` | Sarah | End of sitting |
| Product-repo `/plan` + named-file `/ship` + log row | Sarah (operator) | Go-live day (15 Oct or slip), not this block unless time remains |
| Cloud checker | Sarah | 14 Nov. Not this invite. |

**Follow-up.** Only if G3 is still red: book another 30 min the same day. Do not follow up with a stakeholder readout.

**Next meeting.** None of this type. After G3: weekly 15 min (gate, denominator, star, ships, one decision). Until G3, sit-downs are 5 min: is line 30 still wrong, and when is WK-1.

---

## How to use

Send this as the invite description. Then open the script. A filled agenda with an empty diff is C7.

Next sitting is this sitting. Item 3 is `/plan`.
