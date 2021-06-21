import os
import pathlib

from aio_tg_bot.etc.conf import settings
from aio_tg_bot.etc.management.commands import migrate


settings.BASE_DIR = pathlib.Path(__file__).parent
migrate.Command().handle()
