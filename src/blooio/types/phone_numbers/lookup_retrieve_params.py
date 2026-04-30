# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LookupRetrieveParams"]


class LookupRetrieveParams(TypedDict, total=False):
    number: Required[str]
    """Phone number to look up.

    Can be E.164 format (+12125551234), national format (2125551234), or with
    formatting ((212) 555-1234).
    """
