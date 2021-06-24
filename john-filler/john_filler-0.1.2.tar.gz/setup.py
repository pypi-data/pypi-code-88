# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['john_filler', 'john_filler.nafuka']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['john_filler = john_filler.main:main']}

setup_kwargs = {
    'name': 'john-filler',
    'version': '0.1.2',
    'description': "John team's filler",
    'long_description': '# john_filler\n\njohn_fillerは42の課題、fillerのPython実装です。\n\n## 開発者向け情報\n\n### poetryインストール手順\n\n1. 公式のインストール手順に従いインストール。\n\n   pythonだと2系なので、python3に変更しています。\n\n   ```bash\n   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 - \n   ```\n\n1. ~/.zshrcを編集。poetryのPATHを追加するコマンドを追記します。\n\n   ```bash\n   export PATH="/Users/{login}/Library/Python/3.9/bin:$PATH"\n   ```\n\n   ~/.zshrcの変更を今のshellに反映します。\n\n   ```bash\n   source ~/.zshrc\n   ```\n\n1. venvの保存場所の設定を変更\n\n   venvはデフォルトで ` /Users/{login}/Library/Caches/pypoetry/virtualenvs` にインストールされます。\n\n   プロジェクトの中に置きたいので、設定を行います。\n\n   ```bash\n   poetry config virtualenvs.in-project true\n   ```\n\n   設定を行うと、poetry addなどで、`{プロジェクトのディレクトリ}/.venv` に仮想環境が作られます。\n\n   `poetry shell` で仮想環境の中に入ることができます。\n\n### PyPIへのパッケージアップロード手順\n\n参考\n\n- [[Python] poetryを使用したPyPIパッケージ公開手順 - Qiita](https://qiita.com/sengoku/items/af301fe89b55706ca0c2)\n\n1. [PyPI](https://pypi.org/) or [TestPyPI](https://test.pypi.org/) にユーザ登録します。\n\n1. API Tokenを発行、poetryに登録します。\n\n1. パッケージをビルドします。\n\n   ```bash\n   poetry build\n   ```\n\n1. パッケージをアップロードします。\n\n   ```bash\n   # TestPyPI\n   poetry publish -r testpypi\n   # PyPI\n   poetry publish\n   ```\n\n   アップロードの際、バージョンが既にあるバージョンとは異なる必要があります（パッケージを削除してもNGなようです）。\n\n   このため、TestPyPIにアップロードして確認後、PyPIにアップロードが安全かと思います。\n',
    'author': 'John team',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
