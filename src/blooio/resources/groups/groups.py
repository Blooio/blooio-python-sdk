# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .icon import (
    IconResource,
    AsyncIconResource,
    IconResourceWithRawResponse,
    AsyncIconResourceWithRawResponse,
    IconResourceWithStreamingResponse,
    AsyncIconResourceWithStreamingResponse,
)
from ...types import group_list_params, group_create_params, group_update_params
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.group import Group
from ..._base_client import make_request_options
from ...types.group_list_response import GroupListResponse
from ...types.group_create_response import GroupCreateResponse
from ...types.group_delete_response import GroupDeleteResponse
from ...types.group_update_response import GroupUpdateResponse

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    """Manage contact groups"""

    @cached_property
    def members(self) -> MembersResource:
        """Manage group membership"""
        return MembersResource(self._client)

    @cached_property
    def icon(self) -> IconResource:
        """Manage contact groups"""
        return IconResource(self._client)

    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return GroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        chat_guid: str | Omit = omit,
        members: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupCreateResponse:
        """Create a new group.

        There are two modes:

        **1. Link to existing iMessage chat:** Provide `chat_guid` to join an existing
        group chat that was created outside the API. The `members` list records who is
        in the group but does NOT add them to the linked iMessage chat. Multiple groups
        can have the same participants if they have different `chat_guid`s.

        **2. Create new group:** Omit `chat_guid` to create a new group. When you send
        the first message, a new iMessage chat will be created. Note: iMessage only
        allows one chat per unique participant set when created via API.

        Args:
          name: Group name (max 255 characters)

          chat_guid: BlueBubbles chat GUID to link this group to an existing iMessage chat. Use this
              to join groups created elsewhere. You can get this from the BlueBubbles API or
              from inbound message webhooks.

          members: Phone numbers or emails of contacts in the group. When linking via chat_guid,
              this is for record-keeping only (members are not added to the linked iMessage
              chat).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/groups",
            body=maybe_transform(
                {
                    "name": name,
                    "chat_guid": chat_guid,
                    "members": members,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    def retrieve(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Get details for a specific group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            path_template("/groups/{group_id}", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    def update(
        self,
        group_id: str,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupUpdateResponse:
        """Update a group's name.

        If the group has a linked `chat_guid`, the display name
        will also be updated in the linked iMessage chat. Note: iMessage only allows one
        chat per unique participant set, so renaming simply changes the display name on
        the existing chat thread.

        Args:
          name: New group name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._patch(
            path_template("/groups/{group_id}", group_id=group_id),
            body=maybe_transform({"name": name}, group_update_params.GroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        q: str | Omit = omit,
        sort: Literal["recent", "oldest", "name_asc", "name_desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupListResponse:
        """
        List all groups for the organization with optional search and pagination.

        Args:
          limit: Maximum number of items to return (1-200)

          offset: Number of items to skip

          q: Search query (matches group name)

          sort: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "q": q,
                        "sort": sort,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            cast_to=GroupListResponse,
        )

    def delete(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupDeleteResponse:
        """Soft-delete a group.

        Members are automatically removed. If the group is linked
        to an existing iMessage chat, the number also leaves that chat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._delete(
            path_template("/groups/{group_id}", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupDeleteResponse,
        )


class AsyncGroupsResource(AsyncAPIResource):
    """Manage contact groups"""

    @cached_property
    def members(self) -> AsyncMembersResource:
        """Manage group membership"""
        return AsyncMembersResource(self._client)

    @cached_property
    def icon(self) -> AsyncIconResource:
        """Manage contact groups"""
        return AsyncIconResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        chat_guid: str | Omit = omit,
        members: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupCreateResponse:
        """Create a new group.

        There are two modes:

        **1. Link to existing iMessage chat:** Provide `chat_guid` to join an existing
        group chat that was created outside the API. The `members` list records who is
        in the group but does NOT add them to the linked iMessage chat. Multiple groups
        can have the same participants if they have different `chat_guid`s.

        **2. Create new group:** Omit `chat_guid` to create a new group. When you send
        the first message, a new iMessage chat will be created. Note: iMessage only
        allows one chat per unique participant set when created via API.

        Args:
          name: Group name (max 255 characters)

          chat_guid: BlueBubbles chat GUID to link this group to an existing iMessage chat. Use this
              to join groups created elsewhere. You can get this from the BlueBubbles API or
              from inbound message webhooks.

          members: Phone numbers or emails of contacts in the group. When linking via chat_guid,
              this is for record-keeping only (members are not added to the linked iMessage
              chat).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/groups",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "chat_guid": chat_guid,
                    "members": members,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    async def retrieve(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Group:
        """
        Get details for a specific group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            path_template("/groups/{group_id}", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Group,
        )

    async def update(
        self,
        group_id: str,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupUpdateResponse:
        """Update a group's name.

        If the group has a linked `chat_guid`, the display name
        will also be updated in the linked iMessage chat. Note: iMessage only allows one
        chat per unique participant set, so renaming simply changes the display name on
        the existing chat thread.

        Args:
          name: New group name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._patch(
            path_template("/groups/{group_id}", group_id=group_id),
            body=await async_maybe_transform({"name": name}, group_update_params.GroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        q: str | Omit = omit,
        sort: Literal["recent", "oldest", "name_asc", "name_desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupListResponse:
        """
        List all groups for the organization with optional search and pagination.

        Args:
          limit: Maximum number of items to return (1-200)

          offset: Number of items to skip

          q: Search query (matches group name)

          sort: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "q": q,
                        "sort": sort,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            cast_to=GroupListResponse,
        )

    async def delete(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupDeleteResponse:
        """Soft-delete a group.

        Members are automatically removed. If the group is linked
        to an existing iMessage chat, the number also leaves that chat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._delete(
            path_template("/groups/{group_id}", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupDeleteResponse,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_raw_response_wrapper(
            groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            groups.update,
        )
        self.list = to_raw_response_wrapper(
            groups.list,
        )
        self.delete = to_raw_response_wrapper(
            groups.delete,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        """Manage group membership"""
        return MembersResourceWithRawResponse(self._groups.members)

    @cached_property
    def icon(self) -> IconResourceWithRawResponse:
        """Manage contact groups"""
        return IconResourceWithRawResponse(self._groups.icon)


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_raw_response_wrapper(
            groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            groups.delete,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        """Manage group membership"""
        return AsyncMembersResourceWithRawResponse(self._groups.members)

    @cached_property
    def icon(self) -> AsyncIconResourceWithRawResponse:
        """Manage contact groups"""
        return AsyncIconResourceWithRawResponse(self._groups.icon)


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_streamed_response_wrapper(
            groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            groups.update,
        )
        self.list = to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            groups.delete,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        """Manage group membership"""
        return MembersResourceWithStreamingResponse(self._groups.members)

    @cached_property
    def icon(self) -> IconResourceWithStreamingResponse:
        """Manage contact groups"""
        return IconResourceWithStreamingResponse(self._groups.icon)


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_streamed_response_wrapper(
            groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            groups.delete,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        """Manage group membership"""
        return AsyncMembersResourceWithStreamingResponse(self._groups.members)

    @cached_property
    def icon(self) -> AsyncIconResourceWithStreamingResponse:
        """Manage contact groups"""
        return AsyncIconResourceWithStreamingResponse(self._groups.icon)
