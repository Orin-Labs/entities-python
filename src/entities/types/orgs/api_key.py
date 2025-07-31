# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: int

    created_at: datetime

    key: str

    is_active: Optional[bool] = None

    name: Optional[str] = None
