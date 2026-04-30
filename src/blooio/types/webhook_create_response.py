# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    message: Optional[str] = None

    scope: Optional[Literal["api_key", "organization"]] = None

    webhook_id: Optional[str] = None

    webhook_url: Optional[str] = None
