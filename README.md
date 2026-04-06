<p align="center">
<pre align="center">
  ██████╗ ████████╗███████╗ █████╗ ███╗   ███╗
 ██╔════╝ ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
 ██║  ███╗   ██║   █████╗  ███████║██╔████╔██║
 ██║   ██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
 ╚██████╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
</pre>
  <p align="center">
    <strong>Your AI professional firm for Claude Code.</strong><br>
    29 specialists. 4 orchestrated jobs. 175 reference frameworks. Zero API keys.<br><br>
    <a href="#quick-start">Quick Start</a> &bull;
    <a href="#specialists">Specialists</a> &bull;
    <a href="#jobs">Jobs</a> &bull;
    <a href="#coordinator">Coordinator</a> &bull;
    <a href="#evaluation">Evaluation</a>
  </p>
</p>

---

GTeam gives Claude Code instant access to a full professional firm — lawyers, accountants, engineers, designers, marketers, and more. Each specialist has a real methodology, domain-specific reference libraries, and professional-grade output. Not prompt templates. Actionable skill files that Claude follows like a senior hire would follow a playbook.

**One command. The right specialist. Full deliverable.**

```
/gteam Review this vendor contract and flag the top 5 risks
```

GTeam routes to the lawyer, loads the contract review methodology, applies jurisdiction-aware analysis, and delivers a redlined risk report — automatically.

## Why GTeam?

Most "prompt libraries" give you a paragraph of instructions and hope for the best. GTeam is different:

- **Real methodologies** — not "act as a lawyer", but a multi-phase contract review workflow with jurisdiction confidence marking, risk severity standards, and specific clause-level analysis frameworks
- **175 reference files** — domain-specific frameworks, templates, and checklists that specialists load on demand. The SEO specialist alone carries 24 reference files covering technical audits, keyword clustering, E-E-A-T signals, and Core Web Vitals
- **Orchestrated jobs** — multi-specialist workflows that chain together automatically. A product launch runs SEO + Content + Social + Legal in sequence with typed handoffs between each stage
- **Eval-tested** — every specialist has scored evaluation scenarios with automated LLM-as-judge grading. Average score: 91+ across the board
- **Coordinator mode** — a single ~1,700-token entry point that lazy-loads specialists on demand, instead of burning ~111K tokens upfront. 99% context reduction

## Quick Start

```bash
git clone https://github.com/gcampton/GTeam ~/.claude/skills/gteam
cd ~/.claude/skills/gteam
bun install
./setup lite    # Recommended: coordinator mode (~1,700 tokens)
```

Then in any Claude Code session:

```
/gteam I need to launch my new product next week
```

GTeam routes to the right job and runs all specialists automatically.

### Install Modes

| Mode | Command | Context Cost | Best For |
|---|---|---|---|
| **Lite** | `./setup lite` | ~1,700 tokens | Most users — loads specialists on demand |
| **Full** | `./setup full` | ~111K tokens | Power users who want instant routing |

## Specialists

### Sales & Revenue

| Specialist | Capabilities |
|---|---|
| **Sales** | Outbound prospecting, deal qualification, proposals, pipeline review, lead scoring, coaching methodology |
| **Paid Media** | Google/Meta/LinkedIn ads, account audit, creative testing, tracking, competitive ad analysis |
| **Growth Hacker** | User acquisition, funnel optimisation, referral loops, growth experiments, statistical rigor |

### Marketing & Content

| Specialist | Capabilities |
|---|---|
| **SEO** | Technical audit, keyword research, on-page fixes, content strategy, Core Web Vitals |
| **Social Media** | Platform strategy (5 algorithms), content creation, crisis management, influencer strategy |
| **Email Marketer** | Campaign design, sequence writing, deliverability, segmentation |
| **Content Creator** | Blog posts, landing copy, guides, AI content QC, E-E-A-T compliance |
| **Copywriter** | Sales pages (AIDA/PAS/BAB), email copy, ad copy, VSL scripts, brand voice |
| **CRO Specialist** | Landing page audits, funnel analysis, A/B test design, heatmap interpretation |

### Brand & Design

| Specialist | Capabilities |
|---|---|
| **Brand Strategist** | Positioning, messaging, voice and tone, brand audit, competitive mapping |
| **UI Designer** | Design systems, visual QA, UX review, responsive specs, component tokens |
| **UX Researcher** | User interviews (Mom Test), usability testing, sentiment scoring, research synthesis |

### Product & Delivery

| Specialist | Capabilities |
|---|---|
| **Product Manager** | Discovery, PRDs (JTBD pipeline), roadmap, RICE prioritisation, behavioral nudge design |
| **Project Manager** | Scoping, task breakdown, timeline, Fibonacci estimation, spec drift detection |
| **Data Analyst** | Metrics frameworks, cohort analysis, A/B testing, KPI dashboards |

### Engineering

| Specialist | Capabilities |
|---|---|
| **Software Engineer** | Code review (6-role PR review), debugging methodology, implementation, developer growth analysis |
| **DevOps** | CI/CD, Kubernetes, monitoring (RED/USE), incident response, cost optimisation, DR planning |
| **Technical Writer** | API docs, developer guides, architecture discovery, reading paths, diagrams |
| **Security Engineer** | Threat modeling (STRIDE), OWASP audits, secure architecture, incident analysis |
| **AI Engineer** | RAG pipelines, prompt engineering, model integration, MLOps, evaluation design |
| **Accessibility Auditor** | WCAG 2.2 audit, assistive tech testing, ARIA patterns, remediation plans |

### Business & Legal

| Specialist | Capabilities |
|---|---|
| **Lawyer** | Contract review, risk assessment, redlining, GDPR/privacy, jurisdiction confidence marking |
| **Accountant** | Financial review, P&L analysis, tax considerations, SaaS benchmarking |
| **Recruitment** | Job descriptions, sourcing strategy, interview design, offer negotiation |
| **Customer Success** | Onboarding, health scoring, churn prevention, QBRs, activation metrics |
| **HR Specialist** | Interview frameworks, performance reviews, onboarding plans, employment law flags |

### Research & Strategy

| Specialist | Capabilities |
|---|---|
| **Ideas Man** | Niche research, market validation, TAM/SAM/SOM, unit economics, startup idea scoring |
| **Community Manager** | Discord/Slack/Reddit setup, moderation frameworks, engagement automation, health metrics |

## Jobs

Jobs chain multiple specialists together with typed handoffs. One command runs the full pipeline.

| Job | Specialists | Output |
|---|---|---|
| **content-campaign** | SEO + Content + Social | Keyword strategy, optimised blog post, social distribution plan |
| **product-launch** | SEO + Content + Social + Lawyer | Complete launch package with legal review |
| **legal-review** | Lawyer | Redlined document + risk severity report |
| **gteam-learn** | Meta | Scans logged results, proposes reference file updates |

```
/gteam Run a content campaign for "workflow automation for small teams"
```

## Coordinator

The GTeam Coordinator is a lightweight router (~1,700 tokens) that replaces loading all 29 specialists into context (~111K tokens). It reads the user's request, picks the right specialist, loads their full SKILL.md via the Read tool, then executes as that specialist.

```
                         User Request
                              |
                    [GTeam Coordinator]     ~1,700 tokens
                     routing table only
                              |
                    picks specialist(s)
                              |
                  Read specialist/SKILL.md   loaded on demand
                              |
                   execute as specialist     full methodology
                              |
                         Deliverable
```

This means you get the same depth and quality as the full install, but only pay the token cost for specialists you actually use.

## Evaluation

Every specialist has evaluation scenarios tested with an automated LLM-as-judge pipeline. 90 scenarios across 30 specialists, graded on four dimensions:

- **Relevance** — does the output address the task?
- **Completeness** — are all expected criteria met?
- **Actionability** — are recommendations specific and implementable?
- **Methodology Alignment** — does it follow professional best practices?

```bash
# Run all evals
bun run test:evals

# Run specific specialist
python3 scripts/skill-eval-matrix.py --specialist lawyer

# Compare against previous run
python3 scripts/skill-eval-matrix.py --baseline latest

# pass@k scoring (3 runs per scenario)
python3 scripts/skill-eval-matrix.py --runs 3
```

No API key required — evals use `claude -p` (your existing Claude subscription).

## Architecture

```
gteam/
├── coordinator/          # Lightweight entry point (lite mode)
│   └── SKILL.md
├── specialists/          # 29 domain specialists
│   └── {name}/
│       ├── SKILL.md.tmpl     # Template (edit this)
│       ├── SKILL.md          # Generated (don't edit)
│       ├── methodology.md    # Domain workflow + rules
│       ├── references/       # Frameworks, templates, checklists
│       ├── results/          # Logged deliverables
│       └── evals/            # Evaluation scenarios
├── jobs/                 # Multi-specialist orchestrations
├── references/           # Shared standards (severity, handoffs)
├── scripts/              # Generators and eval runner
└── setup                 # Install script (lite/full modes)
```

### SKILL.md Workflow

SKILL.md files are generated from `.tmpl` templates. Never edit `.md` directly:

```bash
# Edit the template
vim specialists/lawyer/SKILL.md.tmpl

# Regenerate
bun run gen:skill-docs

# Commit both
git add specialists/lawyer/SKILL.md.tmpl specialists/lawyer/SKILL.md
```

## Development

```bash
bun install                     # Install dependencies
bun test                        # Tier 1 static validation
bun run test:evals              # Tier 3 LLM-as-judge evaluation
bun run gen:skill-docs          # Regenerate all SKILL.md from templates
bun run skill:check             # Health dashboard for all skills
```

## Credits

Built on the shoulders of:

- **[gstack](https://github.com/gcampton/gstack)** — the original virtual engineering team for Claude Code
- **[Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** — documentation scraping for reference libraries
- **[agency-agents](https://github.com/gcampton/agency-agents)** — coaching and behavioral frameworks
- **[Skillsmith](https://github.com/gcampton/skillsmith)** — skill scaffolding and standardised skill architecture

## License

MIT
