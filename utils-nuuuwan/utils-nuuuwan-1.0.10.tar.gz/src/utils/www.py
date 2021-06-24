"""Utils for reading remote files."""
import json
import logging
import ssl
import time

import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from utils import filex, tsv

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0)' \
    + 'Gecko/20100101 Firefox/65.0'
ENCODING = 'utf-8'
SELENIUM_SCROLL_SCRIPT = "window.scrollTo(0, document.body.scrollHeight);"
SELENIUM_SCROLL_REPEATS = 3
SELENIUM_SCROLL_WAIT_TIME = 0.5

# pylint: disable=W0212
ssl._create_default_https_context = ssl._create_unverified_context


def _read_helper(url):
    try:
        logging.debug('utils.www._read_helper: %s', url)
        resp = requests.get(url, headers={'user-agent': USER_AGENT})

        if resp.status_code != 200:
            return None

        return resp.content

    except requests.exceptions.ConnectionError:
        return None


def _read_helper_selenium(url):
    options = Options()
    options.headless = True

    browser = webdriver.Firefox(options=options)
    browser.get(url)

    for _ in range(0, SELENIUM_SCROLL_REPEATS):
        browser.execute_script(SELENIUM_SCROLL_SCRIPT)
        time.sleep(SELENIUM_SCROLL_WAIT_TIME)

    content = browser.page_source
    browser.quit()
    return content


def read(url, use_selenium=False):
    """Read url.

    Args:
        url (str): URL

    Return:
        Contents at URL

    """
    if use_selenium:
        content = _read_helper_selenium(url)
    else:
        content = _read_helper(url)
        if content:
            content = content.decode(ENCODING)

    return content


def read_json(url):
    """Read JSON content from url.

    Args:
        url (str): URL

    Return:
        JSON parsed data at URL

    """
    try:
        return json.loads(read(url))
    except TypeError:
        return None


def read_tsv(url):
    """Read TSV content from url.

    Args:
        url (str): URL

    Return:
        TSV parsed data at URL
    """
    csv_lines = read(url).split('\n')
    return tsv._read_helper(csv_lines)


def download_binary(url, file_name):
    """Download binary.

    Args:
        url (str): URL
        file_name (str): file name for output
    """
    content = _read_helper(url)
    filex.write(file_name, content, 'wb')
    logging.debug(
        'Wrote %dB from %s to %s',
        len(content),
        url,
        file_name,
    )


def exists(url):
    """Check if URL exists."""
    try:
        response = requests.head(url, timeout=1)
    except requests.exceptions.ConnectTimeout:
        return False
    return response.status_code == requests.codes.ok


def get_all_urls(root_url):
    """Get all URLs linked to a webpage."""
    soup = BeautifulSoup(read(root_url), 'html.parser')
    urls = []
    for a_link in soup.find_all('a', href=True):
        urls.append(a_link['href'])
    logging.debug('Found %d links on %s', len(urls), root_url)
    return urls
