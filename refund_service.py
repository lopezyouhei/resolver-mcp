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
        dict: The refund status ("refunded" or "refused") and the reason if
    """
    acc = ACCOUNTS.get(account_id)

    return {}
