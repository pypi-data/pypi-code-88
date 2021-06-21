"""
Git hooks generator module.
"""

import os
import stat
import subprocess  # nosec

from rpgt.src.generators.generator import Generator


class GitHooksGenerator(Generator):
    """
    Git hooks generator class.
    """

    def generate(self, cwd: str) -> None:
        """
        Generates the git hooks files.
        """
        # generate a .git folder
        with subprocess.Popen(  # nosec
            ["git", "init"], stdout=subprocess.PIPE
        ) as process:
            process.wait()

        # symlink the githooks folder to the hookspath
        with subprocess.Popen(  # nosec
            ["git", "config", "--local", "core.hooksPath", ".githooks/"],
            stdout=subprocess.PIPE,
        ) as process:
            process.wait()

        # pre-commit file
        file_path = f"{cwd}/.githooks/pre-commit"
        with open(file_path, "w") as file:
            file.write(self.generate_pre_commit())

        # make the file executable
        stat_call = os.stat(file_path)
        os.chmod(file_path, stat_call.st_mode | stat.S_IEXEC)

    def generate_pre_commit(self) -> str:
        """
        Generates pre commit message.
        :return: a stringual representation of the pre commit messag.
        """
        text = ["#!/bin/sh"]

        if self.args.lint:
            # Auto fix import sorting issues
            text.append("pipenv run isort .")
            text.append("pipenv run black .")

        return "\n".join(text)
