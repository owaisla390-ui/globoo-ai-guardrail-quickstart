"""
GLOBOO AI (v3.9) — Enterprise VPC Integration Quickstart
Zero-egress deterministic 6-layer execution firewall for AI agents.

Note: Full zero-dependency Python 3.9+ engine (globoo_shield_v3.py) is distributed
via private wheel during your 14-Day Read-Only Shadow Pilot: https://globooai.com
"""

import os
from globoo_shield import GloboPolicyShield


class SecurityPolicyHold(Exception):
    """Raised when an AI-initiated payout violates a deterministic VPC policy lock."""
    def __init__(self, blocks: list, dispatch: dict | None = None):
        self.blocks = blocks
        self.dispatch = dispatch
        super().__init__(f"Blocked by GLOBOO 6-Layer Firewall: {blocks}")


def init_vpc_firewall(redis_cluster) -> GloboPolicyShield:
    return GloboPolicyShield(
        audit_hmac_key=os.environ["GLOBOO_AUDIT_HMAC_KEY"],
        cfo_public_key_pem=os.environ["GLOBOO_CFO_ED25519_PUB_PEM"],
        max_single_usd="50000.00",
        max_daily_usd="150000.00",
        quorum_threshold_usd="10000.00",
        allowed_ibans={"DE89370400440532013000", "GB29NWBK60161331926819"},
        redis_client=redis_cluster,  # Atomic Lua CAS + one-time SETNX decision lock
    )


def execute_protected_erp_workflow(shield: GloboPolicyShield, sap_idoc_payload: dict, cfo_sig: str = "") -> dict:
    # 1. Fail-closed ERP & Payment adapters (SAP, NetSuite, QuickBooks, Stripe)
    res = shield.guard_sap_idoc(sap_idoc_payload, quorum_sig_b64=cfo_sig)

    if res["verdict"] == "BLOCKED":
        # Auto-dispatches time-bound, one-time Approve/Reject links to CFO Slack/WhatsApp/Email
        raise SecurityPolicyHold(res["blocks"], dispatch=res.get("cfo_approval_dispatch"))

    return res


def handle_cfo_webhook_callback(shield: GloboPolicyShield, query_params: dict) -> dict:
    # 2. One-time atomic CFO webhook consumer (prevents link replay after Reject/Approve)
    return shield.consume_cfo_decision(
        tx_id=query_params["tx_id"],
        action=query_params["action"],  # "APPROVE" or "REJECT"
        exp=int(query_params["exp"]),
        token=query_params["token"],
    )


def generate_auditor_dossier(shield: GloboPolicyShield) -> dict:
    # 3. SOX / SOC2 external auditor tamper-proof ledger export
    return shield.export_compliance_report()
  
