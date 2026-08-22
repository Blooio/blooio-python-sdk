# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blooio import Blooio, AsyncBlooio
from tests.utils import assert_matches_type
from blooio.types import FacetimeInitiateCallResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFacetime:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_call(self, client: Blooio) -> None:
        facetime = client.facetime.initiate_call(
            handle="+15551234567",
        )
        assert_matches_type(FacetimeInitiateCallResponse, facetime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_call(self, client: Blooio) -> None:
        response = client.facetime.with_raw_response.initiate_call(
            handle="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        facetime = response.parse()
        assert_matches_type(FacetimeInitiateCallResponse, facetime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_call(self, client: Blooio) -> None:
        with client.facetime.with_streaming_response.initiate_call(
            handle="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            facetime = response.parse()
            assert_matches_type(FacetimeInitiateCallResponse, facetime, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFacetime:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_call(self, async_client: AsyncBlooio) -> None:
        facetime = await async_client.facetime.initiate_call(
            handle="+15551234567",
        )
        assert_matches_type(FacetimeInitiateCallResponse, facetime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_call(self, async_client: AsyncBlooio) -> None:
        response = await async_client.facetime.with_raw_response.initiate_call(
            handle="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        facetime = await response.parse()
        assert_matches_type(FacetimeInitiateCallResponse, facetime, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_call(self, async_client: AsyncBlooio) -> None:
        async with async_client.facetime.with_streaming_response.initiate_call(
            handle="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            facetime = await response.parse()
            assert_matches_type(FacetimeInitiateCallResponse, facetime, path=["response"])

        assert cast(Any, response.is_closed) is True
