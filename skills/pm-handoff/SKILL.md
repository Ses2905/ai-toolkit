---
name: pm-handoff
description: Compact the current conversation into a handoff document for another agent or session to pick up, with suggested skills and redacted sensitive data. Use when handing work to a fresh agent, ending a session, or writing a pickup brief. Upstream CLI name is `handoff`.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

# PM Handoff

Pinned from [mattpocock/skills `productivity/handoff`](https://github.com/mattpocock/skills/tree/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/skills/productivity/handoff) at `959a8e9f1edc3adbe2f7e3054bb6fbefa6696260` (MIT). Listing: [skills.sh](https://www.skills.sh/mattpocock/skills/handoff) · [AI UX Playground](https://aiuxplayground.com/skills/pm-handoff). Official CLI: `npx skills add github.com/mattpocock/skills/tree/main/skills/productivity/handoff --skill handoff` (upstream name is `handoff`; this repo installs it as `pm-handoff`). Provenance: `SOURCE.txt`.

**In this repo:** `skills/pm-handoff/SKILL.md`. Scoped rule: `rules/pm-handoff.mdc` (`alwaysApply: false`). User install: `~/.cursor/skills/pm-handoff/` via `./scripts/install-local.sh` then `./scripts/sync-user-skills.sh`. Invoke with `/pm-handoff`. Distinct from `/ship-the-change` (commit/push) and `/capture-a-skill` (save a workflow). Do not auto-invoke (`disable-model-invocation: true`).

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
