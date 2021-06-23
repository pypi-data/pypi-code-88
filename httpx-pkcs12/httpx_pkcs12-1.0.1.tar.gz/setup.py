# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['httpx_pkcs12']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=3.4.7,<4.0.0']

setup_kwargs = {
    'name': 'httpx-pkcs12',
    'version': '1.0.1',
    'description': 'Addon which activates PKCS12 certificates usage with HTTPX client.',
    'long_description': "## httpx-pkcs12\n\nAddon which activates PKCS12 certificates usage with HTTPX client.\n\n## Usage\n```python\nwith open('path/to/your/cert', 'rb') as f:\n    cert_contents = f.read()\npassword = 'your-secret-password'\n\ncontext = create_ssl_context(cert_contents, password)\n\n# async version\nasync with httpx.AsyncClient(verify=context) as client:\n    response = ...\n\n# or sync version\nresponse = httpx.get(..., verify=context)\n```",
    'author': 'Shagit Ziganshin',
    'author_email': 'theLastOfCats@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
