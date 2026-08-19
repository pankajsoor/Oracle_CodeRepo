# Pankaj Soor — Oracle & Database Engineering Portfolio

**Principal Database Engineer | Lead Oracle DBA | Database SRE**

15+ years of enterprise database engineering across banking, financial-services and telecom environments.

## Professional focus

- Oracle 10g / 11g / 12c / 19c
- PostgreSQL 15
- Oracle RAC, ASM, Data Guard, RMAN, GoldenGate, Exadata
- Database modernization and migrations
- Python, Terraform, Ansible, Jenkins, GitHub Actions, Rundeck
- **HashiCorp Vault authentication and runtime secret management**
- AWS; GCP working knowledge
- Grafana, Geneos, OEM, AWR/ASH/ADDM
- High availability, disaster recovery, capacity planning and SRE-aligned production reliability

## Selected impact

- 100+ banking applications supported within Global Payments Services
- Approximately 60% Tier-0 systems
- 200+ production servers in the external-resume baseline
- Oracle environments exceeding 30 TB in the external-resume baseline
- Largest migration led: 30 TB
- Approximately 90% of BAU database operations automated
- Annual Pat on the Back / Star Performance recognition for the last six years

## Portfolio case studies

1. [Database BAU Automation](projects/01-database-bau-automation/README.md)
2. [Oracle / PostgreSQL Modernization](projects/02-oracle-postgresql-modernization/README.md)
3. [Oracle Upgrade Program](projects/03-oracle-upgrade-program/README.md)
4. [HA/DR, Capacity & Reliability](projects/04-ha-dr-capacity-reliability/README.md)
5. [Database Observability & Performance](projects/05-database-observability-performance/README.md)
6. [Database DevOps Platform](projects/06-database-devops-platform/README.md)

## Security pattern across all automation

HashiCorp Vault is treated as a common security boundary. Automation authenticates to Vault before protected secret access, prefers short-lived workload authentication such as JWT/OIDC, AppRole or platform-native identity, applies least-privilege policies, retrieves secrets at runtime, and keeps credentials out of Git, logs and artifacts.

A reusable sanitized helper is available at `automation/vault_auth.py`.

## Important note

This is a sanitized professional portfolio. It contains no employer-owned source code, credentials, internal hostnames, customer data, confidential diagrams, proprietary runbooks or other restricted information. Examples describe engineering patterns and responsibilities and are not reproductions of employer implementation code.

## Target roles

Principal Database Engineer • Lead Oracle DBA • Database Architect • Database SRE • Cloud Database Architect
