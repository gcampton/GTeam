## A/B Test Design

**Use when:** Designing a conversion experiment. Poor test design wastes time and produces unactionable results.

**Gather:** Element to test, hypothesis, current baseline conversion rate, monthly traffic to the page/step, desired minimum detectable effect (MDE), testing tool available (Optimizely, VWO, Google Optimize, feature flags).

**Test design checklist:**

**1. Write the hypothesis:**
```
"Because [observation or insight], we believe that changing [element]
from [current state] to [proposed change] will [expected outcome],
measured by [metric]."
```

Good hypothesis: "Because our heatmaps show users are not scrolling past the hero image, we believe moving the primary CTA above the fold will increase click-through rate, measured by CTA clicks per session."

Bad hypothesis: "We think a red button will work better."

**2. Calculate required sample size:**

Use the formula: `n = (16 × σ²) / δ²` (simplified for conversion rates)

Or use a sample size calculator:
- WebSearch: "A/B test sample size calculator"
- Input: baseline conversion rate, MDE (minimum lift you care about), significance level (95% standard)
- Common mistake: running tests with insufficient traffic and calling winners early

Rule of thumb for 95% significance:
| Baseline CR | MDE 5% relative | MDE 10% relative | MDE 20% relative |
|------------|-----------------|-----------------|-----------------|
| 1% | ~290,000 visitors/variant | ~73,000 | ~19,000 |
| 5% | ~58,000 | ~15,000 | ~3,700 |
| 10% | ~29,000 | ~7,300 | ~1,900 |

**3. Isolate one variable:**
- Test one change at a time — if two things change, you can't know which caused the result
- Exception: multivariate testing requires 5x the traffic of A/B

**4. Set test duration:**
- Minimum 2 weeks (to capture weekly seasonality)
- Do not stop early even if results look significant — peeking inflates false positive rates
- Use fixed-horizon testing OR sequential testing methods — not "we'll stop when p < 0.05"

**5. Define success criteria before starting:**
- Primary metric: the one that determines winner (conversion rate, revenue per visitor)
- Secondary metrics: metrics to watch for unintended effects (bounce rate, revenue per order)
- Guardrail metrics: must not regress (page load time, error rate)
- Declare the winner threshold in advance (95% confidence standard; 90% acceptable for low-traffic)

**Deliver:**
- Written hypothesis (fills the template above)
- Required sample size + estimated test duration at current traffic
- Variant specification: exactly what changes between control and variant (copy-ready brief for a developer or CRO tool)
- Analysis plan: what to measure, when, and how to call a winner
- Pre-test checklist: QA steps to verify the test is running correctly before launching
