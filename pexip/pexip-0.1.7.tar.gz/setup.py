# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pexip', 'pexip.cli']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['pexip = pexip.__main__:main']}

setup_kwargs = {
    'name': 'pexip',
    'version': '0.1.7',
    'description': 'Simple CLI utility to manually provision a Pexip Transcoder Client.',
    'long_description': None,
    'author': 'Colin Bruner',
    'author_email': 'colin.d.bruner@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
