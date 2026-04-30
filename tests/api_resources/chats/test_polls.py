# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blooio import Blooio, AsyncBlooio
from tests.utils import assert_matches_type
from blooio.types.chats import PollSendResponse, PollGetResultsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_results(self, client: Blooio) -> None:
        poll = client.chats.polls.get_results(
            poll_id="pollId",
            chat_id="chatId",
        )
        assert_matches_type(PollGetResultsResponse, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_results(self, client: Blooio) -> None:
        response = client.chats.polls.with_raw_response.get_results(
            poll_id="pollId",
            chat_id="chatId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = response.parse()
        assert_matches_type(PollGetResultsResponse, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_results(self, client: Blooio) -> None:
        with client.chats.polls.with_streaming_response.get_results(
            poll_id="pollId",
            chat_id="chatId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = response.parse()
            assert_matches_type(PollGetResultsResponse, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_results(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.polls.with_raw_response.get_results(
                poll_id="pollId",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `poll_id` but received ''"):
            client.chats.polls.with_raw_response.get_results(
                poll_id="",
                chat_id="chatId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: Blooio) -> None:
        poll = client.chats.polls.send(
            chat_id="chatId",
            options=["string", "string"],
        )
        assert_matches_type(PollSendResponse, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Blooio) -> None:
        poll = client.chats.polls.send(
            chat_id="chatId",
            options=["string", "string"],
            title="title",
        )
        assert_matches_type(PollSendResponse, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Blooio) -> None:
        response = client.chats.polls.with_raw_response.send(
            chat_id="chatId",
            options=["string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = response.parse()
        assert_matches_type(PollSendResponse, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Blooio) -> None:
        with client.chats.polls.with_streaming_response.send(
            chat_id="chatId",
            options=["string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = response.parse()
            assert_matches_type(PollSendResponse, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.polls.with_raw_response.send(
                chat_id="",
                options=["string", "string"],
            )


class TestAsyncPolls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_results(self, async_client: AsyncBlooio) -> None:
        poll = await async_client.chats.polls.get_results(
            poll_id="pollId",
            chat_id="chatId",
        )
        assert_matches_type(PollGetResultsResponse, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_results(self, async_client: AsyncBlooio) -> None:
        response = await async_client.chats.polls.with_raw_response.get_results(
            poll_id="pollId",
            chat_id="chatId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = await response.parse()
        assert_matches_type(PollGetResultsResponse, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_results(self, async_client: AsyncBlooio) -> None:
        async with async_client.chats.polls.with_streaming_response.get_results(
            poll_id="pollId",
            chat_id="chatId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = await response.parse()
            assert_matches_type(PollGetResultsResponse, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_results(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.polls.with_raw_response.get_results(
                poll_id="pollId",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `poll_id` but received ''"):
            await async_client.chats.polls.with_raw_response.get_results(
                poll_id="",
                chat_id="chatId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncBlooio) -> None:
        poll = await async_client.chats.polls.send(
            chat_id="chatId",
            options=["string", "string"],
        )
        assert_matches_type(PollSendResponse, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncBlooio) -> None:
        poll = await async_client.chats.polls.send(
            chat_id="chatId",
            options=["string", "string"],
            title="title",
        )
        assert_matches_type(PollSendResponse, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncBlooio) -> None:
        response = await async_client.chats.polls.with_raw_response.send(
            chat_id="chatId",
            options=["string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = await response.parse()
        assert_matches_type(PollSendResponse, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncBlooio) -> None:
        async with async_client.chats.polls.with_streaming_response.send(
            chat_id="chatId",
            options=["string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = await response.parse()
            assert_matches_type(PollSendResponse, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.polls.with_raw_response.send(
                chat_id="",
                options=["string", "string"],
            )
