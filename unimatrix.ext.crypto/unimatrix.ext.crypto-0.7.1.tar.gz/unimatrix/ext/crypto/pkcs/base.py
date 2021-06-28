"""Declares :class:`PKCSObject`."""
from .. import oid


class PKCSObject:
    capabilities = [
        oid.RSAPKCS1v15SHA256,
        oid.RSAPKCS1v15SHA384,
        oid.RSAPKCS1v15SHA512,
        oid.RSAOAEP
    ]
