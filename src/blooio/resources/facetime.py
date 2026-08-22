# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import facetime_initiate_call_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.facetime_initiate_call_response import FacetimeInitiateCallResponse

__all__ = ["FacetimeResource", "AsyncFacetimeResource"]


class FacetimeResource(SyncAPIResource):
    """Initiate FaceTime calls"""

    @cached_property
    def with_raw_response(self) -> FacetimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return FacetimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FacetimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return FacetimeResourceWithStreamingResponse(self)

    def initiate_call(
        self,
        *,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FacetimeInitiateCallResponse:
        """
        **Coming Soon** -- This endpoint is temporarily disabled while we stabilize the
        FaceTime call flow.

        Initiates a FaceTime call to the specified phone number or email address.
        Returns a shareable FaceTime link that anyone can use to join the call. The call
        will ring the contact and auto-admit the first person who joins via the link.

        Args:
          handle: Phone number (E.164) or email address to call

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/facetime/calls",
            body=maybe_transform({"handle": handle}, facetime_initiate_call_params.FacetimeInitiateCallParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FacetimeInitiateCallResponse,
        )


class AsyncFacetimeResource(AsyncAPIResource):
    """Initiate FaceTime calls"""

    @cached_property
    def with_raw_response(self) -> AsyncFacetimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFacetimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFacetimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncFacetimeResourceWithStreamingResponse(self)

    async def initiate_call(
        self,
        *,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FacetimeInitiateCallResponse:
        """
        **Coming Soon** -- This endpoint is temporarily disabled while we stabilize the
        FaceTime call flow.

        Initiates a FaceTime call to the specified phone number or email address.
        Returns a shareable FaceTime link that anyone can use to join the call. The call
        will ring the contact and auto-admit the first person who joins via the link.

        Args:
          handle: Phone number (E.164) or email address to call

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/facetime/calls",
            body=await async_maybe_transform(
                {"handle": handle}, facetime_initiate_call_params.FacetimeInitiateCallParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FacetimeInitiateCallResponse,
        )


class FacetimeResourceWithRawResponse:
    def __init__(self, facetime: FacetimeResource) -> None:
        self._facetime = facetime

        self.initiate_call = to_raw_response_wrapper(
            facetime.initiate_call,
        )


class AsyncFacetimeResourceWithRawResponse:
    def __init__(self, facetime: AsyncFacetimeResource) -> None:
        self._facetime = facetime

        self.initiate_call = async_to_raw_response_wrapper(
            facetime.initiate_call,
        )


class FacetimeResourceWithStreamingResponse:
    def __init__(self, facetime: FacetimeResource) -> None:
        self._facetime = facetime

        self.initiate_call = to_streamed_response_wrapper(
            facetime.initiate_call,
        )


class AsyncFacetimeResourceWithStreamingResponse:
    def __init__(self, facetime: AsyncFacetimeResource) -> None:
        self._facetime = facetime

        self.initiate_call = async_to_streamed_response_wrapper(
            facetime.initiate_call,
        )
