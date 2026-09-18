# Launch-day runbook: Work Kit first delivery (phase 1)

**What's launching:** Work Kit first delivery. After install, the next product-repo change goes through `/plan` (or tiny skip), `/review-diff`, `/ship` of named files.
**Launch date/time:** Wednesday 15 October 2026, 09:00 to 16:00 owner local time. Write the IANA timezone in the header on T-24. Default assumption if unset: the machine's local zone.
**Time zones:** One operator. No multi-region staff. Phase 2 (14 Nov) is a separate runbook day, not this file.
**Launch type:** Soft, phased internal. Not big bang. Not a percentage rollout. Affected users: Avery (100% of this kit's current users, which is one person).
**Risk level:** Low blast radius (no public traffic). Medium if `/ship` would commit secrets. Treat secrets as P0 even on a personal repo.
**Rollback plan:** Yes. Re-run `./scripts/install-local.sh` from a known good git commit. See section 7.
**Related:** [Checklist](q4-2026-first-delivery-checklist.md), [Comms](q4-2026-first-delivery-comms.md), [GTM](q4-2026-first-delivery-gtm.md), [Messaging](../messaging/work-kit.md)
**Source prompt:** [Launch day runbook](https://aiuxplayground.com/prompts/launch-day-runbook) (AI UX Playground)

This runbook is for **15 Oct phase 1 only**. Do not enable cloud counting until 14 Nov.

---

## 1. Launch overview

### Launch summary

- **What.** README and `install-local.sh` next-steps include `/plan`. Avery completes one logged Plan to Ship in a product repo.
- **When.** 15 Oct 2026, 09:00 owner local. Day ends 16:00.
- **Who's affected.** Avery, 100% of current operators. Clone visitors who pull README after merge. No percentage flag. No staged cohort.
- **Success metrics.** Customize shows Work Kit. Session log has a go-live row. `/ship` staged named files only. Script echo matches README. No public GA post.
- **War room.** None. No Slack channel. No Zoom. Coordination surface is this file plus a terminal and Cursor. If a teammate joins, use a 1:1 Cursor chat, not a standup theater.

### Go/no-go criteria

| # | Criterion | Owner | Status at T-24 |
| --- | --- | --- | --- |
| G1 | SLC gate in the launch checklist is all checked | Sarah | Open |
| G2 | `docs/okrs/session-log.md` exists with a header row | Sarah | Open |
| G3 | README next-steps and `install-local.sh` echo are identical, and step 3 is `/plan` (or `/debug` if broken) | Sarah | Open. Today the script still says optional cloud sync as step 3. That must change before go. |
| G4 | `git status` on `cursor-skills` has no secrets. `/review-diff` done on the launch diff | Sarah | Open |
| G5 | No Product Hunt, social, or press artifacts queued | Sarah | Open (must stay empty) |

**Final go/no-go.** 15 Oct 2026, 09:00 owner local. Decider: Sarah Scherer. Any G1 to G4 fail is no-go. Slip the day. Do not launch on a yellow G3.

If no-go: do not merge copy. Do not post release notes. Keep using current skills. Write why in the session log.

---

## 2. Team and roles

One human fills every seat. Contact is the owner's usual phone and Cursor. No on-call rotation.

| Role | Name | Responsibilities | Contact |
| --- | --- | --- | --- |
| Launch lead | Sarah Scherer | Go/no-go, timeline, stop-the-line | Owner phone / Cursor |
| Engineering | Sarah Scherer | Merge, `install-local.sh`, git audit, rollback | Same |
| QA | Sarah Scherer | Customize check, `/plan` to `/ship` smoke, log row | Same |
| Product | Sarah Scherer | Message freeze, no-go if SLC fails | Same |
| Support | Sarah Scherer | Empty Customize, FAQ, GitHub issue if kit bug | Same |
| Marketing | Sarah Scherer | Optional GitHub release notes only. No social. | Same |

**Escalation path.**

1. First: Sarah (the operator on the machine).
2. Second: GitHub issue on `Ses2905/cursor-skills` if the kit is wrong. Title the failure.
3. Emergency: Cursor support, only if Customize or skill sync is a platform bug. Do not page an executive. There is no exec staff.

---

## 3. Pre-launch checklist (T-24 hours)

T-24 is 14 Oct 2026, 09:00 owner local.

### Engineering

- [ ] Launch diff is on a branch or ready to merge. No unrelated catalog skills in the diff.
- [ ] `/review-diff` verdict is ship or needs verification. Fix blockers before T-0.
- [ ] `install-local.sh` still excludes `.git`, `agent-tools`, `.DS_Store`. Confirm it will not copy `.env` from the checkout.
- [ ] Rollback commit SHA recorded here: `________________` (fill on T-24). Must be a commit where install works even if first-delivery copy is absent.
- [ ] No database migrations. N/A.
- [ ] No feature flags. N/A. Launch is copy plus behavior of existing skills.
- [ ] Monitoring is the session log, `git status`, Customize. No new Datadog.

### Product

- [ ] Feature flags: N/A.
- [ ] Launch announcement drafted: README plus Template B (optional).
- [ ] FAQ ready: empty Customize, tiny skip, named-file ship, cloud miss (cloud miss is docs only on 15 Oct, not a go-live path).
- [ ] Session log header exists.

### Marketing

- [ ] Communications scheduled: none except optional GitHub release at 15:00.
- [ ] Social posts: none. Confirm empty.
- [ ] Email campaigns: none. Template A only if a teammate exists.
- [ ] Press release: none.

### Support

- [ ] Re-read `install-work-kit`, `plan-the-work`, `ship-the-change`.
- [ ] Known issues: Teams may block local plugins. Cloud VMs lack local plugins. Script step 3 still optional until G3 lands.
- [ ] Escalation: this runbook section 2.
- [ ] Extra coverage: not applicable. Day ends 16:00. No overnight on-call.

---

## 4. Launch day timeline (15 Oct 2026, owner local)

### T-2 hours (07:00)

Skip a 07:00 all-hands. One person. Optional: skim this runbook over coffee. Owner: Sarah.

### T-1 hour (08:00)

- [ ] Pre-launch smoke on **current** (pre-merge) install: Customize still shows Work Kit.
- [ ] Confirm rollback SHA is filled.
- [ ] Confirm G5: nothing queued on social.
- Owner: Sarah.

### T-0 minus 60 min (09:00) final go/no-go

- [ ] Score G1 to G5.
- [ ] Go or no-go. Write the word in the session log.
- [ ] If go, continue. If no-go, stop the day.
- Owner: Sarah (launch lead and product).

### T-0 (09:30) "deploy"

There is no production cluster. Deploy means merge plus local install.

- [ ] Merge first-delivery README and `install-local.sh` echo to `main` (or install from the launch commit).
- [ ] `./scripts/install-local.sh`
- [ ] Confirm terminal printed three next steps, including `/plan`.
- [ ] Command Palette: Developer: Reload Window.
- Owner: Sarah (engineering).

### T+30 min (10:00) smoke on "production" (this machine)

- [ ] Customize, filter User, Work Kit visible.
- [ ] Open a **product** repo, not only `cursor-skills`.
- [ ] `/plan` or tiny skip. Do not edit before accept unless tiny skip is logged.
- Owner: Sarah (QA).

### T+45 min (10:15) first delivery

- [ ] Implement first slice.
- [ ] `/review-diff`. Verdict written in the session log.
- [ ] `/ship` named files only. Confirm `git show --stat` has no `.env`.
- [ ] Session log row: date, repo, plan/tiny/debug, ship yes, notes.
- Owner: Sarah.

### T+90 min (11:00) install timing

- [ ] If E1 not timed yet, time clone-or-reinstall to Customize visible. Write minutes next to O1 KR1.
- Owner: Sarah.

### T+2.5 hours (12:00) metrics and secrets

- [ ] `git status` clean on the product repo except expected leftovers.
- [ ] Scan the new commit for secrets.
- [ ] Error rate: Customize visible yes/no. Plan accepted yes/no. Ship yes/no. Any no is a P1 at least.
- Owner: Sarah.

### T+5.5 hours (15:00) comms

- [ ] Optional GitHub release notes (comms Template B). Internal announcement is the session log row.
- [ ] Do not send social, email blast, or press.
- [ ] If a teammate exists, paste Template A now, not before smoke passed.
- Owner: Sarah (marketing / support).

### T+6.5 hours (16:00) EOD

- [ ] End of day summary in session log: go/no-go, Customize, plan, ship, minutes, issues.
- [ ] On-call handoff: none. Tomorrow's first task is weekly count, not a pager.
- [ ] If Customize failed, write recovery. Consider rollback (section 7) before tomorrow's work.
- Owner: Sarah.

Phase 2 times on 14 Nov are **not** this timeline. Do not start the six cloud runs today.

---

## 5. Monitoring checklist

No APM. Watch these by hand.

| Metric | Baseline | Alert (treat as P1/P0) | How |
| --- | --- | --- | --- |
| Customize shows Work Kit | Visible after last good install | Missing after reload | Customize, User filter |
| Script / README step 3 | Must mention `/plan` after T-0 | Drift between script and README | Diff the two texts |
| Session log row | 0 before go-live | Still 0 at 16:00 after a "go" | `docs/okrs/session-log.md` |
| `/ship` includes `.env` or credentials | 0 | Any 1 is P0 | `git show --stat` |
| Public GA post | 0 | Any 1 is process P1 | Search before EOD |
| Error rate / latency of a web app | N/A | N/A | No service |

**Dashboards.**

- Primary: session log markdown
- Engineering: `git log -1 --stat` on the product repo and on `cursor-skills`
- Business: Q4 OKR file (update KR forecasts at month end, not hourly)

**Alert channels.** None. No PagerDuty. No Slack webhook. The operator is at the keyboard until 16:00.

---

## 6. Issue response plan

**Severity.**

- **P0.** Secrets in a pushed commit. Security. Data you cannot take back.
- **P1.** Customize empty after install. `/ship` scooped unrelated files. Agent edited before plan accept on a non-tiny change. README and script disagree after merge.
- **P2.** Wording unclear. Teammate question README already answers. Timing over 10 minutes but install works.
- **P3.** Typo, extra catalog mention, cosmetic README layout.

**P0 / P1.**

1. Stop further comms (no release notes).
2. Investigate. Secrets: unstage is too late if pushed. Rotate the secret. Follow the host's leak process. Then rollback kit copy if the skill text caused the scoop.
3. Rollback decision within 15 minutes for P0/P1 that blocks first delivery.
4. Notify: session log plus GitHub issue. No status page.
5. After the day, write what happened in the weekly check-in.

**P2.** Log. Fix in the next README/script commit. Same-day if copy drift (G3).

**P3.** Backlog. Do not extend launch day.

---

## 7. Rollback plan

**Triggers.**

- [ ] Customize empty after reload and the usual recoveries (User scope, Teams policy) do not fix it
- [ ] P0 secrets from `/ship` guidance
- [ ] P1 copy drift that tells people the wrong next step and you cannot hotfix in 15 minutes
- [ ] Operator cannot complete Plan to Ship by 12:00 because the kit is in the way (not because the product repo is hard)

**Not a rollback trigger.** Slow E1 (over 10 minutes) if Customize works. Missing cloud checker (phase 2). Empty social calendar.

**Procedure.**

1. Note current HEAD of `cursor-skills` and the rollback SHA from T-24.
2. `git checkout <rollback-sha>` in the kit checkout (or clone that SHA).
3. `./scripts/install-local.sh` (script does `rm -rf` dest then copy. That is the rollback.)
4. Reload Window. Confirm Customize still shows Work Kit on the old copy.
5. If README on `main` already has bad copy, revert that commit and push. Do not leave GitHub advertising a loop the local plugin no longer matches.
6. Session log: "rolled back," SHA, reason.
7. Comms: Template D in the comms plan.

**Rollback owner:** Sarah (engineering).
**Decision maker:** Sarah (launch lead). Same person. Decision within 15 minutes of P0/P1.
**Expected time:** 5 to 15 minutes (checkout, install, reload). Secrets rotation is extra and can exceed that. Kit rollback still happens first so `/ship` stops scooping.

---

## 8. Communication templates

**Internal launch announcement (session log or teammate).**

Work Kit first delivery is live on this machine as of 15 Oct 2026. Success is an accepted `/plan` and a named-file `/ship`, not the plugin card. Details: `docs/messaging/work-kit.md`. Questions: README FAQ.

**External announcement (GitHub release, optional, after 10:15 smoke).**

Work Kit 1.x: first delivery is the default path. After reload, open a product repo and `/plan`. Cloud Agents still need `./scripts/sync-user-skills.sh`. Local plugins do not reach cloud VMs.

**Issue communication.**

Work Kit first-delivery copy has a problem: [empty Customize / script README drift / ship scooped files]. Investigating. No public status page. Next update in the session log by [time].

**Rollback communication.**

Rolled Work Kit local install back to [SHA] because [reason]. README on GitHub [was / was not] reverted. Do not follow new step 3 until the next tag. Session log still required. Reinstall: `./scripts/install-local.sh` from that SHA.

**No-go communication.**

No-go on 15 Oct. Failed [G1-G4]. Not merged. Using last good install. Next attempt: [date].

---

## Day-of one-pager

1. 09:00 go/no-go G1 to G5.
2. 09:30 install-local and reload.
3. 10:00 Customize.
4. 10:15 `/plan` to `/ship` in a product repo. Log the row.
5. 12:00 secrets scan.
6. 15:00 optional release notes.
7. 16:00 stop. Rollback if P0/P1 still open.
