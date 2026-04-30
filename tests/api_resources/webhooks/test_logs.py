# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blooio import Blooio, AsyncBlooio
from tests.utils import assert_matches_type
from blooio.types.webhooks import LogListResponse, LogReplayResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Blooio) -> None:
        log = client.webhooks.logs.list(
            webhook_id="wh_abc123def456",
        )
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Blooio) -> None:
        log = client.webhooks.logs.list(
            webhook_id="wh_abc123def456",
            limit=1,
            max_status=0,
            min_status=0,
            offset=0,
            sort="asc",
            status=0,
        )
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Blooio) -> None:
        response = client.webhooks.logs.with_raw_response.list(
            webhook_id="wh_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Blooio) -> None:
        with client.webhooks.logs.with_streaming_response.list(
            webhook_id="wh_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogListResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.logs.with_raw_response.list(
                webhook_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replay(self, client: Blooio) -> None:
        log = client.webhooks.logs.replay(
            event_id="eventId",
            webhook_id="wh_abc123def456",
        )
        assert_matches_type(LogReplayResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replay(self, client: Blooio) -> None:
        response = client.webhooks.logs.with_raw_response.replay(
            event_id="eventId",
            webhook_id="wh_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogReplayResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replay(self, client: Blooio) -> None:
        with client.webhooks.logs.with_streaming_response.replay(
            event_id="eventId",
            webhook_id="wh_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogReplayResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replay(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.logs.with_raw_response.replay(
                event_id="eventId",
                webhook_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.webhooks.logs.with_raw_response.replay(
                event_id="",
                webhook_id="wh_abc123def456",
            )


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBlooio) -> None:
        log = await async_client.webhooks.logs.list(
            webhook_id="wh_abc123def456",
        )
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBlooio) -> None:
        log = await async_client.webhooks.logs.list(
            webhook_id="wh_abc123def456",
            limit=1,
            max_status=0,
            min_status=0,
            offset=0,
            sort="asc",
            status=0,
        )
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBlooio) -> None:
        response = await async_client.webhooks.logs.with_raw_response.list(
            webhook_id="wh_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBlooio) -> None:
        async with async_client.webhooks.logs.with_streaming_response.list(
            webhook_id="wh_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogListResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.logs.with_raw_response.list(
                webhook_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replay(self, async_client: AsyncBlooio) -> None:
        log = await async_client.webhooks.logs.replay(
            event_id="eventId",
            webhook_id="wh_abc123def456",
        )
        assert_matches_type(LogReplayResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replay(self, async_client: AsyncBlooio) -> None:
        response = await async_client.webhooks.logs.with_raw_response.replay(
            event_id="eventId",
            webhook_id="wh_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogReplayResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replay(self, async_client: AsyncBlooio) -> None:
        async with async_client.webhooks.logs.with_streaming_response.replay(
            event_id="eventId",
            webhook_id="wh_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogReplayResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replay(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.logs.with_raw_response.replay(
                event_id="eventId",
                webhook_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.webhooks.logs.with_raw_response.replay(
                event_id="",
                webhook_id="wh_abc123def456",
            )
