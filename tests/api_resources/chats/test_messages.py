# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blooio import Blooio, AsyncBlooio
from tests.utils import assert_matches_type
from blooio.types.chats import (
    MessageListResponse,
    MessageSendResponse,
    MessageReactResponse,
    MessageRetrieveResponse,
    MessageGetStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Blooio) -> None:
        message = client.chats.messages.retrieve(
            message_id="msg_abc123def456",
            chat_id="chatId",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Blooio) -> None:
        response = client.chats.messages.with_raw_response.retrieve(
            message_id="msg_abc123def456",
            chat_id="chatId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Blooio) -> None:
        with client.chats.messages.with_streaming_response.retrieve(
            message_id="msg_abc123def456",
            chat_id="chatId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.retrieve(
                message_id="msg_abc123def456",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.chats.messages.with_raw_response.retrieve(
                message_id="",
                chat_id="chatId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Blooio) -> None:
        message = client.chats.messages.list(
            chat_id="chatId",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Blooio) -> None:
        message = client.chats.messages.list(
            chat_id="chatId",
            direction="inbound",
            limit=1,
            offset=0,
            since=0,
            sort="asc",
            until=0,
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Blooio) -> None:
        response = client.chats.messages.with_raw_response.list(
            chat_id="chatId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Blooio) -> None:
        with client.chats.messages.with_streaming_response.list(
            chat_id="chatId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.list(
                chat_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Blooio) -> None:
        message = client.chats.messages.get_status(
            message_id="msg_abc123def456",
            chat_id="chatId",
        )
        assert_matches_type(MessageGetStatusResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Blooio) -> None:
        response = client.chats.messages.with_raw_response.get_status(
            message_id="msg_abc123def456",
            chat_id="chatId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageGetStatusResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Blooio) -> None:
        with client.chats.messages.with_streaming_response.get_status(
            message_id="msg_abc123def456",
            chat_id="chatId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageGetStatusResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.get_status(
                message_id="msg_abc123def456",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.chats.messages.with_raw_response.get_status(
                message_id="",
                chat_id="chatId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_react(self, client: Blooio) -> None:
        message = client.chats.messages.react(
            message_id="messageId",
            chat_id="chatId",
            reaction="+love",
        )
        assert_matches_type(MessageReactResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_react_with_all_params(self, client: Blooio) -> None:
        message = client.chats.messages.react(
            message_id="messageId",
            chat_id="chatId",
            reaction="+love",
            direction="inbound",
        )
        assert_matches_type(MessageReactResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_react(self, client: Blooio) -> None:
        response = client.chats.messages.with_raw_response.react(
            message_id="messageId",
            chat_id="chatId",
            reaction="+love",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageReactResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_react(self, client: Blooio) -> None:
        with client.chats.messages.with_streaming_response.react(
            message_id="messageId",
            chat_id="chatId",
            reaction="+love",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageReactResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_react(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.react(
                message_id="messageId",
                chat_id="",
                reaction="+love",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.chats.messages.with_raw_response.react(
                message_id="",
                chat_id="chatId",
                reaction="+love",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: Blooio) -> None:
        message = client.chats.messages.send(
            chat_id="chatId",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Blooio) -> None:
        message = client.chats.messages.send(
            chat_id="chatId",
            attachments=["string"],
            effect="slam",
            format="plain",
            from_number="from_number",
            link_preview={
                "image_url": "https://example.com",
                "title": "title",
            },
            parts=[
                {
                    "link_preview": {
                        "image_url": "https://example.com",
                        "title": "title",
                    },
                    "mention": "mention",
                    "name": "name",
                    "text": "text",
                    "url": "url",
                }
            ],
            reply_to={
                "guid": "guid",
                "message_id": "message_id",
                "part_index": 0,
            },
            share_contact=True,
            text="string",
            use_typing_indicator=True,
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Blooio) -> None:
        response = client.chats.messages.with_raw_response.send(
            chat_id="chatId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Blooio) -> None:
        with client.chats.messages.with_streaming_response.send(
            chat_id="chatId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.send(
                chat_id="",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBlooio) -> None:
        message = await async_client.chats.messages.retrieve(
            message_id="msg_abc123def456",
            chat_id="chatId",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBlooio) -> None:
        response = await async_client.chats.messages.with_raw_response.retrieve(
            message_id="msg_abc123def456",
            chat_id="chatId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBlooio) -> None:
        async with async_client.chats.messages.with_streaming_response.retrieve(
            message_id="msg_abc123def456",
            chat_id="chatId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.retrieve(
                message_id="msg_abc123def456",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.chats.messages.with_raw_response.retrieve(
                message_id="",
                chat_id="chatId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBlooio) -> None:
        message = await async_client.chats.messages.list(
            chat_id="chatId",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBlooio) -> None:
        message = await async_client.chats.messages.list(
            chat_id="chatId",
            direction="inbound",
            limit=1,
            offset=0,
            since=0,
            sort="asc",
            until=0,
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBlooio) -> None:
        response = await async_client.chats.messages.with_raw_response.list(
            chat_id="chatId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBlooio) -> None:
        async with async_client.chats.messages.with_streaming_response.list(
            chat_id="chatId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.list(
                chat_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncBlooio) -> None:
        message = await async_client.chats.messages.get_status(
            message_id="msg_abc123def456",
            chat_id="chatId",
        )
        assert_matches_type(MessageGetStatusResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncBlooio) -> None:
        response = await async_client.chats.messages.with_raw_response.get_status(
            message_id="msg_abc123def456",
            chat_id="chatId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageGetStatusResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncBlooio) -> None:
        async with async_client.chats.messages.with_streaming_response.get_status(
            message_id="msg_abc123def456",
            chat_id="chatId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageGetStatusResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.get_status(
                message_id="msg_abc123def456",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.chats.messages.with_raw_response.get_status(
                message_id="",
                chat_id="chatId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_react(self, async_client: AsyncBlooio) -> None:
        message = await async_client.chats.messages.react(
            message_id="messageId",
            chat_id="chatId",
            reaction="+love",
        )
        assert_matches_type(MessageReactResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_react_with_all_params(self, async_client: AsyncBlooio) -> None:
        message = await async_client.chats.messages.react(
            message_id="messageId",
            chat_id="chatId",
            reaction="+love",
            direction="inbound",
        )
        assert_matches_type(MessageReactResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_react(self, async_client: AsyncBlooio) -> None:
        response = await async_client.chats.messages.with_raw_response.react(
            message_id="messageId",
            chat_id="chatId",
            reaction="+love",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageReactResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_react(self, async_client: AsyncBlooio) -> None:
        async with async_client.chats.messages.with_streaming_response.react(
            message_id="messageId",
            chat_id="chatId",
            reaction="+love",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageReactResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_react(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.react(
                message_id="messageId",
                chat_id="",
                reaction="+love",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.chats.messages.with_raw_response.react(
                message_id="",
                chat_id="chatId",
                reaction="+love",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncBlooio) -> None:
        message = await async_client.chats.messages.send(
            chat_id="chatId",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncBlooio) -> None:
        message = await async_client.chats.messages.send(
            chat_id="chatId",
            attachments=["string"],
            effect="slam",
            format="plain",
            from_number="from_number",
            link_preview={
                "image_url": "https://example.com",
                "title": "title",
            },
            parts=[
                {
                    "link_preview": {
                        "image_url": "https://example.com",
                        "title": "title",
                    },
                    "mention": "mention",
                    "name": "name",
                    "text": "text",
                    "url": "url",
                }
            ],
            reply_to={
                "guid": "guid",
                "message_id": "message_id",
                "part_index": 0,
            },
            share_contact=True,
            text="string",
            use_typing_indicator=True,
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncBlooio) -> None:
        response = await async_client.chats.messages.with_raw_response.send(
            chat_id="chatId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncBlooio) -> None:
        async with async_client.chats.messages.with_streaming_response.send(
            chat_id="chatId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.send(
                chat_id="",
            )
