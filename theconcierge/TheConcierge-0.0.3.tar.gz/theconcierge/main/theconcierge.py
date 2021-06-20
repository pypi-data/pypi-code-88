from telethon import TelegramClient

from ..settings.config import Config
from ..listener.listener import Listener


class TheConcierge:
    def __init__(self):
        self.bot = TelegramClient(
            Config._get_system_path() + "bot", 
            api_id=Config.get_system("api_id"), 
            api_hash=Config.get_system("api_hash")
        )

    def start_bot(self):
        self.bot.start(bot_token=Config.get_system("bot_token"))
        Listener.add_handlers(self.bot)
        print("The Concierge Bot is up and running!")
        self.bot.run_until_disconnected()
