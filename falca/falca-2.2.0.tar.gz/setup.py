# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['falca',
 'falca.cli',
 'falca.depends',
 'falca.media',
 'falca.middleware',
 'falca.plugins',
 'falca.serializers']

package_data = \
{'': ['*'], 'falca': ['templates/*']}

install_requires = \
['Mako>=1.1.4,<2.0.0',
 'falcon>=3.0.0,<4.0.0',
 'ipython>=7.23.1,<8.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'rich>=10.1.0,<11.0.0',
 'six>=1.15.0,<2.0.0',
 'typer[all]>=0.3.2,<0.4.0',
 'typing-inspect>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['falca = falca.cli.app:cli']}

setup_kwargs = {
    'name': 'falca',
    'version': '2.2.0',
    'description': 'Falca is an intuitive REST APIs framework based on the falcon framework.',
    'long_description': '# Falca\n\n![Logo](https://raw.githubusercontent.com/aprilahijriyan/falca/main/falca.png)\n\n![PyPI - Downloads](https://img.shields.io/pypi/dm/falca?color=yellow&logo=python) ![PyPI](https://img.shields.io/pypi/v/falca?color=yellow&logo=python) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/falca?color=purple&logo=python&logoColor=yellow) ![PyPI - Format](https://img.shields.io/pypi/format/falca?logo=python&logoColor=yellow) ![PyPI - Status](https://img.shields.io/pypi/status/falca?color=red) ![PyPI - License](https://img.shields.io/pypi/l/falca?color=black) ![GitHub issues](https://img.shields.io/github/issues/aprilahijriyan/falca?logo=github) ![GitHub closed issues](https://img.shields.io/github/issues-closed/aprilahijriyan/falca?color=green&logo=github) ![Scrutinizer code quality (GitHub/Bitbucket)](https://img.shields.io/scrutinizer/quality/g/aprilahijriyan/falca/main?logo=scrutinizer) ![Black Formatter](https://img.shields.io/badge/code%20style-black-000000.svg)\n\n<p align="center">\nFalca is an intuitive REST APIs framework.<br>\nPowered by https://falconframework.org/.<br><br>\n:warning: <i><strong>This is a BETA version please don\'t use it in a production environment. Thank you!</strong></i> :construction:<br>\n</p>\n\nGoals of this project:\n\n* Validates request body based on type hints.\n* (Pydantic & Marshmallow) support as object serialization and deserialization\n* Request body mapping\n* Nested routers\n* Plugin support\n* Settings (Global Configuration) support\n* Async Support\n* Routing sub-application\n* CLI\n* Dependency injection\n* Resource shortcut (`get`, `post`, `put`, `delete`, `websocket`, etc)\n\n# Contribution\n\n**Do not hesitate!**\n\nif you want to contribute like bug fixes, feature additions, etc. Please read our [contribution guidelines](https://github.com/aprilahijriyan/falca/blob/main/CONTRIBUTING.md).\n\n# Installation\n\nUsing `pip`:\n\n```\npip install falca\n```\n\nAlternatively, clone this repository and go to the `falca` directory:\n\n```\ngit clone https://github.com/aprilahijriyan/falca\ncd falca\n```\n\nInitialize the environment with python v3.7 using [poetry](https://python-poetry.org/)\n\n```\npoetry env use $(which python3.7)\n```\n\nInstall dependencies\n\n```\npoetry install --no-dev\n```\n\n# Usage\n\nLet\'s see how beautiful it is\n\n```python\n# app.py\n\nfrom typing import Optional\n\nfrom falca.app import ASGI\nfrom falca.depends.pydantic import Query\nfrom falca.responses import JSONResponse\nfrom falca.serializers.pydantic import Schema\n\n\nclass LimitOffsetSchema(Schema):\n    limit: Optional[int]\n    offset: Optional[int]\n\nclass Simple:\n    async def on_get(self, query: dict = Query(LimitOffsetSchema)):\n        return JSONResponse(query)\n\napp = ASGI(__name__)\napp.add_route("/", Simple())\n\n```\n\nSave the code above with filename `app.py`\nAnd run it with the command:\n\n```sh\nfalca runserver\n```\n\n**NOTE**: For the ASGI app, you need to install `uvicorn` before running it.\nAlso for other examples, you can find them [here](https://github.com/aprilahijriyan/falca/tree/main/examples)\n',
    'author': 'aprilahijriyan',
    'author_email': 'hijriyan23@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aprilahijriyan/falca',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
