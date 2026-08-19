# HA/DR, Capacity & Production Reliability

## Scope
Enterprise Oracle environments with high-availability and disaster-recovery requirements, including RAC, ASM, Data Guard, RMAN and role-swap operations.

## Engineering focus
- Capacity planning
- Resilience
- DR readiness
- Incident response
- Production support
- Proactive configuration
- Secure authentication for privileged automation

## Vault authentication pattern
Privileged HA/DR and role-swap automation should authenticate to HashiCorp Vault before retrieving protected credentials. Use short-lived workload authentication, least-privilege policies and runtime secret retrieval. Credentials must not be embedded in scripts, source control, job parameters or logs.

## Portfolio note
Internal topology, recovery objectives and confidential operational data are intentionally omitted.
