# Incident Response Reference

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Use this document when an incident is declared. In the heat of an incident, go to the section you need — do not read top to bottom.

---

## Severity Levels & Response SLAs

| Level | Criteria | Response time | Example |
|-------|----------|--------------|---------|
| **P0** | Site down, data loss, security breach in progress | 15 minutes | Login broken for all users; production DB inaccessible; credentials leaked |
| **P1** | Major feature broken, significant user impact | 1 hour | Payments failing; checkout broken; primary dashboard not loading |
| **P2** | Degraded experience, workaround exists | 4 hours | Search slow; exports timing out; non-critical email not sending |
| **P3** | Minor issue, minimal user impact | Next business day | Cosmetic bug; edge-case error for <1% of users; internal tool broken |

**Response time** = time from detection to an on-call engineer actively investigating.

### Escalation `[HYPOTHESIS]`
- P0: page immediately, escalate to engineering lead within 15 min if not resolved
- P1: page on-call; notify engineering lead if not resolved within 30 min
- P2: Slack notification to team; no page required unless it becomes P1
- P3: create ticket; no page, no Slack alert required

---

## Investigation Checklist

Run through this in order. Each step takes < 2 minutes. Do not skip ahead. `[HYPOTHESIS]`

### Step 1 — Check Monitoring
- [ ] Open primary monitoring dashboard (Datadog / Grafana / CloudWatch)
- [ ] Check error rate: is it elevated above baseline?
- [ ] Check latency P50, P95, P99: is anything spiking?
- [ ] Check saturation: CPU, memory, disk, DB connection pool — any at limits?
- [ ] Check logs for ERROR / FATAL / exception patterns in the last 15 minutes

### Step 2 — Check Recent Deploys
- [ ] What was deployed in the last 2 hours? (check CI/CD deploy log, git tag history)
- [ ] Does the incident start time correlate with a deploy?
- [ ] If yes: strongly consider rollback before further investigation (see rollback decision tree)

### Step 3 — Check Infrastructure
- [ ] All instances/pods healthy and running?
- [ ] Load balancer health checks passing?
- [ ] Database replication lag (if applicable)
- [ ] Message queue depth / consumer lag
- [ ] Certificate expiry (check for SSL errors in logs)

### Step 4 — Check External Dependencies
- [ ] Third-party API status pages (Stripe, Twilio, SendGrid, AWS status, etc.)
- [ ] DNS resolution working?
- [ ] CDN / edge cache behaving correctly?
- [ ] Is the incident isolated to one region, one cloud zone, or one dependency?

---

## Rollback Decision Tree

```
Is there a deploy in the last 2 hours that correlates with the incident?
├── YES → Can you roll back without DB migration issues?
│   ├── YES → ROLLBACK NOW (git revert + redeploy, or re-deploy previous image)
│   └── NO → Is a forward-fix possible in < 30 min?
│       ├── YES → HOTFIX (create hotfix branch, fix, fast-track review, deploy)
│       └── NO → Can a feature flag hide the problem?
│           ├── YES → DISABLE FEATURE FLAG, then hotfix
│           └── NO → ROLLBACK with manual DB migration reversal (document steps)
└── NO → Is the problem in infra / config, not code?
    ├── YES → Restore previous infra state (Terraform apply, config revert)
    └── NO → INVESTIGATE further before taking action
```

**When in doubt, rollback first.** A rollback that turns out to be unnecessary costs minutes. A delayed rollback during a P0 costs users and trust. `[HYPOTHESIS]`

---

## Communication Templates

### Status Page Update

**Initial (post within 5 min of P0/P1 declaration):**
```
Investigating: We are aware of an issue affecting [feature/service].
Our team is actively investigating. We will provide an update within 30 minutes.
```

**Update (every 30 min until resolved for P0/P1):**
```
Update [HH:MM UTC]: We have identified the cause as [brief description].
We are [action being taken]. Estimated resolution: [time or "unknown"].
```

**Resolved:**
```
Resolved [HH:MM UTC]: The issue affecting [feature/service] has been resolved.
[Brief explanation of what happened and what was done.]
A post-mortem will be published within [48–72 hours].
```

---

### Internal Slack / Team Alert

**P0 Slack message:**
```
:red_circle: P0 INCIDENT — [short title]

Impact: [who/what is affected]
Started: [HH:MM UTC]
Incident lead: @[name]
Bridge/thread: [link]

Current status: Investigating
```

**P1 Slack message:**
```
:large_orange_circle: P1 — [short title]

Impact: [who/what is affected]
Owner: @[name]
Ticket: [link]

Status: Investigating
```

**Resolution:**
```
:white_check_mark: RESOLVED — [short title]
Duration: [X] minutes
Fix: [one sentence]
Post-mortem: [link or "TBD"]
```

---

### Stakeholder Email (P0/P1 only) `[HYPOTHESIS]`

**Subject:** `[Resolved/Ongoing] Service disruption — [feature] — [date]`

```
Hi [name / team],

[ONGOING: We are currently experiencing / RESOLVED: We experienced] an issue
with [service/feature] from [start time] [to [end time]].

Impact:
- [Bullet: what users could not do]
- [Bullet: estimated number of users affected, if known]

Current status: [Investigating / Identified / Resolved]

Next update: [time, or "issue is resolved, no further updates planned"]

If you have questions, contact [on-call rotation or email].

[Your name]
```

---

## Post-Mortem Structure

Post-mortems are blameless. The goal is to improve systems and processes, not to assign fault. `[HYPOTHESIS]`

Write within 48–72 hours of a P0 or P1. P2s warrant a post-mortem at team discretion.

### Template

```markdown
# Post-Mortem: [Title]

**Date:** [incident date]
**Severity:** P0 / P1
**Duration:** [start time] → [end time] ([X] minutes)
**Author(s):** [names]
**Status:** Draft / Final

---

## Summary
[2–3 sentence summary: what broke, why, what was the impact, how was it fixed.]

---

## Timeline

| Time (UTC) | Event |
|------------|-------|
| HH:MM | Monitoring alert fired |
| HH:MM | On-call notified |
| HH:MM | Investigation started |
| HH:MM | Root cause identified |
| HH:MM | Fix deployed / rollback initiated |
| HH:MM | Service restored |
| HH:MM | Incident closed |

---

## Root Cause
[Single clear sentence describing the root technical cause.]

[Elaboration: 1–3 paragraphs. Explain the mechanism, not the blame.]

---

## Contributing Factors
- [Factor 1: e.g., "Missing alerting on this specific error class"]
- [Factor 2: e.g., "Deploy lacked a smoke test for this code path"]
- [Factor 3: e.g., "On-call rotation did not include someone familiar with this service"]

---

## What Went Well
- [e.g., "Rollback was executed within 8 minutes"]
- [e.g., "Communication to stakeholders was timely"]

---

## What Went Poorly
- [e.g., "Alert took 20 minutes to fire after problem started"]
- [e.g., "Runbook was out of date"]

---

## Action Items

| Item | Owner | Due date | Status |
|------|-------|----------|--------|
| Add integration test for [scenario] | @name | [date] | Open |
| Update runbook for [service] | @name | [date] | Open |
| Add alert for [metric] threshold | @name | [date] | Open |
| Review deploy process for [service] | @name | [date] | Open |

---

## Lessons Learned
[Optional: broader lessons beyond the specific action items.]
```

### Post-Mortem Review Checklist `[HYPOTHESIS]`

- [ ] Timeline is accurate and complete (verify against logs/alert history)
- [ ] Root cause is a system/process issue, not a person
- [ ] Action items are specific, assigned, and time-bound — not vague ("improve monitoring")
- [ ] "What went well" is included — learning from successes is as important as failures
- [ ] Document is shared with the broader team after review, not buried in a private channel

---

## Quick-Reference: Severity → First Action

| Severity | First action within |
|----------|-------------------|
| P0 | Page on-call, post initial status page update | 5 min |
| P1 | Notify team in Slack, open incident thread | 15 min |
| P2 | Create ticket, note in team standup | Same day |
| P3 | Create ticket | Next sprint |
