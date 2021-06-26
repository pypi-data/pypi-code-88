# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['state']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pystates3',
    'version': '0.1.0',
    'description': 'State aware system implemented in python',
    'long_description': None,
    'author': 'Jaschar Domann',
    'author_email': 'jasjisdo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
