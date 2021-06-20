"""dtool tag CLI commands."""

import sys

import dtoolcore
import click

from dtool_cli.cli import base_dataset_uri_argument


def _validate_name(name):
    if not dtoolcore.utils.name_is_valid(name):
        click.secho("Invalid tag '{}'".format(name), fg="red")
        click.secho(
            "Tag must be 80 characters or less",
        )
        click.secho(
            "Tags may only contain the characters: {}".format(
                " ".join(dtoolcore.utils.NAME_VALID_CHARS_LIST)
            ),
        )
        click.secho("Example: first-class")
        sys.exit(400)


@click.group()
def tag():
    """Tags provide per dataset metadata."""


@tag.command(name="set")
@base_dataset_uri_argument
@click.argument("tag")
def set_tag(dataset_uri, tag):
    """Add a tag to a dataset."""
    try:
        dataset = dtoolcore.ProtoDataSet.from_uri(
            uri=dataset_uri,
            config_path=dtoolcore.utils.DEFAULT_CONFIG_PATH
        )
    except dtoolcore.DtoolCoreTypeError:
        dataset = dtoolcore.DataSet.from_uri(
            uri=dataset_uri,
            config_path=dtoolcore.utils.DEFAULT_CONFIG_PATH
        )

    # Make code Python2 compatible.
    tag = str(tag)

    _validate_name(tag)

    dataset.put_tag(tag)


@tag.command(name="ls")
@base_dataset_uri_argument
def list_tags(dataset_uri):
    """List the dataset tags."""
    try:
        dataset = dtoolcore.ProtoDataSet.from_uri(
            uri=dataset_uri,
            config_path=dtoolcore.utils.DEFAULT_CONFIG_PATH
        )
    except dtoolcore.DtoolCoreTypeError:
        dataset = dtoolcore.DataSet.from_uri(
            uri=dataset_uri,
            config_path=dtoolcore.utils.DEFAULT_CONFIG_PATH
        )
    for tag in sorted(dataset.list_tags()):
        click.secho("{}".format(tag))


@tag.command(name="delete")
@base_dataset_uri_argument
@click.argument("tag")
def delete_tag(dataset_uri, tag):
    """Delete a dataset tag."""
    try:
        dataset = dtoolcore.ProtoDataSet.from_uri(
            uri=dataset_uri,
            config_path=dtoolcore.utils.DEFAULT_CONFIG_PATH
        )
    except dtoolcore.DtoolCoreTypeError:
        dataset = dtoolcore.DataSet.from_uri(
            uri=dataset_uri,
            config_path=dtoolcore.utils.DEFAULT_CONFIG_PATH
        )

    # Make code Python2 compatible.
    tag = str(tag)

    dataset.delete_tag(tag)
