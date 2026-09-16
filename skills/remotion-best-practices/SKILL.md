---
name: remotion-best-practices
description: Router for all Remotion skills
version: 4.0.525
---

# Remotion Best Practices

Pinned from [remotion-dev/skills `remotion-best-practices`](https://github.com/remotion-dev/skills/tree/3b9e6561dababf40a485772a7cd641268bb7c365/skills/remotion-best-practices) at `3b9e6561dababf40a485772a7cd641268bb7c365` (v4.0.525). Listing: [skills.sh](https://www.skills.sh/remotion-dev/skills/remotion-best-practices). Official CLI: `npx skills add https://github.com/remotion-dev/skills --skill remotion-best-practices`. Provenance: `SOURCE.txt`. Nested topic files: `remotion-*/REFERENCE.md`.

**In this repo:** `skills/remotion-best-practices/SKILL.md`. Scoped rule: `rules/remotion-best-practices.mdc` (`alwaysApply: false`). User install: `~/.cursor/skills/remotion-best-practices/` via `./scripts/install-local.sh` then `./scripts/sync-user-skills.sh`. Invoke with `/remotion-best-practices`. Distinct from `/hyperframes-animation` (HyperFrames GSAP) and `/apple-design` (web UI motion).

Do not run `npx create-video`, `npx remotion render` / `still`, Lambda, or paid map APIs unless the user asked. Load nested `REFERENCE.md` files as this skill directs. `remotion-dev/skills` has no LICENSE file.

## Preserve user changes

Users may make edits in the code outside of the conversation.

If you detect a surprising change made in the meanwhile, don't overwrite it, assume it was intentional or ask for confirmation.

## Creating a video

If the user asks to make, create, or build a new video or composition, load [Create a new Remotion video](./remotion-create/REFERENCE.md), whether or not a Remotion project already exists.

## New project setup

If no Remotion project currently exists, load [Create a new Remotion project](./remotion-create/REFERENCE.md)

## React Markup Best Practices

If you are writing Remotion React Markup, load [Remotion Markup Best Practices](./remotion-markup/REFERENCE.md)

## Maps

For static maps, animated routes and markers, geographic explainers, Mapbox, MapLibre, MapTiler, GeoJSON, or 3D geographic flyovers, load [Remotion Maps](./remotion-maps/REFERENCE.md).

## Multimedia

For achieving multimedia tasks in the browser, such as trimming, cropping videos, or getting metadata from them, load [Remotion Multimedia](./remotion-multimedia/REFERENCE.md)

## Improving Interactivity

By structuring the Remotion markup well, we can allow users to interactively change things in the Studio and write back to code. If relevant: [Interactivity Best Practices](./remotion-interactivity/REFERENCE.md)

## Rendering

For advanced rendering beyond simple `npx remotion render`, see: [Rendering Best Practices](./remotion-render/REFERENCE.md)

## Opening Remotion Studio

To launch a project in Remotion Studio, open its exact local URL, or configure Studio CLI flags, load [Remotion Studio](./remotion-studio/REFERENCE.md).

## Captions

When working with Captions, load [Remotion Captions](./remotion-captions/REFERENCE.md).

## Creating a SaaS, automation or application

Use the [Remotion SaaS skill](./remotion-saas/REFERENCE.md) for knowledge about Remotion-powered SaaS apps, such as `<Player>`, rendering on Lambda, Vercel, Cloudflare, via Express.js, client-side rendering, or for finding the right SaaS template.

## Looking up Remotion APIs and documentation

To find and read current Remotion documentation, load [Remotion Docs](./remotion-docs/REFERENCE.md).

## Upgrading

To upgrade Remotion, related packages, compatible Mediabunny packages, and installed Remotion Agent Skills, load [Remotion Upgrade](./remotion-upgrade/REFERENCE.md).
