"""
GLOBOO AI (v3.9) — Local Attack & Policy Simulation Demo
Demonstrates how deterministic pre-execution locks block unauthorized AI payouts
before hitting Stripe, SAP, NetSuite, or QuickBooks.
"""

from decimal import Decimal

POLICY = {
    "max_single_usd": Decimal("50000.00"),
    "quorum_threshold_usd": Decimal("10000.00"),
    "allowed_ibans": {"DE89370400440532013000", "GB29NWBK60161331926819"},
}


def simulate_firewall(tx_id: str, amount_str: str, iban: str, has_cfo_ed25519_sig: bool = False) -> dict:
    amount = Decimal(amount_str)
    blocks = []

    if amount > POLICY["max_single_usd"]:
        blocks.append("L1_SINGLE_TX_CAP_EXCEEDED")
    if iban not in POLICY["allowed_ibans"]:
        blocks.append("L2_UNVERIFIED_BENEFICIARY_IBAN")
    if amount > POLICY["quorum_threshold_usd"] and not has_cfo_ed25519_sig:
        blocks.append("L5_MISSING_ED25519_CFO_QUORUM_SIG")

    return {
        "tx_id": tx_id,
        "amount_usd": str(amount),
        "verdict": "BLOCKED" if blocks else "APPROVED",
        "blocks": blocks,
    }


if __name__ == "__main__":
    print("1. Normal Payout ($9,500):", simulate_firewall("tx_101", "9500.00", "DE89370400440532013000"))
    print("2. Prompt-Injected IBAN ($42,500):", simulate_firewall("tx_102", "42500.00", "RU02044525600407028104"))
    print("3. Over-Threshold Without CFO Sig ($25,000):", simulate_firewall("tx_103", "25000.00", "DE89370400440532013000", False))
    print("4. Over-Threshold WITH Ed25519 CFO Sig ($25,000):", simulate_firewall("tx_104", "25000.00", "DE89370400440532013000", True))
  
