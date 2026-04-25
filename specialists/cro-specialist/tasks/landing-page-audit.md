## Landing Page Audit

**Use when:** A page is getting traffic but not converting — or before launch to pre-empt conversion killers.

**Gather:** URL of the page, page goal (sign-up / purchase / lead / call booking), current conversion rate if known, traffic source (paid / organic / email), any heatmap or session recording data.

**Load psychology reference before auditing:**
Grep `~/dev/1_myprojects/gteam/references/marketing-psychology.md` for the specific challenge (low conversion, price objections, building trust, etc.). Key sections to locate: BJ Fogg Behaviour Model, Hick's Law, Default Effect, Loss Aversion, Social Proof, Status-Quo Bias.

**Setup:**
```bash
$B goto <url> && $B snapshot
```

**Audit framework — 7 conversion killers in priority order:**

**1. Above-the-fold clarity (most impactful)**
- Can a new visitor understand what the page offers within 5 seconds?
- Does the headline state a specific benefit or outcome (not a clever tagline)?
- Is there a clear primary CTA visible without scrolling?
- Does the hero image/video support the headline or distract from it?
- Issues here block all downstream conversion — fix first.

**2. Value proposition strength**
- Is the unique benefit articulated clearly? What makes this better than the obvious alternative?
- Is the copy written in customer language (their words from reviews/Reddit) or internal jargon?
- Does the copy address "why should I do this now?" (urgency) and "why this and not that?" (differentiation)?

**3. Trust & credibility signals**
- Social proof present: testimonials, case studies, logos, review counts, user numbers?
- Testimonials specific and believable (full name + title + quantified result) or generic ("Great product!")?
- Trust badges: security icons, payment logos, guarantees, accreditations — present and prominent?
- Author/company credibility visible near the offer?

**4. Call-to-action effectiveness**
- Single primary CTA, or multiple competing actions confusing the user?
- CTA copy: action verb + benefit, not just "Submit" or "Click here"?
- CTA button: high contrast, thumb-sized on mobile (≥ 44px), above the fold AND after proof?
- Repeated at natural decision points after social proof and after the offer?

**5. Friction in the conversion path**
- Form fields: only ask what's strictly necessary (each extra field drops conversion ~10–15%)
- Page load speed: `WebSearch "<url> PageSpeed score"` — every 1s delay costs ~7% conversion
- Mobile experience: does the page work perfectly on a phone? Most traffic is mobile.
- Payment/signup: how many clicks from landing to complete? Anything unnecessary in that path?

**6. Objection handling**
- FAQ section present? Does it address real objections (price, risk, compatibility, time)?
- Guarantee visible and specific (money-back details, duration, process)?
- Are the most common reasons not to buy addressed before the CTA?

**7. Message match**
- Does the page headline match the ad/email that sent traffic here?
- Mismatch between ad promise and page delivery = bounce. Check the traffic source.

**Scoring:**

| Element | Rating (1–5) | Issues Found | Priority Fix |
|---------|-------------|--------------|-------------|
| Above-fold clarity | | | |
| Value proposition | | | |
| Trust signals | | | |
| CTA effectiveness | | | |
| Friction | | | |
| Objection handling | | | |
| Message match | | | |

**Deliver:**
- Audit scorecard (element → rating → specific issues)
- Top 3 highest-impact fixes (ordered by expected conversion lift)
- Quick wins (< 1 hour to implement)
- A/B test hypothesis for the single biggest issue
