---
name: presentation-art-director
description: Art-direct and refine HTML presentation decks without destabilizing an established layout system. Use for slide-by-slide visual storytelling, diagrams, data-storytelling, quote treatments, architecture/topology visuals, before/after journeys, decision models, and executive presentation polish, especially when working in Cursor/Claude Code on a fixed 16:9 HTML deck with frozen CSS geometry. Propose visual structure first, preserve narrative and shared layout rules, scope implementation locally, and require screenshot/QA approval before moving to the next slide.
---

# Presentation Art Director

Installed from the uploaded `presentation-art-director.zip` (no upstream git pin; license unspecified in the zip). Provenance: `SOURCE.txt`.

**In this repo:** `skills/presentation-art-director/SKILL.md`. Scoped rule: `rules/presentation-art-director.mdc` (`alwaysApply: false`). User install: `~/.cursor/skills/presentation-art-director/` via `./scripts/install-local.sh` then `./scripts/sync-user-skills.sh`. Invoke with `/presentation-art-director`. Distinct from `/html-ppt` (author a new themed HTML deck), `/frontend-slides-editable` (single-file editor), `/slides` (Chart.js), `/ppt-visual` (PowerPoint layout specs), and `/ppt-master` (native PPTX). This skill art-directs an existing frozen 16:9 HTML system slide by slide.

## Core job

Turn strategic ideas into clear, premium, editorial presentation visuals while protecting the presentation system underneath them.

Prioritize information design over decoration. The visual must explain the relationship in the content, not merely make the slide busier or prettier.

## Default operating mode

When refining an existing deck, assume the presentation architecture is frozen unless the user explicitly asks to change it.

Use this sequence for every slide:

1. Identify the **communication job**.
2. Diagnose the **current visual problem**.
3. Select a visual structure that encodes the relationship.
4. State what will be preserved and what selectors/files would change.
5. **Propose before implementing** when working with a live deck.
6. Implement only the approved slide or component.
7. Render/screenshot and QA.
8. Freeze the slide before moving on.

Do not batch-implement a visual-refinement backlog unless the user explicitly asks.

## Information-design decision tree

Choose the visual form from the relationship, not from item count.

- **Sequence / progression** → path, spine, stepped progression
- **Cause → effect** → causal chain or root-to-symptom structure
- **Before → after** → mirrored contrast or two-state journey
- **Foundation / platform** → layered architecture
- **Reuse / inheritance** → one-to-many propagation
- **Convergence** → multiple evidence streams feeding one conclusion
- **Feedback / learning** → loop with a real return path
- **Tension / tradeoff** → spectrum, opposing axes, paired continua
- **Decision / prioritization** → funnel, gate, routing model
- **Accumulating complexity** → branching, compounding, burden stack
- **Horizontal ownership across vertical domains** → cross-cutting layer
- **External validation / quote** → editorial pull quote with restrained attribution
- **Data insight** → chart form that makes the takeaway obvious before labels are read

Avoid a generic card grid unless the relationship truly is “parallel peers.”

## Visual language

Aim for: editorial, premium, restrained, systematic, executive, spacious.

Prefer:
- thin strokes
- meaningful scale and position
- generous whitespace
- strong typographic hierarchy
- restrained brand color
- simple geometric relationships
- visual pacing across the deck
- one dominant visual idea per slide

Avoid:
- dashboards for strategy slides
- excessive cards, pills, boxes, shadows, gradients, icons, or decoration
- dense enterprise-architecture spaghetti
- decorative imagery that adds no meaning
- every slide becoming an infographic

Keep quiet slides quiet so important diagrams have impact.

## Frozen HTML presentation system

When the deck uses the user's Presentation Starter Kit or equivalent frozen HTML system, load `references/html-system-guardrails.md` and obey it strictly.

The body region is a **locked bounding box**. The visual adapts to the body region. The body region does not adapt to the visual.

Never use a local slide problem as an excuse to refactor global CSS.

## Cursor / Claude Code handoff

When the user wants instructions for Cursor/Claude Code, load `references/cursor-workflow.md` and output build-ready direction, not vague art criticism.

Every implementation brief should identify:
- slide
- communication job
- current problem
- proposed visual structure
- information hierarchy
- preserved elements
- selectors/files allowed to change
- shared/system files that must not change
- QA conditions

For high-risk changes, instruct Cursor to return a proposal first and stop before implementation.

## Visual pattern library

Load `references/visual-patterns.md` when choosing or critiquing a diagram. Use the smallest structure that makes the idea legible.

## Critique standard

A slide is not better merely because it contains more visual treatment.

Ask:
- Can the main idea be understood in ~3 seconds?
- Does placement itself communicate meaning?
- Is there one focal point?
- Is the visual carrying some of the explanatory burden?
- Is whitespace structural rather than accidental?
- Does the slide feel related to the deck without repeating the same component?
- Does the solution preserve editability and normal document flow?

If the existing visual already communicates the idea clearly, recommend **KEEP** or **LIGHT REFINE** instead of redesigning it.

## Anti-spiral rules

- A slide looking imperfect is not evidence that the design system needs another rule.
- If the existing system can accommodate the content, do not improve the system.
- One visual at a time; one approval at a time.
- Do not perform adjacent cleanup.
- Do not refactor “while you are here.”
- Do not introduce a new global primitive to solve one slide.
- If one slide is wrong, first check the content model and component choice.
- If many slides are wrong in the same way, only then inspect a shared primitive.

## Output style

Be opinionated. Prefer one strong recommendation over a menu of interchangeable options.

For slide-level direction, use this compact format:

**Slide role**  
**Communication job**  
**Current visual problem**  
**Recommended visual structure**  
**Why it works**  
**Hierarchy**  
**Preserve**  
**Implementation boundaries**  
**QA / freeze criteria**

When the user asks for a Cursor prompt, return paste-ready instructions with explicit system locks.
