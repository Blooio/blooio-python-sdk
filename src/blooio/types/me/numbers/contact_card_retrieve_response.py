# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ContactCardRetrieveResponse", "Sharing"]


class Sharing(BaseModel):
    audience: Optional[int] = None
    """0 = Contacts Only, 1 = Always Ask"""

    enabled: Optional[bool] = None
    """Whether Name & Photo sharing is enabled"""

    name_format: Optional[int] = None
    """0 = First & Last, 1 = First Only"""


class ContactCardRetrieveResponse(BaseModel):
    avatar: Optional[str] = None
    """Base64-encoded JPEG/PNG image"""

    first_name: Optional[str] = None

    has_wallpaper: Optional[bool] = None

    last_name: Optional[str] = None

    name: Optional[str] = None
    """Display name"""

    phone_number: Optional[str] = None

    sharing: Optional[Sharing] = None
