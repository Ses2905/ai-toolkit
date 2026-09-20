# Cursor / Claude Code visual-refinement workflow

Use this when handing a design direction to a coding agent.

## Master lock

Start visual-refinement prompts with the constraint that the presentation system is frozen. State which files are forbidden to edit and that the body region is a locked bounding box.

## Proposal gate

For any meaningful diagram change, require the agent to return only:

1. Slide
2. Communication job
3. Current visual problem
4. Proposed visual structure
5. Why the structure fits the content
6. Information hierarchy
7. Elements preserved
8. Selectors/files it would touch
9. System files/rules it will not touch

Then instruct it to STOP and wait for approval.

## Implementation gate

After approval, instruct it to implement only that slide/component.

Require locally scoped CSS, e.g. `[data-label="..."] .component-name` or an existing semantic slide/component class. Prefer a component class if the treatment will be intentionally reused across several slides.

Do not permit a new global component family unless the user explicitly approves system expansion.

## QA gate

After implementation require:

- header geometry unchanged
- body-region geometry unchanged
- rails unchanged
- 40px transition unchanged
- slide mode unchanged
- no overflow
- type sizes unchanged unless explicitly approved
- no shared layout CSS changed
- no unrelated slides changed
- screenshot rendered at the primary viewport

Then STOP.

Once approved, mark the slide `VISUAL-FROZEN` conceptually and instruct the agent not to revisit it unless explicitly reopened.

## Paste-ready skeleton

```
ENTER VISUAL REFINEMENT MODE.

The presentation architecture is FROZEN.
Treat the existing body region as a LOCKED BOUNDING BOX.
The visual adapts to the body region; the body region never adapts to the visual.

DO NOT MODIFY:
- layout-system.css
- presentation-system.css
- master rails/safe areas/transition
- slide header/body geometry
- Standard/Shallow/Dense assignment
- global typography or spacing tokens
- any unrelated slide

Allowed: locally scoped CSS/markup inside the named visual only.
No negative margins, shell transforms, font shrinking, or adjacent cleanup.

SLIDE: [name/number]
COMMUNICATION GOAL: [one sentence]
CURRENT PROBLEM: [specific visual issue]
VISUAL DIRECTION: [relationship + recommended visual structure]
PRESERVE: [copy/content/system elements]

BEFORE IMPLEMENTING return only:
- proposed structure
- hierarchy
- selectors/files to touch
- confirmation shared CSS will not change

STOP and wait for approval.
```
