# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dandori']

package_data = \
{'': ['*']}

install_requires = \
['ghapi>=0.1.17,<0.2.0',
 'python-box>=5.3.0,<6.0.0',
 'ruamel.yaml>=0.17.10,<0.18.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['dandori = dandori.__main__:main']}

setup_kwargs = {
    'name': 'dandori',
    'version': '0.1.2',
    'description': 'GitHub Actions with Python',
    'long_description': '# dandori: GitHub Actions with Python\n\ndandori runs on your Actions, and automate workflow with using Python.\n\n**Current Status is Super Early Alpha. DO NOT USE IT in your production repository.**\n\n\n## How to Use\n\nFirst, You need to define workflow.\nYou can hook any [events](https://docs.github.com/en/actions/reference/events-that-trigger-workflows) without manual/scheduled workflow such as `pull_request`, `push` or `pull_request_review`.\n\n```yaml\nname: dandori_action\non: [pull_request, issue_comment]\n\njobs:\n  run:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v2\n      - uses: actions/setup-python@v2\n        with:\n          python-version: \'3.9\'\n      - run: pip install dandori\n      - run: dandori run\n        env:\n          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}\n```\n\nNext, you can write your Python script or package on your repo, like `dandori_handler.py` or \'dandori_handlers/\'. dandori automatically import your code and run handler functions defined in your code:\n\n```py\n## dandori_handler.py\n\ndef handle_pull_request(ctx):\n    if ctx.gh.payload.action == \'synchronize\':\n        ctx.gh.create_comment("You pushed new commits!!")\n\n\ndef handle_pull_request_comment(ctx):\n    """It\'s a special handler type, issue_comment event on PR"""\n    comment_body = ctx.gh.comment_body().strip()\n    if comment_body.startswith(\'/some-command\'):\n        some_code_as_you_like()\n```\n\nIf you want more than one file, you need to make a package:\n\n```py\n## handlers/__init__.py\n# Must be relative imports\nfrom .pull_request import handle_pull_request\nfrom .issue import handle_issue\n\n## handlers/pull_request.py\ndef handle_pull_request(ctx):\n    ...\n\n## -- handlers/issue.py\ndef handle_issue(ctx):\n    ...\n```\n\n## Configuration\n\ndandori supports `pyproject.toml`, or make any toml file as you like (default is `dandori.toml`).\n\nIn pyproject.toml, write config in `tool.dandori` section:\n\n```toml\n# pyproject.toml\n[tool.dandori]\nhandlers = [\'path/to/handler\']\n```\n\nIn independent toml file, write config in `dandori` section:\n\n```toml\n# dandori.toml\n[dandori]\nhandlers = [\'path/to/handler\']\n```\n\n\n## Use case\n\n### Share CI code with multiple repo:\n\n\n```yaml\nname: dandori_action\non: [pull_request, issue_comment]\n\njobs:\n  run:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v2\n      - uses: actions/checkout@v2\n        with:\n          repository: your/dandori-handler\n          ref: v1  # something you need\n          ssh-key: ${{ secrets.your_repo_key }}\n          path: dandori-handler\n      - uses: actions/setup-python@v2\n        with:\n          python-version: \'3.9\'\n      - run: pip install dandori\n      - run: dandori run -f dandori-handler/dandori.toml\n        env:\n          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}\n```\n\n### Use third party package in handler\n\nYour handler module or package will be imported dynamically, so you can install any library in the "(virtual)env" same as dandori installed.\n\nMost simple cale, install dandori with other library:\n\n```\n# Install libraries with pip\n- run: pip install dandori requests python-dateutil\n```\n\nIf you want use just a "command" and not to use global env, use `ctx.ops.run_venv()`:\n\n```py\ndef handle_pull_request(ctx):\n    ctx.ops.run_venv(["pip", "install", "twine"])\n    ctx.ops.run_venv([\'twine\', \'upload\', \'dist/*\'])\n```\n\nOr dynamically install it and use it:\n\n```py\nimport importlib\n\ndef handle_pull_request(ctx):\n    ctx.ops.run(["pip", "install", "requests"])\n    requests = importlib.import_module(\'requests\')\n```',
    'author': 'Hiroyuki Tanaka',
    'author_email': 'aflc0x@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/roy-ht/dandori',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
