# Email Deliverability Technical Guide

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Deliverability is infrastructure first, content second. A perfect email that lands in spam is worthless. Audit the DNS layer before optimising subject lines.

---

## DNS Authentication Records

Three records control whether receiving mail servers trust your email. All three must be in place before sending at volume.

### SPF — Sender Policy Framework

**What it does:** Declares which mail servers are authorised to send email on behalf of your domain.

**How it works:** A receiving server checks the `From` domain's DNS for a TXT record listing approved IP ranges. If the sending IP isn't listed, the email may be rejected or marked as spam.

**Example record:**
```
TXT yourdomain.com "v=spf1 include:_spf.google.com include:sendgrid.net ~all"
```

- `include:` — authorises a third-party sender's IP ranges
- `~all` — soft fail (suspicious but not rejected); `-all` is hard fail (reject)
- Use `~all` during initial setup; move to `-all` once you've verified all legitimate sending sources

**Verify:**
```bash
dig TXT yourdomain.com
```
Look for the record starting with `v=spf1`.

---

### DKIM — DomainKeys Identified Mail

**What it does:** Adds a cryptographic signature to each outgoing email. The receiving server verifies the signature against a public key in your DNS. If the signature matches, the email hasn't been tampered with in transit.

**How it works:** Your email provider generates a private/public key pair. The private key signs emails; the public key is published as a DNS TXT record at a selector subdomain.

**Example record location:**
```
TXT google._domainkey.yourdomain.com
```
(`google` is the selector — your provider will specify theirs)

**Verify:**
```bash
dig TXT google._domainkey.yourdomain.com
```
Look for a long string beginning with `v=DKIM1; k=rsa; p=...`

`[HYPOTHESIS]` DKIM is the most important of the three records for inbox placement. SPF alone is insufficient — Gmail and Yahoo have required DKIM alignment since 2024's sender policy updates.

---

### DMARC — Domain-based Message Authentication, Reporting & Conformance

**What it does:** Tells receiving servers what to do when SPF or DKIM fails, and sends you reports of authentication results.

**Policies:**
- `p=none` — monitor only, take no action (use during initial setup)
- `p=quarantine` — failed emails go to spam
- `p=reject` — failed emails are rejected entirely

**Example record:**
```
TXT _dmarc.yourdomain.com "v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com; pct=100"
```

- `rua=` — where aggregate reports are sent (use a real mailbox or a DMARC reporting tool)
- `pct=` — percentage of emails the policy applies to (start at 10, increase as you gain confidence)

**Setup sequence:**
1. Start at `p=none` with reporting → read the reports for 2–4 weeks
2. Move to `p=quarantine; pct=10` → monitor for legitimate mail being flagged
3. Escalate to `p=quarantine; pct=100`
4. Move to `p=reject` when no legitimate sources are failing

**Authentication checklist:**
- [ ] SPF record exists and includes all active sending services
- [ ] DKIM enabled and DNS record published for each sending service
- [ ] DMARC record exists with at least `p=none` and `rua=` reporting address
- [ ] DMARC reports are being monitored (use a tool like Postmark DMARC, Dmarcian, or Valimail)

---

## List Hygiene

A clean list protects your sender reputation. Sending to bad addresses is the fastest way to land in spam permanently.

### Bounce Handling

| Bounce type | Definition | Action |
|-------------|-----------|--------|
| **Hard bounce** | Permanent delivery failure (invalid address, domain doesn't exist) | Remove immediately and suppress — never retry |
| **Soft bounce** | Temporary failure (mailbox full, server timeout) | Retry; remove after 3 consecutive soft bounces |

`[HYPOTHESIS]` Most ESPs handle hard bounces automatically, but soft bounce handling varies. Confirm your ESP's soft bounce policy and supplement with manual review if the list is large. A soft bounce rate above 2% on a send indicates a list quality problem.

### Engagement Segmentation

Unengaged subscribers damage sender reputation even if they don't bounce.

**Segmentation thresholds:**

| Segment | Definition | Action |
|---------|-----------|--------|
| Active | Opened or clicked in last 90 days | Normal sends |
| At-risk | No engagement in 91–180 days | Reduce frequency, send re-engagement |
| Unengaged | No engagement in 181+ days | Sunset sequence before unsubscribe |

**90-day rule:** Move subscribers with zero opens or clicks in 90 days to a sunset sequence. Do not continue sending full campaigns to this segment.

`[HYPOTHESIS]` Some subscribers open with image loading disabled — click-only tracking underestimates engagement. If your ESP allows it, use click data as the primary engagement signal rather than opens alone.

---

## Sunset Sequence

A 3-email re-engagement sequence run before removing unengaged subscribers.

```
Email 1 — "Are we still useful to you?"
Subject: "Quick question, [First name]"
Body: Acknowledge absence. Ask if still relevant. Single yes/no CTA.
Action if no click: move to Email 2 after 5 days.

Email 2 — "Here's what you've been missing"
Subject: "Our best content from the last 6 months"
Body: Value-led. No pressure. Curate 2–3 highest-performing pieces.
Action if no click: move to Email 3 after 5 days.

Email 3 — "We're removing you from our list"
Subject: "Last email from us (unless you want to stay)"
Body: Transparent. Explain the removal. Single CTA to confirm subscription.
Action if no click: unsubscribe and add to suppression list.
```

`[HYPOTHESIS]` The honest "this is our last email" subject line consistently outperforms clever alternatives in re-engagement sequences. The reader appreciates the respect and re-engages at higher rates than with guilt-based or urgency-based messaging.

---

## Spam Triggers to Avoid

### Subject line triggers

| Trigger | Example | Why it fails |
|---------|---------|-------------|
| ALL CAPS | "FREE OFFER INSIDE" | Spam filter heuristic; low trust signal |
| Excessive punctuation | "Wow!!! Act NOW!!!" | Pattern-match for spam |
| Classic spam words | FREE, URGENT, WINNER, GUARANTEED, ACT NOW | Trained spam filter triggers |
| Misleading subjects | "Re: our conversation" (when there was none) | CAN-SPAM violation + trust damage |
| Dollar signs | "$$$", "Make $5,000 this week" | Direct spam signal |

### Content triggers

- **Image-only emails (no visible text):** Spam filters can't read images. Always include substantial text alongside images.
- **Spam word density in body:** Avoid concentrations of "free", "guarantee", "risk-free", "no obligation" in close proximity.
- **Red text on white background:** A known spam visual pattern.
- **Broken HTML:** Spam filters use HTML quality as a trust signal. Validate HTML before sending.
- **Too many links:** More than 3–5 links in a short email raises filter flags.

`[HYPOTHESIS]` Modern spam filters (especially Gmail's) are ML-based and harder to game with simple word avoidance. The stronger signal is engagement history: an email sent to an engaged list will land in inbox even with "free" in the subject. Prioritise list quality over word avoidance.

---

## Sender Reputation and Domain Warm-Up

A new sending domain has no reputation. ISPs throttle or spam-folder email from unknown senders until a positive history is established.

### New domain warm-up schedule

| Week | Daily send volume | Notes |
|------|-------------------|-------|
| 1 | 20–50 | Send only to your most-engaged subscribers |
| 2 | 100–200 | Continue with high engagement segment |
| 3 | 400–500 | Expand to active list |
| 4 | 1,000–2,000 | Can begin normal list sends |
| 5+ | Double weekly | Continue doubling until target volume |

**Rules during warm-up:**
- [ ] Send only to opt-in, engaged contacts — no cold lists during warm-up
- [ ] Monitor spam complaint rate daily (target: below 0.1%; Google threshold: 0.3% for domain suspension)
- [ ] Monitor bounce rate — above 5% indicates a list quality issue
- [ ] Never send a "big blast" — gradual ramp is the only signal ISPs trust

`[HYPOTHESIS]` Warm-up with a dedicated IP is more controllable than warming up on a shared IP, but requires volume to maintain (shared IPs are acceptable below ~100k emails/month). Confirm with your ESP which IP type you're on before setting warm-up expectations.

### Consistent sending frequency

Irregular sending damages reputation. An account that sends 50,000 emails once a month after weeks of silence looks like a spam account to ISPs.

- Send consistently: same day(s) of week, predictable cadence
- If scaling up rapidly, ramp gradually — don't jump from 1,000/week to 50,000/week overnight
- Maintain minimum activity on all sending domains: at least one send per 2 weeks to keep the domain warm

---

## Platform-Specific Notes

### Gmail

- **Clipping at 102KB:** Gmail truncates emails above 102KB HTML size, replacing remaining content with a "View entire message" link. Most recipients won't click it. Keep HTML lean — avoid large inline CSS, repetitive code.
- **Check your HTML size:** In Gmail, open the email → three-dot menu → "Show original" → check "Message size" at the top.
- **Promotions tab escape tactics `[HYPOTHESIS]`:**
  - Plain-text or minimal-HTML emails route more reliably to Primary
  - Reduce image-to-text ratio
  - Avoid marketing-pattern HTML (single-column table layout, large images, multiple buttons)
  - Include a direct reply prompt ("Reply to this email with your question") — two-way conversation signals move emails to Primary
  - Ask subscribers to drag the email to Primary and click "Do this for all from [sender]"
  - Note: none of these are guaranteed — Gmail's tab routing is ML-based and changes without notice

### Outlook / Microsoft 365

- Does not support background images in CSS
- Limited CSS support vs Gmail — test thoroughly in Litmus or Email on Acid
- Microsoft's spam filter (SmartScreen) is reputation-based — clean list hygiene matters more than content tweaks

### Apple Mail Privacy Protection

- Apple MPP pre-loads email pixels for iOS 15+ users, inflating open rates
- `[HYPOTHESIS]` Open rates are unreliable as an engagement metric since 2021. Use click rate, reply rate, and conversion rate as primary engagement signals.

**Deliverability monitoring checklist (run monthly):**
- [ ] Bounce rate below 2%
- [ ] Spam complaint rate below 0.1%
- [ ] SPF, DKIM, DMARC all passing (check via MXToolbox or mail-tester.com)
- [ ] No blacklist listings (check at MXToolbox Blacklist Check)
- [ ] Gmail Postmaster Tools active and monitored for domain reputation
- [ ] Unengaged segment moved to sunset sequence before it grows above 20% of list
