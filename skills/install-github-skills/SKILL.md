---
name: install-github-skills
description: Install selected Agent Skills from a GitHub catalog such as spencerpauly/awesome-cursor-skills. Use when the user wants to pull skills from GitHub, an awesome-skills list, or copy SKILL.md folders into ~/.cursor/skills.
---

# Install skills from GitHub

Catalogs like [awesome-cursor-skills](https://github.com/spencerpauly/awesome-cursor-skills) are **lists**, not a plugin. Do not copy the whole repo into `~/.cursor/skills/`. Pick the skills that match the user's work.

Cursor does not auto-import loose GitHub skills. Either copy a `SKILL.md` folder, or package them in a plugin.

## Personal (every local project)

```bash
# one skill from a catalog repo
git clone --depth 1 https://github.com/spencerpauly/awesome-cursor-skills.git /tmp/awesome-cursor-skills
mkdir -p ~/.cursor/skills
cp -R /tmp/awesome-cursor-skills/resources/<skill-name> ~/.cursor/skills/<skill-name>
```

The folder name must contain `SKILL.md` and match the skill `name` frontmatter.

Then **Developer: Reload Window**. Confirm in **Customize → Skills**.

For Cloud Agents, skills must live in `~/.cursor/skills/` with **Settings → Agents → Sync Skills for Cloud Agents**.

## Project-only

Copy into that repo's `.cursor/skills/<skill-name>/` and commit it.

## Do not do this

- Dump every catalog skill into the user dir (context noise).
- Put skills in `~/.cursor/skills-cursor/` (Cursor-managed).
- Treat awesome-cursor-skills as a Cursor marketplace plugin.

## Impeccable is different

Frontend design skill: follow `skills/install-impeccable/SKILL.md` (`npx impeccable install`), not a copy from awesome-cursor-skills.
