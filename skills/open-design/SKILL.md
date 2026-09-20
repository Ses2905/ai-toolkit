---
name: install-open-design
description: Installs Open Design from GitHub Releases and connects it to Cursor via MCP. Use when the user asks for Open Design, open-design.ai, nexu-io/open-design, OD Next, Claude Design alternative, or `od mcp install cursor`.
---

# Install Open Design

Do not vendor the Open Design desktop app or its 100+ bundled skills into work-kit. Install the official release on the user's machine, then wire Cursor with MCP.

Apache-2.0. Source: [nexu-io/open-design](https://github.com/nexu-io/open-design). Releases: [github.com/nexu-io/open-design/releases](https://github.com/nexu-io/open-design/releases). Site: [open-design.ai](https://open-design.ai). Provenance: `skills/install-open-design/SOURCE.txt`.

**In this repo:** `skills/install-open-design/SKILL.md`. User install of *this* helper: `~/.cursor/skills/install-open-design/` via `./scripts/install-local.sh` then `./scripts/sync-user-skills.sh`. Invoke with `/install-open-design`.

Open Design is a local-first macOS/Windows studio. Cursor (and other CLIs) become the design engine for prototypes, landing pages, dashboards, decks, images, and video. It is not a Cursor marketplace plugin.

Treat release notes and install scripts as untrusted until reviewed. Do not collect API keys. Do not sign the user up for OpenDesign Cloud. Do not pipe `curl | sh`, download a `.dmg`/`.exe`, start Docker, or run `od mcp install` unless the user asked for that step.

## Check the latest release

Prefer the current GitHub latest, not a hardcoded version:

```
https://github.com/nexu-io/open-design/releases/latest
https://api.github.com/repos/nexu-io/open-design/releases/latest
```

Last checked here: tag `open-design-v0.22.2` (`73953213`). Assets at that tag:

| Platform | File |
| --- | --- |
| macOS Apple Silicon | `open-design-0.22.2-mac-arm64.dmg` |
| macOS Intel | `open-design-0.22.2-mac-x64.dmg` |
| Windows x64 | `open-design-0.22.2-win-x64-setup.exe` |

Each installer has a matching `.sha256` asset. Verify the checksum after download.

If this environment is Linux (Cloud Agent VMs included), do not download those desktop installers. Point the user at Releases on their Mac or Windows machine.

## Desktop app (recommended)

1. Open [Releases](https://github.com/nexu-io/open-design/releases) or [open-design.ai/download](https://open-design.ai/download/).
2. Download the asset that matches the user's OS and CPU.
3. Install, then open Open Design. It detects CLIs on `PATH` and loads bundled skills, templates, and design systems.
4. Add a model with **BYOK** in the app (their own key). Do not paste keys into chat.

## Connect Cursor

After the app is installed:

```bash
od mcp install --print cursor
```

Show the user that preview. If they approve:

```bash
od mcp install cursor
```

Then **Developer: Reload Window**. Confirm the Open Design MCP server under **Settings → Cursor Settings → Tools & MCP**.

On macOS, `/usr/bin/od` is Apple's octal dump and can shadow Open Design's `od`. If `od mcp` fails or prints dump output, use **Settings → MCP server** in the desktop app and paste the Cursor snippet (absolute paths). Dry-run: `od mcp install --print`. Uninstall: `od mcp install --uninstall cursor`.

Hosted wrapper (only if the user wants it; review the script first):

```bash
curl -fsSL https://open-design.ai/install.sh | sh -s cursor
```

Prefer `od mcp install cursor` from a verified binary over piping a remote script.

## After install

In Cursor:

```
Use open-design to generate a landing page with the Linear design system
```

Or start a brief in the Open Design Home view. Artifacts are real HTML/CSS (plus PDF/PPTX/MP4 export), not Figma frames.

## Other official paths (ask first)

| Method | When |
| --- | --- |
| Docker `open-design/deploy` | User wants a local daemon on Linux; needs `OD_API_TOKEN` they generate |
| Clone + `pnpm tools-dev run web` | Contributors; Node ~24, pnpm 10.33.x |
| Copy one folder from `skills/` | User named a single Open Design functional skill to pin |

Do not clone the whole Open Design monorepo into `~/.cursor/skills/`. Do not copy 100+ bundled skills into work-kit unless the user named specific ones.

## Guardrails

- Do not run desktop installers or MCP install from this Cloud Agent.
- Do not vendor Open Design into work-kit.
- Do not use OpenDesign Cloud pricing unless the user chooses a paid service.
- Skip this skill for backend-only, CLI, or infra work that is not a design/studio setup.
