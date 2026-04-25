## Sales Page & Landing Page Copy

**Use when:** Writing a long-form sales page, product landing page, or high-converting sign-up page.

**Gather:** Product/service, primary benefit (what transformation does the customer get?), target customer (who they are, what they struggle with), price point, primary call to action, any existing customer testimonials or data.

**Persuasion levers (on demand):**
When the copy calls for a specific principle (social proof, loss aversion, JTBD framing, specificity bias, contrast effect), `Grep ~/dev/1_myprojects/gteam/references/marketing-psychology.md` for that principle. Do not Read the full file — it is ~280 lines.

**Research phase (before writing a word):**

1. Identify the "hair on fire" problem — what is the customer's most urgent, specific pain?
   - WebSearch: `site:reddit.com "<niche problem>"` — read actual customer language verbatim
   - `$B goto <competitor landing page>` — what language do they use? What's the dominant pain they address?
2. Find proof of transformation — what specific results have customers achieved?
3. Identify objections — what would stop someone from buying right now?

**Sales page structure (long-form, ordered by customer psychology):**

```markdown
[HEADLINE] — Primary transformation or biggest benefit. Single sentence. Avoid cleverness.
[SUBHEADLINE] — Who it's for + the specific outcome, in plain language.

[HOOK / PROBLEM] — Open the pain. Make the reader feel understood before you mention the product.
- Describe the before state vividly: the frustration, the cost, the failed alternatives
- Use "you" language, not "many people"
- Do not mention the product yet

[AGITATION] — Make the cost of inaction real
- What happens if this problem isn't solved?
- Opportunity cost, time lost, stress, money wasted
- Quote customer pain in their own words if available

[SOLUTION REVEAL] — Introduce the product as the inevitable answer to the pain just described
- One sentence on what it is
- Immediately pivot to what it does FOR the reader (outcome, not feature)

[BENEFITS] — Translate every feature into a personal benefit
Format: "Because [feature], you get [benefit], which means [emotional outcome]"
List 5–7 benefits. Lead with the most compelling.

[PROOF] — Build credibility before the price reveal
- Testimonials: use full name, title, specific result, specificity > positivity
- Data: conversion rates, time saved, customers served, case study outcomes
- Credentials: relevant social proof (press, awards, customer logos)
- Guarantee: if there is one, explain it clearly here

[OFFER] — What exactly is included
- List everything in the package — specifics, not "bonus material"
- Assign value to each component (anchoring)
- Stack the value, then reveal the price below the stack

[PRICE & CTA] — Clear, single call to action
- Price with context (cost per day, money-back guarantee, comparison to alternative cost)
- Primary CTA button: action-oriented verb + immediate benefit ("Start growing today", "Get instant access")
- Remove all friction: what happens after they click? How fast will they get it?

[OBJECTIONS] — FAQ section addressing the top 5 reasons not to buy
- Price: "Is it worth it?"
- Time: "Will this actually work for someone like me?"
- Trust: "How do I know this is legit?"
- Urgency: "Can I come back later?"
- Risk: "What if it doesn't work?"

[FINAL CTA] — Repeat the primary CTA with a brief re-statement of the transformation
```

**Writing rules:**
- Flesch reading ease ≥ 60 (8th grade or lower)
- No paragraph > 4 lines; use white space aggressively
- One idea per sentence
- Headline must pass the "so what?" test — if the reader can shrug, rewrite it
- Never open with "Welcome to" or "Are you looking for..."

**Deliver:**
- Full sales page copy (publish-ready, all sections)
- 3 headline variants (A/B test candidates)
- CTA button copy variants (3 options)
- Meta title and description for SEO
