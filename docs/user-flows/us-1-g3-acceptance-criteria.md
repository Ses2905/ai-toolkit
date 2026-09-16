# Acceptance criteria: US-1 G3 install copy

**Feature:** After a successful desktop install, next-steps tell Avery to `/plan` (or `/debug` if broken). Cloud sync is not step 3.
**User story:** As Avery, I want the install script and README to name `/plan` as the third step after Reload and Customize, so that I start first delivery instead of stopping at a plugin card or optional cloud sync. [US-1](work-kit-first-delivery-stories.md)
**User goal:** Know the next action without a researcher and without reading a slash catalog.
**Technical context:** Copy only. `scripts/install-local.sh` echo block plus README install sections. Dest path and rsync/tar behavior stay. No new UI. No Cursor runtime change.
**QA owner:** Sarah (same as eng). There is no separate QA team.
**Related:** [Stories](work-kit-first-delivery-stories.md), [Scope](../launches/q4-2026-first-delivery-scope.md), [Runbook G3](../launches/q4-2026-first-delivery-runbook.md), [WK-1 ticket](../tickets/wk-1-g3-install-copy.md)
**Source prompt:** [Acceptance criteria generator](https://aiuxplayground.com/prompts/acceptance-criteria-generator) (AI UX Playground)

**Fail on 16 Sep (must turn green).** Script line 30: `Optional for Cloud Agents: ./scripts/sync-user-skills.sh`. README clone numbered item 3: Cloud Agents sync toggle. README checkout items 3-4: catalog of skill names. Clone bash block runs `sync-user-skills.sh` immediately after install, which reads as required desktop finish.

Each criterion is pass/fail. "G3 pass" means every HP, VF, and SM row below is pass, and ER-1 holds on a forced script failure.

---

## 1. Overview and definition of done

**In scope files.** `scripts/install-local.sh` (echo after successful copy only). README sections "Install from GitHub (desktop skill library)" and "Install from this directory". Cloud Agents section for relocated sync copy.

**Out of scope for this AC.** Changing dest from `~/.cursor/plugins/local/work-kit`. Adding a first-run UI. Enforcing plan-accept in the agent runtime. Fielding the beta survey. US-2 timed E1 (separate story). US-7 checker (phase 2).

**Definition of done.**

1. All happy-path criteria (HP-1 to HP-6) pass on a machine that can run the script.
2. A reviewer diffs script echo vs the two README numbered lists and finds the same three beats, same order, same meaning.
3. `git grep -n "Optional for Cloud Agents"` on `scripts/install-local.sh` returns no matches.
4. Checkout README numbered install list does not include `/install-impeccable` or Remotion names as the third beat.
5. `/review-diff` run on the copy change. No secrets. Story US-1 marked done.
6. Manual test MT-1 recorded in the session log notes (pass/fail).

Not done: docs that describe G3 while the echo is unchanged.

---

## 2. Happy path criteria

Primary flow: E1 or E2, run `./scripts/install-local.sh` from a checkout that contains `skills/`, read stdout, open README, follow numbered steps.

| ID | Given | When | Then |
| --- | --- | --- | --- |
| HP-1 | Script copy to dest succeeds | stdout is printed | A line `Next:` appears, then exactly three numbered items, and no item 4 in that list |
| HP-2 | HP-1 | Read item 1 | It tells Avery to use Command Palette, Developer: Reload Window |
| HP-3 | HP-1 | Read item 2 | It tells Avery to open Customize, filter User, confirm Work Kit |
| HP-4 | HP-1 | Read item 3 | It tells Avery to open a **product repo** and run `/plan`, or `/debug` if something is already broken. It does not say optional cloud sync. It does not say only "confirm Work Kit" again |
| HP-5 | README clone install section | Read the numbered list after the install commands | Same three beats as HP-2 to HP-4, same order |
| HP-6 | README checkout install section | Read the numbered list after `./scripts/install-local.sh` | Same three beats as HP-2 to HP-4. No fourth numbered beat that is a catalog dump |

**Expected outcome.** Avery who follows the list reloads, confirms the card, then types `/plan` or `/debug` in a product repo.

**Success indicators.** G3 binary = pass. Later usability (not this story's DoD): they type `/plan` without being told. Survey Q10 copy-led `/plan` is research after G3, not a ship gate for US-1.

---

## 3. Edge cases

| ID | Case | Pass if |
| --- | --- | --- |
| ED-1 | E2 reinstall over existing dest | Success echo is the same three beats as E1. Dest remains a real directory, not a symlink to the checkout |
| ED-2 | Tiny-change hint | If mentioned, it is a sentence after the list, not numbered step 4 of install |
| ED-3 | `npx skills add` paragraph | Still allowed as an alternate. It must not be numbered step 3 of the plugin install list. It must not claim slash commands exist without the plugin |
| ED-4 | Clone bash still mentions `sync-user-skills.sh` | If the command stays in a fenced block, a sentence must say it is for the skill library / Cloud Agents, not the finish line. Numbered item 3 remains `/plan`. Prefer: move the sync command out of the default clone block into the Cloud Agents section |
| ED-5 | Teams note | May remain near install. Must not replace step 3 |
| ED-6 | `install-work-kit` skill text | If it lists next-steps, they match HP-2 to HP-4. If you do not edit that skill in this change, file a follow-up. Drift there is a P2, not a G3 fail, unless it is the only path a user sees |
| ED-7 | Unicode arrows in echo (`→`) | Allowed if README uses the same meaning. Do not require identical punctuation if meaning matches. Prefer matching strings to make VF-1 easy |
| ED-8 | User already has Cloud Agents as their only workflow | They still see Avery's three beats on desktop install. Casey steps live in the Cloud Agents section (US-7), not as desktop step 3 |

---

## 4. Error handling

| ID | Scenario | Pass if |
| --- | --- | --- |
| ER-1 | Script exits non-zero (`set -e`): missing `skills/`, dest not writable, rsync/tar fail | Stdout does not print the success `Next:` three-beat list. User sees the shell error. No fake "Installed work-kit" after a failed copy |
| ER-2 | Dest would be a symlink into the checkout | Script does not instruct the user to ln -s. Copy stays a real directory. Cursor ignores those symlinks |
| ER-3 | User skips Reload | Copy cannot force reload. Item 1 still says to reload. Empty Customize is US-2 recovery, not a new error toast |
| ER-4 | User follows old cached README on GitHub until push | Out of this story once `main` (or the install branch they clone) has the new list. Do not build a version check |

**Error messages.** Keep script `set -e` failures as native command errors. Do not add a Work Kit GUI error. Do not print "success" next-steps on failure.

**Recovery.** Fix permissions or missing `skills/`, re-run. Do not recover by symlinking.

**User feedback.** Terminal stdout only.

---

## 5. Validation rules

| ID | Rule | Test |
| --- | --- | --- |
| VF-1 | Meaning match | Extract the three numbered beats from script echo, README clone list, README checkout list. Each beat 1, 2, 3 names the same action |
| VF-2 | Forbidden strings in the success echo and in those two numbered lists | Must not contain `Optional for Cloud Agents` as item 3. Must not contain `Sync Skills for Cloud Agents` as item 3. Must not use `/install-impeccable` or `remotion` as item 3 |
| VF-3 | Required tokens in item 3 | `/plan` appears. `product repo` or equivalent ("a product repo", "your repo") appears. `/debug` appears as the broken-path alternative |
| VF-4 | Business rule | Cloud sync is documented, but not as Avery install finish. Search Cloud Agents section for `sync-user-skills.sh` after the move |
| VF-5 | Data | Dest path in the "Installed work-kit to" line still uses the existing `DEST` variable. This story does not change dest |
| VF-6 | Permission | Script does not request sudo. If dest is not writable, ER-1 |
| VF-7 | Secrets | Copy excludes `.env` as today. This story does not weaken excludes |

---

## 6. State management

| State | What it is | Pass if |
| --- | --- | --- |
| Initial | Repo on disk, plugin maybe absent or stale | Script can run |
| Transition | Copy runs, then echo | Echo only after successful copy (ER-1) |
| Final (this story) | Files on disk plus new copy in stdout/README | US-1 DoD. Plugin visibility is US-2 |
| Persistence | README and script in git | Change is committed. Next clone sees HP-5 |

No session cookie. No in-memory UI state. Log row (US-6) is not required to close US-1, but G2 is required to close 15 Oct.

---

## 7. UI/UX requirements

There is no Work Kit screen.

| ID | Requirement |
| --- | --- |
| UX-1 | Numbered list, 3 items, imperative, sentence case |
| UX-2 | `/plan` is readable without opening a 20-name inventory |
| UX-3 | No color-only meaning. No emoji in the three beats |
| UX-4 | README list readable on GitHub mobile (no table required for the three beats) |
| UX-5 | Straight quotes. No em dash in the three beats |
| UX-6 | Do not add a modal, toast, or first-run web page |

Accessibility: terminal and markdown. Skip WCAG on Customize. Contrast of GitHub.com is not ours.

---

## 8. Performance criteria

| ID | Requirement | Not this story |
| --- | --- | --- |
| PF-1 | Copy + echo completes without hanging. Typical: seconds to a couple of minutes on a laptop, bounded by dest size | E1 10 minutes clone-to-Customize is US-2 / O1 KR1 |
| PF-2 | No extra network call added to print next-steps | No telemetry |
| PF-3 | Throughput: one machine, one script run | No QPS target |
| PF-4 | Disk: dest copy as today, no second full copy to print help | No new dashboard DB |

If PF-1 regresses because someone shells out to a URL to "check latest copy," fail this story.

---

## 9. Integration criteria

| ID | Integration | Pass if |
| --- | --- | --- |
| IN-1 | Cursor Command Palette / Customize | Copy names them. No API. We do not automate Reload |
| IN-2 | GitHub README render | Numbered list renders as a list |
| IN-3 | `sync-user-skills.sh` | Still exists. Not deleted. Not item 3 of desktop next-steps |
| IN-4 | Cloud Agents Settings toggle | Documented in Cloud Agents section, not HP-4 |
| IN-5 | External APIs | None. No Mixpanel. No HTTP on install success |
| IN-6 | `install-work-kit` skill | See ED-6 |

---

## 10. Testing requirements

**Unit.** Optional: a small script or test that greps `install-local.sh` for the three required tokens in the echo block and asserts VF-2 forbidden strings are absent from that block. If added, keep it in-repo, no CI vendor required. If not added, VF-1 is a manual grep recorded in MT-1.

**Integration.** Run `./scripts/install-local.sh` on a dest you can overwrite. Confirm ER-1 by running with a broken dest or from a dir without `skills/` if easy. Do not symlink dest as a "test fix."

**E2E.** No browser suite. No Playwright. E2E for this story is MT-1.

**Manual (required).**

MT-1. From a checkout: run install, capture stdout, confirm HP-1 to HP-4. Open README in the working tree, confirm HP-5 and HP-6. `git grep` VF-2. Write pass/fail in session log notes.

MT-2. Read Cloud Agents section. Confirm sync instructions exist and are not desktop step 3.

MT-3 (optional, US-2). Reload, Customize, User, card visible. Not a US-1 fail if copy is right and Cursor is slow to show the card.

**Regression.** After US-1, any future README catalog dump as numbered step 3 is a G3 fail. Re-run VF-1 on that diff.

---

## Traceability

| Criterion | Story | Gate |
| --- | --- | --- |
| HP-1 to HP-6, VF-1 to VF-3 | US-1 | G3 |
| ER-1, ED-1 | US-1 / install script | G4 (no junk) adjacent |
| ED-4, IN-3, MT-2 | US-1 split lists | Protects US-7 |
| PF-1 vs 10 min | US-2 | O1 KR1 |
| Q10 copy-led `/plan` | Research F18 | After this ships |

Ready for development: edit the echo and the two README lists in one change, run MT-1, then `/review-diff`.
