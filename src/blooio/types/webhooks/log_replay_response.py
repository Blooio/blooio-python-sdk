# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LogReplayResponse", "ResponseData"]


class ResponseData(BaseModel):
    """Response details from the replay attempt"""

    body: Optional[object] = None
    """Response body (if parseable)"""

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)

    duration: Optional[int] = None

    error: Optional[str] = None

    error_type: Optional[str] = FieldInfo(alias="errorType", default=None)

    headers: Optional[object] = None

    size: Optional[int] = None


class LogReplayResponse(BaseModel):
    duration_ms: Optional[int] = None
    """Time taken for the replay request in milliseconds"""

    original_event_id: Optional[str] = None
    """The original event ID that was replayed"""

    replay_event_id: Optional[str] = None
    """New event ID for this replay attempt"""

    response_data: Optional[ResponseData] = None
    """Response details from the replay attempt"""

    response_status: Optional[int] = None
    """HTTP status code from replay attempt"""

    success: Optional[bool] = None
    """Whether the replay received a 2xx response"""

    webhook_id: Optional[str] = None

    webhook_url: Optional[str] = None
