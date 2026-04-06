# Evaluation Patterns

Framework for evaluating AI system quality across development, testing, and production.

## Automated Metrics

| Metric | Task Type | What It Measures | Limitations |
|---|---|---|---|
| Exact match | Classification, extraction | Output matches gold label exactly | Too strict for paraphrased correct answers |
| F1 score | Multi-label, NER, extraction | Balance of precision and recall | Doesn't capture semantic equivalence |
| BLEU | Translation, summarisation | N-gram overlap with reference | Correlates poorly with human judgement |
| ROUGE-L | Summarisation | Longest common subsequence with reference | Rewards surface similarity, not meaning |
| Code execution | Code generation | Generated code passes test cases | Only works for well-defined problems |
| JSON schema match | Structured output | Output conforms to expected schema | Validates structure, not content quality |
| Cosine similarity | Embeddings, retrieval | Semantic similarity between vectors | Threshold choice is arbitrary |

**When to use which:**
- Extraction/classification: exact match + F1
- Summarisation: ROUGE-L + LLM-as-judge (ROUGE alone is insufficient)
- Code generation: execution match (strongest signal)
- Open-ended generation: LLM-as-judge (automated metrics are unreliable)

## LLM-as-Judge

**Setup:**
1. Use a stronger model than the one being evaluated (e.g., Claude Opus to judge Haiku output)
2. Write a rubric with clear scoring criteria (1-5 scale with descriptions for each level)
3. Provide the original input, the model output, and optionally a reference answer
4. Run each judgement 3 times — take the majority vote to reduce noise

**Rubric template:**
```
Score 1: Completely wrong or irrelevant. Factual errors, ignores the question.
Score 2: Partially addresses the question but has significant errors or omissions.
Score 3: Addresses the question adequately. Minor errors or missing details.
Score 4: Good answer. Accurate, relevant, well-structured. Minor improvements possible.
Score 5: Excellent. Accurate, comprehensive, well-structured, no improvements needed.
```

**Multi-dimension scoring (for complex tasks):**
- Accuracy: are the facts correct?
- Relevance: does it answer the actual question?
- Completeness: are all aspects of the question addressed?
- Coherence: is it well-structured and easy to follow?
- Conciseness: is it appropriately brief without losing substance?

**Validation:** Score 50 outputs with both LLM-as-judge and human evaluators. Calculate agreement (Cohen's kappa). If kappa < 0.6, refine the rubric.

## Human Evaluation

**When to use:**
- Final validation before launching a new AI feature
- Calibrating automated metrics and LLM-as-judge
- High-stakes domains (medical, legal, financial)
- When automated metrics disagree with user feedback

**Protocol:**
1. Sample 100-200 production outputs (stratified by query type and difficulty)
2. Blind evaluation: evaluators don't know which model/prompt version generated the output
3. Each output scored by 2+ evaluators independently
4. Measure inter-rater reliability (Cohen's kappa or Krippendorff's alpha)
5. If agreement < 0.6, calibrate evaluators with training examples before continuing

**Evaluation form (per output):**
- Task: [the input/question]
- Output: [the model's response]
- Correct? [Yes / Partially / No]
- Quality: [1-5 with rubric]
- Specific issues: [free text — hallucination, incomplete, wrong format, etc.]

## A/B Testing

**Pre-experiment:**
- Define primary metric and guardrail metrics
- Power calculation: sample size needed for 80% power at alpha=0.05
- Minimum detectable effect: what improvement is worth shipping?
- Duration estimate: based on daily traffic and required sample size

**During experiment:**
- Do not peek at results and make decisions (inflates false positives)
- Monitor guardrail metrics only (latency, error rate) — intervene only for regressions
- Set the end date before starting and honour it

**Post-experiment:**
- Report confidence intervals, not just p-values
- Check for segment-level effects: does it help power users but hurt new users?
- Practical significance check: "Is this improvement large enough to justify the complexity?"
- Document the result regardless of outcome — negative results prevent repeat experiments

**Statistical tests:**
- Proportions (conversion rate, success rate): chi-squared test or z-test
- Continuous metrics (latency, revenue): t-test or Mann-Whitney U
- Multiple comparisons: apply Bonferroni correction or use a sequential testing framework

## Evaluation Pipeline

```
Development:    Automated metrics on eval dataset (fast, every prompt change)
                        ↓ passes threshold
Staging:        LLM-as-judge on expanded dataset (medium, every release)
                        ↓ passes threshold
Production:     A/B test with real users (slow, major changes only)
                        ↓ statistically significant improvement
Ship:           Monitor quality metrics continuously (ongoing)
```

**Regression testing:** Run the full eval suite on every prompt or model change. Any score drop > 5% blocks deployment. Track scores over time in a dashboard.
