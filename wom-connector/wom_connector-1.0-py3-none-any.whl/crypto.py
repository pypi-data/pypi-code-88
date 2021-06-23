import base64
import math
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric import padding
from .wom_logger import WOMLogger

class Crypto(object):
    __logger = WOMLogger("Crypto")

    @classmethod
    def encrypt(cls, payload, public_key: RSAPublicKey):
        payload_bytes = payload.encode()

        encrypted_payload_bytes = cls.__encrypt(payload_bytes, public_key)

        return base64.b64encode(encrypted_payload_bytes)

    @classmethod
    def __encrypt(cls, payload_bytes: list, receiver_public_key: RSAPublicKey):
        # see:https://crypto.stackexchange.com/a/50183
        blockSize = int(receiver_public_key.key_size/8) - 11
        blocks = math.ceil((len(payload_bytes)/blockSize))

        encrypted = b''

        for i in range(0, blocks):
            offset = i*blockSize
            block_length = min(blockSize, len(payload_bytes)-offset)
            block = payload_bytes[offset:offset+block_length]
            encrypted = encrypted + receiver_public_key.encrypt(block, padding.PKCS1v15())

        cls.__logger.debug("ENCRYPT Input bytes: {0}, encrypted bytes {1}".format(
            len(payload_bytes), len(encrypted)))

        return encrypted

    @classmethod
    def decrypt(cls, payload, private_key: RSAPrivateKey):
        payload_bytes = base64.b64decode(payload)

        return cls.__decrypt(payload_bytes, private_key)

    @classmethod
    def __decrypt(cls, payload_bytes, private_key: RSAPrivateKey):
        blockSize = int(private_key.key_size / 8)
        blocks = math.ceil((len(payload_bytes) / blockSize))

        decrypted = b''

        for i in range(0, blocks):
            offset = i * blockSize
            block_length = min(blockSize, len(payload_bytes) - offset)
            block = payload_bytes[offset:offset + block_length]
            decrypted = decrypted + private_key.decrypt(block, padding.PKCS1v15())

        cls.__logger.debug("DECRYPT Input bytes: {0}, encrypted bytes {1}".format(
            len(payload_bytes), len(decrypted)))

        return decrypted
