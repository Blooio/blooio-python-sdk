# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .webhook import (
    WebhookResource,
    AsyncWebhookResource,
    WebhookResourceWithRawResponse,
    AsyncWebhookResourceWithRawResponse,
    WebhookResourceWithStreamingResponse,
    AsyncWebhookResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
    @cached_property
    def webhook(self) -> WebhookResource:
        """Account-level configuration"""
        return WebhookResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)


class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def webhook(self) -> AsyncWebhookResource:
        """Account-level configuration"""
        return AsyncWebhookResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

    @cached_property
    def webhook(self) -> WebhookResourceWithRawResponse:
        """Account-level configuration"""
        return WebhookResourceWithRawResponse(self._config.webhook)


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

    @cached_property
    def webhook(self) -> AsyncWebhookResourceWithRawResponse:
        """Account-level configuration"""
        return AsyncWebhookResourceWithRawResponse(self._config.webhook)


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

    @cached_property
    def webhook(self) -> WebhookResourceWithStreamingResponse:
        """Account-level configuration"""
        return WebhookResourceWithStreamingResponse(self._config.webhook)


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

    @cached_property
    def webhook(self) -> AsyncWebhookResourceWithStreamingResponse:
        """Account-level configuration"""
        return AsyncWebhookResourceWithStreamingResponse(self._config.webhook)
