# Go-to-market plan: Work Kit first delivery

**Product:** Work Kit (`work-kit`)
**Motion:** Make first delivery the default path. Plan, then ship named files. Cloud Agents load the same core skills.
**Owner:** Sarah Scherer
**GTM type:** Internal, owned-channel only. Not a paid, PR, or Product Hunt motion.
**Window:** 17 Sep 2026 through 12 Nov 2026 for phase 1 comms. Phase 2 cloud 14 Nov. Grade 31 Dec.
**Related:** [Messaging](../messaging/work-kit.md), [Comms](q4-2026-first-delivery-comms.md), [Checklist](q4-2026-first-delivery-checklist.md), [OKRs](../okrs/q4-2026-work-kit.md)
**Source prompt:** [Go-to-market strategy](https://aiuxplayground.com/prompts/go-to-market-strategy) (AI UX Playground)

Launch skill ORB: everything leads back to owned channels. Owned here is the GitHub README and the install script. Paid is $0. Earned is none. Community is none until the session log shows the loop.

---

## 1. Launch objectives

**Primary goal.** Adoption of the loop, not awareness, signups, or revenue. There is no signup funnel and no price.

**Secondary goal.** Clone visitors who follow README do not copy the plugin into each app repo. Cloud users sync skills before they burn a run.

**Non-goals.** Public GA. Waitlist. Ads. Press. Marketplace listing. Catalog dumps as "launch content."

**KPIs (same as Q4 O1 and O2).**

| KPI | Target | By |
| --- | --- | --- |
| Clean install to Work Kit visible | 10 minutes, timed twice | 31 Dec (first timing 15 Oct) |
| Logged sessions that `/plan` or tiny skip | 80% | 31 Dec |
| `/ship` of named files | 8 sessions | 31 Dec |
| Core skills present after sync | Checker passes | 14 Nov, then every sync |
| Cloud runs that load plan or debug | 6 | 31 Dec |
| Public posts claiming GA | 0 | Whole quarter |

**Timeline and milestones.**

| Date | Milestone | Owner |
| --- | --- | --- |
| 17 Sep 2026 | Session log template. Message freeze. | Sarah |
| 1 Oct 2026 | README and script next-steps draft. | Sarah |
| 8 Oct 2026 | SLC gate. Copy match. | Sarah |
| 15 Oct 2026 | Phase 1 go-live. First logged Plan to Ship. | Sarah |
| 22 Oct 2026 | Week +1 KPI check. | Sarah |
| 14 Nov 2026 | Phase 2 cloud path. | Sarah |
| 31 Dec 2026 | Grade. Disappointment question. | Sarah |

If O1 KR2 is still 0 at 22 Oct, do not add channels. Fix the log habit.

---

## 2. Target audience

**Primary segment.** Solo ICs who live in Cursor, want one quality bar across repos, and will run a shell script.

**Persona: Avery.** Desktop Cursor. Can clone and `./scripts/install-local.sh`. Needs the next change planned and shipped clean. Where they are: this machine, this GitHub repo, Cursor chat. Not a Slack community we run.

**Secondary: Casey.** Cloud Agents. Same person, different runtime. Where they are: Cursor Cloud. Message: local plugins do not mount. Sync `~/.cursor/skills/`.

**Secondary: clone visitor.** Finds `Ses2905/cursor-skills`. Needs E1 steps. Where they are: GitHub.

**Recovery: Riley.** Teams/Enterprise. Where they are: a company Cursor seat. Message: admin toggle or skills fallback.

**Where we will not hunt.** Product Hunt, Hacker News, LinkedIn, Twitter, paid Discord, conference booths. Wrong motion for a one-operator kit this quarter.

---

## 3. Launch channels

### Owned (use)

| Channel | Tactic | Owner | Date |
| --- | --- | --- | --- |
| GitHub README | One-liner plus three next steps, including `/plan` | Sarah | 8 to 15 Oct |
| `install-local.sh` echo | Identical three steps | Sarah | 8 to 15 Oct |
| `install-work-kit` skill | Cloud sync required for cloud work | Sarah | 13 Oct |
| Session log | Conversion tracking | Sarah | 8 Oct |
| Optional GitHub release notes | Template B in comms plan | Sarah | 15 Oct 15:00 |
| Teammate paste | Template A, only if a human asks | Sarah | As needed |

### Paid (do not use)

| Channel | Decision | Budget |
| --- | --- | --- |
| Search / social ads | Skip | $0 |
| Sponsorships | Skip | $0 |
| Product Hunt boosts | Skip | $0 |

Paid spend cannot buy Avery's `/plan` habit. It would also imply a public product we are not launching.

### Earned (do not use this quarter)

| Channel | Decision |
| --- | --- |
| PR / embargo | Skip |
| Influencers | Skip |
| Podcasts | Skip |
| Partner co-marketing | Skip |
| Comparison SEO pages | Skip until the loop is logged. Then maybe vs lists, with honest "best for." |

### Community (do not use this quarter)

| Channel | Decision |
| --- | --- |
| Cursor forum, Reddit, HN | Skip. Providing value in those places is fine later. Pitching this launch is not. |
| Social profiles | Skip. No thread. |

Revisit rented and borrowed only if 80% plan rate is in the log and Avery wants distribution. Gate is explicit.

---

## 4. Launch timeline

### Pre-launch (4 weeks before 15 Oct)

**Week -4 (17 Sep).** Create `docs/okrs/session-log.md`. Freeze the one-liner from the messaging framework. No channel expansion.

**Week -3 (24 Sep).** If a teammate exists, send Template A. Otherwise skip. Re-read `plan-the-work` and `ship-the-change`.

**Week -2 (1 Oct).** Draft README next-steps and script echo. Draft FAQ: empty Customize, cloud miss.

**Week -1 (8 Oct).** SLC gate. Make README and script echo identical. Confirm session log has a header row. Do not schedule social.

### Launch week (13 to 17 Oct)

**Mon 13 Oct.** `/review-diff` on README and script changes. Security pass: no `.env` in install copy.

**Wed 15 Oct.** Go-live script from the comms plan: reload, Customize, `/plan`, `/ship`, log the row, optional release notes. Stop at 16:00. No evening posts.

**Thu 16 Oct.** Optional 20 min Q&A if a teammate appeared.

**Fri 17 Oct.** First weekly check-in. Count sessions.

### Post-launch (4 weeks after)

**Week +1 (22 Oct).** KPI review. Plan rate. Ships. Recoveries.

**Week +2 (29 Oct).** One written "this session planned then shipped" note in the monthly OKR file. Not a public case study.

**Week +3 (5 Nov).** Prep sync checker and Casey checklist. Still no ads.

**Week +4 (12 Nov).** Mini retro. Go / no-go for 14 Nov cloud path. No-go if phase 1 log is empty.

Then phase 2 on 14 Nov sits outside this four-week GTM window on purpose. Cloud is a second launch, same message, different files.

---

## 5. Content strategy

**Launch announcement.** README plus optional GitHub release notes. Copy from [messaging](../messaging/work-kit.md). One-liner first. Three next steps. Cloud warning in the Cloud Agents section, not in the hero if it dilutes Avery.

**Blog posts and articles.** None. README is the article. Do not write "10 tips for agentic workflows."

**Social media content.** None. Calendar is empty. If a post appears, it is a process miss.

**Email campaigns.** None. One optional teammate paste. No sequence, no drip, no "day 3 onboarding."

**Other content that is in scope.**

- FAQ in README / `install-work-kit`
- Session log (the conversion artifact)
- Rollback Template D if copy confuses people

**Content that is out of scope.** Comparison hub, waitlist landing page, demo GIFs for PH, Navattic, sales deck, embargoed screenshots.

---

## 6. Budget allocation

**Money.** $0 paid media. $0 tools beyond GitHub and Cursor seats already in use. $0 agencies.

| Line | Amount | Note |
| --- | --- | --- |
| Ads | $0 | Skip |
| Sponsorships | $0 | Skip |
| Design / video vendor | $0 | Optional personal screen recording, not in repo if it shows private code |
| Product Hunt | $0 | Skip |
| Total paid GTM | $0 | |

**Time (the real budget).** One operator.

| Work | Hours (estimate) | When |
| --- | --- | --- |
| Session log + message freeze | 2 | Week -4 |
| README and script copy | 3 | Weeks -2 and -1 |
| Go-live session (plan to ship plus timing E1) | 4 | 15 Oct |
| Weekly check-ins | 0.25 each week | Ongoing |
| Sync checker + Casey dry-run | 4 | Before 14 Nov |
| Dirty-tree fixtures | 6 | By 15 Dec, not GTM week |

If time is short, cut fixtures after copy match, not the other way around. GTM for this product is the next-steps list and the log.

**Resources required.** Write access to `cursor-skills`. Cursor desktop. Optional second environment for Casey. No marketing hire. No CRM.

---

## Decision rules

- If someone asks "where do we advertise," the answer is we do not, this quarter.
- If someone asks "how do we get signups," there is no signup. There is clone plus install plus `/plan`.
- If someone asks "what is revenue GTM," there is none. MIT. Success is O1 and O2.
- If the log is empty on 22 Oct, this GTM plan pauses. Do not open a new channel to compensate.

That is the whole motion: owned README, identical script echo, counted sessions. Expand channels only after first delivery shows up in the log.
