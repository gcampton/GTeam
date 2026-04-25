## Health Scoring

**Health score model — weight each signal:**

| Signal | Weight | Red | Amber | Green |
|---|---|---|---|---|
| Login frequency (weekly active users / licensed seats) | 25% | <30% | 30–60% | >60% |
| Feature adoption (core features used / total available) | 20% | <25% | 25–50% | >50% |
| Support ticket volume (tickets per user per month) | 15% | >3 | 1–3 | <1 |
| NPS / CSAT (last survey) | 15% | <6 NPS | 6–8 NPS | >8 NPS |
| Contract value (annual) | 10% | n/a | n/a | n/a (weight only) |
| Time since last CSM contact | 10% | >30 days | 15–30 days | <15 days |
| Renewal proximity | 5% | <60 days | 60–120 days | >120 days |

**RAG thresholds:** Score 0–40 = Red (immediate intervention), 41–70 = Amber (proactive outreach within 1 week), 71–100 = Green (monthly check-in sufficient).

**Weekly health review process:**
1. Pull updated scores every Monday morning
2. List all Red accounts — assign save calls within 48 hours
3. List Amber accounts with declining trend (score dropped >10 points week-over-week) — assign outreach within 5 days
4. Flag any Green-to-Amber transitions for CSM awareness
5. Prioritise by contract value within each tier
