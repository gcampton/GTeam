# Pipeline Design & Hygiene Reference

## Opportunity Stage Definitions

### Standard B2B Sales-Led Pipeline

| Stage | Probability | Entry criteria | Exit criteria | Max age |
|-------|-------------|----------------|---------------|---------|
| **Discovery** | 20% | First call completed; pain confirmed | Champion identified; problem clearly defined; next meeting scheduled | 21 days |
| **Qualification** | 35% | MEDDPICC/BANT confirmed; decision process mapped | Economic buyer engaged or scheduled; timeline confirmed; no blockers to proposal | 30 days |
| **Proposal / POC** | 50% | Formal proposal sent OR proof-of-concept underway | Proposal acknowledged; evaluation criteria agreed; stakeholder map confirmed | 30 days |
| **Negotiation** | 75% | Legal/commercial terms under review | Verbal agreement on price and terms; legal in final review | 21 days |
| **Closed-Won** | 100% | Contract signed; payment initiated | — | — |
| **Closed-Lost** | 0% | Deal will not proceed this cycle | Loss reason logged (required field) | — |

### PLG/Self-Serve Upgrade Pipeline

| Stage | Probability | Entry criteria | Exit criteria |
|-------|-------------|----------------|---------------|
| **Expansion Identified** | 30% | PQA signal triggered; account over free tier limits | Sales/CS reaches out and confirms interest |
| **Expansion Engaged** | 50% | Champion responsive; upgrade path discussed | Quote sent or upgrade link opened |
| **Upgrade Won** | 100% | Payment confirmed | — |
| **Upgrade Lost** | 0% | Declined upgrade | Reason logged; re-engage cadence set |

---

## MEDDPICC Qualification Framework

For enterprise deals (ACV > $25K), ensure each element is confirmed before moving to Proposal.

| Letter | Element | Question to answer | Where to record in CRM |
|--------|---------|--------------------|------------------------|
| **M** | Metrics | What is the quantified business impact of solving this problem? | Opportunity "Business Case" field |
| **E** | Economic Buyer | Who controls the budget and has final authority? Have we spoken with them? | Contact role: Economic Buyer |
| **D** | Decision Criteria | What criteria will they use to evaluate solutions? | Opportunity "Evaluation Criteria" field |
| **D** | Decision Process | What is the step-by-step process to reach a signed contract? Who approves each step? | Opportunity "Decision Process" notes |
| **I** | Identify Pain | What is the quantified cost of the problem? What happens if they don't solve it? | Opportunity "Pain" field |
| **C** | Champion | Who internally will fight for your solution? Do they have access to the economic buyer? | Contact role: Champion |
| **C** | Competition | What alternatives are they evaluating? What do they prefer about each? | Opportunity "Competitors" field |

**MEDDPICC deal health scoring:** Score each element 0 (unknown) / 1 (partial) / 2 (confirmed). Total out of 14. Deals below 8 should not advance to Proposal.

---

## Pipeline Velocity Formula

Pipeline velocity tells you how much revenue per day moves through your pipeline.

```
Pipeline Velocity = (# of Opportunities × Win Rate × Average Deal Size) ÷ Sales Cycle Length (days)
```

Example: 50 opps × 30% win rate × $10,000 ACV ÷ 60 days = $2,500/day in pipeline velocity

**How to use it:**
- Falling velocity = pipeline problem before it shows in revenue
- Rising velocity = either better deals or shorter cycles (identify which)
- Compare velocity by segment, rep, and source channel to find the highest-leverage interventions

---

## Hygiene Rules

### Mandatory fields by stage

| Field | Required at | Notes |
|-------|-------------|-------|
| Opportunity Name | Creation | "[Company] — [Product/Tier]" format |
| Amount / ARR | Discovery | Estimate acceptable; must be updated at Qualification |
| Close Date | Creation | Must be a future date; auto-flag if past-due |
| Stage | Always | — |
| Next Step | Always | Specific action + date; no "TBD" |
| Champion Contact | Discovery | Cannot advance to Qualification without |
| Economic Buyer Contact | Qualification | Cannot advance to Proposal without |
| Loss Reason | Closed-Lost | Required field; blocks stage transition if empty |

### Auto-alerts (configure in CRM)

| Condition | Alert trigger | Recipient | Action |
|-----------|--------------|-----------|--------|
| Stage unchanged for 21 days | Daily check | AE + Manager | Flag with "Stuck" tag; manager review |
| Close date in the past, opp still open | Daily check | AE + Manager | Email with link; if 3+ days past due, manager creates task |
| Amount field empty after Discovery | On stage transition to Qualification | AE | Block stage change until field is filled |
| Loss reason empty | On Closed-Lost creation | AE | Required field; pop-up prompt |
| No activity logged in 14 days | Daily check | AE | Task to log next activity |

### Weekly pipeline review checklist (Manager)

- [ ] Opportunities with no next-step date updated this week
- [ ] Opportunities past expected close date
- [ ] Opportunities in same stage for >21 days
- [ ] Close date changes from this week — are they pushes? Understand root cause.
- [ ] Opportunities added this week vs. target
- [ ] Total weighted pipeline vs. quota coverage target (goal: 3–4× remaining quarter quota)

---

## Pipeline Coverage Benchmarks

| Coverage ratio | Interpretation |
|---------------|---------------|
| < 2× quarterly quota | Under-covered — pull in deals from later quarters or accelerate current |
| 2–3× quarterly quota | Low but manageable — focus on conversion rate improvement |
| 3–4× quarterly quota | Healthy — standard benchmark for most B2B SaaS |
| 4–5× quarterly quota | Strong — allows for normal deal slippage |
| > 5× quarterly quota | Either over-projected or deals are too old — audit for stale opps |

**Weighted vs. unweighted pipeline:**
- **Unweighted** (sum of all opportunity values): simple but misleading if win rates vary by stage
- **Weighted** (each opp value × stage probability): more accurate; use this for coverage calculations
- **Commit** (AE-marked as "will close this quarter"): highest confidence; use for CEO/board forecasting

---

## Loss Analysis

The most underused RevOps practice. Structured loss analysis runs quarterly and identifies systemic patterns.

**Loss categories (required field in CRM):**

| Category | Definition | Action |
|----------|------------|--------|
| Chose competitor: [Name] | Lost head-to-head to a specific alternative | Competitive battlecard update; feature gap review |
| No budget | Real budget constraint, not a negotiating tactic | Timing re-engage in 6 months; check if FY budget cycle |
| No decision / status quo | Chose to do nothing or stay with current solution | Messaging review — value prop not compelling enough |
| Wrong timing | Genuine timing issue (reorg, freeze, other priority) | 90-day re-engage sequence |
| Product gap | We couldn't meet a requirement | Product team notification; assess urgency |
| Price | We were more expensive than they were willing to pay | Pricing review; assess whether discount would have won it |
| Poor fit | We shouldn't have created this opportunity | Scoring model review; ICP clarification |
| Ghosted | No response after ≥3 follow-ups | Review if champion was the right contact |

**Quarterly loss review agenda (30 minutes):**
1. Review top 3 loss reasons by volume
2. Are any patterns emerging (one competitor winning repeatedly? specific feature gap?)
3. Are there deals we should have disqualified earlier?
4. Update ICP and scoring model if needed
5. Action items assigned
