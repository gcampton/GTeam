## Long-Form Documentation Structure

For comprehensive technical manuals (10+ pages):

**Standard section order:**

1. Executive summary (1 page — what, why, for whom)
2. Architecture overview (diagrams + narrative)
3. Key design decisions (ADR format: context → decision → consequences)
4. Component deep-dives (one per major component)
5. Data model and flows
6. Security model (authn, authz, data classification)
7. Operations guide (deploy, monitor, troubleshoot, scale)
8. API reference (if applicable)
9. Glossary
10. Appendices (configuration reference, migration guides)

**Cross-document linking:**

- Every page should link to its parent and siblings
- Use consistent anchor naming: `#{section}-{subsection}`
- Include "Prerequisites" at top linking to required reading
- Include "Next steps" at bottom linking to logical next document

The test: can a reader enter at any section and orient themselves within 30 seconds? If not, add context links and a "where you are" breadcrumb.
