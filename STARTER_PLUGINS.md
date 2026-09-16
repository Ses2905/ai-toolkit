# Starter plugins (user scope)

Install from **Customize** in the sidebar. Choose **user** scope so they apply to every project. Do not install these into a single repo unless you want them only there.

Official catalog: [cursor.com/marketplace](https://cursor.com/marketplace)

## Install first

| Plugin | Why |
| --- | --- |
| [Continual Learning](https://cursor.com/marketplace/cursor/continual-learning) | Learns durable preferences and workspace facts into `AGENTS.md` |
| [Create Plugin](https://cursor.com/marketplace/cursor/create-plugin) | Scaffold and validate more plugins, including updates to this kit |
| [GitHub](https://cursor.com/marketplace/github) | Repos, issues, PRs, and Actions from chat |

## Design skill (not a marketplace plugin)

[Impeccable](https://impeccable.style/#downloads) is a Cursor skill, not a Customize plugin. On the user's machine:

```bash
npx impeccable install --providers=cursor --scope=global
```

Reload Cursor, then in each product repo run `/impeccable init`. Details: `skills/install-impeccable/SKILL.md`.

GitHub catalogs such as [awesome-cursor-skills](https://github.com/spencerpauly/awesome-cursor-skills) are lists. From this repo:

```bash
./scripts/install-catalog-skills.sh --preset design-product
```

That copies selected `SKILL.md` folders into `~/.cursor/skills/` (design, visuals, motion, presentations, product). Do not dump the whole catalog. Details: `skills/install-github-skills/SKILL.md`.

[Open Design](https://github.com/nexu-io/open-design/releases) is a local-first desktop studio (macOS/Windows), not a Customize plugin. Install the latest GitHub Release on the user's machine, then `od mcp install cursor`. Details: `skills/install-open-design/SKILL.md`.

[React Bits](https://github.com/DavidHDev/react-bits) is a shadcn registry of animated React components. Add `@react-bits` to the app's `components.json`, then `npx shadcn@latest add @react-bits/<Name>-TS-TW`. Details: `skills/react-bits/SKILL.md`.

[High-End Visual Design](https://www.skills.sh/leonxlnx/taste-skill/high-end-visual-design) is a Leonxlnx taste-skill variant (`soft-skill` folder). Invoke `/high-end-visual-design`. Distinct from `/taste-skill`. Details: `skills/high-end-visual-design/SKILL.md`.

[Lark Slides](https://www.skills.sh/larksuite/cli/lark-slides) needs the official CLI (`npm i -g @larksuite/cli`) and a Lark/Feishu login. Invoke `/lark-slides`. Auth rules live in `skills/lark-shared`. Details: `skills/lark-slides/SKILL.md`.

[ckmslides / Slides](https://www.skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ckmslides) is the HTML Chart.js deck skill from ui-ux-pro-max (`--skill slides`). Invoke `/slides`. Needs sibling `skills/design-system`. Distinct from `/lark-slides`. Details: `skills/slides/SKILL.md`.

[Frontend Slides Editable](https://www.skills.sh/archlizheng/frontend-slides-editable/frontend-slides-editable) is a zero-dependency HTML deck with a built-in editor (drag objects, Pages sidebar, Ctrl+S). Invoke `/frontend-slides-editable`. Distinct from `/slides`. Details: `skills/frontend-slides-editable/SKILL.md`.

[HTML PPT](https://www.skills.sh/lewislulu/html-ppt-skill/html-ppt) authors themed static HTML presentations (36 themes, layouts, presenter mode). Invoke `/html-ppt`. Distinct from `/slides` and `/frontend-slides-editable`. Details: `skills/html-ppt/SKILL.md`.

[Product Strategy Session](https://www.skills.sh/deanpeters/product-manager-skills/product-strategy-session) orchestrates Dean Peters PM skills (positioning, discovery, roadmap). License: CC BY-NC-SA 4.0. Invoke `/product-strategy-session`. Details: `skills/product-strategy-session/SKILL.md`.

[HTML Diagram](https://www.skills.sh/plannotator/effective-html/html-diagram) builds a self-contained HTML diagram (topology, sequence, state, hierarchy). Invoke `/html-diagram`. Visual register lives in `skills/design-artifact`. Details: `skills/html-diagram/SKILL.md`.

[HyperFrames Animation](https://www.skills.sh/heygen-com/hyperframes/hyperframes-animation) is HeyGen motion knowledge (GSAP rules, blueprints, adapters). Invoke `/hyperframes-animation`. Contract lives in `skills/hyperframes-core`. Apache-2.0. Details: `skills/hyperframes-animation/SKILL.md`.

[Review Animations](https://www.skills.sh/emilkowalski/skills/review-animations) reviews motion code against Emil Kowalski's craft bar. Invoke `/review-animations`. Distinct from `/review-the-diff` and `/improve-animations`. Details: `skills/review-animations/SKILL.md`.

[Improve Animations](https://www.skills.sh/emilkowalski/skills/improve-animations) audits a codebase's motion, then writes self-contained plans. Invoke `/improve-animations`. Read-only on source. Distinct from `/review-animations`. Details: `skills/improve-animations/SKILL.md`.

[Find Animation Opportunities](https://www.skills.sh/emilkowalski/skills/find-animation-opportunities) finds places that should animate and rejects the rest. Invoke `/find-animation-opportunities`. Read-only. Distinct from `/improve-animations`. Details: `skills/find-animation-opportunities/SKILL.md`.

## Install if you do this work

| You… | Plugin |
| --- | --- |
| Ship web UI | [Playwright](https://cursor.com/marketplace/playwright) plus Impeccable (above) |
| Track work in Linear | [Linear](https://cursor.com/marketplace/linear) |
| Implement Figma | [Figma](https://cursor.com/marketplace/figma) |
| Keep notes in Notion | [Notion](https://cursor.com/marketplace) (search Customize for Notion) |
| Live in Gmail / Drive / Calendar | [Gmail](https://cursor.com/marketplace), [Google Drive](https://cursor.com/marketplace), [Google Calendar](https://cursor.com/marketplace) |
| Want a second model to gut-check plans | Search Customize for **Advisor** |

Skip the long tail of CRM, ads, and recruiting plugins until you actually need them. Extra tools add noise.

## How to install

1. Open **Customize**
2. Search for the plugin
3. **Install** → **user**
4. Authenticate the app if Cursor prompts you

CLI alternative: `/plugin` (user or project scope).

## Team-wide later

On Teams/Enterprise: **Dashboard → Plugins**. Set **Default On** or **Required** for plugins everyone should have. Publishing a personal skill from **Customize → Skills** puts it on the Default team marketplace (opt-in for others).

## This kit vs marketplace plugins

- **Work Kit** (this repo) → how the agent plans, debugs, reviews, and ships
- **Marketplace plugins** → product integrations (Linear, Figma, GitHub) and Cursor-maintained workflows (Continual Learning)
