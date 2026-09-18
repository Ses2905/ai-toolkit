# ai-lib — installer + librarian for the AI library

A package manager for AI capabilities. Point it at a source and it inspects,
classifies, routes, installs, indexes, and tracks provenance — so you never have
to manually download repos, guess prompt-vs-skill, rename folders, or update
indexes by hand.

```bash
# put it on PATH (optional)
ln -s "$PWD/tools/ai-lib/ai-lib" ~/.local/bin/ai-lib

ai-lib inspect <source>              # classify + show the routing plan
ai-lib install <source> --dry-run    # preview, change nothing
ai-lib install <source> --yes        # apply the plan
ai-lib list [type] [--category X]
ai-lib search <query>
ai-lib info <id>
ai-lib remove <id> [--purge]
ai-lib doctor                        # validate the library
ai-lib reindex                       # regenerate INDEX.md
```

`<source>` can be a **local folder**, a **`.zip`**, a **GitHub URL**, a single
**`SKILL.md`**, or a **prompt file**.

## Where things go

The canonical library is `$AI_LIBRARY_HOME` (default `~/.ai-library`), or pass
`--home <path>`:

```
$AI_LIBRARY_HOME/
├── skills/       prompts/     workflows/
├── references/   templates/   assets/
├── tools/        integrations/ global/
├── inbox/        # low-confidence items land here (needs_review)
└── registry/packages.json     # machine-readable index + provenance
```

## How it classifies

Content first, filename second (a manifest `ai-library.yaml` wins if present):

- **skill** — a directory with `SKILL.md`, or a doc with *Activate When* / *Definition of Done*
- **prompt** — *Use For* / *Prompt* / `[INPUT ...]`
- **workflow** — ordered *Steps* / *Step 1…*
- **asset** — media/font/pdf; **tool** — `.py/.js/.sh/…`
- **global** — `AGENTS.md` / `DESIGN.md` / `CLAUDE.md` / `README.md`
- **reference** — supporting knowledge (fallback)

Domain **category** comes from a keyword taxonomy (presentation, design,
data-visualization, research, strategy, product, frontend, …). Low confidence →
`inbox/` marked `needs_review` rather than inventing a category.

## Safety

Conservative by default: inspect → classify → show plan → flag conflicts →
require `--yes`. `--dry-run` changes nothing. Overlap with an existing item
(same name or similar description) blocks a plain install; re-run with `--yes`
to proceed. Every install records provenance (GitHub url+commit, or original
path) in the registry so items can be found, updated, or removed later.

## Status

V1: local/zip/GitHub install, classification, routing plan, registry +
provenance, duplicate detection, dry-run, doctor, index regeneration, list /
search / info / remove. V2 (planned): agent adapters (`sync cursor|claude|codex`),
upstream `update`, semantic dedupe, prompt `promote`, project `.ai-library.yaml`.

Tests: `python3 tools/ai-lib/ai_lib_test.py`.
