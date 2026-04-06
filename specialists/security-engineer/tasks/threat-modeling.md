### Threat Modeling

**Use when:** A new system, feature, or integration is being designed and needs security analysis before development begins. Also use when an existing system has never been formally threat-modeled.

**Gather:**
- System description: what does it do, who uses it, what data does it handle?
- Architecture diagram or description (components, APIs, data stores, external services)
- Existing security controls (auth, encryption, firewalls, WAF)
- Compliance requirements (PCI-DSS, HIPAA, SOC2, GDPR) if applicable

---

**Step 1 — Identify assets and entry points:**
- List all valuable assets: user data, credentials, API keys, business logic, financial data
- Map every entry point: public APIs, admin interfaces, webhooks, file uploads, WebSocket connections
- Identify data sensitivity levels: public, internal, confidential, restricted

**Step 2 — Draw trust boundaries:**
- Separate zones: public internet, DMZ, application tier, data tier, third-party services
- Mark every point where data crosses a trust boundary
- Each boundary crossing is a potential attack surface
- Note: trust boundaries exist inside applications too (user input vs server logic, client vs API)

**Step 3 — Apply STRIDE analysis:**

For each component and data flow, evaluate all six threat categories:

| Threat | Question | Example |
|---|---|---|
| **S**poofing | Can an attacker pretend to be someone/something else? | Forged JWT, session hijacking, DNS spoofing |
| **T**ampering | Can data be modified in transit or at rest? | Man-in-the-middle, SQL injection, unsigned cookies |
| **R**epudiation | Can a user deny performing an action? | Missing audit logs, unsigned transactions |
| **I**nformation Disclosure | Can sensitive data leak? | Error messages with stack traces, verbose API responses, log files with PII |
| **D**enial of Service | Can the system be made unavailable? | Unbounded queries, resource exhaustion, regex DoS |
| **E**levation of Privilege | Can a user gain unauthorized access? | IDOR, privilege escalation, insecure direct object references |

**Step 4 — Prioritise threats:**

Use a likelihood x impact matrix:

| | Low Impact | Medium Impact | High Impact |
|---|---|---|---|
| **High Likelihood** | MEDIUM | HIGH | CRITICAL |
| **Medium Likelihood** | LOW | MEDIUM | HIGH |
| **Low Likelihood** | LOW | LOW | MEDIUM |

- Likelihood: consider attacker skill required, access needed, and whether exploit is public
- Impact: consider data loss, financial damage, reputational harm, regulatory penalties

**Step 5 — Define mitigations:**

For each HIGH and CRITICAL threat:
1. Describe the specific mitigation (not generic advice)
2. Identify which component implements it
3. State the residual risk after mitigation
4. Assign ownership (team/person responsible)

For MEDIUM and LOW threats:
- Document and accept, or schedule for future hardening
- Never ignore — acknowledged risk is managed risk

**Output — Threat Model Document:**

```markdown
# Threat Model: [System Name]

## Scope
[What is being modeled, what is excluded]

## Assets
[Numbered list of assets with sensitivity levels]

## Trust Boundaries
[Diagram or description of trust boundary map]

## Threat Analysis
| ID | Component | STRIDE Category | Threat | Likelihood | Impact | Severity | Mitigation | Status |
|---|---|---|---|---|---|---|---|---|

## Accepted Risks
[Threats acknowledged but not mitigated, with justification]

## Recommendations
[Prioritised list of security improvements]
```
