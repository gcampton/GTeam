## Lead Routing Rules

Routing must be deterministic — no manual assignment queues for standard leads.

**Routing decision tree:**

```
Is the lead an existing customer account?
  → YES → Route to owning CSM (account-based routing)
  → NO:
    Does the lead have a company domain matching an existing opportunity?
      → YES → Route to owning AE (account-based routing)
      → NO:
        Is this an inbound demo request?
          → YES → Route round-robin to SDR pool (by territory if applicable)
          → NO:
            Does the lead meet MQL threshold?
              → YES → Route to SDR pool (round-robin or territory)
              → NO → Nurture sequence, no SDR assignment
```

**Territory-based routing:** If you have geographic or segment-based territories, routing must check:
1. Company HQ country/state → territory lookup table → assigned rep
2. If territory is open (no rep), route to manager or hold queue with SLA alert

**SLA rules (must be enforced via CRM automation):**
- Inbound demo request: first outreach within 5 minutes (speed-to-lead is the #1 conversion driver)
- MQL → SDR review: within 4 business hours
- SAL → discovery call: within 2 business days
- If SLA breached: auto-alert manager, re-route if no activity within 24h
