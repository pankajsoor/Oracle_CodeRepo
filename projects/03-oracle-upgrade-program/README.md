# Oracle Upgrade Program

## Scope
Oracle upgrade programs covering 11g to 12c and 11g/12c to 19c.

## Engineering focus
- Upgrade planning and sequencing
- Pre/post validation
- Production coordination
- Application and infrastructure dependency management
- Reliability and rollback readiness
- Secure runtime authentication and secret retrieval through HashiCorp Vault

## Vault authentication pattern
Upgrade automation authenticates to HashiCorp Vault before retrieving privileged database credentials or protected configuration. Use short-lived workload authentication where possible, least-privilege policies, runtime retrieval and secret redaction. Never hard-code credentials or commit them to Git.

## What this demonstrates
Deep Oracle lifecycle expertise combined with production engineering discipline and secure automation practices.
