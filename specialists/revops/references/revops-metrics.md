# RevOps Metrics Reference

## Metric Hierarchy

Report the right metrics to the right audience at the right cadence.

### Tier 1 — Board/Investor Level (monthly)
Track the health of the revenue engine at the highest level.

| Metric | Definition | Target (growth-stage) | How to calculate |
|--------|------------|----------------------|------------------|
| **New ARR** | New annual recurring revenue added this month (new logos only) | Growing MoM at your target growth rate | Sum of first-year contract values for new customers |
| **Expansion ARR** | ARR added from existing customers (upsell, cross-sell, seat expansion) | 20–40% of new ARR | Sum of ARR increases on existing customer accounts |
| **Churned ARR** | ARR lost from cancellations and downgrades | < GRR target equivalent | Sum of ARR lost from cancellations + downgrades |
| **Net Revenue Retention (NRR)** | (Starting ARR + Expansion ARR - Churned ARR) / Starting ARR × 100 | > 110% | See formula |
| **Gross Revenue Retention (GRR)** | (Starting ARR - Churned ARR) / Starting ARR × 100 | > 85% | Excludes expansion |
| **CAC (Blended)** | Total S&M spend / New customers acquired | Payback < 18 months | Include salaries, tools, paid ads, events |
| **LTV:CAC ratio** | Average LTV / CAC | > 3:1 | LTV = ARPU × Gross Margin % / Churn Rate |
| **Pipeline Coverage** | Total open pipeline value / Remaining quarter quota | 3–4× | — |

### Tier 2 — Revenue Leadership (weekly)
Track funnel conversion and operational health.

| Metric | Definition | Benchmark | Alert threshold |
|--------|------------|-----------|-----------------|
| **MQL Volume** | Leads reaching MQL stage this week | Your target | < 70% of target |
| **MQL→SQL Rate** | SQLs created / MQLs created | 40–55% | < 30% (scoring too loose) |
| **SQL→Opportunity Rate** | Opportunities created / SQLs | 70–85% | < 60% |
| **Opportunity→Close Rate** | Closed-won / Total closed | 25–35% | < 20% |
| **Average Sales Cycle Length** | Days from Opportunity creation to Closed-Won | 30–90 days (segment-dependent) | Rising trend |
| **ACV (Average Contract Value)** | Total new ARR / Number of new customers | Varies — monitor trend | Declining trend |
| **Pipeline Created (weekly)** | New opportunity value created | Weekly target by stage | < 80% of target |

### Tier 3 — Operational (daily / real-time)
Track process compliance and SLA adherence.

| Metric | Definition | Target | Alert |
|--------|------------|--------|-------|
| **Speed-to-Lead** | Minutes from demo request to first SDR outreach | < 5 minutes | > 30 minutes |
| **MQL SLA Compliance** | % of MQLs reviewed by SDR within 4 business hours | > 90% | < 80% |
| **CRM Completeness Score** | % of opportunities with all required fields complete | > 95% | < 85% |
| **Overdue Tasks** | Count of tasks past due date in CRM | 0 | Any AE with > 5 overdue |
| **Stuck Deals** | Opportunities in same stage for > 21 days | 0 | Any deals flagged |
| **Activity per Rep per Day** | Calls + emails + meetings logged by SDR/AE | [Rep-level target] | Consistently below target |

---

## Funnel Conversion Dashboard

Track the full funnel weekly. Every conversion rate should have a benchmark and a trend arrow.

```
Visitors
  ↓ [Visitor → Lead: target X%]
Leads
  ↓ [Lead → MQL: target X%]
MQLs
  ↓ [MQL → SQL: target X%]
SQLs
  ↓ [SQL → Opportunity: target X%]
Opportunities
  ↓ [Opp → Close: target X%]
Customers
  ↓ [Customer → Expanded: target X%]
Expanded Revenue
```

**Segment this funnel by:**
- Source channel (inbound / outbound / partner / PLG)
- Company segment (SMB / mid-market / enterprise)
- Rep (for coaching conversations)
- Product/use case (if multiple)

**How to read funnel data:**
1. Find the stage with the largest absolute drop in volume
2. That stage is your constraint — fixing it compounds throughout the rest of the funnel
3. Calculate the revenue value of a 5% improvement at each stage to prioritise investment

---

## Attribution Models

**First-touch attribution:** 100% credit to the channel that first brought the lead. Good for: understanding awareness effectiveness. Bad for: multi-touch journeys.

**Last-touch attribution:** 100% credit to the channel that closed the lead. Good for: understanding conversion drivers. Bad for: penalises awareness channels.

**Linear attribution:** Equal credit to every touchpoint. Good for: B2B with long sales cycles. Bad for: undervalues high-impact touches.

**Time-decay attribution:** More credit to recent touchpoints. Good for: long-cycle B2B where late-stage engagement matters most.

**Recommended for most SaaS:** Use first-touch for awareness reporting (what channels bring in new leads), last-touch for conversion reporting (what channels close deals), and linear for total pipeline attribution discussions.

---

## NRR / GRR Deep Dive

**Net Revenue Retention (NRR)** — the single most important metric for SaaS health.

```
NRR = (Starting MRR + Expansion MRR - Churned MRR - Contraction MRR) / Starting MRR × 100
```

| NRR | Interpretation |
|-----|---------------|
| > 130% | World-class (Snowflake, Datadog tier) |
| 110–130% | Excellent — growth from existing customers compounds significantly |
| 100–110% | Good — expansion outpaces churn |
| 90–100% | Fair — some expansion but churn is a concern |
| < 90% | Concerning — churn is destroying growth; fix retention before scaling acquisition |

**Cohort NRR analysis:** Calculate NRR for each quarterly cohort of customers. Improving NRR over time = product and CS improvements working. Declining NRR over time = product-market fit drifting or customer profile changing.

**Gross Revenue Retention (GRR)** — NRR without expansion. Measures pure churn.

```
GRR = (Starting MRR - Churned MRR - Contraction MRR) / Starting MRR × 100
```

GRR is always ≤ NRR. If GRR is high (>90%) but NRR is low, your expansion motion is broken. If GRR is low (<80%), retention is broken and expansion is masking it — a dangerous situation.

---

## Revenue Forecasting

**Commit-based forecast (most common):**

```
Monthly forecast = 
  Committed deals (AE-flagged "will close") × 90% confidence
  + Best-case pipeline × 50% confidence  
  + New business created this month × historical close rate
```

**Signal-based forecast improvements:**
- Weight deals by recency of activity (stale deals close less often than active ones)
- Weight deals by MEDDPICC score (well-qualified deals close at higher rates)
- Subtract deals past expected close date by 30+ days (they rarely close)
- Track forecast accuracy monthly: (Actual revenue / Forecast) × 100. Target: 85–115%.
