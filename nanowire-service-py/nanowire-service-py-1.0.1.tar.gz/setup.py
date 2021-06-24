# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nanowire_service_py']

package_data = \
{'': ['*']}

install_requires = \
['psutil>=5.8.0,<6.0.0',
 'psycopg2>=2.8.6,<3.0.0',
 'pydantic>=1.7.4,<2.0.0',
 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'nanowire-service-py',
    'version': '1.0.1',
    'description': 'Wrapper for interacting with Nanowire platform',
    'long_description': '# nanowire-service-py\n\n<div align="center">\n\n[![Build status](https://github.com/SpotlightData/nanowire-service-py/workflows/build/badge.svg?branch=master&event=push)](https://github.com/SpotlightData/nanowire-service-py/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/nanowire-service-py.svg)](https://pypi.org/project/nanowire-service-py/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/SpotlightData/nanowire-service-py/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/SpotlightData/nanowire-service-py/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/SpotlightData/nanowire-service-py/releases)\n[![License](https://img.shields.io/github/license/SpotlightData/nanowire-service-py)](https://github.com/SpotlightData/nanowire-service-py/blob/master/LICENSE)\n\nWrapper for interacting with Nanowire platform\n\n</div>\n\n## Usage\n\nThis library is designed for tight integration with Nanowire platform (created by Spotlight Data).\n\nThe library does not have a hardcode requirement for a specific web server, but I\'d recommend using [fastapi](https://fastapi.tiangolo.com/) due to it\'s simplicity and speed\n\nThe primary code logic should be placed in a sub-class of `BaseHandler`. User is expected to implement `validate_args` as well as `handle_body` methods:\n\n```python\nimport os\nfrom dotenv import load_dotenv\nfrom fastapi import FastAPI, Response\n\nfrom pydantic import BaseModel, validator\nfrom typing import Any, List, Optional\n\nimport pandas as pd\n\nfrom nanowire_service_py import BaseHandler, create, TaskBody\nfrom toolbox import ClusterTool\n\nload_dotenv()\n\nallowed_methods = ["HDBSCAN", "DBSCAN"]\n# pydantic used to verify function body\nclass Arguments(BaseModel):\n    contentUrl: str\n    textCol: str\n    indexCol: str\n    clusterSize: float = 0.2\n    nLabels: int = 10\n    method: str = "DBSCAN"\n    customStops: Optional[List[str]] = []\n    maxVocab: int = 5000\n    memSave: bool = False\n    withAnomalous: bool = False\n\n    @validator(\'method\')\n    def method_check(cls, method):\n        if method not in allowed_methods:\n            raise ValueError("Method has to be one of: {}, received: {}".format(",".join(allowed_methods), method))\n        return method\n\n# Our custom handler\nclass MyHandler(BaseHandler):\n    def __init__(self, *args):\n        super().__init__(*args)\n        self.cluster_tool = ClusterTool(self.logger)\n\n    def validate_args(self, args: Any, task_id: str) -> Arguments:\n        return Arguments(**args)\n\n    def handle_body(self, args: Arguments, meta: Any, task_id: str):\n        df = pd.read_csv(args.contentUrl, dtype=\'unicode\')\n\n        if args.textCol not in df.columns:\n            raise RuntimeError("Could not find text column \'{}\' in CSV".format(args.textCol), { "origin": "CSV"})\n\n        if args.indexCol not in df.columns:\n            raise RuntimeError("Could not find index column \'{}\' in CSV".format(args.indexCol), { "origin": "CSV"})\n\n        result = self.cluster_tool.main(df, args)\n        return (result, meta)\n\n# Always handled by the library, pass environment directly \nexecutor = create(os.environ, MyHandler)\n\napp = FastAPI()\n\n# Let\'s DAPR know which topics should be subscribed to\n@app.get("/dapr/subscribe")\ndef subscribe():\n    return executor.subscriptions\n\n# Primary endpoint, where request will be delivered to\n# TaskBody type here verifies the post body\n@app.post("/subscription")\ndef subscription(body: TaskBody, response: Response):\n    status = executor.handle_request(body.data.id)\n    response.status = status\n    # Return empty body so dapr doesn\'t freak out\n    return {}\n\n# Start heartbeat thread\nexecutor.heartbeat()\n```\n\nAssuming the filename is `main.py` the server can then be started via `uvicorn main:app`\n\n### Handling failure\n\nThe primary validation happens within `validate_args` function by `pydantic` models. This is where anything related to input should be checked.\n\nIf at any point you want the current task to fail, raise `RuntimeError`. This will indicate the library, that we should fail and not retry again. For example:\n\n* CSV missing columns or having incorrect text format\n* Not enough data passed\n\nAnything else, that raises unexpected exception should be retried automatically.\n\n\n## Contributing\n\nRead [CONTRIBUTING.md](CONTRIBUTING.md)\n\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/SpotlightData/nanowire-service-py)](https://github.com/SpotlightData/nanowire-service-py/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/SpotlightData/nanowire-service-py/blob/master/LICENSE) for more details.\n\n\n## Credits\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).\n',
    'author': 'SpotlightData',
    'author_email': 'info@spotlightdata.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SpotlightData/nanowire-service-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.5,<4.0.0',
}


setup(**setup_kwargs)
