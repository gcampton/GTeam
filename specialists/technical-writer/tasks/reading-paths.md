## Reading Paths for Multiple Audiences

Different audiences need different entry points into the same documentation:

| Audience | Needs | Entry Point | Depth |
|---|---|---|---|
| New developer | Get running locally | Quick-start guide | Step-by-step, copy-paste |
| Contributing developer | Understand architecture to make changes | Architecture overview → module docs | Conceptual + reference |
| Operator | Deploy, monitor, troubleshoot | Runbook / operations guide | Procedural |
| Architect | Evaluate design decisions and trade-offs | Architecture Decision Records (ADRs) | Rationale-focused |
| End user | Accomplish tasks with the product | User guide / tutorials | Task-oriented |

Design principle: **progressive disclosure** — start with the simplest useful information, link to deeper detail. Every page should be useful on its own without requiring the reader to have read everything else first.
