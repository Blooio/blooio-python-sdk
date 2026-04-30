# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.groups import member_add_params, member_list_params
from ...types.groups.member_add_response import MemberAddResponse
from ...types.groups.member_list_response import MemberListResponse
from ...types.groups.member_remove_response import MemberRemoveResponse

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    """Manage group membership"""

    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)

    def list(
        self,
        group_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListResponse:
        """
        List all members of a group.

        Args:
          limit: Maximum number of items to return (1-200)

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            path_template("/groups/{group_id}/members", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            cast_to=MemberListResponse,
        )

    def add(
        self,
        group_id: str,
        *,
        contact_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberAddResponse:
        """
        ⚠️ **COMING SOON** - This endpoint is temporarily disabled while we stabilize
        this feature.

        Add an existing contact to a group. If the group is linked to an existing
        iMessage chat, also adds the participant to that chat.

        Args:
          contact_id: Contact identifier (phone number or email)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            path_template("/groups/{group_id}/members", group_id=group_id),
            body=maybe_transform({"contact_id": contact_id}, member_add_params.MemberAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberAddResponse,
        )

    def remove(
        self,
        contact_id: str,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberRemoveResponse:
        """
        ⚠️ **COMING SOON** - This endpoint is temporarily disabled while we stabilize
        this feature.

        Remove a contact from a group. If the group is linked to an existing iMessage
        chat, also removes the participant from that chat. If the contact being removed
        is the organization's own phone number, leaves the group chat instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._delete(
            path_template("/groups/{group_id}/members/{contact_id}", group_id=group_id, contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberRemoveResponse,
        )


class AsyncMembersResource(AsyncAPIResource):
    """Manage group membership"""

    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)

    async def list(
        self,
        group_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListResponse:
        """
        List all members of a group.

        Args:
          limit: Maximum number of items to return (1-200)

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            path_template("/groups/{group_id}/members", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            cast_to=MemberListResponse,
        )

    async def add(
        self,
        group_id: str,
        *,
        contact_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberAddResponse:
        """
        ⚠️ **COMING SOON** - This endpoint is temporarily disabled while we stabilize
        this feature.

        Add an existing contact to a group. If the group is linked to an existing
        iMessage chat, also adds the participant to that chat.

        Args:
          contact_id: Contact identifier (phone number or email)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            path_template("/groups/{group_id}/members", group_id=group_id),
            body=await async_maybe_transform({"contact_id": contact_id}, member_add_params.MemberAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberAddResponse,
        )

    async def remove(
        self,
        contact_id: str,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberRemoveResponse:
        """
        ⚠️ **COMING SOON** - This endpoint is temporarily disabled while we stabilize
        this feature.

        Remove a contact from a group. If the group is linked to an existing iMessage
        chat, also removes the participant from that chat. If the contact being removed
        is the organization's own phone number, leaves the group chat instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._delete(
            path_template("/groups/{group_id}/members/{contact_id}", group_id=group_id, contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberRemoveResponse,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_raw_response_wrapper(
            members.list,
        )
        self.add = to_raw_response_wrapper(
            members.add,
        )
        self.remove = to_raw_response_wrapper(
            members.remove,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_raw_response_wrapper(
            members.list,
        )
        self.add = async_to_raw_response_wrapper(
            members.add,
        )
        self.remove = async_to_raw_response_wrapper(
            members.remove,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_streamed_response_wrapper(
            members.list,
        )
        self.add = to_streamed_response_wrapper(
            members.add,
        )
        self.remove = to_streamed_response_wrapper(
            members.remove,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
        self.add = async_to_streamed_response_wrapper(
            members.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            members.remove,
        )
