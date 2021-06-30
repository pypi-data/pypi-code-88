# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyquack', 'pyquack._async', 'pyquack.sync']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

extras_require = \
{'async': ['aiohttp>=3.7.4,<4.0.0']}

setup_kwargs = {
    'name': 'pyquack',
    'version': '0.1.1',
    'description': 'Simple Python sync/async duckduckgo wrapper.',
    'long_description': None,
    'author': 'anand2312',
    'author_email': 'anandkrishna2312@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://anand2312.tech/pyquack',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
