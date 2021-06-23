import asyncio
import sys

import click
import ruamel.yaml
from sqlalchemy.exc import ArgumentError

from palaestrai.core import RuntimeConfig
from palaestrai.experiment import Executor, ExecutorState
from palaestrai.experiment.experiment_run import ExperimentRun as Experiment


@click.group()
def client():
    pass


@client.command()
@click.argument(
    "experiment_file",
    type=click.Path(
        exists=True, dir_okay=False, readable=True, allow_dash=True
    ),
)
def experiment_start(experiment_file):
    """Start an experiment from a file"""
    experiment = Experiment.load(experiment_file)
    executor = Executor()
    executor.schedule(experiment)
    executor_final_state = asyncio.run(executor.execute())
    if executor_final_state != ExecutorState.EXITED:
        sys.exit(
            {
                ExecutorState.SIGINT: -2,
                ExecutorState.SIGABRT: -6,
                ExecutorState.SIGTERM: -15,
            }[executor_final_state]
        )


def _get_store_uri():
    config = RuntimeConfig()
    if not config.store_uri:
        click.echo(
            "Please create a runtime config (one of %s), "
            "and set the 'store_uri' options.\n"
            "My configuration, loaded from %s, does not contain it."
            % (config.CONFIG_FILE_PATHS, config._config_file_path),
            file=sys.stderr,
        )
        exit(1)

    return config.store_uri


@client.command()
def database_create():
    """Create the store database. Requires a runtime configuration file."""
    store_uri = _get_store_uri()
    if not store_uri:
        exit(1)
    from palaestrai.store.database_util import setup_database

    try:
        setup_database(store_uri)
    except ArgumentError as e:
        click.echo(
            "SQLalchemy could not open a database connection. "
            "Please make sure that your 'store_uri' in %s is formed like "
            "'driver://user:password@host/database'. Error was: %s"
            % (RuntimeConfig()._config_file_path, e),
            file=sys.stderr,
        )
        exit(1)


@client.command()
def database_migrate():
    store_uri = _get_store_uri()
    if not store_uri:
        exit(1)


@client.command()
def runtime_config_show_default():
    """Shows the default runtime config and search paths."""
    yml = ruamel.yaml.YAML(typ="safe")
    print("%YAML 1.2\n")
    print("# palaestrAI Runtime Configuration")
    print(
        f"# Search path for this file is: {RuntimeConfig().CONFIG_FILE_PATHS}"
    )
    print("#\n\n---")
    yml.dump(RuntimeConfig().DEFAULT_CONFIG, stream=sys.stdout)


@client.command()
def runtime_config_show_effective():
    """Shows the currently effective runtime configuration"""
    yml = ruamel.yaml.YAML(typ="safe")
    print("%YAML 1.2")
    print(f"# Configuration loaded from: {RuntimeConfig()._config_file_path}")
    print("---")
    yml.dump(RuntimeConfig().to_dict(), stream=sys.stdout)
