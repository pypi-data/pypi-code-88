import os
import pathlib

from . import BaseCommand
from aio_tg_bot.etc.conf import settings
from aio_tg_bot.etc.database import models
from aio_tg_bot.etc.database.migrations import Router


class Command(BaseCommand):
    def handle(self):
        database = models.DataBase._meta.database

        migrate_dir = os.path.join(pathlib.Path(__file__).parent.parent.parent, "migrations")
        router = Router(database, migrate_dir, module_name="aio_tg_bot")
        router.run()

        router = Router(database, migrate_dir=os.path.join(settings.BASE_DIR, "migrations"), module_name="bot")
        router.run()
