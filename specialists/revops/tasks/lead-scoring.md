## Lead Scoring Model

Lead scoring = fit score + engagement score. Both matter. A perfect-fit lead who never engages is less valuable than a strong-fit lead who's actively researching.

**Fit Scoring (firmographic / demographic)**

Score based on ICP match. Define ICP first, then assign points:

| Dimension | Strong fit (10 pts) | Moderate fit (5 pts) | Poor fit (0 pts) |
|-----------|---------------------|----------------------|------------------|
| Company size | [Your ICP range] | Adjacent range | Too small / too large |
| Industry | Target verticals | Adjacent verticals | Out-of-scope |
| Job title / seniority | Economic buyer or champion | Influencer | End user / intern |
| Geography | Target markets | Secondary markets | Excluded markets |
| Tech stack (if applicable) | Uses [complementary tool] | Neutral | Uses [competing tool] |

**Engagement Scoring (behavioural)**

Score based on recency-weighted engagement:

| Action | Points | Decay |
|--------|--------|-------|
| Pricing page visit | 15 | 50% after 14 days |
| Demo request | 25 | No decay |
| Trial signup | 20 | 50% after 30 days |
| Case study download | 10 | 50% after 30 days |
| Webinar attendance | 12 | 50% after 30 days |
| Email click (x3 in 7 days) | 8 | 50% after 14 days |
| Blog post view | 2 | 50% after 7 days |
| Unsubscribe | -20 | Permanent |
| Competitor page visit (if tracked) | 15 | 50% after 7 days |

**MQL threshold:** typically 40–60 total points (fit + engagement). Set by looking at historical data: what was the average score of leads that converted to SQL? Set the threshold at ~80% of that average.

**Negative scoring:**
- Student/personal email domain: -15
- "Student" or "intern" in title: -10
- Country in exclusion list: disqualify entirely

Load: Read `~/dev/1_myprojects/gteam/specialists/revops/references/scoring-models.md`
