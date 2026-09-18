# Prompt Kit

A companion Cursor plugin to **Work Kit** — a library of **one-off, input-driven
prompts** exposed as slash commands. Work Kit holds persistent *skills*
(capabilities/quality bars); Prompt Kit holds *prompts* (specific deliverables
whose inputs change every run). See the repo's [LIBRARY.md](../LIBRARY.md) for
the prompt-vs-skill model.

## Layout

```
prompts/
├── .cursor-plugin/plugin.json   # this is a separate plugin
├── commands/                    # slash-command prompts (product, research, …)
├── prompts/                     # fill-in templates + persona references
├── skills/                      # prompt-kit helper skills (capture-a-prompt, …)
├── scripts/install-local.sh     # install Prompt Kit at user scope
└── assets/
```

Prompt commands that overlap a Work Kit skill (e.g. `user-story`,
`press-release`, `epic-hypothesis`, `problem-statement`, `proto-persona`,
`jobs-to-be-done`) are thin **invokers** of the canonical skill — the method
lives once, in `skills/<name>/SKILL.md`.

## Install

```bash
./prompts/scripts/install-local.sh
```

## Add a new prompt

Use the single add-path from the repo root (routes skills → Work Kit, prompts →
Prompt Kit):

```bash
./scripts/library-add.py --file <notes.md>        # or --stdin / inline text
```

Or invoke `/add-to-library` in chat. Don't hand-grow a second library — let the
router place things correctly. For whole external repos/zips, use
`tools/ai-lib/ai-lib install <source>`.
