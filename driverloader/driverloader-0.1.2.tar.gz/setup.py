# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['driverloader']

package_data = \
{'': ['*']}

install_requires = \
['click']

entry_points = \
{'console_scripts': ['driverloader = driverloader.cli:cli']}

setup_kwargs = {
    'name': 'driverloader',
    'version': '0.1.2',
    'description': 'A webdriver downloader',
    'long_description': "## Quick start:\n\nDownload chrome driver:\n```python\nfrom driverloader import chrome_driver\nprint(chrome_driver.default)\n```\n\nDownload firefox driver:\n```python\nfrom driverloader import firefox_driver\nprint(firefox_driver.default)\n```\n\nThe drivers would be downloaded in **executor/** dir of the webdrivers package.\nYou can find chromedriver.exe or geckodriver.exe in the dir.\n\n\nUsing with selenium:\n```python\nfrom selenium.webdriver import Chrome\nfrom driverloader import chrome_driver\n\nbrowser = Chrome(chrome_driver.default)\nbrowser.quit()\n```\n\nDownloading to customized path:\n```python\nfrom driverloader import chrome_driver\ndriver_path = chrome_driver(path='.')\n```\n\nor absolute path:\n```python\nimport pathlib\nfrom driverloader import chrome_driver\n\ncurrent_dir = pathlib.Path(__file__).parent.parent\nprint(chrome_driver(current_dir))\n```\n\ncustomized version:\n```python\nfrom driverloader import chrome_driver\ndriver_path = chrome_driver(path='.', version='70')\n```\n\n\n## command line\nUsing driverloader by command line like this:\n```bash\ndriverloader chrome .\ndriverloader firefox .\n```\nTwo arguments:\n- driver_name, chrome and firefox supported.\n- path,  the path you want to save the driver.\n\nOptions:\n- `-v` or `--version`,  the version would be downloaded.\n- `-f` or `--force`, force downloading if the similar driver exists\n\n## System Platform\nDriverloader would download the given version according to your OS,\nwindows, mac, linux are all OK.\n\n\n## Mirror URL\nwebdriver-downloader get the drivers from https://npm.taobao.org/mirrors/\n- chrome driver: https://npm.taobao.org/mirrors/chromedriver/\n- firefox driver: https://npm.taobao.org/mirrors/geckodriver/",
    'author': 'yuze',
    'author_email': 'looker53@sina.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/looker53/webdriver-downloader',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
