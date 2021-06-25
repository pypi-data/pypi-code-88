# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dpy_docs']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=0.7.0,<0.8.0', 'discord.py>=1.7.3,<2.0.0']

setup_kwargs = {
    'name': 'dpy-docs',
    'version': '0.1.2',
    'description': 'A simple, lightweight tool used for documemting your discord.py commands',
    'long_description': None,
    'author': 'ChiliMX',
    'author_email': 'chili.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ChiliMX/dpy-docs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
