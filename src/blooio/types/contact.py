# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Contact"]


class Contact(BaseModel):
    id: Optional[str] = None
    """Contact identifier (phone or email)"""

    contact_id: Optional[str] = None
    """Internal contact ID"""

    created_at: Optional[int] = None

    identifier: Optional[str] = None
    """Phone number (E.164) or email"""

    last_message_time: Optional[int] = None

    name: Optional[str] = None

    tags: Optional[List[str]] = None

    type: Optional[Literal["phone", "email"]] = None
