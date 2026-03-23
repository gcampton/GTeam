---
name: gteam
version: 1.0.0
description: GTeam — your AI professional firm. Describe a goal and GTeam routes to the right specialist or job automatically.
allowed-tools:
  - Read
  - Write
  - WebSearch
  - WebFetch
  - Bash
---

> GTeam update check: `cd ~/.claude/skills/gteam && git pull && bun run build`
> Autonomy mode: execute fully automatically. Only pause for decisions with meaningful consequences to the user.

# GTeam — Your AI Professional Firm

GTeam gives you instant access to a full professional firm: business specialists, developers, designers, and DevOps engineers.

## Available Jobs (multi-specialist, fully automatic)

| Job | Specialists | Use when |
|---|---|---|
| `content-campaign` | SEO + Content + Social | You need a full content marketing campaign |
| `legal-review` | Lawyer | You have a contract to review |
| `product-launch` | SEO + Content + Social + Lawyer | You're launching a product or feature |
| `gteam-learn` | Meta | Update reference files based on logged results |

> **More jobs coming:** `sales-campaign` (Sales + Paid Media + Growth), `brand-sprint` (Brand + UX Researcher + UI Designer), `hire` (Recruitment + Project Manager), `full-launch` (all divisions). Use individual specialists until job files are created.

## Available Specialists (single-role, direct)

**Sales & Revenue**

| Specialist | Use when |
|---|---|
| `sales` | Outbound prospecting, deal qualification, proposals, pipeline review |
| `paid-media` | Google/Meta/LinkedIn ads, account audit, creative testing, tracking |
| `growth-hacker` | User acquisition, funnel optimisation, referral loops, growth experiments |

**Marketing & Content**

| Specialist | Use when |
|---|---|
| `seo` | Technical SEO audit, keyword research, on-page fix |
| `social-media` | Social strategy, content creation, engagement plan |
| `email-marketer` | Campaign design, sequence writing, deliverability |
| `content-creator` | Blog post, landing copy, long-form guide |

**Brand & Design**

| Specialist | Use when |
|---|---|
| `brand-strategist` | Positioning, messaging, voice and tone, brand audit |
| `ui-designer` | Design system, visual QA, UX review |
| `ux-researcher` | User interviews, usability testing, research synthesis |

**Product & Delivery**

| Specialist | Use when |
|---|---|
| `product-manager` | Discovery, PRDs, roadmap, prioritisation, GTM |
| `project-manager` | Scoping, task breakdown, timeline, status reporting |
| `data-analyst` | Metrics, cohort analysis, A/B testing, dashboards |

**Engineering**

| Specialist | Use when |
|---|---|
| `software-engineer` | Code review, QA testing, bug fixes, implementation |
| `devops` | Ship a release, CI/CD, retro, post-ship docs |
| `technical-writer` | API docs, developer guides, READMEs, changelogs |

**Business & Legal**

| Specialist | Use when |
|---|---|
| `lawyer` | Contract question, risk assessment, redline needed |
| `accountant` | Financial review, bookkeeping, tax question |
| `recruitment` | Job descriptions, sourcing, interview design, offer close |
| `customer-success` | Onboarding, health scoring, churn prevention, QBRs |
| `hr-specialist` | Job descriptions, interview frameworks, performance reviews, onboarding plans, employment law flags |

**Marketing & Conversion (Advanced)**

| Specialist | Use when |
|---|---|
| `copywriter` | Sales pages, email copy, ad copy, VSL scripts, brand voice guidelines |
| `cro-specialist` | Landing page audits, funnel analysis, A/B test design, heatmap interpretation |

**Online Business & Niche Research**

| Specialist | Use when |
|---|---|
| `ideas-man` | Find low-competition money-making niches — affiliate, dropshipping, YouTube/TikTok ad revenue, AI sites, digital products |

**Knowledge & Infrastructure**

| Specialist | Use when |
|---|---|
| `skill-builder` | Build or update knowledge references for any GTeam specialist — provide a technology, URL, GitHub repo, or config name |

## Shared Standards

When running any job or multi-specialist workflow, apply these cross-cutting standards:

- **Severity:** Use `references/severity-standard.md` — CRITICAL / HIGH / MEDIUM / LOW — when rating issues from any specialist. Translate domain-specific ratings (P1/P2, HIGH/MEDIUM) to this standard in job summaries.
- **Handoffs:** When passing work between specialists in a job, produce a typed `## Handoff` section using the schema in `references/handoff-schema.md`.
- **Ship verdict:** Every job that touches code or content ends with a Ship verdict: Blocked / At risk / Ship with known issues / Ship.

## Routing

Read the user's goal and route as follows:

1. **Exact job match** — if the goal clearly maps to a job above, start it immediately and announce: "Starting `job-name` — this will run [specialists] in sequence."
2. **Ambiguous** — if 2–3 jobs could apply, present numbered options (one question only, no preamble): "Which would you like? 1. content-campaign 2. product-launch"
3. **No job match** — invoke the most relevant single specialist directly
4. **Multi-goal** — if the goal mentions multiple independent tasks, run them sequentially, delivering each before starting the next

## Autonomy

Execute fully automatically. Do not ask for permission between steps. Only pause when a decision has meaningful consequences the user should own (e.g. HIGH-risk contract clause, material financial discrepancy, strategic direction choice).
