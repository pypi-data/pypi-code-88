import requests
import json

from .auth import CoinbaseExchangeAuth
from .response_types import BuyPrice, SellPrice, SpotPrice, ServerTime


class CoinbaseApi:

    def __init__(
            self,
            api_key=None,
            api_secret_key=None,
            api_version='2021-03-01',
            api_url='https://api.coinbase.com',
            verbose=False
    ):
        if not api_key or not api_secret_key:
            print(
                'WARN: API Key details not all present, proceeding without authentication')
            self._auth = None
        else:
            self._auth = CoinbaseExchangeAuth(api_key, api_secret_key)
        self._api_url = api_url
        self._verbose = verbose
        self._api_version = api_version

    def _request(self, method, path, body=None, params=None):
        url = self._api_url + path

        if self._verbose:
            print(method, url)

        s = requests.Session()
        response = s.request(
            method,
            url,
            data=json.dumps(body) if body else None,
            params=params,
            auth=self._auth,
            headers={
                'CB-VERSION': self._api_version,
                'Content-Type': 'application/json'
            },
        )

        if response.status_code == 200:
            response_json = response.json()
            if self._verbose:
                print(json.dumps(response_json, indent=2))
            return response_json
        elif response.content:
            raise Exception(str(response.status_code) + ": " +
                            response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    def _data_request(self, method, path, body=None, params=None):
        response_json = self._request(method, path, body, params)
        return response_json.get('data')

    def get_buy_price(self, currency_pair):
        price = self._data_request('GET', f'/v2/prices/{currency_pair}/buy')
        return BuyPrice(price)

    def get_sell_price(self, currency_pair):
        price = self._data_request('GET', f'/v2/prices/{currency_pair}/sell')
        return SellPrice(price)

    def get_server_time(self):
        time = self._data_request('GET', '/v2/time')
        return ServerTime(time)

    # date format: YYYY-MM-DD
    def get_spot_price(self, currency_pair, date=None):
        params = {}
        if date:
            params['date'] = date

        price = self._data_request(
            'GET',
            f'/v2/prices/{currency_pair}/spot',
            params=params)
        return SpotPrice(price)

    # Requires auth; scopes:
    #   wallet:accounts:read
    #
    def list_accounts(self):
        return self._request('GET', '/v2/accounts')

    # next_uri should be something in the response body of a list request
    def get_next_page(self, next_uri):
        return self._request('GET', next_uri)

    # previous_uri should be something in the response body of a list request
    def get_previous_page(self, previous_uri):
        return self._request('GET', previous_uri)
