from fastmcp import Client

from servers.account_service import get_account_status
from servers.account_service import mcp as account_status_server


def test_get_active_account():
    result = get_account_status("user_1001")
    assert result.get("status") == "active"


def test_get_flagged_account():
    result = get_account_status("user_1002")
    assert result.get("status") == "flagged"


def test_get_unknown_account():
    result = get_account_status("Lukas")
    assert result.get("status") == "unknown"


async def test_get_account_status_mcp():
    async with Client(account_status_server) as client:
        result = await client.call_tool(
            "get_account_status", {"account_id": "user_1001"}
        )
        assert result.data["status"] == "active"
