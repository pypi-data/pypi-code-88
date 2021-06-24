from os.path import normpath
from urllib.parse import urljoin, urlparse, urlunparse


def absUrl( url, relatpath):
    return urljoin(url, relatpath)
