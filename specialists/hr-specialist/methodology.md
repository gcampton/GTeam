### Browse Setup

When researching salary benchmarks, company reviews, or compliance resources, run this setup block:

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/.claude/skills/gteam/browse/dist/browse
[ -x "$B" ] && echo "READY: $B" || echo "BROWSE NOT AVAILABLE"
```

If `BROWSE NOT AVAILABLE`: use WebSearch + WebFetch for all research steps.

---

### Job Description Writing

**Use when:** Hiring for a new or existing role. A poor JD attracts the wrong candidates and repels good ones.

**Gather:** Role title, reporting line, key responsibilities (top 5–7), must-have qualifications, nice-to-have qualifications, location/remote policy, salary range (or confirm if confidential), company stage (startup/scaleup/enterprise).

**JD structure:**

```markdown
## [Job Title] at [Company]

**Location:** [City / Remote / Hybrid — X days in office]
**Type:** Full-time / Part-time / Contract
**Salary:** [Range if disclosable, or "Competitive + equity"]

### About [Company]
[2–3 sentences: what you do, who you serve, company stage, mission. Not a marketing pitch — candidates vet you.]

### The Role
[One paragraph: what this person will own, why it matters, what success looks like in 90 days]

### What You'll Do
- [Responsibility 1 — action verb + outcome, e.g. "Own the end-to-end product analytics pipeline"]
- [Responsibility 2]
- [5–7 bullets total — not a task list, not a job description from 2010]

### What We're Looking For
**Must have:**
- [Specific, verifiable qualification — not "excellent communication skills"]
- [X years of relevant experience — be honest about the minimum, not aspirational]

**Nice to have:**
- [Would strengthen the candidate but isn't a dealbreaker]

### What We Offer
- [Salary/equity if disclosable]
- [Benefits — specific, not "great culture"]
- [Growth opportunity — specific, not "room to grow"]

### How to Apply
[Clear instructions: what to submit, any screening questions, expected timeline]
```

**Writing rules:**
- Lead with what the person will build or achieve, not what they'll "be responsible for"
- Avoid: "rockstar", "ninja", "passionate", "self-starter" — these are noise
- Use gender-neutral language throughout
- List requirements as "must have" or "nice to have" — never bury dealbreakers in "nice to have"
- Salary range disclosure: include if the jurisdiction requires it (UK, EU, some US states) and if you want better candidates faster

**Deliver:**
- Complete JD (publish-ready)
- Internal scorecard: the 5–7 criteria you'll actually use to evaluate candidates at each stage
- Sourcing channels recommendation (LinkedIn, job boards, communities) based on the role

---

### Interview Framework

**Use when:** Designing a consistent, fair interview process for a role.

**Gather:** Role title, seniority level, key competencies being evaluated (technical skill, leadership, communication, domain knowledge), number of interview stages the team can support.

**Interview stages (standard — adapt per role):**

| Stage | Format | Duration | Owner | Goal |
|-------|--------|----------|-------|------|
| Recruiter screen | Video/phone | 30 min | Recruiter/HR | Motivation, baseline fit, logistics |
| Hiring manager interview | Video/in-person | 45–60 min | HM | Role understanding, culture fit |
| Technical / skills assessment | Task or interview | 60–90 min | Domain expert | Can they actually do the job? |
| Panel interview | In-person or video | 60 min | 2–3 stakeholders | Cross-functional perspective |
| Reference checks | Phone | 20 min × 3 | HR/HM | Validate, don't rubber-stamp |

**Competency-based question framework (STAR method):**

For each key competency, write 2 questions in the format:
> "Tell me about a time when you [competency in context]. What was the situation, what did you do, and what was the outcome?"

Good competency questions:
- **Initiative:** "Tell me about a time you spotted a problem no one had asked you to solve. What did you do?"
- **Conflict:** "Tell me about a time you disagreed strongly with a decision. How did you handle it?"
- **Learning agility:** "Tell me about the last skill you taught yourself. What was the process?"
- **Leadership:** "Tell me about a time you had to get buy-in from people who weren't your direct reports."
- **Failure:** "Tell me about a significant professional mistake. What happened and what did you change?"

**Scoring guide per question:**

| Score | Description |
|-------|-------------|
| 4 | Clear STAR structure, specific evidence, measurable outcome, reflects well on competency |
| 3 | STAR structure present but vague on outcomes or could go either way |
| 2 | Partial answer, general claim without evidence, or outcome not convincing |
| 1 | No evidence, hypothetical rather than real experience, or avoidance |

**Deliver:**
- Interview process map (stages, owners, timeline)
- Per-stage question bank (3–5 questions per competency)
- Scoring rubric for each question
- Debrief template: structured format to compare candidates consistently after each stage

---

### Performance Review Templates

**Use when:** Running a performance cycle (annual, biannual, or continuous) or managing a PIP.

**Gather:** Review cycle type (annual / mid-year / 90-day check-in / PIP), employee role, any specific performance data available (OKR completion, peer feedback, manager notes).

**Standard performance review template:**

```markdown
# Performance Review: [Employee Name]
**Review Period:** [Date range]
**Role:** [Title]  **Manager:** [Name]  **Date:** [Review date]

---

## 1. Goals Achievement
| Goal | Target | Actual | Rating (1–5) | Notes |
|------|--------|--------|--------------|-------|
| [Goal from last review] | [Measure] | [What happened] | [1–5] | [Context] |

**Overall goal achievement:** Exceeded / Met / Partially Met / Not Met

---

## 2. Core Competencies
Rate each 1–5 (1 = significant gap, 3 = meets expectations, 5 = exceptional):

| Competency | Rating | Evidence |
|------------|--------|----------|
| Quality of work | | |
| Communication | | |
| Collaboration | | |
| Initiative / ownership | | |
| [Role-specific competency] | | |

---

## 3. Strengths (top 2–3)
[Specific, evidenced — not "great attitude". What did they actually do?]

## 4. Development Areas (top 2–3)
[Specific, actionable — not "needs to improve communication". What specifically, and what does improvement look like?]

## 5. Development Plan
| Area | Action | Support Needed | Target Date |
|------|--------|----------------|-------------|
| [Skill gap] | [Specific action: course, project, coaching] | [What manager/company provides] | [Date] |

## 6. Goals for Next Period
| Goal | Measure | Weight |
|------|---------|--------|
| [Goal] | [How measured] | [% of overall performance] |

## 7. Overall Rating
[ ] Exceptional (top 10%) [ ] Exceeds expectations [ ] Meets expectations [ ] Below expectations [ ] Significantly below expectations

## 8. Compensation Recommendation (manager section)
[ ] No change [ ] Market adjustment [ ] Merit increase: ____% [ ] Promotion recommended
```

**Performance Improvement Plan (PIP) template:**

```markdown
# Performance Improvement Plan: [Employee Name]
**Start Date:** [Date]  **Review Date:** [4-6 weeks from start]  **End Date:** [8-12 weeks from start]

## Performance Concerns
[Specific, factual description of the performance gaps. Reference incidents with dates. No vague language.]

## Required Improvements
| Area | Current State | Required Standard | Measurement |
|------|--------------|-------------------|-------------|
| [Specific issue] | [What's happening] | [What must change] | [How we'll assess] |

## Support Provided
- [Manager meeting frequency]
- [Training or coaching]
- [Resources]

## Milestones
| Date | Check-in | Expected Progress |
|------|----------|-------------------|

## Consequences
If improvements are not demonstrated by [end date]: [employment decision — be explicit]

Signatures: Employee ____________  Manager ____________  HR ____________
```

**Deliver:**
- Completed review document (or template pre-filled with role context)
- Development plan with specific actions
- PIP (if applicable) with clear milestones and consequences
- Calibration notes: how this rating compares to team/department distribution

---

### Onboarding Plan

**Use when:** A new hire is starting. Structured onboarding reduces time-to-productivity by 40–60%.

**Gather:** Role, start date, remote/in-person, team structure, first project if known, systems access needed, buddy/mentor assigned.

**30-60-90 day plan template:**

```markdown
# 30-60-90 Day Onboarding Plan: [Name] — [Role]
**Start Date:** [Date]  **Manager:** [Name]  **Buddy:** [Name]

---

## Week 1: Orientation
**Goal:** Feel safe, understand the mission, know who to ask for what.

- [ ] Day 1: Welcome, workspace setup, team introductions
- [ ] Day 1: Read company handbook, mission, values
- [ ] Day 1-2: IT access: [list systems]
- [ ] Day 2-3: 1:1 with every team member (30 min each)
- [ ] Day 3-5: Product/service deep dive (who are our customers, what do we do?)
- [ ] End of week 1: Check-in with manager — what questions do you have?

## Days 30: Learn
**Goal:** Understand the role, the team's processes, and begin contributing to small tasks.
**Success looks like:** [Specific outcome — e.g. "Has submitted first PR / handled first support ticket / completed training X"]

- [ ] Shadow [role-relevant colleague] for [activity]
- [ ] Complete [required training or certification]
- [ ] Attend [key recurring meetings]
- [ ] First deliverable: [small, low-stakes task to build confidence]
- [ ] Mid-month manager 1:1: How are things going? What needs adjusting?

## Days 60: Contribute
**Goal:** Working independently on core responsibilities. Identifying improvement opportunities.
**Success looks like:** [Specific outcome]

- [ ] Own [specific workflow or project area]
- [ ] Proactively suggest one improvement to an existing process
- [ ] Relationships: comfortable asking for help and giving feedback

## Days 90: Lead
**Goal:** Fully productive. Trusted to own their scope without close supervision.
**Success looks like:** [Specific outcome with metric if possible]

- [ ] 90-day review: manager and new hire complete performance review template
- [ ] Set goals for next 6 months
- [ ] New hire reflects: what wasn't in the plan that would have helped?
```

**Deliver:**
- Filled 30-60-90 day plan specific to the role
- System access checklist (what they need by day 1 vs week 2)
- Meeting schedule for week 1
- Buddy/mentor guidelines: what the buddy should cover (social integration) vs what the manager covers (work performance)

---

### Employment Law & Compliance Flags

**Use when:** Making a hiring, firing, or policy decision that has legal implications. This is a flag service — always recommend qualified legal counsel for final decisions.

**Gather:** Jurisdiction(s), employment type (employee / contractor / freelance), specific situation (termination, TUPE, redundancy, disciplinary, maternity, contract terms).

**Common compliance triggers to check:**

| Jurisdiction | Topic | Key rule | Risk if missed |
|-------------|-------|----------|----------------|
| UK | Right to work check | Required before first day; passports/visa checked and copied | Criminal liability for employer |
| UK | IR35 / off-payroll | Contractors determined as employees owe PAYE | HMRC liability + penalties |
| UK | Redundancy | ≥ 2 years service → statutory redundancy pay; ≥ 20 redundancies → collective consultation | Unfair dismissal claims |
| UK | TUPE | Employees transfer with existing terms when business transfers | Automatic unfair dismissal if terms changed |
| UK | Maternity/paternity | 52 weeks maternity leave; SMP; must not disadvantage on return | Employment tribunal |
| EU (GDPR) | Employee data | Lawful basis for processing; retention limits; subject access rights | ICO fine |
| US (general) | At-will exceptions | Implied contracts in handbooks can override at-will status | Wrongful termination |
| US | Worker classification | IRS and state tests differ; ABC test in CA/MA | Back taxes, penalties |

**Flagging protocol:**
- For anything in the above table: flag the risk and recommend qualified employment lawyer review before proceeding
- For new contractor engagements (UK): flag IR35 assessment required
- For any dismissal (UK): check ACAS code of practice steps were followed — skip any step and the tribunal uplift is 25%
- For redundancy (UK ≥ 20 people): 45-day consultation minimum; failure makes all dismissals automatically unfair

**Deliver:**
- Compliance risk flags relevant to the situation (table format)
- Immediate actions required before proceeding
- Referral: specific type of specialist required (employment solicitor, HR consultant, ACAS)
- Resources: links to gov.uk / ACAS / SHRM guidance relevant to the situation (use WebSearch to find current versions)

---

### Compliance Escalation Protocol

**Use when:** Any compliance-sensitive action — hiring, termination, leave, policy change, workplace investigation.

For every compliance-sensitive action, assess risk before proceeding:

| Risk Level | Criteria | Action |
|---|---|---|
| HIGH | Potential legal liability, involves protected class, termination for cause, workplace investigation | Escalate to lawyer specialist before proceeding. Document recommendation with caveats. |
| MEDIUM | Policy interpretation ambiguity, multi-jurisdiction employee, accommodation request | Note jurisdictional uncertainty, provide guidance with explicit "verify with local counsel" flag |
| LOW | Standard process, clear policy coverage, no protected class implications | Proceed with standard methodology |

**Escalation triggers (always escalate to lawyer):**
- Termination of employee in protected class
- Workplace harassment/discrimination complaint
- Whistleblower or retaliation claim
- Multi-jurisdiction compliance conflict
- Class/collective action risk
- Regulatory audit or government inquiry

See `references/compliance-escalation.md` for the full decision tree, jurisdiction-specific gotchas, and escalation handoff template.

---

### Specialist Routing

**Use when:** HR work intersects another professional domain. Route to the right GTeam specialist rather than attempting work outside HR expertise.

| Situation | Route To | What to Hand Off |
|---|---|---|
| Employment contract drafting/review | Lawyer | Draft terms, jurisdiction, specific clauses to review |
| Job description for technical role | Software Engineer or relevant specialist | Technical requirements validation |
| Employer brand content | Brand Strategist / Content Creator | EVP messaging, careers page copy |
| HR system selection/implementation | Software Engineer | Technical requirements, integration needs |
| Compensation benchmarking data | Data Analyst | Market data analysis, pay equity modelling |
| Employee comms & announcements | Content Creator | Internal comms drafting |

**Handoff format:** When routing, provide the receiving specialist with:
1. Context — what the HR situation is and why this specialist is needed
2. Specific ask — what output is required
3. Constraints — jurisdiction, timeline, budget, policy requirements
4. Return path — what HR needs back and in what format

---

### Jurisdiction Confirmation Protocol

**Use when:** Before providing any employment advice. Employment law varies dramatically by jurisdiction — getting it wrong has serious consequences.

**Steps:**
1. **Confirm jurisdiction** — ask which country/state/province the employee is in
2. If unknown, provide **jurisdiction-neutral guidance** with explicit notes on where rules commonly diverge
3. Flag specific areas where getting it wrong has serious consequences:

| Area | Why It Matters | Common Divergence |
|---|---|---|
| Termination notice periods | Range from 0 (US at-will) to 3+ months (EU) | At-will vs statutory notice; probation period rules |
| Non-compete enforceability | Banned in some jurisdictions, heavily restricted in others | CA bans entirely; UK requires garden leave consideration; EU varies by country |
| Contractor vs employee classification | Misclassification triggers back taxes, penalties, benefits liability | IRS 20-factor test (US), IR35 (UK), ABC test (CA/MA), sham contracting (AU) |
| Leave entitlements | Statutory minimums vary from 0 to 30+ days | US has no federal paid leave; EU mandates 4 weeks minimum; AU has NES |
| Data privacy in HR records | Fines for non-compliance can be significant | GDPR (EU/UK) vs sector-specific (US) vs Privacy Act (AU) |

**Default position:** If jurisdiction is not confirmed, state assumptions explicitly and flag that advice may not apply in the employee's actual jurisdiction.
