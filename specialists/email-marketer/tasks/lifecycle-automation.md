## Lifecycle & Automation Map

**Gather:** Business model (SaaS, e-commerce, services), customer journey stages, existing automations if any, key user actions/events that can trigger emails.

**Core lifecycle automations to build:**

**E-commerce:**
1. Abandoned cart (1h, 24h, 72h) — recover lost revenue; 15% recovery rate typical
2. Post-purchase (Day 1: receipt, Day 3: how to use, Day 14: review request)
3. Win-back (90 days no purchase: re-engagement offer)
4. VIP / loyalty tier upgrade (trigger: hits spend threshold)

**SaaS:**
1. Trial onboarding (welcome → feature education → conversion — 7–10 days)
2. Feature adoption (trigger: user hasn't used key feature in 7 days)
3. Trial expiry warning (3 days before, 1 day before, day of)
4. Churn prevention (trigger: usage drops 50% from baseline — send check-in)
5. Expansion (trigger: approaching usage limit — upgrade nudge)

**Services / B2B:**
1. Lead nurture (content education sequence — 4–6 weeks)
2. Proposal follow-up (Day 1, Day 4, Day 8 after proposal sent)
3. Client onboarding (welcome, kickoff prep, check-in at 30 days)
4. Re-engagement (no contact in 6 months — catch-up email)

**Automation rules:**
- Always have an exit condition: if user converts, remove from nurture sequence
- Suppress paying customers from acquisition emails
- Cap frequency: no more than 1 automated email per day, regardless of triggers
- Review automations quarterly — stale copy and broken links cost more than they earn

**Deliver:**
- Lifecycle automation map (flow diagram in text/ASCII)
- Priority order: which 2–3 automations to build first and why
- Copy brief for each automation (objective, tone, key message, CTA)
- Trigger / exit condition spec for developer or ESP configuration
