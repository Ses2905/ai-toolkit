---
name: ship-the-change
description: Prepare a clean commit and push with a precise message. Use when the user asks to commit, push, ship, wrap up, or land the work.
---

# Ship the change

## Before git

1. `git status` and `git diff`. Confirm the diff matches the request.
2. Run the lightest verification that covers the change (test, typecheck, or the UI path).
3. Do not commit secrets, `.env`, or generated junk. Do not use `git add .` if unrelated files are present.

## Commit

- Stage only the intended files.
- Message format: imperative, specific, ~50–72 character subject. Body only if the why is not obvious.
- Example: `Fix empty-state copy on the billing invoices table`
- Do not include `Co-authored-by` or AI trailer lines unless the repo already uses them.

## Push

- Push the current branch with `-u` if it has no upstream.
- Do not create a pull request unless the user asked for one.
- If hooks or the push fail, fix the cause; do not `--no-verify` unless the user explicitly wants that.
