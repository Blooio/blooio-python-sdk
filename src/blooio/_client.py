# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import BlooioError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import me, chats, groups, contacts, facetime, location, webhooks, phone_numbers
    from .resources.me.me import MeResource, AsyncMeResource
    from .resources.facetime import FacetimeResource, AsyncFacetimeResource
    from .resources.chats.chats import ChatsResource, AsyncChatsResource
    from .resources.groups.groups import GroupsResource, AsyncGroupsResource
    from .resources.contacts.contacts import ContactsResource, AsyncContactsResource
    from .resources.location.location import LocationResource, AsyncLocationResource
    from .resources.webhooks.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.phone_numbers.phone_numbers import PhoneNumbersResource, AsyncPhoneNumbersResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Blooio", "AsyncBlooio", "Client", "AsyncClient"]


class Blooio(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Blooio client instance.

        This automatically infers the `api_key` argument from the `BLOOIO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BLOOIO_API_KEY")
        if api_key is None:
            raise BlooioError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BLOOIO_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BLOOIO_BASE_URL")
        if base_url is None:
            base_url = f"https://backend.blooio.com/v2/api"

        custom_headers_env = os.environ.get("BLOOIO_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def me(self) -> MeResource:
        """Authentication and account information"""
        from .resources.me import MeResource

        return MeResource(self)

    @cached_property
    def contacts(self) -> ContactsResource:
        """Manage contacts (phone numbers and emails)"""
        from .resources.contacts import ContactsResource

        return ContactsResource(self)

    @cached_property
    def location(self) -> LocationResource:
        from .resources.location import LocationResource

        return LocationResource(self)

    @cached_property
    def facetime(self) -> FacetimeResource:
        """Initiate FaceTime calls"""
        from .resources.facetime import FacetimeResource

        return FacetimeResource(self)

    @cached_property
    def groups(self) -> GroupsResource:
        """Manage contact groups"""
        from .resources.groups import GroupsResource

        return GroupsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Manage webhook subscriptions"""
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def chats(self) -> ChatsResource:
        from .resources.chats import ChatsResource

        return ChatsResource(self)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        from .resources.phone_numbers import PhoneNumbersResource

        return PhoneNumbersResource(self)

    @cached_property
    def with_raw_response(self) -> BlooioWithRawResponse:
        return BlooioWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlooioWithStreamedResponse:
        return BlooioWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        headers: dict[str, str] = {}
        if security.get("bearer_auth", False):
            for key, value in self._bearer_auth.items():
                headers.setdefault(key, value)
        return headers

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBlooio(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBlooio client instance.

        This automatically infers the `api_key` argument from the `BLOOIO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BLOOIO_API_KEY")
        if api_key is None:
            raise BlooioError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BLOOIO_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BLOOIO_BASE_URL")
        if base_url is None:
            base_url = f"https://backend.blooio.com/v2/api"

        custom_headers_env = os.environ.get("BLOOIO_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def me(self) -> AsyncMeResource:
        """Authentication and account information"""
        from .resources.me import AsyncMeResource

        return AsyncMeResource(self)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        """Manage contacts (phone numbers and emails)"""
        from .resources.contacts import AsyncContactsResource

        return AsyncContactsResource(self)

    @cached_property
    def location(self) -> AsyncLocationResource:
        from .resources.location import AsyncLocationResource

        return AsyncLocationResource(self)

    @cached_property
    def facetime(self) -> AsyncFacetimeResource:
        """Initiate FaceTime calls"""
        from .resources.facetime import AsyncFacetimeResource

        return AsyncFacetimeResource(self)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        """Manage contact groups"""
        from .resources.groups import AsyncGroupsResource

        return AsyncGroupsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Manage webhook subscriptions"""
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def chats(self) -> AsyncChatsResource:
        from .resources.chats import AsyncChatsResource

        return AsyncChatsResource(self)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        from .resources.phone_numbers import AsyncPhoneNumbersResource

        return AsyncPhoneNumbersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncBlooioWithRawResponse:
        return AsyncBlooioWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlooioWithStreamedResponse:
        return AsyncBlooioWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        headers: dict[str, str] = {}
        if security.get("bearer_auth", False):
            for key, value in self._bearer_auth.items():
                headers.setdefault(key, value)
        return headers

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BlooioWithRawResponse:
    _client: Blooio

    def __init__(self, client: Blooio) -> None:
        self._client = client

    @cached_property
    def me(self) -> me.MeResourceWithRawResponse:
        """Authentication and account information"""
        from .resources.me import MeResourceWithRawResponse

        return MeResourceWithRawResponse(self._client.me)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithRawResponse:
        """Manage contacts (phone numbers and emails)"""
        from .resources.contacts import ContactsResourceWithRawResponse

        return ContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def location(self) -> location.LocationResourceWithRawResponse:
        from .resources.location import LocationResourceWithRawResponse

        return LocationResourceWithRawResponse(self._client.location)

    @cached_property
    def facetime(self) -> facetime.FacetimeResourceWithRawResponse:
        """Initiate FaceTime calls"""
        from .resources.facetime import FacetimeResourceWithRawResponse

        return FacetimeResourceWithRawResponse(self._client.facetime)

    @cached_property
    def groups(self) -> groups.GroupsResourceWithRawResponse:
        """Manage contact groups"""
        from .resources.groups import GroupsResourceWithRawResponse

        return GroupsResourceWithRawResponse(self._client.groups)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        """Manage webhook subscriptions"""
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def chats(self) -> chats.ChatsResourceWithRawResponse:
        from .resources.chats import ChatsResourceWithRawResponse

        return ChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def phone_numbers(self) -> phone_numbers.PhoneNumbersResourceWithRawResponse:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        from .resources.phone_numbers import PhoneNumbersResourceWithRawResponse

        return PhoneNumbersResourceWithRawResponse(self._client.phone_numbers)


class AsyncBlooioWithRawResponse:
    _client: AsyncBlooio

    def __init__(self, client: AsyncBlooio) -> None:
        self._client = client

    @cached_property
    def me(self) -> me.AsyncMeResourceWithRawResponse:
        """Authentication and account information"""
        from .resources.me import AsyncMeResourceWithRawResponse

        return AsyncMeResourceWithRawResponse(self._client.me)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithRawResponse:
        """Manage contacts (phone numbers and emails)"""
        from .resources.contacts import AsyncContactsResourceWithRawResponse

        return AsyncContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def location(self) -> location.AsyncLocationResourceWithRawResponse:
        from .resources.location import AsyncLocationResourceWithRawResponse

        return AsyncLocationResourceWithRawResponse(self._client.location)

    @cached_property
    def facetime(self) -> facetime.AsyncFacetimeResourceWithRawResponse:
        """Initiate FaceTime calls"""
        from .resources.facetime import AsyncFacetimeResourceWithRawResponse

        return AsyncFacetimeResourceWithRawResponse(self._client.facetime)

    @cached_property
    def groups(self) -> groups.AsyncGroupsResourceWithRawResponse:
        """Manage contact groups"""
        from .resources.groups import AsyncGroupsResourceWithRawResponse

        return AsyncGroupsResourceWithRawResponse(self._client.groups)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        """Manage webhook subscriptions"""
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithRawResponse:
        from .resources.chats import AsyncChatsResourceWithRawResponse

        return AsyncChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def phone_numbers(self) -> phone_numbers.AsyncPhoneNumbersResourceWithRawResponse:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        from .resources.phone_numbers import AsyncPhoneNumbersResourceWithRawResponse

        return AsyncPhoneNumbersResourceWithRawResponse(self._client.phone_numbers)


class BlooioWithStreamedResponse:
    _client: Blooio

    def __init__(self, client: Blooio) -> None:
        self._client = client

    @cached_property
    def me(self) -> me.MeResourceWithStreamingResponse:
        """Authentication and account information"""
        from .resources.me import MeResourceWithStreamingResponse

        return MeResourceWithStreamingResponse(self._client.me)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithStreamingResponse:
        """Manage contacts (phone numbers and emails)"""
        from .resources.contacts import ContactsResourceWithStreamingResponse

        return ContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def location(self) -> location.LocationResourceWithStreamingResponse:
        from .resources.location import LocationResourceWithStreamingResponse

        return LocationResourceWithStreamingResponse(self._client.location)

    @cached_property
    def facetime(self) -> facetime.FacetimeResourceWithStreamingResponse:
        """Initiate FaceTime calls"""
        from .resources.facetime import FacetimeResourceWithStreamingResponse

        return FacetimeResourceWithStreamingResponse(self._client.facetime)

    @cached_property
    def groups(self) -> groups.GroupsResourceWithStreamingResponse:
        """Manage contact groups"""
        from .resources.groups import GroupsResourceWithStreamingResponse

        return GroupsResourceWithStreamingResponse(self._client.groups)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        """Manage webhook subscriptions"""
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def chats(self) -> chats.ChatsResourceWithStreamingResponse:
        from .resources.chats import ChatsResourceWithStreamingResponse

        return ChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def phone_numbers(self) -> phone_numbers.PhoneNumbersResourceWithStreamingResponse:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        from .resources.phone_numbers import PhoneNumbersResourceWithStreamingResponse

        return PhoneNumbersResourceWithStreamingResponse(self._client.phone_numbers)


class AsyncBlooioWithStreamedResponse:
    _client: AsyncBlooio

    def __init__(self, client: AsyncBlooio) -> None:
        self._client = client

    @cached_property
    def me(self) -> me.AsyncMeResourceWithStreamingResponse:
        """Authentication and account information"""
        from .resources.me import AsyncMeResourceWithStreamingResponse

        return AsyncMeResourceWithStreamingResponse(self._client.me)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithStreamingResponse:
        """Manage contacts (phone numbers and emails)"""
        from .resources.contacts import AsyncContactsResourceWithStreamingResponse

        return AsyncContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def location(self) -> location.AsyncLocationResourceWithStreamingResponse:
        from .resources.location import AsyncLocationResourceWithStreamingResponse

        return AsyncLocationResourceWithStreamingResponse(self._client.location)

    @cached_property
    def facetime(self) -> facetime.AsyncFacetimeResourceWithStreamingResponse:
        """Initiate FaceTime calls"""
        from .resources.facetime import AsyncFacetimeResourceWithStreamingResponse

        return AsyncFacetimeResourceWithStreamingResponse(self._client.facetime)

    @cached_property
    def groups(self) -> groups.AsyncGroupsResourceWithStreamingResponse:
        """Manage contact groups"""
        from .resources.groups import AsyncGroupsResourceWithStreamingResponse

        return AsyncGroupsResourceWithStreamingResponse(self._client.groups)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        """Manage webhook subscriptions"""
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithStreamingResponse:
        from .resources.chats import AsyncChatsResourceWithStreamingResponse

        return AsyncChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def phone_numbers(self) -> phone_numbers.AsyncPhoneNumbersResourceWithStreamingResponse:
        """Phone number validation, formatting, and NANPA geocoding.

        Requires an Enterprise plan (Dedicated Enterprise).
        """
        from .resources.phone_numbers import AsyncPhoneNumbersResourceWithStreamingResponse

        return AsyncPhoneNumbersResourceWithStreamingResponse(self._client.phone_numbers)


Client = Blooio

AsyncClient = AsyncBlooio
