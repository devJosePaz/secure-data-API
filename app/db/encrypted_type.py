from sqlalchemy.types import TypeDecorator, String
from app.services.cryptography import encrypt, decrypt

class EncryptedString(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        return encrypt(value) if value else None

    def process_result_value(self, value, dialect):
        return decrypt(value) if value else None