# Pilot and LOI: Work Kit (refuse paid design partners)

**Us.** Sarah Scherer. Work Kit (`work-kit`), personal MIT Cursor plugin. Repo [Ses2905/cursor-skills](https://github.com/Ses2905/cursor-skills). Not a company.
**Them.** No prospect company. ICP is Avery on this machine ([ICP](../messaging/work-kit-icp.md)). If a champion forwards a request for a team pilot, they are Riley-shaped until proven otherwise. Disqualify as primary.
**Pain.** Install can succeed while the next sitting starts in chat with no plan. Live G3: step 3 is still optional cloud sync.
**Proposed pilot (the only one we run).** Internal first delivery: patch copy, then one product-repo `/plan` and named-file `/ship`, logged. Not a multi-seat trial.
**Length.** One sitting for copy (under 2 hours). Go-live window 15 Oct 2026 if G1-G4 pass. Not a 6-week paid engagement.
**Success metrics.** G3 binary. One log row with `entry` plan or tiny and `ship` named files. Not NPS. Not seats activated.
**Pricing.** $0. MIT. No discounted seats. No full price.
**Resources from "them."** From Avery: a product repo, git, Cursor desktop, dest writable. From a company: none. We do not take their data, SSO, or admin time.
**Legal.** No MSA. No DPA. MIT LICENSE already governs the code. A paid SOW would be a different product we have not chosen to be.
**Related:** [ICP](../messaging/work-kit-icp.md), [Diligence](q4-2026-diligence-qa.md), [GTM](q4-2026-first-delivery-gtm.md), [WK-1](../tickets/wk-1-g3-install-copy.md)
**Source prompt:** [Pilot LOI proposal](https://aiuxplayground.com/prompts/pilot-loi-proposal) (AI UX Playground)

Decision: do not close design partners this quarter. If someone asks, send section 7 email B. If Sarah asks herself, run section 3 internal timeline. Do not sign section 5b.

---

## Filled prompt (no empty brackets)

| Field | Value |
| --- | --- |
| Company | None. Owner Sarah. |
| Prospect | Internal Avery. External: none named. |
| Problem | Wrong install finish line. Loop unlogged. |
| Scope | WK-1 copy plus one logged sitting. No team rollout. |
| Weeks | 0 billed weeks. Calendar: now to 15 Oct for phase 1. |
| Outcomes | G3 pass. Log row. Secrets not in the push. |
| Pricing | Free forever under MIT. Not a trial that converts. |
| From them | Machine + git. No PII dump. No production tenant. |
| MSA / DPA | No. Refuse. |

---

## 1. One-page proposal (forwardable)

**Title.** Work Kit is not a design-partner program. Here is what a person can do instead.

**What it is.** A once-per-machine Cursor plugin. After reload, Customize should show Work Kit. Then open a product repo and run `/plan` (or `/debug` if something is already broken). Review the real diff. `/ship` named files. Do not copy the plugin into each application repo.

**What it is not.** A billed pilot. A 10-seat rollout. A replacement for Continual Learning or a GitHub skill list. A reason to wait on legal.

**Who should try it.** A solo IC who owns the machine, ships with git weekly, and can run `./scripts/install-local.sh`. Who should not: a team that needs Allow Local Plugin Imports from an admin before anything shows, a group that wants the kit vendored in app git, or a buyer who needs an MSA.

**How to try (E1).**

```bash
git clone https://github.com/Ses2905/cursor-skills.git
cd cursor-skills
chmod +x scripts/*.sh
./scripts/install-local.sh
```

Then: Developer, Reload Window. Customize, filter User, confirm Work Kit. Open a product repo and `/plan`. (After WK-1, those three beats will match the script. Today step 3 in stdout is still optional cloud sync. Do not run a "pilot" against that echo and call it first delivery.)

**What we will not do for you.** Dedicated Slack. Weekly QBR. Custom SSO. Putting your logo on a slide. Signing a pilot SOW. Holding a kickoff while G3 is red.

**Ask.** If you match Avery: clone and try after G3, or now if you will ignore live step 3 and still `/plan`. If you need a contract: this is the wrong kit. Forward this page as the no.

**Owner.** Sarah Scherer. Support is README FAQ. There is no CSM.

---

## 2. Success criteria and measurement

### Internal Avery sitting (the real pilot)

| Criterion | Pass if | Instrument |
| --- | --- | --- |
| G3 | Script echo and both README lists: step 3 is `/plan` or `/debug` if broken. No `Optional for Cloud Agents` as item 3 | `git grep`, MT-1 |
| G1/G4 adjacent | `/review-diff` on the copy change. No secrets | Diff + git status |
| Loop | One product-repo sitting: `entry` = plan or tiny, named-file `/ship` | `docs/okrs/session-log.md` |
| E1 time | Clone to Customize visible, twice, 10 minutes or less (US-2, after copy) | Log `minutes_install` |

Fail: plugin card visible, no `/plan`. Fail: paid invoice. Fail: n seats.

### External person who clones anyway

We do not measure them. No telemetry. If they email, count "questions README already answers" (target 0 after week +1 of a go-live). That is comms, not a pilot KPI.

### What we will not score

Activated seats, time-to-value in a CRM, NPS, expansion ARR, "champion score."

---

## 3. Timeline with checkpoints

### Track I. Internal (do this)

| When | Checkpoint | Owner | Exit |
| --- | --- | --- | --- |
| Next sitting | WK-1 copy in `install-local.sh` and README | Sarah | G3 grep clean |
| Same day if possible | Product-repo `/plan`, `/review-diff`, `/ship`, log row | Sarah | Row not blank |
| 8 Oct 2026 | SLC gate | Sarah | Yellow G3 = slip 15 Oct |
| 15 Oct 09:00 | Phase 1 go/no-go | Sarah | No-go if G1-G4 fail |
| 22 Oct | Week +1 log check | Sarah | If KR2 still 0, do not add channels |
| 14 Nov | Casey path, not a customer pilot | Sarah | Checker before cloud runs |

### Track II. External paid (do not schedule)

No kickoff. No week 2 readout. No week 6 convert-to-annual. If a calendar invite appears, decline.

---

## 4. Commercial terms (3 options)

All three are $0 or a refusal. There is no paid ladder.

**Option A. MIT self-serve (default).** Price $0. Term: perpetual under LICENSE. They clone. We owe no implementation hours. They owe no data. Convert-to-paid: never, unless we build a different product.

**Option B. Friend paste (A4).** Same as A. Sarah may paste Template A from comms if a human asks. Still $0. No SLA. No logo rights.

**Option C. Paid pilot / discounted seats / full ACV.** Not offered. If they insist, the answer is no. Do not negotiate 50% off of a list price that does not exist. Do not offer "free for 6 weeks then $X per seat."

A champion who needs a table for procurement:

| | A Self-serve | B Friend paste | C Paid pilot |
| --- | --- | --- | --- |
| Price | $0 | $0 | Not offered |
| Seats | 1 machine | 1 machine | n/a |
| MSA | No | No | Would be required. We still say no |
| DPA | No. We do not process their employee data | No | No |
| Success fee | None | None | None |

Pick A. B only if asked. Never C this quarter.

---

## 5. Paperwork

### 5a. Internal LOI (non-binding, Sarah to herself)

Not a legal instrument. A go/no-go note.

- Parties: Sarah (operator) and this repo.
- Intent: ship G3 copy, then log one Plan to Ship before 15 Oct, or slip the date.
- Not a commitment to Marketplace, cloud as Avery step 3, or interviews as a gate.
- Termination: any sitting can stop. Rollback is `install-local.sh` from a known-good SHA.
- Confidentiality: product-repo secrets stay out of this repo. `/ship` named files only.

### 5b. Paid pilot SOW outline (do not send)

If legal asks for a SOW, do not fill their template with Work Kit as the SOW. Outline of why it fails:

- Statement of work would imply deliverables we do not staff (onboarding, custom skills, weekly calls).
- Fees, payment, and limitation of liability assume an entity. There is none.
- Data processing: we do not host their code. Cursor does. A DPA with Sarah is the wrong vendor.
- Use this sentence instead: "Work Kit is MIT software on GitHub. Clone it. There is no SOW."

---

## 6. Risks and de-risking

| Risk | If we ran a team "pilot" | De-risk (actual) |
| --- | --- | --- |
| G3 still red | They measure old copy and call it UX | Do not invite testers until G3. WK-1 first |
| Teams empty Customize | Pilot "fails" for policy we do not own | Disqualify Riley as primary. Recovery FAQ only |
| They vendor C6 | Drift, support, fights user-scope | README forbids copy into each app |
| Secrets in their push | They blame the kit | Skill forbids `.env`. We do not watch their git |
| Scope creep to catalog | We become C3 | Three beats only |
| MSA delay | Hours die in legal | Refuse MSA. MIT is the paper |
| Logo / case study | Fake social proof | GTM: no press. n=0 interviews |
| Paid terms | Implies a company | Diligence section 0: not raising, not selling |

De-risk for the internal sitting: `/review-diff`, no `.agents/` dump, log the row, slip 15 Oct if G3 yellow.

---

## 7. Emails

### Email A. Internal (Sarah, calendar note to self)

Subject: Next sitting is WK-1, not a partner pilot

Body:

Work Kit has no design partners to close. Next sitting: edit `scripts/install-local.sh` and README so step 3 is `/plan`. Then one product-repo `/plan` and `/ship`. Log the row. Do not draft an LOI for a company. If 8 Oct is still yellow, slip 15 Oct.

### Email B. Champion who asked for a paid pilot (send this)

Subject: Work Kit is MIT. There is no pilot contract

Body:

Thanks for asking. Work Kit is a personal Cursor plugin under MIT. I am not running paid pilots, design-partner seats, or an MSA this quarter.

If you are a solo IC who owns your machine and git: clone https://github.com/Ses2905/cursor-skills and run `./scripts/install-local.sh`. After reload, Customize, User should show Work Kit. Then open a product repo and `/plan`. Do not copy the plugin into each app repo. Cloud Agents need a separate sync path. Teams seats may block local plugins. I cannot fix that with a contract.

If you need a vendor, a DPA, or ten seats on a timeline, this is the wrong kit. Please forward that to procurement so they stop waiting on me.

I will not schedule a kickoff. README is the offer.

Sarah

### Email C. Friend who just wants to try (optional)

Subject: How I install Work Kit

Body:

Clone the repo. Run `./scripts/install-local.sh`. Reload. Confirm Work Kit under Customize, User. Then `/plan` in a product repo, not in the kit checkout. Free. No form. If Customize is empty on Teams, ask admin for Allow Local Plugin Imports, or use `~/.cursor/skills`.

---

## How to use this file

- Champion at a company: email B plus section 1.
- Sarah: email A plus [WK-1](../tickets/wk-1-g3-install-copy.md).
- Legal: section 5b no, LICENSE yes.
- Do not attach a pricing sheet. Next product work is still G3 copy, not a pilot close.
