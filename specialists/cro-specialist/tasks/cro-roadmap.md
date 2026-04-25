## CRO Roadmap & Prioritisation

**Use when:** Building a quarterly CRO plan or prioritising a backlog of conversion experiments.

**Gather:** Current site conversion rate (overall and by key pages), traffic volumes, list of proposed changes or test ideas, development capacity available.

**CRO roadmap structure:**

**Step 1 — Audit and baseline:**
- Document current conversion rates for all key pages and funnel steps
- Calculate the value of a 1% improvement in conversion at each step (traffic × conversion delta × revenue per conversion)
- Identify the top 3 highest-value pages to focus on (impact × traffic)

**Step 2 — Hypothesis backlog:**

Score every test idea on PIE (1–10 each):
- Potential: how much lift is realistically possible?
- Importance: how much traffic and revenue flows through this element?
- Ease: how fast can this be built and deployed?

| Test ID | Hypothesis | Page | Potential | Importance | Ease | PIE Score |
|---------|-----------|------|-----------|------------|------|-----------|
| CRO-001 | [Hypothesis] | [URL] | 8 | 9 | 7 | 8.0 |

**Step 3 — Sprint planning:**

- Run 1–3 tests at a time (more dilutes traffic and extends runtimes)
- Sequence by PIE score; run quick tests (high ease) to build confidence data
- Reserve 20% of capacity for surprise fixes (technical issues found in recordings)

**Step 4 — Learning repository:**

After each test, log:
```markdown
Test: [ID and hypothesis]
Result: Win / Loss / Inconclusive
Lift: [+X% or -X% conversion]
Sample size: [N visitors per variant]
Confidence: [X%]
Learning: [Why this worked / didn't work — the insight for future tests]
Apply to: [Other pages where this learning is relevant]
```

Wins should be propagated across similar pages immediately. Losses are as valuable as wins if the learning is captured.

**Deliver:**
- Prioritised test backlog (PIE scores, ordered)
- 90-day CRO roadmap: test 1 → test 2 → test 3 with expected timelines
- Revenue impact forecast (conservative / optimistic at each lift level)
- Learning repository template for ongoing capture
