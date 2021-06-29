from click.testing import CliRunner

from rio.commands.cmd_deploy import cli
from rio.utilities import errors


def test_deploy_no_package():
    """
    Tests if RIO properly gives an error if no package is given to deploy.
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert isinstance(result.exception, SystemExit)
    assert result.exit_code == 2
    assert "Missing argument" in result.output


def test_deploy_nonlocal():
    """
    Tests that not passing the local flag tells one to contact ChainOpt support.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [r"..\samples\myProject"])
    assert isinstance(result.exception, errors.NoLocalFlagError)


def test_deploy_bad_package_path():
    """
    Tests error handling when passing through a bad package name.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["-l", "asdfljk"])
    assert isinstance(result.exception, errors.PackagePathError)

