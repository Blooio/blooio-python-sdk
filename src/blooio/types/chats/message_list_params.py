# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    direction: Literal["inbound", "outbound"]
    """Filter by message direction"""

    limit: int
    """Maximum number of items to return (1-200)"""

    offset: int
    """Number of items to skip"""

    since: int
    """Only messages sent after this timestamp (ms)"""

    sort: Literal["asc", "desc"]
    """Sort order by time"""

    until: int
    """Only messages sent before this timestamp (ms)"""
