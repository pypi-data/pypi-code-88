# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bstops', 'bstops.security']

package_data = \
{'': ['*']}

install_requires = \
['bitarray>=2.1.3,<3.0.0',
 'pycrypto>=2.6.1,<3.0.0',
 'pyotp>=2.6.0,<3.0.0',
 'qrcode>=6.1,<7.0']

setup_kwargs = {
    'name': 'bstops-security',
    'version': '0.0.4',
    'description': '',
    'long_description': None,
    'author': 'walker',
    'author_email': 'walkerIVI@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
