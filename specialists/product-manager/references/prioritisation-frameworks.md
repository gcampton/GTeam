# Prioritisation Frameworks

Quick reference for the three core prioritisation methods. Use the right tool for the right job.

---

## RICE Scoring

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

---

## MoSCoW Method

Categorise features for a specific release or iteration:

| Category | Definition | Capacity Rule |
|---|---|---|
| **Must have** | Release is unusable or non-compliant without it | ≤ 60% of capacity |
| **Should have** | Important but not critical — workaround exists | ~20% of capacity |
| **Could have** | Nice to have — included only if time permits | ~20% of capacity |
| **Won't have** | Explicitly out of scope for this release (not "never") | 0% — documented for future |

**Rules:**
- Must-haves consume no more than 60% of available capacity. If they exceed 60%, you have too many must-haves — challenge each one.
- "Won't have" is not a rejection — it is a deferral. Always state the condition under which a Won't-have would move up.
- Re-run MoSCoW at the start of every release cycle. Categories shift as context changes.

**Example:**

| Feature | Category | Rationale |
|---|---|---|
| User authentication | Must have | Cannot launch without login |
| Password reset flow | Must have | Support cost too high without it |
| Social login (Google/GitHub) | Should have | Reduces signup friction but email works |
| Dark mode | Could have | User request but not blocking adoption |
| Multi-language support | Won't have (this release) | Revisit when expanding to EU market |

---

## Value vs. Effort Matrix

Plot features on a 2x2 grid for fast visual triage:

```
              High Value
                  │
   Strategic      │      Quick Wins
   Bets           │      ← DO THESE FIRST
                  │
 ─────────────────┼──────────────────
                  │
   Avoid          │      Fill-ins
   (or kill)      │      (low priority)
                  │
              Low Value

   High Effort ←──┼──→ Low Effort
```

| Quadrant | Action |
|---|---|
| **Quick Wins** (high value, low effort) | Do first. Ship this sprint/quarter. |
| **Strategic Bets** (high value, high effort) | Plan carefully. Break into phases. Validate before committing full effort. |
| **Fill-ins** (low value, low effort) | Do only when capacity allows. Good for new team members ramping up. |
| **Avoid** (low value, high effort) | Say no. If stakeholders push, ask them to articulate the value — it may be higher than you think, or the conversation reveals it truly isn't worth doing. |

---

## When to Use Which Framework

| Situation | Framework | Why |
|---|---|---|
| Ranking a backlog of 10+ features | **RICE** | Produces a numerical score for objective comparison across many items |
| Scoping a specific release or sprint | **MoSCoW** | Forces hard trade-offs about what ships now vs. later |
| Quarterly planning or strategy session | **Value vs. Effort** | Fast visual alignment with leadership; good for cross-functional discussion |
| Stakeholder requests competing with roadmap | **RICE** | Score the request alongside existing items — data beats opinion |
| New team or new product with no data | **Value vs. Effort** first, then **MoSCoW** | Start with gut-level triage, refine with MoSCoW for the first release |

**Combining frameworks:** Use Value vs. Effort to shortlist, RICE to rank the shortlist, and MoSCoW to scope the release. They are complementary, not competing.
