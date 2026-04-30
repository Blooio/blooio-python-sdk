# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LogListParams"]


class LogListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return (1-200)"""

    max_status: int
    """Maximum HTTP status code"""

    min_status: int
    """Minimum HTTP status code"""

    offset: int
    """Number of items to skip"""

    sort: Literal["asc", "desc"]
    """Sort order by attempted time"""

    status: int
    """Filter by exact HTTP status code"""
