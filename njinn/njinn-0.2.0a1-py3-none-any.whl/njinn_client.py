import requests
import json


class NjinnClient:
    def __init__(self, host: str, username: str, password: str) -> None:
        self.host = host.lstrip()
        self.auth = (username, password)
        self.headers = {"Content-Type": "application/json"}

    def __get_full_url(self, url: str):
        return f"{self.host}/{url}"

    def get(self, url, **kwargs):
        return self.request("GET", url, **kwargs)

    def post(self, url, data, **kwargs):
        return self.request("POST", url, json=data, **kwargs)

    def put(self, url, data, **kwargs):
        return self.request("PUT", url, json=data, **kwargs)

    def patch(self, url, data, **kwargs):
        return self.request("PATCH", url, json=data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("DELETE", url, **kwargs)

    def request(self, method, url, no_auth=False, **kwargs):
        if not no_auth:
            kwargs.setdefault("auth", self.auth)

        print("Sending request:", method, url)
        print(json.dumps(kwargs.get("json"), indent=2))

        response = requests.request(
            method, self.__get_full_url(url), headers=self.headers, **kwargs
        )

        try:
            response.raise_for_status()
        except Exception:
            print(response.text)
            raise

        if len(response.content) > 0:
            try:
                return response.json()
            except Exception:
                raise Exception("Error in response: " + response.content)
        else:
            return None
