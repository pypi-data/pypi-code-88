"""Declares :class:`EllipticCurvePublicKey`."""
import hashlib

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import ec

from ..public import PublicKey


class EllipticCurvePublicKey(PublicKey):

    @property
    def y(self):
        return self.__numbers.y

    @property
    def x(self):
        return self.__numbers.x

    def __init__(self, key, capabilities=None):
        self.__public = key
        self.__numbers = self.__public.public_numbers()
        self.capabilities = capabilities or self.capabilities

    async def encrypt(self, *args, **kwargs):
        raise NotImplementedError

    async def verify(self, signature: bytes, blob: bytes,
        hasher, algorithm, *args, **kwargs
    ) -> bytes:
        hasher.update(blob)
        digest = hasher.finalize()
        try:
            self.__public.verify(
                bytes(signature), digest,
                ec.ECDSA(utils.Prehashed(algorithm))
            )
            return True
        except InvalidSignature:
            return False

    def __bytes__(self):
        return int.to_bytes(self.__numbers.x, 32, 'big')\
            + int.to_bytes(self.__numbers.y, 32, 'big')
