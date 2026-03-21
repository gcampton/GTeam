# Technical Writer Results Log

This directory stores real-world outcomes from applying GTeam technical writing recommendations.
Over time these results are used by the `gteam-learn` job to upgrade reference file
confidence levels and revise advice that doesn't hold up in practice.

---

## How to log a result

Copy the template below into a new file named `YYYY-MM-DD-brief-description.md`.
Be specific — vague entries ("it helped") don't help future calibration.

```markdown
# [Doc Type / Strategy] — [Month YYYY]

**Reference file:** [which file in references/ this relates to]
**Section:** [which section/recommendation was tried]

## Context
- **Doc type:** [API reference / tutorial / README / release notes / how-to guide]
- **Technical audience:** [beginner developers / experienced engineers / end users / mixed]
- **Product area:** [e.g. authentication, data pipeline, SDK, CLI]
- **Starting state:** [e.g. no docs, outdated docs, partial coverage]

## What was tried
[Describe exactly what you wrote or changed, following which recommendation]

## Result (after X weeks)
- [Metric]: [before] → [after]
- [Metric]: [before] → [after]

## What worked
[Specific observations about what reduced confusion or improved user outcomes]

## What didn't work
[Specific observations about what failed or had no measurable effect]

## Recommendation update
- [ ] Reference advice is correct as-is — mark as [TESTED]
- [ ] Reference advice needs revision — describe what should change
- [ ] Reference advice is wrong for this context — describe the exception
```

---

## Confidence level system

Reference files use these markers on recommendations:

| Marker | Meaning |
|--------|---------|
| `[HYPOTHESIS]` | Best-practice advice, no real-world results yet |
| `[TESTED: YYYY-MM-DD]` | Confirmed by at least one result entry |
| `[REVISED: YYYY-MM-DD]` | Originally hypothesis, updated based on results |
| `[CONTEXT: ...]` | Applies only in specific conditions |

---

## Key metrics to track

- **Support ticket reduction** — did the new or updated doc reduce inbound questions on the covered topic?
- **Time-to-first-success** — how long does it take a new user to complete the tutorial or make their first API call?
- **Doc page ratings** — thumbs up/down or star ratings on published pages; track change before and after rewrites

The `gteam-learn` job reads this directory and proposes changes to reference files
based on accumulated results. Run it periodically to keep references current.
