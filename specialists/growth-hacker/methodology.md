### Growth Audit

**Gather:** Product URL or description, current analytics access (GA4, Mixpanel, Amplitude), any existing funnel data, stage (pre-PMF / post-PMF).

**AARRR funnel mapping:**
1. **Acquisition** — Where are users coming from? (channel breakdown: organic, paid, referral, direct, social). What is the blended CAC?
2. **Activation** — What percentage of new users reach the "aha moment"? What is the activation rate (Day 0 action completion)?
3. **Retention** — Cohort retention: D1 / D7 / D30 / D90. Where is the curve flattening (if at all)?
4. **Referral** — Is there a referral mechanism? What is the current k-factor (invites sent × invite conversion rate)?
5. **Revenue** — ARPU, LTV, payback period. LTV:CAC ratio (target ≥ 3:1).

**Identify the biggest leak:** Map conversion rates at each funnel stage. The stage with the largest absolute user drop is the priority — fix the biggest leak first, not the most interesting one.

**Benchmarks by stage (SaaS defaults):**
- Visitor → signup: 2–5%
- Signup → activation: 40–60%
- D7 retention: 25–40%
- D30 retention: 15–25%
- Referral k-factor: >0.3 is good, >1.0 is viral

**Deliver:** Funnel diagram with conversion rates at each stage. Top 3 leaks ranked by user volume lost. Single recommended priority for the next sprint.

---

### Experiment Design

**ICE scoring for prioritisation:**
- **Impact** (1–10): How much will this move the North Star metric if it works?
- **Confidence** (1–10): How sure are you it will work, based on evidence or analogues?
- **Ease** (1–10): How fast and cheap is it to run?
- ICE score = (Impact + Confidence + Ease) / 3. Run highest-score experiments first.

**Experiment template (complete before starting any test):**

| Field | Content |
|-------|---------|
| Hypothesis | "We believe that [change] will [outcome] because [reason]" |
| North Star metric affected | [primary metric this moves] |
| Guardrail metrics | [metrics that must not degrade] |
| Baseline | [current value of primary metric] |
| Target | [minimum detectable effect — MDE] |
| Test design | [A/B split / multivariate / holdout / pre-post] |
| Sample size | [calculated via power analysis] |
| Duration | [minimum to reach significance, typically 2 weeks] |
| Owner | [who runs it] |

**Minimum detectable effect (MDE):** Use a sample size calculator (e.g. Evan Miller's). Default settings: p<0.05, 80% power, two-tailed test. Never run a test too short to reach significance — underpowered tests produce noise.

**Statistical significance threshold:** p<0.05, 80% power minimum. For high-stakes decisions (pricing, core onboarding), require p<0.01.

**Avoiding HiPPO-driven decisions:** All experiment proposals require an ICE score and written hypothesis before approval. No experiment runs because "the CEO wants to try it" without completing the template. Present experiment results with confidence intervals, not just point estimates.

**Experiment log format:** Maintain a running log with columns: date started, hypothesis, ICE score, result (winner / loser / inconclusive), magnitude of effect, decision made.

---

### Acquisition Channels

**Channel evaluation framework — score each channel on:**

| Criterion | Definition |
|-----------|------------|
| CAC | Fully-loaded cost to acquire one paying customer |
| LTV | Expected revenue over customer lifetime |
| Payback period | Months to recover CAC from gross margin |
| Scalability | Can spend 10× without CAC blowout? |
| Time to signal | How quickly does this channel give feedback? |

**Target unit economics:** LTV:CAC ≥ 3:1, payback period ≤ 12 months (≤6 months for venture-backed).

**Channel-specific tactics:**

- **SEO (content + technical):** Long-tail keyword clusters around problems the product solves. Technical foundation first (crawlability, Core Web Vitals, schema). Programmatic pages for high-volume, low-competition patterns. Compound — slow to start, lowest CAC at scale.

- **Paid search:** High intent, fast signal. Start with exact/phrase match on bottom-of-funnel keywords. Expand to broad + smart bidding once conversion data exists (≥30 conversions/month per campaign). Use for validated offers only — not for testing messaging.

- **Paid social (Meta/LinkedIn/TikTok):** Interrupt-based — creative is the targeting. Meta for B2C and broad B2B. LinkedIn for job-title-targeted B2B (higher CPL, higher quality). TikTok for sub-35 consumer audiences. Test 3–5 creative angles before optimising audiences.

- **Viral / referral (k-factor):** k-factor = invites sent per user × invite acceptance rate. k > 1.0 = viral growth (sustainable). Optimise: trigger referral at the moment of highest satisfaction (post-aha), reduce friction (pre-filled share message, one-click), make the incentive clear to both sides. Track invite send rate, not just k-factor.

- **Partnerships:** Co-marketing, integration partnerships, distribution deals. Best when partner has same ICP but non-competing product. Measure: leads generated, conversion rate vs. other channels, partner attribution accuracy.

- **Community:** Own a niche community (Slack, Discord, Reddit, newsletter). High trust, low CAC, slow to scale. Works best for developer tools, prosumer products, and B2B niches.

- **Product-led (PLG):** Free tier / freemium / trial. Self-serve conversion. Optimise the free-to-paid trigger. PLG works when the product has clear standalone value and the upgrade path is obvious. Measure: PQL (product-qualified lead) conversion rate.

**When to go deep vs. diversify:** Pre-PMF — test 2–3 channels for signal. Post-PMF — go deep on 1–2 channels to scale, then add a second when the first shows diminishing returns (CAC rising >30% quarter-on-quarter).

---

### Activation & Onboarding Optimisation

**Load psychology reference for behavioural design:**
Read `~/.claude/skills/gteam/references/marketing-psychology.md` — use the Quick-Reference table for the specific challenge (low activation, poor retention, referral loop design). Key sections: BJ Fogg Behaviour Model, Goal-Gradient Effect, IKEA Effect, Commitment & Consistency, Endowment Effect, Zeigarnik Effect.

**Time-to-value (TTV) reduction:**
1. Define the "aha moment" — the specific action that predicts long-term retention. (Examples: Slack → send first message with a teammate; Dropbox → add first file; Twitter → follow 30 accounts.)
2. Map every step between signup and aha.
3. Remove or defer every step that isn't strictly necessary to reach aha. Each extra step = conversion loss.
4. Measure TTV in minutes/hours. Set a target and track it as a KPI.

**Onboarding design principles:**
- **Progress indicators:** Show users where they are in setup. Completion anxiety drives action.
- **Empty state design:** Empty states are the most important screens for activation. Show what the product looks like when it's working, or prompt the exact action that fills it.
- **In-app guidance:** Contextual tooltips > onboarding modals. Show guidance at the moment the user needs it, not upfront.
- **Social proof in onboarding:** "1,200 teams use this to do X" — reduces anxiety at decision points.

**Email activation sequence:**

| Day | Subject line angle | Goal |
|-----|--------------------|------|
| Day 0 (immediate) | "Here's how to get started" | Drive first key action |
| Day 1 | "Did you try [aha action] yet?" | Re-engage non-activators |
| Day 3 | Social proof / use case example | Build confidence |
| Day 7 | "You're missing out on [benefit]" | Last push before churn risk |

**A/B testing onboarding flows:** Test one variable at a time. Priority order: number of steps (fewer wins almost always) → field labels and copy → order of steps → optional vs. required fields. Measure: activation rate and D7 retention as joint success metrics — a flow that activates users but destroys retention is not a win.

---

### Retention & Referral

**Cohort retention analysis:**
- Pull weekly or monthly cohorts. Plot D1 / D7 / D30 / D90 retention curves.
- "Flattening" indicates a retained core — the product has some long-term value. No flattening = PMF not yet achieved, focus on product before acquisition.
- Segment cohorts by: acquisition channel, user role/persona, onboarding path, plan type. Differences reveal which segments retain and which churn.

**Churn intervention triggers (set up automated detection):**

| Signal | Trigger | Intervention |
|--------|---------|--------------|
| No login in 7 days (active user) | Usage drop | Re-engagement email / in-app notification |
| Key feature never used after 14 days | Feature non-adoption | Targeted in-app guide or CSM outreach (B2B) |
| Support ticket opened | Friction signal | Proactive follow-up within 24h |
| Downgrade page visited | Intent to churn | Offer pause / discount / alternative plan |
| NPS score 0–6 submitted | Detractor | Human outreach within 48h — understand root cause |

**Referral loop design:**
1. **Incentive structure:** Two-sided incentive (giver and receiver both benefit) outperforms one-sided. Incentive should be product-native where possible (free months, credits) rather than cash — attracts users who want the product.
2. **Timing:** Trigger the referral ask at the moment of highest satisfaction — immediately after the aha moment, after a positive milestone, after a positive NPS response.
3. **Friction reduction:** Pre-fill the share message. One-click share to email or WhatsApp. Don't force the user to write their own message.
4. **K-factor tracking:** Measure (a) referral invite send rate, (b) invite-to-signup conversion rate, (c) signup-to-activation rate from referrals. Referral users typically retain better — track their D30 cohort separately.

**NPS segmentation:**
- **Promoters (9–10):** Trigger referral ask immediately. Feature in case studies with permission.
- **Passives (7–8):** Identify what would move them to promoter. Often one missing feature.
- **Detractors (0–6):** Human outreach within 48h. Don't ask for referrals. Goal: understand root cause and either fix it or document it as a segment the product doesn't serve.

---

### Experiment Statistical Rigor

**Use when:** Designing A/B tests or interpreting experiment results. Prevents premature conclusions and wasted effort.

**Pre-experiment checklist:**

1. **Hypothesis:** "If we change [X], then [metric] will [increase/decrease] by [amount] because [reasoning]"
2. **Primary metric:** One metric that determines success. Define it precisely.
3. **Guardrail metrics:** 2-3 metrics that must NOT degrade (e.g., revenue, error rate, page load time)
4. **Sample size calculation:**
   - Baseline conversion rate: [current %]
   - Minimum detectable effect (MDE): [smallest change worth detecting, typically 5-20% relative]
   - Statistical significance: 95% (p < 0.05)
   - Power: 80% (1 - β)
   - Use: WebSearch `"sample size calculator" A/B test` or formula: n = (Z²× p(1-p)) / E²

5. **Expected duration:** Sample size ÷ daily traffic = days needed. Never run < 7 days (day-of-week effects). Never run > 6 weeks (novelty effects fade).

**During experiment:**

- **No peeking** — don't check results daily and stop early when it "looks significant"
- **Early stopping rules** (only valid reasons to stop early):
  - Guardrail metric breached (e.g., error rate spikes)
  - Technical failure (variant broken, tracking lost)
  - Sample size reached AND significance threshold met
- **Document** any unexpected events (outages, marketing campaigns, seasonality)

**Interpreting results:**

| Result | p-value | Practical significance | Action |
|---|---|---|---|
| Significant + meaningful | < 0.05 | MDE exceeded | Ship the variant |
| Significant + tiny effect | < 0.05 | Below MDE | Don't ship — not worth the complexity |
| Not significant | > 0.05 | N/A | Inconclusive — increase sample or try bigger change |
| Guardrail breached | N/A | N/A | Kill the experiment immediately |

**Common mistakes:**
- Calling a test after 2 days because it "looks good" (insufficient sample)
- Running 10 variants simultaneously (can't isolate what worked)
- Testing button colour instead of value proposition (low-impact variable)
- No guardrail metrics (winning on clicks but losing on revenue)
