# Board Room Strategy

Orchestrator for the 25-skill pack that takes a strategy question to a
board-ready deck. Invoke `/board-room-strategy` or a sibling (`/define-governing-question`,
`/recommendation-statement`, `/action-title-writing`, …).

Install with the rest of Work Kit:

```bash
./scripts/install-local.sh
./scripts/sync-user-skills.sh
```

Then **Developer: Reload Window**. Cloud Agents need **Settings → Agents →
Context and Tools → Sync Skills for Cloud Agents**.

## Stages

1. **Framing the mandate** — governing question, audience, SCQA, hypothesis, storyline
2. **Diagnostics and evidence** — issue tree, drivers, gap, benchmarks, so-whats
3. **Strategic choices** — options, priority, scenarios, tradeoffs, recommendation
4. **Execution planning** — roadmap, investment, risks, owners, metrics
5. **Narrative and communication** — action titles, data callouts, exec summary, hierarchy, Q&A

Each sibling is a `skills/<name>/SKILL.md` folder. The orchestrator is
`skills/board-room-strategy/SKILL.md`. Distinct from `/product-strategy-session`
(PM discovery) and `/plan-the-work` (engineering).
