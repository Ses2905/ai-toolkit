# Skill vs prompt

Two libraries on purpose. Mixing them is what made the skill list noisy.

## The split

| | **Prompt** (this kit) | **Skill** (Work Kit) |
| --- | --- | --- |
| What it is | The message you want to send | The playbook the agent follows |
| Loads when | You type `/name` | Named, or when the description matches the task |
| Context cost | None until you invoke it | Description sits in the skill list; easy to bloat |
| Shape | One markdown file in `commands/` | Folder with `SKILL.md` plus optional refs/scripts |
| Good for | A reusable ask, rewrite, critique, template fill | Multi-step workflow, tools, files, quality gates |
| Test | "I want the model to do *this* to *that input*." | "Whenever this kind of work comes up, work *this way*." |

Rules stay separate: short always-on constraints (Work Kit `rules/` or Cursor user rules).

## Route it

Put it in **Prompt Kit** when:

- You would paste it into ChatGPT, Claude.ai, or a blank Cursor chat
- It is one-shot: input in, artifact out
- You only want it when you ask for it
- Metadata looks like `intent`, `best_for`, `scenarios`, `estimated_time` and the body is "do this to my text"

Put it in **Work Kit** when:

- The agent needs steps, tools, scripts, or reference files
- It should fire without you remembering a slash command
- Quality depends on a repeatable procedure (plan, debug, review, ship, render slides)

Leave it as a **user rule** when it is a sentence-sized preference ("be concise", "don't invent metrics").

## After the 2026-09-18 triage

Moved to this kit (slash prompts):

- `/user-story`, `/press-release`, `/epic-hypothesis`
- `/problem-statement`, `/proto-persona`, `/jobs-to-be-done`

Kept in Work Kit as **slash-only skills** (workshops — they interview, then write):

- `workshop-facilitation`, `positioning-workshop`, `user-story-mapping-workshop`, `customer-journey-mapping-workshop`
- `discovery-interview-prep`, `problem-framing-canvas`, `opportunity-solution-tree`, `lean-ux-canvas`
- `prioritization-advisor`, `epic-breakdown-advisor`, `tam-sam-som-calculator`

Kept in Work Kit as auto skills: plan / debug / review / ship, design, motion, slides, installers, `product-strategy-session`.

Parked on disk, **not** installed into Cursor: Wondel downloads, designer-skill zips, Claude Code slash files, board-room pack. Add those here one at a time; do not dump them into `~/.cursor/skills`.
