# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from entities import Entities, AsyncEntities
from tests.utils import assert_matches_type
from entities.types.memory import (
    DrmInstance,
    DrmInstanceListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDrmInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Entities) -> None:
        drm_instance = client.memory.drm_instances.create()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Entities) -> None:
        drm_instance = client.memory.drm_instances.create(
            max_daily_summaries_before_weekly=-2147483648,
            max_weekly_summaries_before_monthly=-2147483648,
            name="name",
            summarizer_model="summarizer_model",
            summarizer_name_prefix="summarizer_name_prefix",
            timezone="timezone",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Entities) -> None:
        response = client.memory.drm_instances.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = response.parse()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Entities) -> None:
        with client.memory.drm_instances.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = response.parse()
            assert_matches_type(DrmInstance, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Entities) -> None:
        drm_instance = client.memory.drm_instances.retrieve(
            "id",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Entities) -> None:
        response = client.memory.drm_instances.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = response.parse()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Entities) -> None:
        with client.memory.drm_instances.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = response.parse()
            assert_matches_type(DrmInstance, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Entities) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory.drm_instances.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Entities) -> None:
        drm_instance = client.memory.drm_instances.update(
            id="id",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Entities) -> None:
        drm_instance = client.memory.drm_instances.update(
            id="id",
            max_daily_summaries_before_weekly=-2147483648,
            max_weekly_summaries_before_monthly=-2147483648,
            name="name",
            summarizer_model="summarizer_model",
            summarizer_name_prefix="summarizer_name_prefix",
            timezone="timezone",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Entities) -> None:
        response = client.memory.drm_instances.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = response.parse()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Entities) -> None:
        with client.memory.drm_instances.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = response.parse()
            assert_matches_type(DrmInstance, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Entities) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory.drm_instances.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Entities) -> None:
        drm_instance = client.memory.drm_instances.list()
        assert_matches_type(DrmInstanceListResponse, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Entities) -> None:
        response = client.memory.drm_instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = response.parse()
        assert_matches_type(DrmInstanceListResponse, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Entities) -> None:
        with client.memory.drm_instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = response.parse()
            assert_matches_type(DrmInstanceListResponse, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Entities) -> None:
        drm_instance = client.memory.drm_instances.delete(
            "id",
        )
        assert drm_instance is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Entities) -> None:
        response = client.memory.drm_instances.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = response.parse()
        assert drm_instance is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Entities) -> None:
        with client.memory.drm_instances.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = response.parse()
            assert drm_instance is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Entities) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory.drm_instances.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_memory_context(self, client: Entities) -> None:
        drm_instance = client.memory.drm_instances.get_memory_context(
            "id",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_memory_context(self, client: Entities) -> None:
        response = client.memory.drm_instances.with_raw_response.get_memory_context(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = response.parse()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_memory_context(self, client: Entities) -> None:
        with client.memory.drm_instances.with_streaming_response.get_memory_context(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = response.parse()
            assert_matches_type(DrmInstance, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_memory_context(self, client: Entities) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory.drm_instances.with_raw_response.get_memory_context(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_log_messages(self, client: Entities) -> None:
        drm_instance = client.memory.drm_instances.log_messages(
            id="id",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_log_messages_with_all_params(self, client: Entities) -> None:
        drm_instance = client.memory.drm_instances.log_messages(
            id="id",
            max_daily_summaries_before_weekly=-2147483648,
            max_weekly_summaries_before_monthly=-2147483648,
            name="name",
            summarizer_model="summarizer_model",
            summarizer_name_prefix="summarizer_name_prefix",
            timezone="timezone",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_log_messages(self, client: Entities) -> None:
        response = client.memory.drm_instances.with_raw_response.log_messages(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = response.parse()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_log_messages(self, client: Entities) -> None:
        with client.memory.drm_instances.with_streaming_response.log_messages(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = response.parse()
            assert_matches_type(DrmInstance, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_log_messages(self, client: Entities) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory.drm_instances.with_raw_response.log_messages(
                id="",
            )


class TestAsyncDrmInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncEntities) -> None:
        drm_instance = await async_client.memory.drm_instances.create()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEntities) -> None:
        drm_instance = await async_client.memory.drm_instances.create(
            max_daily_summaries_before_weekly=-2147483648,
            max_weekly_summaries_before_monthly=-2147483648,
            name="name",
            summarizer_model="summarizer_model",
            summarizer_name_prefix="summarizer_name_prefix",
            timezone="timezone",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEntities) -> None:
        response = await async_client.memory.drm_instances.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = await response.parse()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEntities) -> None:
        async with async_client.memory.drm_instances.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = await response.parse()
            assert_matches_type(DrmInstance, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEntities) -> None:
        drm_instance = await async_client.memory.drm_instances.retrieve(
            "id",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEntities) -> None:
        response = await async_client.memory.drm_instances.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = await response.parse()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEntities) -> None:
        async with async_client.memory.drm_instances.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = await response.parse()
            assert_matches_type(DrmInstance, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEntities) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory.drm_instances.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncEntities) -> None:
        drm_instance = await async_client.memory.drm_instances.update(
            id="id",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEntities) -> None:
        drm_instance = await async_client.memory.drm_instances.update(
            id="id",
            max_daily_summaries_before_weekly=-2147483648,
            max_weekly_summaries_before_monthly=-2147483648,
            name="name",
            summarizer_model="summarizer_model",
            summarizer_name_prefix="summarizer_name_prefix",
            timezone="timezone",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEntities) -> None:
        response = await async_client.memory.drm_instances.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = await response.parse()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEntities) -> None:
        async with async_client.memory.drm_instances.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = await response.parse()
            assert_matches_type(DrmInstance, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncEntities) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory.drm_instances.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncEntities) -> None:
        drm_instance = await async_client.memory.drm_instances.list()
        assert_matches_type(DrmInstanceListResponse, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEntities) -> None:
        response = await async_client.memory.drm_instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = await response.parse()
        assert_matches_type(DrmInstanceListResponse, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEntities) -> None:
        async with async_client.memory.drm_instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = await response.parse()
            assert_matches_type(DrmInstanceListResponse, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncEntities) -> None:
        drm_instance = await async_client.memory.drm_instances.delete(
            "id",
        )
        assert drm_instance is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEntities) -> None:
        response = await async_client.memory.drm_instances.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = await response.parse()
        assert drm_instance is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEntities) -> None:
        async with async_client.memory.drm_instances.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = await response.parse()
            assert drm_instance is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEntities) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory.drm_instances.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_memory_context(self, async_client: AsyncEntities) -> None:
        drm_instance = await async_client.memory.drm_instances.get_memory_context(
            "id",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_memory_context(self, async_client: AsyncEntities) -> None:
        response = await async_client.memory.drm_instances.with_raw_response.get_memory_context(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = await response.parse()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_memory_context(self, async_client: AsyncEntities) -> None:
        async with async_client.memory.drm_instances.with_streaming_response.get_memory_context(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = await response.parse()
            assert_matches_type(DrmInstance, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_memory_context(self, async_client: AsyncEntities) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory.drm_instances.with_raw_response.get_memory_context(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_log_messages(self, async_client: AsyncEntities) -> None:
        drm_instance = await async_client.memory.drm_instances.log_messages(
            id="id",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_log_messages_with_all_params(self, async_client: AsyncEntities) -> None:
        drm_instance = await async_client.memory.drm_instances.log_messages(
            id="id",
            max_daily_summaries_before_weekly=-2147483648,
            max_weekly_summaries_before_monthly=-2147483648,
            name="name",
            summarizer_model="summarizer_model",
            summarizer_name_prefix="summarizer_name_prefix",
            timezone="timezone",
        )
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_log_messages(self, async_client: AsyncEntities) -> None:
        response = await async_client.memory.drm_instances.with_raw_response.log_messages(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drm_instance = await response.parse()
        assert_matches_type(DrmInstance, drm_instance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_log_messages(self, async_client: AsyncEntities) -> None:
        async with async_client.memory.drm_instances.with_streaming_response.log_messages(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drm_instance = await response.parse()
            assert_matches_type(DrmInstance, drm_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_log_messages(self, async_client: AsyncEntities) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory.drm_instances.with_raw_response.log_messages(
                id="",
            )
