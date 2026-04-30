# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .lookup import (
    LookupResource,
    AsyncLookupResource,
    LookupResourceWithRawResponse,
    AsyncLookupResourceWithRawResponse,
    LookupResourceWithStreamingResponse,
    AsyncLookupResourceWithStreamingResponse,
)
from ...types import phone_number_batch_create_params
from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.phone_number_batch_create_response import PhoneNumberBatchCreateResponse

__all__ = ["PhoneNumbersResource", "AsyncPhoneNumbersResource"]


class PhoneNumbersResource(SyncAPIResource):
    """Phone number validation, formatting, and NANPA geocoding.

    Requires an Enterprise plan (Dedicated Enterprise).
    """

    @cached_property
    def lookup(self) -> LookupResource:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        return LookupResource(self._client)

    @cached_property
    def with_raw_response(self) -> PhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return PhoneNumbersResourceWithStreamingResponse(self)

    def batch_create(
        self,
        *,
        numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberBatchCreateResponse:
        """Look up multiple phone numbers in a single request.

        Returns the same detailed
        information as the single lookup endpoint for each number. Maximum 100 numbers
        per request.

        **Requires an Enterprise plan** (Dedicated Enterprise).

        Args:
          numbers: Array of phone numbers to look up

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/phone-numbers/batch",
            body=maybe_transform({"numbers": numbers}, phone_number_batch_create_params.PhoneNumberBatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberBatchCreateResponse,
        )


class AsyncPhoneNumbersResource(AsyncAPIResource):
    """Phone number validation, formatting, and NANPA geocoding.

    Requires an Enterprise plan (Dedicated Enterprise).
    """

    @cached_property
    def lookup(self) -> AsyncLookupResource:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        return AsyncLookupResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncPhoneNumbersResourceWithStreamingResponse(self)

    async def batch_create(
        self,
        *,
        numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberBatchCreateResponse:
        """Look up multiple phone numbers in a single request.

        Returns the same detailed
        information as the single lookup endpoint for each number. Maximum 100 numbers
        per request.

        **Requires an Enterprise plan** (Dedicated Enterprise).

        Args:
          numbers: Array of phone numbers to look up

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/phone-numbers/batch",
            body=await async_maybe_transform(
                {"numbers": numbers}, phone_number_batch_create_params.PhoneNumberBatchCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberBatchCreateResponse,
        )


class PhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.batch_create = to_raw_response_wrapper(
            phone_numbers.batch_create,
        )

    @cached_property
    def lookup(self) -> LookupResourceWithRawResponse:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        return LookupResourceWithRawResponse(self._phone_numbers.lookup)


class AsyncPhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.batch_create = async_to_raw_response_wrapper(
            phone_numbers.batch_create,
        )

    @cached_property
    def lookup(self) -> AsyncLookupResourceWithRawResponse:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        return AsyncLookupResourceWithRawResponse(self._phone_numbers.lookup)


class PhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.batch_create = to_streamed_response_wrapper(
            phone_numbers.batch_create,
        )

    @cached_property
    def lookup(self) -> LookupResourceWithStreamingResponse:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        return LookupResourceWithStreamingResponse(self._phone_numbers.lookup)


class AsyncPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.batch_create = async_to_streamed_response_wrapper(
            phone_numbers.batch_create,
        )

    @cached_property
    def lookup(self) -> AsyncLookupResourceWithStreamingResponse:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        return AsyncLookupResourceWithStreamingResponse(self._phone_numbers.lookup)
