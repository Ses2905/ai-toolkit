# Meeting notes: Work Kit first-delivery planning chain

**Paste received.** Empty. There was no Zoom transcript. These notes reconstruct the 16-17 Sep 2026 working session from the docs tree and live product inspection.
**What this was.** Sequential Playground templates filled against Work Kit. Not a stand-up. Not a workshop with a facilitated agenda.
**When.** 16 Sep 2026 (first chain, ~22:07-22:48 UTC) plus 17 Sep 2026 continuation (focus metrics through this notes file).
**Where.** Remote. Cursor Cloud Agent on `cursor-skills`. No recording. No whiteboard.
**Share with.** Sarah Scherer only. There is no team list.
**Related:** [16 Sep session summary](2026-09-16-first-delivery-planning.md), [WK-1](../tickets/wk-1-g3-install-copy.md), [WK-1 agenda](../launches/q4-2026-wk1-agenda.md), [Exec summary](../launches/q4-2026-exec-summary.md), [Focus metrics](../okrs/q4-2026-focus-metrics.md)
**Source prompt:** [Clean up meeting notes](https://aiuxplayground.com/prompts/clean-up-meeting-notes) (AI UX Playground)

**Headline.** Planning agrees. Stdout does not. Next sitting is the copy patch, not another notes file.

---

## 1. Clean notes

### Live product (inspected, still true)

- `scripts/install-local.sh` line 30: `Optional for Cloud Agents: ./scripts/sync-user-skills.sh`
- Clone README item 3: Cloud Agents toggle. Checkout README items 3-4: catalog dumps.
- Session log: 0 filled rows. Interviews 0. Survey 0.
- Plugin version live: 1.20.0. First delivery **not released**. Do not publish draft 1.20.1 notes.

### What the chain produced

Docs for flow, OKRs, SMART, scope, stories, AC, roadmap, GTM, metrics, affinity, SWOT, ICP, LOI (paid pilots refused), retention, focus metrics, shareout, tenets, stakeholder map, QBR (kickoff, not a grade), exec summary, WK-1 ticket + 30-min agenda, feedback triage (inbox 0), design guidance, embargoed release notes, idea synthesis. **None of those files changed line 30.**

### Working agreements (do not re-litigate in the copy sitting)

- Job: Plan to Ship after one user-scope install. Customize-visible is not success.
- Primary user: Avery (Sarah on desktop). Casey 14 Nov. Riley recovery only.
- Gate: G3 copy match by 8 Oct, or slip 15 Oct. No-go if step 3 is still sync.
- North star: plan-or-tiny rate 80%. Input: 8 named-file ships. G3 is the gate, not the star.
- O4 capture parked. SaaS tiles (ARR, NPS, DAU) off the board.
- $0 MIT. No Marketplace. No paid partners. No first-run UI.

### Process miss named in the room (the owner vs herself)

More Playground templates felt like progress (C7). That is the highest-probability blocker for 15 Oct.

---

## 2. Summary

**Topics.** First delivery definition; install copy vs stated job; empty instruments; Q4 dates; what not to measure; who the stakeholder is (Sarah hats); whether to announce (no).

**Decisions.** See section 4. They are owner working decisions, not a signed board minute.

**Context.** Kit already exists. Loop commands already exist. The miss is routing: numbered install teaches skip. Adjacent chat and lists win minute one if copy is vague.

---

## 3. Action items

| Action | Owner | Due | Priority | Depends on |
| --- | --- | --- | --- | --- |
| Patch `install-local.sh` echo + both README numbered lists. Item 3 = `/plan` (or `/debug` if broken). `/review-diff`. Commit. Reinstall if `install-work-kit` copy ships in dest. | Sarah | **This sitting** (overdue since 16 Sep). SLC 8 Oct. | P0 | None. US-1 is the wording bar. |
| Re-check `sed -n '25,31p' scripts/install-local.sh`. `git grep` for `Optional for Cloud Agents` on the echo must be empty. | Sarah | End of that sitting | P0 | Patch |
| One product-repo `/plan` (or tiny) + named-file `/ship` + log row | Sarah | Go-live 15 Oct or written slip | P0 after G3 | G3 green |
| E1 or E2 timed twice, <= 10 min | Sarah | 15 Oct or slip | P1 after G3 | Copy in |
| Bump `plugin.json` to 1.20.1 and fill embargoed notes date | Sarah | Same commit as copy, or immediately after | P1 | G3 actually in git |
| Cloud checker + Casey README + six runs | Sarah | 14 Nov, then through 31 Dec | P2 | G3 green. Not Avery step 3 |
| Field survey / leftover interviews | Sarah | After G3 only | P3 | Copy match |
| Do not commit `.agents/skills/` or `skills-lock.json` unless owner asks | Sarah | Standing | P2 | - |

If the P0 row is still open, ignore P2-P3.

---

## 4. Decisions made

| Decision | Who | Rationale |
| --- | --- | --- |
| Avery is the 15 Oct spine | Sarah | One operator. Riley policy not owned. Casey VM cannot mount local plugins |
| 15 Oct is no-go until G3 | Sarah | Launching a skippable loop is not first delivery |
| Slip rather than ship red | Sarah | Date pride vs tenet 1 (echo is the product) |
| Cloud is not Avery item 3 | Sarah | That footnote is the live bug. Phase 2 is 14 Nov |
| North star = plan-or-tiny, not Customize-visible | Sarah | Problem is loop never runs |
| Paid pilots / MSA / B2B ICP / raise | Sarah, refused | $0 MIT. Not a company |
| O4 capture parked | Sarah | Counting captures now rewards C7 |
| Do not publish 1.20.1 notes or social | Sarah | Version still 1.20.0. Log n=0 |
| Next sitting is WK-1, not another template | Sarah (stated every file; not yet done) | Stdout is the product |

A filled notes file is not a signature. Scope still says: signing a doc does not replace editing `install-local.sh`.

---

## 5. Open questions

**Do not block the patch on these.**

- Exact item-3 sentence: default to US-1. `/plan` and `/debug` if broken. Do not bikeshed.
- Whether 15 Oct slips: decide at 8 Oct SLC, not in this notes file.
- E1 minutes: untimed. Measure after copy.
- Will a logged sitting after new copy actually start with `/plan`? Unknown. Survey after G3. Do not interview first.
- Dirty-tree fixtures, plan-gate hardening, Riley paragraph: later, if the log still shows skip after G3.

**Pending that is the sitting itself.** Is line 30 still wrong when Sarah next opens the editor? Yes, as of this file.

---

## 6. Next steps

1. **Now.** Sarah: 30-min WK-1 copy sitting. Calendar title: `WK-1: install step 3 is /plan`. [Agenda](../launches/q4-2026-wk1-agenda.md).
2. **8 Oct.** Sarah: SLC. Green or write a slip date for 15 Oct.
3. **Go-live or slip day.** Sarah: log row. Then weekly 15-min scoreboard.
4. **14 Nov.** Cloud checker. Avery step 3 remains `/plan`.
5. **31 Dec.** Grade 80% and 8 ships. Rewrite the kickoff QBR only if G3 is green and the log has rows.

There is no follow-up meeting of the planning-chain type. Recurring after G3: weekly 15 min. Until G3: 5 min, is line 30 still wrong.

---

## 7. Attendees

| Who | Present | Role |
| --- | --- | --- |
| Sarah Scherer | Yes (prompts) | Owner, Avery, eng, copy, PM, exec. Only decision-maker. |
| Cursor Cloud Agent | Yes | Filled templates, committed docs. Did not patch `install-local.sh` (not asked). |
| Clone visitors, Casey, Riley, Cursor the host app | No | Informed via README later, or not this quarter |
| Testers / interview recruits | No | n=0 |

Key contributor to the miss: the chain itself (C7). Key contributor who can clear it: Sarah in `install-local.sh`.

---

## How to use

If these notes are forwarded as "we aligned," they failed. Forward the script. Item 3 is `/plan`.
