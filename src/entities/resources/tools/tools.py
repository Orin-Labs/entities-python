# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import tools_ as tools
from .adapters import (
    AdaptersResource,
    AsyncAdaptersResource,
    AdaptersResourceWithRawResponse,
    AsyncAdaptersResourceWithRawResponse,
    AdaptersResourceWithStreamingResponse,
    AsyncAdaptersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def adapters(self) -> AdaptersResource:
        return AdaptersResource(self._client)

    @cached_property
    def tools(self) -> tools.ToolsResource:
        return tools.ToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/entities-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/entities-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def adapters(self) -> AsyncAdaptersResource:
        return AsyncAdaptersResource(self._client)

    @cached_property
    def tools(self) -> tools.AsyncToolsResource:
        return tools.AsyncToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/entities-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/entities-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

    @cached_property
    def adapters(self) -> AdaptersResourceWithRawResponse:
        return AdaptersResourceWithRawResponse(self._tools.adapters)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithRawResponse:
        return tools.ToolsResourceWithRawResponse(self._tools.tools)


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

    @cached_property
    def adapters(self) -> AsyncAdaptersResourceWithRawResponse:
        return AsyncAdaptersResourceWithRawResponse(self._tools.adapters)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithRawResponse:
        return tools.AsyncToolsResourceWithRawResponse(self._tools.tools)


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

    @cached_property
    def adapters(self) -> AdaptersResourceWithStreamingResponse:
        return AdaptersResourceWithStreamingResponse(self._tools.adapters)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithStreamingResponse:
        return tools.ToolsResourceWithStreamingResponse(self._tools.tools)


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

    @cached_property
    def adapters(self) -> AsyncAdaptersResourceWithStreamingResponse:
        return AsyncAdaptersResourceWithStreamingResponse(self._tools.adapters)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithStreamingResponse:
        return tools.AsyncToolsResourceWithStreamingResponse(self._tools.tools)
