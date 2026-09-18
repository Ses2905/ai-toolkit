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

- **Display — Space Grotesk** (neo-grotesque): headings, KPI numbers, wordmark.
- **Body — Plus Jakarta Sans** (geometric sans): all UI and reading text.
- **Serif — Fraunces**: editorial eyebrows / lead-ins, used sparingly.
- **Script — Caveat**: a single decorative flourish only.

Fallbacks are defined in `tokens.css` so the system degrades gracefully.

## Fonts &amp; licensing

The type families are **open-licensed (SIL OFL)** — Space Grotesk, Plus Jakarta
Sans, Fraunces, and Caveat (woff2 from Google Fonts). They are safe to embed and
self-host on public **or** private pages, so the binaries are **committed** under
`design-system/fonts/` and the system renders branded type everywhere.

If you'd rather use a purchased commercial face (e.g. Juturu, Lenia Sans), drop
its licensed files into `design-system/fonts/` and point the relevant
`@font-face`/`--font-*` token at them — but keep those binaries out of this
public repo (they're git-ignored by family name).
