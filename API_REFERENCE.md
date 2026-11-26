# GLOBOO AI (`v3.9`) — Zero-Egress VPC API & SDK Reference

GLOBOO AI deploys locally inside your private VPC (`localhost:8443` or inline Python import) with **zero external network calls** and **~0.04ms median evaluation latency**.

---

## 1. Evaluate Outbound Payout (`POST /v1/guard/evaluate`)

### Request Payload
```json
{
  "tx_id": "tx_9948102a",
  "rail": "stripe_payout",
  "amount_usd": "24500.00",
  "beneficiary_iban": "DE89370400440532013000",
  "memo": "Q4 Cloud Infrastructure Settlement",
  "cfo_ed25519_signature": null
}
```

### Response — `202 QUORUM_REQUIRED` (Threshold Exceeded Without CFO Signature)
```json
{
  "verdict": "HOLD_FOR_QUORUM",
  "latency_ms": 0.038,
  "triggered_layers": ["L5_ED25519_CFO_QUORUM"],
  "quorum_ticket_id": "qrm_7f82a19c",
  "dispatched_channels": ["slack", "whatsapp", "email"],
  "merkle_audit_hash": "sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
}
```

### Response — `200 APPROVED` (All 6 Deterministic Locks Passed)
```json
{
  "verdict": "APPROVED",
  "latency_ms": 0.041,
  "triggered_layers": [],
  "merkle_audit_hash": "sha256:4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a"
}
```

---

## 2. Export SOX / SOC2 Forensic Audit Dossier (`GET /v1/audit/dossier?window=24h`)
Returns a cryptographically chained JSON/PDF compliance bundle verifying sequential `HMAC-SHA256` integrity across every evaluated transaction.

**Live Browser Sandbox (No Signup):** [https://globooai.com](https://globooai.com)  
**14-Day Read-Only Shadow Pilot:** [sales@globooai.com](mailto:sales@globooai.com)
