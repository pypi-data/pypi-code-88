# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['instance_builder']

package_data = \
{'': ['*']}

install_requires = \
['autopep8>=1.5.7,<2.0.0',
 'keyring>=23.0.1,<24.0.0',
 'pytest>=6.2.4,<7.0.0',
 'twine>=3.4.1,<4.0.0',
 'wheel>=0.36.2,<0.37.0']

setup_kwargs = {
    'name': 'instance-builder',
    'version': '0.1.0',
    'description': 'Instance builder library for Python inspired by Lombok',
    'long_description': None,
    'author': 'Shuntaro Shimizu',
    'author_email': 'ut.s.shimizu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
