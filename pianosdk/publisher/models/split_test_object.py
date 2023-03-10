from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class SplitTestObject(BaseModel):
    split_test_id: Optional[str]
    state: Optional[str]


SplitTestObject.update_forward_refs()
