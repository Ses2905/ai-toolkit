---
name: sort-skill-or-prompt
description: Classify reusable text as a Cursor prompt, skill, or rule. Use when the user is unsure where something belongs, worries they mixed skills and prompts, or asks to triage a dump before saving.
---

# Sort skill or prompt

Decide where a dump belongs. Do not save files unless the user then asks to add it.

Read `SKILL-VS-PROMPT.md` and apply this test to the pasted text.

## Test

Ask, in order:

1. **Would they paste this into a blank chat as the message?** → prompt (Prompt Kit `commands/`)
2. **Should the agent follow this whenever similar work appears, including tools or files?** → skill (Work Kit `skills/`)
3. **Is it one short constraint that should always apply?** → rule (user rules or Work Kit `rules/`)
4. **Is it repo-specific knowledge?** → that repo's `AGENTS.md` or `.cursor/skills`

If 1 and 2 both feel true, prefer **prompt** when it is one-shot template fill, and **skill** when it interviews, branches, or needs references/scripts.

## Output

```markdown
## Verdict
- **Kind:** prompt | skill | rule | repo-knowledge | skip
- **Library:** Prompt Kit | Work Kit | Cursor user rules | this repo
- **Suggested name:** kebab-case
- **Theme:** (prompts only) product | writing | research | strategy | engineering | personal

## Why
One short paragraph.

## If we add it
- Prompt → `commands/<name>.md` then `/new-prompt`
- Skill → Work Kit `skills/<name>/SKILL.md` then `/new-skill`
- Rule → say so; do not invent a prompt or skill
```

Do not relocate existing Work Kit skills in this pass. Classification only.
