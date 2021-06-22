# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['deep_lynx']

package_data = \
{'': ['*']}

install_requires = \
['requests', 'requests-toolbelt']

entry_points = \
{'console_scripts': ['run = wsgi:main']}

setup_kwargs = {
    'name': 'deep-lynx',
    'version': '0.0.3',
    'description': 'A package for interacting with the Deep Lynx data warehouse',
    'long_description': '# Deep Lynx Python Package  \nDeep Lynx Python Package\n\nAllows applications to interact with the [Deep Lynx](https://github.com/idaholab/Deep-Lynx) data warehouse.  \n\n```python\nimport deep_lynx\n# alternate direct import: from deep_lynx.deep_lynx_service import DeepLynxService\n\ndl_service = deep_lynx.DeepLynxService(\'http://127.0.0.1:8090\', \'MyContainer\', \'MyDatasource\')\n\n# create container\ndl_service.create_container(\n  {\n    \'name\': \'MyContainer\',\n    \'description\': \'My test container\'\n  }\n)\n\n# ensure data source exists or create it\ndl_service.init()\n\n# import data to deep lynx\ndl_service.create_manual_import(\n  dl_service.container_id,\n  dl_service.data_source_id,\n  {\'your data here\': \'data\'}\n)\n```\n\n**DeepLynxService** includes a few helper methods for container verification, data source verification and creation, setting auth headers, and retrieving the latest import time. The majority of the class methods are API calls to Deep Lynx. Please see the Deep Lynx [API Documentation](https://github.com/idaholab/Deep-Lynx/tree/master/API%20Documentation) for further details.  \n  \n  \n## Installation  \n\npip: `pip install deep_lynx`   \npoetry: `poetry add deep_lynx`  \n\n## Contributing\nAfter cloning the repository, please use [Poetry](https://python-poetry.org/) for setup (e.g. `poetry install`, `poetry shell` to activate the virtual environment, etc).  \n\nTests can be run with an active and reachable instance of Deep Lynx. Create a file named `.env` at the root of the project. Then fill it out with the following parameters:  \n\n```\nDEEP_LYNX_URL=  \nCONTAINER_NAME=  \nDATA_SOURCE_NAME=  \n```\n\nSee `tests/REAMDE.md` for more information.  \n\nThis project uses [yapf](https://github.com/google/yapf) for formatting. Please install it and apply formatting before submitting changes (e.g. `yapf src/deep_lynx tests --in-place --recursive --style={column_limit:120}`)  \n\n### Other Software\nIdaho National Laboratory is a cutting edge research facility which is a constantly producing high quality research and software. Feel free to take a look at our other software and scientific offerings at:\n\n[Primary Technology Offerings Page](https://www.inl.gov/inl-initiatives/technology-deployment)\n\n[Supported Open Source Software](https://github.com/idaholab)\n\n[Raw Experiment Open Source Software](https://github.com/IdahoLabResearch)\n\n[Unsupported Open Source Software](https://github.com/IdahoLabCuttingBoard)\n\n### License\n\nCopyright 2021 Battelle Energy Alliance, LLC\n\nLicensed under the MIT License (the "License");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n  https://opensource.org/licenses/MIT  \n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n\n\n\nLicensing\n-----\nThis software is licensed under the terms you may find in the file named "LICENSE" in this directory.\n\n\nDevelopers\n-----\nBy contributing to this software project, you are agreeing to the following terms and conditions for your contributions:\n\nYou agree your contributions are submitted under the MIT license. You represent you are authorized to make the contributions and grant the license. If your employer has rights to intellectual property that includes your contributions, you represent that you have received permission to make contributions and grant the required license on behalf of that employer.\n',
    'author': 'Jeren Browning',
    'author_email': 'jeren.browning@inl.gov',
    'maintainer': 'Jeren Browning',
    'maintainer_email': 'jeren.browning@inl.gov',
    'url': 'https://github.com/idaholab/Deep-Lynx-Python-Package/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
