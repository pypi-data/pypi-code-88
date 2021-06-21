import click

from slai_cli.model.create import create_new_model
from slai_cli.model.save import save_model
from slai_cli.model.open import open_model
from slai_cli.model.list import list_models
from slai_cli.model.train import train_model
from slai_cli.model.call import call_model
from slai_cli.model.test import test_model
from slai_cli.model.deploy import deploy_model
from slai_cli.model.checkout import checkout_model_version
from slai_cli.exceptions import ModelExistsException, InvalidApiKey


@click.group()
def model():
    pass


@model.command()
@click.argument("model_name")
@click.option("--template", required=False, help="An optional notebook template.")
@click.option(
    "--from-model", required=False, help="Start from another model in your project"
)
@click.option("--watch/--no-watch", default=True)
def create(model_name, template, from_model, watch):
    """Create new model."""

    try:
        created = create_new_model(model_name, from_model=from_model)
    except (ModelExistsException, InvalidApiKey):
        return

    if created:
        open_model(model_name, watch=watch)


@model.command()
@click.argument("model_name")
def save(model_name):
    """Save changes to local model trainer."""
    save_model(model_name)


@model.command()
@click.argument("model_name")
@click.option("--watch/--no-watch", default=True)
def open(model_name, watch):
    """Open model notebook in your browser."""
    open_model(model_name, watch=watch)


@model.command()
@click.argument("model_name")
def train(model_name):
    """Train a model locally using the local trainer files."""
    train_model(model_name)


@model.command()
@click.argument("model_name")
@click.option("-name", default=None, required=False)
def checkout(model_name, name):
    checkout_model_version(model_name=model_name, version_name=name)


@model.command()
@click.argument("model_name")
def call(model_name):
    """Call a model using the inference client directly."""
    call_model(model_name=model_name, input={})


@model.command()
@click.argument("model_name")
def test(model_name):
    """Test a model/handler locally before deploying."""
    test_model(model_name=model_name)


@model.command()
@click.argument("model_name")
@click.option(
    "--version", required=False, default="latest", help="An option model version ID."
)
def deploy(model_name, version):
    """
    Deploy a model artifact and handler.
    """

    # TODO: support explicit model artifact IDs
    deploy_model(
        model_name=model_name,
        version=version,
    )


@model.command()
def list():
    """List models in the project."""
    list_models()
