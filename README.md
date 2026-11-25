# GLOBOO AI — Deterministic 6-Layer AI Execution & Treasury Firewall (`v3.9`)

[![Live Sandbox](https://shields.io)](https://globooai.com)
[![Architecture](https://shields.io)](https://globooai.com)
[![Latency](https://shields.io)](https://globooai.com)

Probabilistic LLM prompt filters cannot enforce hard financial invariants. When autonomous AI agents connect to **Stripe Payouts, SAP S/4HANA IDocs, Oracle NetSuite Bills, or QuickBooks**, a single prompt injection, Unicode homoglyph smuggling, or concurrent replay burst can move funds irreversibly.

**GLOBOO AI** sits inline inside your private VPC—validating every AI-initiated financial mutation across **6 deterministic pre-execution locks** before settlement.

> **Interactive Browser Sandbox & L5 CFO Quorum Console:** Test all 6 layers live without signup at **[https://globooai.com](https://globooai.com)**

---

## 6-Layer Deterministic Architecture

| Layer | Security Control | Deterministic Mechanism |
| :--- | :--- | :--- |
| **L1** | **Exact Decimal & Velocity Caps** | Single-tx & 24h cumulative limits with zero IEEE-754 float drift (`Redis Lua CAS` / `PostgreSQL SERIALIZABLE` / `SQLite WAL`). |
| **L2** | **IBAN & Beneficiary Allow-List** | ISO-13616 Mod-97 checksum validation + strict corporate beneficiary allow-listing. |
| **L3** | **Idempotency Replay Lock** | Cryptographic nonce & mutex enforcement against duplicate execution and TOCTOU race conditions. |
| **L4** | **Structural Canonicalization** | NFKC Unicode normalization, BiDi/control character stripping, and Shannon entropy payload inspection. |
| **L5** | **Asymmetric CFO Quorum Sign-Off** | Separates server HMAC keys from offline **Ed25519** executive keys + one-time `SETNX` Slack/WhatsApp/Email dispatch above `$10,000`. |
| **L6** | **Forensic Audit & Compliance Export** | Sequential `HMAC-SHA256` Merkle ledger with 1-click SOX/SOC2 verifiable audit dossier export. |

---

## Quickstart Integration (`v3.9`)

See [`quickstart_example.py`](./quickstart_example.py) for fail-closed ERP adapters (`guard_sap_idoc`, `guard_stripe_payout`, `guard_netsuite_bill`, `guard_quickbooks_payment`), one-time CFO webhook verification, and compliance reporting.

## 14-Day Read-Only Shadow Pilot & Private SDK Access
The core zero-dependency Python 3.9+ wheel (`globoo_shield_v3.py`) runs 100% inside your VPC with **zero data egress**.
* **Live Sandbox & L5 Quorum Demo:** [https://globooai.com](https://globooai.com)
* **Enterprise Pilot & Private Wheel:** [sales@globooai.com](mailto:sales@globooai.com)
* 
