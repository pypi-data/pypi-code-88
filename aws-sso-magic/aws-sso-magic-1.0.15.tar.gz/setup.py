# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aws_sso_magic']

package_data = \
{'': ['*']}

install_requires = \
['aws-error-utils>=1.0.4,<2.0.0',
 'aws-sso-lib>=1.7.0,<2.0.0',
 'boto3>=1.17.20,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'jsonschema>=3.2.0,<4.0.0',
 'prettytable>=2.1.0,<3.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'pyyaml>=5.3.1,<6.0.0']

entry_points = \
{'console_scripts': ['aws-sso-magic = aws_sso_magic.cli:cli']}

setup_kwargs = {
    'name': 'aws-sso-magic',
    'version': '1.0.15',
    'description': 'Magic credentials on the AWS CLI home using AWS SSO login',
    'long_description': '#\n# aws-sso-magic tool cli \n\nThis Docker image updates the aws credentials file for the default profile from the aws sso login. At the moment you should copy/paste the url in your browser and complete the login process.\n\nThis Docker solution mixed the following repositories:\n\n1. [aws-sso-util](https://github.com/benkehoe/aws-sso-util) AWS SSO has some rough edges, and aws-sso-util is here to smooth them out, hopefully temporarily until AWS makes it better.\n2. [aws-sso-credentials](https://github.com/NeilJed/aws-sso-credentials) A simple Python tool to simplify getting short-term credential tokens for CLI/Boto3 operations when using AWS SSO.\n\n## Content of the repository\n\n- [src](src) - The main folder with the aws_sso_magic folder with the .py files & the requirements.txt.\n    - [aws_sso_magic](src/aws_sso_magic)\n- [docker-build.sh](cli/docker-build.sh) - A docker build tool (Linux/MacOS) to build the docker image locally.\n    ```bash\n    sudo ./docker-build.sh\n    ```     \n- [pyproject.toml](pyproject.toml) - The metadata file with the dependencies and application information.    \n- [Dockerfile](Dockerfile) - The docker file with the instructions to build the aws-sso-magic cli.\n\n#\n# Installing aws-sso-magic tool from [pyp.org](https://pypi.org/project/aws-sso-magic/)\n\n## Prerequisites\n1. [Python 3.9](https://www.python.org/downloads/) installed.\n2. [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed, please click on the link depending of your OS.\n\n## Installation Steps\n1. `pip install aws-sso-magic`\n\n## How to use\n\n1. Execute the following command to configure the sso tool: `aws-sso-magic configure`\n2. Type the sso url, sso_region, and the rest of information.\n3. Execute the following command to log: `aws-sso-magic login`\n4. Select the profile to use.\n\n## How to use with pyp installer\n\n1. Follow the pyp [aw-sso-magic](https://pypi.org/project/aws-sso-magic/) project instructions.\n\n    NOTE: You will need the aws cli v2 installed previously.\n\n\n## Prerequisites\n1. [Python 3.9](https://www.python.org/downloads/) installed.\n2. [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed, please click on the link depending of your OS.\n\n## Installation Steps\n1. `pip install aws-sso-magic`\n\n#\n# How to use with Docker\n\n1. Please follow the instructions from the docker hub repository of [aws_sso_magic](https://hub.docker.com/r/javiortizmol/aws_sso_magic)\n\n## Docker Hub\n- [All Repositories](https://hub.docker.com/u/javiortizmol)\n- [aws_sso_magic](https://hub.docker.com/r/javiortizmol/aws_sso_magic)\n',
    'author': 'Javier Ortiz',
    'author_email': 'jahor2@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/javiortizmol/aws-sso-magic',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
