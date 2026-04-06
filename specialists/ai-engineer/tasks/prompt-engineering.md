### Prompt Structure

**Anatomy of a production prompt:**

```
System message:     Role, constraints, output format, guardrails
─────────────────────────────────────────────────────
Few-shot examples:  2-3 input/output pairs showing expected behaviour
─────────────────────────────────────────────────────
User message:       The actual request with variables filled in
─────────────────────────────────────────────────────
Chain-of-thought:   "Think step by step" or structured reasoning block
─────────────────────────────────────────────────────
Output format:      JSON schema, XML tags, or structured template
```

**System message design:**
- Lead with the role and core constraint (1-2 sentences)
- Define what the model MUST do and MUST NOT do
- Specify output format explicitly — never leave it ambiguous
- Include edge case handling: "If the input is empty, return {}"
- Keep it under 500 tokens unless you have prompt caching enabled

**Few-shot examples:**
- Minimum 2 examples, maximum 5 (diminishing returns beyond that)
- Include one "tricky" example that demonstrates edge case handling
- Examples should be diverse — don't repeat the same pattern
- Format examples identically to the expected production input/output

---

### Optimisation Workflow

**Baseline → Measure → Iterate → Ship:**

1. **Baseline:** Write the simplest prompt that could work. Do not optimise prematurely.
2. **Measure:** Run against 20-50 test cases. Score with automated metrics or LLM-as-judge. Record the baseline score.
3. **Iterate:** Change ONE thing at a time. Re-run the eval. Keep changes that improve the score; revert those that don't.
4. **A/B test:** In production, split traffic between current and candidate prompt. Measure real-world performance.

**What to iterate on (in order of impact):**
1. Output format specification (most common source of inconsistency)
2. Few-shot examples (quality and diversity)
3. System message constraints (too vague → hallucination; too rigid → refusals)
4. Chain-of-thought instructions (helps reasoning; hurts speed)
5. Temperature and sampling parameters (last resort)

**Version control:** Every prompt is a code artifact. Store prompts in version control with a changelog. Never edit production prompts without running the eval suite.

---

### Production Patterns

**Prompt templates:**
- Use template variables (`{{user_input}}`, `{{context}}`, `{{format}}`) — never string-concatenate user input into prompts
- Validate all template variables before rendering: type check, length check, sanitise
- Template library: maintain a central registry of approved prompt templates

**Prompt regression testing:**
- Maintain a test suite of input/expected-output pairs (minimum 30 cases)
- Run on every prompt change before deploying
- Track scores over time — alert on regressions > 5%
- Include adversarial cases: prompt injection attempts, edge cases, empty inputs

**Multi-step chains:**
- Break complex tasks into discrete steps with clear handoffs
- Each step should have its own prompt with a defined input/output contract
- Validate intermediate outputs between steps — don't let errors cascade
- Add trace IDs for debugging the full chain

---

### Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Over-prompting | 2000-token system message with contradictory rules | Simplify. If you need that many rules, your task is too complex for one prompt |
| Conflicting instructions | "Be concise" + "Provide detailed analysis" | Pick one. Use separate prompts for summary vs detail |
| Prompt injection vulnerability | User input passed directly into system message | Template variables with sanitisation; never put user input in system role |
| Temperature = 0 for creativity | Deterministic sampling kills creative generation | Use temperature 0.7-1.0 for creative tasks, 0 for extraction/classification |
| No output validation | Trust model output and pass it downstream | Always validate: JSON parse, schema check, business rule validation |
| "Be helpful" padding | Generic instructions that add tokens but no signal | Remove filler. Every token in the system message should change behaviour |

---

### Structured Output

**JSON mode:**
- Use provider-native JSON mode when available (Claude tool_use, OpenAI response_format)
- Always provide a JSON schema — don't rely on "return valid JSON"
- Validate output against the schema before processing; retry on validation failure

**Tool use / function calling:**
- Define tools with clear names, descriptions, and parameter schemas
- Prefer tool use over raw JSON extraction — it's more reliable
- Handle the case where the model calls no tool (unexpected refusal)

**Schema enforcement pipeline:**
```
Model output → JSON parse → Schema validation → Business rule validation → Use
                   ↓ fail        ↓ fail              ↓ fail
               Retry (1x)    Log + retry (1x)     Flag for review
```

---

### Evaluation

**Automated scoring (for structured tasks):**
- Exact match: classification, entity extraction, yes/no questions
- F1 / precision / recall: for multi-label or extraction tasks
- BLEU / ROUGE: for summarisation (but correlates poorly with human judgement — use with caution)
- Custom metrics: domain-specific scoring functions (e.g., SQL execution match, code compilation success)

**LLM-as-judge (for open-ended tasks):**
- Use a stronger model to judge a weaker model's output
- Provide clear rubrics: what constitutes a score of 1, 3, 5
- Run each judgement 3 times and take the majority vote (reduces noise)
- Validate the judge: check agreement with human ratings on a sample

**Human evaluation (for high-stakes tasks):**
- Use for final validation, not iteration (too slow for prompt tuning)
- Blind evaluation: evaluators don't know which prompt version generated the output
- Inter-rater reliability: measure agreement between evaluators; calibrate if low
