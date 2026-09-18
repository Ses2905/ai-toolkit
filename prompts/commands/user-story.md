---
name: user-story
description: Create user stories with Mike Cohn format and Gherkin acceptance criteria. Use when turning user needs into development-ready work with clear outcomes and testable conditions.
type: prompt
category: product
uses_skills:
  - user-story
---

# User story

## Use For
Turning a specific user need into a development-ready story with acceptance criteria.

## Prompt
Treat any text after the slash command as the input; if none was given, ask for it once.

Use the **user-story** skill (`skills/user-story/SKILL.md`) to produce this. Follow its process, decision rules, and definition of done — the skill is the single source of truth for the method (Mike Cohn + Gherkin, splitting, and pitfalls), so it is not restated here.

## Expected Output
A Mike Cohn user story ("As a / I want / so that") plus Gherkin acceptance criteria ("Given / When / Then"), split if it's too large.
