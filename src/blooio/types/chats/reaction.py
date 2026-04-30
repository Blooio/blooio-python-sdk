# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Reaction"]


class Reaction(BaseModel):
    is_added: Optional[bool] = None
    """Whether the reaction is currently active (true) or was removed (false)"""

    reaction: Optional[str] = None
    """The reaction value.

    Classic tapbacks: love, like, dislike, laugh, emphasize, question. Emoji
    reactions: the emoji character (e.g. 😂, 👍).
    """

    sender: Optional[str] = None
    """Phone number or email of who sent the reaction.

    Null when the reaction was sent by you (outbound).
    """

    time_sent: Optional[int] = None
    """Timestamp when the reaction was sent (ms)"""
