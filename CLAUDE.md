# GTeam development

## Commands

```bash
bun install                  # install dependencies
bun test                     # run Tier 1 static validation
bun run test:evals           # run Tier 3 LLM-as-judge (uses claude -p or Ollama)
bun run test:evals:all       # force all skills regardless of hash
bun run gen:skill-docs       # regenerate all SKILL.md from templates
bun run gen:skill-docs:dry-run  # check if generated files are up to date
bun run skill:check          # health dashboard for all skills
bun run build                # alias for gen:skill-docs
```

## Project structure

- `specialists/` — individual professional skills (standalone + methodology block)
- `jobs/` — orchestrated multi-specialist workflows
- `scripts/gen-skill-docs.ts` — template generator (edit this to change {{PREAMBLE}})
- `scripts/skill-check.ts` — health dashboard

## SKILL.md workflow

SKILL.md files are **generated** from `.tmpl` templates. Never edit `.md` files directly:
1. Edit the `.tmpl` file
2. Run `bun run gen:skill-docs`
3. Commit both `.tmpl` and `.md`

## Adding a new specialist

1. Create `specialists/{name}/SKILL.md.tmpl` (follow existing anatomy)
2. Create `specialists/{name}/methodology.md` (condensed workflow + domain rules)
3. Run `bun run gen:skill-docs`
4. Reference `{{NAME_METHODOLOGY}}` in any job template that needs it

## Token naming rule

Directory `content-creator` → token `{{CONTENT_CREATOR_METHODOLOGY}}`
Rule: `dirName.toUpperCase().replace(/-/g, '_') + '_METHODOLOGY'`

---

## TODO — Improvements from community repo analysis

### Priority 1 — MCP integrations (low effort, high leverage)

- [x] **Context7** — installed at user scope (`claude mcp add --scope user context7 -- npx -y @upstash/context7-mcp`)
- [ ] **Exa** — deep research web search MCP: `claude mcp add -e EXA_API_KEY=xxx exa -- npx -y exa-mcp-server` (needs EXA_API_KEY)
- [ ] **Firecrawl** — structured web crawl: `claude mcp add -e FIRECRAWL_API_KEY=xxx firecrawl -- npx -y firecrawl-mcp` (needs FIRECRAWL_API_KEY)
- [ ] **GitHub MCP** — already installed as plugin for `/home/garratt/dev`; needs GITHUB_PERSONAL_ACCESS_TOKEN env var set
- [ ] **Google Search Console MCP** — live ranking data for SEO specialist (needs GSC OAuth setup)
- [ ] **Xero MCP** — accounting data access for accountant specialist (needs Xero OAuth setup)

### Priority 2 — Specialist workflow upgrades

#### software-engineer
- [x] Add **verification gate** — before marking any task done, run tests and show output
- [x] Add **6-role PR review workflow**: Security, Performance, Correctness, Maintainability, UX, and Business logic reviewers each provide a verdict
- [x] Add **systematic debugging methodology**: hypothesis → reproduce → isolate → fix → verify loop
- [x] Add `references/debugging-patterns.md` with common failure modes per language

#### product-manager
- [x] Add **JTBD → PRD pipeline**: Jobs-to-be-done framework with canvas, opportunity scoring, feeds into PRD
- [x] Add **brainstorming gate** — must generate ≥ 3 solution options before committing
- [x] Add `references/prd-template.md` and `references/jtbd-canvas.md`

#### project-manager
- [x] Add **testStrategy** field to project specs — every spec must include acceptance criteria
- [x] Add **complexity scoring** — t-shirt sizes (S/M/L/XL) with criteria for each
- [x] Add **spec drift detection** — flag when implementation scope has grown beyond the spec

#### ui-designer
- [ ] Add **7-phase design review process**: Discovery → Research → Architecture → Visual → Interaction → Accessibility → Handoff
- [ ] Integrate `ui-ux-pro-max` domain search into each phase (already partially done)

#### content-creator
- [x] Add **AI-Assisted Content Quality Control** workflow — hollow openers, vague generalities, E-E-A-T signals, YMYL requirements
- [x] Add `references/ai-writing-patterns.md` with detectable AI tells and fixes

### Priority 3 — New specialists

- [x] **hr-specialist** — job description writing, interview frameworks, performance review templates, onboarding plans, compliance basics (employment law flags)
- [x] **copywriter** — sales page copy, email copy, ad copy, VSL scripts; AIDA/PAS/BAB frameworks; A/B testing guidance
- [x] **cro-specialist** — conversion rate optimisation; landing page audits; funnel analysis; heatmap interpretation; A/B test design

### Priority 4 — Structural improvements

- [x] **Severity standardisation** — `references/severity-standard.md` with CRITICAL/HIGH/MEDIUM/LOW + domain mapping table; referenced in main SKILL.md.tmpl
- [x] **Typed handoffs** — `references/handoff-schema.md` with schemas for all key specialist-to-specialist transitions; referenced in main SKILL.md.tmpl
- [ ] **Framework inventories** — each specialist `references/` should list the frameworks/models it knows (e.g. lawyer: contract frameworks by jurisdiction)
- [ ] **gteam-learn job** — scan `specialists/*/results/*.md` for logged outcomes and propose updates to reference files using `[HYPOTHESIS]`/`[TESTED]`/`[REVISED]` markers

### Startup-analyst integration (into ideas-man)
- [x] Added **Startup Idea Validation** workflow to `specialists/ideas-man/methodology.md`
  - TAM/SAM/SOM analysis
  - Unit economics modelling
  - Competitive moat assessment
  - Investor-readiness scoring
  - Conservative/base/optimistic projections
