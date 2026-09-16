# ICP: Work Kit (Q4 2026)

**Product we "sell."** We do not sell. Work Kit is a $0 MIT Cursor plugin. The offer is: one user-scope install, then `/plan` through named-file `/ship` in every personal repo.
**Current customers / design partners.** One. Sarah Scherer operating as Avery on desktop Cursor. No design-partner companies. Interviews 0.
**Who converted fastest.** The owner, via E2 (existing checkout + `install-local.sh`). There is no second conversion to compare. Log rows proving the loop: 0.
**Who wasted time.** Catalog shoppers (C3), `npx skills add` only (E3), Playground template chains (C7), anyone who needs a Teams admin before Customize shows a card (Riley as primary). Also: any sitting that writes strategy docs instead of G3 copy.
**Price.** $0. No seat. No usage fee.
**Sales motion.** None. README plus script echo. Not PLG, not sales-assisted, not enterprise. Calling this PLG is a fuzzy ICP.
**Opinion.** Primary ICP is **Avery, one solo IC who owns the machine and git**. If that feels too narrow for a B2B prompt, the prompt is the wrong tool. Widening to "AI teams at Series B" is a failed output.
**Related:** [Positioning](work-kit-positioning.md), [Recruitment](../research/first-delivery-recruitment.md), [GTM](../launches/q4-2026-first-delivery-gtm.md), [Diligence](../launches/q4-2026-diligence-qa.md)
**Source prompt:** [ICP definition](https://aiuxplayground.com/prompts/icp-definition-b2b-ai) (AI UX Playground)

Do not print fake logos. Archetypes in section 6 are sitting types. The only named account is the owner.

---

## 1. Primary ICP

**Name.** Avery. Solo IC on desktop Cursor.

**Firmographics (honest).** Not a firm. Headcount 1. Industry: whatever repos she ships. Geography: wherever this machine is. Revenue: irrelevant. No HQ. No procurement.

**Technographics (must).**

- Desktop Cursor, personal or Hobby-like seat she controls (not waiting on Allow Local Plugin Imports).
- Git, GitHub clone, a terminal, write access to `~/.cursor/plugins/local`.
- Uses Agent or chat to change code, not only to ask questions.
- Ships commits at least weekly.
- Will run `./scripts/install-local.sh` and Reload Window.
- Has more than one repo she does not want to vendor a kit into.

**Technographics (optional, not ICP).** Cloud Agents (Casey, same human, 14 Nov). Continual Learning and GitHub Marketplace plugins already at user scope.

**Anti-firmographic.** Company Cursor Teams/Enterprise as the **first** seat. Security review before a shell script. "We need this in every engineer's laptop image next quarter."

**One-line ICP.** A git-shipping IC who already lives in Cursor, owns the machine, and wants the same plan-then-named-ship bar in every personal repo without copying plugin files around.

If you cannot point at one human who matches that on this laptop, you do not have an ICP. You have a wish.

---

## 2. Economic buyer, champion, blocker

There is no buying committee. Map the hats anyway so we do not invent a VP.

| Role | Who | What they control | This quarter |
| --- | --- | --- | --- |
| Economic buyer | Avery (Sarah) | Hours and whether `/plan` runs | Same person |
| Champion | Avery | Will paste README for a friend, or not | Optional teammate paste only if a human asks |
| Blocker (self) | Avery in C1 | Chat implement with no plan | Default. Copy must beat this |
| Blocker (policy) | Teams admin | Local plugin imports | Riley. Not the ICP. Recovery paragraph only |
| Blocker (platform) | Cursor Cloud VM | Local plugin mount | Casey. Phase 2. Same human, different root |
| Blocker (process) | Avery in C7 | More templates instead of WK-1 | Internal. Treat as disqualified work |

**Do not staff.** Sales AE, legal, procurement, a "champion in engineering plus buyer in RevOps."

---

## 3. Jobs to be done and buying triggers

**Primary job.** When I start a real change in Cursor, I want a plan I can accept or reject, a review of the actual diff, and a commit that staged named files only, without copying a kit into this repo.

**Trigger to install (E1/E2).** Clone or checkout `cursor-skills`, need the loop on this machine, willing to run a script. Trigger is not a budget cycle.

**Trigger to use (the actual conversion).** Next non-tiny sitting after Reload. Copy must say `/plan`. Live copy currently fails that trigger (G3).

**Jobs we are not for.**

- Browse community skills (C3).
- Drop one SKILL.md fast (C2).
- Remember repo facts (C4).
- Issues and PRs in chat (C5).
- Vendor `.cursor/` into the app so the team clones it (C6).
- Collect Playground skills until the kit feels "complete" (C7).

**Switch trigger (unvalidated).** Leftover junk in commits, or re-explaining the loop in chat every sitting. We have not heard this from other ICs. Do not claim it as a market trigger.

---

## 4. Must-have vs nice-to-have signals

**Must-have (if missing, not ICP).**

- Can run a shell script and reload Cursor.
- Owns dest path (or a personal machine where local plugins work).
- Git on the product repo.
- Wants a delivery bar, not a larger catalog.
- Will open a product repo after Customize, not stop at the card.

**Nice-to-have (still Avery).**

- Already uses Continual Learning or GitHub plugin at user scope.
- Multiple personal repos.
- Occasional Cloud Agent runs (then they also need Casey list, later).
- English README is readable for them.

**Not signals of ICP.**

- Company size, ARR, "AI transformation" budget.
- Number of engineers.
- Already has awesome-cursor-skills starred.
- Asked for a demo, MSA, or SOC2.
- Teams seat. That is a constraint, not a whale.

---

## 5. Hard disqualifiers

Disqualify as **primary** this quarter. Recovery copy may still exist.

1. Needs billed seats, SSO, or an MSA.
2. Cannot or will not run `install-local.sh`.
3. Primary environment is Cloud Agents with no desktop install (wait for 14 Nov, do not warp Avery copy).
4. Teams/Enterprise seat where local imports are blocked **and** they refuse `~/.cursor/skills`.
5. Success metric is catalog size, Marketplace listing, or NPS.
6. Wants the kit copied into each application repo as policy (C6).
7. `npx skills add` only and expects `/plan` slashes (E3). Educate or walk away. Do not call them converted.
8. Will not use git. `/ship` is git.
9. Wants instant implement on every sitting and will not log tiny or `neither`.
10. Treats this file as a reason to start outbound to ten companies before G3.

If a lead matches three of these, they are not "enterprise expansion." They are a different product.

---

## 6. Ten account examples (archetypes, not logos)

The prompt asked for ten accounts. We have one real account. Nine others are sitting types. No invented company names.

| ID | Archetype | ICP? | Why |
| --- | --- | --- | --- |
| A1 | Sarah / Avery on this laptop, product repos, E2 install | Yes. The account | Only converted human. Loop still unlogged |
| A2 | Clone visitor who follows GitHub README E1 | Yes if they match section 1 | Same copy as Avery. Uncounted |
| A3 | Same human on a Cloud Agent VM | Secondary (Casey) | Skills path, not plugin card. 14 Nov |
| A4 | Friend who asks "how do you work in Cursor?" | Maybe | Teammate paste only. Not a pipeline |
| A5 | Catalog browser of awesome-cursor-skills | No | Send to the list. Do not onboard as first delivery |
| A6 | `npx skills add` only, no plugin dest | No (E3) | Missing slashes. Confusion, not a win |
| A7 | Teams engineer waiting on admin | No as primary (Riley) | Recovery paragraph. Do not sell |
| A8 | IC who wants facts in `AGENTS.md` | No as primary | Continual Learning. Complement |
| A9 | Team that wants `.cursor/` in every app git | No | C6. README forbids it for this kit |
| A10 | Builder filling Playground templates instead of editing line 30 | No this sitting | C7. Waste pattern |

**Converted fastest:** A1 (only data point). **Wasted time:** A5, A6, A10, and A7 if chased as ICP.

Do not replace A5-A10 with "Acme Health, Series B, 40 engineers." That would fail the sharpness test.

---

## 7. Outreach angles matched to the ICP

**Default.** Do not outreach. GTM is inbound README. Paid $0.

**If Avery (A1) is the audience (this machine).** Angle: "Step 3 is `/plan`. Open the script." Not a team-alignment pitch.

**If a clone visitor (A2) emails.** Paste messaging: install once at user scope. Reload, Customize, product-repo `/plan`. Do not copy into each app. Cloud is a different section.

**If they want a list (A5).** Send them to the list. One sentence: Work Kit is a loop, not a catalog.

**If they only ran the CLI (A6).** "Customize, User, Work Kit card, then `/plan`. CLI alone is not this plugin."

**If they are Riley (A7).** Admin toggle or `~/.cursor/skills`. Do not book a pilot.

**If they ask for a demo (A4).** Terminal: install, three beats (after G3), `/plan`, `/review-diff`, `/ship` named files, log row. Do not demo Remotion slashes.

**Do not.** LinkedIn sequences, "AI coding for VP Eng," conference booths, Product Hunt. Those angles select A7 and A9.

---

## 8. What to learn in the next 10 conversations

We do not have ten customers. If leftover hours run problem interviews (F17), cap at 8 Avery-like ICs ([recruitment](../research/first-delivery-recruitment.md)). Do not delay WK-1 for this list.

Learn, in order:

1. After they install a skill or plugin, what do they type first in the next sitting?
2. If README numbered step 3 said `/plan`, would they do it without a researcher? (Only after G3. Do not test the old echo and call it first delivery.)
3. When do they skip a plan on purpose (tiny) vs skip because chat is faster?
4. Have they copied `.cursor/` between repos, and did they hate the drift?
5. Did `npx skills add` ever make them think slashes existed when they did not?
6. Cloud: did a run look empty because sync was skipped? (Quota: 2 of 8 Casey-like.)
7. Teams: empty Customize? (Quota: at most 1 of 8. Do not fill the panel with Riley.)
8. `/ship` vs `git add .`: have they shipped leftovers or `.env`?
9. Would they be disappointed if `/plan` through `/ship` vanished? (31 Dec question, not a 15 Oct KPI.)
10. Did they stop at the plugin card because copy told them to?

**Do not "learn" from fake calls.** Owner diary is n=1 and excluded from the 5 to 8. Session log is the conversion instrument for A1. Fill a row before hunting accounts.

---

## Sharpness check

| Fuzzy (fail) | Sharp (this file) |
| --- | --- |
| B2B AI startups, 20-200 engineers | One IC, this machine |
| PLG with expansion revenue | $0 README |
| Economic buyer = VP Eng | Avery buys with hours |
| 10 named logos | 1 human + 9 archetypes |
| Outreach sequences | No outbound this quarter |
| ICP = anyone using Cursor | Anyone using Cursor is C1, the competitor |

**Decision.** Do not expand ICP until G3 passes, the log has rows, and 31 Dec is not a miss. Next work is still [WK-1](../tickets/wk-1-g3-install-copy.md), not a target-account list.
