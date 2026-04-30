# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .contact_card import (
    ContactCardResource,
    AsyncContactCardResource,
    ContactCardResourceWithRawResponse,
    AsyncContactCardResourceWithRawResponse,
    ContactCardResourceWithStreamingResponse,
    AsyncContactCardResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.me.number_list_response import NumberListResponse

__all__ = ["NumbersResource", "AsyncNumbersResource"]


class NumbersResource(SyncAPIResource):
    """Manage phone numbers linked to your account"""

    @cached_property
    def contact_card(self) -> ContactCardResource:
        """Manage and share your iMessage contact card (Name & Photo)"""
        return ContactCardResource(self._client)

    @cached_property
    def with_raw_response(self) -> NumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#accessing-raw-response-data-eg-headers
        """
        return NumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#with_streaming_response
        """
        return NumbersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberListResponse:
        """List all phone numbers bound to this API key with their availability status.

        Use
        the returned phone numbers as the `:number` path parameter for other
        `/me/numbers/` endpoints.
        """
        return self._get(
            "/me/numbers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberListResponse,
        )


class AsyncNumbersResource(AsyncAPIResource):
    """Manage phone numbers linked to your account"""

    @cached_property
    def contact_card(self) -> AsyncContactCardResource:
        """Manage and share your iMessage contact card (Name & Photo)"""
        return AsyncContactCardResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#with_streaming_response
        """
        return AsyncNumbersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberListResponse:
        """List all phone numbers bound to this API key with their availability status.

        Use
        the returned phone numbers as the `:number` path parameter for other
        `/me/numbers/` endpoints.
        """
        return await self._get(
            "/me/numbers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberListResponse,
        )


class NumbersResourceWithRawResponse:
    def __init__(self, numbers: NumbersResource) -> None:
        self._numbers = numbers

        self.list = to_raw_response_wrapper(
            numbers.list,
        )

    @cached_property
    def contact_card(self) -> ContactCardResourceWithRawResponse:
        """Manage and share your iMessage contact card (Name & Photo)"""
        return ContactCardResourceWithRawResponse(self._numbers.contact_card)


class AsyncNumbersResourceWithRawResponse:
    def __init__(self, numbers: AsyncNumbersResource) -> None:
        self._numbers = numbers

        self.list = async_to_raw_response_wrapper(
            numbers.list,
        )

    @cached_property
    def contact_card(self) -> AsyncContactCardResourceWithRawResponse:
        """Manage and share your iMessage contact card (Name & Photo)"""
        return AsyncContactCardResourceWithRawResponse(self._numbers.contact_card)


class NumbersResourceWithStreamingResponse:
    def __init__(self, numbers: NumbersResource) -> None:
        self._numbers = numbers

        self.list = to_streamed_response_wrapper(
            numbers.list,
        )

    @cached_property
    def contact_card(self) -> ContactCardResourceWithStreamingResponse:
        """Manage and share your iMessage contact card (Name & Photo)"""
        return ContactCardResourceWithStreamingResponse(self._numbers.contact_card)


class AsyncNumbersResourceWithStreamingResponse:
    def __init__(self, numbers: AsyncNumbersResource) -> None:
        self._numbers = numbers

        self.list = async_to_streamed_response_wrapper(
            numbers.list,
        )

    @cached_property
    def contact_card(self) -> AsyncContactCardResourceWithStreamingResponse:
        """Manage and share your iMessage contact card (Name & Photo)"""
        return AsyncContactCardResourceWithStreamingResponse(self._numbers.contact_card)
