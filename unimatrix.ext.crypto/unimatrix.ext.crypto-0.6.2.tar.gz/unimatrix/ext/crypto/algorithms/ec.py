# pylint: disable=line-too-long
"""Declares Elliptic Curve (EC) algorithms."""
import hashlib

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

from .. import oid
from .signing import SigningAlgorithm

__all__ = [
    'SECP256K1SHA256'
]


class ECDSA(SigningAlgorithm):

    def __init__(self, oid, curve, hashfunc):
        self.oid = oid
        self.curve = curve
        self.hashfunc = hashfunc

    def get_sign_parameters(self, key) -> dict:
        algorithm = self.hashfunc()
        return {
            'algorithm': algorithm,
            'hasher': hashes.Hash(algorithm),
            'curve': self.curve()
        }

    def get_verify_parameters(self, key) -> dict:
        algorithm = self.hashfunc()
        return {
            'algorithm': algorithm,
            'hasher': hashes.Hash(algorithm),
            'curve': self.curve()
        }


SECP256K1SHA256 = ECDSA(oid.SECP256K1, ec.SECP256K1, hashes.SHA256)
