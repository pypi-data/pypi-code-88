from app.adapters import Explorer

import hashlib
from base58 import b58encode_check
from ecdsa import VerifyingKey


class P2PKH:
    def __init__(self, pem):
        self.public_key = pem

    @property
    def btc_public_key(self):
        vk = VerifyingKey.from_pem(self.public_key)
        btc_public_key = bytes.fromhex('04') + vk.to_string()

        return btc_public_key.hex()

    @property
    def address(self):
        sha256 = hashlib.sha256(bytes.fromhex(self.btc_public_key)).digest()

        ripemd160_hash = hashlib.new('ripemd160')
        ripemd160_hash.update(sha256)
        ripemd160 = ripemd160_hash.digest()

        hashed_btc_public_key = bytes.fromhex('00') + ripemd160

        addr = b58encode_check(hashed_btc_public_key).decode('utf-8')

        return addr

    @property
    def confirmed_balance(self):
        explorer = Explorer(address=self.address)
        return explorer.confirmed_balance

    @property
    def spent(self):
        explorer = Explorer(address=self.address)
        return explorer.spent
