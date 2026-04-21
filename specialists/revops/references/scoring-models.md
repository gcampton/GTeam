# Lead Scoring Model Reference

## Architecture: Fit + Engagement

Every scoring model has two components. Use both — neither alone is sufficient.

**Fit score** (who they are): firmographic match to your ICP. Static or slowly-changing. Answers: "Is this the right type of person/company?"

**Engagement score** (what they've done): behavioural signals showing intent. Dynamic — decays over time. Answers: "Are they actively considering buying?"

**MQL threshold:** typically fit score + engagement score ≥ [40–60 points]. Calibrate against historical data: what was the average combined score of leads that became customers?

---

## Fit Scoring Dimensions

Customise point values based on your ICP. These are starting defaults.

### Company Fit

| Dimension | Strong (10 pts) | Moderate (5 pts) | Weak (0 pts) | Negative |
|-----------|----------------|-----------------|--------------|---------|
| Company size (employees) | [Your ICP range] | ±50% of ICP | <25 or very large | Specific excluded sizes: -10 |
| Industry / vertical | Primary ICP verticals | Adjacent verticals | All others | Explicitly excluded industries: -15 |
| Revenue/ARR (if known) | [ICP range] | ±50% | Outside range | — |
| Geography | Target markets | Secondary markets | Tier 3 | Excluded countries: -20 |
| Tech stack signals | Uses [complementary tool] | Neutral stack | Uses [direct competitor] | Competitor user: -5 (still worth nurturing) |

### Contact Fit

| Dimension | Strong (10 pts) | Moderate (5 pts) | Weak (0 pts) | Negative |
|-----------|----------------|-----------------|--------------|---------|
| Job title / seniority | Economic buyer or champion title | Influencer / adjacent | End user | Student/intern: -15 |
| Department | Primary buying department | Adjacent department | Unrelated | — |
| Decision-making role | Decision maker confirmed | Likely influencer | Unknown | — |
| Email domain | Business email matching company | — | Personal email (gmail, yahoo) | Personal email: -10 |

---

## Engagement Scoring Actions

Points should reflect buying intent — a pricing page visit signals far more intent than a blog post view.

### High-intent actions (25–30 points)
| Action | Points | Notes |
|--------|--------|-------|
| Demo request | 30 | Immediate MQL regardless of score |
| Trial signup / free account creation | 25 | Start nurture clock |
| "Contact sales" form | 30 | Immediate MQL |
| Pricing page visited ≥3 times in 7 days | 25 | Strong purchase intent signal |
| Free trial active for 7+ days | 20 | Product engagement = retention signal |

### Medium-intent actions (8–15 points)
| Action | Points | Notes |
|--------|--------|-------|
| Pricing page first visit | 15 | Researching |
| Case study or customer story download | 12 | Validation-seeking |
| Webinar attendance (live) | 12 | Active engagement; higher than recorded |
| ROI calculator used | 15 | Intent signal |
| Comparison page viewed ("/vs-[competitor]") | 15 | Late-stage evaluation |
| Integration page viewed | 10 | Technical evaluation |
| Product tour or demo video watched >50% | 12 | — |

### Low-intent actions (2–5 points)
| Action | Points | Notes |
|--------|--------|-------|
| Blog post viewed | 2 | Awareness |
| Email opened | 1 | Weak signal; don't weight heavily |
| Email clicked | 4 | Meaningful; shows interest in that topic |
| Webinar registration (not attended) | 3 | Intent exists; attendance is higher signal |
| Resource/template download | 5 | Research stage |
| Social follow | 2 | Brand awareness |

### Negative scoring (subtract points)
| Action | Points | Notes |
|--------|--------|-------|
| Email unsubscribe | -30 | Remove from all marketing sequences |
| Spam complaint | -50 | Remove and flag |
| Job title is student/intern | -15 | Low conversion probability |
| Personal email domain | -10 | Harder to qualify; lower intent |
| Visited careers page (not product pages) | -5 | May be job-seeking, not buying |

---

## Score Decay

Engagement scores should decay over time — a pricing page visit from 6 months ago is less relevant than one yesterday.

**Standard decay schedule:**
| Action tier | Decay rate | After |
|-------------|-----------|-------|
| High-intent actions | 50% decay | 30 days |
| Medium-intent actions | 50% decay | 14 days |
| Low-intent actions | 50% decay | 7 days |
| All scores | Reset to 0 | 180 days of inactivity |

Most marketing automation platforms (HubSpot, Marketo, Pardot) support score decay. If yours doesn't, manually recalculate scores monthly.

---

## MQL Threshold Calibration

**Empirical approach (best):**

1. Pull the last 6 months of leads that became customers (closed-won)
2. Calculate their score at the time of MQL conversion
3. Find the median score → that's your MQL threshold
4. Set the threshold at 80% of that median (you want to include leads that are slightly below the "average winner" profile)
5. Review quarterly: if SDR acceptance rate (SAL/MQL) drops below 60%, the threshold is too low; if it's above 85%, you may be being too conservative

**If you have no historical data:**

Start with MQL threshold = 40 (a combination of any fit score + some engagement). Adjust after 3 months based on SDR feedback. SDRs who are calling low-quality leads will tell you immediately.

---

## Lead Score Tier Labels (for CRM tags)

Use these labels to route and prioritise:

| Score | Label | Action |
|-------|-------|--------|
| 60+ | **Hot** | Immediate SDR follow-up (same business day) |
| 40–59 | **MQL** | SDR review within 4 business hours |
| 25–39 | **Warm** | Add to active nurture sequence |
| 10–24 | **Nurture** | Long-cycle nurture sequence |
| <10 | **Cold** | No active outreach; retain for re-scoring |

---

## Model Maintenance

- **Monthly:** Review MQL→SQL conversion rate. If below 30%, scoring is too permissive. If below 20%, rebuild the model.
- **Quarterly:** Recalibrate thresholds against closed-won data from the past quarter.
- **Annual:** Re-examine fit dimensions — has the ICP shifted? New verticals opened? New competitor signals to track?
- **After product changes:** If you launch a new feature or change onboarding, update the engagement scoring actions to reflect the new activation path.

**Model drift warning signs:**
- SDRs complain about lead quality consistently
- MQL→SQL rate declining quarter-over-quarter
- CAC rising without market changes
- Marketing and sales teams disagree on what counts as a "good" lead
