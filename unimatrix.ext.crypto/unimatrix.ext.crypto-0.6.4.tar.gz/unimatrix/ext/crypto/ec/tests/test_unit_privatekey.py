# pylint: skip-file
import asyncio
import hashlib
import unittest

import secp256k1
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature

from ...algorithms import SECP256K1SHA256
from .. import EllipticCurvePrivateKey


class EllipticCurvePrivateKeyTestCase(unittest.TestCase):

    def setUp(self):
        self.algorithm = SECP256K1SHA256
        self.private = EllipticCurvePrivateKey({
            'secret': 52343816702797894750525343876377824317010977684994482925768059918275240316046
        })

    def test_sign_and_verify(self):
        buf = hashlib.sha256(b'foo').digest()
        sig = asyncio.run(self.algorithm.sign(self.private, buf))
        asyncio.run(self.algorithm.verify(self.private, sig, buf))

    def test_sign_and_verify_with_secp256k1(self):
        buf = hashlib.sha256(b'foo').digest()
        pub = secp256k1.PublicKey(
            bytes(asyncio.run(self.private.get_public_key())), raw=True)
        sig = pub.ecdsa_deserialize(
            bytes(asyncio.run(self.algorithm.sign(self.private, buf)))
        )
        self.assertTrue(pub.ecdsa_verify(hashlib.sha256(b'foo').digest(),
            sig, raw=True))
