# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flask_healthz', 'flask_healthz.tests']

package_data = \
{'': ['*']}

install_requires = \
['flask<3.0']

setup_kwargs = {
    'name': 'flask-healthz',
    'version': '0.0.3',
    'description': 'A simple module to allow you to easily add health endpoints to your Flask application',
    'long_description': '# Flask-Healthz\n\nDefine endpoints in your Flask application that Kubernetes can use as\n[liveness and readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).\n\n\n## Setting it up\n\n### Blueprint\n\nRegister the blueprint on your Flask application:\n\n```python\nfrom flask import Flask\nfrom flask_healthz import healthz\n\napp = Flask(__name__)\napp.register_blueprint(healthz, url_prefix="/healthz")\n```\n\nDefine the functions you want to use to check health. To signal an error, raise `flask_healthz.HealthError`.\n\n```python\nfrom flask_healthz import HealthError\n\ndef liveness():\n    pass\n\ndef readiness():\n    try:\n        connect_database()\n    except Exception:\n        raise HealthError("Can\'t connect to the database")\n```\n\nNow point to those functions in the Flask configuration:\n\n```python\nHEALTHZ = {\n    "live": "yourapp.checks.liveness",\n    "ready": "yourapp.checks.readiness",\n}\n```\n\nIt is possible to directly set callables in the configuration, so you could write something like:\n\n```python\nHEALTHZ = {\n    "live": lambda: None,\n}\n```\n\nCheck that the endpoints actually work:\n\n```\n$ curl http://localhost/yourapp/healthz/live\n{"status": 200, "title": "OK"}\n$ curl http://localhost/yourapp/healthz/ready\n{"status": 200, "title": "OK"}\n```\n\nNow your can configure Kubernetes or OpenShift to check for those endpoints.\n\n### Extension\n\nYou can also use the provided Flask extension to register the `healthz` blueprint:\n\n```python\nfrom flask import Flask\nfrom flask_healthz import Healthz\n\napp = Flask(__name__)\nHealthz(app)\n```\n\nThe rest of the configuration is identical.\n\nThe extension has an additional option, `no_log`, that can disable logging of the HTTP requests\nhandled by your healthz endpoints, to avoid cluttering your web log files with automated requests.\nAt the moment, only the [gunicorn](https://gunicorn.org/) web server is supported.\n\n```python\nHealthz(app, no_log=True)\n```\n\n## Examples\n\nHere\'s an example of how you could use flask-healthz in OpenShift\'s `deploymentconfig`:\n\n```yaml\nkind: DeploymentConfig\nspec:\n  [...]\n  template:\n    [...]\n    spec:\n      containers:\n      - name: yourapp\n        [...]\n        livenessProbe:\n          httpGet:\n            path: /healthz/live\n            port: 8080\n          initialDelaySeconds: 5\n          timeoutSeconds: 1\n        readinessProbe:\n          httpGet:\n            path: /healthz/ready\n            port: 8080\n          initialDelaySeconds: 5\n          timeoutSeconds: 1\n```\n\nSome projects that have setup flask-healthz:\n\n- Noggin: https://github.com/fedora-infra/noggin/pull/287\n- FASJSON: https://github.com/fedora-infra/fasjson/pull/81\n\n\n## License\n\nCopyright 2020-2021 Red Hat\n\nFlask-Healthz is licensed under the same license as Flask itself: BSD 3-clause.\n\n\n[![codecov](https://codecov.io/gh/fedora-infra/flask-healthz/branch/dev/graph/badge.svg?token=lwlZLiSImq)](https://codecov.io/gh/fedora-infra/flask-healthz)\n',
    'author': 'Fedora Infrastructure',
    'author_email': 'admin@fedoraproject.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fedora-infra/flask-healthz',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
