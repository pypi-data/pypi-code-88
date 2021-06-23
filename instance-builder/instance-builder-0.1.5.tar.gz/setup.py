# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['instance_builder']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'instance-builder',
    'version': '0.1.5',
    'description': 'Instance builder library for Python inspired by Lombok',
    'long_description': '# Instance-Builder - Instance builder library for Python inspired by Lombok\n\n![Python Versions](https://img.shields.io/pypi/pyversions/instance-builder.svg)\n![PyPI version](https://badge.fury.io/py/instance-builder.svg)\n![CI](https://github.com/shimech/instance-builder/actions/workflows/test.yml/badge.svg)\n\n## Installation\n\n```shell\npip install instance-builder\n```\n\n## Usage\n\n```python\n@builder("id", "name", "age", "email")\nclass User:\n    def __init__(self, id: int, name: str, age: int, email: str) -> None:\n        self.id = id\n        self.name = name\n        self.age = age\n        self.email = email\n\nuser = User.Builder().id(0).name("Shuntaro Shimizu").age(99).email("ut.s.shimizu@gmail.com").build()\n```\n\n© Copyright 2021 to Shuntaro Shimizu, under the MIT license\n',
    'author': 'Shuntaro Shimizu',
    'author_email': 'ut.s.shimizu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shimech/instance-builder',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
