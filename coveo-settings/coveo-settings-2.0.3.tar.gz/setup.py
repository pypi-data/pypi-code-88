# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coveo_settings']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'coveo-settings',
    'version': '2.0.3',
    'description': 'Settings driven by environment variables.',
    'long_description': '# coveo-settings\n\nWhenever you want the user to be able to configure something through an environment variable, this module has your back:\n\n```python\nfrom coveo_settings import StringSetting, BoolSetting\n\nDATABASE_URL = StringSetting(\'project.database.url\')\nDATABASE_USE_SSL = BoolSetting(\'project.database.ssl\')\n```\n\nThe user can then configure the environment variables `project.database.url` and `project.database.ssl` to configure the application.\n\nWhen accessed, the values are automatically converted to the desired type:\n\n- `StringSetting` will always be a string\n- `BoolSetting` is either True or False, but accepts "yes|no|true|false|1|0" as input (case-insensitive, of course)\n- `IntSetting` and `FloatSetting` are self-explanatory\n- `DictSetting` allows you to use JSON maps\n- `PathSetting` gives a Path instance, and also implements PathLike and the `/` operator\n\nIf the input cannot be converted to the value type, an `TypeConversionConfigurationError` exception is raised.\n\nA default (fallback) value may be specified. The fallback may be a `callable`.\n\nA validation callback may be specified for custom logic and error messages.\n\n**A setting can be set as sensitive for logging purposes. When logging, use repr(setting) to get the correct representation.**\n\n\n\n## Accessing the value\n\nThere are various ways to obtain the value:\n\n```python\nfrom coveo_settings import BoolSetting\n\nDATABASE_USE_SSL = BoolSetting(\'project.database.ssl\')\n\n# this method will raise an exception if the setting has no value and no fallback\nuse_ssl = bool(DATABASE_USE_SSL)\nassert use_ssl in [True, False]\n\n# this method will not raise an exception\nuse_ssl = DATABASE_USE_SSL.value\nassert use_ssl in [True, False, None]\n\n# use "is_set" to check if there is a value set for this setting; skips validation check\nif DATABASE_USE_SSL.is_set:\n    use_ssl = bool(DATABASE_USE_SSL)\n\n# use "is_valid" to verify if the value passes the validation callback. implies is_set.\nif not DATABASE_USE_SSL.is_valid:\n    ...\n```\n\n\n## Loose environment key matching\n\nMatching the key of the environment variable `project.database.ssl` is done very loosely:\n\n- case-insensitive\n- dots and underscores are ignored completely (`foo_bar` and `f__ooba.r` are equal)\n    - useful for some runners that don\'t support dots in environment variable keys\n\n\n## Use ready validation\n\nYou can quickly validate that a string is in a specific list like this:\n\n```python\nfrom coveo_settings.settings import StringSetting\nfrom coveo_settings.validation import InSequence\n\nENV = StringSetting("environment", fallback="dev", validation=InSequence("prod", "staging", "dev"))\n```\n\n\n## Setting the value\n\nYou can override the value using `setting.value = "some value"` and clear the override with `setting.value = None`. \nClearing the override resumes the normal behavior of the environment variables and the fallback value, if set.\n\nThis is typically used as a way to propagate CLI switches globally.\nFor mocking scenarios, refer to the `Mocking` section below.\n\n\n## Mocking\n\nWhen you need a setting value for a test, use the `mock_config_value` context manager:\n\n```python\nfrom coveo_settings import StringSetting\nfrom coveo_settings.mock import mock_config_value\n\nSETTING = StringSetting(...)\n\nassert not SETTING.is_set\nwith mock_config_value(SETTING, \'new-value\'):\n    assert SETTING.is_set\n```\n\nYou can also clear the value:\n\n```python\nfrom coveo_settings import StringSetting\nfrom coveo_settings.mock import mock_config_value\n\nSETTING = StringSetting(..., fallback=\'test\')\n\nassert SETTING.is_set\nwith mock_config_value(SETTING, None):\n    assert not SETTING.is_set\n```\n',
    'author': 'Jonathan Piché',
    'author_email': 'tools@coveo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/coveooss/coveo-python-oss/tree/main/coveo-settings',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
