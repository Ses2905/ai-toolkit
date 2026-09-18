# User stories: Work Kit first delivery

**Epic:** First delivery. After one user-scope install, the next product-repo change is `/plan` (or a marked tiny skip), then named-file `/ship`.
**Persona:** Avery, solo IC on desktop Cursor. Ships with git weekly. Uses Agent or chat to change code.
**Business goal:** O1. 15 Oct go-live is G1-G4. Q4 grade is 80% plan-or-tiny and 8 named-file ships. Not ARR. Not NPS.
**Feature:** Install copy, slash loop, log. Not a new Work Kit screen.
**Related:** [User flow](work-kit-first-delivery.md), [Scope](../launches/q4-2026-first-delivery-scope.md), [Priority](../okrs/q4-2026-feature-priority.md), [Problem statement](../problem-statements/work-kit-first-delivery.md), [US-1 AC](us-1-g3-acceptance-criteria.md), [US-5 AC](us-5-ship-acceptance-criteria.md), [WK-1 ticket](../tickets/wk-1-g3-install-copy.md)
**Source prompt:** [User story writing](https://aiuxplayground.com/prompts/user-story-writing) (AI UX Playground)

Phase 1 backlog is US-1 through US-6. US-7 is phase 2. Riley is not a story this quarter. Live G3 still fails: treat US-1 as open until `install-local.sh` and README match.

Shared design (all stories). No Work Kit UI. Copy lives in README and script echo. Sentence case. Numbered lists, not color-only status. README readable on GitHub mobile. Skip WCAG on Cursor chrome we do not own.

Shared tech. Real directory at `~/.cursor/plugins/local/work-kit`. No checkout symlink. Hooks stay on. MIT. One owner.

---

## Backlog

| ID | Title | Persona | Phase | Priority ID |
| --- | --- | --- | --- | --- |
| US-1 | Install next-steps tell me to `/plan` | Avery | 15 Oct | F1 / G3 |
| US-2 | Customize shows Work Kit after reload | Avery | 15 Oct | O1 KR1 |
| US-3 | I can accept or reject a plan before edits | Avery | 15 Oct | O1 KR2 |
| US-4 | Tiny work is a logged skip, not a fake plan | Avery | 15 Oct | F4 |
| US-5 | `/ship` stages named files only | Avery | 15 Oct | F5 / O3 |
| US-6 | I log the sitting | Avery | 15 Oct | F2 / G2 |
| US-7 | Cloud run loads synced core skills | Casey | 14 Nov | F7 F8 F10 |

---

## US-1. Install next-steps tell me to `/plan`

**As a** Avery (desktop IC)
**I want** the install script and README to name `/plan` as the third step after Reload and Customize
**So that** I start first delivery instead of stopping at a plugin card or optional cloud sync

**Persona context.** Follows numbered lists. Has not memorized the kit. Will do what step 3 says.

**Business value.** G3. Without this, 15 Oct is no-go. Clone visitors learn the skip.

**User value.** Knows the next action in one glance. Does not have to read a catalog of slash names to find `/plan`.

### Acceptance criteria

Happy path:

- After `./scripts/install-local.sh` succeeds, stdout lists exactly three next-steps: (1) Developer, Reload Window (2) Customize, filter User, confirm Work Kit (3) open a product repo and `/plan`, or `/debug` if something is already broken.
- README clone path and checkout path use the same three beats, same order, same meaning.
- Cloud sync is not item 3 on those lists. It lives under a Cloud Agents heading.

Edge:

- E2 reinstall prints the same three beats.
- Tiny-change hint may appear in prose, not as a fourth numbered install step.

Error:

- Script failure (`set -e`) does not print a success next-step list. User sees the command error.

Success:

- A reviewer can diff script echo vs README and find no drift on the three beats.
- Usability (after this lands): Avery attempts `/plan` without the researcher saying the slash. Survey Q10 copy-led `/plan` is the later research check, not a 15 Oct KPI.

Fail today: script item 3 is still "Optional for Cloud Agents: ./scripts/sync-user-skills.sh". This story is not done.

### User flow

Entry: E1 or E2, or README in a browser.
Steps: clone or cd, `chmod +x` if needed, run install, read "Next:".
Decision: D2 plugin visible, then D4 plan vs tiny vs debug. Copy must point at D4, not at E7.
Exit: user opens a product repo and types `/plan` or `/debug`.
Alt: user ignores copy (cannot prevent). Log as `neither` in US-6. Do not add a modal.

### Technical considerations

- Edit `scripts/install-local.sh` echo block and README install sections in the same change.
- Do not symlink dest. Do not change copy destination.
- Dependency: none besides git and Cursor already installed.
- Constraint: no first-run UI.

### Design requirements

- Three numbered lines. Short. Imperative.
- Do not bury `/plan` inside a 20-name slash inventory.
- No color badges as the only status.

### Success metrics

- G3 binary: match vs mismatch. Not NPS.
- Later: usability copy-led `/plan`. Do not wait for that to ship this story.

### Related

- Blocks US-3 usability of copy. Does not block the slash existing.
- Follow-up: US-7 Casey list, after this, not instead of this.

---

## US-2. Customize shows Work Kit after reload

**As a** Avery
**I want** Work Kit to appear under Customize, User, after Reload Window
**So that** I know the plugin loaded on this machine

**Persona context.** Owns the machine. Can reload. Filters User, not Project.

**Business value.** O1 KR1 timed E1. Discover step of the funnel.

**User value.** Confirm install before starting `/plan`. Empty card is a real stop.

### Acceptance criteria

Happy:

- `~/.cursor/plugins/local/work-kit` is a real directory.
- After Reload, Customize, User, displayName Work Kit is visible.
- Slash commands `/plan`, `/debug`, `/review-diff`, `/ship` are invokable.

Edge:

- E2 overwrite of an existing dest still results in a real directory, not a symlink to the checkout.
- Filter Project does not show the user-scope plugin. Copy says filter User.

Error:

- Script cannot write dest: non-zero exit, no "Installed work-kit" success.
- Teams empty card: out of this story. Point at recovery paragraph (not a phase 1 story). Do not "fix" with a symlink.

Success:

- Two timed E1 runs, each 10 minutes or less, minutes written in the session log.

### User flow

Entry: E1/E2 after US-1 copy.
Steps: reload, Customize, User, confirm card.
Decision: D2 visible? Yes -> US-3. No -> error/recovery.
Exit: card visible.
Alt: E3 skills-only. User chose that. Card may be absent. Not this story's happy path.

### Technical considerations

- `install-local.sh` copy via rsync or tar. Exclude `.git`, `agent-tools`, `.DS_Store`.
- Cursor must load local plugins from that dest. Not owned by this repo. If Cursor stops loading them, slip E1.

### Design requirements

- We do not design Customize. We tell the user which filter to use.

### Success metrics

- O1 KR1: 10 minutes, twice.
- Day 1: Customize yes.

### Related

- Depends on a successful script run. Follows US-1 copy. Enables US-3.

---

## US-3. I can accept or reject a plan before edits

**As a** Avery
**I want** `/plan` to produce a plan I can accept or reject before the agent edits
**So that** first-slice work does not start in chat with no gate

**Persona context.** Non-trivial change in a product repo, not only `cursor-skills` chores.

**Business value.** O1 KR2. Aha moment in the user flow.

**User value.** Can refuse a plan. Avoids a sitting that is already mid-edit.

### Acceptance criteria

Happy:

- In a product repo, `/plan` (or `plan-the-work`) writes a plan and waits for accept or reject before file edits.
- After accept, implementation follows the accepted slice.
- After reject, no silent continue as if accepted.

Edge:

- Agent-decides (E6) should still plan on non-tiny work. If it does not, log `neither`. Do not expand this story into F16 in phase 1.
- Cursor-skills doc-only sitting may be excluded from the KR denominator per metrics spec.

Error:

- `/plan` skill missing: US-2 failed. Reinstall (F13), do not chat-implement as a workaround in the AC.

Success:

- Session log `entry=plan` for that sitting.
- Q4: 80% of logged product-repo sittings are `plan` or `tiny`. Phase 1 needs at least the go-live row.

### User flow

Entry: E5 `/plan` after US-1 and US-2.
Steps: open product repo, `/plan`, read plan, accept or reject.
Decision: D4 plan vs tiny vs debug. This story is the plan branch.
Exit: accepted plan, or rejected and stopped.
Alt: reject then rewrite the request. Still this story. Chat-implement with no `/plan` is US-6 `neither`, a miss.

### Technical considerations

- Skill `plan-the-work`. We own text, not the agent runtime.
- Constraint: cannot patch Cursor to hard-stop edits. Phase 1 AC is skill plus copy plus log, not a new runtime lock.

### Design requirements

- Plan is readable in chat. No new layout. Do not add a Work Kit web board.

### Success metrics

- Plan-or-tiny rate. Log, not CSAT.
- Do not use NPS.

### Related

- US-4 is the tiny branch of D4. US-1 makes the entry discoverable. F16 follow-up only if log shows skip after G3.

---

## US-4. Tiny work is a logged skip, not a fake plan

**As a** Avery
**I want** to mark an obvious one-file change as tiny skip
**So that** the 80% rate stays honest and I do not write a six-section plan for a rename

**Persona context.** Knows when a change is already obvious.

**Business value.** O1 KR2 denominator. Fake plans inflate the rate.

**User value.** Loop still applies. Less ceremony when the work is tiny.

### Acceptance criteria

Happy:

- Before edits, the log row (or a note that will become the row) says `tiny`.
- `/ship` still names files (US-5). Tiny is not `git add .`.

Edge:

- If the sitting grows past tiny, start `/plan`. Do not keep `tiny` on a multi-file surprise.

Error:

- Using tiny to avoid planning a non-trivial feature is a miss. Call it out in notes. Do not add a linter for this in phase 1.

Success:

- `entry=tiny` rows exist. Plan rate is not 100% of six-section fiction.

### User flow

Entry: D4 tiny branch.
Exit: implement, then US-5.
Alt: mid-sitting upgrade to `/plan` (US-3).

### Technical considerations

- Convention in `docs/okrs/session-log.md`. No new flag in Cursor.

### Design requirements

- None beyond the log table. Do not add a Tiny button in a UI we do not have.

### Success metrics

- Presence of `tiny` rows when work was tiny. Qualitative check weekly.

### Related

- Depends on US-6. Follows US-3 as the other D4 branch.

---

## US-5. `/ship` stages named files only

**As a** Avery
**I want** `/ship` to stage the files I meant, with hooks on
**So that** a dirty tree does not ship `.env`, leftover notes, or a `--no-verify` skip I did not ask for

**Persona context.** Working trees are often dirty. May have `.env` next to the patch.

**Business value.** O3 KR3. G4 adjacent. Secrets in a push are P0.

**User value.** Commit matches the review. No junk in git.

### Acceptance criteria

Happy:

- `/ship` / `ship-the-change` instructs staging named paths only.
- Commit message is imperative and specific.
- Hooks run. `--no-verify` is not used unless Avery asked.

Edge:

- Empty diff: do not invent a commit.
- Mixed staged/unstaged: only intended paths.
- Unrelated markdown in the tree: left unstaged.

Error:

- `.env` or gitignored secrets: not staged. If they appear in a `/ship` commit, P0, stop go-live.
- Skill must not recommend `git add .` when unrelated files exist.

Success:

- Go-live row `ship=yes` and `named_files=yes`.
- Phase 1: one `git log --stat` audit. Fixtures (F11) are follow-up, not this story's gate.

### User flow

Entry: after US-3 or US-4, `/review-diff`, then `/ship`.
Decision: review verdict ship / fix / verify (F6).
Exit: push on a branch, or abort on empty/secret.
Alt: fix blockers, re-review, ship.

### Technical considerations

- Skill text in `ship-the-change` and `review-the-diff`.
- Git hooks. Integration: git, GitHub remote.
- Constraint: no scanner product in phase 1.

### Design requirements

- Review output names files. No dashboard.

### Success metrics

- Named-file ship count (O1 KR3 target 8 by 31 Dec). Phase 1: at least the go-live ship.
- Zero `.env` from `/ship` this quarter.

### Related

- F11 fixtures follow-up. F14 hook drill follow-up. F6 verdict is part of the exit.

---

## US-6. I log the sitting

**As a** Avery
**I want** one markdown row per product-repo sitting
**So that** plan-or-tiny has a denominator and skip is visible

**Persona context.** Same person as the operator. Will not fill Mixpanel.

**Business value.** G2. Without a row, 80% is ungradable.

**User value.** Weekly 15-minute check has numbers.

### Acceptance criteria

Happy:

- After a sitting, `docs/okrs/session-log.md` has date, repo, who, `entry` in `plan`/`tiny`/`debug`/`neither`, ship yes/no, named_files yes/no as applicable.
- Header-only table is not done.

Edge:

- `cursor-skills` doc-only row may be excluded from KR2 per metrics spec. Mark notes.
- Missing week: count 0. Do not impute.

Error:

- Lost notes: still do not invent `plan`. Use `neither` or omit and treat as 0.

Success:

- 15 Oct go-live row complete. Then ongoing.

### User flow

Entry: end of sitting, or start-of-sitting capture of `entry`.
Exit: saved markdown.
Alt: none. Not logging is a miss, not an alt path.

### Technical considerations

- File already exists. This story is use, not a new app.
- No analytics vendor.

### Design requirements

- Table stays a table. Do not build a dashboard to complete this story.

### Success metrics

- Rows with non-empty date and repo. Plan-or-tiny rate defined in metrics spec.

### Related

- Required by US-3, US-4, US-5 measurement. Independent of US-7.

---

## US-7. Cloud run loads synced core skills (phase 2)

**As a** Casey (cloud-first)
**I want** a Cloud Agent run to load `plan-the-work` or `debug-from-evidence` from `~/.cursor/skills/`
**So that** I am not planning on a VM that never saw the kit

**Persona context.** Desktop plugin path does not exist on the VM.

**Business value.** O2. Not a 15 Oct blocker.

**User value.** Same loop off-machine.

### Acceptance criteria

Happy:

- After `./scripts/sync-user-skills.sh`, five core folders exist under `~/.cursor/skills/`.
- Checker exits non-zero on a miss.
- README Cloud section: plugin card missing, skills still required. Sync is required for cloud work, not Avery step 3.
- Settings toggle Sync Skills for Cloud Agents is on.
- A run loads `plan-the-work` or `debug-from-evidence`.

Edge:

- Avery desktop install must not list this as numbered step 3 (US-1).

Error:

- Checker red: do not start the run.

Success:

- 6 such runs by 31 Dec. Checker green before counting them.

### User flow

Entry: E7. After US-1 so lists are split.
Exit: run that loaded a core skill, or abort on red checker.
Alt: skip cloud this quarter. Phase 1 still ships.

### Technical considerations

- `scripts/sync-user-skills.sh` plus new fail-closed check.
- Dependency: Cursor sync toggle. Not owned.

### Design requirements

- Casey section in README. Pass/fail boxes. Not Avery's three beats.

### Success metrics

- O2 KR1 script. O2 KR2 six runs. O2 KR3 stranger checklist.

### Related

- Blocked by US-1 split lists. Follows F7 F8 F9 F10. Do not pull into phase 1 to look complete.

---

## Out of backlog (do not write stories)

- Marketplace listing, first-run UI, NPS, Mixpanel, Product Hunt, catalog dump, Riley happy path, public GA.

If a request is not US-1 through US-7, see [scope](../launches/q4-2026-first-delivery-scope.md) section 8.
