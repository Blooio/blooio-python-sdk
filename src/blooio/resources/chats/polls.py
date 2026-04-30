# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.chats import poll_send_params
from ..._base_client import make_request_options
from ...types.chats.poll_send_response import PollSendResponse
from ...types.chats.poll_get_results_response import PollGetResultsResponse

__all__ = ["PollsResource", "AsyncPollsResource"]


class PollsResource(SyncAPIResource):
    """Send native iMessage polls and retrieve poll results with vote counts.

    Poll events are delivered via separate webhook event types (poll.received, poll.created, poll.voted) and require webhook_type 'poll' or 'all'.
    """

    @cached_property
    def with_raw_response(self) -> PollsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#accessing-raw-response-data-eg-headers
        """
        return PollsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PollsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#with_streaming_response
        """
        return PollsResourceWithStreamingResponse(self)

    def get_results(
        self,
        poll_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollGetResultsResponse:
        """Retrieve a poll's definition and aggregated vote counts.

        The pollId is the
        poll_id returned in the poll.received or poll.created webhook event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not poll_id:
            raise ValueError(f"Expected a non-empty value for `poll_id` but received {poll_id!r}")
        return self._get(
            path_template("/chats/{chat_id}/polls/{poll_id}", chat_id=chat_id, poll_id=poll_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollGetResultsResponse,
        )

    def send(
        self,
        chat_id: str,
        *,
        options: SequenceNotStr[str],
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollSendResponse:
        """Send a native iMessage poll to a chat.

        The poll appears as an interactive ballot
        that recipients can vote on.

        Args:
          options: Array of 2-10 option strings for the poll

          title: Poll question or title (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/chats/{chat_id}/polls", chat_id=chat_id),
            body=maybe_transform(
                {
                    "options": options,
                    "title": title,
                },
                poll_send_params.PollSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollSendResponse,
        )


class AsyncPollsResource(AsyncAPIResource):
    """Send native iMessage polls and retrieve poll results with vote counts.

    Poll events are delivered via separate webhook event types (poll.received, poll.created, poll.voted) and require webhook_type 'poll' or 'all'.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPollsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPollsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPollsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blooio-python#with_streaming_response
        """
        return AsyncPollsResourceWithStreamingResponse(self)

    async def get_results(
        self,
        poll_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollGetResultsResponse:
        """Retrieve a poll's definition and aggregated vote counts.

        The pollId is the
        poll_id returned in the poll.received or poll.created webhook event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not poll_id:
            raise ValueError(f"Expected a non-empty value for `poll_id` but received {poll_id!r}")
        return await self._get(
            path_template("/chats/{chat_id}/polls/{poll_id}", chat_id=chat_id, poll_id=poll_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollGetResultsResponse,
        )

    async def send(
        self,
        chat_id: str,
        *,
        options: SequenceNotStr[str],
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollSendResponse:
        """Send a native iMessage poll to a chat.

        The poll appears as an interactive ballot
        that recipients can vote on.

        Args:
          options: Array of 2-10 option strings for the poll

          title: Poll question or title (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/chats/{chat_id}/polls", chat_id=chat_id),
            body=await async_maybe_transform(
                {
                    "options": options,
                    "title": title,
                },
                poll_send_params.PollSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollSendResponse,
        )


class PollsResourceWithRawResponse:
    def __init__(self, polls: PollsResource) -> None:
        self._polls = polls

        self.get_results = to_raw_response_wrapper(
            polls.get_results,
        )
        self.send = to_raw_response_wrapper(
            polls.send,
        )


class AsyncPollsResourceWithRawResponse:
    def __init__(self, polls: AsyncPollsResource) -> None:
        self._polls = polls

        self.get_results = async_to_raw_response_wrapper(
            polls.get_results,
        )
        self.send = async_to_raw_response_wrapper(
            polls.send,
        )


class PollsResourceWithStreamingResponse:
    def __init__(self, polls: PollsResource) -> None:
        self._polls = polls

        self.get_results = to_streamed_response_wrapper(
            polls.get_results,
        )
        self.send = to_streamed_response_wrapper(
            polls.send,
        )


class AsyncPollsResourceWithStreamingResponse:
    def __init__(self, polls: AsyncPollsResource) -> None:
        self._polls = polls

        self.get_results = async_to_streamed_response_wrapper(
            polls.get_results,
        )
        self.send = async_to_streamed_response_wrapper(
            polls.send,
        )
