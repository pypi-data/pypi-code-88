# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vjemmieapi',
 'vjemmieapi.crud',
 'vjemmieapi.exceptions',
 'vjemmieapi.models',
 'vjemmieapi.schemas']

package_data = \
{'': ['*']}

install_requires = \
['aiocache[memcached]>=0.11.1,<0.12.0',
 'aiomysql>=0.0.21,<0.0.22',
 'fastapi>=0.65.1,<0.66.0',
 'sqlalchemy>=1.4.18,<2.0.0']

extras_require = \
{u'server': ['uvicorn[standard]>=0.14.0,<0.15.0']}

setup_kwargs = {
    'name': 'vjemmieapi',
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'Peder Hovdan Andresen',
    'author_email': 'peder.andresen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
