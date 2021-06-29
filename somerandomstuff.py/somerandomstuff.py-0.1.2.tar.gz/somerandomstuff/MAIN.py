import requests


class Session(object):
    def __init__(self):
        self.useless = ""
    @classmethod
    def get_fact(cls,endpoint) -> str:
            e = requests.get("https://some-random-api.ml/facts/{0}".format(endpoint))
            return e.json()['fact']
    @classmethod
    def get_image(cls,endpoint) -> str:
        e = requests.get("https://some-random-api.ml/img/{0}".format(endpoint))
        return e.json()['link']
    @classmethod
    def get_random_token(cls) -> str:
        e = requests.get("https://some-random-api.ml/bottoken")
        return e.json()['token']