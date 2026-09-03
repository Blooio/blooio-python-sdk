# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .reaction import Reaction
from ..._models import BaseModel
from ..pagination import Pagination

__all__ = ["MessageListResponse", "Message", "MessageReplyTo"]


class MessageReplyTo(BaseModel):
    """Inline-reply parent reference.

    Identical shape on `message.received` webhooks and on every GET endpoint that returns a single message or a list of messages.
    """

    guid: Optional[str] = None
    """The raw iMessage GUID of the parent.

    Always populated on real inline replies; the on-device record-of-truth
    identifier that survives even when `message_id` cannot be resolved.
    """

    message_id: Optional[str] = None
    """The Blooio `message_id` of the parent message.

    NULL when the parent isn't in our `messages` table (e.g., the original was sent
    from outside Blooio's pipeline).
    """

    part_index: int
    """Which part of the parent was replied to. 0 for the common single-part case."""


class Message(BaseModel):
    attachments: Optional[List[object]] = None

    direction: Optional[Literal["inbound", "outbound"]] = None

    error: Optional[str] = None

    external_id: Optional[str] = None
    """Phone number or email of the contact, or group ID for group messages"""

    formatted_text: Optional[str] = None
    """Markdown for a rich-text (bold/italic/underline/strikethrough) message.

    Omitted entirely when the message carries no styling, so its presence is how you
    detect rich text.

    Present in both directions: on an outbound send made with `format: "markdown"`,
    and on an inbound iMessage whose sender styled their text — so styling a
    customer applied in Messages arrives here even though your integration never
    asked for it.

    Always a normalized re-serialization of the message's actual styling rather than
    an echo of the source string: bold is spelled `**`, italic `*`, underline `++`,
    strikethrough `~~`, and any character that would otherwise read as a delimiter
    is backslash-escaped. Re-sending this value verbatim with `format: "markdown"`
    reproduces the same styled message. Blooio iMessage only. This is the SAME field
    delivered on the message webhooks, so a message reads identically via REST or
    webhook.
    """

    internal_id: Optional[str] = None
    """Organization phone number (from-number) used for this message"""

    message_id: Optional[str] = None

    protocol: Optional[Literal["pending", "unknown", "imessage", "sms", "rcs"]] = None
    """Transport used to carry the message; never null.

    `pending` = accepted and dispatched, wire service not resolved yet (settles
    within seconds of send); `imessage` = delivered over iMessage (blue bubble);
    `rcs` = delivered over RCS; `sms` = fell back to SMS/MMS (green bubble);
    `unknown` = accepted by the carrier but the wire service could not be resolved
    before the tracking window closed (see `error`).
    """

    reactions: Optional[List[Reaction]] = None
    """Reactions on this message (tapbacks and emoji reactions)"""

    reply_to: Optional[MessageReplyTo] = None
    """Inline-reply parent reference.

    Identical shape on `message.received` webhooks and on every GET endpoint that
    returns a single message or a list of messages.
    """

    sender: Optional[str] = None
    """Sender's phone number or email for inbound group messages.

    Null for outbound messages and 1-1 chats.
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

    text: Optional[str] = None

    time_delivered: Optional[int] = None

    time_sent: Optional[int] = None


class MessageListResponse(BaseModel):
    chat_id: Optional[str] = None

    messages: Optional[List[Message]] = None

    pagination: Optional[Pagination] = None
