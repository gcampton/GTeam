### Secure Architecture Design

**Use when:** Designing or reviewing the security architecture of a system — authentication, authorization, data protection, network security, or secure defaults.

**Gather:**
- System purpose and user types (end users, admins, API consumers, internal services)
- Data classification: what data is stored, its sensitivity level
- Deployment environment (cloud provider, on-prem, hybrid)
- Compliance requirements if any (SOC2, PCI-DSS, HIPAA, GDPR)
- Existing architecture to build on (or greenfield)

---

**Step 1 — Authentication design:**

Select the right pattern for the use case:

| Pattern | Best for | Watch out for |
|---|---|---|
| **Session-based** | Traditional web apps, server-rendered pages | Session fixation, CSRF, cookie security flags |
| **JWT (stateless)** | SPAs, mobile apps, microservices | Token size, revocation difficulty, secret management |
| **OAuth 2.0 + OIDC** | Third-party login, delegated auth, enterprise SSO | Complexity, redirect URI validation, state parameter |
| **API keys** | Server-to-server, developer APIs | Key rotation, rate limiting, scope restriction |
| **mTLS** | Service mesh, zero-trust internal comms | Certificate management, rotation automation |

For every auth system, require:
- Password policy: minimum 12 chars, check against breach databases, no complexity rules (NIST 800-63B)
- MFA support: TOTP or WebAuthn preferred, SMS as fallback only
- Account lockout: progressive delays, not hard lockout (prevents DoS)
- Session management: secure cookie flags (HttpOnly, Secure, SameSite=Lax), rotation on privilege change

**Step 2 — Authorization design:**

| Model | Best for | Trade-offs |
|---|---|---|
| **RBAC** (Role-Based) | Most applications, clear role hierarchy | Role explosion in complex systems |
| **ABAC** (Attribute-Based) | Fine-grained, context-aware access | Complex policy management |
| **Policy-based** (OPA/Cedar) | Microservices, auditable decisions | Learning curve, latency |
| **ACL** (Access Control List) | File systems, document-level access | Doesn't scale to complex hierarchies |

Key principles:
- Default deny — access must be explicitly granted
- Least privilege — grant minimum permissions for the task
- Separation of duties — no single role should control an entire critical flow
- Check authorization on every request, server-side, never trust client claims

**Step 3 — Data protection:**

**Encryption at rest:**
- Database: use transparent encryption (TDE) or application-level encryption for sensitive fields
- File storage: server-side encryption (SSE-S3, SSE-KMS, or client-side)
- Key management: use a KMS (AWS KMS, GCP KMS, HashiCorp Vault) — never store keys alongside data

**Encryption in transit:**
- TLS 1.2+ for all external communication, TLS 1.3 preferred
- Internal service-to-service: mTLS or encrypted overlay network
- Certificate pinning for mobile apps connecting to known backends

**PII handling:**
- Minimise collection — only collect what you need
- Pseudonymise where possible — separate identifying data from usage data
- Retention policies — define and enforce automatic deletion
- Right to deletion — design for GDPR Article 17 from the start

**Step 4 — Network security:**

Apply defense in depth:
1. **Perimeter:** WAF, DDoS protection, rate limiting at edge
2. **Network segmentation:** Separate public, application, and data tiers
3. **Zero trust:** Authenticate and authorize every request, even internal
4. **Least privilege networking:** Security groups/firewalls allow only required ports and protocols
5. **Egress filtering:** Restrict outbound connections to known destinations

**Step 5 — Secure defaults checklist:**

Every new service or component should ship with:
- [ ] Authentication required on all endpoints (opt-out, not opt-in)
- [ ] HTTPS only, HSTS enabled with preload
- [ ] CORS restricted to known origins (never `*` in production)
- [ ] CSP headers configured (script-src, style-src, frame-ancestors)
- [ ] Rate limiting on authentication and expensive endpoints
- [ ] Input validation on all user-supplied data
- [ ] Structured logging with no PII in logs
- [ ] Dependency pinning with automated vulnerability scanning
- [ ] Secrets in environment variables or secrets manager, never in code

**Output:**

```markdown
# Security Architecture: [System Name]

## Authentication
[Pattern chosen, configuration, MFA approach]

## Authorization
[Model chosen, policy structure, enforcement points]

## Data Protection
[Encryption strategy, key management, PII handling]

## Network Security
[Segmentation, zero trust implementation, firewall rules]

## Secure Defaults Applied
[Checklist status for each item]
```
