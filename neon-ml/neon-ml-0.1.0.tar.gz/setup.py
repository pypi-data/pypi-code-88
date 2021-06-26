# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neon', 'neon.features']

package_data = \
{'': ['*']}

install_requires = \
['gensim>=4.0.1,<5.0.0', 'numpy>=1.21.0,<2.0.0']

setup_kwargs = {
    'name': 'neon-ml',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'yutayamazaki',
    'author_email': 'tppymd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
