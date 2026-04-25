## Metrics Definition

Before touching data, define what you're measuring and why.

**North Star metric:** one metric that best represents the value your product delivers to users. It should rise when users succeed and fall when they don't. It is not revenue — revenue is a lagging consequence.

**Supporting metrics:**
- *Input metrics* (leading indicators): the levers that drive the North Star. These are what teams actually control.
- *Guardrail metrics*: things you won't sacrifice while improving the North Star (e.g. don't improve conversion by degrading support quality).

**Vanity metrics to avoid:** raw pageviews, registered users, app downloads, cumulative revenue without a comparison baseline. These go up by default and tell you nothing about whether users are succeeding.

**Metric definition template** for every metric you track: name / formula / data source / update frequency / owner. Undefined metrics become political weapons — define them in writing first.

**Metrics framework delivery gate (required when designing a framework):**
- Include one North Star, 3-5 input metrics, and explicit output/lagging metrics.
- Define formulas and segmentation dimensions before launch (platform, cohort, geography, user type where relevant).
- State instrumentation source for each metric and note privacy/compliance considerations when user-level events are captured.
