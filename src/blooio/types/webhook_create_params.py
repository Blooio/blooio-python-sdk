# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    webhook_url: Required[str]
    """URL of an existing webhook, for the idempotent 200 response.

    A URL that does not already exist returns 410.
    """

    valid_until: int
    """Ignored. Retained so existing request bodies stay valid."""
