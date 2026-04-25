## A/B Test Analysis

**Before running:**
- Power calculation: determine the sample size needed for 80% power at α=0.05 given your expected effect size. Do not start an experiment you cannot finish.
- Expected effect size: what is the minimum improvement that would be worth shipping? Calibrate your sample size to detect this, not smaller effects.
- Randomisation check: run an AA test or verify that control and treatment groups are balanced on key characteristics before launch.

**During:** do not peek at results and make decisions. Peeking inflates false positive rates. Set your analysis date before starting and honour it.

**Post-experiment:**
- Use t-test for continuous metrics (revenue, time on site), chi-squared for proportions (conversion rate, click-through rate)
- Report the confidence interval, not just the p-value. A p-value of 0.04 on a 0.01% lift is not a reason to ship.
- Distinguish statistical significance from practical significance. The question is: "Is this effect real AND large enough to matter?"

**Common mistakes to call out:** multiple comparisons without correction, novelty effects (measure at D14+ not just D1), segment dredging after seeing results (requires Bonferroni correction or pre-registration).
