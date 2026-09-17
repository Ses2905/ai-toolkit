# Release notes draft: Work Kit first-delivery copy (unpublished)

**Product.** Work Kit (`work-kit`), personal MIT Cursor plugin.
**Live version today (17 Sep 2026).** 1.20.0. Install copy still fails G3. **Do not publish these notes against 1.20.0.**
**Draft version when WK-1 lands.** 1.20.1 (patch). Copy only. No dest rewrite. Bump `.cursor-plugin/plugin.json` in the same commit as the echo.
**Draft date.** Not 15 Oct until G3 is green. Publish the day the patch is in `main` and the owner has reinstalled. If that is before 15 Oct, the notes date is that day. If 15 Oct arrives with G3 red, **there is no release.** Slip. Do not post anyway.
**Release type.** Patch. Not major (the loop already exists). Not minor (no new command).
**Features pasted.** Empty. The change is install next-steps, not a new skill.
**Channel.** GitHub README only. No email list, no in-app banner, no Product Hunt, no social. [Comms](q4-2026-first-delivery-comms.md).
**Related:** [WK-1](../tickets/wk-1-g3-install-copy.md), [US-1 AC](../user-flows/us-1-g3-acceptance-criteria.md), [Exec summary](q4-2026-exec-summary.md), [GTM](q4-2026-first-delivery-gtm.md)
**Source prompt:** [Release notes](https://aiuxplayground.com/prompts/release-notes-generator) (AI UX Playground)

Status: **draft, embargoed.** Clone visitors who follow 1.20.0 still see optional cloud sync as step 3. Publishing this file as if that were fixed is a lie.

---

## 1. Release overview (publish only after G3)

**Title.** Work Kit 1.20.1: install step 3 is `/plan`
**Date.** TBD. Fill with the commit day. Not a calendar wish.
**Summary.** After install, the next numbered step is `/plan` (or `/debug` if something is already broken), on the script echo and both README lists. Cloud sync moves to the Cloud Agents section. The Plan, Debug, Review, Ship commands are not new. Routing is.

**Highlights (max three, after the patch exists)**

- Item 3 is `/plan`, not optional cloud sync.
- Clone README and checkout README match the echo.
- Catalog dumps are not numbered install steps.

**Do not highlight.** Skill-folder count. Animation/Remotion catalogs. GitHub stars. "We shipped first delivery" if the log still has 0 rows.

---

## 2. New features

**None.** `/plan` `/debug` `/review-diff` `/ship` already ship in 1.20.0. First delivery is not a new command. If a notes template needs a feature block, use this after G3:

**Install next-steps name the loop**

- What. Numbered install tells you to Reload, confirm Work Kit under Customize, then `/plan` in a product-repo chat.
- Benefit. You are not sent to a Cloud Agents toggle or a catalog list as the finish line.
- How. `./scripts/install-local.sh`, reload, Customize, User, Work Kit, then `/plan` (or `/debug` if something is already broken). Tiny work: mark tiny, do not fake a six-section plan.
- Visual. Terminal paste of the new echo, not a marketing screenshot. Until the patch, the live visual is line 30 optional sync. Do not paste the old echo into a "what's new" blog.

---

## 3. Improvements (after G3)

| What | User impact | Why it matters | Before | After |
| --- | --- | --- | --- | --- |
| Script success echo item 3 | Clone and reinstall paths | Stdout is the product | `Optional for Cloud Agents: ./scripts/sync-user-skills.sh` | `/plan` (or `/debug` if broken) |
| Clone README numbered list | GitHub clone visitors | They do not read `docs/` | Item 3 = Cloud Agents toggle | Same three beats as the echo |
| Checkout README numbered list | Existing checkout | Stops shopping as onboarding | Items 3-4 = catalog dumps | Cloud and catalogs move out of the numbered install |

Until those rows are true in git, this section is empty. Do not publish a before/after that has not been committed.

---

## 4. Bug fixes (after G3)

- **Fixed:** Install next-steps taught skip (G3 / WK-1). Users who follow the list will be told to `/plan`.
- **Not fixed in 1.20.1:** Cloud VMs still do not mount `~/.cursor/plugins/local`. Empty session log. Untimed E1. Teams hiding the card. Dirty-tree fixtures. Those are later, or not this patch.

What users will notice: the three printed lines after `Installed work-kit to ...`. Nothing else in Cursor chrome.

---

## 5. Technical updates

- Backend: none. Not a service.
- Performance: none.
- Security: no change to `/ship` secret rules in this patch. Still forbid `.env` and `git add .` on unrelated files. A copy commit still gets `/review-diff`.
- Infrastructure: dest path unchanged. Real directory copy, not a checkout symlink. Cloud checker is 14 Nov, not this release.

Version bump only: `1.20.0` to `1.20.1` in `.cursor-plugin/plugin.json`.

---

## 6. Deprecations and breaking changes

**Not breaking.** Commands stay. Dest stays. MIT stays.

**Copy change (behavioral for anyone who follows numbered lists).**

- Removed as Avery step 3: optional cloud sync.
- Removed from checkout numbered install: catalog / slash inventory as items 3-4.
- Migration: re-run `./scripts/install-local.sh` so dest skills pick up `install-work-kit` copy if that file changed. Reload Window. No data migration. No flag.

**Timeline.** Effective on the 1.20.1 commit. No sunset window. The old step 3 was a bug, not an API.

---

## 7. What's next (honest, not teasers)

- Next product sitting after this patch: one logged product-repo `/plan` (or tiny) and named-file `/ship`. That is go-live, or the slip date.
- 14 Nov: sync checker that fails closed if a core skill folder is missing. Six cloud runs after that.
- 31 Dec: grade plan-or-tiny 80% and 8 named-file ships.
- Not next: Marketplace, paid tier, first-run UI, capture gallery (O4 parked).

Stay updated: watch this repo. There is no newsletter.

---

## 8. Thank you

**Do not publish a thank-you to testers, community, or "everyone who gave feedback."** Interviews 0. Survey 0. Support tickets pasted: 0.

If a line is required: Work Kit is Sarah Scherer's personal kit. MIT. No contributors to list for this patch unless git history names them on the copy commit.

---

## 9. Support and resources

- Docs: README numbered install (the product). [US-1](../user-flows/us-1-g3-acceptance-criteria.md) is the bar, not a user guide.
- Support: GitHub issues on Ses2905/cursor-skills. No chat queue. No SLA.
- Feedback: after G3, leftover-hours interviews and the beta survey. Not a CSAT widget.
- Community: none. Do not invent a Discord.

---

## 10. Formatting options

**Do not send any of these until G3 is green.**

### Short (notification, after publish)

Work Kit 1.20.1: after install, step 3 is `/plan`. Re-run `install-local.sh` and reload.

### Medium (README "what's new", after publish)

1.20.1 patch. Install echo and both README lists now use the same three beats: Reload, Customize, `/plan` (or `/debug` if something is already broken). Cloud sync lives under Cloud Agents. Catalog lists are not install steps. Reinstall and reload. Commands are unchanged.

### Full (this file's sections 1-9, after publish)

Use sections 1-9 with TBD date filled. Do not add ARR, NPS, or a hero screenshot of Customize-visible.

### Social snippets

**Do not post.** GTM forbids a launch post while the log denominator is 0. If someone asks in passing: "Install step 3 is `/plan` now. That's the note." No hashtags. No Product Hunt.

### What to say about 1.20.0 if asked today

Live kit. Loop commands exist. Install still finishes on optional cloud sync. First delivery is not released. Use [exec summary](q4-2026-exec-summary.md), not this draft.

---

## How to use

When WK-1 merges: bump to 1.20.1, fill the date, move this draft to a dated notes file or README changelog, reinstall, then the short blurb may go in README. Until then this file is a warning not to announce.

Next sitting still does not need release notes. It needs item 3 to be `/plan`.
