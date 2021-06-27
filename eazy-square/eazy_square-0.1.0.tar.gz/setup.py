# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['eazy_square']
setup_kwargs = {
    'name': 'eazy-square',
    'version': '0.1.0',
    'description': 'Square(w, h).draw(size)',
    'long_description': None,
    'author': 'fab4key',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
