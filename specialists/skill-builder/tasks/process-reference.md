## Process into Reference File

After collecting raw content, synthesize into a clean reference markdown file.

**Structure:**
```markdown
# <Technology> Reference

> Source: <url or repo> | Built: <date>

## Overview
[What this technology does — 2-3 sentences]

## Core Concepts
[Key concepts, terminology, mental model]

## [Main Topic 1]
[Content]

## [Main Topic 2]
[Content]

## Common Patterns
[Recipes, examples, typical usage]

## Anti-Patterns
[What to avoid and why]

## Quick Reference
[Cheat sheet: key commands, config options, API endpoints]
```

Remove: marketing copy, nav elements, cookie notices, repetitive boilerplate. Keep: technical specifics, code examples, config schemas, API signatures, error handling.

**Target size:** 20–80KB. Prioritise depth on core concepts over breadth.

**Output location:**
```bash
~/dev/1_myprojects/gteam/specialists/<specialist>/references/<name>.md
```
