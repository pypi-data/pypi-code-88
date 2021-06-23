# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gda_analysis',
 'gda_analysis.compare_to_manifest',
 'gda_analysis.convert_gs_to_df',
 'gda_analysis.convert_vcf_to_df',
 'gda_analysis.dal',
 'gda_analysis.validation_tests']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.18,<2.0.0',
 'openpyxl>=3.0.7,<4.0.0',
 'pandas>=1.2.4,<2.0.0',
 'psycopg2-binary>=2.8.6,<3.0.0']

entry_points = \
{'console_scripts': ['create_gs_dataframe = '
                     'src.gda_analysis.create_dfs:create_gs_df',
                     'create_vcf_dataframe = '
                     'src.gda_analysis.create_dfs:create_vcf_d',
                     'export_join_dfs = '
                     'src.gda_analysis.display_dataset:output_toexcel',
                     'join_dfs = src.gda_analysis.create_dfs:join_vcf_and_gs',
                     'main_merge = src.gda_analysis.create_dfs:main_merge',
                     'main_validation = '
                     'src.gda_analysis.display_dataset:main_validation',
                     'test_join_dfs = '
                     'src.gda_analysis.display_dataset:display_analyzed_data']}

setup_kwargs = {
    'name': 'gda-analysis',
    'version': '0.1.7',
    'description': '',
    'long_description': None,
    'author': 'Tova Hallas',
    'author_email': 'tova.hallas@igentify.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
