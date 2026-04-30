# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .phone_numbers.phone_number_lookup_result import PhoneNumberLookupResult

__all__ = ["PhoneNumberBatchCreateResponse"]


class PhoneNumberBatchCreateResponse(BaseModel):
    results: Optional[List[PhoneNumberLookupResult]] = None
