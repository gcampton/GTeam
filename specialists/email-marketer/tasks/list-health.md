## List Health & Deliverability

**Gather:** ESP name, list size, current open rate / click rate / bounce rate, last list clean date, sending domain age, any spam complaints history.

**Deliverability foundations:**

1. **Authentication — non-negotiable:**
   - SPF record: `v=spf1 include:<esp_domain> ~all` in DNS
   - DKIM: ESP-provided key added to DNS (1024-bit minimum, 2048-bit preferred)
   - DMARC: `v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com` (start with `p=none` to monitor first)
   - BIMI (optional): brand logo in inbox — requires DMARC + VMC

2. **List hygiene:**
   - Remove hard bounces immediately after first bounce
   - Remove soft bounces after 3 consecutive failures
   - Sunset unengaged subscribers (no open in 90 days): send a re-engagement sequence first, then remove
   - Never buy lists; only use confirmed opt-in sources

3. **Sending behaviour:**
   - Warm up new domains: start with 50/day, double weekly over 4–6 weeks
   - Consistent send cadence (irregular spikes trigger spam filters)
   - Send at subscriber's local time where segmentation allows
   - Text-to-image ratio ≥ 60:40 (too many images = spam filter trigger)
   - Always include plain text version

4. **Spam trigger audit:**
   - Run subject lines through a spam checker before sending
   - Avoid: too many links, no unsubscribe link, ALL CAPS, exclamation overload
   - Unsubscribe link must be visible; one-click unsubscribe required (Gmail/Yahoo 2024 rules)

**Health benchmarks by industry:**

| Metric | Good | Warning | Action needed |
|--------|------|---------|---------------|
| Open rate | > 25% | 15–25% | < 15% — list or deliverability issue |
| Click rate | > 2.5% | 1–2.5% | < 1% — content or CTA issue |
| Bounce rate | < 0.5% | 0.5–2% | > 2% — clean list immediately |
| Spam complaint | < 0.08% | 0.08–0.1% | > 0.1% — pause and investigate |
| Unsubscribe | < 0.5% | 0.5–1% | > 1% — frequency or relevance issue |

**Deliver:**
- DNS configuration instructions for SPF/DKIM/DMARC
- List hygiene action plan (who to remove, suppress, or re-engage)
- Sending warm-up schedule if new domain
- Spam audit results with specific fixes
