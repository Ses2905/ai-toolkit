---
name: debug-from-evidence
description: Debug by reproducing the failure and gathering evidence before changing code. Use when something is broken, a test fails, a bug is reported, or the user asks why something does not work.
---

# Debug from evidence

Do not guess-and-patch. Reproduce first, then change one cause.

## Workflow

1. **Restate the failure** in one sentence: expected vs actual.
2. **Reproduce** with the smallest command, test, or UI path. Save the exact output.
3. **Locate** the first frame, log, or assertion that is wrong. Read that code; do not spray logs everywhere.
4. **Form one hypothesis.** Name what you would observe if it is true.
5. **Fix the cause**, not a symptom. Keep the diff small.
6. **Re-run the original reproduction.** Also check one nearby path that should still work.
7. **Report** the root cause, the fix, and the evidence. If you cannot reproduce, say so and stop proposing speculative edits.

## Guardrails

- If reproduction fails, gather more evidence. Do not "try a likely fix."
- Revert failed experiments instead of stacking them.
- Prefer a failing test that captures the bug when the project already has a test runner.
