# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blackdogosint',
 'blackdogosint.osint',
 'blackdogosint.osint.Archives',
 'blackdogosint.osint.Business_Records',
 'blackdogosint.osint.Classifieds',
 'blackdogosint.osint.Dark_Web',
 'blackdogosint.osint.Dating',
 'blackdogosint.osint.Digital_Currency',
 'blackdogosint.osint.Documentation',
 'blackdogosint.osint.Domain_Name',
 'blackdogosint.osint.Email_Address',
 'blackdogosint.osint.Encoding_Decoding',
 'blackdogosint.osint.Exploits_e_Advisories',
 'blackdogosint.osint.Forum_Blog_IRC',
 'blackdogosint.osint.Geolocation_Tool_Maps',
 'blackdogosint.osint.IP_Address',
 'blackdogosint.osint.IP_Address.Geolocation',
 'blackdogosint.osint.IP_Address.Geolocation.My_IP_Address',
 'blackdogosint.osint.Image_Video_Docs',
 'blackdogosint.osint.Instant_Messaging',
 'blackdogosint.osint.Language_Translation',
 'blackdogosint.osint.Malicious_File_Analysis',
 'blackdogosint.osint.Metadata',
 'blackdogosint.osint.Mobile_Emulation',
 'blackdogosint.osint.OpSec',
 'blackdogosint.osint.People_Search_Engines',
 'blackdogosint.osint.Public_Records',
 'blackdogosint.osint.Search',
 'blackdogosint.osint.Search.google',
 'blackdogosint.osint.Search_Engines',
 'blackdogosint.osint.Social_Networks',
 'blackdogosint.osint.Telephone_Numbers',
 'blackdogosint.osint.Terrorism',
 'blackdogosint.osint.Threat_Intelligence',
 'blackdogosint.osint.Tools',
 'blackdogosint.osint.Trainings',
 'blackdogosint.osint.Transportation',
 'blackdogosint.osint.Username',
 'blackdogosint.osint.Username.Specific_Sites',
 'blackdogosint.osint.Username.Username_Search_Engines',
 'blackdogosint.resources']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2.4,<4.0.0',
 'google>=3.0.0,<4.0.0',
 'requests>=2.25.1,<3.0.0',
 'standalone>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'blackdogosint',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'darkcode357',
    'author_email': 'darkcode357@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
