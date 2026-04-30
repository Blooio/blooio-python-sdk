# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .group import Group
from .._models import BaseModel
from .pagination import Pagination

__all__ = ["GroupListResponse"]


class GroupListResponse(BaseModel):
    groups: Optional[List[Group]] = None

    pagination: Optional[Pagination] = None
