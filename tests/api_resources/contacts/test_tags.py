# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blooio import Blooio, AsyncBlooio
from tests.utils import assert_matches_type
from blooio.types import DeleteResponse
from blooio.types.contacts import TagAddResponse, TagListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Blooio) -> None:
        tag = client.contacts.tags.list(
            "%2B15551234567",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Blooio) -> None:
        response = client.contacts.tags.with_raw_response.list(
            "%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Blooio) -> None:
        with client.contacts.tags.with_streaming_response.list(
            "%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.tags.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Blooio) -> None:
        tag = client.contacts.tags.add(
            contact_id="%2B15551234567",
            tags=["vip", "priority"],
        )
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Blooio) -> None:
        response = client.contacts.tags.with_raw_response.add(
            contact_id="%2B15551234567",
            tags=["vip", "priority"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Blooio) -> None:
        with client.contacts.tags.with_streaming_response.add(
            contact_id="%2B15551234567",
            tags=["vip", "priority"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagAddResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.tags.with_raw_response.add(
                contact_id="",
                tags=["vip", "priority"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Blooio) -> None:
        tag = client.contacts.tags.remove(
            tag="vip",
            contact_id="%2B15551234567",
        )
        assert_matches_type(DeleteResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Blooio) -> None:
        response = client.contacts.tags.with_raw_response.remove(
            tag="vip",
            contact_id="%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(DeleteResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Blooio) -> None:
        with client.contacts.tags.with_streaming_response.remove(
            tag="vip",
            contact_id="%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(DeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.tags.with_raw_response.remove(
                tag="vip",
                contact_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            client.contacts.tags.with_raw_response.remove(
                tag="",
                contact_id="%2B15551234567",
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBlooio) -> None:
        tag = await async_client.contacts.tags.list(
            "%2B15551234567",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBlooio) -> None:
        response = await async_client.contacts.tags.with_raw_response.list(
            "%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBlooio) -> None:
        async with async_client.contacts.tags.with_streaming_response.list(
            "%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.tags.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncBlooio) -> None:
        tag = await async_client.contacts.tags.add(
            contact_id="%2B15551234567",
            tags=["vip", "priority"],
        )
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncBlooio) -> None:
        response = await async_client.contacts.tags.with_raw_response.add(
            contact_id="%2B15551234567",
            tags=["vip", "priority"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncBlooio) -> None:
        async with async_client.contacts.tags.with_streaming_response.add(
            contact_id="%2B15551234567",
            tags=["vip", "priority"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagAddResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.tags.with_raw_response.add(
                contact_id="",
                tags=["vip", "priority"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncBlooio) -> None:
        tag = await async_client.contacts.tags.remove(
            tag="vip",
            contact_id="%2B15551234567",
        )
        assert_matches_type(DeleteResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncBlooio) -> None:
        response = await async_client.contacts.tags.with_raw_response.remove(
            tag="vip",
            contact_id="%2B15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(DeleteResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncBlooio) -> None:
        async with async_client.contacts.tags.with_streaming_response.remove(
            tag="vip",
            contact_id="%2B15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(DeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.tags.with_raw_response.remove(
                tag="vip",
                contact_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            await async_client.contacts.tags.with_raw_response.remove(
                tag="",
                contact_id="%2B15551234567",
            )
