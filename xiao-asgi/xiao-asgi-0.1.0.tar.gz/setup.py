# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xiao_asgi']

package_data = \
{'': ['*']}

install_requires = \
['pytest-asyncio>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'xiao-asgi',
    'version': '0.1.0',
    'description': 'A small ASGI framework.',
    'long_description': '# xiao asgi\n[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)\n\nA small ASGI framework.\n\n## License\n\nxiao asgi is open-sourced software licensed under the MIT license.\n',
    'author': 'Jonathan Staniforth',
    'author_email': 'jonathanstaniforth@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/limber-project/limberframework',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
