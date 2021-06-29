# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['daschat_base']

package_data = \
{'': ['*']}

install_requires = \
['cuid>=0.3,<0.4', 'loguru>=0.5.3,<0.6.0', 'pydantic>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'daschat-base',
    'version': '0.4.0',
    'description': 'Base package for Daschat modules.',
    'long_description': '# daschat-handsoff-base\n\nBase package for the development of integration modules with chat applications for the handsoff of conversations.\n\n\n<p align="center">\n<a href="https://www.python.org/">\n    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"\n        alt = "Made with Python">\n</a>\n\n<a href="https://pypi.python.org/pypi/daschat_base">\n    <img src="https://img.shields.io/pypi/v/daschat_base.svg"\n        alt = "Release Status">\n</a>\n\n<a href="https://github.com/daschat-io/daschat_base/actions">\n    <img src="https://github.com/daschat-io/daschat_base/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">\n</a>\n\n<!-- <a href="https://daschat-handsoff-base.readthedocs.io/en/latest/?badge=latest">\n    <img src="https://readthedocs.org/projects/daschat-base/badge/?version=latest" alt="Documentation Status">\n</a> -->\n\n</p>\n\n## Features\n\n* Free software: MIT\n* Documentation: <https://daschat-io.github.io/daschat_base/>\n\n\n## Enabling Python versions\n\nInstall Python versions using `pyenv` and enable all versions to be used with `tox`:\n\n``` console\n$ pyenv install 3.8.10 3.9.5\n$ pyenv shell 3.8.10 3.9.5\n$ pyenv local 3.8.10\n```\n\n## Acknowledgements\n\n - [Cookiecutter](https://github.com/audreyr/cookiecutter)\n - [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage)\n - [Naereen/badges](https://github.com/Naereen/badges)\n',
    'author': 'Abner G Jacobsen',
    'author_email': 'abner@apoana.com.br',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/daschat-io/daschat_base',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
