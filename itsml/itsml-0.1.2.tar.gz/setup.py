# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['itsml', 'itsml.feature_extraction', 'itsml.preprocessing']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.20.1,<2.0.0',
 'pandas>=1.2.3,<2.0.0',
 'scikit-learn>=0.24.2,<0.25.0',
 'setuptools>=57.0.0,<58.0.0']

entry_points = \
{'console_scripts': ['fmt = scripts.code_quality:do_code_formatting',
                     'fmt-check = scripts.code_quality:check_code_formatting',
                     'isort-check = scripts.code_quality:check_import_order',
                     'isort-fmt = scripts.code_quality:sort_import_order',
                     'linter = scripts.code_quality:linter',
                     'tests = scripts.code_quality:run_tests']}

setup_kwargs = {
    'name': 'itsml',
    'version': '0.1.2',
    'description': 'Tools for doing machine learning with some of my custom transformers.',
    'long_description': None,
    'author': 'Alexandre Farias',
    'author_email': '0800alefarias@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
