# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PhoneNumberLookupResult", "Location"]


class Location(BaseModel):
    """NANPA geocoding location (only for North American numbers with country code 1)"""

    city: Optional[str] = None
    """City name"""

    region: Optional[str] = None
    """State/province abbreviation"""

    region_name: Optional[str] = None
    """Full state/province name"""


class PhoneNumberLookupResult(BaseModel):
    area_code: Optional[str] = None
    """NPA area code (first 3 digits of national number, only for NANP numbers)"""

    area_code_region: Optional[str] = None
    """General region for the area code (most common city, only for NANP numbers)"""

    country: Optional[str] = None
    """ISO 3166-1 alpha-2 country code"""

    country_calling_code: Optional[str] = None
    """Country calling code without +"""

    e164: Optional[str] = None
    """E.164 formatted number"""

    exchange: Optional[str] = None
    """NXX exchange code (digits 4-6 of national number, only for NANP numbers)"""

    input: Optional[str] = None
    """The original input string"""

    international: Optional[str] = None
    """International formatted number"""

    location: Optional[Location] = None
    """NANPA geocoding location (only for North American numbers with country code 1)"""

    national: Optional[str] = None
    """National formatted number"""

    national_number: Optional[str] = None
    """National number without country code"""

    possible: Optional[bool] = None
    """Whether the phone number is a possible number (less strict than valid)"""

    type: Optional[
        Literal[
            "FIXED_LINE",
            "MOBILE",
            "FIXED_LINE_OR_MOBILE",
            "TOLL_FREE",
            "PREMIUM_RATE",
            "SHARED_COST",
            "VOIP",
            "PERSONAL_NUMBER",
            "PAGER",
            "UAN",
            "VOICEMAIL",
        ]
    ] = None
    """Number type detected by libphonenumber"""

    valid: Optional[bool] = None
    """Whether the phone number is valid"""
