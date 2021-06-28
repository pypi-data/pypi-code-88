# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['seismicsdk']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'seismicsdk',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Ula',
    'author_email': 'ula@test.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
