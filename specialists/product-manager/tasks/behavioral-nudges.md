### Behavioral Nudge Design

**Use when:** Users aren't adopting a feature, completing onboarding, or forming habits despite the feature being available and functional. The problem isn't the product — it's the behaviour.

**Nudge types:**

| Nudge | Mechanism | Example | Risk |
|---|---|---|---|
| Default setting | Pre-select the desired option | Email notifications ON by default | Can feel manipulative if overused |
| Social proof | Show what others do | "80% of teams use this feature" | Loses power if numbers are low |
| Progress indicator | Show completion status | "Profile 60% complete" | Annoying if too aggressive |
| Loss aversion | Frame as losing, not gaining | "You'll lose access in 3 days" | Can create anxiety |
| Commitment device | Small ask before big ask | "Try it for 7 days" before annual plan | Must deliver value in trial |
| Friction reduction | Remove steps from desired action | Pre-fill forms, one-click actions | Don't remove necessary safety friction |
| Timely prompt | Trigger at moment of relevance | Suggest feature when user hits the problem it solves | Bad timing = annoyance |

**Design process:**
1. **Identify the behaviour gap:** What should users do that they aren't doing? (Be specific — "use feature X" not "engage more")
2. **Diagnose why:** Awareness? Motivation? Ability? Trigger? (Fogg Behavior Model: B = MAP)
3. **Select nudge type** based on the barrier (awareness → prompt, motivation → social proof, ability → friction reduction)
4. **Design the intervention:** Specific copy, placement, timing, frequency
5. **Define success metric:** What behaviour change proves it worked?
6. **Set guardrails:** When does the nudge stop? (after 3 dismissals, after action taken, after X days)
7. **A/B test:** Never ship a nudge without measuring it against no-nudge baseline

**Anti-patterns:**
- Nudging toward business goals that don't align with user value (dark patterns)
- Infinite nudge loops (never stopping after user dismisses)
- Nudging power users who already know the product (insulting)
- Measuring nudge impressions instead of behaviour change (vanity)
