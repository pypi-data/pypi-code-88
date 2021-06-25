import requests
from fgp.model.fgp_session import FGPSession
import copy

class Client:
    base_url: str = None
    application: str = None
    session: FGPSession = None
    headers: dict = None

    def __init__(self, url: str, application: str, headers: dict=None):
        self.base_url = url
        self.application = application
        self.headers = headers

    def call(self, method: str, route: str, data: dict = None, params: dict = None, headers: dict = None):
        url = f'{self.base_url}/{self.application}/{route}'
        method = method.lower()
        headers = {} if headers is None else headers
        if self.headers:
            headers_base = copy.copy(self.headers)
            headers_base.update(headers)
            headers = headers_base
        params = {} if params is None else params
        data = {} if data is None else data

        result = requests.request(
            url=url,
            params=params,
            method=method,
            json=data,
            headers=headers
        )

        if result.status_code >= 400:
            raise Exception(f'{method.upper()} {url} failed -  {result.reason}')

        try:
            if result.text == "" or result.text is None:
                return None
            return result.json()
        except ValueError as e:
            print(result)
            raise Exception(f'Invalid response received from API - {e}')

    def post(self, route: str, data: dict=None, params: dict=None):
        return self.call('post', route, data, params)

    def get(self, route: str, data: dict=None, params: dict=None):
        return self.call('get', route, data, params)

    def put(self, route: str, data: dict=None, params: dict=None):
        return self.call('put', route, data, params)

    def delete(self, route: str, params: dict=None):
        return self.call('get', route, data=None, params=params)
