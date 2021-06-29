from click.testing import CliRunner

from rio.commands.cmd_undeploy import cli
from rio.utilities import errors


def test_undeploy_nonlocal():
    """
    Tests that not passing the local flag tells one to contact ChainOpt support.
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert isinstance(result.exception, errors.NoLocalFlagError)
