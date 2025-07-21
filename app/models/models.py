from sqlalchemy import Column, String, Integer
from app.database import Base
from app.types.encrypted_type import EncryptedString

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_document = Column(EncryptedString(255), nullable=False)
    credit_card_token = Column(EncryptedString(255), nullable=False)
    value = Column(BigInteger, nullable=False)