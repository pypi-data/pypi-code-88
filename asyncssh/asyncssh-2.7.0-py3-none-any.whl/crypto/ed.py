# Copyright (c) 2019-2020 by Ron Frederick <ronf@timeheart.net> and others.
#
# This program and the accompanying materials are made available under
# the terms of the Eclipse Public License v2.0 which accompanies this
# distribution and is available at:
#
#     http://www.eclipse.org/legal/epl-2.0/
#
# This program may also be made available under the following secondary
# licenses when the conditions for such availability set forth in the
# Eclipse Public License v2.0 are satisfied:
#
#    GNU General Public License, Version 2.0, or any later versions of
#    that license
#
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later
#
# Contributors:
#     Ron Frederick - initial implementation, API, and documentation

"""A shim around PyCA and libnacl for Edwards-curve keys and key exchange"""

import ctypes
import os

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends.openssl import backend
from cryptography.hazmat.primitives.asymmetric import ed25519, ed448
from cryptography.hazmat.primitives.asymmetric import x25519, x448
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PrivateFormat
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography.hazmat.primitives.serialization import NoEncryption

from .misc import PyCAKey


ed25519_available = backend.ed25519_supported()
ed448_available = backend.ed448_supported()
curve25519_available = backend.x25519_supported()
curve448_available = backend.x448_supported()


if ed25519_available: # pragma: no branch
    class _EdKey(PyCAKey):
        """Base class for shim around PyCA for Ed25519/Ed448 keys"""

        def __init__(self, pyca_key, pub, priv=None):
            super().__init__(pyca_key)

            self._pub = pub
            self._priv = priv

        @property
        def public_value(self):
            """Return the public value encoded as a byte string"""

            return self._pub

        @property
        def private_value(self):
            """Return the private value encoded as a byte string"""

            return self._priv


    class EdDSAPrivateKey(_EdKey):
        """A shim around PyCA for EdDSA private keys"""

        _priv_classes = {b'ed25519': ed25519.Ed25519PrivateKey,
                         b'ed448': ed448.Ed448PrivateKey}

        @classmethod
        def construct(cls, curve_id, priv):
            """Construct an EdDSA private key"""

            priv_cls = cls._priv_classes[curve_id]
            priv_key = priv_cls.from_private_bytes(priv)
            pub_key = priv_key.public_key()
            pub = pub_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

            return cls(priv_key, pub, priv)

        @classmethod
        def generate(cls, curve_id):
            """Generate a new EdDSA private key"""

            priv_cls = cls._priv_classes[curve_id]
            priv_key = priv_cls.generate()
            priv = priv_key.private_bytes(Encoding.Raw, PrivateFormat.Raw,
                                          NoEncryption())

            pub_key = priv_key.public_key()
            pub = pub_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

            return cls(priv_key, pub, priv)

        def sign(self, data, hash_alg=None):
            """Sign a block of data"""

            # pylint: disable=unused-argument

            return self.pyca_key.sign(data)


    class EdDSAPublicKey(_EdKey):
        """A shim around PyCA for EdDSA public keys"""

        _pub_classes = {b'ed25519': ed25519.Ed25519PublicKey,
                        b'ed448': ed448.Ed448PublicKey}

        @classmethod
        def construct(cls, curve_id, pub):
            """Construct an EdDSA public key"""

            pub_cls = cls._pub_classes[curve_id]
            pub_key = pub_cls.from_public_bytes(pub)

            return cls(pub_key, pub)

        def verify(self, data, sig, hash_alg=None):
            """Verify the signature on a block of data"""

            # pylint: disable=unused-argument

            try:
                self.pyca_key.verify(sig, data)
                return True
            except InvalidSignature:
                return False
else: # pragma: no cover
    class _EdKey:
        """Base class for shim around libnacl for Ed25519 keys"""

        def __init__(self, pub, priv=None):
            self._pub = pub
            self._priv = priv

        @property
        def public_value(self):
            """Return the public value encoded as a byte string"""

            return self._pub

        @property
        def private_value(self):
            """Return the private value encoded as a byte string"""

            return self._priv[:-len(self._pub)] if self._priv else None


    class EdDSAPrivateKey(_EdKey):
        """A shim around libnacl for Ed25519 private keys"""

        @classmethod
        def construct(cls, curve_id, priv):
            """Construct an EdDSA private key"""

            # pylint: disable=unused-argument

            return cls(*_ed25519_construct_keypair(priv))

        @classmethod
        def generate(cls, curve_id):
            """Generate a new EdDSA private key"""

            # pylint: disable=unused-argument

            return cls(*_ed25519_generate_keypair())

        def sign(self, data, hash_alg=None):
            """Sign a block of data"""

            # pylint: disable=unused-argument

            return _ed25519_sign(data, self._priv)[:-len(data)]


    class EdDSAPublicKey(_EdKey):
        """A shim around libnacl for Ed25519 public keys"""

        @classmethod
        def construct(cls, curve_id, pub):
            """Construct an EdDSA public key"""

            # pylint: disable=unused-argument

            if len(pub) != _ED25519_PUBLIC_BYTES:
                raise ValueError('Invalid Ed25519 public key')

            return cls(pub)

        def verify(self, data, sig, hash_alg=None):
            """Verify the signature on a block of data"""

            # pylint: disable=unused-argument

            try:
                return _ed25519_verify(sig + data, self._pub) == data
            except ValueError:
                return False

    try:
        import libnacl

        _ED25519_PUBLIC_BYTES = libnacl.crypto_sign_ed25519_PUBLICKEYBYTES

        _ed25519_construct_keypair = libnacl.crypto_sign_seed_keypair
        _ed25519_generate_keypair = libnacl.crypto_sign_keypair
        _ed25519_sign = libnacl.crypto_sign
        _ed25519_verify = libnacl.crypto_sign_open

        ed25519_available = True
    except (ImportError, OSError, AttributeError):
        pass


if curve25519_available: # pragma: no branch
    class Curve25519DH:
        """Curve25519 Diffie Hellman implementation based on PyCA"""

        def __init__(self):
            self._priv_key = x25519.X25519PrivateKey.generate()

        def get_public(self):
            """Return the public key to send in the handshake"""

            return self._priv_key.public_key().public_bytes(Encoding.Raw,
                                                            PublicFormat.Raw)

        def get_shared(self, peer_public):
            """Return the shared key from the peer's public key"""

            peer_key = x25519.X25519PublicKey.from_public_bytes(peer_public)
            shared = self._priv_key.exchange(peer_key)
            return int.from_bytes(shared, 'big')
else: # pragma: no cover
    class Curve25519DH:
        """Curve25519 Diffie Hellman implementation based on libnacl"""

        def __init__(self):
            self._private = os.urandom(_CURVE25519_SCALARBYTES)

        def get_public(self):
            """Return the public key to send in the handshake"""

            public = ctypes.create_string_buffer(_CURVE25519_BYTES)

            if _curve25519_base(public, self._private) != 0:
                # This error is never returned by libsodium
                raise ValueError('Curve25519 failed') # pragma: no cover

            return public.raw

        def get_shared(self, peer_public):
            """Return the shared key from the peer's public key"""

            if len(peer_public) != _CURVE25519_BYTES:
                raise ValueError('Invalid curve25519 public key size')

            shared = ctypes.create_string_buffer(_CURVE25519_BYTES)

            if _curve25519(shared, self._private, peer_public) != 0:
                raise ValueError('Curve25519 failed')

            return int.from_bytes(shared.raw, 'big')

    try:
        from libnacl import nacl

        _CURVE25519_BYTES = nacl.crypto_scalarmult_curve25519_bytes()
        _CURVE25519_SCALARBYTES = \
            nacl.crypto_scalarmult_curve25519_scalarbytes()

        _curve25519 = nacl.crypto_scalarmult_curve25519
        _curve25519_base = nacl.crypto_scalarmult_curve25519_base

        curve25519_available = True
    except (ImportError, OSError, AttributeError):
        pass


class Curve448DH:
    """Curve448 Diffie Hellman implementation based on PyCA"""

    def __init__(self):
        self._priv_key = x448.X448PrivateKey.generate()

    def get_public(self):
        """Return the public key to send in the handshake"""

        return self._priv_key.public_key().public_bytes(Encoding.Raw,
                                                        PublicFormat.Raw)

    def get_shared(self, peer_public):
        """Return the shared key from the peer's public key"""

        peer_key = x448.X448PublicKey.from_public_bytes(peer_public)
        shared = self._priv_key.exchange(peer_key)
        return int.from_bytes(shared, 'big')
