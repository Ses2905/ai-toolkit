# Library model

This repo is a composable library of AI capabilities. Put each instruction at
the level that matches its **behavior and lifecycle**, and give every rule
**one canonical home**.

| Level | What it is | Lives in | Ask |
| --- | --- | --- | --- |
| **Prompt** | One-off task; inputs change every run | `prompts/<domain>/` | "Is this a one-time instruction?" |
| **Skill** | Persistent capability / quality bar; auto-activates | `skills/<name>/SKILL.md` | "Reusable standard that should apply whenever relevant?" |
| **Workflow** | Ordered multi-step process; composes skills + prompts | `workflows/<name>/` | "Multi-step process with phases?" |
| **Global** | Repo-wide context | `AGENTS.md`, `DESIGN.md`, `CLAUDE.md` | "True across the whole repo?" |

Supporting tiers: `references/` (frameworks, patterns, examples, **schemas**),
`templates/` (reusable starting artifacts), `assets/` (media), `tools/`
(executables like `ai-lib` and the skills catalog).

## Choosing prompt vs skill vs workflow

- Inputs change every time, exploratory, or only occasionally useful → **prompt**.
- Same quality standard repeated, should apply automatically, stable trigger and
  definition of done → **skill**.
- Ordered phases, later steps depend on earlier outputs, review loops → **workflow**.
- True for nearly every task / universal convention → **global** (don't copy it
  into each skill; reference it).

## Deduplication rule

A standard has exactly one home. Example: typography/color/spacing live in
`DESIGN.md`; presentation and frontend skills *reference* it and add only their
context-specific application logic. Do not restate it.

## Composition

Skills are focused and composable — avoid "god skills." A workflow chains them:

```
Build Executive Deck workflow
  → research-synthesis (skill)
  → narrative (skill)
  → presentation-design (skill)  → references DESIGN.md
  → data-visualization (skill)
  → visual-qa (skill)
```

## Schemas

Author new items from `references/schemas/`:
`SKILL.template.md`, `PROMPT.template.md`, `WORKFLOW.template.md`.

## Adding / promoting items

Use the installer so things route correctly and stay indexed (see
`tools/ai-lib/README.md`):

```bash
tools/ai-lib/ai-lib install <folder | zip | github-url | SKILL.md | prompt.md> --dry-run
tools/ai-lib/ai-lib install <source> --yes
```

**Promotion** (planned `ai-lib promote`): when a prompt is reused often and its
trigger/process/definition-of-done stabilize, promote it to a skill; when it
grows ordered phases and review loops, promote it to a workflow — preserving
provenance.

## Catalogs

- Skills catalog (searchable/rankable): `skills-database.html` /
  `./scripts/skills-db.sh`.
- Whole-library index + provenance: `tools/ai-lib/ai-lib reindex` →
  `$AI_LIBRARY_HOME/INDEX.md` and `registry/packages.json`.
