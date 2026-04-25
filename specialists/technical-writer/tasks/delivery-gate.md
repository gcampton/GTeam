## Final Documentation Delivery Gate

Before submitting any documentation output:

1. Run a completeness pass against the request prompt and verify every required element is present.
2. Ensure all code blocks are complete and executable (no truncated snippets, placeholders, or partial lines).
3. If writing getting-started docs, include:
   - an upfront 5-line quickstart
   - explicit prerequisites including credentials/API keys
   - progressive auth -> CRUD -> webhooks flow
   - troubleshooting for common setup failures
4. If producing audit/update plans, include:
   - explicit gap-analysis method
   - prioritisation by endpoint usage or business criticality
   - review + verification workflow proving docs match live behavior
5. End with a concise decision-ready summary: what changed, user impact, and recommended next action.
