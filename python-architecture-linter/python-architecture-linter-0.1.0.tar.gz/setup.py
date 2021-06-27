# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_architecture_linter',
 'python_architecture_linter.ast_validators',
 'python_architecture_linter.domain_objects',
 'python_architecture_linter.domain_objects.tests',
 'python_architecture_linter.tests']

package_data = \
{'': ['*']}

install_requires = \
['astroid>=2.5.8,<3.0.0', 'click>=8.0.1,<9.0.0']

setup_kwargs = {
    'name': 'python-architecture-linter',
    'version': '0.1.0',
    'description': 'monorepo for the python architecture linter',
    'long_description': None,
    'author': 'Brian Graham',
    'author_email': 'Brian@statagroup.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
