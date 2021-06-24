# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['upend']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'upend',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Tomáš Mládek',
    'author_email': 't@mldk.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
