# Paid Media Results Log

This directory stores real-world outcomes from applying GTeam paid media recommendations.
Over time these results are used by the `gteam-learn` job to upgrade reference file
confidence levels and revise advice that doesn't hold up in practice.

---

## How to log a result

Copy the template below into a new file named `YYYY-MM-DD-brief-description.md`.
Be specific — vague entries ("it worked") don't help future calibration.

```markdown
# [Strategy Name] — [Month YYYY]

**Reference file:** [which section of methodology.md this relates to]
**Section:** [Account Audit / Paid Search / Paid Social / Creative Strategy / Tracking & Measurement]

## Context
- **Platform:** [Google Ads / Microsoft Ads / Meta / LinkedIn / TikTok / blended]
- **Industry:** [e-commerce / SaaS / lead gen / local / B2B / other]
- **Monthly spend:** [e.g. $5,000 / $50,000 / $500,000]
- **Campaign type:** [search / shopping / Performance Max / social prospecting / retargeting / other]

## What was tried
[Describe exactly what you did, following which recommendation]

## Result (after X weeks)
- **CTR:** [before] → [after]
- **CPC:** [before] → [after]
- **ROAS:** [before] → [after]
- **CPA:** [before] → [after]
- **Conversion rate:** [before] → [after]
- **Impression share:** [before] → [after]
- [Other relevant metric]: [before] → [after]

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
