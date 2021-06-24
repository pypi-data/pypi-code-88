import requests
import os

from .error import APIError
from .session import Environment
from pyrasgo.schemas.user import UserRegistration, UserLogin
from pyrasgo.utils.monitoring import track_usage

class Register:

    @track_usage
    def login(self, payload: UserLogin):
        url = self._url(resource=f"/pyrasgo-login", api_version=1)
        response = requests.post(url, json=payload.__dict__)
        status_code = response.status_code
        if status_code == 200:
            return response.json()
        if status_code == 401 or status_code == 403:
            print("Username and/or password are incorrect. " \
                    "Please check your credentials " \
                    "or use the register() method to create a new account.")
            raise APIError("Unable to login. Please see warning message.")
        elif status_code == 400:
            print("Credentials Expired. Contact Rasgo Support.")
            raise APIError("Unable to login. Please see warning message.")

    @track_usage
    def register(self, payload: UserRegistration):
        url = self._url(resource=f"/pyrasgo-register", api_version=1)
        response = requests.post(url, json=payload.__dict__)
        status_code = response.status_code
        if status_code == 200:
            return response.json()
        elif status_code == 401:
            print("Invalid Registration. Password must be at least 6 characters")
            raise APIError("Unable to register user. Please see warning message.")
        else:
            print("Please register with a valid email address and password, " \
                    "or use the login() method if already registered")
            raise APIError("Unable to register user. Please see warning message.")

    def _url(self, resource, api_version=None):
        env = Environment.from_environment()
        if '/' == resource[0]:
            resource = resource[1:]
        protocol = 'http' if env.value == 'localhost' else 'https'
        return f"{protocol}://{env.value}/{'' if api_version is None else f'v{api_version}/'}{resource}"
