"""Reusable HashiCorp Vault authentication helper for the public portfolio.

This is a sanitized example and is not employer code.

Security model:
- Prefer a short-lived VAULT_TOKEN supplied by the CI/CD runner or workload identity.
- Never hard-code Vault tokens, AppRole secrets, passwords, or database credentials.
- A production deployment can replace the token bootstrap with AppRole, JWT/OIDC,
  Kubernetes auth, or another approved Vault auth method.
"""
import os
from typing import Dict


def vault_token() -> str:
    token = os.getenv("VAULT_TOKEN")
    if not token:
        raise RuntimeError("VAULT_TOKEN is not present; authenticate the workload before running automation")
    return token


def vault_headers() -> Dict[str, str]:
    return {"X-Vault-Token": vault_token()}


def vault_secret_path() -> str:
    return os.getenv("VAULT_SECRET_PATH", "secret/data/database/automation")


if __name__ == "__main__":
    print(f"Vault authentication prerequisite satisfied; secret path={vault_secret_path()}")
