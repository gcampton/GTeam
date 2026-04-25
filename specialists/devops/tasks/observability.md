## Monitoring & Observability

**RED method (for every service):**

| Metric | What it measures | Alert when |
|--------|-----------------|------------|
| **Rate** | Requests per second | Drops > 50% from baseline |
| **Errors** | Error rate as % of total requests | Exceeds SLO error budget burn rate |
| **Duration** | Latency P50 / P95 / P99 | P99 > SLO target for sustained period |

**USE method (for infrastructure):**

| Metric | What it measures | Alert when |
|--------|-----------------|------------|
| **Utilisation** | % of resource capacity in use | CPU > 80%, memory > 85%, disk > 90% |
| **Saturation** | Queue depth, waiting threads | Queue depth growing over time |
| **Errors** | Hardware/system errors | Any non-zero error count |

**Key metrics to instrument:**
- [ ] Latency: P50, P95, P99 per endpoint
- [ ] Error rate: % of 5xx responses
- [ ] Saturation: request queue depth, DB connection pool usage, CPU, memory
- [ ] Throughput: requests/sec per service

**Alerting rules:**
- Page on **symptoms** (users affected) not **causes** (CPU high)
- Alert on **SLO burn rate** not raw thresholds — a brief spike is fine; sustained burn is not
- Every alert must have a **runbook link** — if there is no runbook, write one before enabling the alert
- Target: < 5 pages per week per team; more = alert fatigue, fix the alerts

**Dashboard hierarchy:**
1. **Service overview** — golden signals (rate, errors, duration) for all services on one screen
2. **Per-endpoint** — drill into individual endpoints, latency breakdown, error types
3. **Infrastructure** — CPU, memory, disk, network per node/pod
4. **Business metrics** — signups, orders, revenue (detect impact even when infra looks healthy)
