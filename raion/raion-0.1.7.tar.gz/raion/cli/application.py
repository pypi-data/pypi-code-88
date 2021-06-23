import typer
from raion import __app_version__, __app_name__
from raion.core import paths
import importlib
import os
import sys

class Application:

    app: typer.Typer

    @classmethod
    def bootstrap(self, path: str = None):
        version  = typer.style(__app_version__, fg=typer.colors.GREEN)
        self.app = typer.Typer(help=f"Raion Framework {version}")

        self.static_commands()
        self.dynamic_commands()

        return self

    def static_commands():
        for module in ["KeyGenerate", "Os", "Serve"]:
            importlib.import_module(f"raion.commands.{module}")

    def dynamic_commands():
        try:
            sys.path.append(paths.PROJECT_PATH)

            for module in paths.list_dir(paths.COMMANDS_PATH):
                importlib.import_module(f"app.commands.{module}")
        except Exception as e:
            pass