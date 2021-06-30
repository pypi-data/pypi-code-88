from mb_commons import Result
from tronpy.keys import PrivateKey

from mb_tron.tron.utils import get_tron_client

USDT_TOKEN_ADDRESS = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"  # nosec noqa


def get_balance(
    token_address: str,
    user_address: str,
    endpoint_uri="https://api.trongrid.io/",
    proxy=None,
    timeout=10,
    api_key=None,
) -> Result[int]:
    try:
        client = get_tron_client(endpoint_uri, proxy=proxy, timeout=timeout, api_key=api_key)
        contract = client.get_contract(token_address)
        balance = contract.functions.balanceOf(user_address)
        return Result(ok=balance)
    except Exception as e:
        return Result(error=str(e))


def transfer(
    token_address: str,
    from_address: str,
    private_key: str,
    to_address: str,
    amount: int,  # in the smallest unit
    endpoint_uri="https://api.trongrid.io/",
    proxy=None,
    timeout=10,
    api_key=None,
) -> Result[str]:
    try:
        client = get_tron_client(endpoint_uri, proxy=proxy, timeout=timeout, api_key=api_key)
        contract = client.get_contract(token_address)
        res = (
            contract.functions.transfer(to_address, amount)
            .with_owner(from_address)
            .build()
            .sign(PrivateKey(bytes.fromhex(private_key)))
            .broadcast()
        )
        if res.get("result") and "txid" in res:
            return Result(ok=res["txid"], data=res)
        else:
            return Result(error="unknown response", data=res)
    except Exception as e:
        return Result(error=str(e))


if __name__ == "__main__":
    # load_dotenv()
    # rrr = transfer(USDT_TOKEN_ADDRESS, os.getenv("ADDRESS_1"), os.getenv("PRIVATE_1"), os.getenv("ADDRESS_2"), 1 * 10 ** 6)
    # pprint(rrr.dict())
    pass
