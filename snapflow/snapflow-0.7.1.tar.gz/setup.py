# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snapflow',
 'snapflow.cli',
 'snapflow.cli.commands',
 'snapflow.core',
 'snapflow.core.declarative',
 'snapflow.core.execution',
 'snapflow.core.extraction',
 'snapflow.core.persistence',
 'snapflow.core.sql',
 'snapflow.core.typing',
 'snapflow.helpers',
 'snapflow.helpers.connectors',
 'snapflow.logging',
 'snapflow.migrations',
 'snapflow.migrations.versions',
 'snapflow.modules',
 'snapflow.modules.core',
 'snapflow.modules.core.functions',
 'snapflow.modules.core.functions.accumulate',
 'snapflow.modules.core.functions.accumulator',
 'snapflow.modules.core.functions.accumulator_sql',
 'snapflow.modules.core.functions.dedupe_keep_latest',
 'snapflow.modules.core.functions.dedupe_keep_latest.tests',
 'snapflow.modules.core.functions.dedupe_keep_latest_dataframe',
 'snapflow.modules.core.functions.dedupe_keep_latest_dataframe.tests',
 'snapflow.modules.core.functions.dedupe_keep_latest_sql',
 'snapflow.modules.core.functions.dedupe_keep_latest_sql.tests',
 'snapflow.modules.core.functions.import_dataframe',
 'snapflow.modules.core.functions.import_local_csv',
 'snapflow.modules.core.functions.import_records',
 'snapflow.modules.core.functions.import_storage_csv',
 'snapflow.modules.core.functions.import_table',
 'snapflow.templates',
 'snapflow.templates.templates.dataspace_template.{{ cookiecutter.name }}',
 'snapflow.templates.templates.dataspace_template.{{ cookiecutter.name '
 '}}.functions',
 'snapflow.templates.templates.function_template.{{ cookiecutter.function_name '
 '}}',
 'snapflow.templates.templates.function_template.{{ cookiecutter.function_name '
 '}}.tests',
 'snapflow.templates.templates.module_template.{{ cookiecutter.name }}',
 'snapflow.templates.templates.module_template.{{ cookiecutter.name '
 '}}.functions',
 'snapflow.templates.templates.old_module_template.{{ '
 'cookiecutter.py_module_name }}',
 'snapflow.templates.templates.old_module_template.{{ '
 'cookiecutter.py_module_name }}.functions',
 'snapflow.templates.templates.sql_function_template.{{ '
 'cookiecutter.function_name }}',
 'snapflow.templates.templates.sql_function_template.{{ '
 'cookiecutter.function_name }}.tests',
 'snapflow.templates.templates.tests_template.tests',
 'snapflow.testing',
 'snapflow.utils']

package_data = \
{'': ['*'],
 'snapflow.modules.core': ['schemas/*'],
 'snapflow.templates': ['templates/dataspace_template/*',
                        'templates/flow_template/*',
                        'templates/function_template/*',
                        'templates/module_template/*',
                        'templates/old_module_template/*',
                        'templates/schema_template/*',
                        'templates/sql_function_template/*',
                        'templates/tests_template/*'],
 'snapflow.templates.templates.dataspace_template.{{ cookiecutter.name }}': ['flows/*',
                                                                             'schemas/*'],
 'snapflow.templates.templates.module_template.{{ cookiecutter.name }}': ['flows/*',
                                                                          'schemas/*']}

install_requires = \
['alembic>=1.5.5,<2.0.0',
 'backoff>=1.10.0,<2.0.0',
 'cleo>=0.8.1,<0.9.0',
 'click>=7.1.1,<8.0.0',
 'colorful>=0.5.4,<0.6.0',
 'common-model>=0.1.4,<0.2.0',
 'cookiecutter>=1.7.2,<2.0.0',
 'datacopy>=0.1.6,<0.2.0',
 'jinja2>=3.0.0,<4.0.0',
 'loguru>=0.5.1,<0.6.0',
 'networkx>=2.4,<3.0',
 'pandas>=1.0.1,<2.0.0',
 'pyarrow>=3.0.0,<4.0.0',
 'pydantic-sqlalchemy>=0.0.9,<0.0.10',
 'pydantic>=1.8.1,<2.0.0',
 'ratelimit>=2.2.1,<3.0.0',
 'requests>=2.23.0,<3.0.0',
 'sqlalchemy>=1.4.1,<2.0.0',
 'sqlparse>=0.3.1,<0.4.0',
 'strictyaml>=1.0.6,<2.0.0']

entry_points = \
{'console_scripts': ['snapflow = snapflow.cli:app']}

setup_kwargs = {
    'name': 'snapflow',
    'version': '0.7.1',
    'description': 'DataFunctional Data Pipelines',
    'long_description': None,
    'author': 'Ken Van Haren',
    'author_email': 'kenvanharen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.4,<4.0.0',
}


setup(**setup_kwargs)
