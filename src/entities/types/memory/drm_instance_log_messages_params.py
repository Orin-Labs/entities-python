# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DrmInstanceLogMessagesParams"]


class DrmInstanceLogMessagesParams(TypedDict, total=False):
    max_daily_summaries_before_weekly: int

    max_weekly_summaries_before_monthly: int

    name: str

    summarizer_model: str

    summarizer_name_prefix: str

    timezone: str
