# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ChatListParams"]


class ChatListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return (1-200)"""

    offset: int
    """Number of items to skip"""

    q: str
    """Search query (matches phone/email or contact name)"""

    sort: Literal["recent", "oldest"]
    """Sort order"""
