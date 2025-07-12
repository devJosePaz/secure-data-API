from pydantic import BaseModel

class TransationCreate(BaseModel):
    user_document : str
    credit_card : str
    value : int

class TransationResponse(BaseModel):
    user_document : str
    credit_card : str
    valie : str

    class Config:
        from_attributes = True