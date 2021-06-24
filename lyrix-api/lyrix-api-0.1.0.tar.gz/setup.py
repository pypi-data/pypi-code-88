# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lyrix_api']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'lyrix-api',
    'version': '0.1.0',
    'description': 'Python bindings for Lyrix backend',
    'long_description': None,
    'author': 'Srevin Saju',
    'author_email': 'srevinsaju@sugarlabs.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
