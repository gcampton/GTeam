## Financial Modelling & KPI Analysis

**Gather:** Business model type (SaaS, e-commerce, marketplace, services), available data (revenue, cohorts, CAC, churn, margins), specific questions to answer.

**Model types by business:**

| Business type | Key model | Critical metrics |
|--------------|-----------|-----------------|
| SaaS | ARR bridge, cohort LTV | MRR, churn rate, NRR, CAC payback |
| E-commerce | Unit economics | AOV, repeat rate, LTV, contribution margin |
| Marketplace | GMV model | Take rate, liquidity, CAC both sides |
| Services | Utilisation model | Billable hours, blended rate, utilisation % |

**SaaS metrics — calculate from raw data:**
- **MRR** = sum of all active subscription monthly values
- **ARR** = MRR × 12
- **Churn rate** = churned MRR ÷ starting MRR (monthly)
- **NRR** = (starting MRR + expansion − contraction − churn) ÷ starting MRR
- **CAC** = total sales & marketing spend ÷ new customers acquired
- **LTV** = ARPU ÷ monthly churn rate
- **LTV:CAC** = should be > 3:1; payback period < 12 months
- **Burn multiple** = net burn ÷ net new ARR (< 1.5 is efficient)

**Cohort analysis:**
- Group customers by acquisition month
- Track retention (% still active) at 1, 3, 6, 12 months
- Calculate cumulative revenue per cohort
- Identify: which cohorts retain best? What changed when retention improved?

**Deliver:**
- Completed model (table or structured format)
- Key metric summary with benchmark comparisons
- 3 business insights derived from the data
- Recommendations: where to focus to move the most important metric
