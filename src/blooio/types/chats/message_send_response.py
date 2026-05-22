# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MessageSendResponse"]


class MessageSendResponse(BaseModel):
    """Response after sending a message"""

    count: Optional[int] = None
    """Number of messages sent. Only present in URL-balloon batch mode."""

    group_created: Optional[bool] = None
    """True if a new unnamed group was created for this multi-recipient message"""

    group_id: Optional[str] = None
    """Group ID when sending to multi-recipient (new or existing)"""

    message_id: Optional[str] = None
    """ID of the sent message (single-message sends)"""

    message_ids: Optional[List[str]] = None
    """IDs of sent messages.

    Present when `text` is an array or when `parts` uses per-part `link_preview`
    (URL-balloon batch mode).
    """

    parent_unresolved: Optional[bool] = None
    """
    Present (and `true`) only when `reply_to.guid` was supplied without a
    `message_id` and the GUID didn't map to any Blooio-minted row. The send still
    proceeds and the device may still thread it; this flag signals that Blooio
    couldn't link the new message to a known parent.
    """

    participants: Optional[List[str]] = None
    """List of participants (present for multi-recipient)"""

    status: Optional[Literal["queued", "failed"]] = None
    """Initial status of the message(s)"""
