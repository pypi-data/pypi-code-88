# pylint: skip-file
import asyncio
import unittest

from cryptography.hazmat.primitives.asymmetric import ec

from ...algorithms import SECP256K1SHA256
from .. import EllipticCurvePrivateKey


class EllipticCurvePrivateKeyTestCase(unittest.TestCase):

    def setUp(self):
        self.algorithm = SECP256K1SHA256
        self.private = EllipticCurvePrivateKey({
            'secret': 52343816702797894750525343876377824317010977684994482925768059918275240316046
        })

    def test_sign_and_verify(self):
        buf = b'foo'
        sig = asyncio.run(self.algorithm.sign(self.private, buf))
        asyncio.run(self.algorithm.verify(self.private, sig, buf))
