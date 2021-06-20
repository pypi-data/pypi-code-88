# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rashsetup',
 'rashsetup.Modules.General.Rash',
 'rashsetup.RashScrappers',
 'rashsetup.RashScrappers.RashScrappers',
 'rashsetup.RashScrappers.RashScrappers.spiders']

package_data = \
{'': ['*'],
 'rashsetup': ['Modules/General/Rash/Media/Gifs/*',
               'Modules/General/Rash/Media/Icons/*']}

setup_kwargs = {
    'name': 'rashsetup',
    'version': '0.0.8',
    'description': 'Setup Module that can be used for both testing Rash and also Setting up Rash',
    'long_description': None,
    'author': 'Rahul',
    'author_email': 'saihanumarahul66@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
