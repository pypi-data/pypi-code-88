import requests
from apitorch.utils import get_api_key, get_api_base_url
from urllib.parse import urljoin


class Client(object):
    def __init__(self):
        self.api_base_url = get_api_base_url()
        self.api_key = get_api_key()
        self.session = requests.Session()

    def get(self, path):
        url = urljoin(self.api_base_url, path)
        return self.session.get(url, auth=self.auth())

    def post(self, path, data):
        url = urljoin(self.api_base_url, path)
        return self.session.post(url, data, auth=self.auth())

    def auth(self):
        return (self.api_key, '')
