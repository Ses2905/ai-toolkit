# DESIGN.md — design foundations (canonical)

The single source of truth for visual standards. Skills, prompts, and workflows
must **reference this file** instead of restating type/color/spacing rules. The
machine-readable tokens live in `design-system/tokens.css`; this document is the
human-readable standard. Brand system name: **Verdant** (botanical / aqua).

## Palette (semantic)

| Token | Value | Use |
| --- | --- | --- |
| `--brand` | `#0e7490` | primary actions, links |
| `--accent` | `#34d399` | emphasis, progress |
| `--info` | `#38a3a5` | informational / "to do" |
| `--success` | `#0f9d6b` (soft `#c7f9cc`) | done / positive |
| `--warning` | `#b5730d` (soft `#f2c078`) | pending / caution |
| `--danger` | `#e0451f` (soft `#fe5d26`) | destructive / cancel |
| `--ink` | `#083344` | text, deep surfaces |
| `--paper` | `#f4faf8` | app background |

Derived from the uploaded Cool Waters / Botanical Breeze palettes plus a Summer
Sorbet warm accent. Prefer semantic tokens over raw hex in any component.

## Typography

- **Display** — Space Grotesk (neo-grotesque): headings, KPI numbers.
- **Body** — Plus Jakarta Sans (geometric): UI + reading text.
- **Serif** — Fraunces: editorial lead-ins, used sparingly.
- **Script** — Caveat: a single decorative flourish only.

All SIL OFL, self-hosted under `design-system/fonts/`. Scale (px):
12 / 13 / 15 (base) / 17 / 20 / 26 / 34 / 46 / 62. Line-height 1.08 tight →
1.55 normal. Default line length < 80 characters. Do not accent a single word in
a heading; avoid ALL-CAPS labels and mono for data.

## Spacing, radius, elevation

- **Space** (4px base): 4, 8, 12, 16, 20, 24, 32, 40, 48, 64.
- **Radius:** 8 / 12 / 16 / 22 / pill.
- **Elevation:** hairline borders + soft, low-contrast shadows — never harsh
  dark drop shadows.

## Motion

- Non-user-triggered motion is sparing and deliberate; one orchestrated moment
  beats scattered effects.
- Animate `transform`/`opacity` only. Custom easing `cubic-bezier(.32,.72,0,1)`.
- Always honor `prefers-reduced-motion`.

## Accessibility (quality bar)

- Visible `:focus-visible` on every interactive element (never remove outline
  without a replacement).
- Icon-only controls need `aria-label`; decorative icons `aria-hidden`.
- Semantic HTML first; `aria-sort` / `aria-live` where relevant.
- Meet WCAG AA contrast; `font-variant-numeric: tabular-nums` for number columns.

## What lives elsewhere

- Component/token CSS: `design-system/tokens.css` + `design-system/index.html`.
- The applied product UI: the Skills Field Guide (`scripts/skills_db.py`).
