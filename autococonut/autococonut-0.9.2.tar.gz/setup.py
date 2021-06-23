# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autococonut', 'autococonut.engine']

package_data = \
{'': ['*'], 'autococonut': ['docs/*', 'templates/*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'Pillow>=8.2.0,<9.0.0',
 'mss>=6.1.0,<7.0.0',
 'pynput>=1.7.3,<2.0.0']

setup_kwargs = {
    'name': 'autococonut',
    'version': '0.9.2',
    'description': 'A workflow recording tool.',
    'long_description': None,
    'author': 'Lukáš Růžička',
    'author_email': 'lruzicka@redhat.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
