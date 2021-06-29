# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['velogames']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.3,<5.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['velogames = velogames.cli:main']}

setup_kwargs = {
    'name': 'velogames',
    'version': '0.1.0',
    'description': 'Small tool for scraping Velogames data',
    'long_description': None,
    'author': 'Ossi Rajuvaara',
    'author_email': 'ossi@robocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
