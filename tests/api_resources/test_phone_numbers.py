# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blooio import Blooio, AsyncBlooio
from tests.utils import assert_matches_type
from blooio.types import PhoneNumberBatchCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_create(self, client: Blooio) -> None:
        phone_number = client.phone_numbers.batch_create(
            numbers=["+12125551234", "+14155551234", "+18582849901"],
        )
        assert_matches_type(PhoneNumberBatchCreateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_create(self, client: Blooio) -> None:
        response = client.phone_numbers.with_raw_response.batch_create(
            numbers=["+12125551234", "+14155551234", "+18582849901"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberBatchCreateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_create(self, client: Blooio) -> None:
        with client.phone_numbers.with_streaming_response.batch_create(
            numbers=["+12125551234", "+14155551234", "+18582849901"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberBatchCreateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_create(self, async_client: AsyncBlooio) -> None:
        phone_number = await async_client.phone_numbers.batch_create(
            numbers=["+12125551234", "+14155551234", "+18582849901"],
        )
        assert_matches_type(PhoneNumberBatchCreateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_create(self, async_client: AsyncBlooio) -> None:
        response = await async_client.phone_numbers.with_raw_response.batch_create(
            numbers=["+12125551234", "+14155551234", "+18582849901"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberBatchCreateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_create(self, async_client: AsyncBlooio) -> None:
        async with async_client.phone_numbers.with_streaming_response.batch_create(
            numbers=["+12125551234", "+14155551234", "+18582849901"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberBatchCreateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True
