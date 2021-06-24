import logging
import os


def setup_logger(debug):
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s] %(message)s", "%d-%m-%Y %H:%M:%S")
    console_handler.setFormatter(formatter)
    logging.basicConfig(
        level=logging.WARNING,
        handlers=[
            console_handler,
        ],
    )

    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.DEBUG if debug else logging.INFO)
    return _logger


class Settings:
    def __init__(self):
        self.QUERY_SERVICE_HOST = os.getenv(
            "OCEANIA_QUERY_SERVICE_HOST", "oceania-1.inriadev.cl"
        )
        self.QUERY_SERVICE_PORT = os.getenv("OCEANIA_QUERY_SERVICE_PORT", "7000")
        self.USE_SSL = os.getenv("OCEANIA_QUERY_SERVICE_HTTPS", "0") == "1"
        self.DEBUG = os.getenv("OCEANIA_DEBUG", "0") == "1"
        self.logger = setup_logger(self.DEBUG)

        if self.USE_SSL:
            protocol = "https://"
        else:
            protocol = "http://"
        self.API_URL = f"{protocol}{self.QUERY_SERVICE_HOST}:{self.QUERY_SERVICE_PORT}/"


settings = Settings()
