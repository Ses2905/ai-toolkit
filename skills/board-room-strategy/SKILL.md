---
name: board-room-strategy
argument-hint: "[strategy question or executive ask]"
description: Run the Board Room Strategy pack from a messy executive ask to a decision-ready board deck. Use when the user needs a governing question, issue tree, strategic options, recommendation, implementation plan, or slide storyline for a board or exec audience.
type: workflow
theme: strategy-positioning
best_for:
  - "Taking a broad executive ask to a board-ready recommendation deck"
  - "Running framing, diagnostics, choices, execution, and narrative in order"
  - "Invoking one stage of the pack without skipping the argument spine"
scenarios:
  - "The CEO wants a growth strategy deck for next month's board"
  - "Turn this messy exec ask into a governing question, options, and a recommendation"
  - "We have analysis; we need a storyline, action titles, and Q&A prep"
estimated_time: "1-2 weeks of analysis, one decision meeting"
---

Uploaded pack **25 Claude Skills to Build Boardroom Strategy Decks**. Provenance: `SOURCE.txt`. User install: `~/.cursor/skills/` via `./scripts/install-local.sh` then `./scripts/sync-user-skills.sh`. Invoke with `/board-room-strategy` or a sibling such as `/define-governing-question`. Distinct from `/product-strategy-session` (PM positioning → discovery → roadmap) and `/plan-the-work` (engineering implementation).

Do not skip stages to “save turns.” Anything in the invocation counts as answers already given — do not re-ask.

## Purpose

Take a strategy question all the way to a board-ready presentation: one governing question, complete analysis, a small set of real options, a committed recommendation, an execution plan, and a skimmable narrative.

This is not a product discovery workshop and not an engineering plan. It is the argument a board can approve.

## Input

**Works best with:** The raw executive ask, who is in the room, the decision date, and any numbers already believed.

**Also useful:** Current performance vs target, constraints (capital, talent, regulation), options already on the table, and prior board materials.

Anything supplied with the invocation — text after the skill name, a pasted brief, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers.

**Arriving empty-handed? That works too.** Start at framing and ask only for the decision, audience, and deadline.

**Example invocation:** `Board deck: should we enter the mid-market in FY27? CFO is skeptical, CHRO wants hiring freeze, decision in 3 weeks.`

## Stages

Run in order. Stop after the stage the user asked for. If they asked for the whole deck, complete every stage.

### 1. Framing the mandate

| Skill | When |
| --- | --- |
| `define-governing-question` | Convert the raw ask into one decision-forcing question |
| `audience-stakeholder-map` | Profile the board so the deck speaks to their priorities |
| `scqa-situation-frame` | Make the governing question feel inevitable |
| `working-hypothesis-answer` | State an answer-first hypothesis to confirm or kill |
| `storyline-skeleton-map` | Sequence one-line slide messages as the argument spine |

### 2. Diagnostics and evidence

| Skill | When |
| --- | --- |
| `issue-tree-decomposition` | MECE sub-questions so analysis is complete without overlap |
| `root-cause-driver-tree` | Map a headline metric to root causes and contribution |
| `quantify-the-gap` | Size current vs target and the value at stake |
| `benchmark-and-compare` | Position vs peers, history, or standards |
| `synthesize-so-whats` | Distill findings into the governing so-what |

### 3. Strategic choices

| Skill | When |
| --- | --- |
| `generate-strategic-options` | Distinct options including the status-quo baseline |
| `prioritization-matrix` | Score on the two most decision-relevant dimensions |
| `scenario-stress-test` | Test robustness under high-impact uncertainty |
| `tradeoff-analysis` | Make the sacrifices of the choice explicit |
| `recommendation-statement` | One committed recommendation, rationale, and ask |

### 4. Execution planning

| Skill | When |
| --- | --- |
| `implementation-roadmap` | Phased workstreams, milestones, dependencies, owners |
| `resource-and-investment-plan` | Cost, investment, return, phasing, payback |
| `risk-and-mitigation-register` | Likelihood, impact, mitigation, owner |
| `operating-model-and-owners` | Who decides, who delivers, governance cadence |
| `metrics-and-milestones` | Success metrics, leading indicators, checkpoints |

### 5. Narrative and communication

| Skill | When |
| --- | --- |
| `action-title-writing` | Assertive takeaway titles that read as the spine |
| `data-callout-design` | Make the one supporting figure unmissable |
| `executive-summary-slide` | One page a busy director can approve from |
| `visual-hierarchy-cleanup` | Layout so the eye hits the takeaway first |
| `objection-and-qa-prep` | Pre-empt the hardest board questions |

Each sibling lives at `../<name>/SKILL.md`. Follow that file's Instructions and Output when you reach its stage.

## Workflow

1. Restate the ask, audience, decision date, and what "done" means. Confirm or pick a governing question before analysis.
2. Run stage 1. Produce the governing question, audience map, SCQA, hypothesis, and storyline skeleton.
3. Run stage 2 only against the issue tree. Quantify. Do not generate options until the so-what is clear.
4. Run stage 3. Keep options mutually exclusive. Recommend one. Name what is given up.
5. Run stage 4 so the board can see path, cost, risk, owners, and metrics.
6. Run stage 5 last. Titles must match the skeleton. Build the exec summary from the recommendation statement.
7. Hand back a pack index: governing question, recommendation, ask, storyline titles, and which sibling artifacts were produced.

## Guardrails

- One governing question. If two decisions are hiding in the ask, split them; do not bury a second decision in appendix slides.
- Status quo is always an option. Do not present a single "the strategy" as if there were no alternative.
- Numbers need a source or an explicit assumption. Do not invent benchmarks, TAM, or payback.
- Distinct from `/product-strategy-session` (customer positioning and roadmap) and `/plan-the-work` (how to change code).
- Distinct from `/slides`, `/html-ppt`, and `/frontend-slides-editable` (how to render a deck). This pack decides **what the deck argues**. Use a presentation skill only if the user asked to build the actual slides.
- Do not skip Q&A prep when the audience is a board.

## Output

A stage-labeled packet. Minimum for a full run:

1. **Governing question** and out of scope
2. **Storyline skeleton** (action titles in order)
3. **Evidence so-whats** and value at stake
4. **Options considered** and the recommendation plus ask
5. **Roadmap, investment, risks, owners, metrics**
6. **Executive summary** and anticipated objections
