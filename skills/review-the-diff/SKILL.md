---
name: review-the-diff
description: Review uncommitted or branch changes for bugs, regressions, missing tests, and scope creep. Use when the user asks for a review, before merging, or after a sizable implementation.
---

# Review the diff

Review the actual diff, not the intention.

## Setup

- Use `git diff` / `git diff --staged` and `git status`. If reviewing a branch, diff against the merge base.
- Skim every changed file. Do not sample.

## Findings

Group findings by severity. Skip nitpicks unless they hide a real bug.

| Severity | Meaning |
| --- | --- |
| Blocker | Wrong behavior, data loss, security hole, broken build |
| Should fix | Likely bug, missing edge case, test gap for the change |
| Note | Clarity or maintainability; optional |

For each finding: file, what is wrong, why it matters, a concrete fix.

## Always check

- Does the change do what the user asked, and nothing extra?
- Error, empty, and loading paths if this is user-facing.
- Tests or a manual verification path for the new behavior.
- Secrets, authz, and untrusted input on any new boundary.

End with a verdict: **ship**, **fix blockers**, or **needs verification**.
