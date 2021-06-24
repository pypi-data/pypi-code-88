# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thechef_filler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'thechef-filler',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'kohkubo',
    'author_email': 'kohkubo@student.42tokyo.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
