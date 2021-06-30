from decimal import Decimal

from mb_commons import Result
from tronpy.keys import PrivateKey

from mb_tron.tron.utils import get_tron_client


def get_balance(
    address: str,
    endpoint_uri="https://api.trongrid.io/",
    proxy=None,
    timeout=10,
    api_key=None,
) -> Result[Decimal]:
    try:
        client = get_tron_client(endpoint_uri, proxy=proxy, timeout=timeout, api_key=api_key)
        return Result(ok=client.get_account_balance(address))
    except Exception as e:
        return Result(error=str(e))


def transfer(
    from_address: str,
    private_key: str,
    to_address: str,
    amount: int,  # in SUN
    endpoint_uri="https://api.trongrid.io/",
    proxy=None,
    timeout=10,
    api_key=None,
) -> Result[str]:
    try:
        client = get_tron_client(endpoint_uri, proxy=proxy, timeout=timeout, api_key=api_key)
        r = client.trx.transfer(from_address, to_address, amount).build().sign(PrivateKey(bytes.fromhex(private_key))).broadcast()

        if r.get("result") and "txid" in r:
            return Result(ok=r["txid"], data=r)
        else:
            return Result(error="unknown response", data=r)
    except Exception as e:
        return Result(error=str(e))


if __name__ == "__main__":
    # load_dotenv()
    # print(transfer(os.getenv("ADDRESS_1"), os.getenv("PRIVATE_1"), os.getenv("ADDRESS_2"), 7 * 10 ** 6).dict())
    pass
