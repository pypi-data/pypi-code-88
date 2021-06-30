from base64 import urlsafe_b64decode, urlsafe_b64encode

from django.db import models
from ecdsa import NIST256p, SigningKey


class VAPIDKeyset(models.Model):
    _private_key = models.BinaryField(max_length=43)
    
    @property
    def private_key(self):
        if isinstance(self._private_key, memoryview):
            return self._private_key.tobytes()
        return self._private_key

    def __str__(self):
        return "public_key:{}... private_key:{}...".format(
            self.public_key[:10], self.private_key[:10]
        )

    @property
    def public_key(self):
        key_str = self.private_key
        padding = len(key_str) % 4
        key_str += b"=" * padding
        key = SigningKey.from_string(
            urlsafe_b64decode(key_str), curve=NIST256p
        ).get_verifying_key()
        return urlsafe_b64encode(b"\x04" + key.to_string()).strip(b"=")
