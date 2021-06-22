# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['data_lineage', 'data_lineage.parser']

package_data = \
{'': ['*'], 'data_lineage': ['assets/*']}

install_requires = \
['PyYAML',
 'SQLAlchemy>=1.3.6,<1.4',
 'amundsen-databuilder[athena,bigquery,glue,rds,snowflake]>=4.4.1,<5.0.0',
 'boto3==1.10.1',
 'click',
 'cryptography>=3.3.2,<4.0.0',
 'dbcat>=0.5.2',
 'flask-restful',
 'flask-restless-ng',
 'flask>=1.1,<2.0',
 'furl',
 'gunicorn',
 'inflection',
 'networkx',
 'pglast==1.18',
 'requests']

entry_points = \
{'console_scripts': ['data_lineage = data_lineage.__main__:main']}

setup_kwargs = {
    'name': 'data-lineage',
    'version': '0.7.2',
    'description': 'Open Source Data Lineage Tool for Redshift. Snowflake and many other databases',
    'long_description': '# Tokern Lineage Engine\n\n[![CircleCI](https://circleci.com/gh/tokern/data-lineage.svg?style=svg)](https://circleci.com/gh/tokern/data-lineage)\n[![codecov](https://codecov.io/gh/tokern/data-lineage/branch/master/graph/badge.svg)](https://codecov.io/gh/tokern/data-lineage)\n[![PyPI](https://img.shields.io/pypi/v/data-lineage.svg)](https://pypi.python.org/pypi/data-lineage)\n[![image](https://img.shields.io/pypi/l/data-lineage.svg)](https://pypi.org/project/data-lineage/)\n[![image](https://img.shields.io/pypi/pyversions/data-lineage.svg)](https://pypi.org/project/data-lineage/)\n\n\nTokern Lineage Engine is _fast_ and _easy to use_ application to collect, visualize and analyze \ncolumn-level data lineage in databases, data warehouses and data lakes in AWS and GCP.\n\nTokern Lineage helps you browse column-level data lineage \n* visually using [kedro-viz](https://github.com/quantumblacklabs/kedro-viz)\n* analyze lineage graphs programmatically using the powerful [networkx graph library](https://networkx.org/)\n\n## Resources\n\n* Demo of Tokern Lineage App\n\n![data-lineage](https://user-images.githubusercontent.com/1638298/118261607-688a7100-b4d1-11eb-923a-5d2407d6bd8d.gif)\n\n* Checkout an [example data lineage notebook](http://tokern.io/docs/data-lineage/example/).\n\n* Check out [the post on using data lineage for cost control](https://tokern.io/blog/data-lineage-on-redshift/) for an \nexample of how data lineage can be used in production.\n\n## Quick Start\n\nInstall a demo of using Docker and Docker Compose\n\nDownload the docker-compose file from Github repository.\n\n\n    # in a new directory run\n    wget https://raw.githubusercontent.com/tokern/data-lineage/master/install-manifests/docker-compose-demodb/docker-compose.yml\n    # or run\n    curl https://raw.githubusercontent.com/tokern/data-lineage/master/install-manifests/docker-compose-demodb/docker-compose.yml -o docker-compose.yml\n\n\nRun docker-compose\n   \n\n    docker-compose up -d\n\n\nCheck that the containers are running.\n\n\n    docker ps\n    CONTAINER ID   IMAGE                                    CREATED        STATUS       PORTS                    NAMES\n    3f4e77845b81   tokern/data-lineage-viz:latest   ...   4 hours ago    Up 4 hours   0.0.0.0:8000->80/tcp     tokern-data-lineage-visualizer\n    1e1ce4efd792   tokern/data-lineage:latest       ...   5 days ago     Up 5 days                             tokern-data-lineage\n    38be15bedd39   tokern/demodb:latest             ...   2 weeks ago    Up 2 weeks                            tokern-demodb\n\nTry out Tokern Lineage App\n\nHead to `http://localhost:8000/` to open the Tokern Lineage app\n\n\n## Supported Technologies\n\n* Postgres\n* AWS Redshift\n* Snowflake\n\n### Coming Soon\n\n* MySQL\n* SparkSQL\n* Presto\n\n## Documentation\n\nFor advanced usage, please refer to [data-lineage documentation](https://tokern.io/docs/data-lineage/index.html)\n## Survey\n\nPlease take this [survey](https://forms.gle/p2oEQBJnpEguhrp3A) if you are a user or considering using data-lineage. Responses will help us prioritize features better. \n',
    'author': 'Tokern',
    'author_email': 'info@tokern.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://tokern.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
