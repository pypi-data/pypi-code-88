# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apis_highlighter', 'apis_highlighter.migrations']

package_data = \
{'': ['*'],
 'apis_highlighter': ['static/apis_highlighter/*',
                      'templates/apis_highlighter/*']}

install_requires = \
['apis-core>=0.16.14,<0.17.0']

setup_kwargs = {
    'name': 'apis-highlighter',
    'version': '0.8.11',
    'description': 'Highlighter module for annotations in APIS framework',
    'long_description': None,
    'author': 'Matthias Schlögl',
    'author_email': 'm.schloegl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.7',
}


setup(**setup_kwargs)
