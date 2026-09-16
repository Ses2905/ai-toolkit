# Work Kit OKRs, Q4 2026

**Product:** Work Kit (`work-kit`), personal Cursor plugin
**Period:** 1 October 2026 through 31 December 2026
**Owner:** Sarah Scherer
**Primary user:** Avery (solo IC on desktop Cursor). Riley (Teams) and Casey (Cloud Agents) are recovery paths, not the happy path, until O2 is graded.
**Source prompt:** [OKR and goal setting](https://aiuxplayground.com/prompts/okr-goal-setting) (AI UX Playground)
**Related:** [First-delivery user flow](../user-flows/work-kit-first-delivery.md), [Feature priority](q4-2026-feature-priority.md), [SMART goals](q4-2026-smart-goals.md)

This is a one-person kit, not a billed product. Key results are about install, first delivery, and reuse. They are not ARR, NPS, or market share.

---

## 1. Context setting

### Team or product area

Work Kit installs once at user scope and supplies the Plan, Debug, Review, Ship, Capture loop across every Cursor project. Public home is [Ses2905/cursor-skills](https://github.com/Ses2905/cursor-skills). Current plugin version in `.cursor-plugin/plugin.json` is 1.20.0.

### Time period

Q4 2026. Weekly check-ins. Monthly deep dives. Grade on 31 December 2026.

### Strategic priorities from leadership

The README states the job. Plan first. Debug from evidence. Review the real diff. Ship a clean commit. Save repeated workflows as skills. Do not copy kit files into each application repo.

Those priorities set the outcome for the quarter. A session that followed the loop and left a verified commit on a branch is success. Files existing under `~/.cursor/plugins/local/work-kit` is not.

### Previous quarter review

Q3 2026 has no instrumented product analytics. Repo history is the review.

What worked:

- The kit stayed a user-scope plugin. `scripts/install-local.sh` copies a real directory. It does not symlink the checkout.
- Core skills stayed small and named for the job: `plan-the-work`, `debug-from-evidence`, `review-the-diff`, `ship-the-change`, `capture-a-skill`, `install-work-kit`.
- Catalog growth stayed scoped. Animation, slides, and Remotion skills shipped with dedicated rules so they do not fire on unrelated work.

What did not:

- First value is still "plugin visible in Customize," not "first `/plan` accepted and `/ship` landed." The first-delivery flow was written in mid-September. It has not been timed on a clean machine.
- Cloud Agents cannot see `~/.cursor/plugins/local`. Casey still depends on `scripts/sync-user-skills.sh` plus a Settings toggle. That path is easy to skip.
- There is no log of sessions that skipped `/plan` and edited anyway. The plan gate is a skill rule with no count behind it.

### Current challenges or opportunities

Challenges:

- Teams/Enterprise can block local plugin imports. Riley's path fails after a "successful" script.
- `npx skills add` can install SKILL.md files without plugin slash commands.
- Unrelated dirty files make `git add .` dangerous. `/ship` must keep staging named paths.

Opportunities:

- The first-delivery flow names entry points E1 through E7, decisions D1 through D8, and empty states. Q4 can turn that map into timed drills and a short checklist.
- Cloud sync is already a script. Making it part of install, not an optional footnote, would close the Casey gap.
- Capture-a-skill is the distribution loop for a personal kit. Repeated chat instructions that become SKILL.md files are the retention signal Uri Levine would call "they came back."

---

## 2. OKR framework overview

**Objective.** A qualitative goal for the quarter. Aspirational, aligned with the README job, ambitious enough that 1.0 is rare, short enough to remember.

**Key results.** Quantitative outcomes, not tasks. Time-bound to 31 December 2026. Three to five per objective. Written so a 0.7 (about 70% confidence at kickoff) is a real stretch.

Rules used here:

- One outcome per KR. "Run a workshop" is an initiative. "Eight of ten logged sessions start with an accepted plan" is a KR.
- Unknown baselines stay unknown. Inventing DAU would fake a SaaS scoreboard this kit does not have.
- Segment first. Avery is the fit to protect. Riley and Casey get one objective, not four.

Google-style grading is in section 10. 0.7 is success. 1.0 means the KR was too easy or the quarter went unusually well.

---

## 3. Team objectives

### Objective 1. Make first delivery the default path

A new or returning Avery who installs Work Kit this quarter completes one Plan to Ship loop in a real product repo, not only a plugin copy on disk.

Why this matters. The user flow's aha moment is `/plan` waiting for accept. If install succeeds and the loop never runs, the kit did not do its job.

How it ladders. Directly implements "plan first, ship a clean commit" from the README.

Owner. Sarah Scherer.

Key results:

- KR1. On a clean user-scope install (E1 or E2), time from clone to Work Kit visible under Customize, User, after Reload Window, is 10 minutes or less. Timed twice (macOS or Linux, recorded). Baseline: untimed.
- KR2. Of logged Work Kit coding sessions in the owner's product repos this quarter, at least 80% either start with an accepted `/plan` or are marked "tiny skip" in the session note. Baseline: untracked. Start the log in week 1.
- KR3. At least 8 sessions this quarter end in `/ship` with a pushed commit that staged named files only (no `git add .` when the tree had unrelated files). Count from git history plus the session log.

### Objective 2. Give Cloud Agents the same loop as desktop

Casey can start a Cloud Agent that loads plan, debug, review, ship, and capture without copying the plugin into the target repo.

Why this matters. Cloud VMs do not mount `~/.cursor/plugins/local`. Skipping E7 makes the kit silently absent.

How it ladders. "Reuse the skills there" is already in `install-work-kit`. Q4 makes that path required for cloud work, not optional.

Owner. Sarah Scherer.

Key results:

- KR1. After `./scripts/sync-user-skills.sh`, all five core skill folders exist under `~/.cursor/skills/` (`plan-the-work`, `debug-from-evidence`, `review-the-diff`, `ship-the-change`, `capture-a-skill`). Verified by a script that exits non-zero on a miss. Baseline: manual copy, no check.
- KR2. Sync Skills for Cloud Agents is on, and at least 6 Cloud Agent runs this quarter load `plan-the-work` or `debug-from-evidence` from the synced library (run notes or agent transcripts). Baseline: unknown.
- KR3. README Cloud Agents section includes the failure mode "plugin card missing, skills still required" and a pass/fail checklist. A stranger following only that section completes sync on a second machine or VM.

### Objective 3. Stop shipping secrets, junk, and unverified diffs

`/review-diff` and `/ship` catch the failure modes already named in the user flow: empty diff, `.env`, hook failure, review of intention instead of `git diff`.

Why this matters. A kit that plans well and then `git add .` a secrets file has failed the last mile.

How it ladders. `ship-the-change` and `review-the-diff` plus `verify-before-done`.

Owner. Sarah Scherer.

Key results:

- KR1. A local fixture (10 dirty trees: `.env`, unrelated markdown, empty diff, hook-fail simulation, mixed staged/unstaged) shows `/ship` instructions would stage only intended paths in 10 of 10 cases. Automate what can be asserted in git. The rest is a scored dry-run against the skill text. Baseline: 0 fixtures.
- KR2. Every PR or branch the owner opens with Work Kit this quarter has a `review-the-diff` verdict in the session note or PR body: ship, fix blockers, or needs verification. Target: 100% of branches that get a `/ship`. Baseline: not required today.
- KR3. Zero commits from the owner's Work Kit `/ship` path this quarter contain `.env`, credentials, or `*.log` files listed in `.gitignore`. Audit with `git log` and `git show --stat`. Baseline: assume zero until a miss is found.

### Objective 4. Turn repeated instructions into skills that survive reload

Chat memory stops at the session. SKILL.md files in this repo, reinstalled with `install-local.sh`, are the retention mechanism.

Why this matters. Measuring PMF for a personal kit is "would I be very disappointed if this workflow vanished." Capture is how a workflow stays.

How it ladders. `capture-a-skill` and the README rule that durable workflow lives in files.

Owner. Sarah Scherer.

Key results:

- KR1. At least 4 workflows that appeared in 3 or more sessions this quarter are written as `skills/<name>/SKILL.md` with valid frontmatter (`name` matches folder) and reinstalled. Baseline: catalog already large. Count only new captures from Q4 repetition, not imports of third-party catalogs.
- KR2. After every kit skill add this quarter, `./scripts/install-local.sh` is run before the next coding session. Misses logged. Target: 90% of skill-add commits followed by a reinstall in the same day.
- KR3. Sean Ellis, personal. End of quarter, for the core loop only: "If `/plan`, `/debug`, `/review-diff`, `/ship` disappeared, I would be very disappointed." Grade 1.0 if yes, 0.0 if no. Somewhat disappointed is 0.3. This is a single-respondent survey. Treat it as a leading indicator, not a team NPS.

---

## 4. Sample objectives by focus area

These are not extra OKRs. They are the pool that produced section 3. Do not stack them on top of O1 to O4.

**Growth (distribution, not vanity installs).**

- Get the documented E1 path to a visible plugin without a Slack thread of recovery.
- Make Cloud Agent sync a counted path so the kit shows up where desktop plugins cannot.

**Product.**

- Keep first-slice planning the default for non-tiny work.
- Keep `/ship` staging named files when the working tree is dirty.

**User experience.**

- Empty Customize after a "successful" script should name Teams policy or forgotten reload, not a blank card.
- `/debug` with no failure should ask expected vs actual, not guess.

**Operational.**

- Log sessions so KRs have a denominator.
- Grade monthly so a failed KR is visible in November, not on 31 December.

---

## 5. Key result examples (Work Kit metric menu)

Use these if a KR in section 3 needs a substitute. Keep them outcomes.

**Adoption and engagement**

- Share of logged sessions that invoke `/plan` or `/debug` before the first edit.
- Count of `/ship` pushes this quarter.
- Count of Cloud Agent runs that loaded a synced core skill.

**Quality and performance**

- Minutes from clone to Work Kit visible (KR1 of O1).
- Fixture pass rate for dirty-tree shipping (KR1 of O3).
- Core skill folders present after sync (KR1 of O2).

**Business impact (personal kit)**

- Repeated workflows captured as skills (KR1 of O4).
- Branches with an explicit review verdict (KR2 of O3).
- Do not use ARR, paid conversion, or TAM. There is no revenue line.

**Satisfaction**

- End-of-quarter disappointment question on the core loop (KR3 of O4).
- Count of install recoveries (symlink dest, Teams block, skipped reload). Down is better. Baseline starts at first logged recovery.

---

## 6. Supporting initiatives

### O1. First delivery default

| Initiative | Description | Expected KR impact | Owner | Timeline |
| --- | --- | --- | --- | --- |
| Clean-machine drill | Time E1 twice. Record blockers. Patch README and `install-work-kit` where the clock dies. | O1 KR1 | Sarah | October |
| Session log | One markdown row per coding session: date, repo, plan/tiny/debug, ship yes/no, notes. | O1 KR2, KR3 | Sarah | Week 1, then ongoing |
| Slash habit in Cursor | Pin `/plan`, `/debug`, `/review-diff`, `/ship` in the command palette muscle memory. No product change required. | O1 KR2 | Sarah | October |
| Tiny-skip rule reminder | If the request is already tiny, write "tiny skip" in the log instead of a fake six-section plan. | O1 KR2 (honest denominator) | Sarah | October |

### O2. Cloud loop

| Initiative | Description | Expected KR impact | Owner | Timeline |
| --- | --- | --- | --- | --- |
| Sync checker script | After `sync-user-skills.sh`, assert the five core folders exist. Fail the script if not. | O2 KR1 | Sarah | October |
| Install path change | README and `install-work-kit`: if you use Cloud Agents, sync is step 3, not optional. | O2 KR2, KR3 | Sarah | October |
| Six cloud runs | Schedule Cloud Agent work that needs planning or debugging. Note which skills loaded. | O2 KR2 | Sarah | November to December |
| Stranger checklist | One page Casey path with pass/fail boxes. Run it on a second environment. | O2 KR3 | Sarah | November |

### O3. Safe ship

| Initiative | Description | Expected KR impact | Owner | Timeline |
| --- | --- | --- | --- | --- |
| Dirty-tree fixtures | Ten synthetic git states plus expected stage set. | O3 KR1 | Sarah | October |
| Verdict footer | After `/review-diff`, paste ship / fix blockers / needs verification into the session note or PR. | O3 KR2 | Sarah | Ongoing |
| Ship audit | Monthly `git log` scan for `.env` and ignored junk. | O3 KR3 | Sarah | Monthly |
| Hook failure drill | Trigger a failing pre-commit once. Confirm the skill forbids `--no-verify` unless asked. | O3 KR1 | Sarah | November |

### O4. Capture

| Initiative | Description | Expected KR impact | Owner | Timeline |
| --- | --- | --- | --- | --- |
| Repeat detector | In the session log, tag a workflow the third time it appears. That row becomes a capture candidate. | O4 KR1 | Sarah | Ongoing |
| Reinstall same day | After a skill-add commit, run `install-local.sh` before the next session. | O4 KR2 | Sarah | Ongoing |
| Disappointment check | 31 December, answer KR3 in writing in this file's grading section. | O4 KR3 | Sarah | 31 December |

---

## 7. Measurement plan

| KR | How to track | Data source | Cadence | Tool | Baseline |
| --- | --- | --- | --- | --- | --- |
| O1 KR1 | Stopwatch on a clean install | Written time in session log | Twice in Q4 | Session log + README | Untimed |
| O1 KR2 | Session log fraction | `docs/okrs/session-log.md` (create week 1) | Weekly | Markdown table | Untracked |
| O1 KR3 | Count `/ship` rows that match `git log` | Session log + git | Weekly | git | Count Q3 by hand if needed |
| O2 KR1 | Script exit code | `scripts/sync-user-skills.sh` plus new checker | Each sync | Shell | No checker |
| O2 KR2 | Cloud run notes | Cursor Cloud run list / transcripts | Weekly | Cursor dashboard | Unknown |
| O2 KR3 | Second-environment dry run | Checklist in README | Once | README | Section exists, no checklist |
| O3 KR1 | Fixture runner or scored dry-run | New test dir or script | After each ship-skill edit | git + script | 0 fixtures |
| O3 KR2 | PR/session footer | GitHub PRs + session log | Each branch | GitHub | Not required |
| O3 KR3 | `git log -p` / `--stat` audit | git | Monthly | git | Assume 0 |
| O4 KR1 | New `skills/*/SKILL.md` from Q4 repeats | git log on `skills/` | Monthly | git | Catalog size is not the baseline |
| O4 KR2 | Skill-add commit date vs install-local run date | Session log | Each skill add | Session log | Unknown |
| O4 KR3 | Written answer | This file, section 10 | 31 December | This file | Not asked yet |

Dashboard. A single markdown table in `docs/okrs/session-log.md` plus this file. No Mixpanel. No Stripe.

Reporting. Weekly: fill the log. Monthly: score each KR 0.0 to 1.0 as a forecast. Quarter end: final grade.

---

## 8. Dependencies and risks

What needs to happen:

- Cursor still loads user-scope local plugins from `~/.cursor/plugins/local/`.
- Cloud skill sync still reads `~/.cursor/skills/` when the setting is on.
- The owner keeps the session log. Without it, O1 KR2 has no denominator.

Dependencies:

- Cursor product behavior (Customize, Cloud Agents, Sync Skills). Not owned by this repo.
- Teams admin, if Riley's path is attempted: Allow Local Plugin Imports.
- GitHub availability for clone and `npx skills add`.

Blockers and mitigation:

| Blocker | Mitigation |
| --- | --- |
| Teams blocks local plugins | Fall back to E3 plus `~/.cursor/skills`. Grade O1 KR1 on the fallback and note the policy. |
| Cloud sync setting ignored | O2 KR1 script fails closed. Do not start cloud runs until it passes. |
| Session log abandoned | Monthly deep dive treats missing rows as 0 for O1 KR2 that week. Do not impute. |
| Fixture work slips | Keep O3 KR3 (secrets audit) even if KR1 fixtures are late. Last-mile safety still grades. |
| Catalog sprawl (installing every playground skill) | O4 KR1 counts only workflows repeated in real sessions. Playground installs are not captures. |
| Cursor changes plugin paths | Re-read `install-work-kit` in November. Adjust scripts before the December grade. |

---

## 9. Review cadence

### Weekly (15 minutes, owner only)

Format:

1. Count sessions this week. Plan / tiny skip / debug / neither.
2. Any `/ship`? Named files only?
3. Cloud run this week? Skills loaded?
4. Blockers. One line.

Who. Sarah. No audience.

### Monthly (45 minutes)

Deep dive. Forecast each KR 0.0 to 1.0. Kill or replace a KR only if the metric was wrong, not because the number is low. Update initiatives.

Who. Sarah. Optional: paste the score table into a GitHub issue on `cursor-skills` for a paper trail.

### Quarterly (grading, first week of January 2027)

Retrospective. Final 0.0 to 1.0 per KR. Average per objective. Reflection questions in section 10. Draft Q1 2027 OKRs from misses, not from a blank template.

Who. Sarah. If a teammate uses the kit by then, invite them for the grade only, not for weekly.

---

## 10. Grading and reflection

Scale is 0.0 to 1.0 per KR. Average the KRs for the objective. Do not weight.

| Score | Meaning |
| --- | --- |
| 0.0 | No progress, or the outcome did not happen. |
| 0.3 | Learning or partial movement. Example: session log exists but `/plan` rate is 40% against an 80% KR. |
| 0.7 | Stretch hit. This is the intended success. Example: 8 of 10 sessions planned. Install timed at 11 minutes against a 10 minute KR (close, not a 1.0). |
| 1.0 | Fully hit or exceeded. If several KRs are 1.0, the next quarter's KRs should be harder. |

End-of-quarter questions:

1. Which KR moved because the kit changed, and which moved because I remembered to type `/plan`?
2. Did Cloud Agents actually load synced skills, or did I only run the sync script?
3. Would I be very disappointed if the core loop vanished? Write the O4 KR3 answer here.
4. What did we install from catalogs that never got a third session? Stop syncing those.
5. What is the single outcome for Q1 2027? One sentence, then build the next tree from that.

How learnings inform next quarter:

- If O1 KR2 is low, the problem is habit or the tiny-skip rule, not another marketplace plugin.
- If O2 KR2 is low, do not add catalog skills. Fix sync and the Settings toggle.
- If O4 KR1 is high but O1 is low, we captured trivia and skipped first delivery. Reverse that.

---

## Opportunity snapshot (for discovery, not extra OKRs)

Desired outcome. Raise the share of logged sessions that finish Plan to Ship.

Customer opportunities (owner as Avery):

- I install the plugin and still start coding in chat with no plan.
- I use Cloud Agents and the kit is invisible.
- I ship with a dirty tree and do not trust staging.

Solutions stay out of the KR list until an experiment runs. First experiments: session log (O1), sync checker (O2), dirty-tree fixtures (O3).

---

## Next build checklist

1. Create `docs/okrs/session-log.md` in week 1 (columns: date, repo, plan/tiny/debug/neither, ship, cloud, notes).
2. Time one E1 install. Write the minutes next to O1 KR1.
3. Add a post-sync folder check to the cloud path.
4. Write the ten dirty-tree fixtures for `/ship`.
5. Start the repeat-workflow tag in the session log so O4 has candidates before December.
