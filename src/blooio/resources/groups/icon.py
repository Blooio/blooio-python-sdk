# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Query, Headers, NotGiven, FileTypes, not_given
from ..._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.groups import icon_set_params
from ...types.groups.group_icon import GroupIcon

__all__ = ["IconResource", "AsyncIconResource"]


class IconResource(SyncAPIResource):
    """Manage contact groups"""

    @cached_property
    def with_raw_response(self) -> IconResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return IconResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IconResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return IconResourceWithStreamingResponse(self)

    def remove(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupIcon:
        """Remove the group icon/photo.

        Requires the group to have a linked chat_guid.

        The icon is removed from both Blooio storage and the linked iMessage chat before
        the request returns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._delete(
            path_template("/groups/{group_id}/icon", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupIcon,
        )

    def set(
        self,
        group_id: str,
        *,
        icon: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupIcon:
        """Set the group icon/photo.

        Requires the group to have a linked chat_guid. Uses
        multipart/form-data.

        The uploaded image is stored in Blooio storage and synced to the linked iMessage
        chat before the request returns.

        Args:
          icon: The icon image file to set as the group photo

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        body = deepcopy_with_paths({"icon": icon}, [["icon"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["icon"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/groups/{group_id}/icon", group_id=group_id),
            body=maybe_transform(body, icon_set_params.IconSetParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupIcon,
        )


class AsyncIconResource(AsyncAPIResource):
    """Manage contact groups"""

    @cached_property
    def with_raw_response(self) -> AsyncIconResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIconResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIconResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncIconResourceWithStreamingResponse(self)

    async def remove(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupIcon:
        """Remove the group icon/photo.

        Requires the group to have a linked chat_guid.

        The icon is removed from both Blooio storage and the linked iMessage chat before
        the request returns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._delete(
            path_template("/groups/{group_id}/icon", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupIcon,
        )

    async def set(
        self,
        group_id: str,
        *,
        icon: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupIcon:
        """Set the group icon/photo.

        Requires the group to have a linked chat_guid. Uses
        multipart/form-data.

        The uploaded image is stored in Blooio storage and synced to the linked iMessage
        chat before the request returns.

        Args:
          icon: The icon image file to set as the group photo

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        body = deepcopy_with_paths({"icon": icon}, [["icon"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["icon"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/groups/{group_id}/icon", group_id=group_id),
            body=await async_maybe_transform(body, icon_set_params.IconSetParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupIcon,
        )


class IconResourceWithRawResponse:
    def __init__(self, icon: IconResource) -> None:
        self._icon = icon

        self.remove = to_raw_response_wrapper(
            icon.remove,
        )
        self.set = to_raw_response_wrapper(
            icon.set,
        )


class AsyncIconResourceWithRawResponse:
    def __init__(self, icon: AsyncIconResource) -> None:
        self._icon = icon

        self.remove = async_to_raw_response_wrapper(
            icon.remove,
        )
        self.set = async_to_raw_response_wrapper(
            icon.set,
        )


class IconResourceWithStreamingResponse:
    def __init__(self, icon: IconResource) -> None:
        self._icon = icon

        self.remove = to_streamed_response_wrapper(
            icon.remove,
        )
        self.set = to_streamed_response_wrapper(
            icon.set,
        )


class AsyncIconResourceWithStreamingResponse:
    def __init__(self, icon: AsyncIconResource) -> None:
        self._icon = icon

        self.remove = async_to_streamed_response_wrapper(
            icon.remove,
        )
        self.set = async_to_streamed_response_wrapper(
            icon.set,
        )
