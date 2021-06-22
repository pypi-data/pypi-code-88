# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mypy_boto3_builder',
 'mypy_boto3_builder.enums',
 'mypy_boto3_builder.import_helpers',
 'mypy_boto3_builder.parsers',
 'mypy_boto3_builder.parsers.docstring_parser',
 'mypy_boto3_builder.structures',
 'mypy_boto3_builder.type_annotations',
 'mypy_boto3_builder.type_maps',
 'mypy_boto3_builder.utils',
 'mypy_boto3_builder.writers']

package_data = \
{'': ['*'],
 'mypy_boto3_builder': ['boto3_stubs_static/*',
                        'boto3_stubs_static/docs/*',
                        'boto3_stubs_static/dynamodb/*',
                        'boto3_stubs_static/ec2/*',
                        'boto3_stubs_static/resources/*',
                        'botocore_stubs_static/*',
                        'botocore_stubs_static/retries/*',
                        'templates/boto3-stubs/*',
                        'templates/boto3-stubs/boto3-stubs/*',
                        'templates/boto3_stubs_docs/*',
                        'templates/botocore-stubs/*',
                        'templates/botocore-stubs/botocore-stubs/*',
                        'templates/common/*',
                        'templates/master/*',
                        'templates/master/master/*',
                        'templates/service/*',
                        'templates/service/service/*',
                        'templates/service_docs/*']}

install_requires = \
['black>=21.5b2,<22.0',
 'boto3',
 'isort>=5.6.4,<6.0.0',
 'jinja2>=3.0.1,<4.0.0',
 'mdformat',
 'pip',
 'pyparsing']

setup_kwargs = {
    'name': 'mypy-boto3-builder',
    'version': '4.18.4',
    'description': 'Builder for boto3-stubs',
    'long_description': None,
    'author': 'Vlad Emelianov',
    'author_email': 'vlad.emelianov.nz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
