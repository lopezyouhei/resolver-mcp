from typing import (
    Literal,
    Optional,
    TypedDict,
)


# default for langgraph, otherwise Pydantic would be a good choice
class ResolverState(TypedDict, total=False):
    request_text: str
    account_id: str
    amount: float  # simplification for prototype

    # facts from account service
    account_status: Optional[Literal["active", "flagged", "unknown"]]
    flag_reason: Optional[str]

    # decision made in policy
    decision: Optional[Literal["refund", "refuse"]]
    policy_reason: Optional[str]

    # outputs
    refund_result: Optional[dict]
    customer_message: Optional[str]
    audit_record: Optional[dict]
