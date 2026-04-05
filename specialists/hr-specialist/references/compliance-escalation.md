# Compliance Escalation Protocol

> Quick-reference for HR compliance risk assessment, jurisdiction-specific gotchas, and escalation to lawyer specialist.

---

## Decision Tree: Is This HIGH / MEDIUM / LOW Risk?

```
START: Is this a compliance-sensitive action?
  (hiring, termination, leave, policy change, investigation)
  |
  +-- Does it involve a protected class characteristic?
  |     YES --> HIGH
  |
  +-- Is there potential legal liability or litigation risk?
  |     YES --> HIGH
  |
  +-- Is it a termination for cause or workplace investigation?
  |     YES --> HIGH
  |
  +-- Is there policy interpretation ambiguity?
  |     YES --> MEDIUM
  |
  +-- Does it span multiple jurisdictions?
  |     YES --> MEDIUM
  |
  +-- Is it an accommodation or adjustment request?
  |     YES --> MEDIUM
  |
  +-- Is the policy clear, no protected class involved, standard process?
        YES --> LOW
```

**HIGH** = Escalate to lawyer specialist before proceeding. Do not advise the client to act.
**MEDIUM** = Provide guidance with explicit "verify with local counsel" flag. Note jurisdictional uncertainty.
**LOW** = Proceed with standard HR methodology.

---

## Always-Escalate Triggers

These situations must always go to the lawyer specialist regardless of other factors:

- Termination of employee in a protected class
- Workplace harassment or discrimination complaint
- Whistleblower or retaliation claim
- Multi-jurisdiction compliance conflict
- Class or collective action risk
- Regulatory audit or government inquiry

---

## Jurisdiction-Specific Gotchas

| Jurisdiction | Area | Gotcha | Consequence If Missed |
|---|---|---|---|
| **UK** | IR35 / off-payroll | Client responsible for determining contractor status since April 2021 (medium/large employers) | HMRC liability for PAYE, NICs + penalties |
| **UK** | Redundancy consultation | 20+ redundancies in 90 days requires 45-day collective consultation with employee reps | All dismissals automatically unfair; protective award up to 90 days' pay per employee |
| **UK** | Unfair dismissal | 2+ years' service = right not to be unfairly dismissed; must follow ACAS Code | 25% tribunal uplift for failure to follow ACAS Code |
| **UK** | TUPE | Business transfer = employees transfer on existing terms; cannot change terms by reason of transfer | Automatic unfair dismissal |
| **US** | At-will exceptions | Handbook language can create implied contracts overriding at-will status | Wrongful termination claims |
| **US** | FMLA | 12 weeks unpaid leave for qualifying employees (50+ employees within 75 miles); job must be held | Interference and retaliation claims; individual manager liability |
| **US** | Worker classification | IRS 20-factor test; ABC test in CA, MA, NJ; state tests vary | Back taxes, penalties, benefits liability, class action risk |
| **US** | State-specific laws | CA: meal/rest break requirements, final pay due on termination day; NY: salary transparency; IL: pay data reporting | State-specific penalties; CA penalties compound fast |
| **EU** | Works council | Many EU countries require works council consultation before collective redundancy, policy changes, or restructuring | Decisions can be voided; fines; employee claims |
| **EU** | GDPR for HR data | Need lawful basis for processing employee data; data minimisation; retention limits; DPIA for monitoring | Fines up to 4% of global turnover |
| **EU** | Fixed-term contracts | Many EU countries limit successive fixed-term contracts (typically 2-3 renewals or 2-4 years total) | Automatic conversion to permanent employment |
| **AU** | Unfair dismissal | Employees with 6+ months' service (or 12 months in small business) can claim unfair dismissal via Fair Work Commission | Reinstatement or compensation up to 26 weeks' pay |
| **AU** | Modern Awards | 120+ industry/occupation awards set minimum pay, conditions, overtime, penalties | Underpayment claims; Fair Work Ombudsman prosecution |
| **AU** | Sham contracting | Employer cannot dismiss and re-engage as contractor to avoid entitlements | Penalties per contravention; back-payment of entitlements |
| **AU** | Redundancy consultation | Genuine redundancy defence requires consultation with employees and consideration of redeployment | Unfair dismissal claim succeeds if process not followed |

---

## Escalation Handoff Template

Use this format when escalating to the lawyer specialist:

```markdown
## HR Compliance Escalation

**Risk Level:** HIGH / MEDIUM
**Urgency:** Immediate / This week / Planning phase

### Situation
[2-3 sentences: what happened, who is involved, what decision needs to be made]

### Jurisdiction
- Country/State: [specify]
- Employee tenure: [length of service]
- Company size: [headcount — relevant for thresholds]
- Employment type: [permanent / fixed-term / contractor]

### Specific Legal Question
[What exactly do we need the lawyer to determine? Be precise.]

### Escalation Triggers Present
- [ ] Protected class involvement
- [ ] Harassment/discrimination complaint
- [ ] Whistleblower/retaliation risk
- [ ] Multi-jurisdiction conflict
- [ ] Class/collective action risk
- [ ] Regulatory inquiry

### Documents to Provide
- [ ] Employment contract
- [ ] Relevant policy documents
- [ ] Correspondence / evidence
- [ ] Previous warnings or performance records
- [ ] Timeline of events

### HR Recommendation (with caveats)
[What HR would recommend, with explicit statement that this is subject to legal review and should not be acted on until lawyer confirms]
```

---

## Key Thresholds to Remember

| Threshold | Jurisdiction | What Triggers |
|---|---|---|
| 2 years' service | UK | Unfair dismissal rights activate |
| 20 redundancies in 90 days | UK | Collective consultation obligation (45 days) |
| 50 employees | US | FMLA applies |
| 15 employees | US | Title VII (discrimination) applies |
| 20 employees | US | ADEA (age discrimination) applies |
| 100 employees | US | WARN Act (60-day notice for mass layoffs) |
| 6 months' service | AU | Unfair dismissal rights (large employer) |
| 12 months' service | AU | Unfair dismissal rights (small business) |
| 15 employees | AU | Unfair dismissal jurisdiction threshold |
