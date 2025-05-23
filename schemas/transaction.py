from pydantic import BaseModel
from typing import Dict

class Transaction(BaseModel):
    provider: str
    amount: float
    currency: str
    recipient: Dict[str, str]
    sender: Dict[str, str]