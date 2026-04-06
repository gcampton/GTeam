### User Profiling

**Use when:** First interaction with the user, or when no prior context exists about their background, skills, and goals. Skip if user profile is already known from memory or context.

**Check first:** Before running this profiling step, check if you already have context about the user (from memory, prior conversations, or a context file). If you already know their background, skills, and goals — summarise what you know and ask "Is this still accurate?" instead of re-asking everything.

**Gather the following through natural conversation (not an interrogation — weave these in):**

1. **Background & experience:**
   - What do you do for work currently?
   - Have you run a business or side project before? What happened?
   - How would you rate your technical skills? (coding, design, video, writing — specify level for each)

2. **Interests & unfair advantages:**
   - What topics do you know deeply or find yourself reading about for fun?
   - What industry or domain knowledge do you have that most people don't?
   - Do you have any existing audience, email list, social following, or distribution channel?

3. **Constraints:**
   - How many hours per week can you realistically commit? (be honest — 5, 10, 20, 40?)
   - What's your available budget to start? (£0 bootstrapping / < £500 / £500–5k / £5k+)
   - Any hard constraints? (location-dependent, can't do video, need income within X months, etc.)

4. **Goals & motivation:**
   - What does success look like to you? (side income, replace salary, build something big, learn a skill?)
   - What's your target monthly income from this? (£500, £2k, £5k, £10k+?)
   - What's your timeline? (need money in 3 months vs. willing to invest 12 months building)

**Output — User Profile Summary:**

```markdown
## User Profile

**Background:** [current role, relevant experience]
**Technical skills:** Coding [0-5] | Design [0-5] | Video [0-5] | Writing [0-5]
**Domain expertise:** [industries/topics they know deeply]
**Existing assets:** [audience, email list, following, domain, content library — or "none"]

**Constraints:**
- Time: [X hours/week]
- Budget: [£amount]
- Hard limits: [any dealbreakers]

**Goals:**
- Target: [£X/month]
- Timeline: [X months to first income]
- Ambition: [side income / salary replacement / build a business]
```

**How this shapes research:**
- Low coding skill + low budget → content, affiliate, or service-based niches
- Strong coding + moderate budget → SaaS, AI tools, developer products
- Domain expertise in X → look for underserved niches within X first (unfair advantage)
- < 10 hours/week → passive models only (affiliate, digital products, not services)
- Needs income in < 3 months → focus on proven models with fast time-to-revenue (freelancing, affiliate), not speculative bets

**After profiling, recommend which research task to run next** based on their profile:
- Service-oriented person with domain expertise → `tasks/niche-scan.md` focused on consulting/productised services
- Content creator type → `tasks/affiliate-content-research.md`
- Technical builder → `tasks/digital-products.md`
- Has a specific idea already → `tasks/startup-validation.md`
