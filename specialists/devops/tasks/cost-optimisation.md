## Cost Optimisation

| Strategy | Action | Review cadence |
|----------|--------|----------------|
| **Right-sizing** | Compare provisioned vs actual CPU/memory usage; downsize over-provisioned instances | Monthly |
| **Reserved/committed-use** | Commit when steady-state usage > 60% of on-demand capacity | Quarterly |
| **Auto-scaling** | Scale on queue depth or latency, not CPU alone — CPU is a lagging indicator | Set once, review quarterly |
| **Storage tiering** | Hot → warm → cold lifecycle policies; delete old logs/backups per retention policy | Monthly |
| **Unused resources** | Terminate idle instances, unattached volumes, old snapshots, unused load balancers | Monthly |

**Cost alerts:**
- Set budget alerts at **50%**, **80%**, **100%** of monthly forecast
- Alert on per-service cost anomalies (> 20% increase week-over-week)
- Tag all resources by team/service/environment for cost attribution

**Quick wins checklist:**
- [ ] Delete unattached EBS volumes / persistent disks
- [ ] Right-size RDS / Cloud SQL instances (check CPU < 20% sustained)
- [ ] Move infrequently accessed S3/GCS objects to infrequent-access tier
- [ ] Use spot/preemptible instances for CI runners and batch jobs
- [ ] Review NAT gateway / data transfer costs (often overlooked)
