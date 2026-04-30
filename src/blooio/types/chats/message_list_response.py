# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .reaction import Reaction
from ..._models import BaseModel
from ..pagination import Pagination

__all__ = ["MessageListResponse", "Message"]


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
