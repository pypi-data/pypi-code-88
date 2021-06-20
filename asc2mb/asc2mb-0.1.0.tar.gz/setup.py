# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asc2mb']

package_data = \
{'': ['*']}

install_requires = \
['click==8.0']

entry_points = \
{'console_scripts': ['asc2mb = asc2mb.asc2mb:main']}

setup_kwargs = {
    'name': 'asc2mb',
    'version': '0.1.0',
    'description': 'Parse XML export from asc and format into two files suitable for upload',
    'long_description': None,
    'author': 'Adam Morris',
    'author_email': 'adam.morris@fariaedu.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
