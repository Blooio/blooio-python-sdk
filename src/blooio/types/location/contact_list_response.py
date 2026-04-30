# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .contact_location import ContactLocation

__all__ = ["ContactListResponse"]


class ContactListResponse(BaseModel):
    friends: Optional[List[ContactLocation]] = None
