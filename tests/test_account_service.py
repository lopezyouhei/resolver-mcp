from servers.account_service import get_account_status


def test_get_active_account():
    result = get_account_status("user_1001")
    assert result.get("status") == "active"


def test_get_flagged_account():
    result = get_account_status("user_1002")
    assert result.get("status") == "flagged"


def test_get_unknown_account():
    result = get_account_status("Lukas")
    assert result.get("status") == "unknown"
