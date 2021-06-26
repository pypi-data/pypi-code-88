# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vial']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyvial',
    'version': '0.5.0',
    'description': 'A micro web framework for AWS Lambda.',
    'long_description': '# Vial\nA micro web framework for AWS Lambda.\n\n## Installation\nTo add vial to your project, run the following command:\n```\npip install pyvial\n```\n\n## Usage\n### Entry Point\nThe main entry point of the application is always the `Vial#__call__` function. When deploying to AWS Lambda,\nthe Lambda handler should point to the `Vial` object in whichever file it\'s defined in. As an example:\n```\nfrom vial.app import Vial\n\napp = Vial(__name__)\n```\nIf this code snippet is defined in an `app.py` file, the handler would be `app.app`.\n\n### Basic API\n```\nfrom typing import Mapping\nfrom vial.app import Vial\n\napp = Vial(__name__)\n\n\n@app.get("/hello-world")\ndef hello_world() -> Mapping[str, str]:\n    return {"hello": "world"}\n```\n\n### Path Parameters\nYou can define path parameters like this:\n```\n@app.get("/users/{user_id}")\ndef get_user(user_id: str) -> User:\n    return user_service.get(user_id)\n```\n\nVial supports some path parameter parsing as part of the invocation process. For example when using a UUID\nas a path parameter, Vial can convert it from a string to a UUID automatically:\n```\nfrom uuid import UUID\n\n@app.get("/users/{user_id:uuid}")\ndef get_user(user_id: UUID) -> User:\n    return user_service.get(user_id)\n```\n\nThe following parsers are supported by default:\n\n| Parser        | Type              |\n| ------------- | ----------------- |\n| `str`         | `str`             |\n| `bool`        | `bool`            |\n| `int`         | `int`             |\n| `float`       | `float`           |\n| `decimal`     | `decimal.Decimal` |\n| `uuid`        | `uuid.UUID`       |\n\nYou can register your own parser like this:\n```\n@app.parser("list")\ndef list_parser(value: str) -> List[str]:\n    return [value]\n\n\n@app.get("/users/{user_id:list}")\ndef get_user(user_ids: List[str]) -> List[User]:\n    return [user_service.get(user_id) for user_id in user_ids]\n```\nAs parsers are bound directly to the registered route function, they have to be defined before the route\nfunction that uses one is registered.\n\n## Resources\nAs your application grows, you may want to split certain functionality amongst resources, similar to\nblueprints of other popular frameworks like Flask.\n\nYou can define a resource like this:\n```\n# store.py\nfrom vial.resources import Resource\n\napp = Resource(__name__)\n\n\n@app.get("/stores/{store_id}")\ndef get_store(store_id: str) -> Store:\n    return store_service.get(store_id)\n\n\n# app.py\nfrom stores import app as stores_app\n\n\napp = Vial(__name__)\n\napp.register_resource(stores_app)\n```\n\n## Middleware\nYou can register middleware functions to be executed before / after route invocations. All middleware is scoped to\nwhere it\'s registered. A middleware function registered with the `Vial` instance is scoped to all routes within\nthe application, but a function registered with a `Resource` instance will only be invoked for routes defined in\nthat specific resource.\n\nBelow is an example of registering a middleware to log route invocation:\n```\nimport logging\nfrom typing import Mapping\nfrom vial.app import Vial\n\napp = Vial(__name__)\n\nlogger = logging.getLogger("my-app")\n\n@app.middleware\ndef log_events(event: Request, chain: CallChain) -> Response:\n    logger.info("Began execution of %s", event.context)\n    try:\n        return chain(event)\n    finally:\n        logger.info("Completed execution of %s", event.context)\n\n\n@app.get("/hello-world")\ndef hello_world() -> Mapping[str, str]:\n    return {"hello": "world"}\n```\n\n\n## Json Encoding\nYou can customize how Vial serializes / deserializes JSON objects by passing a custom encoder. The below\nexample shows how to substitute the native JSON module with another library like `simplejson`:\n```\nimport simplejson\nfrom vial.app import Vial, Json\n\n\nclass SimpleJson(Json):\n    @staticmethod\n    def dumps(value: Any) -> str:\n        return simplejson.dumps(value)\n\n    @staticmethod\n    def loads(value: str) -> Any:\n        return simplejson.loads(value)\n\nclass JsonVial:\n    json_class = SimpleJson\n\n\napp = SimpleJsonVial()\n```\n',
    'author': 'Michael Dimchuk',
    'author_email': 'michaeldimchuk@gmail.com',
    'maintainer': 'Michael Dimchuk',
    'maintainer_email': 'michaeldimchuk@gmail.com',
    'url': 'https://github.com/michaeldimchuk/pyvial',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
