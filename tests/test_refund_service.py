from fastmcp import Client

from servers.refund_service import mcp as refund_server
from servers.refund_service import process_refund

AMOUNT = 12.99


def test_process_active_account():
    result = process_refund("user_1001", AMOUNT)
    assert result.get("refund_status") == "refund"
    assert isinstance(result.get("amount"), float)
    assert result.get("amount") == AMOUNT


def test_process_flagged_account():
    result = process_refund("user_1002", amount=AMOUNT)
    assert result.get("refund_status") == "refuse"
    assert result.get("amount") is None
    assert isinstance(result.get("reason"), str)
    assert "flag" in result.get("reason").lower()


def test_process_unknown_account():
    result = process_refund("Lukas", amount=AMOUNT)
    assert result.get("refund_status") == "refuse"
    assert result.get("amount") is None
    assert isinstance(result.get("reason"), str)
    assert "verif" in result.get("reason").lower()


async def test_process_refund_mcp():
    async with Client(refund_server) as client:
        result = await client.call_tool(
            "process_refund", {"account_id": "user_1001", "amount": AMOUNT}
        )
        assert result.data["refund_status"] == "refund"
