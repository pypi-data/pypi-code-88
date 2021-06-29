from click.testing import CliRunner

from rio.commands import cmd_deploy, cmd_undeploy
from rio.commands.cmd_logs import cli
from rio.utilities import errors


def test_logs_nonlocal():
    """
    Tests that not passing the local flag tells one to contact ChainOpt support.
    """
    runner = CliRunner()
    result = runner.invoke(cli, "afsdl;kj438094fglk")
    assert isinstance(result.exception, errors.NoLocalFlagError)


def test_logs_no_package():
    """
    Tests what happens when no package name is passed through
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert isinstance(result.exception, SystemExit)
    assert result.exit_code == 2


def test_logs_missing_package():
    """
    Tests when a package name is given that doesn't exist
    """
    runner = CliRunner()
    # Undeploys then redeploys the sample project to ensure that something is running
    runner.invoke(cmd_undeploy.cli, ["-l", "-p", "myProject"], input="y\n")
    runner.invoke(cmd_deploy.cli, ["-l", r"..\samples\myProject"])
    result = runner.invoke(cli, ["-l", "rio-api"])
    assert isinstance(result.exception, errors.PackageExistenceError)
