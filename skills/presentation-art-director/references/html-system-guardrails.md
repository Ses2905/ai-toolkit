# Frozen HTML presentation guardrails

Use these rules when working inside the user's HTML Presentation Starter Kit or any deck explicitly described as frozen.

## Approved canvas geometry

- Stage: 1920 × 1080, scaled with `fit()`
- `--rail: 80px`
- `--head-inset: 148px`
- `--foot-safe: 72px`
- `--ls-transition: 40px`
- Spacing scale: 8 / 12 / 16 / 24 / 32 / 40 / 48 / 64 / 80

Do not change these during visual refinement.

## Standard shell

Standard `.s-ls` content slides use five rows:

1. top safe area
2. auto-height header
3. 40px transition row
4. flexible body region
5. bottom safe area

Header and body share the same master frame.

`CONTAINER WIDTH = ALIGNMENT`  
`TEXT MAX-WIDTH = READABILITY`

Standard slide header `h1/h2` and `.lede/.sub` may use the full master frame. Editorial specials may keep narrower text measures.

## Vertical modes

Only three modes:

- Standard `.s-ls`: `0.8fr / content / 1.2fr`
- Shallow `.s-ls.s-ls-shallow`: `0.55fr / content / 1.45fr`
- Dense `.s-ls.s-dense`: top-aligned

Do not create a fourth mode. Do not change a slide's mode during visual refinement unless the user explicitly reopens layout classification.

## Special archetypes

Cover, chapter, quote, close, map, thesis, and bleed slides may use their own internal composition. They still inherit the outer canvas unless intentionally full-bleed.

## Ownership

- Canvas owns outer geometry and safe areas.
- Slide shell owns header, transition, and body region.
- Body mode owns vertical composition.
- Component owns internal geometry.
- Parent owns spacing between siblings.
- Text style owns readable measure and wrapping.
- Theme owns fonts, colors, and decorative treatment.
- Content owns message length and density.

Fix the layer that owns the problem.

## Diagnostic order

1. Parent geometry
2. Grid/flex structure
3. Reusable component
4. Typography/wrapping
5. Content
6. Archetype classification

Never begin with a local margin or position adjustment.

## Forbidden visual-refinement fixes

Do not:
- edit global `layout-system.css` or `presentation-system.css`
- alter rails/safe areas/transition
- move the slide header or body region
- use negative margins
- use transforms to fix normal flow
- shrink font size/line-height/padding to force fit
- add arbitrary structural max-widths
- create slide-specific Y offsets
- globally clean/refactor CSS
- change unrelated slides

New visual CSS must be semantic, locally scoped, and contained inside the existing body region.

## Repeated components

Use `repeat(n, minmax(0, 1fr))`; children get `min-width: 0`. Parent controls gaps. Component controls internal spacing.

Flag content before compressing CSS.
