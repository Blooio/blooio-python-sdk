# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PollGetResultsResponse", "Option"]


class Option(BaseModel):
    text: Optional[str] = None

    votes: Optional[int] = None


class PollGetResultsResponse(BaseModel):
    chat_id: Optional[str] = None

    options: Optional[List[Option]] = None

    poll_id: Optional[str] = None

    title: Optional[str] = None

    total_votes: Optional[int] = None
