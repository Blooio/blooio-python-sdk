# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["GroupCreateParams"]


class GroupCreateParams(TypedDict, total=False):
    name: Required[str]
    """Group name (max 255 characters)"""

    chat_guid: str
    """BlueBubbles chat GUID to link this group to an existing iMessage chat.

    Use this to join groups created elsewhere. You can get this from the BlueBubbles
    API or from inbound message webhooks.
    """

    members: SequenceNotStr[str]
    """Phone numbers or emails of contacts in the group.

    When linking via chat_guid, this is for record-keeping only (members are not
    added to the linked iMessage chat).
    """
