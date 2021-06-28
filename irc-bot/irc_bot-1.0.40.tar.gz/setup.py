# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['irc_bot']

package_data = \
{'': ['*']}

install_requires = \
['future>=0.18.2,<0.19.0', 'six>=1.16.0,<2.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0']}

setup_kwargs = {
    'name': 'irc-bot',
    'version': '1.0.40',
    'description': 'A small library to create an IRC bot. Uses asyncore to ensure compatibility with Python 2.7+.',
    'long_description': "# IRC bot\n\nJust a small library based on asyncore that allows you to quickly create a small IRC bot\n\n## Pull Requests\nPull requests are welcome. The code base is a mess and I'm too lazy to fix it.\n",
    'author': 'Claus Vium',
    'author_email': 'clausvium@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cvium/irc_bot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
