# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.webhooks import log_list_params
from ...types.webhooks.log_list_response import LogListResponse
from ...types.webhooks.log_replay_response import LogReplayResponse

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    """View and replay webhook deliveries"""

    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def list(
        self,
        webhook_id: str,
        *,
        limit: int | Omit = omit,
        max_status: int | Omit = omit,
        min_status: int | Omit = omit,
        offset: int | Omit = omit,
        sort: Literal["asc", "desc"] | Omit = omit,
        status: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogListResponse:
        """
        List delivery logs for a specific webhook.

        Args:
          limit: Maximum number of items to return in a single response. Must be between 1 and
              200; defaults to 50. Use together with `offset` to page through large result
              sets.

          max_status: Maximum HTTP status code

          min_status: Minimum HTTP status code

          offset: Number of items to skip before returning results. Combine with `limit` for
              page-based pagination (e.g. `offset=50&limit=50` returns the second page).
              Defaults to 0.

          sort: Sort order by attempted time

          status: Filter by exact HTTP status code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._get(
            path_template("/webhooks/{webhook_id}/logs", webhook_id=webhook_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "max_status": max_status,
                        "min_status": min_status,
                        "offset": offset,
                        "sort": sort,
                        "status": status,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            cast_to=LogListResponse,
        )

    def replay(
        self,
        event_id: str,
        *,
        webhook_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogReplayResponse:
        """
        Re-send a webhook event to the configured URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._post(
            path_template("/webhooks/{webhook_id}/logs/{event_id}/replay", webhook_id=webhook_id, event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogReplayResponse,
        )


class AsyncLogsResource(AsyncAPIResource):
    """View and replay webhook deliveries"""

    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    async def list(
        self,
        webhook_id: str,
        *,
        limit: int | Omit = omit,
        max_status: int | Omit = omit,
        min_status: int | Omit = omit,
        offset: int | Omit = omit,
        sort: Literal["asc", "desc"] | Omit = omit,
        status: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogListResponse:
        """
        List delivery logs for a specific webhook.

        Args:
          limit: Maximum number of items to return in a single response. Must be between 1 and
              200; defaults to 50. Use together with `offset` to page through large result
              sets.

          max_status: Maximum HTTP status code

          min_status: Minimum HTTP status code

          offset: Number of items to skip before returning results. Combine with `limit` for
              page-based pagination (e.g. `offset=50&limit=50` returns the second page).
              Defaults to 0.

          sort: Sort order by attempted time

          status: Filter by exact HTTP status code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._get(
            path_template("/webhooks/{webhook_id}/logs", webhook_id=webhook_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "max_status": max_status,
                        "min_status": min_status,
                        "offset": offset,
                        "sort": sort,
                        "status": status,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            cast_to=LogListResponse,
        )

    async def replay(
        self,
        event_id: str,
        *,
        webhook_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogReplayResponse:
        """
        Re-send a webhook event to the configured URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._post(
            path_template("/webhooks/{webhook_id}/logs/{event_id}/replay", webhook_id=webhook_id, event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogReplayResponse,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_raw_response_wrapper(
            logs.list,
        )
        self.replay = to_raw_response_wrapper(
            logs.replay,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_raw_response_wrapper(
            logs.list,
        )
        self.replay = async_to_raw_response_wrapper(
            logs.replay,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_streamed_response_wrapper(
            logs.list,
        )
        self.replay = to_streamed_response_wrapper(
            logs.replay,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_streamed_response_wrapper(
            logs.list,
        )
        self.replay = async_to_streamed_response_wrapper(
            logs.replay,
        )
