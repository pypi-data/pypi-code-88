"""Declares :class:`SecretKey`."""
import hashlib
import hmac

import ioc.loader
from unimatrix.conf import settings

from . import oid
from .algorithms import Algorithm
from .ciphertext import Ciphertext
from .keychain import chain
from .plaintext import Plaintext
from .private import PrivateKey
from .signer import ApplicationSigner
from .signer import GenericSigner
from .signature import Signature


class SecretKey(PrivateKey):
    """A :class:`~unimatrix.ext.crypto.PrivateKey` implementation that is
    commonly used as a secret for an application. It supports signing/verifying
    using HMAC, and encryption with AES.
    """
    capabilities = [
        oid.HMACSHA224,
        oid.HMACSHA256,
        oid.HMACSHA384,
        oid.HMACSHA512,
        oid.AES256GCM
    ]

    _algorithms = {
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512,
    }

    @classmethod
    def default(cls, algorithm=None):
        """Return the default secret key as specified by the settings."""
        return cls({'secret': settings.SECRET_KEY})

    def setup(self, opts):
        self._secret = str.encode(opts.secret)\
            if isinstance(opts.secret, str)\
            else opts.secret

    def _hashfunc(self, algorithm):
        return self._algorithms[algorithm]

    async def decrypt(self, ct: Ciphertext, apply_decrypt) -> bytes:
        return await apply_decrypt(self._secret, ct)

    async def encrypt(self, pt: Plaintext, apply_encrypt, **kwargs) -> bytes:
        return await apply_encrypt(self._secret, pt, **kwargs)

    async def sign(self, blob: bytes, algorithm: str) -> bytes:
        """Sign byte-sequence `blob` with the given algorithm."""
        return hmac.new(self._secret, blob, self._hashfunc(algorithm)).digest()

    async def verify(self, digest: bytes, blob: bytes, algorithm: str) -> bytes:
        """Verify that byte-sequence `digest` was created from
        byte-sequence `blob` using the given `algorithm`.
        """
        return hmac.compare_digest(digest, await self.sign(blob, algorithm))


def get_secret_key():
    """Return the default secret key used by an application, as configured
    in :mod:`unimatrix.conf`. The underlying settings module (specified by
    :envvar:`UNIMATRIX_SETTINGS_MODULE`) must expose a ``SECRET_KEY`` attribute
    that holds the private key.
    """
    return SecretKey.default()


def get_signer(algorithm=None, keyid=None, key=None) -> Signature:
    """Return a :class:`~unimatrix.ext.crypto.Signer` implementation
    configured with the default secret key (as returned by
    :func:`get_secret_key()`) and algorithm.
    """
    if algorithm is not None and not (keyid or key):
        raise TypeError("Provide either the `keyid` or `key` parameters.")

    if algorithm is not None and not isinstance(algorithm, Algorithm):
        raise TypeError(
            "`algorithm` must be a subclass of "
            "unimatrix.ext.crypto.algorithms.Algorithm"
        )

    if key is not None and not isinstance(key, PrivateKey):
        raise TypeError(
            "`key` must be a subclass of "
            "unimatrix.ext.crypto.PrivateKey"
        )

    return ApplicationSigner(get_secret_key())\
        if algorithm is None\
        else GenericSigner(algorithm, key or chain.get(keyid))


def get_default_signer():
    """Return a :class:`GenericSigner` instance configured based on the
    settings ``CRYPTO_DEFAULT_SIGNING_KEY`` and ``CRYPTO_DEFAULT_SIGNING_ALG``.
    """
    return get_signer(
        algorithm=ioc.loader.import_symbol(settings.CRYPTO_DEFAULT_SIGNING_ALG),
        keyid=settings.CRYPTO_DEFAULT_SIGNING_KEY
    )
