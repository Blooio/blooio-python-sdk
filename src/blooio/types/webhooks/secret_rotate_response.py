# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SecretRotateResponse"]


class SecretRotateResponse(BaseModel):
    rotated_at: Optional[int] = None
    """Timestamp when the secret was rotated"""

    rotated_by: Optional[str] = None
    """Identifier of who rotated the secret"""

    rotation_count: Optional[int] = None
    """Total number of times this secret has been rotated"""

    signing_secret: Optional[str] = None
    """The new signing secret. Store this securely - it will not be shown again."""

    webhook_id: Optional[str] = None
