# Copyright 2021 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import configparser
import os
import sys
from urllib.parse import urlparse

import click
import click_completion.core
from xmlhelpy import option

from kadi_apy.cli.decorators import apy_command
from kadi_apy.cli.main import kadi_apy
from kadi_apy.globals import config_path


def _check_instance(config_file, instance):
    """Exit if instance is not defined in the config."""

    instances = config_file.sections()
    instances.remove("global")

    if instance not in instances:
        click.echo(
            "Please use an instance which is defined in the config file.\n"
            f"Choose one of {instances}"
        )
        sys.exit(1)


def _load_config_file():
    """Load config file."""

    if not os.path.isfile(config_path):
        click.echo("Config file does not exits. Please run 'kadi-apy config create'.")
        sys.exit(1)

    config_file = configparser.ConfigParser()

    try:
        config_file.read(config_path)
    except configparser.ParsingError as e:
        click.echo(f"Error during parsing the config file:\n{e}")
        sys.exit(1)

    return config_file


def _is_url(value):
    try:
        result = urlparse(value)
        if not result.netloc or not result.scheme in ["http", "https"]:
            return False
        return True
    except ValueError:
        return False


def _set_config_value(key, instance=None):
    """Set a value in the config file."""

    config_file = _load_config_file()

    if instance is None:
        try:
            instance = config_file["global"]["default"]
        except Exception:
            click.echo("No default instance defined in the config file.")
            sys.exit(1)

    _check_instance(config_file, instance)

    value = input(f"Please enter {key} for instance '{instance}' and press enter: ")

    if key == "host":
        if _is_url(value) is False:
            click.echo(f"Please enter a valid url, not '{value}'.")
            sys.exit(1)

    config_file.set(instance, key, value)

    with open(config_path, "w") as configfile:
        config_file.write(configfile)

    if key == "pat":
        value = value[:5].ljust(len(value), "*")

    click.echo(f"Successfully set '{key}' to '{value}' for instance '{instance}'.")


@kadi_apy.group()
def config():
    """Commands to manage configurations."""


@config.command()
def create():
    """Create the config file to store the information to connect to a Kadi instance."""

    if os.path.exists(config_path):
        click.echo(f"Config file already exists at '{config_path}'. Nothing to create.")
        sys.exit(1)
    else:
        config_file = configparser.ConfigParser()
        default_instance = "my_kadi_instance"

        config_file["global"] = {
            "verify": "True",
            "timeout": "60",
            "default": default_instance,
        }
        config_file[default_instance] = {"host": "", "pat": ""}

        with open(config_path, "w") as configfile:
            config_file.write(configfile)

        click.echo(
            f"Created config file at '{config_path}'.\n"
            "You can open the file to add the information about the host and"
            " personal access token (PAT) or use the CLI."
        )


@config.command()
@option(
    "instance",
    char="I",
    description="Name of the instance defined in the config. If empty, the default"
    " instance defined in the config file is used.",
)
def set_host(instance):
    """Set a host in the config file."""

    _set_config_value("host", instance)


@config.command()
@option(
    "instance",
    char="I",
    description="Name of the instance defined in the config. If empty, the default"
    " instance defined in the config file is used.",
)
def set_pat(instance):
    """Set a personal access token (pat) in the config file."""

    _set_config_value("pat", instance)


@config.command()
@option(
    "instance",
    char="I",
    description="Name of the new instance.",
    required=True,
)
def add_instance(instance):
    """Add a new instance to the config file."""

    config_file = _load_config_file()

    if instance == "global":
        click.echo("Please use a different name.")
        sys.exit(1)

    instances = config_file.sections()
    instances.remove("global")

    if instance in instances:
        click.echo(f"Instance {instance} already present.")
        sys.exit(1)

    config_file.add_section(instance)

    with open(config_path, "w") as configfile:
        config_file.write(configfile)

    _set_config_value("pat", instance)
    _set_config_value("host", instance)


@config.command()
@option(
    "instance",
    char="I",
    description="Name of the new default instance.",
    required=True,
)
def change_default_instance(instance):
    """Change the default instance."""

    config_file = _load_config_file()

    _check_instance(config_file, instance)

    config_file.set("global", "default", instance)

    with open(config_path, "w") as configfile:
        config_file.write(configfile)

    click.echo(f"Default instance is {instance}.")


@config.command()
@option(
    "instance",
    char="I",
    description="Name of the instance to change.",
    required=True,
)
@option(
    "instance-new",
    char="N",
    description="New name of the instance.",
    required=True,
)
def rename_instance(instance, instance_new):
    """Rename an instance."""

    config_file = _load_config_file()

    _check_instance(config_file, instance)
    items = config_file.items(instance)
    config_file.remove_section(instance)
    try:
        config_file.add_section(instance_new)
    except configparser.DuplicateSectionError as e:
        click.echo(f"{e}\nPlease choose another name to rename the instance.")
        sys.exit(1)

    for item in items:
        config_file.set(instance_new, item[0], item[1])

    if config_file.get("global", "default") == instance:
        config_file.set("global", "default", instance_new)

    with open(config_path, "w") as configfile:
        config_file.write(configfile)

    click.echo(f"Changed instance name from '{instance}' to '{instance_new}'.")


@config.command()
def show_instances():
    """Show a list of all instances defined in the config."""

    config_file = _load_config_file()

    instances = config_file.sections()
    instances.remove("global")

    default_instance = config_file.get("global", "default")

    click.echo(
        f"Instances defined in the config file: {instances}.\n"
        f"Default instance is '{default_instance}'."
    )


@config.command()
def activate_autocompletion():
    """Activate the autocompletion."""

    shell, path = click_completion.core.install()
    click.echo(f"Successfully installed {shell} completion in '{path}'.")


@config.command()
@apy_command
def get_kadi_info(manager):
    """Get information about the Kadi instance."""

    manager.misc.get_kadi_info(manager)
