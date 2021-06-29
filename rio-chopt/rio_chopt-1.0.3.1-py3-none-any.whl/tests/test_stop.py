from click.testing import CliRunner

from rio.commands.cmd_stop import cli
from rio.utilities import errors


def test_stop_nonlocal():
    """
    Tests that not passing the local flag tells one to contact ChainOpt support.
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert isinstance(result.exception, errors.NoLocalFlagError)
