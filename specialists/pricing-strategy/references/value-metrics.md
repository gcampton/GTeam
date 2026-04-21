# Value Metric Selection Guide

## What Is a Value Metric?

The value metric is the unit you charge for — the dimension of your product that scales with the value customers receive. It determines how customers grow their spend with you as they extract more value.

The value metric is axis 1 of the three pricing axes because it's the hardest to change later. Getting this wrong means customers either hit a pricing wall (and churn) or outgrow the need to pay more (and you leave money on the table).

## The Value Metric Test

Before selecting a metric, apply all four tests:

1. **Does it scale with value?** As the customer extracts more value, does the metric go up? If a customer doubles their revenue using your tool, should they pay more? If yes, can your metric capture that?

2. **Is it immediately understandable?** "Per active user" and "per GB stored" are understood instantly. "Per workflow run" or "per API call" requires explanation — factor in the education cost.

3. **Does it enable land-and-expand?** Small customers should be able to start at a low spend and grow without re-purchasing. If the metric jumps in large increments, it's a barrier to entry.

4. **Does it align your incentives with customer success?** If you charge per user, you're incentivised to increase adoption. If you charge per GB stored, you're incentivised to help customers store more. Ask: "What behaviour does this metric incentivise?" Is that the behaviour your customers want?

## Metric Types

### Per Seat / Per User
**Charge for:** Number of active users in the account.

Best for: Collaboration tools, productivity software, anything where value scales with team adoption.

Variants:
- **All seats:** charge for every account member — simple but punishes companies for adding users
- **Active seats:** charge only for users who logged in within the billing period — friendlier, more complex to track
- **Named seats:** assign specific users to seats — simplest billing, creates friction around user swaps

Risks: Seat-based pricing can discourage broad adoption ("we'll share one login to save costs"). Address with per-seat price drops at volume tiers.

Examples: Slack, Notion, Figma (per editor), HubSpot, Salesforce

### Usage-Based (Consumption)
**Charge for:** Volume of a specific action or resource (API calls, emails sent, records processed, GB stored, transactions processed).

Best for: Infrastructure, developer tools, transactional services, anything where consumption varies widely across customers and correlates directly with value delivered.

Variants:
- **Pay-as-you-go:** no committed spend; complete flexibility; lower initial commitment
- **Committed use + overages:** customer commits to a base volume and pays overage rates above it; gives you predictable revenue while customers get a discount for commitment
- **Credits:** pre-purchase credits at a discount; simpler for customers to understand and budget

Risks: Revenue unpredictability; customers may optimise to reduce usage rather than increase value; support burden on billing disputes.

Examples: Stripe (% of transaction), Twilio (per message), AWS (per GB), OpenAI (per token), Snowflake (per compute unit)

### Flat Fee (Feature-Gated)
**Charge for:** Access to a feature set, not a unit of usage or number of users.

Best for: Tools used by a fixed team with predictable usage; products where value is binary (you either have the feature or you don't); early-stage products before usage patterns are understood.

Risk: Doesn't capture value growth. A company that doubles its revenue using your tool pays the same as one that gets marginal value. This leaves expansion revenue on the table.

Examples: Most legacy SaaS (a fixed monthly fee per tier)

### Outcome-Based
**Charge for:** A percentage of the value delivered (revenue generated, cost saved, churn prevented).

Best for: High-trust enterprise relationships, services with measurable ROI, products that have direct causal impact on a customer metric.

Risk: Very hard to operationalise. Requires attribution agreement, measurement infrastructure, and trust. Usually reserved for services engagements, not pure software.

Examples: Rewardful (% of referred revenue), some professional services firms, performance marketing agencies

### Hybrid Models
Many mature SaaS products combine two metrics:

| Pattern | Example | When to use |
|---------|---------|-------------|
| Seats + usage | Intercom (seats + message volume) | When both team size and consumption correlate with value |
| Flat + overage | Mailchimp (list size base + overage) | Lock in a base commitment, capture upside |
| Free tier + usage | Twilio, SendGrid | Developers start free, pay as they scale |
| Seats + platform fee | Many enterprise tools | Platform fee for access, seats for scale |

Hybrid is more complex to explain. Introduce it only if the simpler alternatives fail the Value Metric Test.

## Selection Guide by Product Type

| Product type | Recommended metric | Why |
|-------------|-------------------|-----|
| Team collaboration / productivity | Per seat (active) | Value scales with adoption |
| CRM / sales tools | Per seat or per contact | Both correlate with deal volume |
| Email marketing | Per subscriber or per email sent | Value scales with audience |
| Analytics / BI | Per seat or per data volume | Depends on whether analysis or storage is the bottleneck |
| Developer tools / APIs | Per usage unit | Wide usage variance; developers expect pay-as-you-go |
| E-commerce / marketplace | % of GMV or per transaction | Revenue-aligned; scales with customer success |
| Data enrichment / leads | Per record or per credit | Clear unit of value |
| AI / LLM tools | Per token, per query, or per seat | Depends on use case variability |
| Project management | Per seat | Team adoption = value |
| Vertical SaaS (niche industry) | Per unit of core domain object (e.g. per property for real estate, per patient for healthcare) | Closest to value metric for the domain |

## Red Flags

**The metric you chose punishes success:** If growing customers are incentivised to reduce usage to save costs, you've picked the wrong metric. Example: charging per database record means customers delete data rather than pay more.

**The metric is invisible to the buyer:** If the economic buyer can't see what's driving the bill, they'll dispute it. Usage metrics need a live dashboard showing current consumption vs. plan limits.

**The metric requires a new billing system you don't have:** Don't choose usage-based if your billing infrastructure can't track the unit reliably. Billing mistakes erode trust faster than almost anything else.
