## Output Formats

**Pricing Recommendation Report:**

```markdown
# Pricing Strategy: [Product Name]

## Executive Summary
[1–2 sentences: what we recommend and why]

## Current State Assessment
- Pricing metric: [current / recommended]
- Tier structure: [current / recommended]
- Conversion rate at pricing page: [current]
- ARPU: [current] / target: [recommended]

## Recommended Tier Structure

| Tier | Price (monthly) | Price (annual) | Target customer |
|------|-----------------|----------------|-----------------|
| [Name] | $[X]/mo | $[Y]/mo | [who] |
| [Name] ⭐ | $[X]/mo | $[Y]/mo | [who] |
| [Name] | $[X]/mo | $[Y]/mo | [who] |

## Feature Allocation
[Table: Feature → which tier(s) include it → rationale]

## Price Point Rationale
[Research method used, competitive comparison, willingness-to-pay evidence]

## Pricing Page Recommendations
[Specific changes to the current pricing page, ordered by impact]

## Implementation Risks
[What could go wrong, how to mitigate it]

## 90-Day Rollout Plan
[Phased approach: test → announce → launch → monitor]
```

Save output to `~/dev/1_myprojects/gteam/specialists/pricing-strategy/results/[company]-pricing-[date].md`
