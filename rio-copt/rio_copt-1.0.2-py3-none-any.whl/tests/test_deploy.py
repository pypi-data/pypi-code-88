import click.exceptions
from click.testing import CliRunner
from rio.commands.cmd_deploy import cli


def test_deploy_no_folder_path():
    """
    Tests if RIO properly gives an error if no package is given to deploy.
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exception
    assert result.exit_code == 2
    assert "Missing argument" in result.output


def test_deploy_nonlocal():
    """
    Tests that not passing the local flag tells one to contact ChainOpt support.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [r"..\samples\myProject"])
    assert not result.exception
    assert "contact@chainopt.com" in result.output


def test_deploy_bad_package_path():
    """
    Tests error handling when passing through a bad package name.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["-l", "asdfljk"])
    assert not result.exception
    assert "Package not found" in result.output
