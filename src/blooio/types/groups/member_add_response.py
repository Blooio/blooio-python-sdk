# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .group_member import GroupMember

__all__ = ["MemberAddResponse"]


class MemberAddResponse(BaseModel):
    member: Optional[GroupMember] = None

    message: Optional[str] = None
