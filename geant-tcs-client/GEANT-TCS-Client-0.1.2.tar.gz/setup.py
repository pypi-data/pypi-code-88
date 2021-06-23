# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geant-tcs-client']

package_data = \
{'': ['*']}

modules = \
['README', 'LICENSE']
install_requires = \
['click>=7.1.2,<8.0.0', 'httpx>=0.17.1,<0.18.0']

entry_points = \
{'console_scripts': ['geant-tcs-client = geant-tcs-client.main:main']}

setup_kwargs = {
    'name': 'geant-tcs-client',
    'version': '0.1.2',
    'description': 'Python module for the GÉANT TCS API',
    'long_description': '# GÉANT-TCS-Client (GÉANT Trusted Certificate Service Client)\n\nWork in progress.\n\n# Install\n\n    pip install geant-tcs-client\n\n# Example\n\n    #!/usr/bin/env python\n    \n    from geant_tcs_client import GEANTTCSClient\n    from ssl_certificates import SSLCertificates\n\n    def main():\n\n        client = GEANTTCSClient.connect()\n        \n        config = {"username": "admin_customer14378", "password": "password123", "custom_uri": "test"}\n        ssl_certs = SSLCertificates(config)\n        \n        print(ssl_certs.listing_ssl_types())\n    \n    \n    if __name__ == \'__main__\':\n        main()\n\n',
    'author': 'Robert Grätz',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ikreb7/GEANT-TCS-Client',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
