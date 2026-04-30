# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.me.numbers import contact_card_update_params
from ....types.me.numbers.contact_card_update_response import ContactCardUpdateResponse
from ....types.me.numbers.contact_card_retrieve_response import ContactCardRetrieveResponse

__all__ = ["ContactCardResource", "AsyncContactCardResource"]


class ContactCardResource(SyncAPIResource):
    """Manage and share your iMessage contact card (Name & Photo)"""

    @cached_property
    def with_raw_response(self) -> ContactCardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ContactCardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactCardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return ContactCardResourceWithStreamingResponse(self)

    def retrieve(
        self,
        number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCardRetrieveResponse:
        """
        ⚠️ **COMING SOON** - This endpoint is temporarily disabled while we stabilize
        this feature.

        Get the personal contact card (Name & Photo) for the specified phone number.
        This is the identity that gets shared with contacts in iMessage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
        return self._get(
            path_template("/me/numbers/{number}/contact-card", number=number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCardRetrieveResponse,
        )

    def update(
        self,
        number: str,
        *,
        avatar: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        sharing: contact_card_update_params.Sharing | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCardUpdateResponse:
        """
        Update the personal contact card (Name & Photo) for the specified phone number.
        All fields are optional — only provided fields are updated.

        Args:
          avatar: Profile photo as base64-encoded JPEG/PNG

          first_name: First name

          last_name: Last name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
        return self._put(
            path_template("/me/numbers/{number}/contact-card", number=number),
            body=maybe_transform(
                {
                    "avatar": avatar,
                    "first_name": first_name,
                    "last_name": last_name,
                    "sharing": sharing,
                },
                contact_card_update_params.ContactCardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCardUpdateResponse,
        )


class AsyncContactCardResource(AsyncAPIResource):
    """Manage and share your iMessage contact card (Name & Photo)"""

    @cached_property
    def with_raw_response(self) -> AsyncContactCardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncContactCardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactCardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncContactCardResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCardRetrieveResponse:
        """
        ⚠️ **COMING SOON** - This endpoint is temporarily disabled while we stabilize
        this feature.

        Get the personal contact card (Name & Photo) for the specified phone number.
        This is the identity that gets shared with contacts in iMessage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
        return await self._get(
            path_template("/me/numbers/{number}/contact-card", number=number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCardRetrieveResponse,
        )

    async def update(
        self,
        number: str,
        *,
        avatar: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        sharing: contact_card_update_params.Sharing | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCardUpdateResponse:
        """
        Update the personal contact card (Name & Photo) for the specified phone number.
        All fields are optional — only provided fields are updated.

        Args:
          avatar: Profile photo as base64-encoded JPEG/PNG

          first_name: First name

          last_name: Last name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
        return await self._put(
            path_template("/me/numbers/{number}/contact-card", number=number),
            body=await async_maybe_transform(
                {
                    "avatar": avatar,
                    "first_name": first_name,
                    "last_name": last_name,
                    "sharing": sharing,
                },
                contact_card_update_params.ContactCardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCardUpdateResponse,
        )


class ContactCardResourceWithRawResponse:
    def __init__(self, contact_card: ContactCardResource) -> None:
        self._contact_card = contact_card

        self.retrieve = to_raw_response_wrapper(
            contact_card.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contact_card.update,
        )


class AsyncContactCardResourceWithRawResponse:
    def __init__(self, contact_card: AsyncContactCardResource) -> None:
        self._contact_card = contact_card

        self.retrieve = async_to_raw_response_wrapper(
            contact_card.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contact_card.update,
        )


class ContactCardResourceWithStreamingResponse:
    def __init__(self, contact_card: ContactCardResource) -> None:
        self._contact_card = contact_card

        self.retrieve = to_streamed_response_wrapper(
            contact_card.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contact_card.update,
        )


class AsyncContactCardResourceWithStreamingResponse:
    def __init__(self, contact_card: AsyncContactCardResource) -> None:
        self._contact_card = contact_card

        self.retrieve = async_to_streamed_response_wrapper(
            contact_card.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contact_card.update,
        )
