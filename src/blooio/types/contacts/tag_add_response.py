# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TagAddResponse"]


class TagAddResponse(BaseModel):
    success: Optional[bool] = None

    tags_added: Optional[List[str]] = None
    """Tags that were added"""
