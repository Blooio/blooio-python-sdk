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
from ...types.webhooks.secret_rotate_response import SecretRotateResponse

__all__ = ["SecretResource", "AsyncSecretResource"]


class SecretResource(SyncAPIResource):
    """Manage webhook subscriptions"""

    @cached_property
    def with_raw_response(self) -> SecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return SecretResourceWithStreamingResponse(self)

    def rotate(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRotateResponse:
        """Generate a new signing secret for the webhook.

        The new secret is returned only
        once in this response - store it securely. The old secret becomes invalid
        immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._post(
            path_template("/webhooks/{webhook_id}/secret/rotate", webhook_id=webhook_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretRotateResponse,
        )


class AsyncSecretResource(AsyncAPIResource):
    """Manage webhook subscriptions"""

    @cached_property
    def with_raw_response(self) -> AsyncSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncSecretResourceWithStreamingResponse(self)

    async def rotate(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRotateResponse:
        """Generate a new signing secret for the webhook.

        The new secret is returned only
        once in this response - store it securely. The old secret becomes invalid
        immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._post(
            path_template("/webhooks/{webhook_id}/secret/rotate", webhook_id=webhook_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretRotateResponse,
        )


class SecretResourceWithRawResponse:
    def __init__(self, secret: SecretResource) -> None:
        self._secret = secret

        self.rotate = to_raw_response_wrapper(
            secret.rotate,
        )


class AsyncSecretResourceWithRawResponse:
    def __init__(self, secret: AsyncSecretResource) -> None:
        self._secret = secret

        self.rotate = async_to_raw_response_wrapper(
            secret.rotate,
        )


class SecretResourceWithStreamingResponse:
    def __init__(self, secret: SecretResource) -> None:
        self._secret = secret

        self.rotate = to_streamed_response_wrapper(
            secret.rotate,
        )


class AsyncSecretResourceWithStreamingResponse:
    def __init__(self, secret: AsyncSecretResource) -> None:
        self._secret = secret

        self.rotate = async_to_streamed_response_wrapper(
            secret.rotate,
        )
