---
name: find-a-skill
description: Search the Work Kit skills database, categorized and ranked
---

Help the user find the right Work Kit skill for their task.

1. Run `./scripts/skills-db.sh find <the user's terms>` to get ranked matches (score, category, invocation). Add `--category "<Category>"` to scope, or `--limit N` for more results.
2. If they want to browse instead of search, run `./scripts/skills-db.sh list` (categorized + ranked) or `./scripts/skills-db.sh stats`. For an interactive UI, run `./scripts/skills-db.sh serve` and open the printed URL — it has search, filters, sorting, and a Refresh button that rescans skills live.
3. Recommend the top match, say how to invoke it (its `/command` when present, otherwise it is model-invoked), and read that skill's `SKILL.md` before acting.

The database is generated from every skill under `skills/`. The served app's Refresh button (or `./scripts/skills-db.sh build`) regenerates the committed catalog (`SKILLS.md`, `skills-database.html`, `catalog/skills-index.json`) after you add or change skills.
