# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination import Pagination
from .group_member import GroupMember

__all__ = ["MemberListResponse"]


class MemberListResponse(BaseModel):
    group_id: Optional[str] = None
    """The group ID"""

    group_name: Optional[str] = None
    """The group name"""

    icon_url: Optional[str] = None
    """URL of the group icon/photo"""

    members: Optional[List[GroupMember]] = None

    pagination: Optional[Pagination] = None
