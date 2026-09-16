# Communication plan: Work Kit first delivery

**Product / feature:** Work Kit first delivery (Plan to Ship as the default path)
**Phase 1:** 15 October 2026 (desktop Avery)
**Phase 2:** 14 November 2026 (Cloud Agents / Casey)
**Grade:** 31 December 2026
**Owner:** Sarah Scherer
**Related:** [Launch checklist](q4-2026-first-delivery-checklist.md), [Problem statement](../problem-statements/work-kit-first-delivery.md), [Q4 OKRs](../okrs/q4-2026-work-kit.md)
**Source prompt:** [Launch communication plan](https://aiuxplayground.com/prompts/launch-communication-plan) (AI UX Playground)

No `.agents/product-marketing.md`. Audience size is one primary operator. Owned channel is the GitHub README. No email list, no in-product banner we control, no press desk.

Launch-skill answers for this plan:

1. What. A medium workflow default, not a new product.
2. Audience. Avery. Optional teammate who clones `cursor-skills`.
3. Owned. README and this repo. Blog traffic and community: none.
4. Timeline. Phase 1 15 Oct. Phase 2 14 Nov.
5. Prior launch. Plugin already installed. First delivery was never announced as the success bar.
6. Product Hunt. No.

---

## 1. Launch overview

**What we are launching.** After install and reload, the next real change in a product repo goes through `/plan` (or a marked tiny skip), then review of the actual diff, then `/ship` of named files. Cloud Agents load the same five core skills from `~/.cursor/skills/`.

**Timeline.**

| Date | Event |
| --- | --- |
| 17 Sep 2026 (week -4) | Internal freeze of message. Session log template. |
| 1 Oct 2026 (week -2) | README and `install-local.sh` next-steps draft. |
| 8 Oct 2026 (week -1) | SLC gate. Copy review. Log exists. |
| 15 Oct 2026 | Phase 1 go-live. |
| 14 Nov 2026 | Phase 2 cloud path. |
| 22 Oct 2026 (week +1) | First metrics review. |
| 31 Oct 2026 | Monthly OKR forecast. |
| 31 Dec 2026 | Grade. Disappointment question. |

**Stakeholders.** Sarah (owner, author, support, "sales"). Future clone of the repo. Cursor (dependency, not a stakeholder we brief). No Sales, Marketing, or Press teams.

**Communication goals.**

1. Avery knows success is an accepted plan and a named-file commit, not a plugin card.
2. Anyone who clones the repo sees the same three next steps in README and script echo.
3. Casey-path readers know local plugins do not exist on Cloud Agent VMs.
4. Do not imply a public product launch.

**Success metrics for communications.** Not open rates. Use:

- README next-steps include `/plan` by 15 Oct.
- Script echo matches README word for word on those steps.
- Session log has a row on go-live day.
- Zero public posts claiming GA.
- Optional teammate, if any, can follow README without a side conversation. Count "questions that README already answers." Target: 0 after week +1.

---

## 2. Audience segmentation

| Audience | Exists here? | What they need to know | Action we want | Channel |
| --- | --- | --- | --- | --- |
| Engineering (Sarah) | Yes | Loop order, tiny skip, named-file ship, rollback | Keep the session log. Run `/plan` before edits. | This repo, Cursor chat |
| Support (Sarah) | Yes | Empty Customize, cloud miss, empty `/ship` | Answer from FAQ. Do not invent Cursor policy fixes. | `install-work-kit`, README |
| Leadership (Sarah) | Yes | O1 to O2 KRs. First delivery vs catalog growth | Grade 0.7 as success. Do not add playground skills to "make launch bigger." | OKR doc, weekly 15 min |
| Sales | No | Skip | Skip | Skip |
| Marketing | No | Skip | Skip | Skip |
| Existing customers | Avery only | New success bar after reload | Log the session. `/plan` then `/ship`. | README, script echo |
| Prospects | Clone visitors | How to install once at user scope | E1 or E2. Do not copy into each app repo. | GitHub README |
| Press / media | No | Skip | Skip | Skip |
| Partners | No | Skip | Skip | Skip |
| Casey (Cloud) | Phase 2 | Sync script plus Settings toggle | Run checker. Fail closed before cloud work. | README Cloud Agents |
| Riley (Teams) | Recovery only | Local imports may be blocked | Ask admin, or use `~/.cursor/skills` fallback | README FAQ |

Channel preference is GitHub markdown and the install script. Not email, not LinkedIn, not an in-app modal.

---

## 3. Messaging framework

**Core message (one line).** Work Kit is installed when the next change is planned, verified, and shipped as named files, not when the plugin card appears.

**What is new and why it matters.** The install path already copied files. Q4 names first delivery as the default path and counts it. A plugin you never `/plan` with is a folder on disk.

**Key benefits (not features).**

- You get a plan you can accept or reject before code moves.
- You get a review of `git diff`, not of intent.
- You get a commit that did not scoop `.env` or leftover notes.
- Cloud runs can load the same loop if you sync skills.

**By audience.**

| Audience | Message | Do not say |
| --- | --- | --- |
| Avery / customers | After reload, open a product repo and `/plan`. Tiny work: write tiny skip in the log, then implement. | "You're all set" after the script only. |
| Sales | Skip. If a teammate asks "why use this," use the one-liner above. | Pipeline, ACV, battle cards. |
| Support | Empty Customize: User scope, reload, Teams policy, then skills fallback. Cloud miss: sync was skipped. | "Try reinstalling Cursor." |
| Press | Skip. Not newsworthy. A personal plugin changed its success bar. | Embargo, embargoed screenshots. |
| Leadership | Business impact is share of sessions that plan then ship, and cloud runs that load core skills. | ARR, NPS, TAM. |

---

## 4. Communication timeline

### Pre-launch

**Week -4 (17 Sep 2026). Internal announcement and training.**

- [ ] Freeze the one-liner. Owner: Sarah.
- [ ] Create `docs/okrs/session-log.md` with header row. Owner: Sarah.
- [ ] Do not announce on social.

**Week -3 (24 Sep 2026). "Sales" enablement.**

- [ ] One-pager is section 3 of this file. No deck required.
- [ ] If a teammate exists, paste Template A. Otherwise skip.

**Week -2 (1 Oct 2026). Support readiness.**

- [ ] Draft FAQ (section 6). Owner: Sarah.
- [ ] Draft rollback paragraph. Owner: Sarah.

**Week -1 (8 Oct 2026). Asset review.**

- [ ] README next-steps and `install-local.sh` echo are identical.
- [ ] SLC gate in the launch checklist.
- [ ] No homepage banner. No blog. No social calendar.

### Launch day (15 Oct 2026)

Hour-by-hour, owner local time. One person. No war room.

| Time | Who | What |
| --- | --- | --- |
| 09:00 | Sarah | SLC gate. Session log exists. |
| 09:30 | Sarah | Merge README and script echo if not already on `main`. Run `install-local.sh`. Reload Cursor. |
| 10:00 | Sarah | Confirm Customize, User, Work Kit. |
| 10:15 | Sarah | Open a product repo. `/plan` or tiny skip. Implement first slice. `/review-diff`. `/ship` named files. Log the row. |
| 11:00 | Sarah | Time E1 if not already timed. Write minutes next to O1 KR1. |
| 12:00 | Sarah | Skim git for accidental `.env`. |
| 15:00 | Sarah | Optional: GitHub release notes using Template B. |
| 16:00 | Sarah | Write one recovery if Customize failed. Stop. No evening social posts. |

**Monitoring.** Session log. `git status` on the product repo. Cursor Customize. Not Datadog, not TweetDeck.

### Phase 2 day (14 Nov 2026)

| Time | Who | What |
| --- | --- | --- |
| 09:00 | Sarah | Sync checker green. |
| 10:00 | Sarah | Casey checklist on a second environment. |
| 11:00 | Sarah | Start or note a Cloud Agent run that should load `plan-the-work`. |

### Post-launch

**Week +1 (22 Oct).** Metrics: sessions, plan rate, ships. Owner: Sarah.

**Week +2 (29 Oct).** "Customer success" is one logged Plan to Ship. Quote it in the monthly OKR note. No case study site.

**Week +4 (12 Nov).** Mini retro before phase 2. If plan rate is 0, do not announce cloud. Fix the log habit.

**31 Oct, 30 Nov, 7 Jan 2027.** Monthly / quarterly as in OKRs.

---

## 5. Channels and content

### Email

| Piece | Status | Timing | Template |
| --- | --- | --- | --- |
| Customer announcement | Skip unless a teammate exists | 15 Oct | Template A |
| Internal all-hands | Skip. Weekly 15 min is the stand-in. | Weekly | Section 1 goals |
| Sales team | Skip | Skip | Skip |
| Partner | Skip | Skip | Skip |

**Template A. Teammate note (paste, do not mail-merge).**

Subject: Work Kit first delivery (15 Oct)

Body:

Work Kit is not done when Customize shows the card. After reload, open a product repo and run `/plan`. If the change is already tiny, write tiny skip in the session log and implement. Review the real `git diff`. `/ship` only named files. Never `git add .` on a dirty tree.

Cloud Agents cannot see `~/.cursor/plugins/local`. Run `./scripts/sync-user-skills.sh` and turn on Sync Skills for Cloud Agents before a cloud run.

FAQ: README Cloud Agents and Empty Customize.

**Template B. GitHub release notes (optional, 15 Oct 15:00).**

Title: Work Kit 1.x first delivery default

Notes:

- Success means Plan to Ship in a product repo.
- Install script next steps now include `/plan`.
- Cloud: sync skills. Local plugins do not reach cloud VMs.

### In-product

| Piece | Status | Why |
| --- | --- | --- |
| Banner | Skip | We do not own Cursor chrome. |
| Modal | Skip | Same. |
| Tooltip or badge | Skip | Same. |
| Targeting | n/a | Agent-decides skills fire on matching work. |

The "in-product" message is the `/plan` skill itself: do not edit until the plan is accepted.

### Website

| Piece | Status | Timing | Notes |
| --- | --- | --- | --- |
| Blog post | Skip | Skip | README is the post. |
| Product page | README update | 8 to 15 Oct | Next-steps list. |
| Homepage banner | Skip | Skip | No marketing site. |

**Template C. README next-steps (must match script echo).**

```text
Next:
  1. Command Palette → Developer: Reload Window
  2. Customize → filter User → confirm Work Kit
  3. Open a product repo and run /plan (or /debug if something is already broken)
```

### Social media

| Piece | Status |
| --- | --- |
| LinkedIn | Skip |
| Twitter thread | Skip |
| Schedule | None |

Rented channels stay unused until the session log shows an 80% plan rate. Then revisit. Not this launch.

### Support channels

| Piece | Owner | Due | Location |
| --- | --- | --- | --- |
| Help article | Sarah | 13 Oct | README FAQ plus `skills/install-work-kit/SKILL.md` |
| FAQ update | Sarah | 13 Oct | Section 6 |
| Talking points | Sarah | 13 Oct | Support row in section 3 |

### Sales

| Piece | Status |
| --- | --- |
| Sales deck | Skip. One-liner in section 3 is the deck. |
| Demo video | Skip phase 1. Optional: record the 15 Oct `/plan` to `/ship` for phase 2. |
| One-pager | This file, sections 1 and 3. |
| Pitch talking points | Core message. Benefit list. Not features. |

---

## 6. Internal enablement

**All-hands deck.** Five slides max if you ever present. Otherwise skip PowerPoint.

1. One-liner.
2. Before: plugin card. After: logged Plan to Ship.
3. Commands: `/plan` `/debug` `/review-diff` `/ship`.
4. Cloud miss.
5. What 0.7 looks like on O1.

**FAQ for internal (also external README).**

1. Customize is empty. Did I fail install? Check User scope, reload, Teams Allow Local Plugin Imports. Fallback: `~/.cursor/skills`.
2. Why did `/plan` skip a long plan? Tiny obvious change. Log tiny skip.
3. Why did `/ship` refuse `git add .`? Unrelated files in the tree. Stage named paths.
4. Cloud Agent has no Work Kit. Local plugins do not mount. Sync and the Settings toggle.
5. Can I add more playground skills as the launch? No.

**Demo walkthrough.** Live 15 Oct session. Optional screen recording stored outside the repo if it shows a private product repo. Do not commit customer code.

**Training schedule.** None. One person. Re-read `plan-the-work` and `ship-the-change` on 14 Oct.

**Q&A plan.** If a teammate appears, 20 minutes on 16 Oct. Agenda: one-liner, three next steps, two failure modes (empty Customize, cloud miss).

---

## 7. Press and media plan

| Item | Status |
| --- | --- |
| Press release | Skip |
| Media list | Skip |
| Spokesperson | None |
| Interview points | None |
| Embargo | None |

Not newsworthy. Do not pitch.

---

## 8. Feedback collection

| Source | How | Owner | Cadence |
| --- | --- | --- | --- |
| Session log | Rows: plan/tiny/debug/neither, ship, notes | Sarah | Each session |
| Git | `/ship` stats, secret audit | Sarah | Weekly and monthly |
| Cloud transcripts | Did `plan-the-work` load | Sarah | Each cloud run after 14 Nov |
| Social | Skip | n/a | n/a |
| Support inbox | None. Issues on this GitHub repo | Sarah | As filed |
| Sales | Skip | n/a | n/a |

**Response protocol.** Kit bug: issue on `cursor-skills`, then patch, then `install-local.sh` same day. Cursor platform bug: do not promise a kit fix. Write the limitation in README.

**Who owns what.** Sarah owns all channels that exist. Unowned channels stay skipped.

---

## 9. Escalation plan

**If Customize stays empty after a "successful" script.** Stop announcing. Log recovery. Check scope, reload, Teams policy. Do not tweet a workaround.

**If `/ship` would commit `.env`.** Do not push. Unstage. Note in log. Treat as a Sev1 for O3.

**If Cloud Agent lacks skills on 14 Nov.** Fail the sync checker. Do not start the six counted runs. Fix sync first.

**Who to contact.** Sarah. Cursor support only for product-path bugs.

**Issue protocol.** One GitHub issue. Title names the failure (empty Customize, secrets in diff, cloud miss). No status page.

**Rollback communication.**

Template D:

First-delivery copy on README caused confusion. Reverted script echo to reload plus Customize only. Loop remains in the skills. Do not follow step 3 until the next tag. Session log still required.

Reinstall from the last good commit with `./scripts/install-local.sh`.

---

## 10. Success metrics

Replace the SaaS scoreboard with what this launch can count.

| Typical SaaS metric | This launch |
| --- | --- |
| Email open / click | Skip. If Template A is sent to one teammate, a reply that they ran `/plan` is the click. |
| Social engagement | Target 0 posts. |
| Press mentions | Target 0. |
| Support ticket volume | GitHub issues on install/copy. Track count. Rising after README change means copy failed. |
| Sales pipeline | Skip. |
| Customer adoption | O1 KR2: 80% of logged sessions plan or tiny skip. O1 KR3: 8 named-file ships. O2 KR2: 6 cloud runs after 14 Nov. |

Comms-specific pass/fail by 15 Oct:

- [ ] Template C is in README and in script echo
- [ ] Session log has the go-live row
- [ ] No PH, social, or press artifacts
- [ ] FAQ answers empty Customize and cloud miss

---

## Cut list

Do not produce: waitlist landing page, customer email series, LinkedIn, Twitter thread, homepage banner, press release, sales deck, embargo, Product Hunt, comparison pages, Navattic demo.

Those wait until first delivery shows up in the log. Owned README first. Rented and borrowed later, if ever.
