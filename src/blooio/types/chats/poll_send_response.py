# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PollSendResponse", "Poll"]


class Poll(BaseModel):
    options: Optional[List[str]] = None

    title: Optional[str] = None


class PollSendResponse(BaseModel):
    chat_id: Optional[str] = None

    poll: Optional[Poll] = None

    poll_id: Optional[str] = None
    """Unique identifier for the poll"""

    sent_at: Optional[float] = None
