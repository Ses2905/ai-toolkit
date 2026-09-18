# Verdant — Design System

A botanical / aqua interface language distilled from the uploaded inspiration
(the Cool Waters, Botanical Breeze, and Minty Fresh palettes, with a Summer
Sorbet warm accent) and the uploaded type families. It's a self-contained,
dependency-free reference: open `index.html` in a browser.

```bash
# from repo root
python3 -m http.server 8080 -d design-system   # then open http://localhost:8080
```

## What's here

- `tokens.css` — the design tokens (primitive → semantic layers) plus `@font-face`
  declarations. This is the single source of truth; import it and style with
  `var(--…)` only.
- `index.html` — the living showcase: color, type, scale/space, a component
  gallery (buttons, inputs, status pills, tags, progress, avatars, KPI stats,
  data table), and a composed project dashboard applying the system.
- `fonts/` — **not committed** (see licensing). Drop your licensed font files
  here to see the branded type; otherwise the system falls back to high-quality
  system stacks.

## Palette (semantic)

| Token | Value | Role |
| --- | --- | --- |
| `--brand` | `#0e7490` | primary actions, links |
| `--accent` | `#34d399` | emphasis, progress |
| `--info` | `#38a3a5` | "To do" / informational |
| `--success` | `#0f9d6b` (soft `#c7f9cc`) | "Done" |
| `--warning` | `#b5730d` (soft `#f2c078`) | "Pending" |
| `--danger` | `#e0451f` (soft `#fe5d26`) | "Cancel" / destructive |
| `--ink-900` | `#083344` | text, deep surfaces |

## Type roles

- **Display — Juturu** (neo-grotesque): headings, KPI numbers, wordmark.
- **Body — Lenia Sans** (geometric sans): all UI and reading text.
- **Serif — Virtus Verona**: editorial eyebrows / lead-ins, used sparingly.
- **Script — Bombshell**: a single decorative flourish only.

Fallbacks are defined in `tokens.css` so the system degrades gracefully.

## Fonts &amp; licensing

The type families (Juturu, Lenia Sans, Virtus Verona, Bombshell) are **purchased
commercial fonts**. This is a public repository, so the font binaries are **not
committed** — `design-system/fonts/` is git-ignored. To render the branded type
locally, copy your licensed files into `design-system/fonts/` using the names
referenced in `tokens.css` (e.g. `Juturu-Semibold.woff2`, `LeniaSans-Regular.ttf`,
`VirtusVerona-Serif.woff`, `Bombshell-Script.woff`). Do not redistribute them.
