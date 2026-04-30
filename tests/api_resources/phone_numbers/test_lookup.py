# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blooio import Blooio, AsyncBlooio
from tests.utils import assert_matches_type
from blooio.types.phone_numbers import PhoneNumberLookupResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLookup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Blooio) -> None:
        lookup = client.phone_numbers.lookup.create(
            number="+12125551234",
        )
        assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Blooio) -> None:
        response = client.phone_numbers.lookup.with_raw_response.create(
            number="+12125551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lookup = response.parse()
        assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Blooio) -> None:
        with client.phone_numbers.lookup.with_streaming_response.create(
            number="+12125551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lookup = response.parse()
            assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Blooio) -> None:
        lookup = client.phone_numbers.lookup.retrieve(
            number="+12125551234",
        )
        assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Blooio) -> None:
        response = client.phone_numbers.lookup.with_raw_response.retrieve(
            number="+12125551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lookup = response.parse()
        assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Blooio) -> None:
        with client.phone_numbers.lookup.with_streaming_response.retrieve(
            number="+12125551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lookup = response.parse()
            assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLookup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBlooio) -> None:
        lookup = await async_client.phone_numbers.lookup.create(
            number="+12125551234",
        )
        assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBlooio) -> None:
        response = await async_client.phone_numbers.lookup.with_raw_response.create(
            number="+12125551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lookup = await response.parse()
        assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBlooio) -> None:
        async with async_client.phone_numbers.lookup.with_streaming_response.create(
            number="+12125551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lookup = await response.parse()
            assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBlooio) -> None:
        lookup = await async_client.phone_numbers.lookup.retrieve(
            number="+12125551234",
        )
        assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBlooio) -> None:
        response = await async_client.phone_numbers.lookup.with_raw_response.retrieve(
            number="+12125551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lookup = await response.parse()
        assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBlooio) -> None:
        async with async_client.phone_numbers.lookup.with_streaming_response.retrieve(
            number="+12125551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lookup = await response.parse()
            assert_matches_type(PhoneNumberLookupResult, lookup, path=["response"])

        assert cast(Any, response.is_closed) is True
