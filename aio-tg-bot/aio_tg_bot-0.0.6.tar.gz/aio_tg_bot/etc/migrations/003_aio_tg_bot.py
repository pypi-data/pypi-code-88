import peewee

from aio_tg_bot.etc.database import models, fields, validators


# noinspection PyUnusedLocal
def migrate(migrator, database, fake=False, **kwargs):
    migrator.rename_table("broadcast", "tg_bot_broadcast")


# noinspection PyUnusedLocal
def rollback(migrator, database, fake=False, **kwargs):
    migrator.rename_table("tg_bot_broadcast", "broadcast")

