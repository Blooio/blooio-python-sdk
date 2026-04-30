# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MemberAddParams"]


class MemberAddParams(TypedDict, total=False):
    contact_id: Required[str]
    """Contact identifier (phone number or email)"""
