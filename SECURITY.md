# Security Architecture & Threat Model — GLOBOO AI (`v3.9`)

## 1. Zero-Egress VPC Deployment Guarantee
GLOBOO AI is engineered as an air-gapped, zero-egress execution firewall (`globoo_shield_v3.py`) that executes 100% locally inside the customer's private VPC (AWS, GCP, Azure, or on-premise Kubernetes).
- **Zero Payload Telemetry:** No IBANs, invoice amounts, vendor names, or ERP records ever leave your infrastructure.
- **Zero External Runtime Dependencies:** Built on Python 3.9+ standard primitives (`decimal`, `hmac`, `hashlib`, `unicodedata`, `sqlite3`) with optional Redis Lua and PostgreSQL `SERIALIZABLE` connectors.

## 2. Cryptographic Key Separation (L5 CFO Quorum)
To eliminate single-point-of-compromise risks:
- **Execution Plane Key (`GLOBOO_AUDIT_HMAC_KEY`):** Used strictly for sequential `HMAC-SHA256` Merkle audit chaining and time-bound webhook tokens.
- **Approval Plane Key (`Ed25519` Offline Public/Private Keypair):** Held exclusively by authorized CFO/Controller signers. Even a full application server compromise cannot forge an L5 quorum approval for payouts exceeding `quorum_threshold_usd`.

## 3. Concurrency & Race-Condition Hardening
- **Redis Backend:** Executes cap checks and 24-hour rolling velocity increments inside a single atomic `EVAL` Lua script (`CAS`), preventing TOCTOU double-spend bursts.
- **PostgreSQL Backend:** Enforces `ISOLATION LEVEL SERIALIZABLE` with `SELECT ... FOR UPDATE` row locking.
- **Webhook Replay Protection:** One-time `SETNX` decision locks ensure every CFO `APPROVE` or `REJECT` link is single-use and strictly time-bound.

## 4. Responsible Disclosure
To report a security vulnerability or request our full SOC2 / ISO-27001 readiness packet, contact: **security@globooai.com**

