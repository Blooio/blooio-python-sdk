# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    deprecate: bool
    """Set to true to deprecate, false to undeprecate"""

    valid_until: int
    """Expiration timestamp. Use -1 or null for no expiration."""

    webhook_type: Literal["message", "status", "all"]
    """Type of events to receive"""
