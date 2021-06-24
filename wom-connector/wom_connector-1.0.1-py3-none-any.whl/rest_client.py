import requests
import sys

from .wom_logger import WOMLogger

class RestClient:
    headers = {'Content-type': 'application/json'}
    __logger = WOMLogger("RestClient")

    def __init__(self, domain):
        self.__domain = domain

    @classmethod
    def __post_request(cls, payload, url):
        try:
            r = requests.post(url, data=payload, headers=RestClient.headers)
            cls.__logger.debug("POST {url} STATUS {code}".format(url=url, code=r.status_code))
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as err:
            cls.__logger.error(err)
            raise

    @classmethod
    def __post_command(cls, payload, url):
        try:
            r = requests.post(url, data=payload, headers=RestClient.headers)
            cls.__logger.debug("POST {url} STATUS {code}".format(url=url, code=r.status_code))
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            cls.__logger.error(err)
            raise

    def registry_pkey_retrieve(self):
        try:
            url = "https://" + self.__domain + "/api/v1/auth/key"
            r = requests.get(url, headers=RestClient.headers)
            self.__logger.debug("GET {url} STATUS {code}".format(url=url, code=r.status_code))
            r.raise_for_status()
            return r.text
        except requests.exceptions.HTTPError as err:
            cls.__logger.error(err)
            raise

    def voucher_create(self, payload):
        url = "http://" + self.__domain + "/api/v1/voucher/create"

        return RestClient.__post_request(payload, url)

    def voucher_verify(self, payload):
        url = "http://" + self.__domain + "/api/v1/voucher/verify"

        RestClient.__post_command(payload, url)

    def payment_register(self, payload):
        url = "http://" + self.__domain + "/api/v1/payment/register"

        return RestClient.__post_request(payload, url)

    def payment_verify(self, payload):
        url = "http://" + self.__domain + "/api/v1/payment/verify"

        RestClient.__post_command(payload, url)
