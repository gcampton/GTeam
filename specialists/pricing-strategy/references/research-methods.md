# Pricing Research Methods

## When to Do Research vs. Competitive Benchmarking

**Use quantitative research when:**
- Launching pricing from scratch with no comparable products
- Planning a significant price increase (>20%) and need to know the ceiling
- Deciding between two pricing metrics and want customer preference data
- You have 50+ survey-reachable customers or prospects

**Use competitive benchmarking when:**
- Time is short and research isn't feasible
- You're in an established category with transparent pricing
- You just need to sanity-check a price point
- You're doing a minor optimisation (<15% change)

---

## Method 1: Van Westendorp Price Sensitivity Meter (PSM)

### Purpose
Find the acceptable price range and optimal price point for a defined customer segment.

### Survey questions (ask in this order, each with a dollar input)
1. "At what price would you consider this product to be **so inexpensive** that you would question the quality?"
2. "At what price would this product represent a **good value for money**?"
3. "At what price would this product start to seem **expensive**, but you'd still consider buying it?"
4. "At what price would this product be **too expensive** to even consider?"

### Minimum sample size
- 50 respondents for early direction
- 150+ for reliable segmented analysis
- Segment by: customer tier, company size, industry — responses often differ significantly across segments

### Plotting the results
Plot four cumulative frequency curves:
1. **Too cheap** (Q1) — % of respondents who say price X is "so cheap it's suspicious" — rises from right to left
2. **Bargain** (Q2) — % who say X is a "good value" — rises left to right
3. **Expensive** (Q3) — % who say X is "expensive but acceptable" — rises left to right
4. **Too expensive** (Q4) — % who say X is "too expensive" — rises left to right

**Key intersection points:**
- **OPP (Optimal Price Point):** intersection of "Too cheap" and "Too expensive" curves. The price where equal numbers find it suspiciously cheap as find it unacceptably expensive.
- **IDP (Indifference Price Point):** intersection of "Bargain" and "Expensive" curves. Where an equal number find it a bargain as find it expensive.
- **Acceptable price range:** area between "Too cheap" and "Too expensive"

**Recommended price:** between OPP and IDP. OPP maximises volume; IDP maximises perceived quality. Position closer to OPP for market-share focus; closer to IDP for premium positioning.

### Distribution
Prioritise in this order:
1. Current trial users (they have the most accurate willingness-to-pay for your specific product)
2. Target prospects who match your ICP but haven't trialled
3. Churned customers (useful but weight their responses lower — they may be price-sensitive outliers)

### Tool
Build in Typeform (conditional logic keeps questions clean) or Google Forms. Target: 3-minute completion time.

---

## Method 2: Gabor-Granger

### Purpose
Test willingness to buy at specific price points to find the revenue-maximising price and build a demand curve.

### How it works
Present a series of pre-defined prices in randomised order and ask: "Would you pay [price] for this product?" (Yes / No / Maybe — score Maybe as 0.5× Yes)

Typical price sequence: $29, $49, $79, $99, $149, $199

For each price point, calculate:
- % of respondents who would buy at that price
- Expected revenue per respondent = price × % who would buy

Plot: Price (x-axis) vs. Revenue per respondent (y-axis). The peak of the curve is the revenue-maximising price.

### Notes
- Use Gabor-Granger to validate a specific candidate price point identified by Van Westendorp
- Keep price sequences to 4–6 points (too many creates respondent fatigue)
- Gabor-Granger underestimates real-world willingness to pay slightly (people say no to prices they'd actually pay). Use it for relative comparisons, not absolute.

---

## Method 3: Competitive Benchmarking

### When to use
Quick validation; no access to customers; established category with transparent pricing.

### Process

1. **Identify 5 direct competitors.** Direct means: same ICP, same use case, overlapping features. Indirect alternatives (Excel, doing it manually) can be listed separately but don't drive the benchmark.

2. **Record comparable tier pricing.** Find the tier that most closely matches your Recommended tier. Note: per seat or flat fee, annual vs. monthly, what's included.

3. **Calculate your relative value position.**

| Factor | Your product | Competitor median |
|--------|-------------|-------------------|
| Price (comparable tier) | $[X]/mo | $[Y]/mo |
| Feature parity (1–5) | [score] | [baseline: 3] |
| Integrations | [count] | [median] |
| Support SLA | [SLA] | [median] |
| UX quality (1–5) | [score] | [baseline: 3] |

**Value premium/discount formula:**
If your feature score is 4/5 and the median is 3/5, you can justify a ~15–25% premium over the median price.
If your features are at parity, price at median.
Only price below median if you're explicitly pursuing a market-share strategy — under-pricing trains prospects to perceive lower quality.

4. **Adjust for positioning intent:**
- Premium positioning: price at 20–40% above median with clear differentiation justification
- Value positioning: price at 0–15% below median
- Market-share play: price at 20–30% below median (requires a clear cost structure advantage)

---

## Method 4: Price Increase Validation (Existing Customer Survey)

Before raising prices for existing customers, survey a sample to estimate churn risk.

### Survey question
"If the price of [Product] increased from $[current price] to $[new price], which of these best describes what you'd do?"
- Continue at the new price (no change)
- Continue but consider alternatives
- Actively look for an alternative
- Cancel within 30 days

### Interpreting results
- "Continue" + "consider alternatives" combined > 70%: safe to proceed
- "Actively look" + "Cancel" combined > 25%: high churn risk — re-examine increase magnitude
- Segment by plan tier and tenure — long-tenured customers often have higher tolerance

### Note
Always validate with a subset of price-sensitive accounts via sales or CS before announcing. Customers who self-identify as at-risk should be handled individually before the mass announcement.
