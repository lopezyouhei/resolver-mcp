from fastmcp import FastMCP

mcp = FastMCP("account-service")

ACCOUNTS = {
    "user_1001": {"status": "active", "flag_reason": None},
    "user_1002": {"status": "flagged", "flag_reason": "chargeback fraud pattern"},
}


@mcp.tool()
def get_account_status(account_id: str) -> dict:
    """Look up an account's status.

    Args:
        account_id (str): The account ID to look up.

    Returns:
        dict: The account's information, including status ("active" or "flagged") and flag reason.
              If the account is not found, returns "unknown" status.
    """
    acc = ACCOUNTS.get(account_id)
    if acc is None:
        return {"account_id": account_id, "status": "unknown", "flag_reason": None}
    return {
        "account_id": account_id,
        "status": acc["status"],
        "flag_reason": acc["flag_reason"],
    }


if __name__ == "__main__":
    mcp.run(show_banner=False)
