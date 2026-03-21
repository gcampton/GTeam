# Financial Review Checklist

> **Confidence:** All benchmarks are `[HYPOTHESIS]` (reasoned accounting best-practice) unless marked `[TESTED: context]`. Industry norms vary — adjust thresholds for the specific sector before advising.

Use this checklist systematically. Work top-to-bottom: cash flow first (survival), then revenue and expenses (accuracy), then balance sheet and reconciliations (completeness).

---

## Priority 1 — Cash Flow Analysis

**Survival depends on this. Do it first.**

### Runway Calculation

`[HYPOTHESIS]` Standard formula:

```
Runway (months) = Cash & Cash Equivalents / Average Monthly Net Burn Rate

Net Burn Rate = Total Cash Out − Total Cash In (for operating activities)
```

- [ ] Obtain last 3 months of bank statements or cash flow statements
- [ ] Calculate average monthly burn — do not use a single month (may be anomalous)
- [ ] Confirm what "cash" includes: petty cash, short-term deposits, overdraft facilities
- [ ] **Flag if runway < 6 months** — HIGH urgency
- [ ] **Flag if runway < 3 months** — CRITICAL; escalate immediately

### Cash Conversion Cycle (CCC)

`[HYPOTHESIS]` Formula:

```
CCC = Days Sales Outstanding (DSO) + Days Inventory Outstanding (DIO) − Days Payable Outstanding (DPO)
```

- [ ] Calculate DSO, DIO (if relevant), DPO — see `key-ratios.md` for formulas
- [ ] A rising CCC = cash is tied up longer = deteriorating position
- [ ] Negative CCC (e.g. subscription businesses, retail) = clients pay before you pay suppliers = cash-generative model — confirm this is genuine, not from delaying payables

### Cash Flow Statement Review

- [ ] Operating cash flow positive? — if negative while profit is positive, investigate working capital movements
- [ ] Investing cash flow: large capex? Acquisitions? Confirm these are discretionary or necessary
- [ ] Financing cash flow: new debt or equity? Loan repayments coming due?
- [ ] `[HYPOTHESIS]` Profitable but cash-poor = likely timing issue (deferred revenue, slow collections) — trace through AR and deferred revenue balances

---

## Priority 2 — Revenue Recognition Red Flags

**Incorrect revenue recognition distorts every downstream metric.**

- [ ] **Revenue recognised when earned, not when cash received** — check against contract milestones
  - Early recognition (booking revenue before delivery): HIGH financial misstatement risk
  - Deferred revenue understated relative to cash received: MEDIUM
- [ ] **Long-term contracts** — is percentage-of-completion or milestone method applied consistently?
  - `[HYPOTHESIS]` Under IFRS 15 / ASC 606: recognise revenue as (or when) performance obligations are satisfied.
  - Flag: lumpy revenue that exactly matches period-end targets — may indicate channel stuffing or pull-forward
- [ ] **Subscription / SaaS revenue** — is MRR recognised ratably over the subscription period?
  - Annual subscriptions received upfront: should be in deferred revenue; not all recognised on day 1
  - Check: deferred revenue balance growing proportionately with sales? If not, investigate
- [ ] **Refunds and returns** — is a returns provision set up? Revenue should be net of expected returns
- [ ] **Related-party revenue** — any transactions with connected parties at non-arm's-length prices?
  - `[HYPOTHESIS]` Flag any revenue from directors, shareholders, or entities connected to them — transfer pricing risk and potential misrepresentation
- [ ] **Consignment revenue** — goods on consignment should not be recognised as revenue until sale to end customer

---

## Priority 3 — Expense Categorisation

### Personal vs Business

`[HYPOTHESIS]` Common personal expenses incorrectly claimed as business:

| Expense Type | Personal Flag | Business OK | Ask |
|-------------|--------------|-------------|-----|
| Meals & entertainment | Personal meals, family dinners | Client entertaining with business purpose | Who attended? Was there a business purpose? |
| Travel | Holidays with work days attached | Genuine business travel | Itemised breakdown; was personal element separated? |
| Vehicle | Personal use of company car | Genuine business use | Mileage log; benefit-in-kind calculation |
| Home office | Entire home costs | Proportion attributable to workspace | Sq footage calculation; utility bills |
| Clothing | Regular clothing, even if "worn for work" | Protective/safety clothing, uniforms with logo | Can it be worn outside work? If yes, personal |
| Subscriptions | Netflix, personal software | Business software, professional journals | Is it used for business? |
| Mobile phone | 100% personal use | Genuine business use proportion | Split needed if dual use |

- [ ] Review T&E claims for personal elements — spot-check 3–5 large claims
- [ ] Check vehicle log / mileage claims — is benefit in kind calculated?
- [ ] Home office claim: confirm calculation basis (flat rate or apportioned actuals)

### Capital vs Revenue Expenditure

`[HYPOTHESIS]` Capital = creates enduring asset (> 1 year); Revenue = consumed in period.

- [ ] Large one-off payments: are they expensed (revenue) or capitalised?
  - Expensing capital items: overstates costs in current period, understates assets
  - Capitalising revenue items: understates costs in current period, overstates assets
- [ ] Software development costs: has the company capitalised development costs?
  - `[HYPOTHESIS]` Under IAS 38 / GAAP: development costs can be capitalised once technical and commercial feasibility established — research costs cannot. Mixed positions in practice.
  - Flag: large "capitalised development" line without clear feasibility evidence
- [ ] Repairs vs improvements: repair restores (revenue); improvement enhances beyond original (capital)
- [ ] Leasehold improvements: confirm correct amortisation period (shorter of lease term and useful life)

---

## Priority 4 — Balance Sheet Review

### Key Ratios to Calculate

See `key-ratios.md` for full formulas and thresholds. At minimum:

- [ ] Current ratio (current assets / current liabilities) — below 1.0 = liquidity concern
- [ ] Quick ratio (liquid assets / current liabilities) — below 0.8 = HIGH concern
- [ ] Debt-to-equity — rising trend more important than single snapshot

### Accounts Receivable (AR)

- [ ] AR ageing report — obtain breakdown by: current, 30, 60, 90, 90+ days overdue
  - `[HYPOTHESIS]` Concentration risk: if > 25% of AR is from one client, flag customer concentration
  - Growing 90+ day balances = bad debt risk; confirm bad debt provision is adequate
- [ ] Bad debt provision: is it based on historical collection rates, or just a fixed percentage?
  - No provision despite aged receivables = overstated assets = MEDIUM
- [ ] Related-party receivables — amounts owed by directors or connected parties?
  - `[HYPOTHESIS]` Flag immediately — may represent undisclosed loans or dividends

### Accounts Payable (AP)

- [ ] AP ageing report — are suppliers being paid within terms?
  - `[HYPOTHESIS]` Rapidly ageing AP can signal cash flow strain — the company is using trade credit as informal finance
  - Check for disputed invoices buried in AP
- [ ] Accruals complete? Expenses incurred but not yet invoiced should be accrued

### Deferred Revenue / Contract Liabilities

- [ ] Deferred revenue balance: does it match cash received for services not yet delivered?
  - Declining deferred revenue faster than revenue growth = catching up on old obligations or revenue pull-forward
- [ ] Check for "revenue clearing" or similar accounts that may obscure timing

---

## Priority 5 — Reconciliation Checks

**Every number should tie to an independent source.**

- [ ] **Bank reconciliation** — last period: does book cash match bank statement?
  - Outstanding items > 90 days: stale — investigate
  - Reconciling items that are round numbers: HIGH flag — may be plugs
- [ ] **AR per ledger vs invoice register** — do they agree?
  - Discrepancy: check for invoices booked but not sent, credits not applied, duplicate invoices
- [ ] **Payroll reconciliation** — gross payroll per P&L vs payroll system vs PAYE/payroll tax filings
  - `[HYPOTHESIS]` Discrepancy between payroll ledger and tax filings = compliance risk
- [ ] **VAT/Sales tax reconciliation** — output tax on sales per VAT return vs revenue × VAT rate
  - Persistent underpayment of VAT = liability building up = HIGH
- [ ] **Stock / inventory count vs ledger** (if applicable) — last count date? Discrepancy?

---

## Red Flags Table

| Symptom | Likely Issue | How to Verify |
|---------|-------------|---------------|
| Revenue growing but cash declining | Deferred revenue/AR timing, or losses masked by accrual accounting | Cash flow statement + AR ageing |
| Gross margin declining quarter-on-quarter | Cost increases not passed on, revenue mix shift, fraud in COGS | COGS breakdown; compare to prior periods |
| Large round-number journal entries at period end | Smoothing / manipulation | Request journal entry approvals + supporting docs |
| AR growing faster than revenue | Slow collections, fictitious invoices, revenue pull-forward | AR ageing + customer confirmation |
| Deferred revenue declining while cash increases | Revenue recognised too early | Recalculate recognition against contract terms |
| COGS spikes in one period | Inventory write-off, unbooked expenses lumped in | Stock records + purchase invoices |
| High director loans or inter-company balances | Cash extracted informally, transfer pricing issues | Board minutes + loan agreements |
| Persistent AP ageing | Cash flow stress, disputed suppliers | Cash position + creditor calls |
| Tax provisions < prior year on same profit | Tax planning or underestimation | Tax computation vs prior year |
| Payroll costs flat despite headcount growth | Ghost employees excluded from payroll, bonus accrual missing | Headcount schedule + payroll file |
