# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lmanage', 'lmanage.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'coloredlogger>=1.3.12,<2.0.0',
 'coloredlogs>=15.0,<16.0',
 'debugpy>=1.3.0,<2.0.0',
 'icecream>=2.1.0,<3.0.0',
 'ipython>=7.20.0,<8.0.0',
 'lookml>=3.0.3,<4.0.0',
 'pandas>=1.2.2,<2.0.0',
 'pynvim>=0.4.3,<0.5.0',
 'pytest-mock>=3.5.1,<4.0.0',
 'snoop>=0.3.0,<0.4.0',
 'sqlparse>=0.4.1,<0.5.0',
 'tabulate>=0.8.8,<0.9.0',
 'verboselogs>=1.7,<2.0']

entry_points = \
{'console_scripts': ['lmanage = lmanage.cli:lmanage']}

setup_kwargs = {
    'name': 'lmanage',
    'version': '0.1.5',
    'description': "LManage is a collection of useful tools for Looker admins to help curate and cleanup content and it's associated source LookML.",
    'long_description': '# Lmanage\n## What is it.\nLManage is a collection of useful tools for [Looker](https://looker.com/) admins to help curate and cleanup content and it\'s associated source [LookML](https://docs.looker.com/data-modeling/learning-lookml/what-is-lookml).\n\n## How do i Install it.\nLmanage can be found on [pypi](#).\n```\npip install lmanage\n```\n\n## How do I Use it.\n### Commands\nLManage will ultimately will have many different commands as development continues \n| Status  | Command    | Rationale                                                                                                                                                                                            |\n|---------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| Live    | mapview    | Find the LookML fields and tables that are associated with a piece of Looker content                                                                                                                 |\n| Planned | removeuser | Based on last time logged in, prune Looker users to ensure a performant, compliant Looker instance                                                                                                   |\n| Planned | dcontent   | Iterate through an input of content, delete content and back it up using [gzr](https://github.com/looker-open-source/gzr) for easy restoration                                                                                               |\n| Planned | bcontent   | Iterate through all broken content (using content validator) and email a customized message to each dashboard owner                                                                                  |\n| Planned | scoper     | Takes in a model file, elminates the * includes, iterate through the explores and joins and creates a fully scoped model include list for validation performance and best practice code organization |\n\n#### help and version\n```\nlmanage --help\nUsage: lmanage [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --version  Show the version and exit.\n  --help     Show this message and exit.\n\nCommands:\n  mapview\n```\n#### mapview\nThe mapview command will find the etymology of the content on your dashboard, exporting a CSV that looks like [this](https://docs.google.com/spreadsheets/d/1TzeJW46ml0uzO9RdLOOLxwtvUWjhmZxoa-xq4pbznV0/edit?resourcekey=0-xbWC87hXYFNgy1As06NncA#gid=900312158).\n\n##### example usage\n`lmanage mapview --path ./output/my_output.csv --ini-file ~/py/projects/ini/k8.ini --project /test_lookml_files/the_look -table "order_items"`\n##### flags\n- **path** (`--path`, `-fp`) This is the path where you would like the outputfile for your returned dataset to be. \n- **ini-file** (`--ini-file`, `-i`) This is the file path to the ini file that you\'ve created to use the Looker SDK\n```\n#example Ini file\n[Looker_Instance]\nbase_url=https://looker-dev.company.com:19999 (or 443 if hosted in GCP)\nclient_id=abc\nclient_secret=xyz\nverify_ssl=True\n```\n- **project** (`--project`, `-p`) This is the file path to your local project of LookML files that lmanage will scan to associate connections between your Looker content and LookML\nLmanage can either return a full dataset of all content mapping, or a prefiltered dataset with all content associated with a specific table or field.\n- **table** (`--table`, `-t`) Expecting input of lookml view name\n- **field** (`--field`, `-f`) Expecting input of fully scoped LookML field name e.g. viewname.fieldname \n\n\n![](./images/mapview_walkthru.jpeg)\n\n\n## Fields Returneds\n\n- **dashboard_id**: the id of the looker dashboard \t\n- **element_id**: the id of the visualization element on the looker dashboard\t\n- **sql_joins**: the joins used in a query grouped by element id\t\n- **fields_used**: the fields used by the query grouped by element id\n- **sql_table_name**: the underlying sql value being referenced at the view level of the lookml (assuming the view is standard)\t\n- **potential_join**: for the explore that powers the element query: what are all the potential joins available\t\n- **used_joins**: joins used by the underlying queries obtained by parsing sql of query \t\n- **used_view_names**: views that are used by each query grouped by element_id\t\n- **unused_joins**: views that are unused by the specific query of the dashboard element\n\n**This is not an officially supported Google Product.**\n',
    'author': 'hselbie',
    'author_email': 'hselbie@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/llooker/lmanage',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.9',
}


setup(**setup_kwargs)
