# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GroupIcon", "DeviceSync"]


class DeviceSync(BaseModel):
    """Linked chat sync status"""

    chat_guid: Optional[str] = None

    message: Optional[str] = None
    """Status message about linked chat sync"""

    synced: Optional[bool] = None
    """Whether the icon change was synced to the linked iMessage chat.

    This will be true on successful set/remove operations.
    """


class GroupIcon(BaseModel):
    """Response for group icon operations"""

    chat_guid: Optional[str] = None
    """The BlueBubbles chat GUID"""

    device_sync: Optional[DeviceSync] = None
    """Linked chat sync status"""

    group_id: Optional[str] = None

    icon_url: Optional[str] = None
    """URL of the uploaded icon (only present on set)"""

    message: Optional[str] = None

    success: Optional[bool] = None
