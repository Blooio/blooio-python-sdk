# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .polls import (
    PollsResource,
    AsyncPollsResource,
    PollsResourceWithRawResponse,
    AsyncPollsResourceWithRawResponse,
    PollsResourceWithStreamingResponse,
    AsyncPollsResourceWithStreamingResponse,
)
from .typing import (
    TypingResource,
    AsyncTypingResource,
    TypingResourceWithRawResponse,
    AsyncTypingResourceWithRawResponse,
    TypingResourceWithStreamingResponse,
    AsyncTypingResourceWithStreamingResponse,
)
from ...types import chat_list_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .background import (
    BackgroundResource,
    AsyncBackgroundResource,
    BackgroundResourceWithRawResponse,
    AsyncBackgroundResourceWithRawResponse,
    BackgroundResourceWithStreamingResponse,
    AsyncBackgroundResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.chat_list_response import ChatListResponse
from ...types.chat_retrieve_response import ChatRetrieveResponse
from ...types.chat_mark_as_read_response import ChatMarkAsReadResponse
from ...types.chat_share_contact_card_response import ChatShareContactCardResponse

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def polls(self) -> PollsResource:
        """Send native iMessage polls and retrieve poll results with vote counts.

        Poll events are delivered via separate webhook event types (poll.received, poll.created, poll.voted) and require webhook_type 'poll' or 'all'.
        """
        return PollsResource(self._client)

    @cached_property
    def typing(self) -> TypingResource:
        """Control typing indicators for conversations"""
        return TypingResource(self._client)

    @cached_property
    def background(self) -> BackgroundResource:
        """View conversations and messages"""
        return BackgroundResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return ChatsResourceWithStreamingResponse(self)

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
    ) -> ChatRetrieveResponse:
        """
        Get details for a specific conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            path_template("/chats/{chat_id}", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        q: str | Omit = omit,
        sort: Literal["recent", "oldest"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatListResponse:
        """
        List all unique conversations for the organization, sorted by most recent
        message.

        Args:
          limit: Maximum number of items to return in a single response. Must be between 1 and
              200; defaults to 50. Use together with `offset` to page through large result
              sets.

          offset: Number of items to skip before returning results. Combine with `limit` for
              page-based pagination (e.g. `offset=50&limit=50` returns the second page).
              Defaults to 0.

          q: Search query (matches phone/email or contact name)

          sort: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/chats",
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
                    chat_list_params.ChatListParams,
                ),
            ),
            cast_to=ChatListResponse,
        )

    def mark_as_read(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatMarkAsReadResponse:
        """Mark all messages in a chat as read.

        This sends a read receipt to the sender.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/chats/{chat_id}/read", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatMarkAsReadResponse,
        )

    def share_contact_card(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatShareContactCardResponse:
        """Stage the contact card (Name & Photo) for sharing in a chat.

        The contact card
        will be piggybacked onto the next outgoing message (text or attachment) sent to
        this chat. This is idempotent — calling it multiple times is harmless.

        ⚠️ **Plan requirement:** Contact card sharing is only available on **Dedicated
        Commercial** and **Dedicated Enterprise** plans. Numbers on other plans receive
        a `403`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/chats/{chat_id}/contact-card", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatShareContactCardResponse,
        )


class AsyncChatsResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def polls(self) -> AsyncPollsResource:
        """Send native iMessage polls and retrieve poll results with vote counts.

        Poll events are delivered via separate webhook event types (poll.received, poll.created, poll.voted) and require webhook_type 'poll' or 'all'.
        """
        return AsyncPollsResource(self._client)

    @cached_property
    def typing(self) -> AsyncTypingResource:
        """Control typing indicators for conversations"""
        return AsyncTypingResource(self._client)

    @cached_property
    def background(self) -> AsyncBackgroundResource:
        """View conversations and messages"""
        return AsyncBackgroundResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncChatsResourceWithStreamingResponse(self)

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
    ) -> ChatRetrieveResponse:
        """
        Get details for a specific conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            path_template("/chats/{chat_id}", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatRetrieveResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        q: str | Omit = omit,
        sort: Literal["recent", "oldest"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatListResponse:
        """
        List all unique conversations for the organization, sorted by most recent
        message.

        Args:
          limit: Maximum number of items to return in a single response. Must be between 1 and
              200; defaults to 50. Use together with `offset` to page through large result
              sets.

          offset: Number of items to skip before returning results. Combine with `limit` for
              page-based pagination (e.g. `offset=50&limit=50` returns the second page).
              Defaults to 0.

          q: Search query (matches phone/email or contact name)

          sort: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/chats",
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
                    chat_list_params.ChatListParams,
                ),
            ),
            cast_to=ChatListResponse,
        )

    async def mark_as_read(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatMarkAsReadResponse:
        """Mark all messages in a chat as read.

        This sends a read receipt to the sender.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/chats/{chat_id}/read", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatMarkAsReadResponse,
        )

    async def share_contact_card(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatShareContactCardResponse:
        """Stage the contact card (Name & Photo) for sharing in a chat.

        The contact card
        will be piggybacked onto the next outgoing message (text or attachment) sent to
        this chat. This is idempotent — calling it multiple times is harmless.

        ⚠️ **Plan requirement:** Contact card sharing is only available on **Dedicated
        Commercial** and **Dedicated Enterprise** plans. Numbers on other plans receive
        a `403`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/chats/{chat_id}/contact-card", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatShareContactCardResponse,
        )


class ChatsResourceWithRawResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.retrieve = to_raw_response_wrapper(
            chats.retrieve,
        )
        self.list = to_raw_response_wrapper(
            chats.list,
        )
        self.mark_as_read = to_raw_response_wrapper(
            chats.mark_as_read,
        )
        self.share_contact_card = to_raw_response_wrapper(
            chats.share_contact_card,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._chats.messages)

    @cached_property
    def polls(self) -> PollsResourceWithRawResponse:
        """Send native iMessage polls and retrieve poll results with vote counts.

        Poll events are delivered via separate webhook event types (poll.received, poll.created, poll.voted) and require webhook_type 'poll' or 'all'.
        """
        return PollsResourceWithRawResponse(self._chats.polls)

    @cached_property
    def typing(self) -> TypingResourceWithRawResponse:
        """Control typing indicators for conversations"""
        return TypingResourceWithRawResponse(self._chats.typing)

    @cached_property
    def background(self) -> BackgroundResourceWithRawResponse:
        """View conversations and messages"""
        return BackgroundResourceWithRawResponse(self._chats.background)


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.retrieve = async_to_raw_response_wrapper(
            chats.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            chats.list,
        )
        self.mark_as_read = async_to_raw_response_wrapper(
            chats.mark_as_read,
        )
        self.share_contact_card = async_to_raw_response_wrapper(
            chats.share_contact_card,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._chats.messages)

    @cached_property
    def polls(self) -> AsyncPollsResourceWithRawResponse:
        """Send native iMessage polls and retrieve poll results with vote counts.

        Poll events are delivered via separate webhook event types (poll.received, poll.created, poll.voted) and require webhook_type 'poll' or 'all'.
        """
        return AsyncPollsResourceWithRawResponse(self._chats.polls)

    @cached_property
    def typing(self) -> AsyncTypingResourceWithRawResponse:
        """Control typing indicators for conversations"""
        return AsyncTypingResourceWithRawResponse(self._chats.typing)

    @cached_property
    def background(self) -> AsyncBackgroundResourceWithRawResponse:
        """View conversations and messages"""
        return AsyncBackgroundResourceWithRawResponse(self._chats.background)


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.retrieve = to_streamed_response_wrapper(
            chats.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            chats.list,
        )
        self.mark_as_read = to_streamed_response_wrapper(
            chats.mark_as_read,
        )
        self.share_contact_card = to_streamed_response_wrapper(
            chats.share_contact_card,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._chats.messages)

    @cached_property
    def polls(self) -> PollsResourceWithStreamingResponse:
        """Send native iMessage polls and retrieve poll results with vote counts.

        Poll events are delivered via separate webhook event types (poll.received, poll.created, poll.voted) and require webhook_type 'poll' or 'all'.
        """
        return PollsResourceWithStreamingResponse(self._chats.polls)

    @cached_property
    def typing(self) -> TypingResourceWithStreamingResponse:
        """Control typing indicators for conversations"""
        return TypingResourceWithStreamingResponse(self._chats.typing)

    @cached_property
    def background(self) -> BackgroundResourceWithStreamingResponse:
        """View conversations and messages"""
        return BackgroundResourceWithStreamingResponse(self._chats.background)


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.retrieve = async_to_streamed_response_wrapper(
            chats.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            chats.list,
        )
        self.mark_as_read = async_to_streamed_response_wrapper(
            chats.mark_as_read,
        )
        self.share_contact_card = async_to_streamed_response_wrapper(
            chats.share_contact_card,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._chats.messages)

    @cached_property
    def polls(self) -> AsyncPollsResourceWithStreamingResponse:
        """Send native iMessage polls and retrieve poll results with vote counts.

        Poll events are delivered via separate webhook event types (poll.received, poll.created, poll.voted) and require webhook_type 'poll' or 'all'.
        """
        return AsyncPollsResourceWithStreamingResponse(self._chats.polls)

    @cached_property
    def typing(self) -> AsyncTypingResourceWithStreamingResponse:
        """Control typing indicators for conversations"""
        return AsyncTypingResourceWithStreamingResponse(self._chats.typing)

    @cached_property
    def background(self) -> AsyncBackgroundResourceWithStreamingResponse:
        """View conversations and messages"""
        return AsyncBackgroundResourceWithStreamingResponse(self._chats.background)
