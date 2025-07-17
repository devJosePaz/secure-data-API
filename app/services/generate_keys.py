from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

# Garante que a pasta keys/ exista
os.makedirs("app/keys", exist_ok=True)

# Gera o par de chaves (2048 bits)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Salva a chave privada
with open("app/keys/private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

# Salva a chave pública
public_key = private_key.public_key()
with open("app/keys/public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )

print("✅ Chaves RSA geradas em app/keys/")
