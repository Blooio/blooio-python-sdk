# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    api_key_name: Optional[str] = None
    """Name of the API key (if scope is api_key)"""

    created_at: Optional[int] = None

    deprecated_at: Optional[int] = None

    failure_count: Optional[int] = None

    integration_name: Optional[str] = None
    """Name of the integration (if scope is integration)"""

    is_active: Optional[bool] = None
    """Whether the webhook is active (not deprecated)"""

    last_triggered: Optional[int] = None

    scope: Optional[Literal["api_key", "organization", "integration"]] = None

    valid_until: Optional[int] = None
    """-1 means no expiration"""

    webhook_id: Optional[str] = None

    webhook_type: Optional[Literal["message", "status", "all"]] = None

    webhook_url: Optional[str] = None
