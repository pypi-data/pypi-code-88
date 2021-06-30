from tronpy import Tron
from tronpy.providers import HTTPProvider


def get_tron_client(endpoint_uri="https://api.trongrid.io/", proxy=None, timeout=10, api_key=None) -> Tron:
    provider = HTTPProvider(endpoint_uri=endpoint_uri, timeout=timeout, api_key=api_key)
    if proxy:
        provider.sess.proxies = {"http": proxy, "https": proxy}
    client = Tron(provider=provider)
    return client


def to_sun(trx_amount) -> int:
    return int(trx_amount * 10 ** 6)
