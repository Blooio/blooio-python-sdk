# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blooio import Blooio, AsyncBlooio
from tests.utils import assert_matches_type
from blooio.types import (
    Contact,
    DeleteResponse,
    ContactListResponse,
    ContactCheckCapabilitiesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Blooio) -> None:
        contact = client.contacts.create(
            identifier="+15551234567",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Blooio) -> None:
        contact = client.contacts.create(
            identifier="+15551234567",
            name="John Doe",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Blooio) -> None:
        response = client.contacts.with_raw_response.create(
            identifier="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Blooio) -> None:
        with client.contacts.with_streaming_response.create(
            identifier="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Blooio) -> None:
        contact = client.contacts.retrieve(
            "%2B15551234567",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Blooio) -> None:
        response = client.contacts.with_raw_response.retrieve(
            "%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Blooio) -> None:
        with client.contacts.with_streaming_response.retrieve(
            "%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Blooio) -> None:
        contact = client.contacts.update(
            contact_id="%2B15551234567",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Blooio) -> None:
        contact = client.contacts.update(
            contact_id="%2B15551234567",
            name="Jane Doe",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Blooio) -> None:
        response = client.contacts.with_raw_response.update(
            contact_id="%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Blooio) -> None:
        with client.contacts.with_streaming_response.update(
            contact_id="%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.with_raw_response.update(
                contact_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Blooio) -> None:
        contact = client.contacts.list()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Blooio) -> None:
        contact = client.contacts.list(
            limit=1,
            offset=0,
            q="q",
            sort="recent",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Blooio) -> None:
        response = client.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Blooio) -> None:
        with client.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Blooio) -> None:
        contact = client.contacts.delete(
            "%2B15551234567",
        )
        assert_matches_type(DeleteResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Blooio) -> None:
        response = client.contacts.with_raw_response.delete(
            "%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(DeleteResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Blooio) -> None:
        with client.contacts.with_streaming_response.delete(
            "%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(DeleteResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_capabilities(self, client: Blooio) -> None:
        contact = client.contacts.check_capabilities(
            "%2B15551234567",
        )
        assert_matches_type(ContactCheckCapabilitiesResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_capabilities(self, client: Blooio) -> None:
        response = client.contacts.with_raw_response.check_capabilities(
            "%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactCheckCapabilitiesResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_capabilities(self, client: Blooio) -> None:
        with client.contacts.with_streaming_response.check_capabilities(
            "%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactCheckCapabilitiesResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_check_capabilities(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.with_raw_response.check_capabilities(
                "",
            )


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBlooio) -> None:
        contact = await async_client.contacts.create(
            identifier="+15551234567",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBlooio) -> None:
        contact = await async_client.contacts.create(
            identifier="+15551234567",
            name="John Doe",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBlooio) -> None:
        response = await async_client.contacts.with_raw_response.create(
            identifier="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBlooio) -> None:
        async with async_client.contacts.with_streaming_response.create(
            identifier="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBlooio) -> None:
        contact = await async_client.contacts.retrieve(
            "%2B15551234567",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBlooio) -> None:
        response = await async_client.contacts.with_raw_response.retrieve(
            "%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBlooio) -> None:
        async with async_client.contacts.with_streaming_response.retrieve(
            "%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBlooio) -> None:
        contact = await async_client.contacts.update(
            contact_id="%2B15551234567",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBlooio) -> None:
        contact = await async_client.contacts.update(
            contact_id="%2B15551234567",
            name="Jane Doe",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBlooio) -> None:
        response = await async_client.contacts.with_raw_response.update(
            contact_id="%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBlooio) -> None:
        async with async_client.contacts.with_streaming_response.update(
            contact_id="%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.with_raw_response.update(
                contact_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBlooio) -> None:
        contact = await async_client.contacts.list()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBlooio) -> None:
        contact = await async_client.contacts.list(
            limit=1,
            offset=0,
            q="q",
            sort="recent",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBlooio) -> None:
        response = await async_client.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBlooio) -> None:
        async with async_client.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBlooio) -> None:
        contact = await async_client.contacts.delete(
            "%2B15551234567",
        )
        assert_matches_type(DeleteResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBlooio) -> None:
        response = await async_client.contacts.with_raw_response.delete(
            "%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(DeleteResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBlooio) -> None:
        async with async_client.contacts.with_streaming_response.delete(
            "%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(DeleteResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_capabilities(self, async_client: AsyncBlooio) -> None:
        contact = await async_client.contacts.check_capabilities(
            "%2B15551234567",
        )
        assert_matches_type(ContactCheckCapabilitiesResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_capabilities(self, async_client: AsyncBlooio) -> None:
        response = await async_client.contacts.with_raw_response.check_capabilities(
            "%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactCheckCapabilitiesResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_capabilities(self, async_client: AsyncBlooio) -> None:
        async with async_client.contacts.with_streaming_response.check_capabilities(
            "%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactCheckCapabilitiesResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_check_capabilities(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.with_raw_response.check_capabilities(
                "",
            )
