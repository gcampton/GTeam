# Multi-Cloud Service Mapping

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Use this table to find equivalent services when migrating between providers or designing multi-cloud architectures.

---

## Service Equivalents

| Category | AWS | Azure | GCP |
|----------|-----|-------|-----|
| **Compute (VMs)** | EC2 | Virtual Machines | Compute Engine |
| **Compute (serverless)** | Lambda | Functions | Cloud Functions |
| **Containers (managed K8s)** | EKS | AKS | GKE |
| **Containers (managed)** | ECS, Fargate | Container Apps | Cloud Run |
| **Object Storage** | S3 | Blob Storage | Cloud Storage |
| **Database (relational)** | RDS, Aurora | Azure SQL, Cosmos DB (SQL) | Cloud SQL, AlloyDB |
| **Database (NoSQL)** | DynamoDB | Cosmos DB | Firestore, Bigtable |
| **Message Queue** | SQS, SNS | Service Bus | Pub/Sub |
| **CDN** | CloudFront | Front Door | Cloud CDN |
| **DNS** | Route 53 | Azure DNS | Cloud DNS |
| **Secrets** | Secrets Manager | Key Vault | Secret Manager |
| **Monitoring** | CloudWatch | Monitor | Cloud Monitoring |
| **Logging** | CloudWatch Logs | Log Analytics | Cloud Logging |
| **Tracing** | X-Ray | Application Insights | Cloud Trace |
| **CI/CD** | CodePipeline | Azure DevOps | Cloud Build |
| **IaC (native)** | CloudFormation | ARM / Bicep | Deployment Manager |
| **Container Registry** | ECR | Container Registry | Artifact Registry |
| **Load Balancer** | ALB / NLB | Load Balancer | Cloud Load Balancing |
| **VPN / Networking** | VPC, Transit Gateway | VNet, Virtual WAN | VPC, Cloud Interconnect |
| **Identity** | IAM, Cognito | Entra ID (AAD) | IAM, Identity Platform |
| **Data Warehouse** | Redshift | Synapse Analytics | BigQuery |
| **Stream Processing** | Kinesis | Event Hubs | Dataflow |

**Note:** Services are approximate equivalents. Feature parity varies — always verify specific capabilities against current provider documentation.

---

## Cross-Provider Tools (IaC)

| Tool | Best for |
|------|----------|
| **Terraform / OpenTofu** | Multi-cloud IaC; largest provider ecosystem; state management required |
| **Pulumi** | Teams preferring real programming languages (TS, Python, Go) over HCL |
| **Crossplane** | K8s-native infrastructure provisioning; gitops workflows |
| **Native (CFN / Bicep / DM)** | Single-cloud shops wanting deepest integration and fastest feature support |

---

## Provider Selection Criteria `[HYPOTHESIS]`

Evaluate these factors before choosing a cloud provider. Rank by importance to your organisation.

| Criterion | Questions to answer |
|-----------|-------------------|
| **Data residency** | Where must data physically reside? Which regions does each provider offer? Are there regulatory constraints (GDPR, data sovereignty)? |
| **Team expertise** | What does the team already know? Migration cost includes learning curve, not just infrastructure. |
| **Pricing model fit** | Sustained-use vs reserved vs spot pricing? Egress costs? Per-request vs per-hour billing for serverless? |
| **Managed service maturity** | Is the managed service production-ready or in preview? Check SLA commitments, not marketing pages. |
| **Existing contracts** | Enterprise agreements, committed spend, credits? Switching cost includes contract penalties. |
| **Ecosystem / integrations** | Does your stack (monitoring, CI/CD, identity) integrate better with one provider? |

**Decision rule:** Default to the provider your team knows best. Multi-cloud adds operational complexity — only adopt it when there is a concrete business requirement (data residency, vendor risk, acquired company on a different cloud). `[HYPOTHESIS]`
