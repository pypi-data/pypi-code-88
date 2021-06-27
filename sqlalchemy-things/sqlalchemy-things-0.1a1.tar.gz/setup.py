# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sqlalchemy_things',
 'sqlalchemy_things.declarative',
 'sqlalchemy_things.types']

package_data = \
{'': ['*']}

install_requires = \
['sqlalchemy>=1.4.18,<2.0.0']

extras_require = \
{'mysql': ['aiomysql>=0.0.21'],
 'postgresql': ['asyncpg>=0.23.0'],
 'sqlite': ['aiosqlite>=0.17.0']}

setup_kwargs = {
    'name': 'sqlalchemy-things',
    'version': '0.1a1',
    'description': '',
    'long_description': '=================\nsqlalchemy-things\n=================\n|ReadTheDocs| |PyPI release| |PyPI downloads| |License| |Python versions| |GitHub CI| |Codecov|\n\n.. |ReadTheDocs| image:: https://readthedocs.org/projects/sqlalchemy-things/badge/?version=latest\n  :target: https://sqlalchemy-things.readthedocs.io/en/latest/?badge=latest\n  :alt: Read The Docs build\n\n.. |PyPI release| image:: https://badge.fury.io/py/sqlalchemy-things.svg\n  :target: https://pypi.org/project/sqlalchemy-things/\n  :alt: Release\n\n.. |PyPI downloads| image:: https://img.shields.io/pypi/dm/sqlalchemy-things\n  :target: https://pypistats.org/packages/sqlalchemy-things\n  :alt: PyPI downloads count\n\n.. |License| image:: https://img.shields.io/badge/License-MIT-green\n  :target: https://github.com/ri-gilfanov/sqlalchemy-things/blob/master/LICENSE\n  :alt: MIT License\n\n.. |Python versions| image:: https://img.shields.io/badge/Python-3.8%20%7C%203.9-blue\n  :target: https://pypi.org/project/sqlalchemy-things/\n  :alt: Python version support\n\n.. |GitHub CI| image:: https://github.com/ri-gilfanov/sqlalchemy-things/actions/workflows/ci.yml/badge.svg?branch=master\n  :target: https://github.com/ri-gilfanov/sqlalchemy-things/actions/workflows/ci.yml\n  :alt: GitHub continuous integration\n\n.. |Codecov| image:: https://codecov.io/gh/ri-gilfanov/sqlalchemy-things/branch/master/graph/badge.svg\n  :target: https://codecov.io/gh/ri-gilfanov/sqlalchemy-things\n  :alt: codecov.io status for master branch\n',
    'author': 'Ruslan Ilyasovich Gilfanov',
    'author_email': 'ri.gilfanov@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ri-gilfanov/sqlalchemy-things',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
