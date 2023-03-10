from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.source import Source
from typing import List


class KeySource(BaseModel):
    key: Optional[str]
    key_sources: Optional['List[Source]']


KeySource.update_forward_refs()
