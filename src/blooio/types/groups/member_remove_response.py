# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MemberRemoveResponse"]


class MemberRemoveResponse(BaseModel):
    removed_at: Optional[int] = None

    success: Optional[bool] = None
