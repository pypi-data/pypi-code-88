import requests
import json


class NjinnClient:
    def __init__(
        self, host: str, username: str = None, password: str = None, token: str = None
    ) -> None:
        self.host = host.strip()
        if self.host.endswith("/"):
            self.host = self.host[:-1]

        self._headers = {"Content-Type": "application/json"}
        
        if token is None:
            assert username is not None and password is not None
            self._auth = (username, password)
            self._headers = None
        else:
            self._auth = None
            self._headers["Authorization"] = f"JWT {token}"

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
        headers = self._headers
        if not no_auth:
            if self._auth is not None:
                kwargs.setdefault("auth", self._auth)
        else:
            del headers["Authorization"]

        print("Sending request:", method, url)
        print(json.dumps(kwargs.get("json"), indent=2))

        response = requests.request(
            method, self.__get_full_url(url), headers=headers, **kwargs
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
