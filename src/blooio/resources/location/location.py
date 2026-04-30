# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .contacts import (
    ContactsResource,
    AsyncContactsResource,
    ContactsResourceWithRawResponse,
    AsyncContactsResourceWithRawResponse,
    ContactsResourceWithStreamingResponse,
    AsyncContactsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["LocationResource", "AsyncLocationResource"]


class LocationResource(SyncAPIResource):
    @cached_property
    def contacts(self) -> ContactsResource:
        """FindMy contact location tracking"""
        return ContactsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return LocationResourceWithStreamingResponse(self)


class AsyncLocationResource(AsyncAPIResource):
    @cached_property
    def contacts(self) -> AsyncContactsResource:
        """FindMy contact location tracking"""
        return AsyncContactsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Blooio/blooio-python-sdk#with_streaming_response
        """
        return AsyncLocationResourceWithStreamingResponse(self)


class LocationResourceWithRawResponse:
    def __init__(self, location: LocationResource) -> None:
        self._location = location

    @cached_property
    def contacts(self) -> ContactsResourceWithRawResponse:
        """FindMy contact location tracking"""
        return ContactsResourceWithRawResponse(self._location.contacts)


class AsyncLocationResourceWithRawResponse:
    def __init__(self, location: AsyncLocationResource) -> None:
        self._location = location

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        """FindMy contact location tracking"""
        return AsyncContactsResourceWithRawResponse(self._location.contacts)


class LocationResourceWithStreamingResponse:
    def __init__(self, location: LocationResource) -> None:
        self._location = location

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        """FindMy contact location tracking"""
        return ContactsResourceWithStreamingResponse(self._location.contacts)


class AsyncLocationResourceWithStreamingResponse:
    def __init__(self, location: AsyncLocationResource) -> None:
        self._location = location

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        """FindMy contact location tracking"""
        return AsyncContactsResourceWithStreamingResponse(self._location.contacts)
