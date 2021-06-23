# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['normie', 'normie.compat']

package_data = \
{'': ['*']}

install_requires = \
['setuptools>=56.0.0,<57.0.0']

entry_points = \
{'console_scripts': ['doctest = tools.run_tests:run_doctest',
                     'test = tools.run_tests:test']}

setup_kwargs = {
    'name': 'normie',
    'version': '0.3.0a1',
    'description': 'Accurate and efficient normal distribution statistics.',
    'long_description': None,
    'author': 'Jack Grahl',
    'author_email': 'jack.grahl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
