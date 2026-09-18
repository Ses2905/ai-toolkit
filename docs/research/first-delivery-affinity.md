# Affinity map: Work Kit first delivery (16 Sep 2026)

**Method used.** Expert product inspection plus one owner planning session. Not moderated interviews. Not usability. Not a diary study with other ICs.
**Sessions with participants.** 0 of 8 planned Avery-like ICs. Owner diary n=1 (Sarah Scherer). One Cloud Agent working session that inspected the repo. No recordings.
**Participant profile (planned, unfilled).** Solo IC who ships with git weekly and uses Cursor Agent or chat to change code. See [recruitment](first-delivery-recruitment.md).
**Raw paste.** The Playground brackets were empty. Stickies below are inspection notes from live files on 16 Sep, plus process notes from the planning chain. They are not interview quotes.
**Questions this map can answer.** What does install tell someone to do next? Can we count whether the loop ran? Did planning change stdout?
**Questions this map cannot answer.** Why other ICs skip `/plan`. Whether good copy produces `/plan` without a researcher. How often Teams hides the card. How often cloud runs miss skills.
**Related:** [Insights](first-delivery-insights.md), [Synthesis](first-delivery-synthesis.md), [Survey analysis](first-delivery-survey-analysis.md), [WK-1](../tickets/wk-1-g3-install-copy.md), [Feedback triage](first-delivery-feedback-triage.md)
**Source prompt:** [Affinity mapping assistant](https://aiuxplayground.com/prompts/affinity-mapping-assistant) (AI UX Playground)

Do not present this as "what testers said." Rewrite after 5 interview notes exist, or after G3 usability, whichever comes first. Do not mix owner rows into a fake n=8.

---

## Study context (filled)

| Field | Value |
| --- | --- |
| Research method | Heuristic product inspection of install copy, session log, and planning docs. Owner process observation. |
| Unit of analysis | Install surfaces (n=3), instruments (log, survey, interviews), owner session (n=1) |
| Testers | 0 completes |
| Key questions asked of the product | After a successful install, what is numbered step 3? Does any instrument have a complete? Did today's docs change the echo? |
| Decision this informs | Next sitting is WK-1 / G3 copy, not another research template |

---

## 1. Clean the data

### Kept (usable evidence)

Literal product text, file state, and counts. Each sticky has a source path.

### Removed as duplicates

Repeated restatements of "step 3 should be `/plan`" across launch docs. Kept one process sticky (N-P3). The rest are copies of the same owner intent, not new observations.

### Transcription

No audio. No typos to fix in tester speech. Script line 30 is quoted as printed, including the unicode arrow in items 1-2.

### Flagged too vague or not evidence (do not cluster as user findings)

| ID | Note | Why it is not evidence |
| --- | --- | --- |
| X1 | PR/FAQ composite Avery quote about getting a plugin card then starting in chat | Imaginary launch-day copy. Owner-authored. Not a participant. |
| X2 | "Users skip `/plan` because they are busy" | Hypothesis. 0 mentions. Copy never asked them to `/plan`. |
| X3 | "Chat wins minute one" as a usability finding | Desk competitive claim. We did not watch a tester choose chat. |
| X4 | "8 of 10 participants struggled with onboarding" | Invented n. Discard. |
| X5 | Blank session-log placeholder row with `who = Sarah` | Not a sitting. Do not code as `neither`. |
| X6 | Survey codebook themes written for 14 Oct | Empty cells. Not observations. |
| X7 | "The plugin is hard to find in Customize" | Unobserved. US-2. No empty-card screenshot this sitting. |

---

## 2. Code the data

Each observation: source, code (2-5 words), note. `P-owner` is Sarah. `T0` means testers.

| ID | Source | Code | Observation |
| --- | --- | --- | --- |
| N1 | `scripts/install-local.sh` L30 | Wrong finish line | Success echo item 3: `Optional for Cloud Agents: ./scripts/sync-user-skills.sh` |
| N2 | README clone numbered item 3 | Wrong finish line | Item 3 is Settings, Sync Skills for Cloud Agents |
| N3 | README checkout items 3-4 | Catalog as onboarding | Numbered steps dump skill names and slash catalogs, including Remotion |
| N4 | README clone bash block | Sync reads required | `./scripts/sync-user-skills.sh` runs immediately after install in the default clone commands |
| N5 | README opening job line | Stated job is plan | "plan first, debug from evidence, review the real diff, ship a clean commit" |
| N6 | README Cloud Agents section | Cloud documented elsewhere | Sync script plus Settings toggle already live under a Cloud Agents heading |
| N7 | `docs/okrs/session-log.md` | Empty denominator | Headers plus one blank placeholder. 0 filled `entry` or `ship` |
| N8 | Survey analysis 16 Sep | Survey not fielded | Completes 0. Invites 0. G3 block on fielding |
| N9 | Recruitment plan | Interviews unrun | Planned 5 to 8. Completes 0. No screener responses |
| N10 | `skills/plan-the-work` and slashes | Loop skills exist | `/plan` `/debug` `/review-diff` `/ship` are already in the plugin |
| N11 | `install-local.sh` dest copy | Install mechanics work | Copies a real directory to `~/.cursor/plugins/local/work-kit`. No symlink instruction |
| N12 | `skills/ship-the-change` | Ship refuses junk | Forbids `git add .` on unrelated files and `--no-verify` unless asked |
| N13 | P-owner 16 Sep session | Docs not echo | Playground chain filled. Line 30 unchanged |
| N14 | Priority / runbook / WK-1 | Spec already G3 | F1 ranked 5.0. G3 is a 15 Oct no-go bit. Ticket names the files |
| N15 | `skills/install-work-kit` item 3 | Skill copy drifted | Local plugin list item 3 is a catalog of skill names, same miss as README checkout |
| N16 | Architecture (known) | Cloud cannot see plugin | Cloud VMs do not mount `~/.cursor/plugins/local` |
| N17 | Messaging three beats | Canonical copy exists | Messaging already specifies Reload, Customize, product-repo `/plan` |
| N18 | P-owner hat objection | Owner may skip copy | Stakeholder readout names "I already know to `/plan`" as the operator objection |

---

## 3. Cluster into themes

Frequency uses two denominators. **Testers: 0 of 8.** **Surfaces / instruments / owner** as noted. Do not write "8 of 10."

### Theme A. Install copy names the wrong finish line

A person who follows numbered steps will stop at a plugin card, optional sync, or a catalog. They will not be told to `/plan`.

**Appeared across:** 3 of 3 desktop install surfaces (script, clone README, checkout README). Also `install-work-kit` skill (N15). Testers: 0 of 8.

**Stickies:** N1, N2, N3, N4, N15.

**So what.** The mental model the product teaches is "installed = done." That is the problem statement, produced by our next-steps.

### Theme B. Stated job and shipped next-steps contradict each other

The README already says plan first. Messaging already has the three beats. Numbered lists disagree.

**Appeared across:** 1 of 1 README (N5 vs N2/N3). Messaging vs script (N17 vs N1). Testers: 0 of 8.

**Stickies:** N5, N17, N1, N2, N3.

**So what.** This is not a missing strategy. It is drift between headline and instructions. Preserve the tension. Do not average them into "onboarding is unclear."

### Theme C. Desktop and cloud share one numbered list, so neither job is marked done

Optional sync as Avery step 3 is the wrong success for desktop. Optional is the wrong strength for Casey.

**Appeared across:** Copy (N1, N2, N4) plus architecture (N16). Cloud Agents section already splits the job correctly (N6). Testers: 0 of 8. Casey sessions watched: 0.

**Stickies:** N1, N2, N4, N6, N16.

**So what.** Cloud is not undocumented. It is duplicated into the wrong list. Avery is told a step that is not first delivery.

### Theme D. The 80% loop target has no denominator

We cannot tell if sittings plan, tiny-skip, debug, or skip to chat.

**Appeared across:** 0 of 1 operators have a completed log row. Survey 0. Interviews 0.

**Stickies:** N7, N8, N9, X5 (flagged, not counted as a sitting).

**So what.** Empty instruments hide skip-to-chat the same way a plugin card hides it. They are not a theme from skippers. They are a missing count.

### Theme E. Planning volume is up. Executable copy is unchanged.

The owner already named F1 / G3 as rank 1 and did not edit the echo.

**Appeared across:** 1 of 1 owner sessions this day (N13, N14). Testers: n/a.

**Stickies:** N13, N14, N17.

**So what.** Extra affinity maps do not change what the next installer reads. Time on templates competes with two files: script and README.

### Theme F. Unique loop skills exist and are undiscoverable after install

`/plan` and `/ship` are real. First-run IA does not point at them.

**Appeared across:** Skills present (N10, N12, N11) vs install lists (N1-N3). Testers: 0 of 8.

**Stickies:** N10, N11, N12, N1, N3.

**So what.** Do not recommend "build the loop." Recommend "point numbered step 3 at the loop that already exists."

### Theme G. The skipper hypothesis is still a recruitment plan

We do not know how other Cursor ICs start agent sessions after they install skills.

**Appeared across:** 0 of 8 planned participants. Owner self-study excluded from that n.

**Stickies:** N9, N8, N18.

**So what.** Treat skippers in the wild as untested. Do not delay F1 to wait for n=5. Run problem interviews in leftover hours. Usability only after G3.

---

## 4. Contradictions and outliers

Preserve these. Do not smooth.

**Headline vs list (Theme B).** Same README file says plan first and then numbers cloud sync or a catalog as step 3. Segment: clone visitor vs owner who wrote the headline.

**Cloud is documented and misplaced (Theme C).** N6 contradicts any sticky that would say "we forgot cloud." We remembered cloud in the wrong slot.

**Owner already knows `/plan` vs copy is for clone visitors (N18 vs Theme A).** If Sarah already types `/plan`, Theme A still holds for anyone who follows the list. Do not use the owner as proof that copy is fine. Do not use the owner as proof that copy is unused. Log has no row either way (Theme D).

**Install works vs first delivery fails (N11 vs Theme A).** Dest copy succeeding is not an outlier failure. It is why G3 can fail while G4-adjacent junk is quiet. Success of rsync is not success of the sitting.

**Survey and interviews are empty on purpose vs empty by neglect.** Survey is blocked until G3 (correct). Interviews can run before G3 and have not. Do not merge those zeros into one "research failed" theme.

**Outlier we do not have.** A tester who followed step 3 and still `/plan`. Sample is 0.

---

## 5. Rank by frequency and severity

Severity = blocks 15 Oct first delivery or O1 measurement. Frequency = how many independent sources show it, not a fake user %.

| Rank | Theme | Frequency | Severity | Why this rank |
| --- | --- | --- | --- | --- |
| 1 | A. Wrong finish line | 3/3 install surfaces plus skill | Blocking. 15 Oct G3 no-go | Highest surface count and it teaches the skip |
| 2 | B. Headline vs steps | 1 README plus messaging vs script | Blocking. Same files Avery reads | Same defect as A, called out so we do not "add more explanation" |
| 3 | E. Docs not echo | 1/1 owner session, many artifacts | High process severity. Competes with F1 hours | Does not change stdout until someone edits |
| 4 | F. Skills exist, undiscoverable | Skills Y, install N | High. Wrong fix would be "build more skills" | Protects against C7 |
| 5 | C. One list, two jobs | Copy + architecture. Casey n=0 | High for Avery now. Casey is 14 Nov | Misplaced, not missing |
| 6 | D. Empty log | 0 rows | Blocking for O1 KR2, not for G3 copy | Measure after F1. Do not wait on Mixpanel |
| 7 | G. Skippers untested | 0/8 testers | Medium for 15 Oct. High if we treat hypothesis as fact | Leftover hours only |

---

## 6. Unexpected findings

1. **Specification is not shipped UX.** The surprising cluster is Theme E sitting on top of Theme A: every planning artifact already requires `/plan` as step 3, and stdout still does not. The product team (Sarah) is unlikely to be surprised by "copy is wrong" and more likely to be surprised that more reports did not count as the fix.

2. **Cloud is not the missing section.** Unexpected relative to a naive "add cloud onboarding" brief. Theme C: the Cloud Agents section is already right enough. The miss is Avery's third beat.

3. **Empty n is a finding, not a delay.** Theme D and G. Teams often wait for research to start copy. Here the inspectable product is enough for F1, and fielding survey now would measure the old echo.

4. **Catalog IA leaked into E1.** Theme A via N3/N15. Checkout install reads like a shopping list. That challenges "we need more discoverability of skills."

5. **The loop is not missing.** Theme F. Challenges "Work Kit is incomplete, so do not launch copy yet."

---

## Readout lead (surprise theme)

Theme E is the paragraph to open with if the audience is the owner wearing a PM hat. Theme A is the paragraph to open with if the audience is a clone visitor.

**E, one paragraph.** On 16 Sep we produced user flows, OKRs, a survey, insights, a Jira-ready ticket, and positioning, all of which say first delivery starts at `/plan`. The installer still reads optional cloud sync or a slash catalog. The surprise is not a new user quote. It is that research-shaped artifacts can pile up while the two files a person follows stay still. If this affinity map is used as a reason to delay editing `install-local.sh`, it has failed its own Theme E.

**A, one paragraph.** After a successful desktop install, numbered step 3 is not `/plan` on any of the three surfaces we inspected. Script: optional cloud sync. Clone README: Cloud Agents toggle. Checkout README: catalog of names. A diligent new installer who does what they are told will not start first delivery. We have not watched eight people do this. We read the instructions they would get.

---

## What not to do with this map

- Do not put X1 in a quote slide.
- Do not report Theme G as "users skip planning."
- Do not start interviews as a gate on WK-1.
- Do not run this prompt again until there are transcripts or G3 usability notes.
- Next product work is still the copy edit in [WK-1](../tickets/wk-1-g3-install-copy.md).
