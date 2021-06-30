"""Browser utils."""

import time
import logging

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from utils import filex

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('browserx')

MAX_T_WAIT = 60


def open_browser(url):
    """Open brower and return."""
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('browser.download.folderList', 2)
    firefox_profile.set_preference(
        'browser.download.manager.showWhenStarting',
        False,
    )
    firefox_profile.set_preference('browser.download.dir', '/tmp/')
    firefox_profile.set_preference(
        'browser.helperApps.neverAsk.saveToDisk',
        'application/xls;text/csv',
    )

    options = Options()
    options.headless = True
    browser = webdriver.Firefox(
        options=options,
        firefox_profile=firefox_profile,
    )
    browser.get(url)
    return browser


def find_elements_by_id_retry(browser, elem_id):
    """Find elements by id."""
    elems = None
    t_wait = 1
    while True:
        elems = browser.find_elements_by_id(elem_id)

        if len(elems) > 0:
            log.info('Found %d elems for id="%s"', len(elems), elem_id)
            return elems

        tmp_file = filex.get_tmp_file() + '.png'
        browser.save_screenshot(tmp_file)
        log.warning(
            'Could not find id="%s". Waiting for %ds. Saved screenshot to %s',
            elem_id,
            t_wait,
            tmp_file,
        )

        time.sleep(t_wait)
        t_wait *= 2
        if t_wait > MAX_T_WAIT:
            log.error('Could not find any id="%s"s. Aborting', elem_id)
            return None


def find_element_by_id_retry(browser, elem_id):
    """Find single element by id."""
    elems = find_elements_by_id_retry(browser, elem_id)
    if elems:
        return elems[0]
    return None


def scroll_to_bottom(browser):
    """Scroll to the bottom of the page."""
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def scroll_to_element(browser, elem):
    """Scroll to element."""
    browser.execute_script("arguments[0].scrollIntoView();", elem)


def find_scroll_and_click(browser, elem_id):
    """Find element, scroll to it and click."""
    elem = find_element_by_id_retry(browser, elem_id)
    scroll_to_element(browser, elem)
    elem.click()
    return elem
