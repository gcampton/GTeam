# GTeam Design Spec
**Date:** 2026-03-19
**Status:** Approved
**Repo:** https://github.com/gcampton/GTeam

---

## Overview

GTeam is a standalone Claude Code skill system that provides job-based AI orchestration across professional domains — law, accounting, marketing, SEO, content creation, and more. Where gstack gives you a virtual engineering team, GTeam gives you a virtual professional firm.

Unlike gstack's human-in-the-loop model (user invokes each skill manually), GTeam is designed to be **automatically executing**: the user describes a goal, GTeam routes to the right job, and the job runs all required specialists end-to-end with minimal interruption.

GTeam references gstack in its description and borrows its browse binary and template infrastructure, but is developed and maintained independently.

---

## Architecture: Two-Layer Specialist + Jobs

GTeam uses a two-layer architecture:

### Layer 1: Specialists
Individual professional skills. Each specialist encapsulates deep domain expertise, workflow, and deliverable format for one role. Specialists can be invoked directly for focused tasks, or embedded into jobs.

**v1 Specialists:**
- `lawyer` — contract review, legal risk assessment, redlining
- `accountant` — financial analysis, bookkeeping review, tax considerations
- `seo` — technical SEO audit, keyword strategy, on-page recommendations
- `social-media` — platform strategy, post creation, engagement planning
- `email-marketer` — campaign strategy, copywriting, sequence design
- `content-creator` — blog posts, landing copy, long-form content

### Layer 2: Jobs
Orchestrated multi-specialist workflows. A job defines a goal and the sequence of specialist methodologies needed to achieve it. Jobs run automatically — Claude executes all steps, only surfacing decisions that genuinely require human input.

**v1 Jobs (initial set, grows over time):**
- `content-campaign` — SEO + Content Creator + Social Media → full campaign package
- `legal-review` — Lawyer → redlined document + risk report
- `product-launch` — all specialists → complete launch package

---

## Orchestration Model

Claude Code skills cannot invoke other skills at runtime. GTeam solves this with **build-time methodology embedding** via the template generator.

Each specialist defines a reusable methodology block (e.g. `{{SEO_METHODOLOGY}}`). Job templates embed the relevant specialist methodologies inline:

```
jobs/content-campaign/SKILL.md.tmpl:

Step 1: SEO Foundation
{{SEO_METHODOLOGY}}

Step 2: Content Strategy
{{CONTENT_CREATOR_METHODOLOGY}}

Step 3: Social Distribution plan
{{SOCIAL_MEDIA_METHODOLOGY}}

Step 4: Deliver complete campaign package
```

This means:
- Jobs are self-contained SKILL.md files — no runtime chaining required
- Specialist knowledge lives in one place, shared across all jobs that need it
- Fully automatic execution — Claude reads one document and completes all steps
- Easy to extend — new specialist = new methodology block = referenced in any job

The main `/gteam` entry point skill routes the user's stated goal to the appropriate job or specialist automatically.

---

## Repository Structure

```
gteam/
├── browse/                      # git submodule → gstack's browse binary
├── specialists/
│   ├── lawyer/
│   │   ├── SKILL.md.tmpl
│   │   └── SKILL.md             # generated
│   ├── accountant/
│   ├── seo/
│   ├── social-media/
│   ├── email-marketer/
│   └── content-creator/
├── jobs/
│   ├── content-campaign/
│   │   ├── SKILL.md.tmpl
│   │   └── SKILL.md             # generated
│   ├── legal-review/
│   └── product-launch/
├── scripts/
│   ├── gen-skill-docs.ts        # template → SKILL.md generator (adapted from gstack)
│   └── skill-check.ts           # health dashboard
├── test/
│   ├── skill-validation.test.ts # Tier 1: static validation (free)
│   └── skill-llm-eval.test.ts   # Tier 3: LLM-as-judge (~$0.15/run)
├── docs/
│   └── superpowers/specs/       # design specs
├── SKILL.md.tmpl                # main entry point skill
├── SKILL.md                     # generated
├── CLAUDE.md
├── package.json
├── setup                        # install script
└── README.md
```

---

## Browse Binary

GTeam includes Playwright-powered browser automation via gstack's `browse` binary, added as a git submodule:

```
git submodule add https://github.com/garrytan/gstack browse
```

Skills reference the browser via `$B` — same command interface, persistent Chromium daemon, sub-second latency per command. Useful for:
- SEO audits on live sites
- Checking email campaign renders
- Reviewing a client site for legal compliance
- Social media page analysis

---

## Install Model

```bash
git clone https://github.com/gcampton/GTeam ~/.claude/skills/gteam
cd ~/.claude/skills/gteam
git submodule update --init   # pulls browse binary source
./setup                        # builds browse + registers skills
```

The `setup` script:
1. Initialises the browse submodule
2. Builds the browse binary (`bun build --compile`)
3. Makes skills available to Claude Code

Follows the same pattern as gstack (`~/.claude/skills/gstack`). Users with gstack already installed may reuse the compiled binary.

---

## Testing

### Tier 1 — Static Validation (free, <2s)
- Parses every `$B` command in all SKILL.md files, validates against browse command registry
- Validates SKILL.md frontmatter structure
- Checks all `{{PLACEHOLDER}}` references resolve in the template generator
- Runs on every `bun test`

### Tier 3 — LLM-as-judge (~$0.15/run)
- Sonnet scores each specialist and job skill on: clarity, completeness, actionability, domain accuracy
- Critical for professional skills where correctness matters (legal, financial)
- Results saved to `~/.gteam-dev/evals/`
- Run via `bun run test:evals`
- Diff-based selection — only re-evaluates skills whose source files changed

### Tier 2 — E2E (deferred)
Added in a future version once skills are mature enough to test end-to-end via `claude -p`.

---

## Autonomy Design Principle

GTeam skills are designed to **minimise human-in-the-loop interruptions**. The standard pattern:

- **Do automatically:** all research, analysis, drafting, formatting, file writes
- **Ask the user only when:** a decision has meaningful consequences they'd care about (e.g. "I found a high-risk clause — do you want to negotiate it out or flag it as accepted risk?")
- **Never ask about:** process steps, tool choices, formatting preferences, intermediate results

This contrasts with gstack, where human approval at each phase is intentional. GTeam's target experience: describe a goal, get a complete deliverable.

---

## Relationship to gstack

GTeam is an independent project. It:
- References gstack in its description/README as inspiration
- Borrows the browse binary via git submodule
- Adapts gstack's `gen-skill-docs.ts` template generator and `skill-check.ts`
- Does **not** depend on gstack being installed
- Has its own release cycle, versioning, and CHANGELOG

---

## Out of Scope (v1)

- Tier 2 E2E testing
- Parallel job execution (multiple specialists running simultaneously)
- Job state persistence between sessions
- skill-seekers integration (auto-generating skills from documentation scraping)
- Custom job builder UI
- Non-English specialists
