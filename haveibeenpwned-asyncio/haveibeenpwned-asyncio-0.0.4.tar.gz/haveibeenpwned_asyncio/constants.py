from enum import Enum


class hashing(Enum):
    ENCODING = "utf-8"


class haveibeenpwned(Enum):
    """"""

    BASE_URL: str = "https://haveibeenpwned.com/api"
    PASSWORD_BASE_URL: str = "https://api.pwnedpasswords.com"
    API_VERSION: str = "/v3"
    HTTP_HEADER: dict = {
        "user-agent": "haveibeenpwned-asyncio-PyPi-Package",
        "hibp-api-key": "",
    }
    ACCOUNT_ENDPOINT: str = "breachedaccount"
    PASSWORD_ENDPOINT: str = "range"
    PASTES_ENDPOINT: str = "pasteaccount"
