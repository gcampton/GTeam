## Usability Testing

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
