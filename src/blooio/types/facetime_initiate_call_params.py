# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FacetimeInitiateCallParams"]


class FacetimeInitiateCallParams(TypedDict, total=False):
    handle: Required[str]
    """Phone number (E.164) or email address to call"""
