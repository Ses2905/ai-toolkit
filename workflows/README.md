# Workflows

Ordered, multi-step playbooks that **compose** skills and prompts (see
[LIBRARY.md](../LIBRARY.md)). Each workflow lives in `workflows/<name>/` with a
`WORKFLOW.md` authored from [`references/schemas/WORKFLOW.template.md`](../references/schemas/WORKFLOW.template.md).

A workflow should define its goal, trigger, ordered steps (each naming the skill
or prompt it uses), review gates, and a definition of done — and **refer to**
skills/prompts rather than duplicating them.
