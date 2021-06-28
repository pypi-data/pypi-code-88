"""Declares :class:`GoogleManagedKey`."""
from .const import CRYPTO_KEY_ALGORITHMS_OIDS
from .const import GOOGLE_SYMMETRIC_ENCRYPTION
from .client import GoogleKMSClient
from .googlemanagedkey import GoogleManagedKey
from .kmsloader import KMSLoader
from .secretmanagerloader import SecretManagerKeyLoader


SecretManagerLoader = SecretManagerKeyLoader

__all__ = [
    'KMSLoader',
    'SecretManagerLoader'
]
