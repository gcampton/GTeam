# SaaS Tier Design Reference

## The Good-Better-Best Architecture

Three tiers is the default for SaaS. The logic:
- **Two tiers** removes the anchor effect (nothing makes the paid tier look reasonable)
- **Three tiers** is the cognitive sweet spot — the middle option feels like the "sensible" choice
- **Four tiers** is acceptable for complex products with distinct market segments
- **Five or more tiers** causes decision paralysis and drops overall conversion

## Tier Roles

### Entry Tier (Free / Starter / Basic)
**Role:** Acquire, activate, demonstrate value, qualify for upgrade

The entry tier must include enough value to be genuinely useful standalone. If it's not useful on its own, it's not a real entry tier — it's a crippled product that trains customers to distrust you.

**What goes in Entry:**
- Core value feature (the thing that creates the "aha moment")
- Basic usage limits (not zero — customers need to experience value)
- Individual-use features (no collaboration or team features)

**What stays OUT of Entry:**
- Collaboration and admin features
- Reporting and analytics (beyond basic)
- Integrations (limit to 1–2 core ones)
- Priority support
- API access (unless your product is developer-tool based)

**Entry tier pricing options:**
- **Free (freemium):** works when the product has clear standalone value for free users and natural upgrade triggers. Requires high conversion rates to be sustainable (industry average: 2–5% free-to-paid).
- **Low price ($9–$29/mo):** filters out the lowest-intent leads; lower support burden than free; works well when the product requires significant setup.
- **Trial-only (no permanent free tier):** best when the product requires integration with customer systems and a permanent free tier would create support overhead.

### Recommended Tier (Pro / Growth / Professional)
**Role:** Target landing tier for 40–60% of paying customers. The anchor for the pricing page.

This tier defines your product's core value proposition. Customers who land here should feel they're getting full value — nothing important is withheld.

**What goes in Recommended:**
- Full individual value features (no meaningful limits for individual users)
- Collaboration features (multiple users, shared workspaces)
- Core integrations (your most popular 5–10)
- Standard reporting and analytics
- Standard support (email or chat)
- Reasonable usage limits (high enough that normal customers never hit them)

**Design rule:** The jump from Entry to Recommended should feel obvious for the customer who starts growing — triggered by usage limits, the need to invite a teammate, or the need to see better reporting.

### Pro/Business Tier (Business / Scale / Enterprise-lite)
**Role:** Anchor the price perception of the Recommended tier; serve power users and companies with compliance/governance needs.

**What goes in Business:**
- Unlimited (or very high) usage
- All integrations
- Admin controls (user management, permission levels)
- SSO (SAML or Google Workspace) — often the purchase trigger for IT-involved buying
- Advanced reporting and data export
- SLA-backed support (or priority support)
- Audit logs (security requirement for many enterprises)
- Custom branding (for client-facing tools)

**Price target:** 3–5× the Recommended tier price. The purpose is partly anchor pricing — it makes the Recommended tier feel like a bargain.

### Enterprise (Custom / Enterprise)
**Role:** Sales-assisted contracts for large accounts with custom needs.

Enterprise is not a tier in the traditional sense — it's a negotiated contract. Include it on the pricing page as "Contact us" to signal you serve large companies, but don't publish a price.

**What triggers Enterprise:**
- SSO / SAML required by IT (if not on Business tier)
- Custom security review or penetration test required
- Custom SLA or uptime guarantee
- Dedicated CSM or professional services
- Custom data residency requirements
- Volume pricing > 100+ seats
- Multi-year contracts

## Feature Allocation Decision Framework

For each feature, answer these questions:

1. **Who uses this feature?** Individual contributors → Entry. Teams → Recommended. Admins/IT → Business.
2. **When do customers discover they need it?** During activation → Entry. After first win → Recommended. When scaling → Business.
3. **What happens to retention if we gate it?** If gating it causes churn → don't gate it. If it creates a natural upgrade trigger → gate it.
4. **Is it a compliance or security feature?** → Business or Enterprise.

## Common Tier Design Mistakes

**Mistake 1: Putting the most compelling features in the highest tier only**
This kills activation. Customers need to experience your best feature to understand why it's worth paying for. Gate the *scale* of the feature, not access to it.

Example: Give 3 integrations in Entry, 10 in Recommended, unlimited in Business — don't block integrations entirely in Entry.

**Mistake 2: Usage limits so low they feel punitive**
If a customer hits the limit on day 3 of a trial, they feel cheated, not motivated to upgrade. Limits should be hit at 30–90 days of normal use.

**Mistake 3: No clear upgrade trigger**
Customers should know exactly what they'll get when they upgrade. Vague "advanced features" doesn't work. "Invite your team" or "unlock automated reporting" is actionable.

**Mistake 4: Recommended tier priced too close to Entry**
If Entry is $0 and Recommended is $9, the price is so low that customers don't believe it has full value. A 3–5× price gap between tiers creates the right psychological distance.

**Mistake 5: Enterprise tier mixed with self-serve**
Enterprise customers expect to negotiate. Showing them a "Buy now" button erodes trust. If ACV > $10K, require a sales conversation.
