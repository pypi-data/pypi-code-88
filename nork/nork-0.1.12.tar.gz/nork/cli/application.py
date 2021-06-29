
from typing import Union
import typer
import importlib
import sys

from .. import __version__, config
from ..core import paths


class Application:

    app: typer.Typer

    @classmethod
    def bootstrap(self):
        self.app = typer.Typer(
            help=f"NOR/K {typer.style(__version__, fg=typer.colors.GREEN)}")

        sys.path.append(paths.PROJECT_PATH)

        self.dynamic_commands(["OsEnv", "FrameworkNew", "Install"], "nork.commands")

        if config.get("framework"):
            self.dynamic_commands(["Serve"], "nork.framework.commands")

        self.dynamic_commands(paths.COMMANDS_PATH, "commands")
        self.dynamic_commands(paths.COMMANDS_PATH_APP, "app.commands")

        return self

    def dynamic_commands(path: Union[str, list], module_path: str):
        try:
            for module in (paths.list_dir(path) if isinstance(path, str) else path):
                importlib.import_module(f"{module_path}.{module}")
        except Exception as exception:
            pass
