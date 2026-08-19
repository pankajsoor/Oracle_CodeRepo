# Oracle / PostgreSQL Modernization

## Scope
Enterprise database modernization and migration planning across Oracle and PostgreSQL platforms.

## Engineering focus
- Migration assessment and planning
- Compatibility and performance validation
- Cutover and rollback readiness
- Post-migration monitoring
- Production reliability
- Secure runtime authentication and secret retrieval through HashiCorp Vault

## Vault authentication pattern
Migration automation should authenticate to HashiCorp Vault before retrieving migration credentials, connection strings or other protected configuration. Prefer short-lived workload authentication (JWT/OIDC, AppRole or platform-native identity), least-privilege Vault policies, runtime secret retrieval and no secrets in Git, logs or pipeline artifacts.

## Outcome
The professional resume records database migrations up to 30 TB and experience with Oracle 19c to PostgreSQL 15 modernization.

## Portfolio note
Specific customer names, internal topology and proprietary implementation details are intentionally excluded.
