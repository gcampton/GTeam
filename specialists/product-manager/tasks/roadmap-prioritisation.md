### Roadmap & Prioritisation

A roadmap is a prioritised bet, not a promise. It should answer: what are we working on, in what order, and why?

**RICE Prioritisation Framework:**

**Formula:** RICE Score = (Reach x Impact x Confidence) / Effort

| Factor | Scale | Description |
|---|---|---|
| Reach | # of users/accounts affected per quarter | How many people will this impact? |
| Impact | 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive) | How much will it impact each person? |
| Confidence | 0.5 (low), 0.8 (medium), 1.0 (high) | How confident are we in our estimates? |
| Effort | Person-months (e.g., 0.5, 1, 2, 3) | How much work is this? |

**Worked example:**
- Feature: In-app onboarding wizard
- Reach: 500 new signups/quarter
- Impact: 2 (high — directly affects activation)
- Confidence: 0.8 (medium — based on competitor analysis, not own data)
- Effort: 1.5 person-months
- RICE = (500 x 2 x 0.8) / 1.5 = **533**

**Rules:**
- Score all candidate features before committing to a roadmap
- Rank by RICE score, then apply strategic judgment for tie-breaks
- Re-score quarterly as data improves (confidence should increase)
- Confidence < 0.5 → run a discovery spike before building

Score every roadmap candidate. High-RICE items go first. When two items have similar scores, prefer the one that builds a foundation for future work.

**Roadmap format (Now / Next / Later):**

| Horizon | Meaning | Commitment Level |
|---------|---------|-----------------|
| **Now** | This quarter — actively in design or development | Fully committed, scoped, and staffed |
| **Next** | Next 1–2 quarters — directionally planned, needs scoping | Directionally committed; may shift with new evidence |
| **Later** | 3–6 month horizon — strategic bets | Not scheduled; advances when evidence or priority warrants |

Do not use fixed dates in Next and Later. Time horizons communicate priority without creating false commitments.

**Handling stakeholder roadmap requests:** When a stakeholder requests a feature, qualify the problem before evaluating the solution. Ask: "What problem is this solving?", "Who experiences it and how often?", "What's the impact if we don't solve it?" Then score it against current roadmap items. If it scores higher, reprioritise. If it doesn't, communicate clearly why it's deferred — with the condition under which it would move up.

**Quarterly planning process:**
1. Audit the previous quarter: which items shipped, which didn't, which success metrics were hit
2. Collect new discovery signal: interviews, support trends, NPS verbatims, sales blockers
3. Rescore the backlog with updated RICE scores
4. Draft the Now/Next/Later roadmap
5. Review with engineering for feasibility and capacity
6. Present to leadership for strategic alignment
7. Publish — including the "What we're not building and why" section

---

### Jobs-to-be-Done (JTBD) Framework

**Use when:** Starting a new product area, questioning why an existing feature isn't getting traction, or when user research reveals confusion between what users say they want and what they actually do.

**Core principle:** People don't buy products — they hire them to do a job. The job is stable; the product is just the current best solution. Understanding the job lets you build things that will be hired.

**The JTBD canvas — fill this before writing a PRD:**

```markdown
# JTBD Canvas: [Job Name]

## Job Statement
When [situation/context],
I want to [motivation/goal],
So I can [expected outcome].

## Job Dimensions
- **Functional job:** What are they trying to accomplish practically?
- **Emotional job:** How do they want to feel during/after?
- **Social job:** How do they want to be perceived by others?

## Job Executor
Who performs this job? [Role / persona / situation that triggers it]

## Job Circumstances
- Frequency: [How often does this job arise?]
- Urgency: [Time pressure — planned vs. ad-hoc?]
- Context: [Where / when / with what tools?]

## Current Solutions (what they "fire" when they hire us)
| Current solution | Why it's inadequate | Our advantage |
|-----------------|--------------------|----|
| [Spreadsheet / manual process / competitor] | [Specific gap] | [What we do better] |

## Desired Outcomes (how the job executor measures success)
List 10–15 desired outcomes in the format: [direction] [metric] [object] [context]
Example: "Minimise the time it takes to find a relevant contact when preparing for a call"

Rate each outcome: Importance (1–10) × Satisfaction with current solution (1–10)
Opportunity score = Importance + (Importance − Satisfaction) → focus on score ≥ 10
```

**Finding the real job (not the stated one):**

The stated job is what users ask for ("make the dashboard faster"). The real job is what they're trying to accomplish ("know if something is wrong before my manager does"). Uncover it by asking:

- "What are you trying to accomplish when you use this?"
- "What would you do if this feature didn't exist?"
- "Walk me through the last time you needed to do [X]. What happened before you opened our product?"
- "What does success look like after you've done this?"

**JTBD → PRD pipeline:**

```
Step 1: Fill the JTBD Canvas for the primary user segment
Step 2: Calculate opportunity scores for all desired outcomes
Step 3: Focus PRD on the top 3 opportunity-score outcomes
Step 4: For each outcome, define a feature hypothesis (if we build X, outcome Y improves)
Step 5: PRD acceptance criteria must map back to outcome metrics
```

**Brainstorming gate (mandatory before choosing a solution):**

Before committing to any feature direction, generate ≥ 3 distinct solution approaches:

```markdown
## Solution Options for [Job/Outcome]

### Option A: [Name]
- Approach: [How it works]
- Effort: S/M/L/XL
- Risk: High/Medium/Low
- Outcome coverage: [Which desired outcomes it addresses, and how well]
- Downside: [What it doesn't solve or makes worse]

### Option B: [Name]
...

### Option C: [Name]
...

## Recommendation
[Which option and why — cite specific desired outcomes and trade-offs]
```

This is not a formality. The first idea is rarely the best one. The brainstorming gate prevents tunnel vision and gives engineers and designers a seat in the solution space.

**Deliver:**
- Completed JTBD canvas
- Opportunity score table (desired outcomes ranked by priority)
- Solution options brief (≥ 3 options with recommendation)
- PRD with acceptance criteria mapped to JTBD outcomes

---

### Opportunity Solution Tree

Visual framework linking business outcomes to discovery:

```
Business Outcome (metric to move)
├── Opportunity 1 (user pain/need from research)
│   ├── Solution A
│   │   ├── Experiment 1
│   │   └── Experiment 2
│   └── Solution B
│       └── Experiment 3
├── Opportunity 2
│   └── Solution C
│       └── Experiment 4
```

**How to build:**
1. Start with the target outcome (e.g., "Increase activation rate from 25% to 40%")
2. Map opportunities from user research (JTBD interviews, support tickets, analytics)
3. Brainstorm 2-3 solutions per opportunity (this satisfies the brainstorming gate: ≥ 3 options)
4. Design small experiments to validate each solution before building

**Rules:**
- One tree per business outcome
- Opportunities come from research, not assumptions
- Solutions are options, not commitments — validate before building
- Update the tree weekly as experiments complete

---

### North Star Metric Framework

**Definition:** A single metric that captures the core value your product delivers to customers.

**Criteria for a good North Star:**
- Measures value delivered (not vanity: not pageviews or signups)
- Actionable by the product team (not revenue alone — that's a lagging indicator)
- Measurable weekly (fast enough feedback loop)
- Leading indicator of revenue (if North Star grows, revenue follows)

**Examples:**
| Product Type | North Star | Why |
|---|---|---|
| SaaS tool | Weekly active users completing core action | Measures habitual value delivery |
| Marketplace | Transactions completed per week | Measures both-side value |
| Content platform | Weekly reading/watching time | Measures engagement depth |
| Developer tool | API calls per week | Measures integration depth |

**Supporting metrics (input metrics):**
Break the North Star into 3-5 input metrics the team can directly influence:
- Acquisition: new users reaching activation
- Activation: users completing first-value action
- Engagement: frequency/depth of core action
- Retention: users returning week-over-week

---

### Funnel Analysis Template

| Stage | Metric | Current | Target | Gap | Owner |
|---|---|---|---|---|---|
| Awareness | Website visitors/month | | | | Marketing |
| Acquisition | Signups/month | | | | Growth |
| Activation | Users completing first-value action (Day 7) | | | | Product |
| Retention | Users active at Day 30 | | | | Product |
| Revenue | Paying customers / MRR | | | | Sales/Product |
| Referral | Users who invite others | | | | Growth |

**Analysis process:**
1. Fill in current numbers
2. Calculate conversion rate between each stage
3. Identify the largest drop-off (this is your biggest lever)
4. Focus product efforts on the weakest conversion step
5. Review monthly — the bottleneck shifts as you fix each stage
