# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MeRetrieveResponse", "Device", "Organization", "Usage"]


class Device(BaseModel):
    is_active: Optional[bool] = None

    last_active: Optional[int] = None

    phone_number: Optional[str] = None
    """Phone number assigned to this device (E.164 format)"""

    plan_kind: Optional[Literal["shared", "dedicated", "inbound", "trial", "2fa"]] = None
    """Plan type the underlying allocation runs on.

    `inbound` numbers are reply-only — see `/me/numbers` for details.
    """


class Organization(BaseModel):
    country_code: Optional[str] = None

    created_at: Optional[int] = None

    name: Optional[str] = None

    organization_id: Optional[str] = None


class Usage(BaseModel):
    """Usage statistics (only for api_key auth)"""

    inbound_messages: Optional[int] = None

    last_message_sent: Optional[int] = None

    outbound_messages: Optional[int] = None


class MeRetrieveResponse(BaseModel):
    """Response depends on auth_type.

    For 'api_key': includes full API key details. For 'dashboard': includes user_id and organization info only.
    """

    api_key: Optional[str] = None
    """The API key (only for api_key auth)"""

    auth_type: Optional[Literal["api_key", "dashboard"]] = None
    """Type of authentication used"""

    devices: Optional[List[Device]] = None
    """List of devices associated with this API key (only for api_key auth)"""

    integration_details: Optional[object] = None
    """
    Integration details if the API key is associated with an integration (only for
    api_key auth)
    """

    metadata: Optional[object] = None
    """API key metadata (only for api_key auth)"""

    organization: Optional[Organization] = None

    organization_id: Optional[str] = None
    """Organization ID (only for api_key auth)"""

    usage: Optional[Usage] = None
    """Usage statistics (only for api_key auth)"""

    user_id: Optional[str] = None
    """User ID (only for dashboard auth)"""

    valid: Optional[bool] = None
    """Whether the API key is valid (only for api_key auth)"""
