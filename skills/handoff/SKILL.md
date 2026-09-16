---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

# Handoff (PM Handoff)

Pinned from [mattpocock/skills `handoff`](https://github.com/mattpocock/skills/tree/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/skills/productivity/handoff) at `959a8e9f1edc3adbe2f7e3054bb6fbefa6696260` (MIT). Listing: [skills.sh](https://www.skills.sh/mattpocock/skills/handoff) · [AI UX Playground PM Handoff](https://aiuxplayground.com/skills/pm-handoff). Official CLI: `npx skills add github.com/mattpocock/skills/tree/main/skills/productivity/handoff --skill handoff` (`--skill pm-handoff` is not a package name; the install name is `handoff`). Provenance: `SOURCE.txt`.

**In this repo:** `skills/handoff/SKILL.md`. Scoped rule: `rules/handoff.mdc` (`alwaysApply: false`). User install: `~/.cursor/skills/handoff/` via `./scripts/install-local.sh` then `./scripts/sync-user-skills.sh`. Invoke with `/handoff`. `disable-model-invocation: true` — do not auto-run. Distinct from `/capture-a-skill` (save a reusable workflow) and `/compact` (same-session compression). Write the document to the OS temp directory, not this workspace.

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
