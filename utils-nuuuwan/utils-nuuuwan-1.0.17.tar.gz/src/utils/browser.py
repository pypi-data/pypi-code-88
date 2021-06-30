"""Browser utils."""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


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
        'text/csv',
    )

    options = Options()
    options.headless = True
    browser = webdriver.Firefox(
        options=options,
        firefox_profile=firefox_profile,
    )
    browser.get(url)
    return browser
