# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['tusky']
setup_kwargs = {
    'name': 'tusky',
    'version': '0.0.0',
    'description': 'Namespace squatting before the package is ready',
    'long_description': None,
    'author': 'Snapper',
    'author_email': 'LearningWithSnapper@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
