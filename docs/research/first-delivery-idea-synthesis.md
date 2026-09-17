# Idea synthesis: Work Kit first delivery (17 Sep 2026)

**Problem.** Install can succeed while the next sitting starts in chat with no plan. Live step 3 still teaches optional cloud sync. We need one concept for how first delivery actually happens, not a pile of adjacent jobs.
**Source.** Not a brainstorm, hackathon, or workshop with testers. Ideas are competing paths already in the repo: live install copy, [scope](../launches/q4-2026-first-delivery-scope.md) in/out, [feature priority](../okrs/q4-2026-feature-priority.md) F1-F18, adjacent jobs C1-C7, hat objections, Playground fills (C7). **Paste was empty.**
**Constraints.** One owner. $0. MIT. Cursor chrome not owned. Cloud VMs do not mount local plugins. G3 red today. 8 Oct SLC, 15 Oct go-live or slip, 14 Nov cloud, 31 Dec grade. Interviews 0. Log 0.
**Related:** [Priority](../okrs/q4-2026-feature-priority.md), [Positioning](../messaging/work-kit-positioning.md), [Tenets](../messaging/work-kit-tenets.md), [WK-1](../tickets/wk-1-g3-install-copy.md), [Feedback triage](first-delivery-feedback-triage.md)
**Source prompt:** [Idea synthesis](https://aiuxplayground.com/prompts/idea-synthesis-framework) (AI UX Playground)

This is not user research. Do not present concepts as "the team voted." Next sitting is still WK-1, not a concept-test sprint.

---

## 1. Theme identification

**Theme 1. Routing.** How does a sitting start after install? Candidates: `/plan` as item 3, default chat (C1), catalog list (C3), optional cloud sync (live).

**Theme 2. Proof.** How do we know the loop ran? Candidates: session log, Customize-visible, skill-folder count, interviews, Mixpanel (cut).

**Theme 3. Distribution.** How does the kit spread? Candidates: README + echo (owned), Marketplace, `npx skills add`, copy-into-repo, paid pilots (refused), Playground template volume (C7).

**Theme 4. Runtime.** Where does the loop load? Desktop plugin (Avery now), synced skills on a VM (Casey, 14 Nov), Teams card (Riley, recovery).

**Patterns.** Every failed path treats "kit present" as success. Every serious path needs a named start (`plan` / `tiny` / `debug`) and a named-file `/ship`. Paper (docs, this file) keeps clustering as if it were a product.

**Outlier worth keeping.** Honest **tiny skip** (F4). Not a separate product. A rule inside the logged loop so one-line work does not fake a six-section plan.

**Outlier to discard as a concept.** "More planning templates." That is C7, the trap this sitting is in.

---

## 2. Synthesized concepts

### Concept A. Three-beat echo

**One sentence.** After install, numbered step 3 is `/plan` (or `/debug` if broken) on the script echo and both README lists.

**Components.** Reload, Customize User, `/plan`. Cloud sync under Cloud Agents only. Catalogs out of the numbered list. WK-1 / F1 / G3.

**Solves.** Clone visitors follow stdout. Today they follow optional sync or a catalog. Skills already exist; routing does not.

**User value.** Stranger (and cold-clone Sarah) is told the job. Avery who already `/plan`s is unhurt. Use: E1/E2 install, then first chat in a product repo.

**Feasibility.** Complexity low. One sitting, under 2 hours. Depends on owning the echo (we do). Risk: owner skips because "I already know."

**Differentiation.** Chat implements first. Lists shop. Continual Learning remembers. This concept only claims plan-then-named-ship, and only if copy says so. Not new technology. New finish line.

**Recommended now.** Yes. Only 15 Oct gate that is still red.

### Concept B. Logged loop

**One sentence.** Every product-repo sitting is a log row: `plan` / `tiny` / `debug` / `neither`, then named-file `/ship`.

**Components.** Session log, plan-or-tiny 80%, 8 named-file ships, tiny-skip honesty, review verdict, secrets P0.

**Solves.** "Installed = done" has no counter. Empty log hides skip the same way a plugin card does.

**User value.** Avery can see whether the week was the loop. Q4 can be graded. Use: day-1 go-live row, then weekly sittings.

**Feasibility.** Complexity low (markdown). Value is rows, not the header. Depends on G3 so the row is not `neither` by instruction. Risk: n=1 looks like 100%.

**Differentiation.** Not DAU. Not Customize-visible. Counts sittings we can audit in git.

**Recommended.** Yes, after A. Same quarter. Not instead of A.

### Concept C. Cloud-first installer

**One sentence.** Avery's third beat is sync / Cloud Agents, because VMs cannot see `~/.cursor/plugins/local`.

**Components.** Live line 30. Settings toggle. Sync script. (Later: checker, six runs, Casey README.)

**Solves.** Casey's missing skills. **Does not solve** desktop first delivery. It is how G3 failed.

**User value.** Casey, after 14 Nov, with a checker. Harmful for Avery and clone visitors if it stays item 3.

**Feasibility.** Sync script exists (low). Checker is medium, dated 14 Nov. Risk: dashboard greens "cloud mentioned" and G3 together.

**Differentiation.** Unique constraint (VMs). Unique failure when used as the happy-path finish line.

**Recommended.** As Avery install: no. As phase 2 (checker + Casey README + six runs): yes, after 14 Nov, off Avery's numbered list.

### Concept D. Catalog onboarding

**One sentence.** Numbered install dumps skill names, slashes, Remotion, so people see what they got.

**Components.** Checkout README items 3-4 today. `install-work-kit` skill item 3 drift. C3 lists, C7 Playground dumps.

**Solves.** "What is in the kit?" **Does not solve** first delivery. Trains shopping.

**User value.** Catalog shoppers. Wrong ICP.

**Feasibility.** Already shipped (too easy). Risk: looks like launch content.

**Differentiation.** Indistinguishable from GitHub skill lists and `npx skills add`.

**Recommended.** No this quarter. Optional non-numbered "also in the kit" heading after G3.

### Concept E. Research-first, then copy

**One sentence.** Interview 5-8 ICs and field a survey, then write step 3 from what they say.

**Components.** Recruitment, beta survey, synthesis. F17 can run before G3. F18 must not.

**Solves.** Fear of wrong words. **Does not solve** a skippable step 3 while copy never asks for `/plan`.

**User value.** Future skipper hypothesis. Zero current respondents.

**Feasibility.** Effort medium. Blocked ethically: talking to people about a skippable step wastes their hour. Risk: C7 in PM clothing.

**Differentiation.** None until G3. Empty instruments stay empty.

**Recommended.** Leftover hours after A. Survey only after G3. Do not delay WK-1.

### Concept F. Chrome, Marketplace, paid path

**One sentence.** First-run UI, Marketplace listing, or paid design partners make first delivery feel like a real product.

**Components.** Modal we cannot ship. Listing. MSA/LOI (already refused).

**Solves.** Status anxiety ("is this big enough?"). **Does not solve** stdout.

**User value.** Imaginary buyers. Not Avery.

**Feasibility.** Chrome: high and not owned. Paid path: refused. Timeline: never this quarter.

**Differentiation.** Would make Work Kit look like every other listing. Unique job would still be untaught.

**Recommended.** No. Cut.

---

## 3. Comparison

| Concept | User value | Feasibility | Uniqueness | Recommended |
| --- | --- | --- | --- | --- |
| A. Three-beat echo | High for clone visitors | Low effort, this sitting | Routing, not a new command | **Now** |
| B. Logged loop | High for Q4 grade | Low, needs A so rows are not `neither` by copy | Sittings, not DAU | **After A** |
| C. Cloud-first as Avery step 3 | High for Casey, harmful for Avery | Script exists; wrong job | VM constraint | **No as item 3.** Phase 2 dated |
| D. Catalog onboarding | High for shoppers, wrong job | Already live | None vs C3 | **No** |
| E. Research-first | None while n=0 | Medium, stalls A | None | **After A only** |
| F. Chrome / Marketplace / paid | None we can ship | High or refused | Status, not the loop | **Cut** |

Tiny skip rides inside B. Do not score it as a seventh product.

---

## 4. Recommendations

**Move forward (3)**

1. **A. Three-beat echo.** Only live miss that blocks 15 Oct. P=5.0 in the priority matrix. Do it this sitting.
2. **B. Logged loop.** Denominator for the north star. Day-1 row on go-live or slip.
3. **C as phase 2, not as item 3.** Checker + Casey README + six runs after 14 Nov.

**Explore later**

- Non-numbered catalog heading after G3 (from D, stripped of install numbers).
- Interviews leftover, survey after G3 (from E).
- Dirty-tree fixtures and capture-from-repeats after B has rows.

**Deprioritize / cut**

- D as numbered onboarding.
- E before copy.
- F entirely this quarter.
- C as Avery step 3 (live bug, not a concept to "try").
- Another synthesis or Playground fill as a seventh concept.

Why A over E: US-1 already has the words. Why B over D: we need a count, not a list. Why not F: we do not own chrome and we refused paid pilots.

---

## 5. Next steps

**Validation before building A.** None. Open the file. The echo is the experiment.

**Quick experiments.** The copy sitting is the experiment (30 min). After it: `sed -n '25,31p' scripts/install-local.sh`. After go-live: one log row. Do not A/B catalog vs `/plan` in chrome we cannot ship.

**Questions to answer after A, not before.** Does the new item 3 produce `/plan` without a researcher? (Survey after G3.) How long is E1? (Time twice.) Does Casey still miss skills? (Checker, 14 Nov.)

**Who to involve next.** Sarah, in the editor. Not testers. Not Cursor. Not a workshop.

If this synthesis produces a concept-test plan instead of a patch, it failed. Item 3 is `/plan`.
