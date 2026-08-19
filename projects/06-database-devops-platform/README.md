# Database DevOps Platform

## Objective
Create a repeatable engineering platform around database operations rather than relying on manual DBA execution.

## Technology
Python • Terraform • Ansible • Jenkins • GitHub Actions • Rundeck • **HashiCorp Vault**

## Vault authentication standard
HashiCorp Vault is treated as a common security layer across the automation platform:
- Authenticate the workload before secret access.
- Prefer short-lived JWT/OIDC, AppRole or platform-native workload identity over static tokens.
- Retrieve database credentials and protected configuration at runtime.
- Apply least-privilege Vault policies per automation/job.
- Redact secrets from console output and logs.
- Never commit credentials, Vault tokens or secret values to Git.

A reusable sanitized helper is available at `automation/vault_auth.py`.

## Engineering principles
- Infrastructure/configuration as code
- Repeatable workflows
- Controlled changes
- Vault-authenticated secret management
- Automation-first operations
- Least privilege
- Mentoring and adoption across engineering/application teams

## Outcome
The professional material records approximately 90% BAU automation and monthly mentoring sessions for database and application teams.

## Portfolio note
No employer-owned implementation code is included.
