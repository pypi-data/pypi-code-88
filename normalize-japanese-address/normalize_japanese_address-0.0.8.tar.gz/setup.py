# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['normalize_japanese_address',
 'normalize_japanese_address.lib',
 'normalize_japanese_address.tests']

package_data = \
{'': ['*'],
 'normalize_japanese_address': ['japanese_address/api/*',
                                'japanese_address/api/ja/三重県/*',
                                'japanese_address/api/ja/京都府/*',
                                'japanese_address/api/ja/佐賀県/*',
                                'japanese_address/api/ja/兵庫県/*',
                                'japanese_address/api/ja/北海道/*',
                                'japanese_address/api/ja/千葉県/*',
                                'japanese_address/api/ja/和歌山県/*',
                                'japanese_address/api/ja/埼玉県/*',
                                'japanese_address/api/ja/大分県/*',
                                'japanese_address/api/ja/大阪府/*',
                                'japanese_address/api/ja/奈良県/*',
                                'japanese_address/api/ja/宮城県/*',
                                'japanese_address/api/ja/宮崎県/*',
                                'japanese_address/api/ja/富山県/*',
                                'japanese_address/api/ja/山口県/*',
                                'japanese_address/api/ja/山形県/*',
                                'japanese_address/api/ja/山梨県/*',
                                'japanese_address/api/ja/岐阜県/*',
                                'japanese_address/api/ja/岡山県/*',
                                'japanese_address/api/ja/岩手県/*',
                                'japanese_address/api/ja/島根県/*',
                                'japanese_address/api/ja/広島県/*',
                                'japanese_address/api/ja/徳島県/*',
                                'japanese_address/api/ja/愛媛県/*',
                                'japanese_address/api/ja/愛知県/*',
                                'japanese_address/api/ja/新潟県/*',
                                'japanese_address/api/ja/東京都/*',
                                'japanese_address/api/ja/栃木県/*',
                                'japanese_address/api/ja/沖縄県/*',
                                'japanese_address/api/ja/滋賀県/*',
                                'japanese_address/api/ja/熊本県/*',
                                'japanese_address/api/ja/石川県/*',
                                'japanese_address/api/ja/神奈川県/*',
                                'japanese_address/api/ja/福井県/*',
                                'japanese_address/api/ja/福岡県/*',
                                'japanese_address/api/ja/福島県/*',
                                'japanese_address/api/ja/秋田県/*',
                                'japanese_address/api/ja/群馬県/*',
                                'japanese_address/api/ja/茨城県/*',
                                'japanese_address/api/ja/長崎県/*',
                                'japanese_address/api/ja/長野県/*',
                                'japanese_address/api/ja/青森県/*',
                                'japanese_address/api/ja/静岡県/*',
                                'japanese_address/api/ja/香川県/*',
                                'japanese_address/api/ja/高知県/*',
                                'japanese_address/api/ja/鳥取県/*',
                                'japanese_address/api/ja/鹿児島県/*'],
 'normalize_japanese_address.tests': ['.pytest_cache/*',
                                      '.pytest_cache/v/cache/*']}

install_requires = \
['kanjize>=1.0.0,<2.0.0',
 'mojimoji>=0.0.11,<0.0.12',
 'neologdn>=0.5.1,<0.6.0',
 'orjson>=3.5.3,<4.0.0',
 'pytest>=6.2.4,<7.0.0',
 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'normalize-japanese-address',
    'version': '0.0.8',
    'description': 'To normalize Japanese address.',
    'long_description': "\nGeolonia様のオープンソースの住所正規化ライブラリ( https://github.com/geolonia/normalize-japanese-addresses )をPythonに移植したものです。\n現在まだ試作段階であり、Geolonia様のもとのライブラリと完全に同じ動作にはなっていません（テストのうち7.2%で失敗）。\nまた、仕様はすぐに変更する可能性があります。\n\n## インストール方法\n\n- Windows環境の場合は、インストールの前に環境変数を設定してください\n```\nset PYTHONUTF8=1\n```\n\n```\npip install --upgrade normalize_japanese_address\n```\n\n## 使い方\n```python\nfrom normalize_japanese_address.normalize import normalize\n\nresult = normalize('大阪府堺市北区新金岡町4丁1−8')\nprint(result)\n```\n\nとすると、resultに\n```python\n{'pref': '大阪府', 'city': '堺市北区', 'town': '新金岡町四丁', 'address': '1-8', 'level': 3}\n```\nを返します。levelは、住所文字列のどこまでを判別できたかを以下の数値で示しています。\n\n* `0` - 都道府県も判別できなかった。\n* `1` - 都道府県まで判別できた。\n* `2` - 市区町村まで判別できた。\n* `3` - 町丁目まで判別できた。\n\n## ライセンス、利用規約\n- 本プログラムは、下記のプログラムをもとに開発されています。住所データのライセンスは CC BY 4.0、それ以外はMITとされており、本プログラムもそれに従います。\n\nhttps://github.com/geolonia/normalize-japanese-addresses\nhttps://github.com/geolonia/japanese-addresses\n",
    'author': 'SAWADA takahiro',
    'author_email': 'saw@computer.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fanannan/normalize-japanese-address',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
