## Product Context Setup

**Purpose:** Create or update `~/.agents/product-context.md` — a shared foundation file that all GTeam marketing specialists reference before starting work. A complete context file eliminates redundant discovery questions across every marketing engagement.

**Check for existing file first:**

```bash
[ -f ~/.agents/product-context.md ] && echo "EXISTS" || echo "MISSING"
```

If EXISTS: Read the file, confirm it's complete, offer to update specific sections or refresh the whole document.

If MISSING: Proceed with creation via one of two paths (ask user to choose):
1. **Auto-draft from codebase** (faster — requires a project directory)
2. **Interactive walkthrough** (more accurate — good for agencies or external products)

---

## Auto-Draft Path

Run these discovery reads in parallel:

```bash
# Scan for product signals
find . -maxdepth 2 -name "README*" -o -name "package.json" -o -name "*.mdx" | head -20
```

Then Read:
- `README.md` or `README.mdx` — product description, features, taglines
- `package.json` — product name, description, keywords
- Any files matching `landing*`, `homepage*`, `marketing*`, `about*`

Extract and draft each section from what you find. Mark sections `[NEEDS REVIEW]` where signals are absent or ambiguous.

After drafting: present the draft to the user section by section. Ask them to confirm, correct, or expand each one. Do not write the file until at least the first 5 sections are confirmed.

---

## Interactive Walkthrough Path

Ask these questions **one at a time** — do not dump all questions at once. Wait for each answer before asking the next. Keep questions conversational, not form-like.

**Section 1 — Product Overview**
> "Describe the product in one sentence the way you'd say it to a stranger at a party."

Follow-up if vague: "What does someone actually do with it? What changes in their life or work?"

**Section 2 — Category & Positioning**
> "What category does this compete in? (e.g. 'project management software', 'email marketing platform', 'accounting tool for freelancers')"

**Section 3 — Target Audience**
> "Who is your best customer? Not a demographic — describe them behaviourally. What are they doing when they decide they need this?"

For B2B: "What's their job title? What team are they on? What does their boss measure them on?"

**Section 4 — Pain Points**
> "What problem does your best customer have right before they find you? What have they already tried that didn't work?"

**Section 5 — Competitive Positioning**
> "Name 3 alternatives a customer might consider instead of you. What do you beat them on?"

**Section 6 — Differentiators**
> "What's the one thing you do that no one else does — or does nowhere near as well?"

**Section 7 — Objections & Anti-Personas**
> "Who is NOT a good fit? What objections do you hear most from people who don't buy?"

**Section 8 — Customer Language** *(most important section)*
> "Can you share any direct quotes from customers — reviews, support tickets, interview transcripts, sales calls? Even 2–3 sentences in their exact words."

If none available: "What phrases do customers use when they describe the problem they had before finding you? Think: what do they say in Slack or email, not what you'd write in a press release."

**Section 9 — Brand Voice**
> "If your brand were a person, how would you describe them in 3 adjectives? What's one brand they should NOT sound like?"

**Section 10 — Proof Points**
> "What numbers can you share publicly? (customer count, time saved, revenue impact, NPS score, growth rate, etc.)"

**Section 11 — Business Goals & Conversion Actions**
> "What's the primary action you want a visitor to take? What does 'a win' look like this quarter — a signup, a booked demo, a paid upgrade?"

---

## Writing the Context File

Once sections are confirmed, write to `~/.agents/product-context.md` using this exact template:

```markdown
# Product Marketing Context
> Last updated: [YYYY-MM-DD]
> Use this file as the shared foundation for all GTeam marketing work on [Product Name].

## Product Overview
[One-sentence description — plain language, no jargon]

## Category
[The market category this competes in]

## Target Audience
[Behavioural description of the ideal customer — who they are, what they're doing, what they're responsible for]

### B2B Personas (if applicable)
| Persona | Title | Team | Primary Goal | What they're measured on |
|---------|-------|------|-------------|--------------------------|
| Champion | [title] | [team] | [goal] | [metric] |
| Economic Buyer | [title] | [team] | [goal] | [metric] |
| End User | [title] | [team] | [goal] | [metric] |

## Pain Points
[The problem(s) the customer has immediately before finding this product. What have they already tried?]

## Competitive Positioning
| Competitor | Their strength | We beat them on |
|------------|---------------|-----------------|
| [Name] | [strength] | [differentiator] |

## Key Differentiators
[What this product does that alternatives don't — or don't do as well. Be specific.]

## Objections & Anti-Personas
**Common objections:**
- [Objection 1]
- [Objection 2]

**Who is NOT a good fit:**
[Description of anti-persona — who churns, who complains, who never should have bought]

## Customer Language
> These are verbatim phrases from real customers. Use these exact words in copy — they outperform polished descriptions.

- "[Verbatim phrase 1]"
- "[Verbatim phrase 2]"
- "[Verbatim phrase 3]"

## Brand Voice
**We are:** [adjective 1], [adjective 2], [adjective 3]
**We are not:** [opposite 1], [opposite 2], [opposite 3]
**Don't sound like:** [brand to avoid]

## Proof Points & Metrics
- [Metric or social proof point 1]
- [Metric or social proof point 2]

## Business Goals & Conversion Actions
**Primary conversion action:** [e.g. "Free trial signup", "Book a demo", "Paid plan upgrade"]
**Current focus:** [e.g. "Grow trial signups by 40% this quarter", "Reduce churn below 2%/month"]
```

Confirm the file path with the user before writing. Default is `~/.agents/product-context.md`.

---

## How Other Specialists Use This File

At the start of any marketing specialist workflow, check for this file:

```bash
[ -f ~/.agents/product-context.md ] && echo "Context found" || echo "Run product-context specialist first"
```

If found: Read it and use it to pre-fill context — skip discovery questions already answered.

If not found: Mention to the user that running the `product-context` specialist first will make this specialist faster and more accurate. Then proceed with manual context gathering.
