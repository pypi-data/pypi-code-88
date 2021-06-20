# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['temprl']

package_data = \
{'': ['*']}

install_requires = \
['gym>=0.17.2,<0.18.0', 'numpy>=1.19.0,<2.0.0', 'pythomata==0.3.2']

setup_kwargs = {
    'name': 'temprl',
    'version': '0.3.0',
    'description': 'Framework for Reinforcement Learning with Temporal Goals.',
    'long_description': '<h1 align="center">\n  <b>temprl</b>\n</h1>\n\n<p align="center">\n  <a href="https://pypi.org/project/temprl">\n    <img alt="PyPI" src="https://img.shields.io/pypi/v/temprl">\n  </a>\n  <a href="https://pypi.org/project/temprl">\n    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/temprl" />\n  </a>\n  <a href="">\n    <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/temprl" />\n  </a>\n  <a href="">\n    <img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/temprl">\n  </a>\n  <a href="">\n    <img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/temprl">\n  </a>\n  <a href="https://github.com/whitemech/temprl/blob/master/LICENSE">\n    <img alt="GitHub" src="https://img.shields.io/github/license/whitemech/temprl">\n  </a>\n</p>\n<p align="center">\n  <a href="">\n    <img alt="test" src="https://github.com/whitemech/temprl/workflows/test/badge.svg">\n  </a>\n  <a href="">\n    <img alt="lint" src="https://github.com/whitemech/temprl/workflows/lint/badge.svg">\n  </a>\n  <a href="">\n    <img alt="docs" src="https://github.com/whitemech/temprl/workflows/docs/badge.svg">\n  </a>\n  <a href="https://codecov.io/gh/whitemech/temprl">\n    <img alt="codecov" src="https://codecov.io/gh/whitemech/temprl/branch/master/graph/badge.svg?token=FG3ATGP5P5">\n  </a>\n</p>\n<p align="center">\n  <a href="https://img.shields.io/badge/flake8-checked-blueviolet">\n    <img alt="" src="https://img.shields.io/badge/flake8-checked-blueviolet">\n  </a>\n  <a href="https://img.shields.io/badge/mypy-checked-blue">\n    <img alt="" src="https://img.shields.io/badge/mypy-checked-blue">\n  </a>\n  <a href="https://img.shields.io/badge/code%20style-black-black">\n    <img alt="black" src="https://img.shields.io/badge/code%20style-black-black" />\n  </a>\n  <a href="https://www.mkdocs.org/">\n    <img alt="" src="https://img.shields.io/badge/docs-mkdocs-9cf">\n  </a>\n</p>\n\nFramework for Reinforcement Learning with Temporal Goals defined by LTLf/LDLf formulas.\n\nStatus: **development**.\n\n## Install\n\nInstall the package:\n\n- from PyPI:\n\n\n        pip3 install temprl\n\n- with `pip` from GitHub:\n\n\n        pip3 install git+https://github.com/sapienza-rl/temprl.git\n\n\n- or, clone the repository and install:\n\n\n        git clone htts://github.com/sapienza-rl/temprl.git\n        cd temprl\n        pip install .\n\n\n## Tests\n\nTo run tests: `tox`\n\nTo run only the code tests: `tox -e py3.7`\n\nTo run only the linters: \n- `tox -e flake8`\n- `tox -e mypy`\n- `tox -e black-check`\n- `tox -e isort-check`\n\nPlease look at the `tox.ini` file for the full list of supported commands. \n\n## Docs\n\nTo build the docs: `mkdocs build`\n\nTo view documentation in a browser: `mkdocs serve`\nand then go to [http://localhost:8000](http://localhost:8000)\n\n## License\n\ntemprl is released under the GNU Lesser General Public License v3.0 or later (LGPLv3+).\n\nCopyright 2018-2020 Marco Favorito\n\n## Authors\n\n- [Marco Favorito](https://whitemech.github.io/)\n',
    'author': 'MarcoFavorito',
    'author_email': 'marco.favorito@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://whitemech.github.io/temprl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
