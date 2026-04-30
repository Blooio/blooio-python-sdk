# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ContactCardUpdateResponse"]


class ContactCardUpdateResponse(BaseModel):
    first_name: Optional[str] = None

    last_name: Optional[str] = None

    phone_number: Optional[str] = None

    success: Optional[bool] = None
