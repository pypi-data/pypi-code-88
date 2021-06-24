# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yuzu']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'yuzu',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Yasunori Horikoshi',
    'author_email': 'hotoku@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
