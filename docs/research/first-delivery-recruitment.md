# Recruitment plan: Work Kit first-delivery research

**Study:** Why Cursor ICs skip a plan-first loop after installing skills or plugins, and whether they can complete install then `/plan` from README copy.
**Product:** Work Kit (`work-kit`)
**Owner / researcher:** Sarah Scherer
**Method:** Problem interviews (n=5 to 8) plus optional usability of install copy after G3 is fixed. Owner diary is separate (session log, n=1).
**Related:** [Problem statement](../problem-statements/work-kit-first-delivery.md), [User flow](../user-flows/work-kit-first-delivery.md), [Session log](../okrs/session-log.md), [Beta survey](first-delivery-beta-survey.md), [Insights](first-delivery-insights.md)
**Source prompt:** [User research recruitment plan](https://aiuxplayground.com/prompts/user-research-recruitment-plan) (AI UX Playground)

This is discovery plus a short usability pass after G3. Sample size is 5 to 8 interviews, not a 100-person survey. Do not demo Work Kit on the call.

**Hypothesis to test (do not read it to participants).** Install can succeed while the next session starts in chat with no plan. Cloud skill sync is easy to skip.

---

## 1. Participant criteria

### Demographics

Do not screen on age, gender, or ethnicity. Screen on work context.

- **Location.** Remote OK. Time zone overlap with Sarah of at least 2 hours for a 45-minute call. Language: English for this round.
- **Job.** Ships software with git. Individual contributor or player-coach. Not a full-time recruiter or vendor selling research panels.
- **Environment.** Uses Cursor on desktop at least 3 days per week. Has access to a real repo they can talk about (no need to share private code).

### Behavioral characteristics

**Must have (Avery-like).**

- Commits to git at least weekly.
- Uses Cursor Agent or chat to change code, not only to ask questions.
- Has installed at least one Cursor skill, rule, plugin, or `npx skills add` package, **or** has copied `.cursor/` files between repos.

**Nice to have (quota).**

- 2 of 8: also use Cursor Cloud Agents (Casey-like).
- 1 of 8: Teams/Enterprise Cursor seat (Riley-like). Do not fill the whole sample with Riley. Avery is the primary segment.

**Experience level.** Mix of 3+ years shipping and people in the first year of agentic coding. Exclude people who have never shipped a commit.

### Inclusion

- Adults who consent.
- Can join a 45-minute remote call with screen share (usability) or audio-only (problem interview).
- Willing to describe a recent change they shipped with AI help.

### Exclusion

- Current Cursor employees (platform bias).
- People Sarah manages or who manage Sarah (power bias). Owner self-study stays in the session log, not in this n=5 to 8.
- People who cannot use git.
- People recruiting for a competing study this week if they will only pitch their tool.
- Anyone who needs to keep their entire workflow secret to the point they cannot answer "how did last Tuesday's change start."

### Number needed

| Cell | Completes | Screened backups |
| --- | --- | --- |
| Avery-like desktop ICs | 5 | 2 |
| Casey-like (also Cloud Agents) | 2 of those 5, or +2 if the first 5 have zero cloud | 1 |
| Riley-like Teams | at most 1 in the 5 to 8 | 1 |
| **Total interviews** | **5 to 8** | **2 to 3 backups** |
| Owner diary | 1 (Sarah), not counted in the 5 | n/a |

Stop at 5 if themes repeat. Do not go past 8 this round. Nielsen-style usability: 5 is enough to see install-copy failures. Problem interviews: 5 to 8 per the user-research skill.

---

## 2. Recruitment channels

**Primary (use).**

- Sarah's own network: people already on Cursor. Personal DM. Not a company-wide Slack blast that looks like a launch.
- GitHub: issues or discussions on `cursor-skills` only after G3 copy is public. Do not recruit on a README that still omits `/plan`.
- Existing teammates who clone the kit, if they are not in the exclusion list.

**Secondary (use lightly).**

- Cursor community forums: offer a research slot, not a product pitch. One post. No "we launched."
- Local or remote IC friends who match the behavioral bar.

**Do not use this round.**

- UserTesting / Respondent panels unless the $400 gift-card budget is approved. Default is $0 cash and network only.
- Product Hunt comments.
- Paying for ads.
- Intercept surveys in a product we do not own.

### Screening questions

Score: include if Q1-Q4 pass and Q5 is not "never." Cloud and Teams are quota, not auto-include.

1. In the last 7 days, on how many days did you use Cursor to change code? (0 / 1-2 / 3+)
2. In the last 30 days, did you `git commit` at least once? (yes / no)
3. Have you installed a Cursor skill, rule, plugin, or copied `.cursor` files between repos? (yes / no / not sure)
4. Are you employed by Cursor? (yes / no)
5. When you last used an agent to change code, how did the session start? (I wrote a plan first / I asked it to just implement / I pasted a ticket / I do not remember / I do not use agents that way)
6. Do you use Cursor Cloud Agents? (yes / no)
7. Is your Cursor seat personal, Teams, or Enterprise?
8. Time zone?
9. Can you do 45 minutes the week of [date]?

**Include if:** Q1 = 3+, Q2 = yes, Q3 = yes or not sure (probe), Q4 = no.

**Quota:** Q6 = yes for Casey cells. Q7 = Teams/Enterprise at most one complete unless you explicitly open a Riley study.

**Red flag:** Q5 = "I wrote a plan first" for *every* recruit. You would only talk to people who already do the loop. Aim for at least 3 of 5 who say they jump to implement.

### Incentive strategy

**Default track (network, $0).** Thank-you email. Optional: share a one-page findings note (no raw quotes without consent). Say unpaid in the first sentence of the invite.

**Paid track (if you open it).** $50 USD gift card per 45-minute complete. Cap 8 x $50 = $400. Pay after the call, within 7 days. Backups who are not scheduled: $0. No-shows: no pay. Partial calls under 20 minutes: $25 if they showed.

**Do not** offer equity, swag that looks like a launch, or "early access" to a waitlist that does not exist.

---

## 3. Recruitment materials

### Screening survey

Copy into a form (Google Form, Tally, or email). Title: Cursor workflow research (45 min)

**Intro (paste).**

You are not applying for a job. This is a 45-minute research call about how you start coding sessions in Cursor. Unpaid unless we emailed you a gift-card offer. We will not pitch a product for the first 30 minutes. You can stop at any time.

**Fields (paste).**

- Name
- Email
- OK to contact you about scheduling? (yes / no)
- Q1. In the last 7 days, on how many days did you use Cursor to change code? (0 / 1-2 / 3+)
- Q2. In the last 30 days, did you git commit at least once? (yes / no)
- Q3. Have you installed a Cursor skill, rule, plugin, or copied .cursor files between repos? (yes / no / not sure)
- Q4. Are you employed by Cursor? (yes / no)
- Q5. When you last used an agent to change code, how did the session start? (I wrote a plan first / I asked it to just implement / I pasted a ticket / I do not remember / I do not use agents that way)
- Q6. Do you use Cursor Cloud Agents? (yes / no)
- Q7. Is your Cursor seat personal, Teams, or Enterprise?
- Q8. Time zone?
- Q9. Can you do 45 minutes the week of [date]? (yes / no / maybe)

**Close (paste).**

If you match, Sarah will email 3 time slots. If you do not, you will get a short no. We will not add you to a marketing list. There is no marketing list.

### Recruitment email template

Subject: 45 min: how you start Cursor sessions (research)

Hi [Name],

I am doing a short study on how individual contributors start work in Cursor after they have installed skills or plugins. I am not selling anything on the call.

Looking for people who ship with git at least weekly and use Cursor most days. 45 minutes, remote. [Unpaid / $50 gift card].

If that is you, reply with: days you used Cursor last week, whether you use Cloud Agents, and two times that work next week.

Thanks,
Sarah

### Confirmation email (24 hours before)

Subject: still on for [day] [time]? (45 min, optional screen share)

Hi [Name],

Confirming 45 minutes on [day] at [time] [timezone]. Link: [calendar URL]

Screen share is optional. No product pitch in the first 30 minutes. Skip any question that hits confidential work. Do not share .env files or tokens if we do share a screen.

Consent text is below this email. Reply yes if you still want to do it, or send a time that works better.

Sarah

### Consent form (paste at start of call or send 24h before)

**Study title.** Cursor session-start research (Work Kit first delivery)

**Researcher.** Sarah Scherer. Personal project. Not on behalf of Cursor Inc.

**Purpose.** Learn how people start coding sessions with agents, and whether install instructions lead to a planned change or to immediate edits.

**What you will do.** 45-minute remote conversation. Optional screen share of Cursor and git (you choose what is visible). No need to show secrets or customer data. You may use a dummy repo.

**Risks.** Low. You might mention workplace practices. Skip anything confidential. Do not share `.env` or tokens on screen.

**Benefits.** None required. Findings may improve public docs on github.com/Ses2905/cursor-skills.

**Recording.** Default: notes only. Recording only if you say yes below. Recording stays on Sarah's machine. Deleted within 90 days after the study. Quotes in docs are anonymized unless you agree to a named quote.

**Voluntary.** You can skip questions or end the call. That will not affect any future use of Work Kit (MIT, free).

**Data.** Notes stored without your employer name if you prefer. Email used only to schedule and pay (if paid).

I agree to participate: yes / no  
I agree to recording: yes / no  
I agree to anonymized quotes: yes / no  
Name and date:

Researcher keeps a copy. Participant gets this text in email.

---

## 4. Timeline

**Recruitment duration.** 10 calendar days of outreach, then rolling schedule.

| Date | Activity |
| --- | --- |
| 17 to 19 Sep 2026 | Freeze screener. DM 10 Avery-like people. Do not post a launch. |
| 20 to 26 Sep | Screen replies. Book 5 completes plus 2 backups. |
| 22 Sep to 6 Oct | Problem interviews (current workflow). Can run **before** G3 copy fix. |
| 8 Oct | G3 due. If copy matches, start usability: E1 + `/plan` from README. |
| 8 to 14 Oct | Usability sessions (same people if willing, or 3 new). 45 min including install. |
| 14 Oct T-24 | Stop recruiting. Backups only if a 13 Oct cancel. |
| 15 Oct | Launch day. No research calls. |
| 22 Oct | Synthesis due with post-launch rewrite. |

If G3 slips, slip usability. Do not test the old script echo and call it first-delivery UX.

### Scheduling approach

- Offer 3 slots per person, 45 minutes, 15-minute buffer.
- One researcher. Max 2 interviews per day.
- Calendar: Sarah owns. Send a link with consent text.
- Confirmation email 24 hours before: "Still ok? Screen share optional. No product pitch in the first 30 minutes."
- For usability: they need a machine with Cursor and git. Send that in the invite.

### Backup participants

- Screen 2 extra Avery-like people. Do not book them until a complete cancels.
- Backup hold: "You are on the backup list for week of [date]. I will ping you only if a slot opens. You can say no."
- Replace a no-show after 10 minutes. Do not wait 30.
- If Casey quota is 0 after 5 Avery completes, recruit 2 cloud users in 27 Sep to 3 Oct. Do not delay the Avery 5 for Casey.

---

## Session mix (so recruitment matches the method)

**Problem interview (no Work Kit install required).** 35 min talk, 10 min optional reaction to the one-liner only. Do not walk them through `/plan` until G3 is fixed.

**Usability (after G3).** 10 min current workflow, 25 min: clone or open kit, follow README, reload, try `/plan` on a throwaway repo. 10 min debrief. Success: they attempt `/plan` without being told by the researcher. If you have to tell them, log that as a copy fail.

**Owner diary.** Session log. Not recruited. Do not mix Sarah's rows into the n=5 interview count.

---

## Bias notes (read before outreach)

- Do not recruit only people who already `/plan`. The problem is skippers.
- Do not pitch Work Kit in the screener.
- Do not pay more for "positive" quotes.
- Do not interview your reports.
- Stop at 8. More interviews will not replace G3 or an empty session log.
