# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    webhook_url: Required[str]
    """URL to receive webhook events"""

    valid_until: int
    """Expiration timestamp (-1 for no expiration)"""

    webhook_type: Literal["message", "status", "all"]
    """Type of events to receive"""
