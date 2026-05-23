# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ChatBackgroundResponse"]


class ChatBackgroundResponse(BaseModel):
    """Response for chat background operations"""

    background_id: Optional[str] = None
    """Unique identifier for the current background, or null if none"""

    background_url: Optional[str] = None
    """Public URL of the persisted background image stored in R2.

    Returned after a successful PUT and on GET when a background has been set
    through the API. May be null if persistence failed or the background was set
    outside of the API.
    """

    background_version: Optional[int] = None
    """Version number of the background (for cache invalidation)"""

    changed: Optional[bool] = None
    """Whether the background was changed by this operation (only present on PUT)"""

    chat_id: Optional[str] = None
    """Normalized chat identifier (phone number, email, or group ID)"""

    has_background: Optional[bool] = None
    """Whether the chat currently has a background set"""
