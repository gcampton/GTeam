### Browse Setup

When a URL is provided, run this setup block before any browse step:

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/.claude/skills/gteam/browse/dist/browse
[ -x "$B" ] && echo "READY: $B" || echo "BROWSE NOT AVAILABLE"
```

If `BROWSE NOT AVAILABLE`: skip all `$B` steps and use WebFetch instead for URL inspection.

---

### Task Router

Route to the appropriate task file based on what the user needs:

| User Need | Task File | When |
|-----------|-----------|------|
| Full or partial WCAG audit | `tasks/wcag-audit.md` | Auditing a page, component, or codebase for WCAG 2.2 compliance |
| Assistive technology testing | `tasks/assistive-tech-testing.md` | Testing with screen readers, keyboard, zoom, colour blindness, motion |
| Fixing accessibility violations | `tasks/remediation.md` | Fixing specific violations with code examples and ARIA patterns |

**Routing rules:**
1. If the user provides a URL or code and asks "is this accessible?" → start with `tasks/wcag-audit.md`
2. If the user asks about screen readers, keyboard navigation, or specific AT → use `tasks/assistive-tech-testing.md`
3. If the user has a known violation and wants a fix → use `tasks/remediation.md`
4. If an audit reveals violations → automatically continue to `tasks/remediation.md` for fixes
5. For a full accessibility review, run all three tasks in sequence: audit → AT testing → remediation

**Load task:** Read the task file, then execute its workflow.
