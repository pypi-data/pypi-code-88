from click.testing import CliRunner

from rio.commands import cmd_undeploy, cmd_deploy
from rio.commands.cmd_start import cli
from rio.utilities import errors


def test_start_nonlocal():
    """
    Tests that not passing the local flag tells one to contact ChainOpt support.
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert isinstance(result.exception, errors.NoLocalFlagError)


def test_start_bad_package():
    """
    Tests when a bad package name is passed as input
    """
    runner = CliRunner()
    # Undeploys then redeploys the sample project to ensure that something is running
    runner.invoke(cmd_undeploy.cli, ["-l", "-p", "myProject"], input="y\n")
    runner.invoke(cmd_deploy.cli, ["-l", r"..\samples\myProject"])
    result = runner.invoke(cli, ["-l", "-p", "rio-api"])
    assert isinstance(result.exception, errors.PackageExistenceError)


def test_start_no_running_packages():
    """
    Tests when there are no packages running.
    """
    runner = CliRunner()
    # Undeploys ALL packages
    runner.invoke(cmd_undeploy.cli, ["-l", "--all"], input="y\n")
    result = runner.invoke(cli, ["-l", "-p", "rio-api"])
    assert isinstance(result.exception, errors.NoRunningPackagesError)
