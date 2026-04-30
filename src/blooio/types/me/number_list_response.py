# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["NumberListResponse", "Number"]


class Number(BaseModel):
    is_active: Optional[bool] = None

    last_active: Optional[datetime] = None

    phone_number: Optional[str] = None


class NumberListResponse(BaseModel):
    numbers: Optional[List[Number]] = None
