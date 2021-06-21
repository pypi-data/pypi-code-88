from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from aio_tg_bot.etc.conf import settings


class IsAdmin(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        if isinstance(message, types.CallbackQuery):
            message = message.message

        return self.is_admin == self.check_user_on_admin(message)

    @staticmethod
    def check_user_on_admin(message):
        return message.user.is_stuff or message.chat.id in settings.ADMINS_IDS
