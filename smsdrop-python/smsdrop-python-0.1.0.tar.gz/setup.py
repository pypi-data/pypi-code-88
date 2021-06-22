# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smsdrop']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.18.2,<0.19.0',
 'mkdocs-include-markdown-plugin>=3.1.4,<4.0.0',
 'mkdocs-material-extensions>=1.0.1,<2.0.0',
 'mkdocs-material>=7.1.8,<8.0.0',
 'mkdocs>=1.2.1,<2.0.0',
 'mkdocstrings>=0.15.2,<0.16.0',
 'redis>=3.5.3,<4.0.0',
 'tenacity>=7.0.0,<8.0.0']

setup_kwargs = {
    'name': 'smsdrop-python',
    'version': '0.1.0',
    'description': 'A python sdk for the smsdrop.net platform',
    'long_description': '# Smsdrop-Python\n\n[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)\n[![](https://img.shields.io/pypi/v/smsdrop-python.svg)](https://pypi.python.org/pypi/smsdrop-python)\n\n- Documentation: <a href="https://tobi-de.github.io/smsdrop-python/" target="_blank">https://tobi-de.github.io/smsdrop-python/</a>\n- Source Code: <a href="https://github.com/Tobi-De/smsdrop-python/" target="_blank">https://github.com/Tobi-De/smsdrop-python/</a>\n\nThe official python sdk for the [smsdrop](https://smsdrop.net) api.\n\n## Quickstart\n\n```python\nimport datetime\nimport logging\nimport time\n\nimport pytz\nfrom dotenv import dotenv_values\n\nfrom smsdrop import CampaignCreate, Client, RedisStorage\n\n# Enable Debug Logging\n# This will og the API request and response data to the console:\nlogging.basicConfig(level=logging.DEBUG, format="%(message)s")\n\nconfig = dotenv_values(".env")\n\nTEST_EMAIL = config.get("TEST_EMAIL")\nTEST_PASSWORD = config.get("TEST_PASSWORD")\nMY_TIMEZONE = config.get("MY_TIMEZONE")\n\n\ndef main():\n    # Initialize the client\n    client = Client(\n        email=TEST_EMAIL, password=TEST_PASSWORD, storage=RedisStorage()\n    )\n    # Get your account profile informations\n    print(client.read_me())\n    # Get your subscription informations\n    print(client.read_subscription())\n    # Get your first 500 campaigns\n    print(client.read_campaigns(skip=0, limit=500))\n\n    # Send a simple sms\n    client.send_message(message="hi", sender="Max", phone="<phone>")\n\n    # Create a new Campaign\n    cp = CampaignCreate(\n        title="Test Campaign",\n        message="Test campaign content",\n        sender="TestUser",\n        recipient_list=["<phone1>", "<phone2>", "<phone3>"],\n    )\n    cp = client.launch_campaign(cp)\n    time.sleep(20)  # wait for 20 seconds for the campaign to proceed\n    cp = client.read_campaign(cp.id)  # refresh your campaign data\n    print(cp.status)  # Output Example : COMPLETED\n\n    # create a scheduled campaign\n    naive_dispatch_date = datetime.datetime.now() + datetime.timedelta(hours=1)\n    aware_dispatch_date = pytz.timezone(MY_TIMEZONE).localize(\n        naive_dispatch_date\n    )\n    cp2 = CampaignCreate(\n        title="Test Campaign 2",\n        message="Test campaign content 2",\n        sender="TestUser",\n        recipient_list=["<phone1>", "<phone2>", "<phone3>"],\n        # The date will automatically be send in isoformat with the timezone data\n        defer_until=aware_dispatch_date,\n    )\n    cp2 = client.launch_campaign(cp2)\n    # If you check the status one hour from now it should return \'COMPLETED\'\n\n    # create another scheduled campaign using defer_by\n    cp3 = CampaignCreate(\n        title="Test Campaign 3",\n        message="Test campaign content 3",\n        sender="TestUser",\n        recipient_list=["<phone1>", "<phone2>", "<phone3>"],\n        defer_by=120,\n    )\n    cp3 = client.launch_campaign(cp3)\n    time.sleep(120)  # wait for 120 seconds for the campaign to proceed\n    cp3 = client.read_campaign(cp3.id)  # refresh your campaign data\n    print(cp3.status)  # should output : COMPLETED\n    # If you get a \'SCHEDULED\' printed, you can wait 10 more seconds in case the network\n    # is a little slow or the server is busy\n\n\nif __name__ == "__main__":\n    main()\n```\n\n  \n',
    'author': 'Tobi DEGNON',
    'author_email': 'tobidegnon@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Tobi-De/smsdrop-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
