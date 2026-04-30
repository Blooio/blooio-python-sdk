# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .contact import Contact
from .._models import BaseModel
from .pagination import Pagination

__all__ = ["ContactListResponse"]


class ContactListResponse(BaseModel):
    contacts: Optional[List[Contact]] = None

    pagination: Optional[Pagination] = None
