# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arakneed']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'arakneed',
    'version': '0.1.0',
    'description': "A common use targeted concurrent crawler for any directed graph. It's designed to be easy to use.",
    'long_description': None,
    'author': 'arakneed',
    'author_email': 'arakneed@somarl.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
