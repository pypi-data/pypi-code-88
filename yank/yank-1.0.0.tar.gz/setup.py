# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yank', 'yank.tools']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.11,<2.0.0',
 'arrow>=1.1.0,<2.0.0',
 'beautifulsoup4>=4.9.3,<5.0.0',
 'inflect>=5.3.0,<6.0.0',
 'lxml>=4.6.3,<5.0.0',
 'requests>=2.25.1,<3.0.0',
 'rich>=10.1.0,<11.0.0',
 'selenium-wire>=4.2.4,<5.0.0',
 'selenium>=3.141.0,<4.0.0',
 'tldextract>=3.1.0,<4.0.0',
 'undetected-chromedriver>=2.2.1,<3.0.0',
 'webdriver-manager>=3.4.0,<4.0.0',
 'xlwt>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'yank',
    'version': '1.0.0',
    'description': 'A high-level web scraping utility kit for Python 3 and above',
    'long_description': None,
    'author': 'khunspoonzi',
    'author_email': 'khunspoonzi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
