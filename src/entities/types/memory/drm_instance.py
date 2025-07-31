# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DrmInstance"]


class DrmInstance(BaseModel):
    id: int

    created_at: datetime

    updated_at: datetime

    max_daily_summaries_before_weekly: Optional[int] = None

    max_weekly_summaries_before_monthly: Optional[int] = None

    name: Optional[str] = None

    summarizer_model: Optional[str] = None

    summarizer_name_prefix: Optional[str] = None

    timezone: Optional[str] = None
