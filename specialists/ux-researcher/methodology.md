### Research Planning

**Frame the research question before choosing a method:**
"We need to understand [X] so we can decide [Y]."

If you cannot complete that sentence, the research is not ready to begin. Do not start recruiting until the decision it serves is named.

**Method selection:**
- Generative (understanding the problem space): user interviews, diary studies, contextual inquiry, field observation
- Evaluative (testing a solution): usability testing, A/B testing, first-click testing, concept testing
- Quantitative (measuring prevalence or significance): surveys (100+ responses for meaningful segmentation), analytics review, card sorting at scale

Use qualitative methods when the question is "why" or "how". Use quantitative when the question is "how many" or "how much".

**Recruiting criteria — define before writing a screener:**
- Primary characteristic: the key behaviour or context that qualifies someone (e.g. "has purchased online in the last 30 days", not "ages 25–45")
- Screener questions: 5–8 maximum, written to reveal behaviour not self-report ("How often do you..." not "Do you...")
- Sample size: 5–8 participants for usability testing and interviews (diminishing returns after 5 for most qualitative studies); 100+ for surveys; 1,000+ for A/B tests
- Diversity targets: representation by role, experience level, and context of use — not just demographics

**Timeline and deliverables — define upfront:**
- Recruiting: 5–7 business days minimum for external participants
- Sessions: schedule over 3–5 days to allow daily debriefs before memory fades
- Analysis: 2–3 days for synthesis
- Report: 1–2 days for writing

Commit to a specific decision the research will inform and by when.

---

### User Interviews

**Discussion guide structure:**

1. Warm-up (2 min): put the participant at ease, explain the session format and that you're testing the product not them, confirm recording consent
2. Context (5 min): understand their background, role, and relationship to the subject area — do not show the product yet
3. Core questions (20–30 min): explore their current behaviour, mental models, and pain points
4. Concept reaction (10 min, if applicable): show a design, prototype, or concept — observe first, then ask
5. Close (3 min): ask what we didn't ask, thank them, explain next steps

**Question types:**
- Past behaviour: "Tell me about the last time you [did the relevant task]. Walk me through what happened." — reliable, grounded in real experience
- Not hypotheticals: do not ask "Would you use a feature that...?" or "How often do you think you would...?" — people are inaccurate predictors of their own future behaviour
- Exploratory: "What made you decide to do it that way?", "What happened next?", "What were you hoping to happen?"

**Probing techniques:**
- "Tell me more about that." (open follow-up — use when an answer is too brief)
- "What did you do then?" (timeline probe — keeps the story grounded in action)
- Silence: after a participant finishes speaking, wait 3–5 seconds before asking the next question. Most participants will add something important.
- "You mentioned [X] — can you say more about what you meant by that?" (echo probe)
- Avoid leading: never say "So it sounds like you found that confusing?" — rephrase as "How did that feel?"

---

### Usability Testing

**Task scenario writing — rules:**
- Realistic: base scenarios on actual tasks real users have, not simplified versions
- Not leading: "Try to find out what you owe this month" — not "Click the billing tab to see your invoice"
- No hints: do not include terminology from the UI in the task description
- One goal per task: compound tasks (find X, then do Y) make it impossible to isolate where issues occur

**Think-aloud protocol:**
- Brief participants before the first task: "As you work through this, please say out loud what you're thinking, what you're looking for, and any reactions you have."
- Do not correct or guide during tasks unless the participant is completely blocked and you need to move on
- Note what participants say versus what they actually do — these often diverge

**Severity rating for issues found:**

| Severity | Definition | Priority |
|---|---|---|
| Critical | Blocks task completion — user cannot proceed | Fix before launch |
| High | Significant friction, most users affected, no clear workaround | Fix in current sprint |
| Medium | Workaround exists but is non-obvious or frustrating | Fix in next sprint |
| Low | Cosmetic or affects very few users | Backlog |

**What to observe (beyond task completion):**
- Where users hesitate or pause (indicates uncertainty)
- Where they look before they click (reveals mental model)
- What they say when they fail ("I expected this to be under...")
- Where they succeed despite the design being unclear (false positives — users may complete the task for the wrong reason)

---

### Synthesis & Analysis

**Affinity mapping:**
1. Write one observation per sticky note (digital or physical): participant ID, verbatim quote or behaviour description
2. Group related observations — do not name the groups yet
3. Name the groups once clusters are stable — names should describe what users do or experience, not what the design does
4. Look for patterns across groups: which clusters appear across multiple participants? Which are outliers?

**JTBD (Jobs-to-be-Done) format — use to frame the insight from the user's perspective:**
> "When [situation / trigger], I want to [motivation / action] so I can [intended outcome]."

**Insight format — three parts, always:**
1. Observation: what users did or said (specific, evidenced — cite participant count)
2. So what: why this matters for the product or business
3. Therefore: what the product should do differently (specific and actionable)

**Turning insights into recommendations:**
- Specific: name the element, flow, or feature — not "improve the navigation"
- Actionable: something the team can act on without further research
- Prioritised: sort by impact (how many users affected, how severe the friction) × effort (estimate from engineering)

---

### Deliverables

**Research report structure:**
1. Executive summary: 3 key findings, 3 recommendations — written for someone who will read only this page
2. Methodology: method used, participant count and profile, dates, screener criteria
3. Participants: anonymised overview table (role, experience level, context)
4. Findings: one section per finding, structured as insight format (observation + so what + therefore), with supporting quotes and screenshots
5. Recommendations: prioritised table (recommendation → priority → owner → success metric)

**Journey map format:**
- Stages: the key steps in the user's process (not the product's navigation)
- Actions per stage: what the user physically does
- Thoughts per stage: what the user is thinking (use verbatim quotes)
- Emotions per stage: feeling (frustrated / confused / confident / delighted) — use evidence, not inference
- Opportunities per stage: specific product improvements that would improve this stage

**Presenting to non-researchers:**
- Lead with the findings and recommendations — put methodology in an appendix
- Use one quote and one data point per finding: "6 of 8 participants could not find the export function. One said: 'I looked everywhere — I assumed it just didn't exist.'"
- State what the team should do differently, not what users said — translate, don't transcribe

**Deliver:**
- Research plan (before fieldwork begins)
- Discussion guide or test protocol
- Synthesis notes (affinity map or equivalent)
- Research report with recommendations and priority
- Journey map (if appropriate to scope)
