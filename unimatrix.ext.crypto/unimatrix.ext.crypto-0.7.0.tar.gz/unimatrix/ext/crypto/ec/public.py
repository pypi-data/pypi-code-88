"""Declares :class:`EllipticCurvePublicKey`."""
import hashlib

from ..public import PublicKey
from .verifier import EllipticCurveVerifier


class EllipticCurvePublicKey(EllipticCurveVerifier, PublicKey):

    @property
    def keyid(self):
        return hashlib.md5(bytes(self)).hexdigest() # nosec

    @property
    def y(self):
        return self.__numbers.y

    @property
    def x(self):
        return self.__numbers.x

    @property
    def public(self):
        return self.__public

    def __init__(self, key, capabilities=None):
        self.__public = key
        self.__numbers = self.__public.public_numbers()
        self.capabilities = capabilities or self.capabilities

    async def encrypt(self, *args, **kwargs):
        raise NotImplementedError

    def __bytes__(self):
        buf = bytearray()
        buf.append(0x04)
        buf.extend(int.to_bytes(self.__numbers.x, 32, 'big'))
        buf.extend(int.to_bytes(self.__numbers.y, 32, 'big'))
        return bytes(buf)
