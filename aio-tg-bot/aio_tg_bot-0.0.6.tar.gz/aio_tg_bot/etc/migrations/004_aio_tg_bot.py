import peewee

from aio_tg_bot.etc.conf import settings
from aio_tg_bot.etc.database import models, fields, validators


# noinspection PyUnusedLocal
def migrate(migrator, database, fake=False, **kwargs):
    @migrator.create_model
    class WrapCache(models.DataBase):
        id = peewee.AutoField()
        key = fields.CharField(unique=True)
        value = peewee.BlobField(null=True)
        time = peewee.IntegerField()

        class Meta:
            table_name = "wrap_cache"


# noinspection PyUnusedLocal
def rollback(migrator, database, fake=False, **kwargs):
    migrator.remove_model("wrap_cache")
