# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ebay_feedsdk',
 'ebay_feedsdk.config',
 'ebay_feedsdk.constants',
 'ebay_feedsdk.enums',
 'ebay_feedsdk.errors',
 'ebay_feedsdk.examples',
 'ebay_feedsdk.filter',
 'ebay_feedsdk.oauthclient',
 'ebay_feedsdk.oauthclient.model',
 'ebay_feedsdk.tests.oauthclient',
 'ebay_feedsdk.tests.sdk',
 'ebay_feedsdk.utils']

package_data = \
{'': ['*'],
 'ebay_feedsdk': ['sample-config/*'],
 'ebay_feedsdk.tests.oauthclient': ['config/*'],
 'ebay_feedsdk.tests.sdk': ['test-data/*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'SQLAlchemy>=1.3.8,<2.0.0',
 'aenum>=3.00,<4.0',
 'certifi>=2020.12.5,<2021.0.0',
 'pandas>=1.1.1,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'urllib3>=1.26.4,<2.0.0']

setup_kwargs = {
    'name': 'ebay-feedsdk',
    'version': '0.2.6',
    'description': 'Port of https://github.com/eBay/FeedSDK-Python and https://github.com/eBay/ebay-oauth-python-client to python3',
    'long_description': 'Feed SDK\n==========\nPython SDK for downloading and filtering item feed files including oauth authentication.\n\nForked and merged from [https://github.com/eBay/FeedSDK-Python](https://github.com/eBay/FeedSDK-Python) and [https://github.com/eBay/ebay-oauth-python-client](https://github.com/eBay/ebay-oauth-python-client) and ported to python3\n\nNothing serious changed, made it barely working. \n\nCode is not improved yet and would need some maintenance. \n\nAutomatic Tests not working due to the nature the tests were original programmed (you need to provide actual token etc.)\n\nAvailable as PyPI package under https://pypi.org/project/ebay-feedsdk/\n\nExample code to retrieve oauth token and download file (you need working ebay-config.yaml)\n\nSee ebay_feedsk/ebay_download_example.py for example how to download feed files\n\nSee also for details:\n\n* [https://github.com/eBay/ebay-oauth-python-client/blob/master/README.adoc](https://github.com/eBay/ebay-oauth-python-client/blob/master/README.adoc)\n* [https://github.com/eBay/FeedSDK-Python/blob/master/README.md](https://github.com/eBay/FeedSDK-Python/blob/master/README.md)\n',
    'author': 'Lars Erler',
    'author_email': 'lars@xaospage.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/taxaos/FeedSDK-Python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
