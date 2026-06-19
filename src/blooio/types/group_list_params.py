# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GroupListParams"]


class GroupListParams(TypedDict, total=False):
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

    q: str
    """Search query (matches group name)"""

    sort: Literal["recent", "oldest", "name_asc", "name_desc"]
    """Sort order"""
