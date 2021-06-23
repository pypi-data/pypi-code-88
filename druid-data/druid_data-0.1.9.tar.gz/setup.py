# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['druid_data']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.17.0,<2.0.0']

setup_kwargs = {
    'name': 'druid-data',
    'version': '0.1.9',
    'description': 'A library to store and retrieve python objects in a DynamoDB database. It supports the basic CRUD operations',
    'long_description': '# DruidData \n![PythonSupport](https://img.shields.io/static/v1?label=python&message=3.7%20|%203.8|%203.9&color=blue?style=flat-square&logo=python) ![PyPI version](https://badge.fury.io/py/druid_data.svg) ![PyPi monthly downloads](https://img.shields.io/pypi/dm/druid_data)\n\nA library to store and retrieve python objects in a DynamoDB database. It supports the basic CRUD operations\n\n## Features\n* **[dynamo_entity]()** - A decorator for classes whose objects will be stored in and retrived from the database\n\n* **[DynamoCrudRepository]()** - A tool to execute CRUD operations on DynamoDB using the classes decorated with the dynamo_entity decorator\n\n### Installation\nWith [pip](https://pip.pypa.io/en/latest/index.html) installed, run: ``pip install druid_data``\n\n## License\n\nThis library is licensed under the MIT-0 License. See the LICENSE file.',
    'author': 'Druid',
    'author_email': None,
    'maintainer': 'Fernando Magalhaes',
    'maintainer_email': 'fmagalhaes@druid.com.br',
    'url': 'https://github.com/druid-rio/druid-data',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
