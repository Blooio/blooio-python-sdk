# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ContactLocation"]


class ContactLocation(BaseModel):
    coordinates: Optional[List[float]] = None
    """GPS coordinates [latitude, longitude]"""

    handle: Optional[str] = None
    """Contact's phone number or email"""

    last_updated: Optional[int] = None
    """Timestamp of last location update (epoch ms)"""

    status: Optional[str] = None
    """Location status (e.g., 'live', 'shallow', 'legacy')"""
