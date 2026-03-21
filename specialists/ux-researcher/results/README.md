# UX Researcher Results Log

This directory stores real-world outcomes from applying GTeam UX research recommendations.
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
- **Research method:** [user interviews / usability testing / survey / diary study / A/B test / other]
- **Product area:** [onboarding / core workflow / navigation / checkout / settings / other]
- **Participant count:** [number of participants and recruitment source]
- **Starting position:** [e.g. pre-design, pre-launch, post-launch redesign, feature validation]

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

- **Decision influenced:** was a product or design decision changed as a direct result of this research? (yes / no / partial)
- **Recommendation adoption rate:** percentage of prioritised recommendations that were implemented within one quarter.
- **Time-from-research-to-decision:** days between research report delivery and a documented product decision that cited the research.
- **Usability improvement:** task completion rate or time-on-task before vs. after implementing recommendations (where measurable).

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
