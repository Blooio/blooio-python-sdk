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

    protocol: Optional[Literal["pending", "unknown", "imessage", "sms", "rcs"]] = None
    """Transport used to carry the message; never null.

    `pending` = accepted and dispatched, wire service not resolved yet (settles
    within seconds of send); `imessage` = delivered over iMessage (blue bubble);
    `rcs` = delivered over RCS; `sms` = fell back to SMS/MMS (green bubble);
    `unknown` = accepted by the carrier but the wire service could not be resolved
    before the tracking window closed (see `error`).
    """

    status: Optional[
        Literal["pending", "queued", "sent", "delivered", "failed", "cancellation_requested", "cancelled"]
    ] = None
    """Delivery lifecycle state.

    `pending` = persisted and being prepared for dispatch; `queued` = accepted and
    waiting to be handed to Apple/the carrier; `sent` = handed off to Apple/the
    carrier (protocol resolution happens around here); `delivered` = a delivery
    receipt was received; `failed` = could not be delivered (see `error`);
    `cancellation_requested` = a cancel was requested for a still-queued message
    (best-effort); `cancelled` = cancelled before dispatch. Inbound messages are
    surfaced via webhooks with `received`; read receipts arrive as a `read` event.
    """

    time_delivered: Optional[int] = None

    time_sent: Optional[int] = None
