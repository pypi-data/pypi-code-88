import peewee
import functools

from . import model, fields, validators


DataBase = model.Model


class State(DataBase):
    bot_id = peewee.IntegerField(help_text="Идентефикатор бота")
    chat = peewee.TextField()
    user = peewee.TextField()
    state = peewee.TextField(null=True)
    data = fields.JSONField(null=True)
    bucket = fields.JSONField(null=True)


class TGBotBroadcast(DataBase):
    starter_chat_id = peewee.IntegerField(help_text="Чай айди, кто запустил")
    text = peewee.TextField(help_text="Текст рассылки")
    recipients = fields.JSONField(help_text="chat_id получателей")
    success = peewee.IntegerField(default=0, help_text="Кол-во юзеров успешно получили")
    failed = peewee.IntegerField(default=0, help_text="Кол-во юзеров не получили")
    last_send = peewee.TimestampField(default=0, help_text="Последнее отправленное сообщение")


Broadcast = TGBotBroadcast


class CallbackDataFilter(DataBase):
    code = peewee.TextField(index=True, help_text="Код, который будет в callback_data")
    data = fields.JSONField(help_text="Информация с кнопок")


class TgBotSettings(DataBase):
    coinbase_api_key = peewee.IntegerField(null=True, help_text="Апи ключ коинбаз")
    coinbase_secret_key = peewee.IntegerField(null=True, help_text="Приват ключ коинбейза")
    fiat_currency = fields.TextField(validators=[validators.fiat_currency_validator], help_text="Валюта в боте")

    CREATE_FIRST_RECORD = True


class Users(DataBase):
    bot_id = peewee.IntegerField(help_text="Айди бота, в котором юзер")
    chat_id = peewee.IntegerField(help_text="Чат айди юзера")
    username = peewee.TextField(null=True, help_text="Юзернейм юзера")
    is_stuff = peewee.BooleanField(default=False)
    joined_date = peewee.TimestampField(help_text="Дата регистрации")
    last_use = peewee.TimestampField(help_text="Последние использование")

    @classmethod
    @functools.lru_cache()
    def get_modified_model(cls):
        return cls.__subclasses__()[0]

    @classmethod
    @functools.lru_cache()
    def get_model(cls):
        if 0 < len(cls.__subclasses__()):
            user_model = cls.__subclasses__()[0]
        else:
            user_model = cls

        return user_model


class MigrateHistory(DataBase):

    """Presents the migrations in database."""

    name = peewee.CharField()
    module = peewee.CharField(null=True)
    migrated_at = peewee.TimestampField()

    def __unicode__(self):
        """String representation."""
        return self.name


class WrapCache(DataBase):
    key = fields.CharField(unique=True)
    value = peewee.BlobField(null=True)
    time = peewee.IntegerField()
