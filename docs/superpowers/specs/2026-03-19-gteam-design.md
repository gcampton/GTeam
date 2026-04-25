# GTeam Design Spec
**Date:** 2026-03-19
**Status:** Approved
**Repo:** https://github.com/gcampton/GTeam

---

## Overview

GTeam is a standalone Claude Code skill system that provides job-based AI orchestration across professional domains — law, accounting, marketing, SEO, content creation, and more.
It has borrowed and extended a number of projects notably Gstack, and Skill-Seekers and a few other ideas and concepts from others.
Where gstack gives you a virtual engineering team, GTeam gives you a virtual professional firm and the ability to create super defined agents via skill scraper.

GTeam is designed to be **automatically executing**: the user describes a goal, GTeam routes to the right job, and the job runs all required specialists end-to-end with minimal interruption.

GTeam references gstack in its description and borrows its browse binary and template infrastructure, but is developed and maintained independently as it is automation focused.

---

## Architecture: Two-Layer Specialist + Jobs

GTeam uses a two-layer architecture:

### Layer 1: Specialists
Individual professional skills. Each specialist encapsulates deep domain expertise, workflow, and deliverable format for one role. Specialists can be invoked directly for focused tasks, or embedded into jobs.

**v1.0 Specialists:**
- `lawyer` — contract review, legal risk assessment, redlining
- `accountant` — financial analysis, bookkeeping review, tax considerations
- `seo` — technical SEO audit, keyword strategy, on-page recommendations
- `social-media` — platform strategy, post creation, engagement planning
- `email-marketer` — campaign strategy, copywriting, sequence design
- `content-creator` — blog posts, landing copy, long-form content

*More to come*
- `Assistant` - Works with accountant and tools for company finances, spreadsheets, general housekeeping
- `Email Support` - Answers support emails
- `Designer` - Web designer, graphical designer, works with social media and dev team.

### Layer 2: Jobs
Orchestrated multi-specialist workflows. A job defines a goal and the sequence of specialist methodologies needed to achieve it. Jobs run automatically — Claude executes all steps, only surfacing decisions that genuinely require human input.

**v1.0 Jobs (initial set, grows over time):**
- `content-campaign` — SEO + Content Creator + Social Media → full campaign package
- `legal-review` — Lawyer → redlined document + risk report
- `product-launch` — subset of specialists (SEO + Content Creator + Social Media + Lawyer) → launch package. Does NOT embed all six specialists — accountant and email-marketer are excluded from v1 to keep context length manageable.

---

## Orchestration Model

Claude Code skills cannot invoke other skills at runtime. GTeam solves this with **build-time methodology embedding** via the template generator.

Each specialist has a dedicated `methodology.md` file — a focused, self-contained description of that specialist's workflow, process steps, and decision rules. Job templates reference these via placeholder tokens:

```
specialists/seo/methodology.md             → resolves {{SEO_METHODOLOGY}}
specialists/content-creator/methodology.md → resolves {{CONTENT_CREATOR_METHODOLOGY}}
specialists/social-media/methodology.md    → resolves {{SOCIAL_MEDIA_METHODOLOGY}}
```

**Token naming rule:** directory name → `UPPER_SNAKE_CASE` + `_METHODOLOGY` suffix.
`content-creator` → `{{CONTENT_CREATOR_METHODOLOGY}}`, `social-media` → `{{SOCIAL_MEDIA_METHODOLOGY}}`.
Implementation: `dirName.toUpperCase().replace(/-/g, '_') + '_METHODOLOGY'`.

The generator reads `specialists/{name}/methodology.md` when resolving `{{NAME_METHODOLOGY}}` in job templates:

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
- Specialist methodology lives in one file, shared across any job that needs it
- Fully automatic execution — Claude reads one document and executes all steps
- Easy to extend — new specialist = new `methodology.md` = available to any job via `{{NEW_SPECIALIST_METHODOLOGY}}`

The `methodology.md` and `SKILL.md.tmpl` are separate concerns:
- `SKILL.md.tmpl` — the full standalone skill (when invoked directly by the user)
- `methodology.md` — the embeddable workflow block (when embedded into a job)

---

## Repository Structure

```
gteam/
├── browse/                      # git submodule → gstack repo (full source)
│   └── src/                     # TypeScript source used by gen-skill-docs.ts
├── specialists/
│   ├── lawyer/
│   │   ├── SKILL.md.tmpl        # full standalone skill
│   │   ├── methodology.md       # embeddable workflow block for jobs
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
│   ├── gen-skill-docs.ts        # template → SKILL.md generator
│   └── skill-check.ts           # health dashboard (auto-discovers skills)
├── test/
│   ├── skill-validation.test.ts # Tier 1: static validation (free)
│   └── skill-llm-eval.test.ts   # Tier 3: LLM-as-judge (~$0.15/run)
├── docs/
│   └── superpowers/specs/
├── SKILL.md.tmpl                # main entry point skill
├── SKILL.md                     # generated
├── CLAUDE.md
├── package.json
├── setup                        # install script
└── README.md
```

---

## Browse Binary

GTeam uses gstack's `browse` binary for Playwright-powered browser automation. The full gstack repo is added as a git submodule at `browse/`:

```bash
git submodule add https://github.com/gcampton/gstack browse
```

The submodule includes TypeScript source (`browse/src/`), which `gen-skill-docs.ts` imports for browse command validation in Tier 1 static tests. The compiled binary is built from this source during `./setup`.

Skills reference the browser via `$B` — same command interface as gstack, persistent Chromium daemon, sub-second latency. Useful for:
- SEO audits on live sites
- Checking email campaign renders
- Reviewing a client site for legal compliance
- Social media page analysis

**Note:** GTeam's `gen-skill-docs.ts` does **not** generate browse command reference tables (those are a gstack concern). 
It only uses the browse source for `$B` command validation in Tier 1 tests — confirming that commands used in SKILL.md files exist in the registry.

---

## Install Model

```bash
git clone https://github.com/gcampton/GTeam ~/dev/1_myprojects/gteam
cd ~/dev/1_myprojects/gteam
git submodule update --init   # pulls gstack source (for browse binary)
./setup                        # builds browse + registers skills
```

**The `setup` script logic:**

1. Check for an existing compiled binary at `~/.claude/skills/gstack/browse/dist/browse`
   - If found and executable: symlink `browse/dist/browse` → existing binary (skip rebuild)
   - If not found: build from submodule source via `bun build --compile`
2. Verify SKILL.md files exist at `specialists/*/SKILL.md` and `jobs/*/SKILL.md` and print a summary. 
   - No explicit Claude Code registration is required 
   - Claude Code reads skills directly from `~/dev/1_myprojects/gteam/**/*.md` because the clone target is the install location.

This means users with gstack already installed skip the ~30s Bun compile step entirely.

---

## Template Token Reference

All `.tmpl` files (both specialist and job) support these tokens:

| Token | Resolves to | Source |
|---|---|---|
| `{{PREAMBLE}}` | Generated static preamble block | `gen-skill-docs.ts` (hardcoded output) |
| `{{NAME_METHODOLOGY}}` | Contents of `specialists/{name}/methodology.md` | File read by generator |

No other tokens are defined in v1. `{{PREAMBLE}}` and `{{NAME_METHODOLOGY}}` variants are the complete set of known placeholders. The Tier 1 validator rejects any unrecognised `{{TOKEN}}` found in a `.tmpl` file.

**`{{PREAMBLE}}` expands to:**
```
> GTeam update check: `cd ~/dev/1_myprojects/gteam && git pull && bun run build`
> Autonomy mode: execute fully automatically. Only pause for decisions with meaningful consequences to the user.
```

This is a static string produced by the generator — no file read, no conditional logic.

---

## Specialist SKILL.md Template Structure

All specialist templates follow this anatomy:

```markdown
---
name: gteam-{specialist}
version: 1.0.0
description: One-line description of the specialist role
allowed-tools:
  - Read
  - Write
  - WebSearch
  - WebFetch
  - Bash        # only for specialists that need CLI tools (e.g. SEO audit scripts)
---

{{PREAMBLE}}

# {Specialist Title} — GTeam

## Role
One paragraph: who this specialist is and what they're here to do.

## Workflow

Step 1: [First action — always starts with gathering context]
Step 2: ...
Step N: Deliver [specific named output]

## Deliverables
- Named output 1 (format: ...)
- Named output 2 (format: ...)

## Domain Rules
- Critical constraints for this professional domain
- What this specialist will and won't do
- When to surface a decision to the user vs. proceed automatically
```

Specialist templates use only `{{PREAMBLE}}` — no `{{NAME_METHODOLOGY}}` tokens. The `methodology.md` for each specialist is a condensed version of the Workflow + Domain Rules sections, authored separately for use by job templates.

---

## Entry Point Routing

The main `/gteam` skill receives a user's goal and routes automatically:

1. **Exact job match** — if the goal clearly maps to a defined job (`content-campaign`, `legal-review`, `product-launch`), begin that job immediately and announce what was selected
2. **Partial match / ambiguous** — if 2–3 jobs could apply, present them as numbered options and ask the user to choose (one question, no preamble)
3. **No job match** — fall through to the most relevant specialist and invoke it directly
4. **Multi-goal** — if the goal spans multiple independent jobs (e.g. "review this contract AND build a campaign"), execute jobs sequentially, delivering each output before starting the next

The routing decision is shown to the user: "Starting `content-campaign` — this will run SEO, Content Creator, and Social Media in sequence."

---

## Testing

### Tier 1 — Static Validation (free, <2s)
- Parses every `$B` command in all SKILL.md files, validates against browse command registry (imported from `browse/src/commands.ts`)
- Validates SKILL.md frontmatter: required fields (`name`, `version`, `description`, `allowed-tools`), no unknown fields
- Checks all `{{PLACEHOLDER}}` tokens in `.tmpl` files resolve to a known placeholder or a `specialists/*/methodology.md` file
- `skill-check.ts` auto-discovers skills by scanning `specialists/*/SKILL.md` and `jobs/*/SKILL.md` — no hardcoded list
- Runs on every `bun test`

### Tier 3 — LLM-as-judge (no API key required)

GTeam does not require a paid Anthropic API key. The judge runs via one of two backends, selected automatically:

| Backend | How | When used |
|---|---|---|
| `claude -p` subprocess | Spawns Claude Code CLI as a subprocess (uses existing Claude subscription) | Default — if `claude` is on PATH |
| Local LLM via Ollama | HTTP call to `localhost:11434` with a capable model (e.g. `llama3`, `mistral`) | Fallback — if `claude` not available, or `GTEAM_JUDGE=ollama` is set |

The judge evaluates each specialist and job SKILL.md on four dimensions (0–100 each, threshold ≥70 to pass):

| Dimension | What it checks |
|---|---|
| Clarity | Can a non-expert understand the output and deliverables? |
| Completeness | Does the workflow cover the key professional obligations for this domain? |
| Actionability | Does Claude produce concrete deliverables, not vague advice? |
| Domain accuracy | Checked against a per-specialist reference prompt (see below) |

**Domain accuracy reference prompts** (defined per specialist, checked against output):
- `lawyer`: Does it check for liability clauses, indemnification, IP ownership, termination rights, governing law?
- `accountant`: Does it flag cash flow issues, tax exposure, missing categorisation, reconciliation gaps?
- `seo`: Does it check title tags, meta descriptions, Core Web Vitals, backlink profile, keyword cannibalisation?
- `social-media`: Does it cover platform-specific formats, posting cadence, engagement hooks, hashtag strategy?
- `email-marketer`: Does it cover subject line testing, segmentation, deliverability, sequence timing, CTA clarity?
- `content-creator`: Does it check keyword integration, readability score, CTA presence, internal linking?

Results saved to `~/.gteam-dev/evals/`. Run via `bun run test:evals`.

**Diff-based selection mechanism:** On each eval run, the evaluator computes a SHA-256 hash of each skill's source files (`SKILL.md.tmpl` + `methodology.md` if present) and compares against hashes stored in `~/.gteam-dev/evals/.skill-hashes.json`. Skills whose hash matches the stored value are skipped. Hashes are updated after a passing eval run. Use `EVALS_ALL=1` or `bun run test:evals:all` to force evaluation of all skills regardless of hash.

### Tier 2 — E2E (deferred)
Added in a future version. Will also use `claude -p` subprocess — no API key required.

---

## Autonomy Design Principle

GTeam skills are designed to **minimise human-in-the-loop interruptions**. The standard pattern:

- **Do automatically:** all research, analysis, drafting, formatting, file writes
- **Ask the user only when:** a decision has meaningful consequences they'd care about (e.g. "I found a high-risk clause — do you want to negotiate it out or flag it as accepted risk?")
- **Never ask about:** process steps, tool choices, formatting preferences, intermediate results

---

## Relationship to gstack

GTeam is an independent project. It:
- References gstack in its description/README as inspiration
- Borrows the browse binary via git submodule (full gstack repo)
- Adapts gstack's `gen-skill-docs.ts` template generator and `skill-check.ts`
- Does **not** depend on gstack being installed at runtime
- Has its own release cycle, versioning, and CHANGELOG

---

## Out of Scope (v1)

- Tier 2 E2E testing
- Parallel job execution (multiple specialists running simultaneously)
- Job state persistence between sessions
- skill-seekers integration (auto-generating skills from documentation scraping)
- Custom job builder UI
- Non-English specialists
- Accountant and email-marketer specialists embedded in `product-launch` job (context length — deferred to v2)
