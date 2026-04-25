## Disaster Recovery

**Service tier targets:**

| Tier | RTO | RPO | Examples |
|------|-----|-----|----------|
| **Tier 1** (critical) | < 1 hour | < 5 minutes | Payment processing, auth, primary database |
| **Tier 2** (important) | < 4 hours | < 1 hour | Search, notifications, reporting |
| **Tier 3** (standard) | < 24 hours | < 24 hours | Internal tools, analytics, batch jobs |

- **RTO** (Recovery Time Objective) — max acceptable downtime
- **RPO** (Recovery Point Objective) — max acceptable data loss

**Backup strategy:**
- [ ] Automated backups at frequency matching RPO (Tier 1: continuous/WAL, Tier 2: hourly, Tier 3: daily)
- [ ] Retention: 7 days minimum, 30 days for compliance-sensitive data
- [ ] Cross-region replication for Tier 1 services
- [ ] Backups encrypted at rest and in transit

**Failover testing:**
- [ ] Quarterly game days — simulate failure of each Tier 1 dependency
- [ ] Document runbooks for every failover scenario before the game day
- [ ] Time the actual RTO during game day; compare to target; file action items for gaps

**Restore verification:**
- [ ] Monthly restore-from-backup test for Tier 1 databases
- [ ] Verify data integrity post-restore (row counts, checksums, sample queries)
- [ ] Log restore duration — if it exceeds RTO, the backup strategy needs revision
