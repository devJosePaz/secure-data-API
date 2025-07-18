from pydantic import BaseModel

class TransactionCreate(BaseModel):
    user_document : str
    credit_card : str
    value : int

class TransactionResponse(BaseModel):
    id: int 
    user_document : str
    credit_card : str
    value : str

    class Config:
        from_attributes = True