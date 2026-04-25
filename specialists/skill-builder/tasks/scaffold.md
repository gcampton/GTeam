## Scaffold New Specialist

**Use when:** User wants to create a new specialist from scratch.

**Gather:** Specialist name (kebab-case), domain/role, key capabilities (3–5), target category.

**Step 1 — Create directory structure:**
```bash
GTEAM=~/dev/1_myprojects/gteam
NAME=<specialist-name>

mkdir -p $GTEAM/specialists/$NAME/references
mkdir -p $GTEAM/specialists/$NAME/evals
mkdir -p $GTEAM/specialists/$NAME/results
```

**Step 2 — Write `methodology.md`:**

Synthesize collected reference content into a structured methodology covering:
- Domain workflow (phases, decision points)
- Quality standards and professional rules
- Common patterns and anti-patterns
- Output formats

**Step 3 — Write `SKILL.md.tmpl`:**

Follow this exact structure:
```markdown
---
name: gteam-<name>
version: 1.0.0
description: <one-line description>
type: standalone
category: <category>
allowed-tools:
  - Read
  - Write
  - Bash
  - WebFetch
  - WebSearch
  - Glob
  - Grep
---

{{PREAMBLE}}

# <Role Title> — GTeam

## Role

You are a [senior/expert] <role> specialising in <domain>. <2-3 sentences on what makes this specialist distinct — methodology, depth, professional standards it holds itself to.>

## When to Use

- <trigger scenario 1>
- <trigger scenario 2>
- <trigger scenario 3>

## Not For

- <out-of-scope scenario 1> (use <other specialist> instead)
- <out-of-scope scenario 2>

## Workflow

{{<NAME>_METHODOLOGY}}

## Reference Materials

Domain frameworks and reference files are in `{{GTEAM_DIR}}/specialists/<name>/references/`:

<list any scraped reference files installed>

**Before starting any task:**
1. Read relevant reference files for the task at hand
2. Check `{{GTEAM_DIR}}/specialists/<name>/results/` for prior work on similar tasks
```

Token naming rule: directory `content-creator` → token `{{CONTENT_CREATOR_METHODOLOGY}}`
Formula: `dirName.toUpperCase().replace(/-/g, '_') + '_METHODOLOGY'`

**Step 4 — Generate SKILL.md:**
```bash
cd ~/dev/1_myprojects/gteam && bun run gen:skill-docs
```

**Step 5 — Create a placeholder eval:**
```bash
cat > $GTEAM/specialists/$NAME/evals/scenarios.md << 'EOF'
# <Name> Eval Scenarios

## Scenario 1: [Description]
**Input:** ...
**Expected:** ...
**Criteria:** relevance, completeness, actionability, methodology alignment
EOF
```

**Deliver:** Confirm which files were created, run `bun run skill:check` to verify the specialist registers correctly.
