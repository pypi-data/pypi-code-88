# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dbgen',
 'dbgen.cli',
 'dbgen.cli.newfiles',
 'dbgen.core',
 'dbgen.core.airflow_plugin',
 'dbgen.core.expr',
 'dbgen.core.model',
 'dbgen.example',
 'dbgen.example.generators',
 'dbgen.example.scripts',
 'dbgen.templates',
 'dbgen.utils']

package_data = \
{'': ['*'], 'dbgen.example': ['data/*'], 'dbgen.utils': ['config_templates/*']}

install_requires = \
['hypothesis>=5.23.7',
 'infinite>=0.1',
 'jinja2>=2.10.0',
 'networkx>=2.4',
 'pathos>=0.2.6',
 'psycopg2-binary>=2.7.4',
 'sshtunnel>=0.1.5,<0.2.0',
 'tqdm>=4.48.0',
 'typer>=0.3.2,<0.4.0']

extras_require = \
{':extra == "docs"': ['pdocs>=1.1.1,<2.0.0'],
 'airflow': ['apache-airflow[postgres]>=2.1.0,<3.0.0'],
 'docs': ['markdown-include==0.6.0',
          'mkdocs>=1.1.2,<2.0.0',
          'mkdocs-autorefs>=0.1.1,<0.2.0',
          'mkdocs-markdownextradata-plugin>=0.2.4,<0.3.0',
          'mkdocs-material>=7.0.6,<8.0.0',
          'mkdocstrings>=0.15.0,<0.16.0']}

entry_points = \
{'console_scripts': ['dbgen = dbgen.__main__:main']}

setup_kwargs = {
    'name': 'modelyst-dbgen',
    'version': '0.4.6',
    'description': 'DBgen (Database Generator) is an open-source Python library for connecting raw data, scientific theories, and relational databases',
    'long_description': '<!--\n   Copyright 2021 Modelyst LLC\n\n   Licensed under the Apache License, Version 2.0 (the "License");\n   you may not use this file except in compliance with the License.\n   You may obtain a copy of the License at\n\n       http://www.apache.org/licenses/LICENSE-2.0\n\n   Unless required by applicable law or agreed to in writing, software\n   distributed under the License is distributed on an "AS IS" BASIS,\n   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n   See the License for the specific language governing permissions and\n   limitations under the License.\n -->\n\n# DBgen\n\n<p align="center">\n  <a href="https://dbgen.modelyst.com"><img src="docs/img/dbgen_logo.png" alt="DBgen"></a>\n</p>\n---\n\n**Documentation**: <a href="https://dbgen.modelyst.com" target="_blank">https://dbgen.modelyst.com</a>\n\n**Github**: <a href="https://github.com/modelyst/dbgen" target="_blank">https://github.com/modelyst/dbgen</a>\n\n---\n\nDBgen (Database Generator) is an open-source Python library for\nconnecting raw data, scientific theories, and relational databases.\nThese are some of the main features:\n\n1.  Very easy to work with\n2.  Integration with the PostgreSQL databases.\n\nDBgen was initially developed by [Modelyst](https://www.modelyst.com/).\n\n## What is DBgen?\n\nDBgen was designed to support scientific data analysis with the following\ncharacteristics:\n\n1.  Transparent\n\n    - Because scientific efforts ought be shareable and mutually\n      understandable.\n\n2.  Flexible\n\n    - Because scientific theories are under continuous flux.\n\n3.  Maintainable\n    - Because the underlying scientific models one works with are\n      complicated enough on their own, we can\'t afford to introduce\n      any more complexity via our framework.\n\nDBGen is an opinionated ETL tool. ETL tools exist but they rarely\ngive the tools necessary for a scientific workflow. Opinionated\naspect: it really cares about what the end product is (ID columns on\nall the tables). We\'re dealing with a much more restricted ETL\nproblem (extracting and ).\n\nComparison to\n\n1. [Airflow](https://airflow.apache.org/)\n\n   - Has a priority for ETL scalability\n\n2. [Fireworks](https://materialsproject.github.io/fireworks/)\n\n3. [AiiDA](http://www.aiida.net/) or [Atomate](https://atomate.org/)\n   - We don\'t focus on the actual submission of computational\n     science workflows.\n\n## What isn\'t DBgen?\n\n1. An [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) tool (see [Hibernate](http://hibernate.org/orm/) for Java or [SQLAlchemy](https://www.sqlalchemy.org/) for Python)\n\n   - DBgen operates at a higher level of abstrload, not exposing the user to low level SQL commands like SELECT or INSERT.\n\n2. A database manager (see\n   [MySQLWorkbench](https://www.mysql.com/products/workbench/),\n   [DBeaver](https://dbeaver.io/), [TablePlus](https://tableplus.com/),\n   etc.)\n3. An opinioniated tool with a particular schema for scientific data /\n   theories.\n\n## Getting DBgen\n\n### Via Github\n\nCurrently, the only method of installing DBgen is through Github. This is best done by using the [poetry](https://python-poetry.org/) package manager. To do this, first clone the repo to a local directory. Then use the command `poetry install` in the directory to install the required dependencies. You will need at least python 3.8 to install the package.\n\nThis installation process is still in development, please contact the DBgen if you encounter issues. Moving forward we plan to use make dbgen installable through `pip`.\n\n### API documentation\n\nDocumentation of modules and classes can be found in\nAPI docs \\</modules\\>.\n\n#### Reporting bugs\n\nPlease report any bugs and issues at DBgen\'s [Github Issues\npage](https://github.com/modelyst/dbgen/issues).\n\n## License\n\nDBgen is released under the [Apache 2.0 License](license/).\n',
    'author': 'Michael Statt',
    'author_email': 'michael.statt@modelyst.io',
    'maintainer': 'Michael Statt',
    'maintainer_email': 'michael.statt@modelyst.io',
    'url': 'https://www.dbgen.modelyst.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
