"""
Abstract env generator module.
"""

import argparse

from rpgt.src.setup.environment.environment_setup import EnvironmentSetup
from rpgt.src.setup.environment.pipenv_setup import PipEnvSetup


def get_env(name: str, args: argparse.Namespace, cwd: str) -> EnvironmentSetup:
    """
    Get env setup.
    :return: the env setup.
    """
    # Environment
    if name == "pipenv":
        env_setup: EnvironmentSetup = PipEnvSetup(args, cwd)
    else:
        raise Exception(f"'{name}' is not supported as an environment")

    return env_setup
