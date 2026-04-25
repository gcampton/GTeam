## QA Testing

**Gather:** URL of running application, or path to codebase. Clarify: Quick (critical/high bugs only), Standard (+ medium), or Exhaustive (+ cosmetic). Default: Standard. If a URL is provided, use `$B` to load and test the live app.

**Testing sequence:**
1. Load and verify the app starts: `$B goto <url> && $B console && $B snapshot`
2. Test primary user flows end-to-end (registration, login, core feature, logout)
3. Test edge cases: empty inputs, very long inputs, special characters, concurrent actions
4. Test error states: invalid credentials, network failure, missing required fields
5. Test responsive layout: desktop, tablet, mobile breakpoints
6. Check accessibility basics: focusable elements, alt text on images, colour contrast
7. Verify no sensitive data exposed in network responses or localStorage

**For each bug found:**
- Severity: CRITICAL (data loss/security) / HIGH (feature broken) / MEDIUM (degraded UX) / LOW (cosmetic)
- Repro steps (numbered, copy-pasteable)
- Expected vs actual behaviour
- Screenshot or console output as evidence

**Fix loop:** Fix bugs in severity order, commit each fix atomically, re-verify before moving to next.

**Output:**
- Health score before and after (0–100)
- Bug table: component → severity → description → status (fixed/open)
- Ship-readiness verdict
