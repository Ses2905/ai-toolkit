---
name: add-to-library
description: Add a pasted prompt/skill/workflow to the library, routed correctly
---

Follow `skills/library-add/SKILL.md`. Ask for the pasted text if it is not in the
conversation, classify it (skill vs prompt vs workflow / reference / template),
then run `./scripts/library-add.py` so it lands in Work Kit (`skills/`) or Prompt
Kit (`prompts/`) correctly. Use `--dry-run` first to confirm the destination.
For installing a whole external repo, zip, or GitHub URL, use
`tools/ai-lib/ai-lib install <source>` instead.
