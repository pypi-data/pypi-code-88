import peewee

from aio_tg_bot.etc.conf import settings
from aio_tg_bot.etc.database import models, fields, validators


# noinspection PyUnusedLocal
def migrate(migrator, database, fake=False, **kwargs):
    class State(models.DataBase):
        bot_id = peewee.IntegerField(help_text="Идентефикатор бота")
        chat = peewee.TextField()
        user = peewee.TextField()
        state = peewee.TextField(null=True)
        data = fields.JSONField(null=True)
        bucket = fields.JSONField(null=True)

    State.create_table()

    @migrator.create_model
    class Broadcast(models.DataBase):
        starter_chat_id = peewee.IntegerField(help_text="Чай айди, кто запустил")
        text = peewee.TextField(help_text="Текст рассылки")
        recipients = fields.JSONField(help_text="chat_id получателей")
        success = peewee.IntegerField(default=0, help_text="Кол-во юзеров успешно получили")
        failed = peewee.IntegerField(default=0, help_text="Кол-во юзеров не получили")
        last_send = peewee.TimestampField(default=0, help_text="Последнее отправленное сообщение")

        class Meta:
            table_name = "broadcast"


    class CallbackDataFilter(models.DataBase):
        code = peewee.TextField(index=True, help_text="Код, который будет в callback_data")
        data = fields.JSONField(help_text="Информация с кнопок")

    CallbackDataFilter.create_table()


    class TgBotSettings(models.DataBase):
        coinbase_api_key = peewee.IntegerField(null=True, help_text="Апи ключ коинбаз")
        coinbase_secret_key = peewee.IntegerField(null=True, help_text="Приват ключ коинбейза")
        fiat_currency = fields.TextField(validators=[validators.fiat_currency_validator], help_text="Валюта в боте")

    TgBotSettings.create_table()
    TgBotSettings.create(fiat_currency=settings.DEFAULT_FIAT_CURRENCY)


# noinspection PyUnusedLocal
def rollback(migrator, database, fake=False, **kwargs):
    migrator.remove_model("broadcast")
