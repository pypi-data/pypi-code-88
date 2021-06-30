# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['renag', 'renag.tests']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.17,<4.0.0', 'pyparsing>=2.4.7,<3.0.0']

entry_points = \
{'console_scripts': ['renag = renag.__main__:main']}

setup_kwargs = {
    'name': 'renag',
    'version': '0.3.5',
    'description': 'A Regex based linter tool that works for any language and works exclusively with custom linting rules.',
    'long_description': None,
    'author': 'Ryan',
    'author_email': 'ryanpeach@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
