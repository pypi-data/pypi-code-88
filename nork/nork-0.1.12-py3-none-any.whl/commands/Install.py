from nork.commands import nork, typer
from subprocess import call
import os


if os.path.isfile('requirements.txt'):
    @nork.command(name="install")
    def handle():
        """
        Install all of requirements.txt
        """
        try:
            call(["pip", "install", "-r", "requirements.txt"])
        except Exception:
            call(["pip3", "install", "-r", "requirements.txt"])
