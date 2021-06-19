# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['omniblack', 'omniblack.caddy']

package_data = \
{'': ['*']}

install_requires = \
['attrs==21.2.0',
 'multidict>=5.1.0,<6.0.0',
 'requests>=2.25.1,<3.0.0',
 'urllib3>=1.26.5,<2.0.0']

extras_require = \
{'async': ['aiohttp[speedups]>=3.7.4,<4.0.0', 'anyio>=3.1.0,<4.0.0']}

setup_kwargs = {
    'name': 'omniblack.caddy',
    'version': '0.0.1rc9',
    'description': "A python client for Caddy's admin api.",
    'long_description': "A python client for Caddy's admin api.\n",
    'author': 'Terry Patterson',
    'author_email': 'Terryp@wegrok.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/terryp/caddy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
