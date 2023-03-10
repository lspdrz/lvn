from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LicenseeManager(BaseModel):
    uid: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    personal_name: Optional[str]


LicenseeManager.update_forward_refs()
