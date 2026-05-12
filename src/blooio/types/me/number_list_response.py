# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NumberListResponse", "Number"]


class Number(BaseModel):
    is_active: Optional[bool] = None

    last_active: Optional[datetime] = None

    phone_number: Optional[str] = None

    plan_kind: Optional[Literal["shared", "dedicated", "inbound", "trial", "2fa"]] = None
    """Plan type the underlying allocation runs on.

    Sourced directly from `allocation_pool.type` — the enum mirrors the DB `CHECK`
    constraint (see migration 2026-05-09-inbound-plan.sql), so any value here is
    also a valid type stored in the database. `inbound` numbers are reply-only —
    outbound to a recipient (a contact for 1:1 chats, the group for group chats)
    requires that recipient to have messaged the number first (otherwise the send
    returns `403 inbound_only_no_prior_inbound`). `null` indicates the underlying
    allocation predates the type column or is unattributed; clients should treat
    `null` the same as `dedicated` for routing decisions.
    """


class NumberListResponse(BaseModel):
    numbers: Optional[List[Number]] = None
