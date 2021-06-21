# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quisby',
 'quisby.benchmarks',
 'quisby.benchmarks.aim',
 'quisby.benchmarks.autohpl',
 'quisby.benchmarks.etcd',
 'quisby.benchmarks.fio',
 'quisby.benchmarks.hammerdb',
 'quisby.benchmarks.linpack',
 'quisby.benchmarks.pig',
 'quisby.benchmarks.reboot',
 'quisby.benchmarks.speccpu',
 'quisby.benchmarks.specjbb',
 'quisby.benchmarks.streams',
 'quisby.benchmarks.uperf',
 'quisby.credentials',
 'quisby.pricing',
 'quisby.sheet']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.17.97,<2.0.0',
 'bs4>=0.0.1,<0.0.2',
 'google-api-core>=1.30.0,<2.0.0',
 'google-api-python-client>=2.9.0,<3.0.0',
 'google-auth-oauthlib>=0.4.4,<0.5.0',
 'google_api>=0.1.12,<0.2.0']

entry_points = \
{'console_scripts': ['quisby = quisby.quisby:main']}

setup_kwargs = {
    'name': 'quisby',
    'version': '0.2',
    'description': 'Quisby is a tool to provide first view into the results from various benchmarks such as linpack, streams, fio etc.',
    'long_description': "## Quisby \n\n###### (Unoffical name) Quisby: An idler; one who does not or will not work. (noun)\n\nQuisby is a tool to provide first view into the results from various benchmarks such as linpack, streams, fio etc. It doesn't aim to replace existing data viz tool but rather to provide a simplified view to the data with basic metric to understand the benchmark results from a higher level view. For detailed view, there are other tools such as pbench-dashboard, js-charts etc at hand.\n\nBechmarks currently supported:\n\n|   Benchmark   |   Source data  |\n|---|---|\n| linpack | Benchmark result     |\n| streams | Summary result       |\n| uperf   | Summary csv result   |\n| specjbb | Benchmark result     |\n| pig     | Benchmark  result    |\n| hammerDB| Benchmark  result    |\n| fio     | pbench result        |\n| autohpl | Summary  result      |\n| aim     | Benchmark  result    |\n| etcd    | pbench  result       |\n| reboot  | Benchmark  result    |\n| speccpu | Benchmark  result    |\n\n\n### What it does\n\nIt extracts data from benchmark results file or summary results produced by wrapper benchmark programs and move that results to Google Sheet via sheets API V4. \n\n### Development \n\n```bash\n#Clone the repo\ngit clone git@github.com:sourabhtk37/data-to-sheet.git\n\n# Installation\nsource ./install.sh\n(optional, for configuring aws and/or azure cli)\nsource ./install -aws -azure\n```\n#### config.py \n\n`config.py` is the only file you need to edit. Sample example have been provided in the file. \n\n####  quisby.py\n\nThis is the main driver program that will be called once you have edited `config.py` file accordingly. It takes in an input file with list of location to the test results.\n\nThe location file will look like:\n\n``` \ntest: results_linpack\n</path/to/results>\n...\ntest: pbench_fio\n<http url with results>\n...\n```\n\n```bash\nquisby process --os-type <add-here> --os-release <add-here> --cloud-type <add-here>  location_file`\n```\nFor more information on options, run:\n\n    `quisby -h`\n\n*That's it. It will return a google sheet. Visit the google sheet page and you will see a newly created spreadsheet with the data populated and graphed.*\n\n### Comparison\n\nIf you want to compare two different OS release of similar system type then there are scripts that will help you to create a spreadsheet for the same. \n\nand then run:\n\n```bash\nquisby compare --test-name <benchmark-name-(optional)>  --spreadsheets <spreadsheet1,spreadsheet2>\n```\nand it would return a newly created spreadsheet with the comparison data.\n\n## Contributing\n\nCreate issues and create a seperate feature branch to work on it. Push the changes to your clone repo and then create a pull request to the master branch of the origin repo.\n",
    'author': 'T K Sourab',
    'author_email': 'tsourab@redhat.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sourabhtk37/Quisby',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
