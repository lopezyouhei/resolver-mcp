from fastmcp import FastMCP

mcp = FastMCP("refund-service")

ACCOUNTS = {"user_1001": {"status": "active"}, "user_1002": {"status": "flagged"}}


@mcp.tool()
def process_refund(account_id: str, amount: float) -> dict:
    """Issues a refund only if this service independently agrees that it's safe.

    Args:
        account_id (str): User's account ID.
        amount (float): Requested refund amount.

    Returns:
        dict: The refund status ("refund" or "refuse"), and the amount if refund or reason if refuse.
    """

    acc = ACCOUNTS.get(account_id)
    if acc is None:  # account
        return {
            "refund_status": "refuse",
            "reason": f"Account {account_id} could not be verified.",
        }

    if acc.get("status") == "active":
        return {"refund_status": "refund", "amount": amount}
    if acc.get("status") == "flagged":
        return {
            "refund_status": "refuse",
            "reason": f"Account {account_id} is flagged for suspicious activity: human review required.",
        }

    # Catch-all for now: any
    return {
        "refund_status": "refuse",
        "reason": f"Account {account_id} is not in good standing - refusing.",
    }
