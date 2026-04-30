# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageGetStatusResponse"]


class MessageGetStatusResponse(BaseModel):
    chat_id: Optional[str] = None

    direction: Optional[Literal["inbound", "outbound"]] = None

    error: Optional[str] = None

    message_id: Optional[str] = None

    protocol: Optional[Literal["imessage", "sms", "rcs", "non-imessage"]] = None

    status: Optional[
        Literal["pending", "queued", "sent", "delivered", "failed", "cancellation_requested", "cancelled"]
    ] = None

    time_delivered: Optional[int] = None

    time_sent: Optional[int] = None
