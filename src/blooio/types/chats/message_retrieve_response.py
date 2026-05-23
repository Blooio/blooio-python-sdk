# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .reaction import Reaction
from ..._models import BaseModel

__all__ = ["MessageRetrieveResponse", "Contact"]


class Contact(BaseModel):
    contact_id: Optional[str] = None

    identifier: Optional[str] = None
    """The contact's phone number or email"""

    name: Optional[str] = None


class MessageRetrieveResponse(BaseModel):
    attachments: Optional[List[object]] = None

    chat_id: Optional[str] = None

    contact: Optional[Contact] = None

    direction: Optional[Literal["inbound", "outbound"]] = None

    error: Optional[str] = None

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
