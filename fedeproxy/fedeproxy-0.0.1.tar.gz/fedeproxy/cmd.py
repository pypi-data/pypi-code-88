import logging
import os
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager

from fedeproxy.version import __version__

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fedeproxy.settings")


class FedeproxyApp(App):
    def __init__(self, modules):
        super().__init__(
            description="fedeproxy",
            version=__version__,
            command_manager=CommandManager(modules),
            deferred_help=True,
        )

    def configure_logging(self):
        super().configure_logging()

        root_logger = logging.getLogger("")
        root_logger.setLevel(logging.WARNING)

        level = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}.get(
            self.options.verbose_level, logging.DEBUG
        )

        root_logger = logging.getLogger("fedeproxy")
        root_logger.setLevel(level)


def main(argv=sys.argv[1:]):
    myapp = FedeproxyApp("fedeproxy.cli")
    return myapp.run(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
