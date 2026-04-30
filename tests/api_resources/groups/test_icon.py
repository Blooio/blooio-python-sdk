# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blooio import Blooio, AsyncBlooio
from tests.utils import assert_matches_type
from blooio.types.groups import GroupIcon

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIcon:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Blooio) -> None:
        icon = client.groups.icon.remove(
            "grp_abc123def456",
        )
        assert_matches_type(GroupIcon, icon, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Blooio) -> None:
        response = client.groups.icon.with_raw_response.remove(
            "grp_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        icon = response.parse()
        assert_matches_type(GroupIcon, icon, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Blooio) -> None:
        with client.groups.icon.with_streaming_response.remove(
            "grp_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            icon = response.parse()
            assert_matches_type(GroupIcon, icon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.groups.icon.with_raw_response.remove(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set(self, client: Blooio) -> None:
        icon = client.groups.icon.set(
            group_id="grp_abc123def456",
            icon=b"Example data",
        )
        assert_matches_type(GroupIcon, icon, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set(self, client: Blooio) -> None:
        response = client.groups.icon.with_raw_response.set(
            group_id="grp_abc123def456",
            icon=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        icon = response.parse()
        assert_matches_type(GroupIcon, icon, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set(self, client: Blooio) -> None:
        with client.groups.icon.with_streaming_response.set(
            group_id="grp_abc123def456",
            icon=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            icon = response.parse()
            assert_matches_type(GroupIcon, icon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set(self, client: Blooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.groups.icon.with_raw_response.set(
                group_id="",
                icon=b"Example data",
            )


class TestAsyncIcon:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncBlooio) -> None:
        icon = await async_client.groups.icon.remove(
            "grp_abc123def456",
        )
        assert_matches_type(GroupIcon, icon, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncBlooio) -> None:
        response = await async_client.groups.icon.with_raw_response.remove(
            "grp_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        icon = await response.parse()
        assert_matches_type(GroupIcon, icon, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncBlooio) -> None:
        async with async_client.groups.icon.with_streaming_response.remove(
            "grp_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            icon = await response.parse()
            assert_matches_type(GroupIcon, icon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.groups.icon.with_raw_response.remove(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set(self, async_client: AsyncBlooio) -> None:
        icon = await async_client.groups.icon.set(
            group_id="grp_abc123def456",
            icon=b"Example data",
        )
        assert_matches_type(GroupIcon, icon, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncBlooio) -> None:
        response = await async_client.groups.icon.with_raw_response.set(
            group_id="grp_abc123def456",
            icon=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        icon = await response.parse()
        assert_matches_type(GroupIcon, icon, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncBlooio) -> None:
        async with async_client.groups.icon.with_streaming_response.set(
            group_id="grp_abc123def456",
            icon=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            icon = await response.parse()
            assert_matches_type(GroupIcon, icon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set(self, async_client: AsyncBlooio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.groups.icon.with_raw_response.set(
                group_id="",
                icon=b"Example data",
            )
