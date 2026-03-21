### Metrics Definition

Before touching data, define what you're measuring and why.

**North Star metric:** one metric that best represents the value your product delivers to users. It should rise when users succeed and fall when they don't. It is not revenue — revenue is a lagging consequence.

**Supporting metrics:**
- *Input metrics* (leading indicators): the levers that drive the North Star. These are what teams actually control.
- *Guardrail metrics*: things you won't sacrifice while improving the North Star (e.g. don't improve conversion by degrading support quality).

**Vanity metrics to avoid:** raw pageviews, registered users, app downloads, cumulative revenue without a comparison baseline. These go up by default and tell you nothing about whether users are succeeding.

**Metric definition template** for every metric you track: name / formula / data source / update frequency / owner. Undefined metrics become political weapons — define them in writing first.

---

### Exploratory Analysis

**Data quality check before anything else:**
- Null rates by column — which fields have missing values, and is the missingness random or systematic?
- Duplicates — check primary keys, flag unexpected duplicates
- Outliers — p95, p99, max; determine if they're data errors or real signal
- Date range coverage — are there gaps? Is the data current?
- Join key validation — if joining tables, confirm key cardinality and match rate before trusting the join

**Summary statistics:** mean, median, p25, p75, p95 for numeric fields. Distribution shape matters — a metric with mean 50 and median 5 is not a normal distribution and cannot be summarised by its mean alone.

**Segmentation:** never accept an aggregate. Break every key metric by cohort, geography, product line, acquisition channel, and user type. The aggregate hides the story. Ask "what's driving this number?" until you can answer it with data, not hypothesis.

---

### Cohort & Retention Analysis

**Cohort setup:** group users by their acquisition period (first purchase week, signup week, or first active month). This is the only way to compare apples to apples — users acquired in different periods face different product experiences.

**Retention table:** for each cohort, calculate the percentage of users still active at D1 / D7 / D14 / D30 / D90. Present as a triangle table: cohorts as rows, time periods as columns.

**Key questions to answer:**
- At what time period does retention stabilise? This is the "floor" — the percentage of users who find long-term value.
- Which cohorts show stronger retention, and what changed between them (product changes, acquisition channel, seasonality)?
- Is the floor above 0%? A floor of 0% means no users find sustained value. A floor of 10% means there is a retained core — find out who they are.

Retention floor comparison across cohorts is the primary signal that product changes are working. Don't show only the most recent cohort.

---

### A/B Test Analysis

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

---

### Reporting & Dashboards

**Dashboard design rules:**
- One metric per chart. Combining multiple metrics on one chart obscures both.
- Sort by value, not alphabetically. Sorted bars make rank visible instantly.
- Show percentages alongside absolute numbers. 50% of 10 and 50% of 10,000 are not equivalent.
- Every chart needs a title that states the finding ("Conversion rate fell 3pp in Q4"), not just the metric name ("Conversion Rate").

**Weekly business review format:**
1. What happened — facts only, no interpretation yet
2. Why — the analysis, with confidence level
3. What we're doing about it — a specific decision or action, owned by a named person

**Executive summary rule:** every analysis must close with exactly three sentences: the finding, the implication for the business, and the recommended action. If you cannot write these three sentences, the analysis is not complete. Stakeholders make decisions on this summary — it must be unambiguous.
