# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['signhere']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.2.0,<9.0.0', 'PyMuPDF>=1.18.13,<2.0.0']

setup_kwargs = {
    'name': 'signhere',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
