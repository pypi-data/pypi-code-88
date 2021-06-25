# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['common_client_scheduler',
 'terality',
 'terality._terality',
 'terality._terality.data_transfers',
 'terality._terality.encoding',
 'terality._terality.terality_structures',
 'terality._terality.utils',
 'terality_serde']

package_data = \
{'': ['*']}

install_requires = \
['aioboto3>=8.2.0,<9.0.0',
 'aiobotocore>=1.1,<2.0',
 'backoff>=1.10.0,<2.0.0',
 'boto3>=1.16,<2.0',
 'dill>=0.3.2,<0.4.0',
 'numpy>=1.18,<2.0',
 'pandas>=1.0.0,<2.0.0',
 'pyarrow>=3.0.0,<4.0.0',
 'pydantic>=1.7.3,<2.0.0',
 'requests>=2.24.0,<3.0.0',
 'single-source>=0.1.5,<0.2.0']

setup_kwargs = {
    'name': 'terality',
    'version': '0.8.17',
    'description': 'The Data Processing Engine for Data Scientists',
    'long_description': "# Terality\n\nTerality is a distributed data processing engine for Data Scientists to execute all their Pandas code 100 times faster, even on terabytes of data, by only changing one line of code.\nTerality is hosted, so there is no infrastructure to manage, and memory is virtually unlimited.\n\n**Note:** You will need a Terality account to use this package. Contact us on [terality.com](https://www.terality.com/) to get started!\n\n## Setup\n\nConfigure your credentials once and for all by calling the `configure` function:\n\n```python\nimport terality\nterality.configure('<YOUR_USER_ID>', '<YOUR_USER_SECRET>')\n```\n\nBy default, the configuration is written inside a `.terality` directory under the current user's home. You can customize that location through the `TERALITY_HOME` environment variable.\n",
    'author': 'Terality Engineering Team',
    'author_email': 'dev.null@terality.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://terality.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
