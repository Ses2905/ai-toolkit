# Naming Rules

Read this when naming a feature, surface, metric, audience, control, or state.

A name is a product decision with a long tail. It reaches UI, docs, training,
support macros, sales decks, and advertiser habit — and each of those makes the
name more expensive to change. Spend real effort here, once.

## What to produce

Never hand back a single name. A lone name invites a yes/no reaction and hides
the reasoning. Produce **two or three genuinely different candidates**, then:

```
## Recommendation: <name>

<One sentence: what this thing is, in advertiser language.>

| Candidate | Reads as | Cost / risk |
|---|---|---|
| <name> ★ | ... | ... |
| <name> | ... | ... |
| <name> | ... | ... |

**Why this one.** <2–3 sentences tied to the tests below.>
**Rejected.** <What each loser was testing, and what killed it.>
**Collisions checked.** <Existing registry terms this could be confused with.>
**Decision needed from.** <Who owns this — naming is rarely one person's call.>
```

Recording what the rejected candidates were *testing* matters more than
recording that they lost. Six months on, someone will propose one of them
again, and the note is what prevents relitigating it from scratch.

## The tests a name has to pass

Apply in order. A name that fails an early test is not rescued by passing later
ones.

**1. Would an advertiser say it out loud?**
Names come from the advertiser's vocabulary, not our system architecture. If it
describes how we built the thing rather than what it does for them, restart.

**2. Does it survive being said with no context?**
Names get repeated in a hallway, a support call, a sales pitch. If it needs its
own sentence of explanation to be understood, it is a description, not a name.

**3. Is it distinct from everything in the registry?**
Check `registry.md` before proposing. Near-collisions are worse than obvious
ones, because nobody notices them until both terms are in production and
advertisers are conflating them.

**4. Does it stay true when the thing grows?**
Names scoped to today's implementation break on the next release. A name tied
to one channel, one format, or one surface will be wrong the moment the
capability spans two. Prefer what it *does for the advertiser* over where it
currently lives.

**5. Does it belong to a family?**
If it sits beside existing things, it should be parallel with them in
grammatical form and specificity. Mismatched siblings are the most common
source of the fragmentation advertisers feel — the objects seem unrelated
because their names are shaped differently.

**6. Can it be said plainly in other languages and markets?**
Puns, idioms, and internal in-jokes do not survive localization or a global
sales team.

## Patterns that consistently fail

- **Internal project codenames escaping into the product.** They carry no
  meaning for advertisers and quietly signal that the product was built
  for us.
- **Adjective-led names** (*Smart*, *Advanced*, *Enhanced*, *Pro*). They
  promise a quality rather than naming a thing, they age badly, and they force
  the next tier into a worse name.
- **Names that describe the technology** (*engine*, *platform*, *service*,
  *framework*) on an advertiser-facing surface.
- **Reusing a word already doing a job** — the fastest way to make two
  different objects feel like one broken object.
- **Names that only make sense next to their competitor's name.** They date
  instantly and cede the frame.

## Renaming something that already shipped

Renaming is a migration, not an edit, and it is usually more expensive than it
looks. Before recommending one, say plainly what it costs: UI strings, API
fields, reporting columns, help content, saved advertiser workflows, training,
and the support backlog of people searching the old word.

Then make it a real decision rather than a silent swap:

- **State the trigger.** Rename when the current term actively misleads or
  blocks a capability — not because a better word exists.
- **Define the transition.** Both names visible, for a stated period, with a
  sunset date. Record it in the registry's `transition` field.
- **Retire the crutch on schedule.** "New name (formerly Old name)" left
  forever becomes permanent clutter and teaches advertisers that neither name
  is real.
