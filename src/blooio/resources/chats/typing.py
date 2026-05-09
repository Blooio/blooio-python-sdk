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
from ...types.chats.typing_response import TypingResponse

__all__ = ["TypingResource", "AsyncTypingResource"]


class TypingResource(SyncAPIResource):
    """Control typing indicators for conversations"""

    @cached_property
    def with_raw_response(self) -> TypingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TypingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return TypingResourceWithStreamingResponse(self)

    def start(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypingResponse:
        """Start the typing indicator for a chat.

        The indicator shows the recipient that
        you are typing.

        **RCS limitation:** typing indicators are only delivered for iMessage chats —
        the RCS protocol does not carry composing state. Calls against RCS-routed chats
        return 200 with a `warning` field and have no visible effect on the recipient.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/chats/{chat_id}/typing", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypingResponse,
        )

    def stop(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypingResponse:
        """
        Stop the typing indicator for a chat.

        **RCS limitation:** typing indicators are only delivered for iMessage chats —
        the RCS protocol does not carry composing state. Calls against RCS-routed chats
        return 200 with a `warning` field and have no visible effect on the recipient.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._delete(
            path_template("/chats/{chat_id}/typing", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypingResponse,
        )


class AsyncTypingResource(AsyncAPIResource):
    """Control typing indicators for conversations"""

    @cached_property
    def with_raw_response(self) -> AsyncTypingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTypingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncTypingResourceWithStreamingResponse(self)

    async def start(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypingResponse:
        """Start the typing indicator for a chat.

        The indicator shows the recipient that
        you are typing.

        **RCS limitation:** typing indicators are only delivered for iMessage chats —
        the RCS protocol does not carry composing state. Calls against RCS-routed chats
        return 200 with a `warning` field and have no visible effect on the recipient.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/chats/{chat_id}/typing", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypingResponse,
        )

    async def stop(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypingResponse:
        """
        Stop the typing indicator for a chat.

        **RCS limitation:** typing indicators are only delivered for iMessage chats —
        the RCS protocol does not carry composing state. Calls against RCS-routed chats
        return 200 with a `warning` field and have no visible effect on the recipient.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._delete(
            path_template("/chats/{chat_id}/typing", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypingResponse,
        )


class TypingResourceWithRawResponse:
    def __init__(self, typing: TypingResource) -> None:
        self._typing = typing

        self.start = to_raw_response_wrapper(
            typing.start,
        )
        self.stop = to_raw_response_wrapper(
            typing.stop,
        )


class AsyncTypingResourceWithRawResponse:
    def __init__(self, typing: AsyncTypingResource) -> None:
        self._typing = typing

        self.start = async_to_raw_response_wrapper(
            typing.start,
        )
        self.stop = async_to_raw_response_wrapper(
            typing.stop,
        )


class TypingResourceWithStreamingResponse:
    def __init__(self, typing: TypingResource) -> None:
        self._typing = typing

        self.start = to_streamed_response_wrapper(
            typing.start,
        )
        self.stop = to_streamed_response_wrapper(
            typing.stop,
        )


class AsyncTypingResourceWithStreamingResponse:
    def __init__(self, typing: AsyncTypingResource) -> None:
        self._typing = typing

        self.start = async_to_streamed_response_wrapper(
            typing.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            typing.stop,
        )
