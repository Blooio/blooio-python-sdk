# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FacetimeInitiateCallResponse"]


class FacetimeInitiateCallResponse(BaseModel):
    handle: Optional[str] = None
    """The handle that was called"""

    link: Optional[str] = None
    """Shareable FaceTime link"""

    success: Optional[bool] = None
