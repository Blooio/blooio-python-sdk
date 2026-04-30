# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ContactCheckCapabilitiesResponse", "Capabilities"]


class Capabilities(BaseModel):
    facetime: Optional[bool] = None
    """Whether FaceTime is available"""

    imessage: Optional[bool] = None
    """Whether iMessage is available"""

    sms: Optional[bool] = None
    """Whether SMS is available (phone only)"""


class ContactCheckCapabilitiesResponse(BaseModel):
    capabilities: Optional[Capabilities] = None

    contact: Optional[str] = None
    """Normalized contact identifier"""

    last_checked: Optional[int] = None
    """Timestamp when capabilities were checked"""

    type: Optional[Literal["phone", "email"]] = None
