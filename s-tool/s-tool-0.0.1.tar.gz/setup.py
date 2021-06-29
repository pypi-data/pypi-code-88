# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['s_tool', 's_tool.utils']

package_data = \
{'': ['*']}

install_requires = \
['selenium>=3.141.0,<4.0.0', 'webdriver-manager>=3.4.2,<4.0.0']

setup_kwargs = {
    'name': 's-tool',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
