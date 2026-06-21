from servers.refund_service import process_refund

AMOUNT = 12.99


def test_process_active_account():
    result = process_refund("user_1001", AMOUNT)
    assert result.get("refund_status") == "refunded"
    assert type(result.get("amount")) is float


def test_process_flagged_account():
    pass


def test_process_unknown_account():
    pass
