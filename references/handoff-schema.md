# GTeam Typed Handoff Schema

Defines the structured output format each specialist produces so downstream specialists in a job know exactly what to consume.

When a job runs multiple specialists sequentially, the producing specialist should end their output with a `## Handoff` section in this schema format. The consuming specialist reads this section first.

---

## Specialist Output Schemas

### product-manager → software-engineer

```markdown
## Handoff: product-manager → software-engineer

**PRD link / ref:** [filename or section]
**Sprint goal:** [One sentence]
**Stories ready for dev:** [List task IDs with acceptance criteria confirmed]
**Open questions blocking dev:** [List — if none, say "None"]
**Out of scope (do not build):** [Explicit list]
**Success metric:** [How to know when it's done, with measurable threshold]
```

### product-manager → ui-designer

```markdown
## Handoff: product-manager → ui-designer

**Problem being solved:** [One sentence from PRD problem statement]
**User personas:** [Name + context for each persona the design serves]
**Key user flows:** [Numbered list of flows to design]
**Constraints:** [Technical, brand, accessibility requirements]
**Success criteria for design:** [Acceptance criteria the design must satisfy]
**Out of scope for this design:** [Explicit]
```

### ui-designer → software-engineer

```markdown
## Handoff: ui-designer → software-engineer

**Figma link:** [URL or "attached"]
**Design tokens to use:** [Colours, spacing, typography — or "follow existing design system"]
**Components needed:** [List of new components required]
**Interaction specs:** [Animations, hover states, loading states, empty states]
**Accessibility requirements:** [Specific A11y constraints from design review]
**Edge cases to handle in code:** [Empty state, error state, loading state — with design spec for each]
```

### software-engineer → devops

```markdown
## Handoff: software-engineer → devops

**What shipped:** [Feature name and brief description]
**Deployment notes:** [Migrations, env vars needed, feature flags, order of operations]
**Rollback plan:** [Specific steps if rollback is needed]
**Monitoring:** [Metrics to watch, alert thresholds recommended]
**Known risks:** [Anything that could go wrong in production that wasn't in dev]
```

### seo → content-creator

```markdown
## Handoff: seo → content-creator

**Target keyword:** [Primary keyword]
**Search intent:** [Informational / commercial / transactional]
**Content type:** [Blog post / landing page / pillar page / cluster article]
**Word count target:** [Based on top-ranking pages ± 20%]
**H2 structure recommended:** [List of suggested H2s based on People Also Ask and competitor gaps]
**Keywords to include:** [Primary + 3–5 related terms]
**Competitor gaps to exploit:** [Specific angles the top pages miss]
**Internal links to include:** [URLs and anchor text]
```

### content-creator → social-media

```markdown
## Handoff: content-creator → social-media

**Source piece:** [URL or filename]
**Key insights (top 3):** [The most shareable, quotable points]
**Pull quotes ready:** [3 × tweet-length excerpts]
**Repurposing brief:** [Which formats are needed: carousel / thread / newsletter]
**Audience:** [Who this content is for]
**CTA:** [What action should social content drive — link in bio / comment / share]
```

### ideas-man → product-manager

```markdown
## Handoff: ideas-man → product-manager

**Opportunity:** [Name and one-sentence description]
**Niche score:** [Composite score from rubric]
**TAM estimate:** [£/$ range with source]
**Validation evidence:** [Reddit complaints, competitor pricing, search volume]
**Recommended entry model:** [Affiliate / SaaS / content / dropship]
**First action:** [Specific next step to validate before building]
**Risks:** [Top 2–3 reasons this might not work]
```

### lawyer → product-manager / software-engineer

```markdown
## Handoff: lawyer → [recipient]

**Document reviewed:** [Contract name / type]
**Overall verdict:** GREEN (proceed) / AMBER (negotiate) / RED (do not proceed)
**Blocking issues (CRITICAL/HIGH):** [List — must resolve before proceeding]
**Negotiation points (MEDIUM):** [List — worth raising but not blockers]
**Accepted as-is (LOW/OK):** [Summary — no action needed]
**Required next steps:** [Specific actions before signing/building]
```

---

## Job-Level Summary Format

When a job runs multiple specialists, the orchestrator produces a combined summary:

```markdown
# Job Summary: [Job Name]
**Date:** [Date]  **Specialists run:** [List]

## Cross-Specialist Issues (by severity)

### CRITICAL
- [Issue] — Source: [specialist] — Owner: [who fixes it]

### HIGH
- [Issue] — Source: [specialist] — Owner: [who fixes it]

### MEDIUM (ship with known issues)
- [Issue] — Source: [specialist]

## Ship Verdict: [Blocked / At risk / Ship with known issues / Ship]

## Completed Deliverables
| Specialist | Output | Status |
|-----------|--------|--------|
| [Name] | [What was produced] | Complete |
```
