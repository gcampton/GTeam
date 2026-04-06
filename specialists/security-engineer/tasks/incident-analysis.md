### Incident Analysis

**Use when:** A security incident has occurred or is suspected — breach, data leak, unauthorized access, malware, or anomalous behaviour. Also use for post-incident review and remediation verification.

**Gather:**
- What was detected? (alert, user report, anomaly, external notification)
- When was it detected? When did it likely start?
- What systems are affected?
- What containment actions have already been taken?
- Is the incident still active?

---

**Step 1 — Triage and classify severity:**

| Severity | Criteria | Response time |
|---|---|---|
| **CRITICAL** | Active data exfiltration, production compromise, credential theft at scale | Immediate — all hands |
| **HIGH** | Unauthorized access confirmed, vulnerability actively exploited, PII exposed | Within 1 hour |
| **MEDIUM** | Suspicious activity, potential compromise not confirmed, minor data exposure | Within 4 hours |
| **LOW** | Policy violation, failed attack attempt, security misconfiguration discovered | Within 24 hours |

**Step 2 — Contain the incident:**

Containment before investigation — stop the bleeding:
- Revoke compromised credentials immediately
- Isolate affected systems (network segmentation, disable accounts)
- Preserve evidence before making changes (snapshot VMs, export logs, copy artifacts)
- Document every containment action with timestamp

**Evidence preservation:**
- Take disk snapshots before any remediation
- Export and save relevant logs (application, access, audit, network)
- Screenshot any anomalous UI states or error messages
- Record the exact state of affected systems (running processes, network connections, file modifications)
- Maintain chain of custody — who accessed what evidence, when

**Step 3 — Root cause analysis:**

Use the 5 Whys adapted for security:

1. **What happened?** — Describe the incident in one factual sentence
2. **How did the attacker get in?** — Initial access vector (phishing, exploit, credential stuffing, insider)
3. **Why was this possible?** — What security control was missing or failed?
4. **Why was that control missing?** — Process gap, oversight, technical debt, budget constraint?
5. **What systemic issue enabled this?** — Culture, training, tooling, architecture decision

Stop when you reach a systemic cause that, if fixed, would prevent this class of incident.

**Step 4 — Assess blast radius:**

- What data was accessed or exfiltrated? Classify its sensitivity
- How many users/records are affected?
- Was the attacker's access lateral (did they pivot to other systems)?
- Are there persistence mechanisms (backdoors, new accounts, scheduled tasks)?
- Is there regulatory notification required? (GDPR: 72 hours, various US state laws)

**Step 5 — Remediate and verify:**

For each root cause identified:
1. Implement the fix
2. Verify the fix blocks the original attack vector
3. Check for similar vulnerabilities in related systems
4. Add monitoring/alerting to detect recurrence

Verification must be demonstrated, not assumed:
- Re-test the original attack vector — confirm it fails
- Review logs to confirm no ongoing suspicious activity
- Validate all compromised credentials have been rotated
- Confirm persistence mechanisms are removed

**Output — Post-Incident Report:**

```markdown
# Security Incident Report

**Incident ID:** [unique identifier]
**Date detected:** [date/time]
**Date resolved:** [date/time]
**Severity:** [CRITICAL/HIGH/MEDIUM/LOW]
**Status:** [Active/Contained/Resolved/Post-mortem complete]

## Summary
[2-3 sentences: what happened, impact, current status]

## Timeline
| Time | Event |
|---|---|
| [timestamp] | [what happened] |

## Root Cause
[5 Whys analysis results — the systemic cause]

## Impact
- Data affected: [type, volume, sensitivity]
- Users affected: [count, notification status]
- Systems affected: [list]
- Regulatory implications: [notification requirements]

## Containment Actions Taken
[Numbered list with timestamps]

## Remediation
| Action | Owner | Status | Verified |
|---|---|---|---|
| [fix] | [person/team] | [done/in-progress] | [yes/no] |

## Lessons Learned
1. [What went well in the response]
2. [What could be improved]
3. [Systemic changes to prevent recurrence]

## Follow-up Items
- [ ] [Action item with owner and deadline]
```
