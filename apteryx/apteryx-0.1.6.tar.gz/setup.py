# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apteryx', 'apteryx.google', 'apteryx.utils', 'apteryx.utils.http']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=2.9.0,<3.0.0',
 'google-auth-httplib2>=0.1.0,<0.2.0',
 'google-auth-oauthlib>=0.4.4,<0.5.0',
 'google-cloud-storage>=1.39.0,<2.0.0',
 'numpy>=1.20.3,<2.0.0',
 'pandas>=1.2.4,<2.0.0',
 'ray>=1.4.0,<2.0.0',
 'tqdm>=4.61.1,<5.0.0']

setup_kwargs = {
    'name': 'apteryx',
    'version': '0.1.6',
    'description': 'Utilities and useful things for Apteryx Labs',
    'long_description': None,
    'author': 'apteryxlabs',
    'author_email': 'matthew@apteryxlabs.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
