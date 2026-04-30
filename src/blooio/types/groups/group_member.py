# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GroupMember"]


class GroupMember(BaseModel):
    id: Optional[str] = None
    """Contact identifier (phone or email)"""

    added_at: Optional[int] = None

    contact_id: Optional[str] = None

    identifier: Optional[str] = None

    name: Optional[str] = None
