import requests


def get_btc_usd_value():
    r = requests.get('https://cex.io/api/last_price/BTC/USD')
    r.raise_for_status()
    return r.json()
