# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fenestrate']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.1.0,<2.0.0',
 'attrs>=21.2.0,<22.0.0',
 'icontract>=2.5.2,<3.0.0',
 'intervaltree>=3.1.0,<4.0.0',
 'toolz>=0.11.1,<0.12.0']

setup_kwargs = {
    'name': 'fenestrate',
    'version': '0.1.0a2',
    'description': '',
    'long_description': None,
    'author': 'Vic Putz',
    'author_email': 'vbputz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
