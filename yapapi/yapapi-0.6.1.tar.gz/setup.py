# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yapapi',
 'yapapi._cli',
 'yapapi.executor',
 'yapapi.package',
 'yapapi.payload',
 'yapapi.props',
 'yapapi.rest',
 'yapapi.storage']

package_data = \
{'': ['*']}

install_requires = \
['Deprecated>=1.2.12,<2.0.0',
 'aiohttp-sse-client>=0.1.7,<0.2.0',
 'aiohttp>=3.6,<4.0',
 'async_exit_stack>=1.0.1,<2.0.0',
 'colorama>=0.4.4,<0.5.0',
 'jsonrpc-base>=1.0.3,<2.0.0',
 'more-itertools>=8.6.0,<9.0.0',
 'python-statemachine>=0.8.0,<0.9.0',
 'srvresolver>=0.3.5,<0.4.0',
 'toml>=0.10.1,<0.11.0',
 'typing_extensions>=3.7.4,<4.0.0',
 'urllib3>=1.25.9,<2.0.0',
 'ya-aioclient>=0.5.0,<0.6.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.8,<0.9'],
 'cli': ['fire>=0.3.1,<0.4.0', 'rich>=10.2,<11.0'],
 'integration-tests:python_version >= "3.8.0" and python_version < "4.0.0"': ['goth>=0.4,<0.5']}

setup_kwargs = {
    'name': 'yapapi',
    'version': '0.6.1',
    'description': 'High-level Python API for the New Golem',
    'long_description': '# Golem Python API\n\n[![Tests - Status](https://img.shields.io/github/workflow/status/golemfactory/yapapi/Continuous%20integration/master?label=tests)](https://github.com/golemfactory/yapapi/actions?query=workflow%3A%22Continuous+integration%22+branch%3Amaster)\n![PyPI - Status](https://img.shields.io/pypi/status/yapapi)\n[![PyPI version](https://badge.fury.io/py/yapapi.svg)](https://badge.fury.io/py/yapapi)\n[![GitHub license](https://img.shields.io/github/license/golemfactory/yapapi)](https://github.com/golemfactory/yapapi/blob/master/LICENSE)\n[![GitHub issues](https://img.shields.io/github/issues/golemfactory/yapapi)](https://github.com/golemfactory/yapapi/issues)\n\n## What\'s Golem, btw?\n\n[Golem](https://golem.network) is a global, open-source, decentralized supercomputer\nthat anyone can access. It connects individual machines - be that laptops, home PCs or\neven data centers - to form a vast network, the purpose of which is to provide a way to\ndistribute computations to its provider nodes and allow requestors to utilize its unique\npotential - which can lie in its combined computing power, the geographical distribution\nor its censorship resistance.\n\n## Golem\'s requestor setup\n\nGolem\'s requestor-side configuration consists of two separate components:\n* the [`yagna` daemon](https://github.com/golemfactory/yagna) - your node in the\n  new Golem network, responsible for communication with the other nodes, running the\n  market and providing easy access to the payment mechanisms.\n* the requestor agent - the part that the developer of the specific Golem application\n  is responsible for.\n\nThe daemon and the requestor agent communicate using three REST APIs which\n`yapapi` - Golem\'s Python high-level API - aims to abstract to large extent to make\napplication development on Golem as easy as possible.\n\n## How to use this API?\n\nAssuming you have your Golem node up and running (you can find instructions on how to\ndo that in the [yagna repository](https://github.com/golemfactory/yagna) and in our\n[handbook](https://handbook.golem.network)), what you need to do is:\n* **prepare your payload** - this needs to be a Docker image containing your application\n  that will be executed on the provider\'s end. This image needs to have its volumes\n  mapped in a way that will allow the supervisor module to exchange data (write and\n  read files) with it. This image needs to be packed and uploaded into Golem\'s image repository\n  using our dedicated tool - [`gvmkit-build`](https://pypi.org/project/gvmkit-build/).\n* **create your requestor agent** - this is where `yapapi` comes in. Utilizing our high-level\n  API, the creation of a requestor agent should be straightforward and require minimal effort.\n  You can use examples contained in this repository as references, the directory\n  [`examples/hello-world/`](https://github.com/golemfactory/yapapi/tree/master/examples/hello-world)\n  contains minimal examples of fully functional requestor agents and\n  is therefore the best place to start exploring.\n\n\n### Components\n\nThere are a few components that are crucial for any requestor agent app:\n\n#### Golem\n\nThe heart of the high-level API is the `Golem` class (`yapapi.Golem`), which serves as \nthe "engine" of a requestor agent. `Golem` is responsible for finding providers interested in\nthe jobs you want to execute, negotiating agreements with them and processing payments. It also\nimplements core functionality required to execute commands on providers that have signed such agreements.\n\n`Golem` provides two entry points for executing jobs on the Golem network, corresponding to the\ntwo basic modes of operation of a requestor agent:\n\n* The method `execute_tasks` allows you to submit a _task-based_ job for execution. Arguments\nto this method must include a sequence of independent _tasks_ (units of work) to be distributed\namong providers, a _payload_ (a VM image) required to compute them, and a _worker_ function, which\nwill be used to convert each task to a sequence of steps to be executed on a provider. You may also\nspecify the timeout for the whole job, the maximum number of providers used at any given time,\nand the maximum amount that you want to spend.\n\n* The method `run_service` allows you, as you probably guessed, to run a _service_ on Golem. \nInstead of a task-processing worker function, an argument to `run_service` is a\nclass (a subclass of `yapapi.Service`) that implements the behaviour of your service in various\nstages of its lifecycle (when it\'s _starting_, _running_ etc.). Additionally, you may specify\nthe number of _service instances_ you want to run and the service expiration datetime.\n\nPrior to version `0.6.0`, only task-based jobs could be executed. For more information on both types of jobs please refer to our [handbook](https://handbook.golem.network).\n \n#### Worker function\n\nThe worker will most likely be the very core of your task-based requestor app.\nYou need to define this function in your agent code and then you pass it (as the value of\nthe `worker` parameter) to the `execute_tasks` method of `Golem`.\n\nThe worker receives a _work context_ (`yapapi.WorkContext`) object that serves\nas an interface between your script and the execution unit within the provider.\nUsing the work context, you define the steps that the provider needs to execute in order\nto complete the job you\'re giving them - e.g. transferring files to and from the provider\nor running commands within the execution unit on the provider\'s end.\n\nDepending on the number of workers, and thus, the maximum number of providers that \n`execute_tasks` utilizes in parallel, a single worker may tackle several tasks\nand you can differentiate the steps that need to happen once\nper worker run, which usually means once per provider node - but that depends on the\nexact implementation of your worker function - from those that happen for each\ntask. An example of the former would be an upload of a source\nfile that\'s common to each task; and of the latter - a step that triggers the\nprocessing of the file using a set of parameters specified for a particular task.\n\n#### Task\n\nThe _task_ (`yapapi.Task`) object describes a unit of work that your application needs\nto carry out.\n\n`Golem` will feed an instance of your worker - bound to a single provider node -\nwith `Task` objects. The worker will be responsible for completing those tasks. Typically,\nit will turn each task into a sequence of steps to be executed in a single run\nof the execution script on a provider\'s machine, in order to compute the task\'s result.\n\n\n### Example\n\nAn example task-based Golem application, using a minimal Docker image\n(Python file with the example and the Dockerfile for the image reside in\n[`examples/hello-world/`](https://github.com/golemfactory/yapapi/tree/master/examples/hello-world)):\n```python\nimport asyncio\nfrom typing import AsyncIterable\n\nfrom yapapi import Golem, Task, WorkContext\nfrom yapapi.log import enable_default_logger\nfrom yapapi.payload import vm\n\n\nasync def worker(context: WorkContext, tasks: AsyncIterable[Task]):\n    async for task in tasks:\n        context.run("/bin/sh", "-c", "date")\n\n        future_results = yield context.commit()\n        results = await future_results\n        task.accept_result(result=results[-1])\n\n\nasync def main():\n    package = await vm.repo(\n        image_hash="d646d7b93083d817846c2ae5c62c72ca0507782385a2e29291a3d376",\n    )\n\n    tasks = [Task(data=None)]\n\n    async with Golem(budget=1.0, subnet_tag="devnet-beta.2") as golem:\n        async for completed in golem.execute_tasks(worker, tasks, payload=package):\n            print(completed.result.stdout)\n\n\nif __name__ == "__main__":\n    enable_default_logger(log_file="hello.log")\n\n    loop = asyncio.get_event_loop()\n    task = loop.create_task(main())\n    loop.run_until_complete(task)\n```\n',
    'author': 'Przemysław K. Rekucki',
    'author_email': 'przemyslaw.rekucki@golem.network',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/golemfactory/yapapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
