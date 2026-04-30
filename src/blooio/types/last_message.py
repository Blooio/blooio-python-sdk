# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LastMessage"]


class LastMessage(BaseModel):
    direction: Optional[Literal["inbound", "outbound"]] = None

    message_id: Optional[str] = None

    text: Optional[str] = None

    time_sent: Optional[int] = None
