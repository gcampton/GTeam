## The Three Pricing Axes

Every pricing decision operates on three independent axes. Solve them in this order — axis 1 mistakes can't be fixed by axis 2 or 3.

**Axis 1 — Pricing Metric (what you charge for)**
The unit of value. This is the most important decision in pricing.

| Metric type | Examples | Best for |
|-------------|----------|----------|
| Per seat / per user | Slack, Notion, HubSpot | Collaboration tools where value scales with team size |
| Usage-based | Stripe (% of revenue), Twilio (per message), AWS (per GB) | Infrastructure, APIs, tools where consumption = value |
| Outcome-based | % of revenue saved, % of churn prevented | High-trust enterprise; hard to operationalise |
| Feature-gated flat fee | Most SaaS | Products where all users get similar value |
| Hybrid | Seats + usage overages | When both team size and consumption correlate with value |

**Choosing the right metric — the Value Metric Test:**
1. Does the metric scale with the value the customer receives? (more seats = more value)
2. Can the customer understand it immediately? (if you have to explain it, reconsider)
3. Does it allow customers to start small and expand? (land-and-expand model)
4. Does it align your incentives with customer success? (you grow when they grow)

Load: Read `~/dev/1_myprojects/gteam/specialists/pricing-strategy/references/value-metrics.md`

**Axis 2 — Packaging (what's included in each tier)**
Feature allocation across tiers. Most companies get this backwards by putting the best features in the highest tier — this rewards big buyers but punishes activation.

Rules for packaging decisions:
- Core value features go in the entry tier (users must experience the "aha moment" to convert)
- Collaboration and admin features go in mid/upper tiers (these scale with team size)
- Compliance, security, and SLA features go in enterprise (these are enterprise buying criteria)
- Power user features can go in any tier based on who uses them most

**Packaging audit:** For each feature, ask: "Who uses this? When do they discover they need it? What happens to retention if we gate it?"

Load: Read `~/dev/1_myprojects/gteam/specialists/pricing-strategy/references/tier-design.md`

**Axis 3 — Price Points (the actual dollar amounts)**
Set after axes 1 and 2 are decided. Price points should be set using research, not gut feel or cost-plus.
