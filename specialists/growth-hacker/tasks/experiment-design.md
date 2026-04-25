## Experiment Design

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
