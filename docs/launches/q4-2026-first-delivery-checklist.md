# Launch checklist: Work Kit first delivery

**What ships:** First delivery as the default path. Install, then Plan to Ship in a product repo. Cloud Agents load the same five core skills.
**Product type:** Cursor user-scope plugin (developer tool), not a consumer web or mobile app
**Target audience:** Avery (solo IC, desktop Cursor). Casey (Cloud Agents) in phase 2. Riley (Teams) is recovery copy only.
**Launch scope:** Phased internal. Not a public GA, waitlist, or Product Hunt day.
**Internal go-live:** 15 October 2026
**Cloud path go-live:** 14 November 2026
**Grade date:** 31 December 2026
**Owner:** Sarah Scherer
**Related:** [Problem statement](../problem-statements/work-kit-first-delivery.md), [Q4 OKRs](../okrs/q4-2026-work-kit.md), [User flow](../user-flows/work-kit-first-delivery.md)
**Source prompt:** [Product launch checklist](https://aiuxplayground.com/prompts/product-launch-checklist) (AI UX Playground)

No `.agents/product-marketing.md` exists. Context is the README job plus those three docs.

This is a medium update in the launch-skill matrix (workflow default, not a new product). Marketing fanfare would fake a SaaS launch. Owned channel is the GitHub README. Skip rented and borrowed channels this quarter.

---

## SLC gate (run before any phase)

Simple, Lovable, Complete (Jason Cohen). One job, whole experience, something Avery would choose.

- [ ] **Simple.** The launch does one thing: first delivery. Not a new dashboard, marketplace listing, or catalog dump.
- [ ] **Lovable.** Avery would be very disappointed to lose `/plan` wait-for-accept and `/ship` of named files. If the answer is "somewhat," do not announce. Fix the loop.
- [ ] **Complete.** Happy path E1 or E2, reload, Customize shows Work Kit, `/plan` then `/ship` in a product repo. Empty, error, and tiny-skip states exist in the user flow. Cloud sync is phase 2, not a stub inside phase 1.
- [ ] **Not stealth.** User flow, OKRs, and problem statement already exist. Stop polishing docs if the session log is still missing.
- [ ] **Not one more feature.** Playground skill installs are out of this launch.

If any box is unchecked on 8 October 2026, cut scope. Do not move the date to add catalog skills.

---

## Launch context (filled)

| Field | Value |
| --- | --- |
| Launch date | Phase 1: 15 Oct 2026. Phase 2: 14 Nov 2026. Grade: 31 Dec 2026. |
| Product type | Cursor plugin, user scope |
| Target audience | Avery first. Casey second. |
| Launch scope | Phased internal |

**Phase 1, Internal (by 15 Oct).** Session log exists. One timed E1 install. README tells the next step after reload: open a product repo and `/plan`. Avery uses the loop on real work.

**Phase 2, Alpha for cloud (by 14 Nov).** Sync checker. Casey path checklist. Six cloud runs start after this date.

**Phase 3, Close Q4 (31 Dec).** Grade O1 to O4. No public "full launch."

---

## 1. Pre-launch design

Work Kit has no product screens of its own. Design here means Cursor chrome copy, README structure, and the first-delivery flow. Owner is Sarah unless noted.

| Done | Item | Work Kit meaning | Owner | Due |
| --- | --- | --- | --- | --- |
| [ ] | Design review complete | Read [user flow](../user-flows/work-kit-first-delivery.md) against README install steps. D2 (plugin visible) and D4 (plan vs tiny skip) must match the words users see. | Sarah | 8 Oct 2026 |
| [ ] | Design QA passed | Walk E1 on a machine that already has Cursor. Confirm Customize filter User, not Project. | Sarah | 10 Oct 2026 |
| [ ] | Accessibility audit complete | README and install script output: sentence case, no color-only status. Terminal next-steps are numbered lists, not color badges. Skip WCAG on a Cursor UI we do not own. | Sarah | 10 Oct 2026 |
| [ ] | Responsive design verified | Skip. No Work Kit viewport. README readable on GitHub mobile. | Sarah | 10 Oct 2026 |
| [ ] | Design system compliance | Plugin `displayName` stays Work Kit. Slash names stay `/plan`, `/debug`, `/review-diff`, `/ship`. Do not rename for launch. | Sarah | 8 Oct 2026 |
| [ ] | Asset exports ready | `assets/logo.svg` present. No App Store screenshots. No Product Hunt gallery. | Sarah | 8 Oct 2026 |
| [ ] | Design documentation complete | User flow plus this checklist. ASCII or mermaid in the flow doc is enough. | Sarah | 8 Oct 2026 |

---

## 2. Pre-launch development

| Done | Item | Work Kit meaning | Owner | Due |
| --- | --- | --- | --- | --- |
| [ ] | Code review complete | Review diffs to `scripts/install-local.sh`, `scripts/sync-user-skills.sh`, `skills/install-work-kit/SKILL.md`, README Cloud Agents section. Use `/review-diff` on this branch. | Sarah | 13 Oct 2026 |
| [ ] | Unit tests passing | Add a post-sync folder check that fails if any of the five core skill dirs are missing. | Sarah | 13 Oct 2026 |
| [ ] | Integration tests passing | Dirty-tree fixtures for `/ship` (10 cases). Can slip to 15 Dec without blocking phase 1. Blocks O3 grade. | Sarah | 15 Dec 2026 |
| [ ] | Performance testing complete | Time E1 clone to Customize visible. Target 10 minutes. Record in session log. | Sarah | 15 Oct 2026 |
| [ ] | Security review complete | Confirm `install-local.sh` does not copy `.env`. Confirm `/ship` text forbids staging secrets. Spot-check `.gitignore`. | Sarah | 13 Oct 2026 |
| [ ] | Browser/device testing complete | Desktop Cursor on the owner's OS. One second environment for Casey path by 14 Nov. Skip iOS/Android. | Sarah | Phase 1: 15 Oct. Phase 2: 14 Nov. |
| [ ] | API documentation updated | Skip HTTP APIs. Update `install-work-kit` and README so cloud sync is required for cloud work, not optional. | Sarah | 13 Oct 2026 |

---

## 3. Content and copy

UX writing: tell the next step, not that install "succeeded."

| Done | Item | Work Kit meaning | Owner | Due |
| --- | --- | --- | --- | --- |
| [ ] | All copy reviewed | README install "Next" lines: Reload, confirm Work Kit, then open a product repo and run `/plan` (or `/debug` if something is already broken). | Sarah | 13 Oct 2026 |
| [ ] | Microcopy finalized | Script echo after `install-local.sh` matches README. Same three next steps, same order. | Sarah | 13 Oct 2026 |
| [ ] | Error messages written | Empty Customize: check User scope, reload, Teams Allow Local Plugin Imports, or fallback to `~/.cursor/skills`. `/debug` with no failure: ask expected vs actual. `/ship` on empty diff: do not create an empty commit. | Sarah | 13 Oct 2026 |
| [ ] | Help documentation complete | Casey pass/fail checklist in README Cloud Agents. Riley policy note. Tiny-skip rule in `plan-the-work` left as-is unless it contradicts the log. | Sarah | 14 Nov 2026 |
| [ ] | Release notes written | GitHub release or README changelog entry: "First delivery is the default path. Session log starts Q4." Plugin version bump only if scripts or skills changed. | Sarah | 15 Oct 2026 |
| [ ] | Marketing copy ready | One README paragraph. No ads. No slogan. | Sarah | 13 Oct 2026 |

---

## 4. Analytics and tracking

There is no Mixpanel. The dashboard is markdown plus git.

| Done | Item | Work Kit meaning | Owner | Due |
| --- | --- | --- | --- | --- |
| [ ] | Analytics events implemented | Create `docs/okrs/session-log.md` columns: date, repo, plan/tiny/debug/neither, ship, cloud, notes. | Sarah | 8 Oct 2026 |
| [ ] | Conversion tracking set up | Conversion is accepted `/plan` then `/ship`. Count rows, not pageviews. | Sarah | 8 Oct 2026 |
| [ ] | Error tracking configured | Log install recoveries: symlink dest, Teams block, skipped reload, cloud skills missing. | Sarah | 8 Oct 2026 |
| [ ] | Performance monitoring active | Two timed E1 installs in Q4. O1 KR1. | Sarah | 15 Oct and one more before 31 Dec |
| [ ] | User feedback mechanisms ready | Weekly 15-minute check-in in the OKR doc. End-of-quarter disappointment question on the core loop. | Sarah | Weekly from 8 Oct. Survey 31 Dec. |

---

## 5. Marketing and communication

Owned: GitHub README and repo. Rented and borrowed: skip this launch.

| Done | Item | Work Kit meaning | Owner | Due |
| --- | --- | --- | --- | --- |
| [ ] | Launch announcement prepared | README plus optional GitHub release notes. Audience is future-you and anyone who clones the repo. | Sarah | 15 Oct 2026 |
| [ ] | Email campaigns ready | Skip. No list. | N/A | Skip |
| [ ] | Social media posts scheduled | Skip. No Twitter/LinkedIn campaign. | N/A | Skip |
| [ ] | Blog post ready | Skip unless README is the post. Do not write a company blog. | N/A | Skip |
| [ ] | Press release | Skip. | N/A | Skip |
| [ ] | Internal communication sent | If a teammate uses Cursor with this kit by launch, send the README Cloud and first-delivery sections. Otherwise the session log is the internal record. | Sarah | 15 Oct 2026 |
| [ ] | Product Hunt listing | Skip. Wrong audience and wrong scope (launch skill: PH needs a list and all-day engagement). | N/A | Skip |

ORB for a later public launch, not Q4: owned README, rented Cursor forum or X only if Avery wants distribution, borrowed none until the loop is logged.

---

## 6. Operations and support

Support team is Sarah.

| Done | Item | Work Kit meaning | Owner | Due |
| --- | --- | --- | --- | --- |
| [ ] | Support team briefed | Re-read `install-work-kit`, `plan-the-work`, `ship-the-change`. | Sarah | 15 Oct 2026 |
| [ ] | FAQ prepared | Why is Customize empty. Why Cloud Agents lack skills. Why `/plan` skipped a tiny change. Why `/ship` refused `git add .`. | Sarah | 13 Oct 2026 |
| [ ] | Support documentation ready | FAQ lives in README or `skills/install-work-kit/SKILL.md`. | Sarah | 13 Oct 2026 |
| [ ] | Escalation process defined | Cursor product bugs (plugin path, sync toggle) go to Cursor support. Kit bugs stay in this repo. | Sarah | 13 Oct 2026 |
| [ ] | Monitoring dashboards set up | Weekly OKR table. Session log. Sync checker exit code. | Sarah | 8 Oct 2026 |
| [ ] | Rollback plan documented | `git checkout` previous `work-kit` copy is wrong. Re-run `install-local.sh` from a known good commit. For a bad skill, revert the SKILL.md commit and reinstall the same day (O4 KR2). Cloud: delete the bad folder under `~/.cursor/skills/` and re-sync. | Sarah | 13 Oct 2026 |

---

## 7. Legal and compliance

Personal MIT-licensed plugin. Do not invent a GDPR program.

| Done | Item | Work Kit meaning | Owner | Due |
| --- | --- | --- | --- | --- |
| [ ] | Privacy policy updated | Skip a public policy. Session log must not contain secrets, tokens, or customer PII from product repos. | Sarah | 8 Oct 2026 |
| [ ] | Terms of service reviewed | LICENSE is MIT. No change required for this launch. | Sarah | 8 Oct 2026 |
| [ ] | GDPR compliance verified | Skip as a launch workstream. No new personal-data processor. Session log is the owner's notes. | N/A | Skip |
| [ ] | Accessibility compliance verified | README and script output as in section 1. No new interactive UI. | Sarah | 10 Oct 2026 |
| [ ] | Data handling reviewed | `/ship` must not commit `.env`. Sync copies skill markdown, not credentials. | Sarah | 13 Oct 2026 |

---

## 8. Post-launch

| Done | Item | Work Kit meaning | Owner | Due |
| --- | --- | --- | --- | --- |
| [ ] | Monitoring plan active | Weekly 15-minute check-in. Monthly KR forecast. | Sarah | First Friday after 15 Oct |
| [ ] | Success metrics defined | O1 KR1 to KR3, O2 KR1 to KR2. See OKRs. | Sarah | Already in OKR doc |
| [ ] | Review meeting scheduled | Monthly deep dive. Quarterly grade first week of January 2027. | Sarah | Hold 31 Oct, 30 Nov, 7 Jan 2027 |
| [ ] | User feedback collection plan | Session log notes plus O4 KR3 disappointment question. | Sarah | Ongoing. Write KR3 on 31 Dec. |
| [ ] | Iteration plan ready | If O1 KR2 is low, fix habit or tiny-skip honesty, not catalogs. If O2 KR2 is low, fix sync and the Settings toggle. Next launch moment: only after 80% plan rate is in the log. | Sarah | 31 Oct 2026 (first monthly) |

---

## Launch day scripts

### 15 October 2026 (phase 1)

- [ ] SLC gate still passes
- [ ] Session log has at least one row
- [ ] Timed E1 recorded
- [ ] README next-steps include `/plan`
- [ ] `install-local.sh` echo matches README
- [ ] Open a product repo. `/plan` or tiny skip. `/ship` named files.
- [ ] Watch for install recoveries. Log them.

### 14 November 2026 (phase 2)

- [ ] Sync checker passes
- [ ] Casey checklist dry-run on a second environment
- [ ] Start counting Cloud Agent runs toward O2 KR2

Do not: email a list, file Product Hunt, post a press release, or dump playground skills as the announcement.

---

## Cut list (one more feature)

Leave out of this launch:

- Product Hunt, BetaList, Hacker News
- Waitlist landing page
- In-app "New" badge (no app chrome we own)
- Comparison pages vs other Cursor kits
- Interactive Navattic demo
- Paid ads

Those belong to a later public launch if Avery ever wants distribution. First delivery has to exist in the log first.
