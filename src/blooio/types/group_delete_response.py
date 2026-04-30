# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GroupDeleteResponse"]


class GroupDeleteResponse(BaseModel):
    deleted_at: Optional[int] = None

    success: Optional[bool] = None
