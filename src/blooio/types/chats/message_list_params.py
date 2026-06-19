# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    direction: Literal["inbound", "outbound"]
    """Filter by message direction"""

    limit: int
    """Maximum number of items to return in a single response.

    Must be between 1 and 200; defaults to 50. Use together with `offset` to page
    through large result sets.
    """

    offset: int
    """Number of items to skip before returning results.

    Combine with `limit` for page-based pagination (e.g. `offset=50&limit=50`
    returns the second page). Defaults to 0.
    """

    since: int
    """Only messages sent after this timestamp (ms)"""

    sort: Literal["asc", "desc"]
    """Sort order by time"""

    until: int
    """Only messages sent before this timestamp (ms)"""
