import logging
from loguru import logger
import asyncio
import io
import os
from aiogram import types

from aio_tg_bot.etc.conf import settings


class BaseHandler:
    LEVELS_MAP = {
        logging.CRITICAL: "CRITICAL",
        logging.ERROR: "ERROR",
        logging.WARNING: "WARNING",
        logging.INFO: "INFO",
        logging.DEBUG: "DEBUG",
    }

    def _get_level(self, record):
        return self.LEVELS_MAP.get(record.levelno, record.levelno)


class SendErrorToTelegram(BaseHandler, logging.Handler):
    errors = []

    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

        if self.bot is not None:
            asyncio.create_task(self.sender(self.bot))

    def emit(self, record):
        if self.LEVELS_MAP[logging.ERROR] == self._get_level(record):
            self.errors.append(record)

    async def sender(self, bot):
        while True:
            for error in self.errors:
                file = "error.txt"

                with open(file, "w") as f:
                    f.write(str(error.exc_text))

                for admin_chat_in in settings.ADMINS_IDS:
                    await bot.send_document(admin_chat_in, types.InputFile(file))

                os.remove(file)
                self.errors.remove(error)

            await asyncio.sleep(0.5)


class InterceptHandler(BaseHandler, logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(self._get_level(record), record.getMessage())


def setup(logging_level="INFO", bot=None, logger_file=None):
    telegram_handler = SendErrorToTelegram(bot=bot)

    if logger_file is None:
        logging.basicConfig(handlers=[InterceptHandler(), telegram_handler], level=logging_level)
    else:
        logger = logging.getLogger()
        logging_level = getattr(logging, logging_level)

        logger.setLevel(logging_level)
        handler = logging.FileHandler(logger_file, "w", encoding="UTF-8")
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"))
        logger.addHandler(handler)
