from click.testing import CliRunner

from rio.commands import cmd_begin
from rio.commands.cmd_end import cli
from rio.utilities import errors


def test_end_nonlocal():
    """
    Tests that not passing the local flag tells one to contact ChainOpt support.
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert isinstance(result.exception, errors.NoLocalFlagError)


# TODO: Not working due to unintended behaviour of RIO end
# def test_end_not_running():
#     """
#     Tests to ensure that when there's no image running locally that there will be the proper output.
#     """
#     runner = CliRunner()
#     # First runs the command to ensure that if RIO is running we stop it first.
#     runner.invoke(cli, "-l")
#     result = runner.invoke(cli, "-l")
#     assert not result.exception
#     assert "RIO was not running. To restart, simply run the 'rio begin' command.\n" in result.output


def test_end_base():
    """
    Base case where we end the local rio instance that was already running.
    """
    runner = CliRunner()
    # First ensure that RIO is running
    runner.invoke(cmd_begin.cli, "-l")
    result = runner.invoke(cli, "-l")
    assert not result.exception
    assert "RIO has ended. To restart, simply run the 'rio begin -l' command.\n" in result.output
