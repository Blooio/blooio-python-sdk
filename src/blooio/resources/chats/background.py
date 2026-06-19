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
from ...types.chats import background_set_params
from ..._base_client import make_request_options
from ...types.chats.chat_background_response import ChatBackgroundResponse

__all__ = ["BackgroundResource", "AsyncBackgroundResource"]


class BackgroundResource(SyncAPIResource):
    """View conversations and messages"""

    @cached_property
    def with_raw_response(self) -> BackgroundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BackgroundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BackgroundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return BackgroundResourceWithStreamingResponse(self)

    def retrieve(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatBackgroundResponse:
        """Get the current background image metadata for a conversation.

        Works for both
        1-on-1 and group chats.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            path_template("/chats/{chat_id}/background", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatBackgroundResponse,
        )

    def remove(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatBackgroundResponse:
        """
        Remove the background image from a conversation, reverting to the default
        appearance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._delete(
            path_template("/chats/{chat_id}/background", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatBackgroundResponse,
        )

    def set(
        self,
        chat_id: str,
        *,
        background: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatBackgroundResponse:
        """Set or update the background image for a conversation.

        Works for both 1-on-1 and
        group chats.

        The request body must be `multipart/form-data` with a single `background` field
        containing the **raw image file bytes** (not a URL or base64 string). Supported
        formats: JPEG, PNG, GIF, WebP, HEIC/HEIF. Maximum file size: 10 MB.

        **Example with curl** — note the `@` prefix that tells curl to read the file
        from disk:

        ```bash
        curl -X PUT "https://api.blooio.com/v2/api/chats/%2B15551234567/background" \\
          -H "Authorization: Bearer YOUR_API_KEY" \\
          -F "background=@/path/to/image.jpg;type=image/jpeg"
        ```

        When the chat id is a phone number, percent-encode the leading `+` as `%2B` in
        the URL path.

        Args:
          background: Binary image file upload (JPEG, PNG, GIF, WebP, HEIC/HEIF, max 10 MB). Send as a
              file field in `multipart/form-data` — e.g. `-F "background=@/path/to/image.jpg"`
              with curl, or a `File`/`Blob` appended to `FormData` in JavaScript. Do NOT send
              a URL or base64 string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        body = deepcopy_with_paths({"background": background}, [["background"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["background"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            path_template("/chats/{chat_id}/background", chat_id=chat_id),
            body=maybe_transform(body, background_set_params.BackgroundSetParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatBackgroundResponse,
        )


class AsyncBackgroundResource(AsyncAPIResource):
    """View conversations and messages"""

    @cached_property
    def with_raw_response(self) -> AsyncBackgroundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBackgroundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBackgroundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncBackgroundResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatBackgroundResponse:
        """Get the current background image metadata for a conversation.

        Works for both
        1-on-1 and group chats.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            path_template("/chats/{chat_id}/background", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatBackgroundResponse,
        )

    async def remove(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatBackgroundResponse:
        """
        Remove the background image from a conversation, reverting to the default
        appearance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._delete(
            path_template("/chats/{chat_id}/background", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatBackgroundResponse,
        )

    async def set(
        self,
        chat_id: str,
        *,
        background: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatBackgroundResponse:
        """Set or update the background image for a conversation.

        Works for both 1-on-1 and
        group chats.

        The request body must be `multipart/form-data` with a single `background` field
        containing the **raw image file bytes** (not a URL or base64 string). Supported
        formats: JPEG, PNG, GIF, WebP, HEIC/HEIF. Maximum file size: 10 MB.

        **Example with curl** — note the `@` prefix that tells curl to read the file
        from disk:

        ```bash
        curl -X PUT "https://api.blooio.com/v2/api/chats/%2B15551234567/background" \\
          -H "Authorization: Bearer YOUR_API_KEY" \\
          -F "background=@/path/to/image.jpg;type=image/jpeg"
        ```

        When the chat id is a phone number, percent-encode the leading `+` as `%2B` in
        the URL path.

        Args:
          background: Binary image file upload (JPEG, PNG, GIF, WebP, HEIC/HEIF, max 10 MB). Send as a
              file field in `multipart/form-data` — e.g. `-F "background=@/path/to/image.jpg"`
              with curl, or a `File`/`Blob` appended to `FormData` in JavaScript. Do NOT send
              a URL or base64 string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        body = deepcopy_with_paths({"background": background}, [["background"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["background"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            path_template("/chats/{chat_id}/background", chat_id=chat_id),
            body=await async_maybe_transform(body, background_set_params.BackgroundSetParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatBackgroundResponse,
        )


class BackgroundResourceWithRawResponse:
    def __init__(self, background: BackgroundResource) -> None:
        self._background = background

        self.retrieve = to_raw_response_wrapper(
            background.retrieve,
        )
        self.remove = to_raw_response_wrapper(
            background.remove,
        )
        self.set = to_raw_response_wrapper(
            background.set,
        )


class AsyncBackgroundResourceWithRawResponse:
    def __init__(self, background: AsyncBackgroundResource) -> None:
        self._background = background

        self.retrieve = async_to_raw_response_wrapper(
            background.retrieve,
        )
        self.remove = async_to_raw_response_wrapper(
            background.remove,
        )
        self.set = async_to_raw_response_wrapper(
            background.set,
        )


class BackgroundResourceWithStreamingResponse:
    def __init__(self, background: BackgroundResource) -> None:
        self._background = background

        self.retrieve = to_streamed_response_wrapper(
            background.retrieve,
        )
        self.remove = to_streamed_response_wrapper(
            background.remove,
        )
        self.set = to_streamed_response_wrapper(
            background.set,
        )


class AsyncBackgroundResourceWithStreamingResponse:
    def __init__(self, background: AsyncBackgroundResource) -> None:
        self._background = background

        self.retrieve = async_to_streamed_response_wrapper(
            background.retrieve,
        )
        self.remove = async_to_streamed_response_wrapper(
            background.remove,
        )
        self.set = async_to_streamed_response_wrapper(
            background.set,
        )
