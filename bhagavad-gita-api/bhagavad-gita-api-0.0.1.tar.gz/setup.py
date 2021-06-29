# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gita_api',
 'gita_api.api',
 'gita_api.api.api_v2',
 'gita_api.api.api_v2.endpoints',
 'gita_api.db',
 'gita_api.models',
 'gita_api.schemas']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.19,<2.0.0',
 'fastapi>=0.65.2,<0.66.0',
 'graphene-elastic>=0.7,<0.8',
 'graphene-sqlalchemy-filter>=1.12.2,<2.0.0',
 'graphene-sqlalchemy>=2.3.0,<3.0.0',
 'psycopg2-pgevents>=0.2.2,<0.3.0',
 'python-dotenv>=0.18.0,<0.19.0',
 'pytz>=2021.1,<2022.0',
 'uvicorn>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'bhagavad-gita-api',
    'version': '0.0.1',
    'description': 'Bhagavad Gita API allows any developer to use content from Bhagavad Gita in their applications.',
    'long_description': '<!-- markdownlint-disable -->\n<p align="center">\n  <a href="https://bhagavadgita.io">\n    <img src=".github/gita.png" alt="Logo" width="300">\n  </a>\n\n  <h3 align="center">Bhagavad Gita API v2</h3>\n\n  <p align="center">\n    Code for the BhagavadGita.io v2 API, which is an app built for Gita readers by Gita readers.\n    <br />\n    <br />\n    <a href="https://api.bhagavadgita.io/docs">View Docs</a>\n    ·\n    <a href="https://github.com/gita/bhagavad-gita-api/issues">Report Bug</a>\n    ·\n    <a href="https://github.com/gita/bhagavad-gita-api/issues">Request Feature</a>\n  </p>\n</p>\n\n<p align="center">\n  <a href="https://github.com/gita/bhagavad-gita-api/blob/master/LICENSE">\n    <img alt="LICENSE" src="https://img.shields.io/badge/License-MIT-yellow.svg?maxAge=43200">\n  </a>\n  <a href="https://starcharts.herokuapp.com/gita/bhagavad-gita-api"><img alt="Stars" src="https://img.shields.io/github/stars/gita/bhagavad-gita-api.svg?style=social"></a>\n</p>\n\n## Usage\n\nIf you are interested in using this API for your application ... read the docs.\n\n## Projects\n\nProjects using this API.\n- bhagavatgita.io\n- Android app\n\nHave you build something with this API ? Open a "Show and tell" discussion. The maintainers will feature your project on the README if they find it interesting.\n\n## Self Hosting\n<!-- markdownlint-enable -->\n\n### Local/Linux VPS\n\nIf you want to deploy your own instance,You can deploy the API server on your system or VPS.\n\n- Using `pipx`\n\n    ```shell\n    pipx run gita-api\n    ```\n\n- Or using `docker`\n\n    ```shell\n    docker run -d --env-file=.env gita-org/gita-api\n    ```\n\nNow open `http://localhost:8081/docs` to see docs.\n\n### Heroku\n\nClick here  -> Configure env vars -> Deploy -> Open app\n\n### Digital Ocean\n\nOpen Dashboard -> Create -> Apps -> Docker Hub -> Repo name gita-org/gita-api -> Configure env vars\n\n## Configuration\n\nBy default SQLite database is used. But you may use any SQL database.\n\nIn your current directory, create a `.env` file with the following details.\n\nFor local/linux vps, you can use a `.env` file. For Heroku and Digital Ocean\nuse the UI provided in their Dashboard.\n\n## Development\n\nIf you are interested in contributing to this api, see the contributing guide.\nPRs are most welcome!\n\n- Feel free to create issues for bugs and feature requests\n- If you have any questions ask in the Discusion forum\n',
    'author': 'The Gita Initiative',
    'author_email': 'contact@bhagavadgita.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://bhagavadgita.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
