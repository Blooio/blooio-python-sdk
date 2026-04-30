# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageReactResponse"]


class MessageReactResponse(BaseModel):
    action: Optional[Literal["add", "remove"]] = None
    """The action that was performed"""

    message_id: Optional[str] = None
    """The ID of the message that was reacted to"""

    reaction: Optional[str] = None
    """The reaction that was added or removed.

    For classic tapbacks: love, like, dislike, laugh, emphasize, question. For emoji
    reactions: the emoji character (e.g. 😂, 👍, 🔥).
    """

    success: Optional[bool] = None
    """Whether the reaction was sent successfully"""
