## Exploratory Analysis

**Data quality check before anything else:**
- Null rates by column — which fields have missing values, and is the missingness random or systematic?
- Duplicates — check primary keys, flag unexpected duplicates
- Outliers — p95, p99, max; determine if they're data errors or real signal
- Date range coverage — are there gaps? Is the data current?
- Join key validation — if joining tables, confirm key cardinality and match rate before trusting the join

**Summary statistics:** mean, median, p25, p75, p95 for numeric fields. Distribution shape matters — a metric with mean 50 and median 5 is not a normal distribution and cannot be summarised by its mean alone.

**Segmentation:** never accept an aggregate. Break every key metric by cohort, geography, product line, acquisition channel, and user type. The aggregate hides the story. Ask "what's driving this number?" until you can answer it with data, not hypothesis.
