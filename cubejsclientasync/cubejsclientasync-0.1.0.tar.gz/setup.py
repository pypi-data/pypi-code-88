# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cubejsclientasync']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.1.0,<3.0.0', 'backoff>=1.10.0,<2.0.0', 'httpx>=0.18.2,<0.19.0']

setup_kwargs = {
    'name': 'cubejsclientasync',
    'version': '0.1.0',
    'description': 'Async Python Cube.js client',
    'long_description': '# cubejsclientasync\n\n[![](https://img.shields.io/pypi/v/cubejsclientasync.svg)](https://pypi.org/pypi/cubejsclientasync/) [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)\n\nAsync Python Cube.js client\n\nFeatures:\n\n- Cube.js API client that makes async requests\n- Rich objects for building queries with measures, dimensions, etc.\n\nTable of Contents:\n\n- [Installation](#installation)\n- [Development](#development)\n\n## Installation\n\ncubejsclientasync requires Python 3.6 or above.\n\n```bash\npip install cubejsclientasync\n```\n\n## Development\n\nTo develop cubejsclientasync, install dependencies and enable the pre-commit hook:\n\n```bash\npip install pre-commit poetry\npoetry install\npre-commit install\n```\n\nTo run tests:\n\n```bash\npoetry shell\npytest\n```\n',
    'author': 'Jonathan Drake',
    'author_email': 'jdrake@narrativescience.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NarrativeScience/cubejs-client-async',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.5,<4.0.0',
}


setup(**setup_kwargs)
