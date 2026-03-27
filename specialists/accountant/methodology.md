### Financial Review

**Gather:** Financial documents (P&L, balance sheet, bank statements, invoices, spreadsheet — whatever is available). Identify: period, entity type, currency.

**Use Grep to search `references/financial-review-checklist.md` for relevant categories as needed.** Work through:

1. Cash flow — runway, burn rate, cash conversion cycle
2. Revenue recognition — timing, deferred revenue, refunds
3. Expense categorisation — misclassified items, personal vs business
4. Tax exposure — VAT/GST obligations, payroll tax, corporation tax provisions
5. Reconciliation gaps — bank vs books, accounts receivable vs invoices
6. Unusual items — one-off costs, related-party transactions
7. Key ratios — gross margin, net margin, current ratio, debt-to-equity (check `references/key-ratios.md` for benchmarks)

**Surface to user only when:** a material discrepancy, significant tax exposure, or solvency concern is found.

**Deliver:**
- Financial health summary (one paragraph)
- Issues table (item → severity → recommended action)
- Corrected figures or journal entries where appropriate
- Questions requiring user clarification (numbered list)

---

### Bookkeeping Cleanup

**Gather:** Accounting software used (Xero, QuickBooks, Wave, spreadsheet), period to clean, chart of accounts if available, bank statements.

**Cleanup process:**

1. **Chart of accounts audit:**
   - Named clearly? Merge duplicates.
   - Standard structure present: Revenue → COGS → Gross Profit → OpEx → EBITDA → Financing
   - Remove accounts with zero activity for 12+ months

2. **Transaction categorisation sweep:**
   - Classify all uncategorised transactions
   - Consistent category for recurring vendors (e.g. AWS → always "Cloud Infrastructure")
   - Personal expenses in business account — flag each; confirm reimbursement or reclassify
   - Split transactions covering multiple categories

3. **Bank reconciliation:**
   - Opening balance matches bank statement
   - All transactions present, no duplicates
   - Reconciling items documented (outstanding cheques, timing differences)

4. **Accounts receivable cleanup:**
   - Invoices > 90 days overdue — flag for write-off consideration or collections
   - Credit notes matched against invoices
   - Deferred revenue recognised correctly

5. **Payroll check:**
   - Payroll journal entries match actual payroll runs
   - Employer NI / FICA / super contributions accrued correctly

**Deliver:**
- Cleaned chart of accounts structure
- List of transactions requiring owner decision (categorise / reimburse / write off)
- Reconciliation summary by bank account
- Material errors found + corrected journal entries

---

### Tax Planning & Compliance

**Gather:** Entity type (sole trader, Ltd, LLC, S-corp, etc.), jurisdiction(s), financial year end, last filed return, approximate revenue and profit, major transactions expected.

**Check `references/tax-calendar.md` for jurisdiction-specific deadlines.**

**Tax health check:**

1. **Filing status** — all returns filed on time? Penalties outstanding?
2. **VAT / GST / Sales tax:**
   - Registered in correct jurisdictions (economic nexus thresholds)?
   - Input tax claimed correctly?
   - Reverse charge applied for cross-border services?
3. **Corporation / Income tax:**
   - Profit estimate → estimated tax liability for current year
   - R&D tax credits applicable? (UK RDEC, US R&D credit)
   - Loss carry-forward position?
4. **Payroll taxes:**
   - PAYE / withholding filed and paid on time?
   - Director loans — interest charge required?
   - Benefits in kind reported?
5. **Planning opportunities:**
   - Expense timing to shift profit between years
   - Pension contributions (tax deductible)
   - Asset purchase timing (capital allowances / Section 179)
   - Dividend vs salary split for owner-directors

**Deliver:**
- Tax liability estimate for current period
- Filing calendar with deadlines for next 12 months
- Top 3 planning opportunities with estimated tax saving
- Records needed for next return

---

### Budget & Forecast

**Gather:** Historical P&L (ideally 12 months), headcount plan, major known costs, revenue assumptions or targets, forecast period (quarterly / annual).

**Budget build:**

1. **Revenue forecast:**
   - Bottom-up: units × price × conversion rate, or MRR × growth rate
   - Three scenarios: conservative / base / optimistic
   - Seasonal adjustments from prior year actuals

2. **COGS:**
   - Direct costs as % of revenue (baseline from prior year actuals)
   - Per-unit COGS for product businesses
   - Gross margin target vs industry benchmark

3. **Operating expenses — by department:**
   - Headcount: current salary + planned hires (month-by-month)
   - SaaS & tools: current + planned subscriptions
   - Marketing: budget as % of revenue target
   - Fixed overheads: rent, insurance, professional fees

4. **Cash flow projection:**
   - Convert P&L to cash (add back D&A, adjust for working capital movements)
   - Identify lowest cash point — when is the trough?
   - Funding required if cash goes negative

5. **KPI targets:**
   - Set monthly targets: ARR/MRR, CAC, LTV, gross margin, burn rate, runway

**Deliver:**
- 12-month P&L forecast (three scenarios)
- Monthly cash flow projection with runway calculation
- KPI target table with monthly milestones
- Assumptions log (every number has a stated assumption behind it)

---

### Financial Modelling & KPI Analysis

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
