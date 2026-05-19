# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TypingResponse"]


class TypingResponse(BaseModel):
    chat_id: Optional[str] = None
    """Chat identifier"""

    started_at: Optional[int] = None
    """Timestamp when typing started (only for start)"""

    stopped_at: Optional[int] = None
    """Timestamp when typing stopped (only for stop)"""

    typing: Optional[bool] = None
    """Whether typing indicator is active"""

    warning: Optional[str] = None
    """Present when the request was accepted but the indicator could not be delivered.

    The most common reason is that the chat last routed via RCS, which does not
    carry composing state.
    """
