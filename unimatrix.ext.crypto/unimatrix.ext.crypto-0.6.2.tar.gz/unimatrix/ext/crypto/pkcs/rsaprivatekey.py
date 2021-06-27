"""Declares :class:`RSAPrivateKey`."""
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.exceptions import InvalidSignature

from ..private import PrivateKey
from .base import PKCSObject
from .pempublickey import PEMPublicKey


class RSAPrivateKey(PKCSObject, PrivateKey):
    """Uses an RSA private key to perform cryptographic operations.

    The options format recognized by this implementation is specified below:

    .. code:: python

        {
            "path": "/path/to/private/key",
            "content": b'-----BEGIN RSA PRIVATE KEY-----...'
        }
    """

    def setup(self, opts):
        """Configures the :class:`RSAPrivateKey` using the given options `opts`.
        This method is called in the constructor and should not be called more
        than once.
        """
        if not bool(opts.get('content')) ^ bool(opts.get('path')):
            raise ValueError("Specify either .content or .path")
        content = opts.get('content')
        if opts.get('path'):
            content = open(opts.path, 'rb').read()
        self._private = load_pem_private_key(content, opts.get('password'))
        self._public = self._private.public_key()

    def has_public_key(self):
        """Return a boolean indicating if the private key is able to
        extract and provide its public key.
        """
        return True

    async def get_public_key(self):
        return PEMPublicKey(self._public)

    async def decrypt(self, ct, padding):
        return self._private.decrypt(bytes(ct), padding)

    async def sign(self, blob: bytes, padding, algorithm) -> bytes:
        return self._private.sign(blob, padding, algorithm)

    async def encrypt(self, pt, padding):
        return self._public.encrypt(bytes(pt), padding)

    async def verify(self, digest: bytes, blob: bytes,
        padding, algorithm) -> bytes:
        try:
            self._public.verify(bytes(digest), blob, padding, algorithm)
            return True
        except InvalidSignature:
            return False
