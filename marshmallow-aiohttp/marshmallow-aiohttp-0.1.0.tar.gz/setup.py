# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marshmallow_aiohttp']

package_data = \
{'': ['*']}

install_requires = \
['aiodns>=3.0,<4.0',
 'aiohttp>=3.7,<4.0',
 'marshmallow>=3.12,<4.0',
 'ujson>=4.0,<5.0']

setup_kwargs = {
    'name': 'marshmallow-aiohttp',
    'version': '0.1.0',
    'description': 'marshmallow-aiohttp',
    'long_description': '# marshmallow-aiohttp',
    'author': 'Gleb Karpushkin',
    'author_email': 'rugleb@gmail.com',
    'maintainer': 'Gleb Karpushkin',
    'maintainer_email': 'rugleb@gmail.com',
    'url': 'https://pypi.org/project/marshmallow-aiohttp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
