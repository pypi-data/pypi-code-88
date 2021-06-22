# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypmp']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'pypmp',
    'version': '0.3.0.post1',
    'description': "Python lib to interact with ManageEngine Password Manager Pro's REST API",
    'long_description': '# pypmp\n\nPython lib to interact with ManageEngine Password Manager Pro\'s REST API\n\n## Installation\n\n```bash\npip install pypmp\n```\n\n## Usage\n\n```python\nfrom pypmp import PasswordManagerProClient\n\n# Connect\npmp = PasswordManagerProClient("pmp.example.com", "REST_API_TOKEN", verify=True)\n\n# Get all resources\npmp.get_resources()\n# Get accounts\npmp.get_accounts(resource_id=resource_id)\n# Get password\npmp.get_account_password(resource_id=resource_id, account_id=account_id)\n\n# Shortcuts\n# Get resource by name\npmp.get_resource_by_name(name="resource01")\n# Get account by name\npmp.get_account_by_name(resource_name="resource01", account_name="Administrator")\n# Get password\npmp.get_password(resource_name="resource01", account_name="Administrator")\n```\n\n## API Documentation\n\nhttps://www.manageengine.com/products/passwordmanagerpro/help/restapi.html\n',
    'author': 'Philipp Schmitt',
    'author_email': 'philipp.schmitt@post.lu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/post-luxembourg/pypmp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
