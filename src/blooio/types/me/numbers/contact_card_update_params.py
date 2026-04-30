# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ContactCardUpdateParams", "Sharing"]


class ContactCardUpdateParams(TypedDict, total=False):
    avatar: str
    """Profile photo as base64-encoded JPEG/PNG"""

    first_name: str
    """First name"""

    last_name: str
    """Last name"""

    sharing: Sharing


class Sharing(TypedDict, total=False):
    audience: int
    """0 = Contacts Only, 1 = Always Ask"""

    enabled: bool
    """Enable/disable Name & Photo sharing"""

    name_format: int
    """0 = First & Last, 1 = First Only"""
