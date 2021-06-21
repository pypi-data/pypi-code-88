# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['make_runner']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['mrun = make_runner.run:main']}

setup_kwargs = {
    'name': 'make-runner',
    'version': '0.1.0',
    'description': 'Enhanced Makefile-based task runner',
    'long_description': None,
    'author': 'Hiroyuki Deguchi',
    'author_email': 'deguchi.hiroyuki.db0@is.naist.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
