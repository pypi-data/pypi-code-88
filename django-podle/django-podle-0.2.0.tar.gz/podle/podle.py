import json
import requests

from django.conf import settings


class PodleHttpClient:
    @staticmethod
    def make_request(url, method, data=None):
        # Build header
        access_token = settings.PODLE_AUTH_TOKEN
        headers = {
            "content-type": "application/json",
            "Authorization": "Bearer {}".format(access_token),
        }

        # Make HTTP request
        try:
            response = requests.request(method, url, json=data, headers=headers)
            result = response.text
        except Exception as e:
            raise e

        # Parse and return JSON Result
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            return None


class PodleHelper:
    """
    Podle helper to interact the API.
    https://docs.podle.io/
    """

    client = PodleHttpClient()
    endpoints = {
        "newsletters": "https://api.podle.io/v1/newsletters",
        "dictionaries": "https://api.podle.io/v1/dictionaries/default/words",
    }

    def create_newsletter(self, data):
        url = self.endpoints["newsletters"]
        return self.client.make_request(url, "POST", data)

    def retrieve_newsletter(self, newsletter_id):
        url = f"{self.endpoints['newsletters']}/{newsletter_id}"
        return self.client.make_request(url, "GET")

    def create_or_update_word(self, data):
        url = self.endpoints["dictionaries"]
        return self.client.make_request(url, "POST", data)

    def delete_word(self, word):
        url = f"{self.endpoints['dictionaries']}/{word}"
        return self.client.make_request(url, "DELETE")

    def lookup_word(self, word):
        url = f"{self.endpoints['dictionaries']}/{word}"
        return self.client.make_request(url, "GET")

    def lookup_all_words(self):
        url = self.endpoints["dictionaries"]
        return self.client.make_request(url, "GET")
