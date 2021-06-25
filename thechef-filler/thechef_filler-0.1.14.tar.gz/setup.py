# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['thechef_filler']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['thechef_filler = thechef_filler.cli:main']}

setup_kwargs = {
    'name': 'thechef-filler',
    'version': '0.1.14',
    'description': '',
    'long_description': None,
    'author': 'thechef',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
