# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['intents',
 'intents.connectors',
 'intents.connectors.dialogflow_es',
 'intents.language',
 'intents.model']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-dialogflow>=2.0.0,<3.0.0', 'pyyaml>=5.4.1,<6.0.0']

setup_kwargs = {
    'name': 'intents',
    'version': '0.1a1',
    'description': 'Define and operate Dialogflow Agents with a simple, code-first, approach',
    'long_description': '# Intents ⛺\n\n[![Documentation Status](https://readthedocs.org/projects/intents/badge/?version=latest)](https://intents.readthedocs.io/en/latest/?badge=latest)\n[![codecov](https://codecov.io/gh/dariowho/intents/branch/master/graph/badge.svg?token=XAVLW70J8S)](https://codecov.io/gh/dariowho/intents)\n[![HEAD version](https://badgen.net/badge/head/v0.1a1/blue)](https://badgen.net/badge/head/v0.1a1/blue)\n[![PyPI version](https://badge.fury.io/py/intents.svg)](https://badge.fury.io/py/intents)\n\n**Intents** is a unofficial Python library to define and operate Dialogflow Agents with a simple,\ncode-first approach.\n\n## Project status\n\nThis project is in **alpha** stage, some API adjustments are to be expected before\nrelease. A detailed view of available features can be found in [STATUS.md](STATUS.md)\n\n## Install\n\n*Intents* can be installed as follows:\n\n```sh\npip install intents\n```\n\n## Usage\n\nIntents are defined like standard Python **dataclasses**:\n\n```python\n@dataclass\nclass HelloIntent(Intent):\n    """A little docstring for my Intent class"""\n    user_name: Sys.Person = "Guido"\n```\n\nTheir **language** resources are stored in separate YAML files:\n\n```yaml\nutterances:\n  - Hi! My name is $user_name{Guido}\n  - Hello there, I\'m $user_name{Mario}\n\nresponses:\n  default:\n    text:\n      - Hi $user_name\n      - Hello $user_name\n      - Nice to meet you, $user_name\n```\n\nAgents can be **uploaded** into Dialogflow ES projects directly from code; *Intents* will act transparently as a prediction client:\n\n```python\ndf = DialogflowEsConnector(\'/path/to/service-account.json\', MyAgent)\ndf.upload()  # You will find it in your Dialogflow Console\n\npredicted = df.predict("Hi there, my name is Mario")  # HelloIntent(user_name="Mario")\nprint(predicted.fulfillment_text)                     # "Hello Mario"\n```\n\nFor a complete working example, check out the included [Example Agent](example_agent/). Also, *Intents* **documentation** is published at https://intents.readthedocs.io/ 📚\n\n## Disclaimer\n\n*This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Dialogflow. The names Dialogflow, Google, as well as related names, marks, emblems and images are registered trademarks of their respective owners.*\n',
    'author': 'Dario',
    'author_email': 'dario.chi@inventati.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dariowho/intents',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
