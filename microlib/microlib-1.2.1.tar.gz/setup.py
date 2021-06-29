# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['microlib']

package_data = \
{'': ['*'], 'microlib': ['data/*', 'meta/*']}

install_requires = \
['blessed>=1.18.1,<2.0.0', 'click>=8.0.1,<9.0.0', 'toml>=0.10.2,<0.11.0']

extras_require = \
{':python_version >= "3.6.0" and python_version < "3.8.0"': ['importlib-metadata>=3.1,<4.0']}

setup_kwargs = {
    'name': 'microlib',
    'version': '1.2.1',
    'description': '',
    'long_description': None,
    'author': 'Nicolas Hainaux',
    'author_email': 'nh.techn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
