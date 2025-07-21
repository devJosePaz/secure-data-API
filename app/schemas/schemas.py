from pydantic import BaseModel
from typing import Optional

class TransactionCreate(BaseModel):
    user_document : str
    credit_card_token : str
    value : int

class TransactionResponse(BaseModel):
    id: int 
    user_document : str
    credit_card_token : str
    value : int

    class Config:
        from_attributes = True

