# Recruitment Results Log

This directory stores real-world outcomes from applying GTeam recruitment recommendations.
Over time these results are used by the `gteam-learn` job to upgrade reference file
confidence levels and revise advice that doesn't hold up in practice.

---

## How to log a result

Copy the template below into a new file named `YYYY-MM-DD-brief-description.md`.
Be specific — vague entries ("it worked") don't help future calibration.

```markdown
# [Strategy Name] — [Month YYYY]

**Reference file:** [which file in references/ this relates to]
**Section:** [which section/recommendation was tried]

## Context
- **Role type:** [engineering / sales / operations / design / executive / other]
- **Company stage:** [seed / Series A / Series B / growth / enterprise]
- **Team size:** [number of people in the hiring team at time of hire]
- **Starting position:** [e.g. new role, backfill, urgent hire, executive search]

## What was tried
[Describe exactly what you did, following which recommendation]

## Result (after X weeks)
- [Metric]: [before] → [after]
- [Metric]: [before] → [after]

## What worked
[Specific observations about what drove the positive result]

## What didn't work
[Specific observations about what failed or had no effect]

## Recommendation update
- [ ] Reference advice is correct as-is — mark as [TESTED]
- [ ] Reference advice needs revision — describe what should change
- [ ] Reference advice is wrong for this context — describe the exception
```

---

## Key metrics to track in result entries

- **Time-to-hire:** days from job opening to offer accepted. Benchmark: 30–45 days for most roles; 60–90 days for executive.
- **Offer acceptance rate:** offers made vs. accepted. Benchmark: 85%+ overall; 90%+ for roles with strong employer brand.
- **90-day retention:** percentage of hires still employed at 90 days. Benchmark: 90%+.
- **Cost-per-hire:** total recruiting spend (sourcing, tools, agency fees, referral bonuses) / number of hires.
- **Interview-to-offer ratio:** candidates who reached interview stage vs. offers made. Benchmark: 3:1 to 5:1.

---

## Confidence level system

Reference files use these markers on recommendations:

| Marker | Meaning |
|--------|---------|
| `[HYPOTHESIS]` | Best-practice advice, no real-world results yet |
| `[TESTED: YYYY-MM-DD]` | Confirmed by at least one result entry |
| `[REVISED: YYYY-MM-DD]` | Originally hypothesis, updated based on results |
| `[CONTEXT: ...]` | Applies only in specific conditions |

The `gteam-learn` job reads this directory and proposes changes to reference files
based on accumulated results. Run it periodically to keep references current.
