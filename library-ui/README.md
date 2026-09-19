# Library UI — functional wireframe

A data-driven, self-contained prototype of the **AI Skills Library + Installer**
UX. Focus is **information architecture, navigation, flows, and interaction**
— styling is intentionally neutral (brand/type/color polish is deferred).

```bash
# Serve from the repo root so the app can read the live catalog:
python3 -m http.server 8090            # then open http://localhost:8090/library-ui/
```

## What's implemented

- **App shell** — persistent left nav (Home · Library w/ kind sub-nav · Discover
  · Projects · Integrations · Inbox · Activity · Settings), top bar with global
  search + New + Add, max-width workspace, collapsible sidebar on narrow widths.
- **Home** — search hero, compact library summary, *Needs attention*,
  collections, recent activity.
- **Library browse** — search, kind tabs, category/sort filters, removable
  filter chips, **Cards / List** toggle, compact cards with the type visual
  language (label + glyph, not color-only).
- **Global search** — grouped by kind; plus a **Command palette** (⌘/Ctrl-K).
- **Item detail drawer** — Overview / Relationships / Source tabs, with
  *Used by / Depends on / References / Enabled in* as links, a relationship
  mini-map, and progressive disclosure of technical details.
- **Workflow detail** — numbered step sequence showing the skills each step
  invokes.
- **Add to Library** — source picker → staged **inspection** → **routing
  review** (with confidence + conflict) → **conflict compare** → **install
  success** summary.
- **Projects / Integrations / Inbox / Activity / Health / Create** — structured
  screens with realistic content.

## Data

The synthesis lives in **`data-live.js`** (`buildLibraryData(catalog)`): it turns
`catalog/skills-index.json` (real skills + prompts) into the UI's item set and
adds synthesized workflows, references, tools, projects, integrations, inbox,
updates, health and activity so the still-sparse tiers show realistic content.

That one module is used two ways, so the two can never drift:

- **At runtime** — `app.js` fetches the real catalog and builds the data live,
  so the Library always reflects the current index. The sidebar shows a **live**
  badge. Served from within `library-ui/` (or `file://`), the catalog isn't
  reachable, so the app falls back to the bundled snapshot and shows a
  **snapshot** badge.
- **At build time** — `build-data.mjs` renders the committed `data.js` snapshot
  used as that fallback. Regenerate it whenever the catalog changes:

```bash
node library-ui/build-data.mjs
```

## Status

This is Phase 1–6 of the UX plan (IA → primitives → flows). Final visual styling
(Phase 7) is deliberately not applied. Discover's external feed and live install
are wired as UI architecture, not real network calls.
