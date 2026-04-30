# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TagListResponse", "Tag"]


class Tag(BaseModel):
    created_at: Optional[int] = None
    """Timestamp when the tag was added (ms since epoch)"""

    tag: Optional[str] = None
    """The tag value"""


class TagListResponse(BaseModel):
    tags: Optional[List[Tag]] = None
