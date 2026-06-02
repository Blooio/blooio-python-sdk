# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pagination import Pagination
from .last_message import LastMessage

__all__ = ["ChatListResponse", "Chat", "ChatContact"]


class ChatContact(BaseModel):
    """Contact info (only for non-group chats)"""

    contact_id: Optional[str] = None

    identifier: Optional[str] = None

    name: Optional[str] = None


class Chat(BaseModel):
    id: Optional[str] = None
    """Chat identifier (phone number, email, or group ID)"""

    background_id: Optional[str] = None
    """Identifier for the active chat background"""

    background_url: Optional[str] = None
    """Public URL of the chat background image (if one has been set via the API)"""

    contact: Optional[ChatContact] = None
    """Contact info (only for non-group chats)"""

    group_id: Optional[str] = None
    """Group ID (only for group chats)"""

    group_name: Optional[str] = None
    """Group name (only for group chats)"""

    inbound_count: Optional[int] = None

    is_group: Optional[bool] = None
    """Whether this is a group chat"""

    last_inbound_time: Optional[int] = None

    last_message: Optional[LastMessage] = None

    last_message_time: Optional[int] = None

    last_outbound_time: Optional[int] = None

    member_count: Optional[int] = None
    """Number of members (only for group chats)"""

    message_count: Optional[int] = None

    outbound_count: Optional[int] = None

    type: Optional[Literal["phone", "email", "group"]] = None


class ChatListResponse(BaseModel):
    chats: Optional[List[Chat]] = None

    pagination: Optional[Pagination] = None
