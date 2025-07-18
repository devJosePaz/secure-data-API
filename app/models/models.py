from sqlalchemy import Column, String, BigInteger
from database.database import Base
from db.encrypted_type import EncryptedString

class Transaction:
    __tablename__ = "transactions"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_document = Column(EncryptedString(255), nullable=False)
    credit_card_token = Column(EncryptedString(255), nullable=False)
    value = Column(BigInteger, nullable=False)