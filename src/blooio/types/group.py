# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    chat_guid: Optional[str] = None
    """BlueBubbles chat GUID if linked to a device group chat"""

    created_at: Optional[int] = None

    group_id: Optional[str] = None

    icon_url: Optional[str] = None
    """URL of the group icon/photo"""

    last_message_direction: Optional[Literal["inbound", "outbound"]] = None
    """Direction of the most recent message"""

    last_message_text: Optional[str] = None
    """Text of the most recent message in the group"""

    last_message_time: Optional[int] = None
    """Timestamp of the most recent message"""

    member_count: Optional[int] = None

    message_count: Optional[int] = None
    """Total number of messages in this group"""

    name: Optional[str] = None
    """Group name. Null for unnamed groups."""
