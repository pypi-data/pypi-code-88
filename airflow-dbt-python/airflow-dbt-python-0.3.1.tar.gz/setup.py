# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['airflow_dbt_python', 'airflow_dbt_python.operators']

package_data = \
{'': ['*']}

install_requires = \
['apache-airflow>=1.10.12', 'dbt-core>=0.19,<0.20']

extras_require = \
{'all': ['dbt-postgres>=0.19,<0.20',
         'dbt-redshift>=0.19,<0.20',
         'dbt-snowflake>=0.19,<0.20',
         'dbt-bigquery>=0.19,<0.20'],
 'bigquery': ['dbt-bigquery>=0.19,<0.20'],
 'postgres': ['dbt-postgres>=0.19,<0.20'],
 'redshift': ['dbt-redshift>=0.19,<0.20'],
 'snowflake': ['dbt-snowflake>=0.19,<0.20']}

setup_kwargs = {
    'name': 'airflow-dbt-python',
    'version': '0.3.1',
    'description': 'A dbt operator for Airflow that uses the dbt Python package',
    'long_description': '# airflow-dbt-python\n\nAn [Airflow](https://airflow.apache.org/) operator to call the `main` function from the [`dbt-core`](https://pypi.org/project/dbt-core/) Python package\n\n# Motivation\n\nAlthough [`dbt`](https://docs.getdbt.com/) is meant to be installed and used as a CLI, we may not have control of the environment where Airflow is running, disallowing us the option of using `dbt` as a CLI.\n\nThis is exactly what happens when using [Amazon\'s Managed Workflows for Apache Airflow](https://aws.amazon.com/managed-workflows-for-apache-airflow/) or MWAA: although a list of Python requirements can be passed, the CLI cannot be found in the worker\'s PATH.\n\nThere is a workaround which involves using Airflow\'s `BashOperator` and running Python from the command line:\n\n```py\nfrom airflow.operators.bash import BashOperator\n\nBASH_COMMAND = "python -c \'from dbt.main import main; main()\' run"\noperator = BashOperator(\n    task_id="dbt_run",\n    bash_command=BASH_COMMAND,\n)\n```\n\nBut it can get sloppy when appending all potential arguments a `dbt run` command (or other subcommand) can take.\n\n`airflow-dbt-python` abstracts the complexity of handling CLI arguments by defining an operator for each `dbt` subcommand, and having each operator be defined with attribute for each possible CLI argument.\n\nThe existing [`airflow-dbt`](https://pypi.org/project/airflow-dbt/) package, by default, would not work if `dbt` is not in the PATH, which means it would not be usable in MWAA. There is a workaround via the `dbt_bin` argument, which can be set to `"python -c \'from dbt.main import main; main()\' run"`, in similar fashion as the `BashOperator` example. Yet this approach is not without its limitations:\n* `airflow-dbt` works by wrapping the `dbt` CLI, which makes our code dependent on the environment in which it runs.\n* `airflow-dbt` does not support the full range of arguments a command can take. For example, `DbtRunOperator` does not have an attribute for `fail_fast`.\n\nFinally, `airflow-dbt-python` does not depend on `dbt` but on `dbt-core`. The connectors are available as installation extras instead of being bundled up by default. This allows you to easily control what is installed in your environment. One particular example of when this is useful is in the case of the `dbt-snowflake` connector, which has dependencies which may not compile in all distributions (like the one MWAA runs on). Even if that\'s not the case, `airflow-dbt-python` results in a lighter installation due to only depending on `dbt-core`.\n\n# Usage\n\nCurrently, the following `dbt` commands are supported:\n\n* `clean`\n* `compile`\n* `debug`\n* `deps`\n* `ls`\n* `run`\n* `seed`\n* `snapshot`\n* `test`\n\n## Examples\n\n```py\nfrom datetime import timedelta\n\nfrom airflow import DAG\nfrom airflow.utils.dates import days_ago\nfrom airflow_dbt_python.operators.dbt import (\n    DbtRunOperator,\n    DbtSeedOperator,\n    DbtTestoperator,\n)\n\nargs = {\n    \'owner\': \'airflow\',\n}\n\nwith DAG(\n    dag_id=\'example_dbt_operator\',\n    default_args=args,\n    schedule_interval=\'0 0 * * *\',\n    start_date=days_ago(2),\n    dagrun_timeout=timedelta(minutes=60),\n    tags=[\'example\', \'example2\'],\n) as dag:\n    dbt_test = DbtTestOperator(\n        task_id="dbt_test",\n        selector="pre-run-tests",\n    )\n\n    dbt_seed = DbtSeedOperator(\n        task_id="dbt_seed",\n        select=["/path/to/first.csv", "/path/to/second.csv"],\n        full_refresh=True,\n    )\n\n    dbt_run = DbtRunOperator(\n        task_id="dbt_run",\n        models=["/path/to/models"],\n        full_refresh=True,\n        fail_fast=True,\n    )\n\n    dbt_test >> dbt_seed >> dbt_run\n```\n\n# Installing\n\n## From PyPI:\n\n```sh\npip install airflow-dbt-python\n```\n\n## From this repo:\n\nClone the repo:\n```sh\ngit clone https://github.com/tomasfarias/airflow-dbt-python.git\ncd airflow-dbt-python\n```\n\nWith poetry:\n```sh\npoetry install\n```\n\nInstall any extras you need, and only those you need:\n```sh\npoetry install -E postgres -E redshift\n```\n\n# Testing\n\nTests are written using `pytest`, can be located in `test/`, and they can be run locally with `poetry`:\n\n```sh\npoetry run pytest -vv\n```\n\n# License\n\nMIT\n',
    'author': 'Tomás Farías Santana',
    'author_email': 'tomas@tomasfarias.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
