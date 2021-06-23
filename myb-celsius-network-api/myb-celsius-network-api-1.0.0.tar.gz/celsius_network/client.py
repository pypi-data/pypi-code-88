import requests
import gzip, json
import copy

from .auth import CelsiusNetworkAuth

class CelsiusNetworkApi:

    def __init__(
            self, 
            celsius_partner_token,
            user_api_key, 
            api_url='https://wallet-api.celsius.network', 
            verbose=False
    ):
        self._auth = CelsiusNetworkAuth(celsius_partner_token, user_api_key)
        self._api_url = api_url
        self._verbose = verbose

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
            auth=self._auth
        )

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    # Wallet Endoints

    def get_balance_summary(self):
        return self._request('GET', '/wallet/balance')

    def get_balance_coin(self, coin):
        return self._request('GET', f'/wallet/{coin}/balance')

    def get_transactions_summary(self, page, per_page=10):
        params = {
            'page': page,
            'per_page': per_page
        }
        return self._request('GET', f'/wallet/transactions', params=params)

    def get_transactions_for_coin(self, coin, page):
        params = {
            'page': page
        }
        return self._request('GET', f'/wallet/{coin}/transactions', params=params)
    
    def get_deposit_address_for_coin(self, coin):
        return self._request('GET', f'/wallet/{coin}/deposit')

    def withdraw_coin(self, coin, address, amount):
        body = {
            'address': address,
            'amount': amount
        }

        return self._request('POST', f'/wallet/{coin}/withdraw', body=body)

    def get_withdrawal_transaction_id(self, transaction):
        return self._request('GET', f'/wallet/transactions/{transaction}/status')

    # Utility Endpoints

    # This endpoint doesn't require authentication - auth headers are ignored
    def get_interest_rates(self):
        return self._request('GET', f'/util/interest/rates')