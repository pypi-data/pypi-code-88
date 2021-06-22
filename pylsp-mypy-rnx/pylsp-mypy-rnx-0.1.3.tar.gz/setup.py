# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylsp_mypy_rnx']

package_data = \
{'': ['*']}

install_requires = \
['python-lsp-server>=1.0,<2.0', 'setuptools']

entry_points = \
{'pylsp': ['pylsp_mypy_rnx = pylsp_mypy_rnx.plugin']}

setup_kwargs = {
    'name': 'pylsp-mypy-rnx',
    'version': '0.1.3',
    'description': 'mypy-ls fork for more options',
    'long_description': '<p align="center"><strong>pylsp-mypy-rnx</strong> <em>- mypy-ls fork</em></p>\n\n<p align="center">\n<a href="https://github.com/gjeusel/pylsp-mypy-rnx/actions">\n    <img src="https://github.com/gjeusel/pylsp-mypy-rnx/workflows/Test%20Suite/badge.svg" alt="Test Suite">\n</a>\n<a href="https://pypi.org/project/pylsp-mypy-rnx/">\n    <img src="https://badge.fury.io/py/pylsp-mypy-rnx.svg" alt="Package version">\n</a>\n<a href="https://codecov.io/gh/gjeusel/pylsp-mypy-rnx">\n    <img src="https://codecov.io/gh/gjeusel/pylsp-mypy-rnx/branch/master/graph/badge.svg" alt="Codecov">\n</a>\n</p>\n\n---\n\n## Installation\n\n``` bash\npip install pylsp-mypy-rnx\n```\n\n\n## Develop\n\n```bash\npoetry install\npoetry run pre-commit install -t pre-push\npoetry run pytest\n```\n',
    'author': 'Guillaume Jeusel',
    'author_email': 'guillaume.jeusel@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gjeusel/pylsp-mypy-rnx',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
