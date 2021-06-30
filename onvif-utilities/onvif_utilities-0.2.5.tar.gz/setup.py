# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onvif_utilities']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.17.1,<0.18.0', 'wsdiscovery>=2.0.0,<3.0.0', 'zeep>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'onvif-utilities',
    'version': '0.2.5',
    'description': '',
    'long_description': None,
    'author': 'MohammadHossein',
    'author_email': 'hos1377@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
