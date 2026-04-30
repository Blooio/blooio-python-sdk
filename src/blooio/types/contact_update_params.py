# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ContactUpdateParams"]


class ContactUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """New display name (null to clear)"""
