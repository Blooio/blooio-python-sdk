# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContactCreateParams"]


class ContactCreateParams(TypedDict, total=False):
    identifier: Required[str]
    """Phone number (E.164 format, e.g., +15551234567) or email address"""

    name: str
    """Display name for the contact"""
