from sqlalchemy import Column, String, BigInteger
from database.database import Base

class Transaction:
    __tablename__ = "transations"

    id = Column(BigInteger, primary_key=True, index=True)
    user_document = Column(String, nullable=False)
    credit_card_token = Column(String, nullable=False)
    value = Column(BigInteger, nullable=False)