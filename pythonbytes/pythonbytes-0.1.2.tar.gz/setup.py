# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pythonbytes']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pythonbytes',
    'version': '0.1.2',
    'description': 'PythonBytes ep. #239 said so...',
    'long_description': None,
    'author': 'Scott Stoltzman',
    'author_email': 'stoltzmaniac@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/stoltzmaniac/pythonbytes',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
