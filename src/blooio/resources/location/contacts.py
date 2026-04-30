# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.location.contact_location import ContactLocation
from ...types.location.contact_list_response import ContactListResponse
from ...types.location.contact_refresh_response import ContactRefreshResponse

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    """FindMy contact location tracking"""

    @cached_property
    def with_raw_response(self) -> ContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return ContactsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactLocation:
        """
        Returns the cached location for a specific contact identified by phone number or
        email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return self._get(
            path_template("/location/contacts/{handle}", handle=handle),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactLocation,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """
        Returns cached FindMy contact locations available through your blooio account.
        Each entry includes the contact's handle (phone/email), coordinates, and last
        update time.
        """
        return self._get(
            "/location/contacts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactListResponse,
        )

    def refresh(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactRefreshResponse:
        """Triggers a refresh of cached FindMy contact locations.

        Updated results may take
        15-20 seconds to appear.
        """
        return self._post(
            "/location/contacts/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRefreshResponse,
        )


class AsyncContactsResource(AsyncAPIResource):
    """FindMy contact location tracking"""

    @cached_property
    def with_raw_response(self) -> AsyncContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncContactsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactLocation:
        """
        Returns the cached location for a specific contact identified by phone number or
        email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return await self._get(
            path_template("/location/contacts/{handle}", handle=handle),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactLocation,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """
        Returns cached FindMy contact locations available through your blooio account.
        Each entry includes the contact's handle (phone/email), coordinates, and last
        update time.
        """
        return await self._get(
            "/location/contacts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactListResponse,
        )

    async def refresh(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactRefreshResponse:
        """Triggers a refresh of cached FindMy contact locations.

        Updated results may take
        15-20 seconds to appear.
        """
        return await self._post(
            "/location/contacts/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRefreshResponse,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.retrieve = to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            contacts.list,
        )
        self.refresh = to_raw_response_wrapper(
            contacts.refresh,
        )


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.retrieve = async_to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )
        self.refresh = async_to_raw_response_wrapper(
            contacts.refresh,
        )


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.retrieve = to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            contacts.list,
        )
        self.refresh = to_streamed_response_wrapper(
            contacts.refresh,
        )


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.retrieve = async_to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )
        self.refresh = async_to_streamed_response_wrapper(
            contacts.refresh,
        )
