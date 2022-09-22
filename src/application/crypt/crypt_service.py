import os
from pathlib import Path

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode
from base64 import b64encode


class CryptService:
    __current_path = os.path.dirname(__file__)
    PUBLIC_KEY_PATH = Path(f'{__current_path}/keys/public_key.pem')
    PRIVATE_KEY_PATH = Path(f'{__current_path}/keys/private_key.pem')

    @classmethod
    def encrypt(cls, value: str) -> str:
        with open(cls.PUBLIC_KEY_PATH, "rb") as file:
            public_key = RSA.importKey(file.read())

        encryptor = PKCS1_OAEP.new(public_key)
        return b64encode(encryptor.encrypt(value.encode())).decode()

    @classmethod
    def decrypt(cls, value: str) -> str:
        with open(cls.PRIVATE_KEY_PATH, "rb") as file:
            private_key = RSA.importKey(file.read())

        decryptor = PKCS1_OAEP.new(private_key)
        return decryptor.decrypt(b64decode(value)).decode()
