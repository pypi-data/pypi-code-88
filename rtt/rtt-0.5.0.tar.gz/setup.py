# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rtt']

package_data = \
{'': ['*']}

install_requires = \
['tabulate>=0.8.9,<0.9.0']

entry_points = \
{'console_scripts': ['rtt = rtt:cli']}

setup_kwargs = {
    'name': 'rtt',
    'version': '0.5.0',
    'description': '',
    'long_description': None,
    'author': 'tlonny',
    'author_email': 't@lonny.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
