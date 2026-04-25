### Browse Setup

When researching salary benchmarks, company reviews, or compliance resources, run this setup block:

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/dev/1_myprojects/gteam/browse/dist/browse
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
