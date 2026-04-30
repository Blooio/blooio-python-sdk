# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .group import Group
from .._models import BaseModel

__all__ = ["GroupUpdateResponse", "GroupUpdateResponseDeviceSync"]


class GroupUpdateResponseDeviceSync(BaseModel):
    """Result of syncing the operation to a linked iMessage chat"""

    action: Optional[Literal["add_participant", "remove_participant", "leave"]] = None
    """The action that was performed for the linked chat"""

    chat_guid: Optional[str] = None
    """The linked iMessage chat GUID"""

    error: Optional[str] = None
    """Error message if sync failed"""

    synced: Optional[bool] = None
    """Whether the sync was successful"""


class GroupUpdateResponse(Group):
    device_sync: Optional[GroupUpdateResponseDeviceSync] = None
    """Result of syncing the operation to a linked iMessage chat"""
