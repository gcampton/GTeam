### Discovery & Validation

Never evaluate a solution before you understand the problem. Discovery is not optional — it's the only thing that separates a roadmap from a wish list.

**Problem framing:** Start with a crisp problem statement: "Who is experiencing what pain, in what context, and what is the cost of not solving it?" If you can't answer all four parts, you haven't framed the problem yet. Do not accept "users want X" as a problem statement — X is a solution. Ask what they're trying to achieve and what's preventing them.

**User interview guide (5–7 questions, open-ended, pain-focused):**
1. "Walk me through the last time you tried to [task in the problem space]. What happened?"
2. "What's the hardest part of [task] for you right now?"
3. "How do you handle it today? What's your workaround?"
4. "How much time does this take? What does it cost you when it goes wrong?"
5. "If this problem went away tomorrow, what would be different for you?"
6. "Who else is affected by this problem on your team?"
7. "What have you already tried? Why didn't it stick?"

Run a minimum of 5 interviews before drawing any conclusions. 10 is better for new problem spaces. Take verbatim notes — paraphrasing introduces bias. Patterns that appear in 3+ interviews independently are signal; isolated mentions are noise.

**Competitive analysis (3–5 competitors):**

| Competitor | Core Features | Positioning | Pricing | Key Gap |
|------------|---------------|-------------|---------|---------|
| [Name] | [What they do] | [Who they claim to serve] | [Model] | [What they don't do or do poorly] |

Look for gaps that appear consistently across multiple competitors — those are markets being under-served, not just product failures.

**Market sizing (TAM/SAM/SOM with stated assumptions):**
- **TAM** (Total Addressable Market): The total revenue opportunity if you had 100% of the relevant market. Use a bottom-up approach: estimated number of potential customers × average revenue per customer per year.
- **SAM** (Serviceable Addressable Market): The portion of TAM you can realistically reach given your product's current scope and go-to-market capability.
- **SOM** (Serviceable Obtainable Market): What you can realistically capture in 12–24 months given competition, sales capacity, and execution risk.

Always state your assumptions. A market size without assumptions is a guess dressed as analysis.

**Output — Opportunity Brief (one page):**

```markdown
# Opportunity Brief: [Name]

**Problem:** [Who / what pain / in what context / cost of inaction]
**Evidence:** [Interview signal, behavioral data, support volume, competitive gap]
**Market Size:** TAM $Xm / SAM $Xm / SOM $Xm — [key assumptions]
**Why Now:** [What makes this urgent — market shift, data signal, competitive pressure]
**Hypothesis:** [If we build X, users will Y, and we'll see Z metric improve]
**Recommendation:** Explore / Build MVP / Full build / Defer / Kill
```
