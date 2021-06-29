# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shutup']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'shutup',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Fred Israel',
    'author_email': 'fredpublico@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
