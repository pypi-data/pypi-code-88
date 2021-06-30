from dataclasses import dataclass

from tronpy.keys import PrivateKey, is_base58check_address


@dataclass
class NewAccount:
    address: str
    private_key: str


def generate_account() -> NewAccount:
    acc = PrivateKey.random()
    return NewAccount(address=acc.public_key.to_base58check_address(), private_key=acc.hex())


def is_valid_address(address: str) -> bool:
    try:
        return is_base58check_address(address)
    except ValueError:
        return False


def get_address_from_private_key(private_key: str) -> str:
    return PrivateKey(bytes.fromhex(private_key)).public_key.to_base58check_address()


if __name__ == "__main__":
    pass
