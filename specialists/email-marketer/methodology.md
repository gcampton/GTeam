### Email Campaign

**Gather:** Product/offer, audience segment, campaign goal (acquisition/nurture/re-engagement/announcement), existing sequences if any, ESP (Mailchimp, Klaviyo, ActiveCampaign, etc.).

**Campaign design:**
1. Sequence map: how many emails, timing (Day 0, Day 3, Day 7...)
2. Segmentation: who gets this, who's excluded, any personalisation variables
3. Deliverability pre-check: SPF/DKIM/DMARC status, list hygiene (remove hard bounces + unengaged > 90 days)

**Per email — write:**
- Subject line (+ 2 A/B variants)
- Preview text (40–90 chars — extends the subject line, don't repeat it)
- Full email body (plain text first, then HTML layout notes)
- Primary CTA (button copy + destination URL)

**Subject line rules:**
- 40 characters or fewer for mobile preview
- Avoid spam triggers: FREE, URGENT, !!!, ALL CAPS, excessive punctuation
- Curiosity gap, personalisation, or specificity — pick one approach per email
- Test: would you open this if a stranger sent it?

**Deliver:**
- Sequence map (ASCII diagram)
- Full copy for each email
- Subject line A/B variants
- Deliverability setup checklist (SPF/DKIM/DMARC)

---

### Welcome & Onboarding Sequence

**Use for:** New subscribers, new trial users, new customers. Goal: deliver immediate value, establish expectations, drive first key action.

**Sequence structure (7–10 days):**

| Email | Timing | Job to be done | CTA |
|-------|--------|---------------|-----|
| Welcome | Immediately | Deliver what was promised, set expectations | Primary action (activate, explore, download) |
| Value #1 | Day 2 | Single insight or tip that makes them successful fast | Optional — keep trust-building |
| Value #2 | Day 4 | Address top objection or common question | Soft CTA (read a case study, watch a video) |
| Social proof | Day 6 | Customer story or result — make it specific | Trial/demo/purchase CTA |
| Conversion | Day 9 | Hard offer (upgrade, book call, buy) | Direct CTA |

**Writing principles for onboarding:**
- Email 1: deliver the lead magnet or welcome bonus first — then the message
- Never sell in email 1; earn trust first
- Use "you" not "we" — focus on what the subscriber gets, not what you offer
- One CTA per email; competing CTAs reduce clicks

**Personalisation where possible:**
- `{{first_name}}` in subject line increases open rate ~5–10%
- Segment by signup source: different welcome for blog subscriber vs trial user vs buyer
- Trigger sequences from behaviour: viewed pricing page → send conversion email sooner

**Deliver:**
- Full 5-email welcome sequence (copy-ready)
- Subject lines + A/B variants for each
- Segmentation rules (who gets which version)
- Plain text + HTML layout notes

---

### List Health & Deliverability

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

---

### A/B Testing & Optimisation

**Gather:** ESP with A/B testing capability, list size (need ≥ 2,000 for statistically meaningful tests), current performance baseline (open rate, click rate, conversion rate).

**What to test and in what order:**

| Test priority | Variable | Why it matters | Minimum list size |
|--------------|---------|---------------|-----------------|
| 1 | Subject line | Drives open rate — everything else is moot if email isn't opened | 1,000 |
| 2 | From name | "Sarah from Acme" vs "Acme" — affects trust and opens | 1,000 |
| 3 | Send time / day | Different audiences have different peak open windows | 2,000 |
| 4 | CTA copy | "Get started" vs "Start your free trial" — affects clicks | 2,000 |
| 5 | Email length | Long vs short — depends heavily on audience and offer | 3,000 |
| 6 | Plain text vs HTML | Some audiences prefer plain; affects deliverability | 3,000 |

**Test discipline:**
- Test one variable at a time — never two simultaneously
- Split 50/50 to the test segment; hold a control group
- Wait for statistical significance before declaring a winner (80% confidence minimum)
- Sample size: use calculator (`n = (16σ²/δ²)` or just use > 200 per variant as minimum)
- Document every test: hypothesis, result, confidence level, what was learned

**Optimisation targets per metric:**
- Low open rate (< 20%): test subject lines, from name, send time
- Low click rate (< 1.5%): test CTA copy, button placement, email length, offer clarity
- Low conversion (clicks not converting): problem is on the landing page, not the email

**Deliver:**
- Testing roadmap: 4–6 tests in priority order
- Hypothesis per test (if we change X, we expect Y to improve because Z)
- Results tracker template
- Recommendations based on any existing test data provided

---

### Lifecycle & Automation Map

**Gather:** Business model (SaaS, e-commerce, services), customer journey stages, existing automations if any, key user actions/events that can trigger emails.

**Core lifecycle automations to build:**

**E-commerce:**
1. Abandoned cart (1h, 24h, 72h) — recover lost revenue; 15% recovery rate typical
2. Post-purchase (Day 1: receipt, Day 3: how to use, Day 14: review request)
3. Win-back (90 days no purchase: re-engagement offer)
4. VIP / loyalty tier upgrade (trigger: hits spend threshold)

**SaaS:**
1. Trial onboarding (welcome → feature education → conversion — 7–10 days)
2. Feature adoption (trigger: user hasn't used key feature in 7 days)
3. Trial expiry warning (3 days before, 1 day before, day of)
4. Churn prevention (trigger: usage drops 50% from baseline — send check-in)
5. Expansion (trigger: approaching usage limit — upgrade nudge)

**Services / B2B:**
1. Lead nurture (content education sequence — 4–6 weeks)
2. Proposal follow-up (Day 1, Day 4, Day 8 after proposal sent)
3. Client onboarding (welcome, kickoff prep, check-in at 30 days)
4. Re-engagement (no contact in 6 months — catch-up email)

**Automation rules:**
- Always have an exit condition: if user converts, remove from nurture sequence
- Suppress paying customers from acquisition emails
- Cap frequency: no more than 1 automated email per day, regardless of triggers
- Review automations quarterly — stale copy and broken links cost more than they earn

**Deliver:**
- Lifecycle automation map (flow diagram in text/ASCII)
- Priority order: which 2–3 automations to build first and why
- Copy brief for each automation (objective, tone, key message, CTA)
- Trigger / exit condition spec for developer or ESP configuration
