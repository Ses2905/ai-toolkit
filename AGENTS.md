# AGENTS.md — how agents work in this repo

This repository is a **library of AI capabilities**, not an application. It holds
four kinds of things; put each new instruction at the right level (see
`LIBRARY.md` for the full model and `references/schemas/` for the templates):

- **Prompts** — one-off, input-driven tasks (`prompts/<domain>/`).
- **Skills** — persistent capabilities / quality bars that auto-activate (`skills/<name>/SKILL.md`).
- **Workflows** — ordered multi-step playbooks that compose skills + prompts (`workflows/<name>/`).
- **Global instructions** — repo-wide context that must not be duplicated inside every skill:
  - `AGENTS.md` (this file) — agent behavior + conventions
  - `DESIGN.md` — visual/design foundations
  - `CLAUDE.md` — tool entry points and commands

## Conventions

- **Naming:** directories and file ids are `lowercase-kebab-case`; keep the
  human title in front-matter / the `# Heading`.
- **One canonical home per rule.** Never copy a standard into multiple files —
  reference the canonical file (e.g. `See /DESIGN.md`) instead. Deduplicate
  aggressively.
- **Front-matter** on skills/prompts/workflows uses: `type`, `category`,
  optional `depends_on`, `references`. Skills also need a specific
  `description` (task type + trigger) so agents can decide when to use them.
- **Skills must be self-describing:** every `SKILL.md` needs *Activate When*,
  *Required Context*, *Process*, and *Definition of Done*.

## Editing rules

- Prefer editing an existing file over adding a near-duplicate. Before adding a
  skill, search for overlap (`tools/ai-lib/ai-lib search <topic>`).
- Regenerate derived artifacts after changes: the skills catalog
  (`./scripts/skills-db.sh build`) and the library index
  (`tools/ai-lib/ai-lib reindex`).
- Keep changes tightly scoped; do not restructure the library wholesale in a
  single change without a migration plan.

## Adding to the library

Use the installer/librarian so things land in the right place and stay indexed:

```bash
tools/ai-lib/ai-lib inspect <source>     # classify + preview routing
tools/ai-lib/ai-lib install <source> --dry-run
tools/ai-lib/ai-lib install <source> --yes
```

`<source>` can be a local folder, a `.zip`, a GitHub URL, a single `SKILL.md`,
or a prompt file. See `tools/ai-lib/README.md`.
