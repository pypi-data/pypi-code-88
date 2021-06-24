"""
Author:     LanHao
Date:       2021/6/24 9:13

"""
from dynaconf import Dynaconf

conf = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
    load_dotenv=True,
)

