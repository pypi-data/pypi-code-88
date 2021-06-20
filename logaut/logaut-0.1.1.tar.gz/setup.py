# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['logaut',
 'logaut.backends',
 'logaut.backends.common',
 'logaut.backends.ltlf2dfa',
 'logaut.backends.lydia']

package_data = \
{'': ['*']}

install_requires = \
['pylogics>=0.1.0,<0.2.0', 'pythomata>=0.3.2,<0.4.0']

setup_kwargs = {
    'name': 'logaut',
    'version': '0.1.1',
    'description': 'From logic to automata.',
    'long_description': '<h1 align="center">\n  <b>logaut</b>\n</h1>\n\n<p align="center">\n  <a href="https://pypi.org/project/logaut">\n    <img alt="PyPI" src="https://img.shields.io/pypi/v/logaut">\n  </a>\n  <a href="https://pypi.org/project/logaut">\n    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/logaut" />\n  </a>\n  <a href="">\n    <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/logaut" />\n  </a>\n  <a href="">\n    <img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/logaut">\n  </a>\n  <a href="">\n    <img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/logaut">\n  </a>\n  <a href="https://github.com/whitemech/logaut/blob/master/LICENSE">\n    <img alt="GitHub" src="https://img.shields.io/github/license/marcofavorito/logaut">\n  </a>\n</p>\n<p align="center">\n  <a href="">\n    <img alt="test" src="https://github.com/whitemech/logaut/workflows/test/badge.svg">\n  </a>\n  <a href="">\n    <img alt="lint" src="https://github.com/whitemech/logaut/workflows/lint/badge.svg">\n  </a>\n  <a href="">\n    <img alt="docs" src="https://github.com/whitemech/logaut/workflows/docs/badge.svg">\n  </a>\n  <a href="https://codecov.io/gh/marcofavorito/logaut">\n    <img alt="codecov" src="https://codecov.io/gh/marcofavorito/logaut/branch/master/graph/badge.svg?token=FG3ATGP5P5">\n  </a>\n</p>\n<p align="center">\n  <a href="https://img.shields.io/badge/flake8-checked-blueviolet">\n    <img alt="" src="https://img.shields.io/badge/flake8-checked-blueviolet">\n  </a>\n  <a href="https://img.shields.io/badge/mypy-checked-blue">\n    <img alt="" src="https://img.shields.io/badge/mypy-checked-blue">\n  </a>\n  <a href="https://img.shields.io/badge/code%20style-black-black">\n    <img alt="black" src="https://img.shields.io/badge/code%20style-black-black" />\n  </a>\n  <a href="https://www.mkdocs.org/">\n    <img alt="" src="https://img.shields.io/badge/docs-mkdocs-9cf">\n  </a>\n</p>\n\n\nLOGics formalisms to AUTomata\n\n## What is `logaut`\n\nLogaut is to the logics-to-DFA problem\nwhat Keras is for Deep Learning:\na wrapper to performant back-ends,\nbut with human-friendly APIs.\n\n## Install\n\nTo install the package from PyPI:\n```\npip install logaut\n```\n\nMake sure to have [Lydia](https://github.com/whitemech/lydia) \ninstalled on your machine.\nWe suggest the following setup:\n\n- [Install Docker](https://www.docker.com/get-started)\n- Download the Lydia Docker image:\n```\ndocker pull whitemech/lydia:latest\n```\n- Make the Docker image executable under the name `lydia`.\n  On Linux and MacOS machines, the following commands should work:\n```\necho \'#!/usr/bin/env sh\' > lydia\necho \'docker run -v$(pwd):/home/default whitemech/lydia lydia $@\' >> lydia\nsudo chmod u+x lydia\nsudo mv lydia /usr/local/bin/\n```\n\nThis will install an alias to the inline Docker image execution\nin your system PATH. Instead of `/usr/local/bin/`\nyou may use another path which is still in the `PATH` variable.\n\n## Quickstart\n\nNow you are ready to go:\n```python\nfrom logaut import ltl2dfa\nfrom pylogics.parsers import parse_ltl\nformula = parse_ltl("F(a)")\ndfa = ltl2dfa(formula, backend="lydia")\n```\n\nThe function `ltl2dfa` takes in input a \n[pylogics](https://github.com/whitemech/pylogics) \n`formula` and gives in output\na [pythomata](https://github.com/whitemech/pythomata) DFA.\n\nThen, you can manipulate the DFA as done with Pythomata,\ne.g. to print:\n```\ndfa.to_graphviz().render("eventually.dfa")\n```\n\nCurrently, the `lydia` backend only supports\nthe `ltl` and `ldl` logics.\n\nThe `ltlf2dfa`, based on \n[LTLf2DFA](https://github.com/whitemech/LTLf2DFA/),\nsupports `ltl` and `pltl`.\nFirst, install it at version `1.0.1`:\n```\npip install git+https://github.com/whitemech/LTLf2DFA.git@develop#egg=ltlf2dfa\n```\n\nThen, you can use:\n```python\nfrom logaut import pltl2dfa\nfrom pylogics.parsers import parse_pltl\nformula = parse_pltl("a S b")\ndfa = pltl2dfa(formula, backend="ltlf2dfa")\n```\n\n## Write your own backend\n\nYou can write your back-end by implementing\nthe `Backend` interface:\n\n```python\nfrom logaut.backends.base import Backend\n\nclass MyBackend(Backend):\n\n    def ltl2dfa(self, formula: Formula) -> DFA:\n        """From LTL to DFA."""\n\n    def ldl2dfa(self, formula: Formula) -> DFA:\n        """From LDL to DFA."""\n\n    def pltl2dfa(self, formula: Formula) -> DFA:\n        """From PLTL to DFA."""\n\n    def pldl2dfa(self, formula: Formula) -> DFA:\n        """From PLDL to DFA."""\n        \n    def fol2dfa(self, formula: Formula) -> DFA:\n        """From FOL to DFA."""\n\n    def mso2dfa(self, formula: Formula) -> DFA:\n        """From MSO to DFA."""\n```\n\nThen, you can register the custom backend\nclass in the library:\n\n```python\nfrom logaut.backends import register\nregister(id_="my_backend", entry_point="dotted.path.to.MyBackend")\n```\n\nAnd then, use it through the main entry point:\n```python\ndfa = ltl2dfa(formula, backend="my_backend")\n```\n\n## Tests\n\nTo run tests: `tox`\n\nTo run only the code tests: `tox -e py3.7`\n\nTo run only the linters: \n- `tox -e flake8`\n- `tox -e mypy`\n- `tox -e black-check`\n- `tox -e isort-check`\n\nPlease look at the `tox.ini` file for the full list of supported commands. \n\n## Docs\n\nTo build the docs: `mkdocs build`\n\nTo view documentation in a browser: `mkdocs serve`\nand then go to [http://localhost:8000](http://localhost:8000)\n\n## License\n\nlogaut is released under the GNU Lesser General Public License v3.0 or later (LGPLv3+).\n\nCopyright 2021 WhiteMech\n\n## Authors\n\n- [Marco Favorito](https://marcofavorito.me/)\n',
    'author': 'Marco Favorito',
    'author_email': 'favorito@diag.uniroma1.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://marcofavorito.me/logaut',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
