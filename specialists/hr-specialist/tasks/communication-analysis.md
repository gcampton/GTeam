### Communication & Meeting Analysis

**Use when:** Analysing meeting transcripts for behavioural patterns, coaching prep, leadership development, or team dynamics assessment.

**Transcript sources:** Zoom (cloud recording export), Microsoft Teams (transcript download), Google Meet (attached transcript), Granola (markdown export), Otter.ai (export as .txt/.srt). Supported formats: `.txt`, `.md`, `.vtt`, `.srt`. Naming convention: `YYYY-MM-DD-meeting-name.txt`.

**Gather:** Transcript file(s), participant names/roles, context (1:1, team standup, client call, interview), what the analysis is for (coaching, performance review, team health, interview debrief).

---

**Analysis categories — evaluate each that applies:**

**1. Communication style**
- Hedging language frequency ("I think maybe", "sort of", "kind of", "probably")
- Directness ratio — clear statements vs qualifiers
- Filler words ("um", "like", "you know", "basically") per minute of speaking
- Jargon density — insider terms that exclude newcomers

**2. Speaking ratios**
- % of meeting spoken per participant
- Interruptions given vs received per person
- Question vs statement ratio
- Monologue stretches (unbroken speaking > 90 seconds)

**3. Conflict handling**
- Avoidance patterns — topic changes when tension rises
- Deflection — redirecting accountability ("that's not my area")
- Indirect feedback — vague criticism without specifics
- Passive agreement — saying yes without commitment signals

**4. Active listening**
- References to others' points ("As [name] mentioned...")
- Paraphrasing before responding
- Clarifying questions asked
- Building on vs overriding others' ideas

**5. Leadership & facilitation**
- Agenda control — keeping discussion on track
- Inclusion — drawing out quieter participants
- Decision clarity — explicit "we decided X" statements
- Action item assignment — who, what, by when
- Parking lot discipline — deferring tangents without dismissing

**6. Emotional intelligence**
- Empathy signals ("I understand that's frustrating")
- Tone shifts — when and why tone changes
- Acknowledgement of others' feelings before problem-solving
- Celebration/recognition of contributions

---

**Output format per finding:**

```markdown
### [Pattern Name]
**Finding:** [One-sentence summary]
**Frequency:** [X times across Y meetings]
**Example:**
> [Actual quote from transcript]
**Why it matters:** [Impact on team/individual]
**Better approach:** [Specific alternative with example phrasing]
```

---

**Summary report structure:**

```markdown
## Communication Analysis Report
**Period:** [date range] | **Meetings analysed:** [count]
**Subject:** [individual or team name] | **Context:** [purpose of analysis]

### Speaking Statistics
| Participant | % Speaking | Questions Asked | Filler Rate | Interruptions (given/received) |
|-------------|-----------|-----------------|-------------|-------------------------------|

### Key Patterns
**Strengths (top 3)**
1. [Pattern] — [one-line evidence summary]

**Growth areas (top 3)**
1. [Pattern] — [one-line evidence summary]

### Action Items
1. [Concrete behaviour change with example phrasing]
2. ...

### Period Comparison (if prior analysis exists)
| Metric | Previous | Current | Trend |
|--------|----------|---------|-------|
```

---

**Use cases and what to prioritise:**

| Use Case | Priority Categories | Depth |
|----------|-------------------|-------|
| Pre-performance-review coaching | All 6 categories | Deep — quote-heavy |
| Leadership development | 5 (Leadership), 6 (EI), 4 (Listening) | Deep — pattern tracking over time |
| Team dynamics assessment | 2 (Ratios), 3 (Conflict), 4 (Listening) | Broad — all participants |
| Interview debrief | 1 (Style), 5 (Leadership), 4 (Listening) | Focused — interviewer effectiveness |
| Sales/support call review | 1 (Style), 4 (Listening), 6 (EI) | Cross-ref with sales specialist |

**Rules:**
- Never diagnose personality types or apply clinical labels — stick to observable behaviour
- Quote the transcript directly; do not paraphrase evidence
- Frame growth areas as behaviour changes, not character flaws ("say X instead of Y")
- If fewer than 3 meetings are provided, flag that patterns may not be representative
- Compare against prior analyses when available to show trajectory
