# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.phone_numbers import lookup_create_params, lookup_retrieve_params
from ...types.phone_numbers.phone_number_lookup_result import PhoneNumberLookupResult

__all__ = ["LookupResource", "AsyncLookupResource"]


class LookupResource(SyncAPIResource):
    """Phone number validation, formatting, and NANPA geocoding.

    Requires an Enterprise plan (Dedicated Enterprise).
    """

    @cached_property
    def with_raw_response(self) -> LookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#accessing-raw-response-data-eg-headers
        """
        return LookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#with_streaming_response
        """
        return LookupResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberLookupResult:
        """
        Same as the GET endpoint, but accepts the phone number in the request body.
        Useful when the number contains characters that are difficult to URL-encode.

        **Requires an Enterprise plan** (Dedicated Enterprise).

        Args:
          number: Phone number to look up

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/phone-numbers/lookup",
            body=maybe_transform({"number": number}, lookup_create_params.LookupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberLookupResult,
        )

    def retrieve(
        self,
        *,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberLookupResult:
        """
        Returns detailed information about a phone number including validation,
        formatting (E.164, national, international), number type, and NANPA geocoding
        (city, state/province) for North American numbers. The geocoding data is sourced
        from different database with 240,000+ NPA-NXX entries.

        **Requires an Enterprise plan** (Dedicated Enterprise). Returns 403 if your
        organization does not have an active enterprise subscription.

        Args:
          number: Phone number to look up. Can be E.164 format (+12125551234), national format
              (2125551234), or with formatting ((212) 555-1234).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/phone-numbers/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"number": number}, lookup_retrieve_params.LookupRetrieveParams),
            ),
            cast_to=PhoneNumberLookupResult,
        )


class AsyncLookupResource(AsyncAPIResource):
    """Phone number validation, formatting, and NANPA geocoding.

    Requires an Enterprise plan (Dedicated Enterprise).
    """

    @cached_property
    def with_raw_response(self) -> AsyncLookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#with_streaming_response
        """
        return AsyncLookupResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberLookupResult:
        """
        Same as the GET endpoint, but accepts the phone number in the request body.
        Useful when the number contains characters that are difficult to URL-encode.

        **Requires an Enterprise plan** (Dedicated Enterprise).

        Args:
          number: Phone number to look up

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/phone-numbers/lookup",
            body=await async_maybe_transform({"number": number}, lookup_create_params.LookupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberLookupResult,
        )

    async def retrieve(
        self,
        *,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberLookupResult:
        """
        Returns detailed information about a phone number including validation,
        formatting (E.164, national, international), number type, and NANPA geocoding
        (city, state/province) for North American numbers. The geocoding data is sourced
        from different database with 240,000+ NPA-NXX entries.

        **Requires an Enterprise plan** (Dedicated Enterprise). Returns 403 if your
        organization does not have an active enterprise subscription.

        Args:
          number: Phone number to look up. Can be E.164 format (+12125551234), national format
              (2125551234), or with formatting ((212) 555-1234).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/phone-numbers/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"number": number}, lookup_retrieve_params.LookupRetrieveParams),
            ),
            cast_to=PhoneNumberLookupResult,
        )


class LookupResourceWithRawResponse:
    def __init__(self, lookup: LookupResource) -> None:
        self._lookup = lookup

        self.create = to_raw_response_wrapper(
            lookup.create,
        )
        self.retrieve = to_raw_response_wrapper(
            lookup.retrieve,
        )


class AsyncLookupResourceWithRawResponse:
    def __init__(self, lookup: AsyncLookupResource) -> None:
        self._lookup = lookup

        self.create = async_to_raw_response_wrapper(
            lookup.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            lookup.retrieve,
        )


class LookupResourceWithStreamingResponse:
    def __init__(self, lookup: LookupResource) -> None:
        self._lookup = lookup

        self.create = to_streamed_response_wrapper(
            lookup.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            lookup.retrieve,
        )


class AsyncLookupResourceWithStreamingResponse:
    def __init__(self, lookup: AsyncLookupResource) -> None:
        self._lookup = lookup

        self.create = async_to_streamed_response_wrapper(
            lookup.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            lookup.retrieve,
        )
