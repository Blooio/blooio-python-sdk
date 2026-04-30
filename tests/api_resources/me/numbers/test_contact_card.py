# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blooio import Blooio, AsyncBlooio
from tests.utils import assert_matches_type
from blooio.types.me.numbers import ContactCardUpdateResponse, ContactCardRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContactCard:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Blooio) -> None:
        contact_card = client.me.numbers.contact_card.retrieve(
            "number",
        )
        assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Blooio) -> None:
        response = client.me.numbers.contact_card.with_raw_response.retrieve(
            "number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_card = response.parse()
        assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Blooio) -> None:
        with client.me.numbers.contact_card.with_streaming_response.retrieve(
            "number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_card = response.parse()
            assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            client.me.numbers.contact_card.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Blooio) -> None:
        contact_card = client.me.numbers.contact_card.update(
            number="number",
        )
        assert_matches_type(ContactCardUpdateResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Blooio) -> None:
        contact_card = client.me.numbers.contact_card.update(
            number="number",
            avatar="avatar",
            first_name="first_name",
            last_name="last_name",
            sharing={
                "audience": 0,
                "enabled": True,
                "name_format": 0,
            },
        )
        assert_matches_type(ContactCardUpdateResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Blooio) -> None:
        response = client.me.numbers.contact_card.with_raw_response.update(
            number="number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_card = response.parse()
        assert_matches_type(ContactCardUpdateResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Blooio) -> None:
        with client.me.numbers.contact_card.with_streaming_response.update(
            number="number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_card = response.parse()
            assert_matches_type(ContactCardUpdateResponse, contact_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            client.me.numbers.contact_card.with_raw_response.update(
                number="",
            )


class TestAsyncContactCard:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBlooio) -> None:
        contact_card = await async_client.me.numbers.contact_card.retrieve(
            "number",
        )
        assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBlooio) -> None:
        response = await async_client.me.numbers.contact_card.with_raw_response.retrieve(
            "number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_card = await response.parse()
        assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBlooio) -> None:
        async with async_client.me.numbers.contact_card.with_streaming_response.retrieve(
            "number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_card = await response.parse()
            assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            await async_client.me.numbers.contact_card.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBlooio) -> None:
        contact_card = await async_client.me.numbers.contact_card.update(
            number="number",
        )
        assert_matches_type(ContactCardUpdateResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBlooio) -> None:
        contact_card = await async_client.me.numbers.contact_card.update(
            number="number",
            avatar="avatar",
            first_name="first_name",
            last_name="last_name",
            sharing={
                "audience": 0,
                "enabled": True,
                "name_format": 0,
            },
        )
        assert_matches_type(ContactCardUpdateResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBlooio) -> None:
        response = await async_client.me.numbers.contact_card.with_raw_response.update(
            number="number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_card = await response.parse()
        assert_matches_type(ContactCardUpdateResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBlooio) -> None:
        async with async_client.me.numbers.contact_card.with_streaming_response.update(
            number="number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_card = await response.parse()
            assert_matches_type(ContactCardUpdateResponse, contact_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            await async_client.me.numbers.contact_card.with_raw_response.update(
                number="",
            )
