---
name: plan-the-work
description: Turn a request into a scoped implementation plan before writing code. Use when the user asks to plan, the work has multiple approaches, scope is unclear, or before a non-trivial implementation.
---

# Plan the work

Do not start editing until the user has a plan they can accept or reject.

## Output

Write a short plan with:

1. **Goal** — one sentence
2. **Out of scope** — what you will not do
3. **Approach** — 3–7 concrete steps, named files/components when known
4. **Risks** — what could break
5. **First slice** — the smallest change that proves the approach
6. **Verify** — how you will know it works (command, UI path, or test)

## Rules

- Prefer the existing stack and files. Do not propose a new framework, database, or service unless the request needs it.
- If a decision is blocking (API shape, library, destructive migration), stop and ask. Otherwise pick a default and note it.
- If the request is already a tiny, obvious change, skip the long plan and say you are implementing it directly.
