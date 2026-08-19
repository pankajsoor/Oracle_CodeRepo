# Database BAU Automation

## Problem
Repetitive database operations such as patching, monitoring-agent upgrades, maintenance/restart workflows and role swaps create operational effort and execution variance.

## Engineering approach
Build repeatable workflows using Python, Terraform, Ansible, Jenkins, GitHub Actions and Rundeck, with **HashiCorp Vault authentication and secret retrieval** as a security boundary.

## Vault authentication pattern
- Automation authenticates to Vault before accessing protected secrets.
- Prefer short-lived workload credentials such as JWT/OIDC, AppRole or platform-native workload identity rather than long-lived static credentials.
- Database credentials, API tokens and other secrets are retrieved at runtime and are never committed to Git.
- CI/CD and job runners receive only the minimum Vault permissions required for the workflow.
- Secrets are not written to logs, source files or generated artifacts.

## Scope
- PSU patching
- OEM agent upgrades
- Maintenance/restart workflows
- Database role swaps
- Repeatable operational execution
- Automation-led change control
- Vault-authenticated secret retrieval

## Outcome
The professional resume states that approximately 90% of BAU database operations were automated.

## Portfolio note
Sanitized case study. No employer-owned scripts, credentials, hostnames or proprietary configuration are included.
