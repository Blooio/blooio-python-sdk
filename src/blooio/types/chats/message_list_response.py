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

    internal_id: Optional[str] = None
    """Organization phone number (from-number) used for this message"""

    message_id: Optional[str] = None

    protocol: Optional[Literal["imessage", "sms", "rcs", "non-imessage"]] = None

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

    text: Optional[str] = None

    time_delivered: Optional[int] = None

    time_sent: Optional[int] = None


class MessageListResponse(BaseModel):
    chat_id: Optional[str] = None

    messages: Optional[List[Message]] = None

    pagination: Optional[Pagination] = None
