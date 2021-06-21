# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lsf_stats']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0',
 'humanize>=3.9.0,<4.0.0',
 'ipython>=7.24.1,<8.0.0',
 'matplotlib>=3.4.2,<4.0.0',
 'pandas>=1.2.4,<2.0.0',
 'pyskim==0.1.3',
 'seaborn>=0.11.1,<0.12.0',
 'tqdm>=4.61.1,<5.0.0']

entry_points = \
{'console_scripts': ['lsf_stats = lsf_stats:cli']}

setup_kwargs = {
    'name': 'lsf-stats',
    'version': '0.3.0',
    'description': 'Summarize LSF job properties by parsing log files.',
    'long_description': '# lsf_stats\n\n[![PyPI](https://img.shields.io/pypi/v/lsf_stats.svg?style=flat)](https://pypi.python.org/pypi/lsf_stats)\n[![Tests](https://github.com/kpj/lsf_stats/workflows/Tests/badge.svg)](https://github.com/kpj/lsf_stats/actions)\n\nSummarize [LSF](https://www.ibm.com/support/pages/what-lsf-cluster) job properties by parsing log files of workflows executed by [Snakemake](https://github.com/snakemake/snakemake/).\n\n\n## Installation\n\n```python\n$ pip install lsf_stats\n```\n\n\n## Usage\n\n```bash\n$ lsf_stats --help\nUsage: lsf_stats [OPTIONS] COMMAND [ARGS]...\n\n  Summarize LSF job properties by parsing log files.\n\nOptions:\n  --version  Show the version and exit.\n  --help     Show this message and exit.\n\nCommands:\n  gather     Aggregate information from log files in single dataframe.\n  summarize  Summarize and visualize aggregated information.\n```\n\n### Example\n\nAssume that you executed your Snakemake workflow using the [lsf-profile](https://github.com/Snakemake-Profiles/lsf) and all generated log files are stored in the directory `./logs/`:\n```bash\n$ snakemake --profile lsf\n[..]\n```\n\nYou can then quickly aggregate resource, rule and other types of information about the workflow execution into a single dataframe:\n```bash\n$ lsf_stats gather -o workflow_stats.csv.gz ./logs/\n[..]\n```\n\nThis dataframe can then be summarized in various ways:\n```bash\n$ lsf_stats summarize \\\n    --query \'status == "Successfully completed."\' \\\n    --split-wildcards \\\n    --grouping-variable category \\\n    workflow_stats.csv.gz\n[..]\n```\n\nFor example, the following plots will be generated:\nJob execution                                 |  Job resources\n:--------------------------------------------:|:----------------------------------------:\n![Job execution](gallery/job_completions.png) | ![Job resources](gallery/scatterplot.png)\n',
    'author': 'kpj',
    'author_email': 'kim.philipp.jablonski@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kpj/lsf_stats',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
