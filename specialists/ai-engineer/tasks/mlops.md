### Model Deployment

**Serving options by use case:**

| Option | Best For | Latency | Scaling | Complexity |
|---|---|---|---|---|
| Managed API (Claude, OpenAI) | Most production use cases | Medium (100-2000ms) | Automatic | Low |
| Self-hosted API (vLLM, TGI) | Data sovereignty, custom models, cost at scale | Low-Medium | Manual | High |
| FastAPI wrapper | Custom models, preprocessing pipelines | Low | Manual (+ load balancer) | Medium |
| Serverless (Lambda, Cloud Functions) | Low-traffic, bursty workloads | High (cold start) | Automatic | Low |
| Edge deployment (ONNX, TensorRT) | On-device inference, ultra-low latency | Very Low | N/A | High |

**Self-hosting decision:** Only self-host if you need data sovereignty, have > 1M requests/month (cost savings), or need a fine-tuned open-source model. Otherwise, managed APIs are cheaper when you account for engineering time.

**Deployment checklist:**
- [ ] Health check endpoint (`/health`) that verifies model is loaded and responding
- [ ] Graceful shutdown: finish in-flight requests before stopping
- [ ] Request timeout: kill requests that exceed the SLA (e.g., 30s)
- [ ] Input validation: reject malformed requests before they hit the model
- [ ] Output validation: verify model output before returning to caller
- [ ] Rate limiting: protect the model from traffic spikes
- [ ] Authentication: API key or OAuth on all endpoints

---

### Monitoring

**The four pillars of AI system monitoring:**

**1. Latency:**
- Track P50, P95, P99 per endpoint and per model
- Set alerts: P95 > 2x baseline = degradation warning; P99 > 5x = critical
- Break down: network time vs model inference time vs pre/post-processing
- Time-to-first-token (TTFT) for streaming responses

**2. Error rates:**
- HTTP errors (4xx, 5xx) by endpoint
- Model-specific errors: rate limits, content filters, timeouts, malformed output
- Downstream errors: failures in systems that consume model output
- Alert threshold: error rate > 1% sustained for 5 minutes

**3. Cost:**
- Token usage per request (input tokens, output tokens, cached tokens)
- Cost per request by model and endpoint
- Daily and monthly spend with budget alerts at 50%, 80%, 100%
- Cost per user/customer for unit economics

**4. Quality:**
- Output quality score (automated eval on a sample of production traffic)
- User feedback signals: thumbs up/down, regeneration rate, task completion
- Drift detection: compare current output distribution against baseline
- Alert on quality score drop > 10% week-over-week

---

### A/B Testing Models

**Traffic splitting:**
- Use feature flags or a routing layer to split traffic between model versions
- Start with 5-10% to the new model, ramp up if metrics hold
- Ensure random, consistent assignment (hash user ID, not random per-request)

**What to measure:**
- Primary metric: task success rate or user satisfaction score
- Guardrail metrics: latency, error rate, cost — must not regress
- Statistical significance: run until you have 95% confidence (use a power calculator)
- Minimum detectable effect: decide upfront what improvement is worth shipping

**Common mistakes:**
- Stopping too early (peeking): use sequential testing if you must check early
- Ignoring latency differences: a better model that's 3x slower may hurt overall UX
- Not segmenting: check results by user type, query type, and complexity — aggregate results hide problems

---

### Model Versioning

**What to version (all of these change output):**
- Prompt templates (version string in template file, e.g., `v2.3`)
- Model identifier (e.g., `claude-sonnet-4-20250514` — pin exact versions, never use `latest`)
- System configuration: temperature, max_tokens, top_p, tool definitions
- Evaluation snapshots: scores for each version on the eval suite

**Version tracking schema:**
```
{
  "deployment_id": "deploy-2024-03-15-001",
  "model": "claude-sonnet-4-20250514",
  "prompt_version": "v2.3",
  "config": { "temperature": 0, "max_tokens": 1024 },
  "eval_score": 0.87,
  "deployed_at": "2024-03-15T10:00:00Z",
  "deployed_by": "engineer@company.com"
}
```

**Rollback plan:** Every deployment must have a one-command rollback to the previous version. Test the rollback before you need it.

---

### Data Pipeline

**Training data management:**
- Version training datasets alongside model versions
- Track data provenance: where did each training example come from?
- Data quality checks: duplicates, label consistency, class balance
- PII detection and redaction before any data enters the training pipeline

**Feedback loops:**
- Collect user corrections and feedback as potential training data
- Human review pipeline: sample production outputs, label quality, feed back into evals
- Fine-tuning trigger: when you have 500+ validated corrections in a category, consider fine-tuning

**Data flywheel:**
```
Production traffic → Sample outputs → Human review → Labelled dataset
                                                          ↓
                                      Eval suite update ← Fine-tuning trigger
```

---

### Observability

**Logging requirements (every model call):**
- Request ID / trace ID (for multi-step chains, use a correlation ID)
- Model, prompt version, parameters used
- Input tokens, output tokens, latency
- Output (with PII redaction — never log raw user data)
- Success/failure status and error type if failed

**PII redaction (mandatory):**
- Detect and mask PII before logging: names, emails, phone numbers, addresses, SSNs
- Use regex patterns + NER model for detection
- Log redacted versions only — original data stays in the request/response, not in logs
- Audit: who accessed raw logs, when, and why

**Trace visualisation for multi-step chains:**
```
[User Query] → [Router] → [Retrieval] → [Re-rank] → [Generation] → [Validation] → [Response]
   trace_id=abc  12ms       45ms          120ms        890ms           15ms           total: 1082ms
```

- Each step logs its trace ID, parent ID, duration, and status
- Visualise in Jaeger, Honeycomb, or Langfuse for debugging
- Alert on chains where total latency > SLA or any step fails
