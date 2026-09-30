---
name: practice-plan-creator
description: Design a sport-specific practice session with timed drills, warm-up, skill work, scrimmage, and cool-down. Use when the user asks to plan a practice, build a training session, or pick drills for a team or athlete by sport, skill level, and time available.
metadata:
  source: https://app.mcpmarket.com/ses2905/skills/practice-plan-creator
  mcpmarket-version: 1.0.0
---

# Practice Plan Creator

Design an effective practice session with drills, timing, and progression matched to the sport, skill level, and time available.

## Activate When

- The user asks to "plan a practice", "build a training session", or "what drills should we run"
- The user names a sport plus a team, age group, or skill level
- The user needs a timed session outline with a warm-up and a cool-down

## Required Context

Ask only for what is missing; otherwise assume and state the assumption.

- **Sport** and the skill focus (for example, defense, passing, conditioning)
- **Skill level or age group** (beginner, intermediate, advanced; youth or adult)
- **Total time** and number of athletes
- **Space and equipment** available

## Process

1. Fix the session goal: one or two skills to improve, not five.
2. Split the total time into blocks: warm-up, skill work, game-speed work (scrimmage), cool-down.
3. Choose drills that fit the level. Progress from isolated reps to pressured, game-like reps.
4. For each drill give name, duration, setup, coaching points, and one way to make it easier or harder.
5. Check that the blocks sum to the total time and that equipment and space are realistic.

## Output

```markdown
# Practice Plan: {sport}, {level}, {total minutes} min

**Goal**: {one line}

| Block | Minutes | Drill | Setup | Coaching Points | Easier / Harder |
| --- | --- | --- | --- | --- | --- |

## Recommendations
{what to repeat, what to progress next practice}
```

## Definition of Done

- Block times add up to the stated total
- Every drill is runnable with the stated space, equipment, and headcount
- The session ends with a cool-down and a next-practice suggestion
- Assumptions about level, space, or equipment are listed
