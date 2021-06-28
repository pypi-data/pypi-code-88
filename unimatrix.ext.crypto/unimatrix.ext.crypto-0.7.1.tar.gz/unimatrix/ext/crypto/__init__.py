# pylint: skip-file
from unimatrix.lib import meta

from . import algorithms
from .abstractkeystore import AbstractKeystore
from .algorithms import *
from .ciphertext import Ciphertext
from .conf import configure
from .keychain import chain
from .keyloader import KeyLoader
from .secret import get_default_signer
from .secret import get_secret_key
from .secret import get_signer
from .secret import SecretKey
from .signable import Signable
from .signature import Signature
from .signer import Signer
from .signer import GenericSigner
from .truststore import trust
from .plaintext import Plaintext
from .private import PrivateKey
from .public import PublicKey


__all__ = [
    'algorithms',
    'configure',
    'get_default_signer',
    'get_secret_key',
    'get_signer',
]
default_app_config = 'unimatrix.ext.crypto.apps.ApplicationConfig'


def add(keyconf):
    """Add a key to the internal key registry."""
    chain.register_deferred(keyconf)


def get(name) -> PublicKey:
    """Return the :class:`Key` identified by `name`."""
    return chain.get(name)


def plain(pt: bytes, **kwargs) -> Plaintext:
    """Return a :class:`Plaintext` instance configured with the given
    attributes. This function is used for cryptographic algorithms that
    require additional input besided the plaintext itself.

    Args:
        pt: the plain text. If `pt` is :class:`str`, then UTF-8 encoding is
            assumed.

    Returns:
        :class:`Plaintext`

    Below is an example with Authenticated Encryption with Associated Data
    (AEAD):

    .. code:: python

        from unimatrix.ext import crypto

        pt = crypto.plain(b"My secret text", aad=b"Authenticated data")
        print(pt.aad)
    """
    pt = Plaintext(pt)
    for k in dict.keys(kwargs):
        if str.startswith(k, '_'):
            continue
        setattr(pt, k, kwargs[k])
    return pt


AbstractKeyStore = AbstractKeystore
