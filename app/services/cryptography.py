import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

from pathlib import Path

# Caminhos das chaves
PRIVATE_KEY_PATH = Path("app/keys/private_key.pem")
PUBLIC_KEY_PATH = Path("app/keys/public_key.pem")

# Carrega chave pública
def load_public_key():
    with open(PUBLIC_KEY_PATH, "rb") as f:
        return serialization.load_pem_public_key(f.read())

# Carrega chave privada
def load_private_key():
    with open(PRIVATE_KEY_PATH, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

# Criptografa com a chave pública
def encrypt(plaintext: str) -> str:
    public_key = load_public_key()

    encrypted = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.b64encode(encrypted).decode()

# Descriptografa com a chave privada
def decrypt(ciphertext: str) -> str:
    private_key = load_private_key()

    decrypted = private_key.decrypt(
        base64.b64decode(ciphertext),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return decrypted.decode()

