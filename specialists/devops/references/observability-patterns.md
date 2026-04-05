# Observability Patterns

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

---

## The Three Pillars

| Pillar | What it captures | When to use | Key tools |
|--------|-----------------|-------------|-----------|
| **Logs** | Discrete events with context | Debugging specific requests, audit trails, business events | ELK, Loki, CloudWatch Logs, Cloud Logging |
| **Metrics** | Numeric time-series data | Dashboards, alerting, capacity planning, SLO tracking | Prometheus, Datadog, CloudWatch Metrics, Cloud Monitoring |
| **Traces** | Request flow across services | Latency debugging, dependency mapping, bottleneck identification | Jaeger, Zipkin, X-Ray, Cloud Trace, Tempo |

**Relationship:** Logs tell you *what* happened. Metrics tell you *how much*. Traces tell you *where* (across services). Use correlation IDs to link all three for a single request.

---

## Structured Logging `[HYPOTHESIS]`

**Format:** JSON. Always. No unstructured text in production.

**Mandatory fields:**

| Field | Purpose | Example |
|-------|---------|---------|
| `timestamp` | When (ISO 8601, UTC) | `2026-04-05T10:23:45.123Z` |
| `level` | Severity | `INFO`, `ERROR` |
| `message` | Human-readable description | `Payment processed` |
| `correlation_id` | Links logs across services for one request | `req-abc-123` |
| `service` | Which service emitted the log | `payment-api` |
| `trace_id` | Links to distributed trace | `4bf92f3577b34da6` |

**Optional but recommended:**
- `user_id` — who triggered the action (redact PII in logs)
- `duration_ms` — how long the operation took
- `error.type`, `error.message`, `error.stack` — structured error context

**Example:**
```json
{
  "timestamp": "2026-04-05T10:23:45.123Z",
  "level": "ERROR",
  "message": "Payment charge failed",
  "service": "payment-api",
  "correlation_id": "req-abc-123",
  "trace_id": "4bf92f3577b34da6",
  "user_id": "usr-456",
  "error": {
    "type": "StripeCardDeclined",
    "message": "Card was declined"
  },
  "duration_ms": 342
}
```

---

## Log Levels `[HYPOTHESIS]`

| Level | Meaning | Production default | Action required |
|-------|---------|-------------------|-----------------|
| **ERROR** | Something failed; action required | Yes | Investigate; may page on-call |
| **WARN** | Degraded but functional; potential problem | Yes | Review in next business day |
| **INFO** | Business events, request lifecycle | Yes | No action; used for dashboards and audit |
| **DEBUG** | Development diagnostics | **No** — never in prod default | Enable temporarily per-service for debugging |

**Rules:**
- ERROR must be actionable — if no one needs to do anything, it is WARN or INFO
- Do not log PII (email, SSN, full card number) at any level
- Do not log secrets, tokens, or passwords at any level — even at DEBUG
- Rate-limit repeated identical log lines (log once + count, not 10,000 identical lines)

---

## Distributed Tracing `[HYPOTHESIS]`

**Propagation standard:** W3C Trace Context (`traceparent` / `tracestate` HTTP headers). Do not invent custom headers.

**What to instrument:**
- [ ] HTTP server ingress (auto-instrumented by most frameworks)
- [ ] HTTP client egress (outbound calls to other services)
- [ ] Database queries (as child spans with sanitised query text)
- [ ] Message queue publish/consume (propagate trace context in message headers)
- [ ] Cache operations (as child spans, especially cache misses)

**Span naming convention:**
```
HTTP <METHOD> <route>     →  HTTP GET /api/v2/orders
DB <operation> <table>    →  DB SELECT orders
QUEUE <action> <topic>    →  QUEUE PUBLISH payment.completed
```

**Key span attributes:**
- `http.status_code` — response status
- `db.statement` — sanitised query (no user data)
- `error` — boolean; set to true on failure
- `duration_ms` — span duration

**Sampling strategy:**
- 100% of errors and slow requests (> P95 latency)
- 1-10% of successful requests (adjust based on volume and cost)
- Always sample the full trace if any span in the trace is sampled (head-based sampling)

---

## Alerting Anti-Patterns `[HYPOTHESIS]`

| Anti-pattern | Problem | Fix |
|-------------|---------|-----|
| **Alert fatigue** | > 5 pages/week per team; on-call ignores alerts | Audit and delete low-signal alerts; merge related alerts; tune thresholds |
| **Alerting on causes** | "CPU > 80%" pages but users are fine | Alert on symptoms: error rate, latency, SLO burn rate |
| **Missing runbook** | On-call gets paged with no context on what to do | Every alert must link to a runbook; no runbook = no alert |
| **Flapping alerts** | Alert fires and resolves repeatedly in minutes | Add hysteresis: require condition sustained for N minutes before firing |
| **Too many recipients** | Everyone gets every alert; no one owns any alert | Route alerts to the owning team only; use escalation policies |
| **Stale alerts** | Alerts for services that no longer exist or have changed | Review all alerts quarterly; delete orphaned alerts |

**Alerting checklist for new services:**
- [ ] Alert on error rate > SLO burn rate (e.g., 10x burn = page, 2x burn = ticket)
- [ ] Alert on latency P99 > SLO target sustained for 5+ minutes
- [ ] Alert on zero traffic (service may be down but not erroring)
- [ ] Every alert has: severity, owning team, runbook link, expected response time
- [ ] Test the alert fires correctly before enabling in production

---

## Quick-Reference: Observability Smell → Fix

| Smell | Fix |
|-------|-----|
| Unstructured log lines (`console.log("error: " + msg)`) | Switch to structured JSON logger with mandatory fields |
| No correlation ID across services | Generate at ingress, propagate in headers, include in all logs |
| Dashboards but no alerts | Add SLO-based alerts; dashboards are for investigation, not detection |
| Alerts but no runbooks | Write runbook for every alert before enabling it |
| Traces exist but no one uses them | Link trace IDs in error logs; train team to start debugging from traces |
| DEBUG logging in production by default | Set production default to INFO; enable DEBUG per-service via config |
