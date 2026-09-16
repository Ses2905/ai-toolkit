# Scope: Work Kit first delivery

**Project name:** Work Kit first delivery (Plan to Ship as the default path)
**Problem:** Install can succeed while the next sitting starts in chat with no plan. Cloud sync is easy to skip. `/ship` can still meet a dirty tree.
**Target users:** Avery (solo IC, desktop Cursor) is in scope. Casey (Cloud Agents) is phase 2. Riley (Teams/Enterprise) is recovery copy only.
**Timeline:** Phase 1 go-live 15 Oct 2026. Cloud 14 Nov. Grade 31 Dec. G3 copy due 8 Oct.
**Resources:** One owner, Sarah Scherer. $0 paid GTM. MIT. No separate eng/design/research team.
**Related:** [Problem statement](../problem-statements/work-kit-first-delivery.md), [Priority](../okrs/q4-2026-feature-priority.md), [Checklist](q4-2026-first-delivery-checklist.md), [User flow](../user-flows/work-kit-first-delivery.md), [OKRs](../okrs/q4-2026-work-kit.md)
**Source prompt:** [Scope definition](https://aiuxplayground.com/prompts/scope-definition-template) (AI UX Playground)

This is the freeze for phase 1. If a request is not in section 2, it is out until Sarah files a change (section 8). Playground templates are not scope. F1 (G3 copy) is.

**Status.** Proposed 16 Sep 2026. Not signed. Live product still fails G3. Signing this document does not replace editing `install-local.sh`.

---

## 1. Project overview

**One-sentence summary.** Make Work Kit's next-steps produce an accepted `/plan` (or a marked tiny skip) and a named-file `/ship` in a product repo after one user-scope install, without copying kit files into each app.

**Success statement.** This project is successful when, on 15 Oct, Customize shows Work Kit, `install-local.sh` and README step 3 are `/plan` or `/debug` if broken, the session log has a go-live row that is plan-or-tiny plus named-file `/ship`, and there are no secrets in that push.

Q4 grade (31 Dec) is a later bar: 80% plan-or-tiny, 8 named-file ships. It is not phase 1 launch success.

---

## 2. In scope (explicitly)

### Features and functionality

Phase 1 (must, by 15 Oct):

- **F1 G3 copy.** README and `install-local.sh` identical. Step 3 is `/plan` (or `/debug` if broken). Cloud sync is not Avery's third beat.
- **F2 Session log in use.** One row per product-repo sitting. Header-only is not in-scope complete.
- **F3 Timed E1.** Clone to Customize visible, twice, 10 minutes or less, written in the log.
- **F4 Tiny-skip logging.** Honest tiny rows. No fake six-section plan.
- **F5 `/ship` secrets text plus one `git log` audit.** Confirm skill forbids `.env` and `git add .` on unrelated files.
- **F6 Review verdict footer.** Ship / fix / needs verification on each `/ship` branch.
- **F13 Same-day reinstall** after a skill-add commit.

Phase 2 (in scope for 14 Nov, not for 15 Oct):

- **F7 Sync checker.** Fail if any of the five core skill folders is missing.
- **F8 Casey README.** Plugin card missing, skills still required. Pass/fail boxes.
- **F9 Second-environment Casey run.**
- **F10 Six Cloud Agent runs** that load `plan-the-work` or `debug-from-evidence`. Starts after F7 is green.

Phase 3 (in scope for 31 Dec grade, not for 15 Oct):

- **F11 Dirty-tree fixtures** (10 cases). May slip to 15 Dec without blocking phase 1.
- **F12 Four captures** from log repeats only.
- **F14 Hook-fail drill.**
- **F15 Riley recovery paragraph.**

Research, leftover hours only (does not block F1):

- **F17 Problem interviews** n=5 to 8. Current workflow. Can run before G3.
- **F18 Usability and beta survey.** After G3 only.

### User flows

- **E1/E2 Avery happy path.** Clone or existing checkout, `install-local.sh`, Reload, Customize User shows Work Kit, `/plan` or tiny skip, `/review-diff`, `/ship` named files in a product repo.
- **Tiny skip.** Logged, then implement.
- **Debug-first.** `/debug` when something is already broken.
- **E7 Casey.** Phase 2 only. Sync script, checker, Settings toggle.

### Platforms and environments

- Desktop Cursor on the owner's OS (macOS or Linux).
- Git, GitHub clone, local terminal.
- Cloud Agent VMs: phase 2, skills path only.
- Production for this kit is `main` plus the owner's user-scope install. There is no staging web app.

### User segments

- Avery: in. Primary.
- Casey: phase 2 in. Not a 15 Oct blocker.
- Clone visitor following README: in, same copy as Avery.
- Riley: recovery paragraph only.

### Integrations

- Cursor user-scope local plugins (`~/.cursor/plugins/local/work-kit`).
- Cursor skill library (`~/.cursor/skills/`) and Sync Skills for Cloud Agents (phase 2).
- Git hooks stay on.
- GitHub as clone source and issue tracker.

---

## 3. Out of scope (explicitly)

### Not building

- First-run UI, metrics dashboard app, marketplace listing. We do not own Cursor chrome. SLC: not simple.
- Mixpanel, Amplitude, GA4, NPS tracker. Session log is the instrument.
- Paid waitlist, billing, auth, multiplayer admin.
- Enforcing the plan gate inside Cursor's agent runtime (F16 is stretch, 31 Dec, only if the log still shows skip after G3).
- Catalog dumps or installing every Playground skill into the kit as "launch content."
- Comparison SEO, Product Hunt gallery, press site, email drip.

### Not addressing now

- Skipper hypothesis in other ICs. Interviews are leftover hours. Do not delay F1 for n=5.
- Teams admin unlocking local plugins. We cannot set that policy.
- Cloud-first as the happy path before 14 Nov.
- Repeat-workflow capture as a substitute for plan-or-tiny (O4 follows O1).

### Not supporting

- iOS, Android, web app, Windows-only QA as a launch gate (owner OS only for phase 1).
- Cursor Enterprise as happy path.
- SLA support, chat widget, on-call rotation.
- Guests who do not use git or Cursor.

### Future consideration (after 31 Dec, and only if O4 KR3 is "very disappointed")

- Plan-gate hardening (F16) if copy is good and skip remains.
- Stronger Casey tooling if six runs miss skills.
- Riley as a real path if the owner is on Teams.
- Not: public GA as a default next phase.

---

## 4. Scope boundaries

| Decision point | In scope | Out of scope | Rationale |
| --- | --- | --- | --- |
| Job | First delivery: `/plan` then named-file `/ship` | Plugin-visible as success | Problem statement |
| User | Avery desktop | Riley happy path, press, sales | One operator |
| Install copy | Three beats: Reload, Customize, `/plan` | Optional sync as Avery step 3 | G3. Mixing lists caused the miss |
| Cloud | Phase 2 from 14 Nov | Cloud work that blocks 15 Oct | Checklist SLC |
| Research | Leftover interviews. Survey after G3 | Mixed synthesis with invented n | Empty instruments |
| Metrics | Session log, git | NPS, ARR, Mixpanel | OKRs |
| Channel | README, script echo | Product Hunt, ads, PR wire | $0 GTM |
| Skills | Core five plus reinstall | Playground catalog as launch | O4 counts repeats only |
| Ship | Named paths, hooks on | `--no-verify` by default, `git add .` | O3 |
| Docs | Copy that installers read | Another Playground template before F1 | Insights 3 |
| Surfaces | Terminal, README, Cursor chrome we already have | New Work Kit screens | No product UI |

---

## 5. Assumptions

**Technical.** Cursor still loads user-scope plugins from `~/.cursor/plugins/local/` as a real directory, not a checkout symlink. If wrong: E1 breaks. Re-read `install-work-kit` and slip.

**Technical.** Cloud VMs still do not mount local plugins. If wrong: F8/F7 change. Do not put sync back as Avery step 3 without a new scope change.

**User.** Avery will log sittings. If wrong: O1 KR2 is 0. Do not impute. Do not buy analytics.

**User.** Skippers exist outside this repo. If wrong: F17 finds planners only. Still ship F1. Copy-led `/plan` is for clone visitors, not only skippers.

**Business.** $0, MIT, internal go-live. If someone wants a billed product: new project, not a change to this one.

**Resource.** One owner can land F1 in under 2 hours. If that session is spent on templates instead: 15 Oct stays no-go. Impact is the whole launch.

**Dependencies.**

| Dependency | Owner | If unmet |
| --- | --- | --- |
| G3 copy in script and README | Sarah | No-go 15 Oct |
| Session log rows | Sarah | Cannot grade 80% |
| Cursor plugin and sync behavior | Cursor | Patch scripts or slip |
| Teams Allow Local Plugin Imports | Admin, if Riley is tried | E3 fallback. Not a phase 1 gate |
| GitHub clone | GitHub | E1 blocked |

---

## 6. Constraints

**Hard.**

- Dates: 8 Oct SLC, 15 Oct phase 1, 14 Nov phase 2, 31 Dec grade. Slip the day rather than launch on yellow G3. Do not move the date to add catalog skills.
- Budget: $0 paid. Gift cards for research only if a $400 cap is approved. Default unpaid.
- Surfaces: Cursor, git, terminal, GitHub README. No new web app.
- License: MIT. No secrets in git.
- `/ship` must not `--no-verify` unless asked.
- One decision maker.

**Soft.**

- Avery remains primary even if a teammate clones.
- Sentence-case, straight quotes, no launch fanfare in README.
- Research n cap 8.
- Playground skill installs stay out of the plugin tree unless captured from real repeats.

---

## 7. Success criteria

**Minimum viable (must have for 15 Oct).**

- G1 SLC boxes that apply to phase 1 are checked.
- G2 log exists with at least one completed go-live row (not only headers).
- G3 copy match: step 3 is `/plan` or `/debug` if broken.
- G4 no secrets on the launch diff. `/review-diff` done.
- Customize shows Work Kit after reload.

**Target (plan to include by 15 Oct, still phase 1).**

- F3 two timed E1 runs.
- F4, F6, F13 habits started.
- F5 one audit.

**Stretch (if time, still not cloud).**

- F17 interviews in leftover hours.
- F18 usability after G3, only if F1 already landed.
- F16 not stretch for 15 Oct. It is 31 Dec and evidence-gated.

**Not success.** Number of docs in `docs/`. Number of Playground skills in `.agents/`. Plugin card without a log row.

---

## 8. Scope change process

If someone (including a Cloud Agent filling a template) wants work that is not in section 2:

1. Write the request in one paragraph: job, hours, which gate it affects (15 Oct / 14 Nov / 31 Dec / cut).
2. Score it on the [priority matrix](../okrs/q4-2026-feature-priority.md). Gate first, then value/effort.
3. Sarah approves or refuses. There is no committee.
4. Update this file and the matrix. If it threatens G3, refuse.

**Default refuse.** Marketplace, NPS, first-run UI, public GA, catalog dump, mixed research synthesis with n=0, another Playground doc before F1.

**Triggers that force a scope discussion.**

- Cursor changes plugin or sync paths.
- G3 still fails on 8 Oct.
- Two of five survey Q21 = no after G3 (slip 15 Oct).
- A `/ship` that contains `.env` (P0, expand F5/F11, still do not add a scanner product without a change request).
- Owner moves to a Teams seat (promote F15).
- O4 KR3 on 31 Dec is not "very disappointed" (do not start a 2027 platform).

---

## 9. Sign-off

Proposed. Not agreed until 8 Oct SLC, and only if G3 is actually patched.

| Role | Name | Date | Sign |
| --- | --- | --- | --- |
| Product | Sarah Scherer | 8 Oct 2026 | Pending |
| Engineering | Sarah Scherer | 8 Oct 2026 | Pending |
| Design (copy) | Sarah Scherer | 8 Oct 2026 | Pending |
| Stakeholder (operator) | Sarah Scherer | 8 Oct 2026 | Pending |

There are no other signers. A filled Playground template is not a signature.

**How to treat this file until F1 lands.** Binding for what not to build. Not evidence that first delivery shipped.
