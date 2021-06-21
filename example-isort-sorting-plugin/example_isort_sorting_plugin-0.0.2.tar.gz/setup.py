# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['example_isort_sorting_plugin']
install_requires = \
['natsort>=7.1.1,<8.0.0']

entry_points = \
{'isort.sort_function': ['natural_plus = '
                         'example_isort_sorting_plugin:natural_plus']}

setup_kwargs = {
    'name': 'example-isort-sorting-plugin',
    'version': '0.0.2',
    'description': 'An example plugin that modifies isorts sorting order to provide an even more natural sort by utilizing natsort.',
    'long_description': None,
    'author': 'Timothy Crosley',
    'author_email': 'timothy.crosley@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
