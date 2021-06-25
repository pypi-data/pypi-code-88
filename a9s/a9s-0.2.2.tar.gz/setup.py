# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['a9s', 'a9s.aws_resources', 'a9s.components']

package_data = \
{'': ['*']}

install_requires = \
['attrdict>=2.0.1,<3.0.0',
 'blessed>=1.18.0,<2.0.0',
 'boto3>=1.17.87,<2.0.0',
 'cached-property>=1.5.2,<2.0.0',
 'colored>=1.4.2,<2.0.0',
 'pyperclip>=1.8.2,<2.0.0']

entry_points = \
{'console_scripts': ['a9s = a9s.main:main']}

setup_kwargs = {
    'name': 'a9s',
    'version': '0.2.2',
    'description': 'Cli tool for navigation in Amazon AWS services. Highly inspired from k9s',
    'long_description': '# a9s\nCli tool for easily navigating in AWS services.  \nHighly inspired from [k9s](https://github.com/derailed/k9s). \n\n\n## How to install\n\n```shell\npip install a9s\n```\n\n## Goals\n\n### Services\n- [X] s3 support\n- [X] route53 support\n- [ ] EC2 support\n- [ ] ELB support\n- [ ] Cloudfront support\n\n\n### Features\n- [X] responsive tables\n- [X] allow to easily switch between services\n- [X] auto-complete commands\n- [X] vim shortcuts support\n- [X] opening files in S3\n- [ ] quick yank (half done)\n- [ ] smart navigation between services - route53 pointing to ELB etc..\n',
    'author': 'Elran Shefer',
    'author_email': 'elran777@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/IamShobe/a9s',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
