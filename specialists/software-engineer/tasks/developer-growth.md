## Developer Growth Analysis

**Use when:** Assessing a developer's skill gaps, preparing for performance reviews, or creating a personal development plan based on actual work patterns rather than generic checklists.

**Evidence sources:**
- Git history: `git log --author="name" --since="30 days ago" --stat` — what files and areas they've been touching
- PR review comments: patterns in feedback received (recurring themes = skill gaps)
- Claude Code chat history: `~/.claude/history.jsonl` — problems they struggled with, questions they asked repeatedly
- Bug tracker: types of bugs they introduced or fixed (categories reveal blind spots)
- Code review given: quality of review comments they leave for others

**Analysis framework:**

1. **Map work patterns:**
   - What areas of the codebase do they work in most?
   - What types of tasks? (feature implementation, bug fixes, refactoring, infrastructure, tests)
   - What technologies are they using vs avoiding?
   - What's their commit frequency and size pattern? (many small = incremental; few large = batch mode)

2. **Identify skill gaps (evidence-based, not assumed):**
   For each gap, require specific evidence:
   
   | Gap | Evidence | Impact | Priority |
   |---|---|---|---|
   | [Specific skill] | [What was observed — PR comment, repeated bug type, struggled question] | [How this affects their work] | HIGH/MED/LOW |
   
   Good gap identification:
   - "TypeScript generics — struggled typing auth config in 3 PRs this month"
   - "Error handling — 4 bugs in last sprint were missing null checks"
   - "Database query performance — rewrote the same query 3 times seeking optimisation"
   
   Bad gap identification (too vague):
   - "Needs to improve coding skills"
   - "Should learn more about the stack"

3. **Identify strengths:**
   Equally important — what are they consistently good at?
   - Areas where their PRs get approved with minimal changes
   - Bug categories they never introduce
   - Types of problems they solve efficiently
   - Quality of code reviews they give

4. **Generate development plan:**

   ```markdown
   # Developer Growth Report: [Name]
   
   **Period:** [date range]
   **Based on:** [git history / PR reviews / chat history / bug tracker]
   
   ## Work Summary
   [2-3 sentences: what they focused on, technologies used, types of contributions]
   
   ## Strengths
   1. [Strength with evidence]
   2. [Strength with evidence]
   3. [Strength with evidence]
   
   ## Growth Areas (Prioritised)
   
   ### 1. [Skill Gap]
   **Evidence:** [specific observations]
   **Why it matters:** [impact on code quality / velocity / team]
   **Recommended action:** [specific learning path or practice]
   **Time estimate:** [X hours of focused learning]
   
   ### 2. [Skill Gap]
   [same structure]
   
   ## Action Items (next 30 days)
   1. [Concrete action tied to #1 priority gap]
   2. [Concrete action tied to #2 priority gap]
   3. [Practice exercise or project to reinforce learning]
   
   ## Recommended Resources
   - [Specific article/course/repo relevant to gap #1]
   - [Specific article/course/repo relevant to gap #2]
   ```

**Integration with performance reviews:**
When used alongside the hr-specialist's performance review templates, the growth report provides the evidence base. The HR specialist provides the structure and rating framework; the software-engineer specialist provides the technical substance.

**Self-assessment mode:**
Developers can run this on their own work: `git log --author="$(git config user.name)" --since="30 days ago" --stat` and ask for a growth analysis. This is a self-coaching tool, not just a management tool.
