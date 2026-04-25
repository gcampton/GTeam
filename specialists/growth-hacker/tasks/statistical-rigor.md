## Experiment Statistical Rigor

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
