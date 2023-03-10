from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PayeeSettingsEntry(BaseModel):
    merchant_account_id: Optional[str]
    payee_email: Optional[str]


PayeeSettingsEntry.update_forward_refs()
