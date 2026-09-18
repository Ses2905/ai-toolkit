# Acceptance criteria: US-5 named-file `/ship`

**Feature:** `/ship` stages only the files Avery meant, with hooks on, and does not commit secrets or `git add .` on a dirty tree.
**User story:** As Avery, I want `/ship` to stage the files I meant, with hooks on, so that a dirty tree does not ship `.env`, leftover notes, or a `--no-verify` skip I did not ask for. [US-5](work-kit-first-delivery-stories.md)
**User goal:** The commit matches `/review-diff`. Junk and secrets stay unstaged.
**Technical context:** Skill text in `skills/ship-the-change/SKILL.md` and verdict in `skills/review-the-diff/SKILL.md`. Git, hooks, GitHub remote. No scanner product in phase 1. Ten dirty-tree fixtures are F11, due 15 Dec, not this DoD.
**QA owner:** Sarah. No separate QA team.
**Related:** [Stories](work-kit-first-delivery-stories.md), [US-1 AC](us-1-g3-acceptance-criteria.md), [Scope](../launches/q4-2026-first-delivery-scope.md), [Metrics](../launches/q4-2026-first-delivery-metrics.md)
**Source prompt:** [Acceptance criteria generator](https://aiuxplayground.com/prompts/acceptance-criteria-generator) (AI UX Playground)

**Status 16 Sep.** Skill text already forbids `git add .` when unrelated files are present, forbids secrets and `.env`, and forbids `--no-verify` unless the user asks. This story is not done until a real product-repo `/ship` is logged with `named_files=yes` and a `git log --stat` audit finds no `.env` in that commit. Text without a sitting is not DoD.

Each criterion is pass/fail. Phase 1 "US-5 pass" means HP, VF, ER-1/ER-2, and MT-1 pass. F11 fixture runner is follow-up (ED-9).

---

## 1. Overview and definition of done

**In scope.** `ship-the-change` skill. `review-the-diff` verdict line (ship / fix blockers / needs verification). One go-live `/ship` in a product repo. One `git show --stat` (or `git log --stat`) on that commit. Session log columns `ship` and `named_files`.

**Out of scope.** Building a secret scanner. Changing git itself. `--no-verify` as a default. Creating a PR unless Avery asked (skill already says this). F11 ten fixtures. F14 hook-fail drill (related, later). US-1 copy. Mixpanel.

**Definition of done.**

1. VF-1 to VF-5 pass on `skills/ship-the-change/SKILL.md`.
2. VF-6 pass on `skills/review-the-diff/SKILL.md` (verdict is one of three words).
3. MT-1: a sitting that ran `/ship` (or `ship-the-change`) staged named paths only. Log row `ship=yes`, `named_files=yes`.
4. MT-2: `git show --stat` on that commit has no `.env`, no `*.log` that is gitignored, no credentials file.
5. `/review-diff` verdict recorded (F6): ship, fix, or verify.
6. If MT-2 fails, P0. Do not mark US-5 done. Do not go 15 Oct.

Not done: skill text looks right and the log is still blank.

---

## 2. Happy path criteria

Primary flow: after US-3 or US-4, `/review-diff` on `git diff`, verdict ship, then `/ship`.

| ID | Given | When | Then |
| --- | --- | --- | --- |
| HP-1 | Intended files are known. Tree may also have unrelated files | Avery runs `/ship` | Agent stages **named paths only**, not `git add .` |
| HP-2 | HP-1 | Commit is created | Message is imperative and specific. Subject about 50 to 72 characters. No `Co-authored-by` or AI trailer unless the repo already uses them |
| HP-3 | HP-1 | Verification | Lightest check that covers the change ran, or the skill asked for it before commit |
| HP-4 | Branch has no upstream | Push | `git push -u` on the current branch. No PR unless Avery asked |
| HP-5 | Hooks are installed | Commit and push | Hooks run. `--no-verify` is not in the commands |
| HP-6 | Review ran | Sitting ends | Log: `review` is `ship`, `fix`, or `verify`. `ship=yes` only if a commit was pushed |

**Expected outcome.** Remote branch has a commit whose `--stat` matches the intended files.

**Success indicators.** Phase 1: one such sitting (go-live). Q4: 8 named-file ships (O1 KR3). Zero `.env` from `/ship` (O3 KR3). Not NPS.

---

## 3. Edge cases

| ID | Case | Pass if |
| --- | --- | --- |
| ED-1 | Empty diff | No commit. Skill says confirm diff matches the request. Do not invent files |
| ED-2 | Mixed staged and unstaged | Only intended paths remain staged. Unrelated already-staged files are unstaged or never added |
| ED-3 | Unrelated markdown in the tree | Left unstaged |
| ED-4 | Tiny skip sitting (US-4) | Still named-file `/ship`. Tiny is not permission to `git add .` |
| ED-5 | `cursor-skills` doc-only sitting | May ship named docs. Mark log notes so KR2 denominator rules can exclude if needed |
| ED-6 | User explicitly asks `--no-verify` | Allowed only then. Skill still prefers fixing the hook. Record in log notes |
| ED-7 | User asked to create a PR | Cloud Agent / owner may open a PR. Skill default is no PR unless asked. This AC does not fail if a PR exists because the owner asked |
| ED-8 | Binary or large generated junk | Not staged. Skill: no generated junk |
| ED-9 | Ten synthetic dirty trees (F11) | Out of phase 1 DoD. Target 15 Dec. 10 of 10 named-path stage. Do not block US-5 DoD on missing fixtures |
| ED-10 | Agent ignores the skill and runs `git add .` | Behavior miss. Log `named_files=no`. Treat as US-5 fail for that sitting. Do not "pass" on skill text alone if MT-1 used `git add .` |

---

## 4. Error handling

| ID | Scenario | Pass if |
| --- | --- | --- |
| ER-1 | `.env`, credentials, or gitignored secrets in the working tree | Not staged. Not in `git show --stat`. If they land in a `/ship` commit: P0, stop 15 Oct, rewind or revert |
| ER-2 | Hook or push fails | Agent fixes the cause. Does not retry with `--no-verify` unless Avery said to |
| ER-3 | Diff does not match the request | No ship. Review verdict `fix` or `verify`. Extra files called out |
| ER-4 | Empty diff (also ED-1) | No empty commit. Feedback in chat: nothing to ship |
| ER-5 | Push rejected (auth, non-fast-forward) | Native git error. Recover: fetch/rebase or fix creds. Do not force-push unless Avery asked |

**Error messages.** Git's own output. Skill may restate "do not commit `.env`" in chat. No Work Kit toast.

**Recovery.** Unstage, add named paths, fix hooks, re-run `/review-diff`, `/ship` again.

**User feedback.** Chat plus `git status`. Log notes if P0.

---

## 5. Validation rules

| ID | Rule | Test |
| --- | --- | --- |
| VF-1 | Skill forbids `git add .` when unrelated files are present | `rg "git add \\." skills/ship-the-change/SKILL.md` matches a forbid, not an instruction to use it |
| VF-2 | Skill forbids secrets and `.env` | File contains `.env` and "Do not commit secrets" (or equivalent) |
| VF-3 | Skill forbids `--no-verify` unless the user explicitly wants it | File contains `--no-verify` in a do-not-unless-asked rule |
| VF-4 | Commit message rule | Imperative, specific, subject length guidance present |
| VF-5 | Before git: status, diff, lightest verification | Numbered "Before git" steps still in the skill |
| VF-6 | Review verdict | `review-the-diff` ends with ship / fix blockers / needs verification |
| VF-7 | Business: named files only | MT-1 `git show --stat` paths are a subset of what Avery named in chat or the plan |
| VF-8 | Permission | Script does not require sudo. Git uses Avery's creds. No token in the commit |
| VF-9 | Data | No `.env` content in blob. `git show --stat` is the phase 1 check, not a full history scan (monthly audit is O3 KR3) |

---

## 6. State management

| State | What it is | Pass if |
| --- | --- | --- |
| Initial | Dirty or clean working tree after implement | `git status` run (skill step 1) |
| Transition | Review verdict | `ship` proceeds to stage/commit/push. `fix` or `verify` does not push |
| Final | Commit on the branch, optionally on remote | HP-4. Log row filled (US-6) |
| Persistence | Git objects and session log | Commit SHA exists. Log `ship` column not blank for that sitting |

No app session store. Aborting `/ship` leaves the tree as git left it. Do not delete Avery's unrelated files to "clean" the tree.

---

## 7. UI/UX requirements

No Work Kit screen.

| ID | Requirement |
| --- | --- |
| UX-1 | Agent names the files it will stage before staging, or stages only paths already named in the sitting |
| UX-2 | Verdict is one of: ship, fix blockers, needs verification. Readable in chat |
| UX-3 | No dashboard, no ship button, no color-only status |
| UX-4 | Do not dump a 20-skill catalog into the commit message |
| UX-5 | Sentence case in skill text. Straight quotes |

Accessibility: chat and terminal. Skip WCAG on Cursor chrome.

---

## 8. Performance criteria

| ID | Requirement |
| --- | --- |
| PF-1 | `/ship` is a sitting wrap-up, not a batch job. No extra full-repo crawl beyond `git status` / `git diff` |
| PF-2 | Do not add network calls to a secret-scanning SaaS |
| PF-3 | Throughput: one operator, one branch |
| PF-4 | Resource: do not `git add` the whole dest plugin copy or `node_modules` |

No page-load budget. If someone adds a cloud scanner to "help" US-5, fail PF-2 and reopen scope.

---

## 9. Integration criteria

| ID | Integration | Pass if |
| --- | --- | --- |
| IN-1 | git | status, diff, add named paths, commit, push |
| IN-2 | Git hooks | Run on commit/push. `--no-verify` only if asked (HP-5, ER-2) |
| IN-3 | GitHub remote | Push current branch. PR only if asked |
| IN-4 | `review-the-diff` | Actual `git diff`, not intention. Verdict before ship |
| IN-5 | Session log | `ship` and `named_files` columns |
| IN-6 | External APIs | None required. No Mixpanel, no secret-scan vendor |
| IN-7 | Cursor slash `/ship` | Invokable after US-2. Maps to `ship-the-change` |

---

## 10. Testing requirements

**Unit.** Grep tests for VF-1 to VF-6 (skill text). Optional: a shell snippet that fails if `ship-the-change/SKILL.md` loses the `.env` or `--no-verify` lines. No CI vendor required.

**Integration.** F11 later: 10 dirty trees (`.env`, unrelated markdown, empty diff, hook-fail simulation, mixed staged/unstaged, …). Phase 1: skip the runner. Do one human dirty tree in MT-1 if the go-live repo is already dirty. If the tree is clean, still pass HP-1 (named paths of the files that changed). Note "tree was clean" in the log.

**E2E.** No Playwright. E2E is MT-1 plus MT-2.

**Manual (required).**

MT-1. In a product repo: `/review-diff`, then `/ship`. Record files named vs `git show --stat`. Log the row.

MT-2. `git show --stat <sha>` has no `.env`, no credential files, no gitignored `*.log`.

MT-3 (optional, F14). Trigger a failing hook once. Confirm the agent does not `--no-verify` unless asked. Not phase 1 DoD.

**Regression.** Any skill edit that instructs `git add .` as the default is an immediate US-5 fail. Re-run VF-1 on that diff.

---

## Traceability

| Criterion | Story | Gate |
| --- | --- | --- |
| HP-1, VF-1, VF-7, MT-1 | US-5 | O1 KR3, O3 |
| ER-1, MT-2 | US-5 | G4 / O3 KR3 P0 |
| HP-6, VF-6 | F6 | O3 KR2 |
| ED-9 | F11 | 15 Dec, not 15 Oct |
| MT-3 | F14 | Later |
| Log row | US-6 | G2 |

Ready for QA this week: VF grep plus MT-1 on the next real sitting. Do not wait for a fixture framework to close US-5. Do not close US-5 on grep alone.
