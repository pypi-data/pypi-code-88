import requests

from tuneuptechnology.customers import Customers
from tuneuptechnology.inventory import Inventory
from tuneuptechnology.locations import Locations
from tuneuptechnology.tickets import Tickets


class Client():
    def __init__(self, email=None, api_key=None, base_url='https://app.tuneuptechnology.com/api', timeout=10):
        self.email = email
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self._version = '3.0.0'

        if not self.email or not self.api_key:
            raise ValueError('Credentials are required to create a Client.')

    @property
    def Customers(self):
        return Customers(self.base_url, self.make_http_request)

    @property
    def Inventory(self):
        return Inventory(self.base_url, self.make_http_request)

    @property
    def Locations(self):
        return Locations(self.base_url, self.make_http_request)

    @property
    def Tickets(self):
        return Tickets(self.base_url, self.make_http_request)

    def make_http_request(self, method, endpoint, data=None):
        """Makes an HTTP request to the Tuneup Technology API."""
        headers = {
            'Accept': 'application/json',
            'User-Agent': f'TuneupTechnologyApp/PythonClient/{self._version}',
            'Email': self.email,
            'Api-Key': self.api_key,
        }

        try:
            request = requests.request(
                method=method,
                url=endpoint,
                json=data,
                headers=headers,
                timeout=self.timeout,
            )
        except Exception as error:
            raise Exception(error)

        return request.json()
