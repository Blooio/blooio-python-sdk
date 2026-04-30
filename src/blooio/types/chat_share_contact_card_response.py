# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ChatShareContactCardResponse"]


class ChatShareContactCardResponse(BaseModel):
    chat_id: Optional[str] = None
    """Normalized chat identifier"""

    message: Optional[str] = None

    success: Optional[bool] = None
