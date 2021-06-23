# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_unpoly', 'tests']

package_data = \
{'': ['*'], 'django_unpoly': ['static/django_unpoly/*', 'templates/up/*']}

install_requires = \
['Django>=3.2.4,<4.0.0', 'fire==0.4.0']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0'],
 'doc': ['mkdocs>=1.1.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.13.6,<0.14.0',
         'mkdocs-autorefs==0.1.1'],
 'test': ['black==20.8b1',
          'isort==5.6.4',
          'flake8==3.8.4',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest==6.1.2',
          'pytest-cov==2.10.1']}

entry_points = \
{'console_scripts': ['django-unpoly = django_unpoly.cli:main']}

setup_kwargs = {
    'name': 'django-unpoly',
    'version': '0.1.1',
    'description': 'Unpoly integration for Django.',
    'long_description': '# django-unpoly\n\n\n<p align="center">\n<a href="https://pypi.python.org/pypi/django-unpoly">\n    <img src="https://img.shields.io/pypi/v/django-unpoly.svg"\n        alt = "Release Status">\n</a>\n\n<a href="https://github.com/jwaschkau/django-unpoly/actions">\n    <img src="https://github.com/jwaschkau/django-unpoly/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">\n</a>\n\n<a href="https://django-unpoly.readthedocs.io/en/latest/?badge=latest">\n    <img src="https://readthedocs.org/projects/django-unpoly/badge/?version=latest" alt="Documentation Status">\n</a>\n\n<a href="https://pyup.io/repos/github/jwaschkau/django-unpoly/">\n<img src="https://pyup.io/repos/github/jwaschkau/django-unpoly/shield.svg" alt="Updates">\n</a>\n\n</p>\n\n\nUnpoly 2 integration and utilities for Django\n\n\n* Free software: MIT\n* Documentation: <https://jwaschkau.github.io/django-unpoly/>\n\n\n## Features\n\n* Implements the Unpoly 2 Server protocol (https://unpoly.com/up.protocol)\n* Provides utilities for using Unpoly 2 with Django.\n* django-debug-toolbar support (https://github.com/jazzband/django-debug-toolbar).\n* django-concurrency support (https://github.com/saxix/django-concurrency).\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage) project template.\n',
    'author': 'Jannik Eilers',
    'author_email': 'j.waschkau@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jwaschkau/django-unpoly',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
