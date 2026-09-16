# WK-1. Install next-steps name `/plan` as step 3

**Type:** Story (copy only)
**Priority:** Highest. Blocks G3. 15 Oct is no-go until this lands.
**Assignee:** Sarah Scherer (eng, copy, QA)
**Reporter:** Sarah Scherer. Product inspection 16 Sep 2026.
**Due:** Next coding sitting. Hard gate 8 Oct 2026 SLC.
**Estimate:** Under 2 hours. One change. No dest rewrite.
**Epic:** First delivery. Plan to Ship as the default path.
**IDs:** US-1, F1, G3, SMART A.
**Status:** Open. Live product still fails.
**Source prompt:** [Rewrite JIRA tickets](https://aiuxplayground.com/prompts/rewrite-jira-tickets-clarity) (AI UX Playground)

Paste this into Jira if you ever stand up a board. Until then this file is the ticket. There is no Jira project, no Linear, no designer queue.

---

## Original ticket (what we started from)

There was no filled Jira card. The implicit ask was:

> Fix install copy. Make README and the script match. Step 3 should be plan.

That is not assignable. It does not name files, the forbidden string, or how to test. This rewrite is that card, using live product text as the bug report.

**Live fail (16 Sep, still true until this ships):**

- `scripts/install-local.sh` line 30: `Optional for Cloud Agents: ./scripts/sync-user-skills.sh`
- README clone numbered item 3: Settings, Sync Skills for Cloud Agents
- README checkout numbered items 3 to 4: skill-name catalog, then a second slash catalog including Remotion
- Clone bash block runs `./scripts/sync-user-skills.sh` immediately after install, which reads as required desktop finish

---

## 1. Improved ticket structure

**Title.** WK-1. After a successful desktop install, next-steps tell Avery to `/plan` (or `/debug` if broken). Cloud sync is not step 3.

**Summary for the board.** Copy change in `install-local.sh` and two README install lists. Three numbered beats. Same order. Same meaning. No new UI.

**Who it is for.** Avery, desktop IC, follows numbered lists. Clone visitors on GitHub see the same list. Casey (Cloud Agents) is not this ticket's step 3.

**Who does the work.** Sarah. Designer and developer are the same person. "Designer" here means the author of the three beats. There is no Figma file to wait on.

---

## 2. Context

**Background.** Work Kit is a once-per-machine Cursor plugin. Success is an accepted plan and a named-file commit, not a plugin card. Install already copies a real directory to `~/.cursor/plugins/local/work-kit`. The loop skills already exist (`/plan`, `/debug`, `/review-diff`, `/ship`). Clone visitors never reach them if step 3 names something else.

**Why now.** G3 is a 15 Oct go/no-go bit. Planning docs (stories, AC, messaging, stakeholder readout) already specify the three beats. Stdout does not. Specification is not shipped UX. Default chat wins minute one if step 3 is vague.

**User / business.** O1: 80% plan-or-tiny and 8 named-file ships this quarter. Without this copy, every new clone learns skip. Cost is $0. ROI is not a field on this ticket. Impact is every future install.

**Related work.**

| Doc | Role |
| --- | --- |
| [US-1 AC](../user-flows/us-1-g3-acceptance-criteria.md) | Pass/fail table. Do not invent extra AC. |
| [US-1 story](../user-flows/work-kit-first-delivery-stories.md) | Persona and so-that |
| [Messaging](../messaging/work-kit.md) section 3 | Canonical three beats |
| [Scope](../launches/q4-2026-first-delivery-scope.md) F1 | In freeze. Not a Playground template. |
| [Runbook](../launches/q4-2026-first-delivery-runbook.md) G3 | Launch no-go if this is still yellow |
| [Stakeholder readout](../launches/q4-2026-stakeholder-presentation.md) | CTA is this ticket |

**Dependencies.** None besides git and a machine that can run `./scripts/install-local.sh`. Cursor is already installed for MT-3 (optional).

**Does not depend on.** Interviews. Survey. Session log row. Sync checker (US-7). Timed E1 (US-2). Marketplace.

**Design system.** There is no component library. The system is: numbered list, three items, imperative, sentence case, straight quotes, no emoji in the beats. GitHub markdown numbered lists plus bash `echo` lines. README must stay readable on GitHub mobile. Skip WCAG on Cursor Customize. Contrast of GitHub.com is not ours.

---

## 3. Requirements

### What needs to be done

Edit, in one change:

1. `scripts/install-local.sh` success echo after a successful copy (the `Next:` block only).
2. README section "Install from GitHub (desktop skill library)" numbered list, and prefer moving `./scripts/sync-user-skills.sh` out of the default clone bash block into Cloud Agents (ED-4).
3. README section "Install from this directory" numbered list. Remove catalog dump as numbered steps 3 and 4.

Target meaning (match [messaging](../messaging/work-kit.md); punctuation may use the existing `→` if README matches):

1. Command Palette, Developer: Reload Window
2. Customize, filter User, confirm Work Kit
3. Open a product repo and run `/plan` (or `/debug` if something is already broken)

### Acceptance criteria (testable)

Full table lives in [US-1 AC](../user-flows/us-1-g3-acceptance-criteria.md). Ship gate for this ticket:

- HP-1: success stdout has `Next:` then exactly three numbered items, no item 4 in that list.
- HP-2: item 1 is Reload Window via Command Palette / Developer.
- HP-3: item 2 is Customize, filter User, confirm Work Kit.
- HP-4: item 3 names a product repo and `/plan`, with `/debug` if already broken. It does not say optional cloud sync. It does not only repeat "confirm Work Kit".
- HP-5: README clone numbered list matches HP-2 to HP-4, same order.
- HP-6: README checkout numbered list matches HP-2 to HP-4. No fourth numbered beat that is a catalog dump.
- VF-2: `git grep -n "Optional for Cloud Agents"` on `scripts/install-local.sh` returns no matches. Numbered item 3 must not contain `Sync Skills for Cloud Agents`, `/install-impeccable`, or `remotion`.
- VF-3: item 3 contains `/plan`, a product-repo phrase, and `/debug`.
- VF-4: `sync-user-skills.sh` still exists. Cloud Agents section still documents sync and the Settings toggle.
- ER-1: non-zero script exit does not print the success `Next:` list.
- ED-1: reinstall over existing dest prints the same three beats. Dest stays a real directory, not a symlink to the checkout.

### Design requirements

- Three numbered lines. Short. Imperative. Sentence case.
- `/plan` readable without opening a 20-name inventory (UX-2).
- No color-only meaning. No emoji in the three beats (UX-3).
- Tiny-change hint, if any, is prose after the list, not numbered step 4 (ED-2).
- `npx skills add` paragraph may stay as an alternate. It is not numbered step 3 of plugin install (ED-3).
- Teams note may stay near install. It must not replace step 3 (ED-5).
- No modal, toast, or first-run web page (UX-6).

### Technical requirements

- Copy-only. Dest path stays `${HOME}/.cursor/plugins/local/work-kit`.
- Do not add `ln -s`. Cursor ignores a symlink into the checkout.
- Do not change rsync/tar excludes. Do not weaken `.env` exclude.
- Do not add a network call to "check latest copy".
- Do not request sudo.
- Echo the `Next:` block only after successful copy (`set -e` already covers ER-1 if you do not print Next before copy).
- Do not delete `scripts/sync-user-skills.sh`.

---

## 4. Action items

Owner is Sarah on every row.

| # | Task | Deliverable | Depends on |
| --- | --- | --- | --- |
| 1 | Read US-1 AC HP/VF/ER rows | Nothing to commit | None |
| 2 | Change `install-local.sh` line 30 to the `/plan` beat | New stdout | 1 |
| 3 | Rewrite both README numbered install lists to the same three beats | README diff | 2, same sitting |
| 4 | Move clone-block `sync-user-skills.sh` into Cloud Agents (preferred) or add a sentence that it is not desktop finish | README clone section | 3 |
| 5 | Run `./scripts/install-local.sh`, capture stdout (MT-1) | Notes in session log | 2 |
| 6 | `git grep` VF-2. Diff script echo vs two README lists (VF-1) | Pass/fail in log | 3, 5 |
| 7 | Read Cloud Agents section (MT-2) | Confirm sync still documented | 4 |
| 8 | `/review-diff` on this change only. No secrets. No `.agents/` dump | Review verdict | 2-4 |
| 9 | Optional same sitting: align `skills/install-work-kit/SKILL.md` next-steps (ED-6) | Skill diff or a WK-1b follow-up | 3 |
| 10 | Mark US-1 done only after HP-1 to HP-6 pass | Status on this ticket | 5-8 |

**Blockers.** None on people or APIs. The only blocker is doing another Playground template instead of this patch. Do not wait on interviews (F17 leftover hours). Do not field the beta survey until G3 is green (F18).

**Out of this sitting.** US-2 timed Customize. US-5 ship secrets audit. US-6 log habit. US-7 checker. First-run UI. Dest path change.

---

## 5. Design specifications

**Design files.** None. Do not open Figma. Do not commission a plugin card mock. The card is Cursor Customize, which we do not restyle.

**Source of copy.** [Messaging](../messaging/work-kit.md) section 3, README / homepage next-steps. Treat that as the locked string set. If script and README drift after this ticket, G3 fails again.

**Components to use.**

| Surface | Component | Notes |
| --- | --- | --- |
| Terminal | `echo` lines under `Next:` | Three items. Indent as today. |
| GitHub README | Markdown ordered list | Renders as 1. 2. 3. on mobile. |
| Alternate | Fenced bash | Clone commands. Sync is not the numbered finish. |

**States and variants.**

| State | What the user sees |
| --- | --- |
| Success | `Installed work-kit to ${DEST}` then `Next:` and three beats |
| Failure (missing `skills/`, dest not writable, rsync/tar fail) | Native shell error. No success Next list |
| Reinstall (E2) | Same three beats as first install |
| Casey / Cloud | Same desktop three beats on install. Sync lives under Cloud Agents |
| `npx skills add` only | Skills without plugin slashes. Must not claim `/plan` exists without the plugin |

**Responsive.** README list must work in a GitHub mobile browser. No table required for the three beats. Terminal wrap is acceptable. Do not put the three beats in a screenshot-only image.

**Visual QA.** Side-by-side before/after of the three beats is the review artifact. Not a year gantt. Not a fake funnel.

---

## 6. Technical notes

**Constraints.** Bash. `set -euo pipefail`. rsync if present, else tar. Excludes `.git`, `agent-tools`, `.DS_Store`. MIT. One owner. User-scope dest only.

**Integration points.**

- Cursor Command Palette: named in copy. No API. We do not automate Reload.
- Customize, User filter: named in copy. Visibility after reload is US-2, not a fail of this ticket if copy is right (MT-3 optional).
- `scripts/sync-user-skills.sh`: keep. Relocate instructions, do not delete.
- Cloud Agents Settings toggle: Cloud Agents section only.
- External APIs: none. No Mixpanel. No HTTP on install success.

**API requirements.** None.

**Testing.**

- No Playwright. No browser suite.
- Unit optional: grep the echo block for `/plan` and assert VF-2 strings are absent. In-repo only if you add it. Not a CI vendor.
- Integration: run the script on a dest you can overwrite. Optional ER-1: run from a dir without `skills/` or a dest you cannot write. Do not "fix" a test by symlinking dest.
- Required manual: MT-1 (stdout + README lists + grep). MT-2 (Cloud Agents section still has sync).
- Regression: any future README catalog dump as numbered step 3 is a G3 fail. Re-run VF-1 on that diff.

**Security.** `/review-diff` before push. Do not stage `.env`, `.agents/`, or `skills-lock.json` unless you explicitly decide to. This ticket's diff should be copy files plus optional `install-work-kit` skill.

---

## 7. Resources and references

| Kind | Link |
| --- | --- |
| Canonical copy | [docs/messaging/work-kit.md](../messaging/work-kit.md) |
| AC | [docs/user-flows/us-1-g3-acceptance-criteria.md](../user-flows/us-1-g3-acceptance-criteria.md) |
| Story | [docs/user-flows/work-kit-first-delivery-stories.md](../user-flows/work-kit-first-delivery-stories.md) US-1 |
| Scope freeze | [docs/launches/q4-2026-first-delivery-scope.md](../launches/q4-2026-first-delivery-scope.md) F1 |
| Runbook gate | [docs/launches/q4-2026-first-delivery-runbook.md](../launches/q4-2026-first-delivery-runbook.md) G3 |
| Competitive why | [docs/messaging/work-kit-competitive-ux.md](../messaging/work-kit-competitive-ux.md) chat wins minute one |
| Live script | `scripts/install-local.sh` lines 25-30 |
| Live README | `README.md` clone list items 1-3, checkout list items 1-4, Cloud Agents section |
| Skill drift (P2) | `skills/install-work-kit/SKILL.md` local plugin numbered list item 3 |
| Inspiration | Do not copy a SaaS onboarding modal. Copy a three-line man page. |

Related tickets (local IDs, not Jira keys):

- WK-1 (this). G3 copy.
- WK-1b. Align `install-work-kit` if skipped here. P2. Not a G3 fail unless it is the only path a user sees.
- US-2. Customize visible. After copy.
- US-7. Casey checker. 14 Nov. Must not become desktop step 3.

---

## 8. Definition of done

**Complete when all of these are true:**

1. HP-1 to HP-6 pass on a machine that can run the script.
2. A reviewer diffs script echo vs the two README numbered lists and finds the same three beats, same order, same meaning.
3. `git grep -n "Optional for Cloud Agents"` on `scripts/install-local.sh` returns no matches.
4. Checkout README numbered install list does not include `/install-impeccable` or Remotion names as the third beat.
5. `/review-diff` run on the copy change. No secrets. This ticket marked done.
6. MT-1 recorded in `docs/okrs/session-log.md` notes (pass/fail). A header-only log with no MT-1 note is not DoD for the test, even if the echo is right.

**Deliver.** A git commit that changes the echo and the two README lists (and optionally `install-work-kit`). Not a new PDF. Not a slide. Not a survey.

**How to verify.**

```bash
./scripts/install-local.sh
sed -n '25,31p' scripts/install-local.sh
git grep -n "Optional for Cloud Agents" scripts/install-local.sh
```

Read README clone and checkout numbered lists. Confirm item 3 is `/plan`. Confirm Cloud Agents still documents sync.

**Handoff.** There is no receiving team. After merge, the next sitting is a product-repo `/plan` then `/ship` (US-3/US-5) and a log row (US-6). Do not hand to research. Do not open WK-2 as "more templates."

**Not done.** Docs that describe G3 while the echo is unchanged. This ticket file existing is not G3.

---

## Jira field cheat sheet (if you paste this)

| Field | Value |
| --- | --- |
| Project | Personal Work Kit. No Jira site required |
| Issue type | Story |
| Priority | Highest |
| Labels | first-delivery, copy, g3, us-1, f1 |
| Sprint | Next sitting, before 8 Oct 2026 |
| Story points | Skip. Use wall clock: under 2 hours |
| Assignee | Sarah Scherer |
| Reporter | Sarah Scherer |
| Linked | Blocks 15 Oct go-live. Blocked by nothing |
| Environment | Desktop Cursor. Owner OS. Terminal plus GitHub README |

Ready to assign means: open the two files and edit. Do not wait for a kickoff.
