## Lead Lifecycle Design

The lifecycle is the spine of RevOps. Every other system (scoring, routing, reporting) depends on having clean, agreed-on stage definitions.

**Standard B2B lifecycle stages:**

| Stage | Owner | Definition | Entry criteria | Exit criteria |
|-------|-------|------------|----------------|---------------|
| Subscriber | Marketing | Opted into marketing communications | Email opt-in | Any qualifying activity |
| Lead | Marketing | Showed any interest signal | Form fill, content download, webinar registration | Meets MQL criteria |
| MQL | Marketing | Marketing-qualified, ready for sales review | Lead score threshold OR behaviour trigger | SDR accepts → SQL; SDR rejects → recycle |
| SAL (Sales Accepted Lead) | Sales | SDR has reviewed and accepted for outreach | SDR marks accepted within SLA | First meeting booked or disqualified |
| SQL | Sales | Sales-qualified: confirmed budget, authority, need, timeline (BANT or MEDDPICC subset) | Discovery call completed, qualified | Opportunity created |
| Opportunity | Sales | Active deal in pipeline | Opp created in CRM | Closed-won or closed-lost |
| Customer | CS | Paying | Payment received | Churn or expansion event |
| Churned | CS | Cancelled | Cancellation confirmed | Re-engage or archive |

**For PLG motions — product-qualified additions:**

| Stage | Definition | Entry |
|-------|------------|-------|
| PQL (Product-Qualified Lead) | Free/trial user who hit activation signal | Reached aha moment (product-defined) |
| PQA (Product-Qualified Account) | Account with multiple active users or usage spike | ≥3 seats active, or usage >80% of free tier limit |

**Stage definition rules:**
- Each stage must have unambiguous entry criteria (if two people would disagree, redefine)
- Each stage must have a single owner (marketing owns through MQL; sales owns from SAL)
- No stage can last more than 30 days without an escalation rule
- Disqualification must put the lead into a specific recycle stage, not limbo

Load: Read `~/dev/1_myprojects/gteam/specialists/revops/references/lifecycle-stages.md`
