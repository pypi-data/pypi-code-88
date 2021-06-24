# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['textfile']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'textfile',
    'version': '0.1.0',
    'description': '',
    'long_description': '\nFunctions that enables us to write out or read from text file in shorter syntax\nthan using only standard library.\n\n\n\n',
    'author': 'kenjimaru',
    'author_email': 'kendimaru2@gmail.com',
    'maintainer': 'kenjimaru',
    'maintainer_email': 'kendimaru2@gmail.com',
    'url': 'https://github.com/kendimaru/textfile',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
