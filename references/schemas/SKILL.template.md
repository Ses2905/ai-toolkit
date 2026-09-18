---
type: skill
category: <one of the library categories>
depends_on: []          # other skills this composes with
references:              # canonical files — do not duplicate their content
  - ../../DESIGN.md
description: >-
  <task type + trigger + core capability>. e.g. "Use when creating, redesigning,
  or reviewing presentation slides. Applies editorial layout, hierarchy,
  whitespace, and typography. Do not use for general webpage UI."
---

# <Skill Name>

## Purpose
The reusable capability or quality standard this skill provides.

## Activate When
Explicit, specific trigger conditions (an agent must be able to decide relevance).

## Do Not Activate When
Cases to skip (one-off tasks, unrelated work, explicit bypass requests).

## Required Context
What to inspect before acting (e.g. `DESIGN.md`, the component library, source data).

## Operating Principles
The durable quality bar — rules that stay true across tasks, not one project's facts.

## Process
The default, reusable sequence the skill follows.

## Decision Rules
Conditional logic. `IF <condition> THEN <action>.`

## Output Requirements
What the skill produces.

## Definition of Done
Checklist that determines completion.

## References
Point to shared repo files instead of duplicating them (e.g. `See /DESIGN.md`).
