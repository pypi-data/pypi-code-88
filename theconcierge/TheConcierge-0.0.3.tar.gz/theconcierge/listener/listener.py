from .handlers import Handlers


class Listener:
    @staticmethod
    def add_handlers(bot):
        for handler in Handlers.get_handlers():
            bot.add_event_handler(handler)
