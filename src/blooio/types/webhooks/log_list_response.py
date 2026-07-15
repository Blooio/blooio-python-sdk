# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "LogListResponse",
    "Log",
    "LogEventBody",
    "LogEventBodyAttachment",
    "LogEventBodyParticipant",
    "LogMetadata",
    "Pagination",
]


class LogEventBodyAttachment(BaseModel):
    name: Optional[str] = None

    url: Optional[str] = None


class LogEventBodyParticipant(BaseModel):
    contact_id: Optional[str] = None

    identifier: Optional[str] = None

    name: Optional[str] = None


class LogEventBody(BaseModel):
    """Webhook event payload.

    Structure varies by event type. All message events include group information when applicable.
    """

    attachments: Optional[List[LogEventBodyAttachment]] = None
    """Array of attachment objects"""

    delivered_at: Optional[int] = None
    """Timestamp when message was delivered (for message.delivered events)"""

    error_code: Optional[str] = None
    """Error code (for message.failed events)"""

    error_message: Optional[str] = None
    """Error description (for message.failed events)"""

    event: Optional[str] = None
    """
    Event type (e.g., message.received, message.sent, message.delivered,
    message.failed, message.read)
    """

    external_id: Optional[str] = None
    """Recipient identifier (phone number, email, or group ID)"""

    group_id: Optional[str] = None
    """Group ID (only present when is_group=true)"""

    group_name: Optional[str] = None
    """Group display name (only present when is_group=true)"""

    internal_id: Optional[str] = None
    """Phone number that sent/received the message"""

    is_group: Optional[bool] = None
    """Whether this message is from/to a group chat. Always present."""

    message_id: Optional[str] = None
    """Unique message identifier"""

    participants: Optional[List[LogEventBodyParticipant]] = None
    """Array of group participants (only present when is_group=true)"""

    protocol: Optional[Literal["pending", "unknown", "imessage", "sms", "rcs"]] = None
    """Transport used to carry the message; never null.

    `pending` = accepted and dispatched, wire service not resolved yet (settles
    within seconds of send); `imessage` = delivered over iMessage (blue bubble);
    `rcs` = delivered over RCS; `sms` = fell back to SMS/MMS (green bubble);
    `unknown` = accepted by the carrier but the wire service could not be resolved
    before the tracking window closed (see `error`).
    """

    read_at: Optional[int] = None
    """Timestamp when message was read (for message.read events)"""

    sender: Optional[str] = None
    """Sender identifier (for inbound messages)"""

    sent_at: Optional[int] = None
    """Timestamp when message was sent (for message.sent events)"""

    status: Optional[Literal["queued", "pending", "sent", "delivered", "failed", "read", "received"]] = None
    """Message status carried by the event.

    `queued` / `pending` = accepted, not yet handed off; `sent` = handed to
    Apple/the carrier; `delivered` = a delivery receipt was received; `read` = a
    read receipt was received (iMessage, when the recipient has read receipts on);
    `failed` = delivery failed (see `error_code` / `error_message`); `received` = an
    inbound message arrived.
    """

    text: Optional[str] = None
    """Message text content"""

    timestamp: Optional[int] = None
    """Event timestamp in milliseconds"""


class LogMetadata(BaseModel):
    """Additional metadata about the webhook delivery"""

    duration_ms: Optional[int] = None

    event_name: Optional[str] = None

    is_replay: Optional[bool] = None

    message_id: Optional[str] = None

    organization_id: Optional[str] = None

    original_event_id: Optional[str] = None


class Log(BaseModel):
    attempted_time: Optional[int] = None

    event_body: Optional[LogEventBody] = None
    """Webhook event payload.

    Structure varies by event type. All message events include group information
    when applicable.
    """

    event_id: Optional[str] = None

    metadata: Optional[LogMetadata] = None
    """Additional metadata about the webhook delivery"""

    response_json: Optional[object] = None
    """Response body from the webhook endpoint (if JSON)"""

    response_received_at: Optional[int] = None

    response_status: Optional[int] = None
    """HTTP status code received from the webhook endpoint"""

    scope: Optional[Literal["api", "integration", "org"]] = None

    webhook_url: Optional[str] = None


class Pagination(BaseModel):
    has_more: Optional[bool] = None
    """Whether there are more logs to fetch"""

    limit: Optional[int] = None

    offset: Optional[int] = None

    returned: Optional[int] = None
    """Number of logs returned in this response"""

    total: Optional[int] = None
    """Total number of matching logs"""


class LogListResponse(BaseModel):
    logs: Optional[List[Log]] = None

    pagination: Optional[Pagination] = None
