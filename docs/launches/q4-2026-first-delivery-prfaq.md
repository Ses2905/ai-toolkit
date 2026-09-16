# PR/FAQ: Work Kit first delivery

**Working backwards artifact.** Not a press wire. Do not post this to Product Hunt, Twitter, or a journalist. Owned channel on launch day is the GitHub README and the install script echo.
**Customer:** Avery, solo IC on desktop Cursor
**Launch day this document stands in:** 15 October 2026 (phase 1). Cloud path 14 November 2026.
**Owner / "company":** Sarah Scherer. Personal MIT plugin. Not Cursor Inc.
**Related:** [Messaging](../messaging/work-kit.md), [Problem statement](../problem-statements/work-kit-first-delivery.md), [GTM](q4-2026-first-delivery-gtm.md), [Insights](../research/first-delivery-insights.md)
**Source prompt:** [Amazon PR/FAQ](https://aiuxplayground.com/prompts/amazon-prfaq) (AI UX Playground)

Written as if 15 Oct already happened with G3 copy live. As of 16 Sep 2026 that copy is not live. If you ship this narrative while `install-local.sh` still says optional cloud sync as step 3, the press release is false.

---

## 1. Press release

**Headline.** Work Kit makes the next Cursor change a planned, named-file ship after one user-scope install.

**Subtitle.** Success is an accepted `/plan` (or a marked tiny skip) and a commit that staged the files you named. A plugin card in Customize is not the finish line.

**Date.** 15 October 2026

**Intro.** Work Kit is a once-per-machine Cursor plugin. You install it at user scope, reload, confirm it under Customize, User, then open a product repo and run `/plan`. The agent writes a plan you can accept or reject before it edits. You review the real `git diff`. You `/ship` named paths only. You do not copy kit files into each application repo.

**Problem.** Ranked by pain for Avery:

1. Skills and plugins install cleanly, then the next sitting starts in chat and the agent implements with no plan. There is nothing to accept or reject. The change is already underway.
2. A dirty tree plus `git add .` ships leftover notes, or a secrets file, with the intended patch.
3. A Cloud Agent run looks like Work Kit is missing, because local plugins do not exist on cloud VMs, and sync was easy to skip.

**Solution.** Matching those three:

1. Install next-steps are Reload, Customize shows Work Kit, then `/plan` in a product repo (or `/debug` if something is already broken). Tiny obvious changes are logged as tiny skip, not a fake six-section plan.
2. `/review-diff` reads `git diff`. `/ship` stages named files, keeps hooks on, and does not `--no-verify` unless you ask.
3. For Cloud Agents, `./scripts/sync-user-skills.sh` plus the Sync Skills toggle. A checker fails if a core skill folder is missing. That path is the Cloud Agents section, not Avery's third install beat.

**Leader quote.** Sarah Scherer, owner: "I could get a plugin card and still start the next sitting in chat. The kit had not done its job. First delivery means a plan I can refuse, then a ship of the files I meant. If the README congratulates Customize, we trained the skip."

**How it works.**

1. Clone [github.com/Ses2905/cursor-skills](https://github.com/Ses2905/cursor-skills).
2. Run `./scripts/install-local.sh`. That copies a real directory to `~/.cursor/plugins/local/work-kit`. Cursor ignores a symlink into the checkout.
3. Command Palette: Developer, Reload Window. Customize, filter User, confirm Work Kit.
4. Open a product repo. `/plan`. Accept or reject. Implement the first slice.
5. `/review-diff`. Then `/ship` the named files. Push.
6. If you use Cloud Agents: run `./scripts/sync-user-skills.sh`, turn on Sync Skills for Cloud Agents, and do not start a run if the checker fails. Phase 2, 14 Nov.

**Customer quote.** Avery, desktop IC (composite, not a survey complete): "I used to stop when Customize showed the card. Today the next-steps said open the app repo and `/plan`. I accepted a one-slice plan. `/ship` staged two files. It did not take the `.env` sitting next to them."

**How to get started.** Clone the repo and run `./scripts/install-local.sh`, then follow the three next-steps: [github.com/Ses2905/cursor-skills](https://github.com/Ses2905/cursor-skills)

---

## 2. FAQ

### Customer FAQs

**Is this Cursor Inc.?** No. Personal project, MIT license. Cursor is the host. Work Kit is a user-scope plugin in this GitHub repo.

**What does it cost?** $0. There is no waitlist and no paid tier.

**When is it done installing?** After reload, Customize shows Work Kit, and you have started `/plan` (or a tiny skip) in a product repo. Visible plugin, no plan, is not done.

**Do I copy this into every app repo?** No. User scope, once per machine. Repo facts stay in that repo's `AGENTS.md`.

**How is this different from `npx skills add`?** Skills-only install can put `SKILL.md` files on disk without the plugin slash commands. First delivery is `/plan`, `/debug`, `/review-diff`, `/ship` from the plugin. Skills-only is a fallback, not the happy path.

**How is this different from Continual Learning?** Continual Learning stores durable facts in `AGENTS.md`. Work Kit is the session loop. You can use both.

**What if the change is one obvious file?** Log tiny skip. Do not invent a six-section plan. Then implement and `/ship`.

**I am on Teams and Customize is empty.** Local plugin imports may be blocked. Ask admin for Allow Local Plugin Imports, or use `~/.cursor/skills`. Teams is not the happy path this quarter.

**Will Cloud Agents see the plugin card?** No. Sync skills. Phase 2 is 14 Nov. Do not treat optional sync as desktop step 3.

**Can it ship secrets?** `/ship` is written to refuse `.env` and `git add .` on a dirty tree. You can still paste a secret in chat. Do not. There is no magic scanner product.

**Who supports this?** GitHub issues on the repo. No SLA. One owner.

### Internal FAQs

**Is this a big idea?** Not a TAM idea. It is big enough if every product-repo sitting this quarter starts with plan or tiny and ends in named-file ship. If the test is "market share of Cursor plugins," this PR/FAQ fails and should not be written as a company launch.

**Should we be the ones to build it?** Yes, because the kit already exists and the miss is our copy. No, if the next work is a marketplace listing or a catalog dump. Those are not first delivery.

**Is there a legitimate plan?** Yes, if G3 lands by 8 Oct, the session log has rows, and 15 Oct is go only when G1 to G4 pass. No, if we publish this PR while step 3 is still optional cloud sync.

**Elephant: is this press release true today (16 Sep)?** No. `install-local.sh` still prints optional cloud sync as step 3. README clone path still ends on the Cloud Agents toggle. Do not use this document as launch comms until F1 ships.

**Why not wait for 5 to 8 interviews?** Problem interviews can run in leftover hours. They do not replace G3. Usability of the old echo is not first-delivery UX.

**Why no Product Hunt?** $0 GTM. Audience is one primary operator plus clone visitors. A Hunt post would announce a plugin card.

**Who is the launch team?** Sarah. There is no PR desk, support rotation, or sales engineer.

**What do we cut if 8 Oct SLC fails?** Cut catalog work, research templates, and cloud copy on Avery's list. Do not cut the log. Slip 15 Oct rather than launch on yellow G3.

**How do we know it worked?** Session log: plan-or-tiny rate, named-file ships. Not NPS. Not Mixpanel. Grade 31 Dec. Disappointment question on the core loop only.

### Technical FAQs

**Where does it live?** `~/.cursor/plugins/local/work-kit` as a real directory. Install script copies. It does not symlink the checkout. Cursor ignores those symlinks.

**Why do Cloud Agents miss it?** Cloud VMs do not mount `~/.cursor/plugins/local`. Skills must be in `~/.cursor/skills/` with Sync Skills for Cloud Agents on. A checker should exit non-zero if `plan-the-work` or the other four core folders are missing.

**What are the core skills?** `plan-the-work`, `debug-from-evidence`, `review-the-diff`, `ship-the-change`, `capture-a-skill`. Slashes: `/plan`, `/debug`, `/review-diff`, `/ship`, `/new-skill`.

**Does `/ship` disable hooks?** No, unless the user asks for `--no-verify`.

**What is G3?** README next-steps and `install-local.sh` echo are identical, and step 3 is `/plan` or `/debug` if broken.

**Can we enforce the plan gate in Cursor itself?** No. We own skill text and copy. We do not own the agent runtime. If agents still edit before accept after G3, that is F16, only after the log shows skip.

### Business FAQs

**Price?** $0. MIT.

**Availability?** Phase 1 15 Oct, desktop, personal Cursor seat. Phase 2 14 Nov, cloud sync. Not a regional rollout. Not a percentage flag.

**Support?** Owner. Issues on GitHub. No chat widget.

**Revenue?** None. Do not put ARR in a FAQ.

**Competition?** Adjacent tools do different jobs (catalog lists, `AGENTS.md` memory). We do not write comparison SEO this quarter.

---

## 3. Key principles (how to read this file)

**Customer-centric.** Avery's sitting, not a plugin marketplace. The benefit is a plan they can refuse and a commit that did not scoop `.env`.

**Forward-looking.** Dated 15 Oct 2026. Describes the experience after G3. It is not a status report of 16 Sep.

**Specific.** Paths, slash names, dates, $0, MIT, GitHub URL. No "seamless workflow" and no "empower developers."

**Testable assumptions.**

| Assumption | How we will know | When |
| --- | --- | --- |
| Installer tries `/plan` without a researcher | Usability: they type it from copy. Survey Q10 copy-led `/plan` | After G3, by 14 Oct |
| E1 takes 10 minutes or less | Two timed runs in the session log | 15 Oct, again in Q4 |
| Loop is default | Plan-or-tiny >= 80% of logged product-repo sittings | 31 Dec |
| Ship is safe | 8 named-file ships. Zero `.env` from `/ship` | 31 Dec |
| Cloud path works | Checker green. 6 runs load plan or debug | 14 Nov onward |
| This PR is honest | G3 pass. Script step 3 is `/plan` | 8 Oct, or the PR is withdrawn |

**Three tests (McAllister).** Big enough for this operator's quarter: yes. Big enough as a company launch: no, so we do not send this to press. Should we do it: yes, the miss is our next-steps. Legitimate plan: only after F1.

---

## What this PR/FAQ does not authorize

- Shipping a first-run UI, dashboard, or marketplace listing.
- Announcing public GA.
- Filling the session log with invented rows so the "customer quote" looks measured.
- Using the composite Avery quote as a real testimonial.

If the customer quote were true today, G3 would already pass. It does not. Work backwards means change the echo until the quote could happen, then log whether it did.
