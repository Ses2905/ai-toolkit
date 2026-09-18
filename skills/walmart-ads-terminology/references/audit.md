# Terminology Audit

Read this when reviewing existing material — a flow, a spec, a help center, a
set of screenshots, an export — for terminology drift.

The goal is not a list of inconsistencies. It is a ranked, decidable set of
findings, because an unranked list of forty nits gets skimmed and dropped.

## How to run one

**1. Fix the scope and say what it was.** One flow, one document set, one
surface. Name it in the output, including what you could not see — a reader
must know whether "no findings in the API docs" means clean or unexamined.

**2. Extract terms before judging them.** List every term that names a product,
surface, object, metric, audience, control, or state. Judging as you read makes
you notice the jarring ones and miss the quiet ones.

**3. Compare against the registry, then against itself.** Two failure modes,
and the second is more common: drift *from* canon, and drift *within* the
material where no canon exists yet.

**4. Rank by advertiser impact, not by frequency.** A wrong term on the budget
field beats twelve wrong terms in a footer. Rank by whether the term is load-
bearing for a decision the advertiser is making.

## Severity

Use the consequence to the advertiser, not the size of the edit.

| Severity | Test |
|---|---|
| **Blocking** | An advertiser could make a wrong money decision, or cannot complete a task |
| **High** | Same object named differently across surfaces they use in one sitting |
| **Medium** | Internal or system vocabulary leaking into advertiser-facing copy |
| **Low** | Inconsistent capitalization, pluralization, or house style |

Sort Blocking and High to the top and resist padding the list — findings below
Medium can be summarized as a count rather than enumerated.

## Output

```
# Terminology audit: <scope>

**Reviewed.** <what you looked at>
**Not reviewed.** <what you could not see, and why it matters>

## Findings

| # | Severity | Term as used | Where | Should be | Why it matters |
|---|---|---|---|---|---|

## Patterns
<2–4 root causes. Individual findings are symptoms; this is the section
that changes anything.>

## Open terminology questions
<Terms with no canonical answer — each one is a decision, with an owner.>

## Recommended sequence
<What to fix now, what to batch into the next release, what needs a
decision first. Not everything is worth fixing immediately.>
```

The **Patterns** section is what makes the audit worth commissioning. Forty
findings that all trace to "the reporting team named columns independently of
the campaign team" is one organizational problem with one fix, and reporting it
as forty separate nits hides that.

Name structural causes — ownership gaps, missing canon, teams working from
different sources — not the people who wrote the strings.
