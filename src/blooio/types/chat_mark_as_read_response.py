# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChatMarkAsReadResponse"]


class ChatMarkAsReadResponse(BaseModel):
    chat_id: Optional[str] = None
    """Chat identifier"""

    marked_at: Optional[int] = None
    """Timestamp when marked as read"""

    status: Optional[Literal["read"]] = None
    """Read status"""
