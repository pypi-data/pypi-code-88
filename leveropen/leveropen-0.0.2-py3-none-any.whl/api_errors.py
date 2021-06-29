class APIError(Exception):

    info = (
        "See https://www.leveropen.com for information on "
        "how to obtain your personal Access Token."
    )

    def __init__(self, resp):
        super().__init__(f"{self.info}\nResponse {resp.status_code}: {resp.json()}")
