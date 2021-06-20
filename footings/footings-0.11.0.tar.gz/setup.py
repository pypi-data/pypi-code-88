# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['footings', 'footings.io']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20.0,<21.0',
 'numpy>=1.11,<2.0',
 'openpyxl>=3.0,<4.0',
 'pandas>=1.0,<2.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=3.0,<4.0']}

setup_kwargs = {
    'name': 'footings',
    'version': '0.11.0',
    'description': 'A model building library',
    'long_description': '# Footings - A Model Building Library\n\n![tests](https://github.com/footings/footings/workflows/tests/badge.svg)\n[![gh-pages](https://github.com/footings/footings/workflows/gh-pages/badge.svg)](https://footings.github.io/footings/main/)\n[![license](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)\n[![codecov](https://codecov.io/gh/dustindall/footings/branch/main/graph/badge.svg?token=SC5BHMYBSN)](https://codecov.io/gh/dustindall/footings)\n![version](https://img.shields.io/pypi/pyversions/footings.svg)\n[![PyPI version](https://badge.fury.io/py/footings.svg)](https://badge.fury.io/py/footings)\n\n## What is it?\n\nFootings is a model building Python library. No out-of-the box models are provided. Instead it is a framework library that provides key objects and functions to help users  construct custom models.\n\n## Purpose\n\nThe footings library was developed with the intention of making it easier to develop actuarial models in Python. Actuarial models are a mix of data engineering and math/calculations. In addition, actuarial models are usually not defined by one calculation, but a series of calculations. So even though the original purpose is actuarial work, if the problem at hand sounds familiar, others might find this library useful.\n\n## Principles\n\nThe Footings library was designed as framework library using the below principles -\n\n- Models are a sequence of linked steps\n- Models need to be easy to understand\n- Models need to have validation built in\n- Models need to be easy to audit\n- Models need to be self documenting\n- Models need to be able to scale up\n- Models need to be able to build off other models\n- Model environments should not be monolithic\n\n**These all become easier when you can leverage the amazing Python and wider open source ecosystems.**\n\n## Installation\n\nTo install from PyPI run -\n\n```\npip install footings\n```\n\nTo install the latest version on github run -\n\n```\npip install git+https://github.com/foootings/footings-core.git\n```\n\n## License\n[BSD 3](LICENSE)\n\n\n## Changelog\n\n[File](./docs/changelog.md)\n',
    'author': 'Dustin Tindall',
    'author_email': 'dustin.tindall@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/footings/footings',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
