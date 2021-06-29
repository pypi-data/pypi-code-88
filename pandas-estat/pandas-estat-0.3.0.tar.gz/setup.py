# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pandas_estat']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.1.4,<2.0.0', 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'pandas-estat',
    'version': '0.3.0',
    'description': 'Fetch e-Stat data as Pandas DataFrame.',
    'long_description': None,
    'author': 'Shota Imaki',
    'author_email': 'shota.imaki.0801@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/simaki/pandas-estat',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.13,<4.0.0',
}


setup(**setup_kwargs)
