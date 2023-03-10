from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class DatatransApplePayConfig(BaseModel):
    url: Optional[str]


DatatransApplePayConfig.update_forward_refs()
