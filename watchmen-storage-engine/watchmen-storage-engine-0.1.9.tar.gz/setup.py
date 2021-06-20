# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['storage',
 'storage.common',
 'storage.config',
 'storage.mongo',
 'storage.mongo.engine',
 'storage.mysql',
 'storage.mysql.dbscript',
 'storage.mysql.model',
 'storage.oracle',
 'storage.snowflake',
 'storage.storage',
 'storage.utils']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.1.0,<2.0.0',
 'cx-Oracle>=8.2.1,<9.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'pymongo>=3.11.4,<4.0.0']

setup_kwargs = {
    'name': 'watchmen-storage-engine',
    'version': '0.1.9',
    'description': '',
    'long_description': None,
    'author': 'luke0623',
    'author_email': 'luke0623@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
