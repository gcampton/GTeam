### Startup Idea Validation

**Use when:** User has a specific business idea (online or offline) and wants to know if it's worth pursuing — beyond the niche scan, this goes deeper on market size, unit economics, and competitive moat.

**Gather:** The idea (one sentence: "X for Y"), target customer, proposed price point or revenue model, any existing traction (users, revenue, waitlist).

**Step 1 — Market sizing (TAM / SAM / SOM):**

```
TAM (Total Addressable Market): everyone who could ever buy this
SAM (Serviceable Addressable Market): the segment you can realistically reach
SOM (Serviceable Obtainable Market): what you can capture in 3 years realistically
```

Research process:
- WebSearch: `"<market>" market size <year> billion` — find published market research
- WebSearch: `"<niche>" total addressable market OR TAM site:techcrunch.com OR site:crunchbase.com`
- Cross-check: count potential customers × average revenue per customer per year
- Flag: TAM > £1B is needed for VC. £10M–1B is viable for lifestyle/bootstrapped. Under £10M = niche trap.

**Step 2 — Unit economics:**

Build a simple model before committing:

```
Revenue side:
  Price per customer: £XX/month OR £XX one-time
  Target customers (year 1 / year 2 / year 3): X / X / X
  MRR/ARR target: £XX

Cost side:
  Customer Acquisition Cost (CAC): estimate from similar businesses
    - Organic (SEO/content): £5–50 CAC typical
    - Paid ads: £20–200 CAC typical (check WebSearch: "<niche> customer acquisition cost")
    - Sales-led: £200–2,000+ CAC
  Cost to Serve (COGS per customer): hosting, support, licences
  Gross margin target: ≥ 60% for software, ≥ 40% for services

Key ratios:
  LTV:CAC ratio — must be ≥ 3:1 (ideally 5:1+)
    LTV = (monthly revenue × gross margin %) ÷ monthly churn rate
  Payback period — how many months to recover CAC? Target < 12 months
```

- WebSearch: `"<business model>" average churn rate <year>` — find industry benchmarks
- WebSearch: `"<niche>" SaaS metrics OR unit economics` — find comparable businesses

**Step 3 — Competitive moat assessment:**

Rate each moat type for this idea (Strong / Weak / None):

| Moat type | Description | Test |
|-----------|-------------|------|
| Network effects | More users → more value | Does value increase as users join? |
| Switching costs | Painful to leave | Is data locked in? Workflow dependency? |
| Brand | Premium perception | Would customers pay more for the name? |
| Scale economics | Cheaper per unit at volume | Do margins improve with growth? |
| IP / technology | Patents, unique algorithm | Can competitors copy in 6 months? |
| Regulatory | Licence or compliance barrier | Needed to operate legally? |

**Weak moat = race to the bottom on price.** Any idea with no moat needs to win on execution speed and distribution alone.

**Step 4 — Investor-readiness scoring** (if raising is the goal):

| Criterion | Score 1–5 | Weight |
|-----------|-----------|--------|
| Market size (TAM > £1B = 5) | | 25% |
| Growth rate (> 20% YoY = 5) | | 20% |
| Team / founder–market fit | | 20% |
| Defensibility (moat score) | | 15% |
| Traction (users/revenue/LOIs) | | 20% |

Score ≥ 4.0 weighted → fundable for pre-seed. Score < 3.0 → bootstrap or don't pursue.

- WebSearch: `"<niche>" startup funding <year> seed round` — is this space getting VC attention?
- `$B goto https://www.crunchbase.com/discover/funding_rounds` — check recent rounds in the category

**Step 5 — Go / No-Go decision framework:**

```
GREEN (pursue): TAM > £50M, LTV:CAC ≥ 3:1, at least 1 strong moat, validated demand
AMBER (de-risk first): TAM £10–50M OR LTV:CAC 1.5–3:1 OR weak moat — run a cheap test first
RED (don't build): TAM < £10M AND/OR LTV:CAC < 1.5:1 AND/OR no moat AND/OR no paying validation
```

Cheapest validation options (before building):
- Landing page with waitlist + paid ad → measure sign-up rate (target ≥ 5% conversion)
- Concierge MVP: do the thing manually for 10 customers before automating
- Pre-sell via email list or community: get LOIs or deposits before writing code

**Deliver:**
- TAM/SAM/SOM estimates with sources
- Unit economics model (conservative / base / optimistic projections)
- Moat scorecard with the #1 risk to defensibility
- Investor-readiness score (if relevant) with gap analysis
- Go/Amber/Red verdict with the single biggest reason
- Cheapest validation experiment to run in the next 2 weeks
