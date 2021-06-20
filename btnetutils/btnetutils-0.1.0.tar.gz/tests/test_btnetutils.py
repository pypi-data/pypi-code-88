#!/usr/bin/env python

"""Tests for `btnetutils` package."""

import pytest

from click.testing import CliRunner

from btnetutils import cli

def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.btnetutils)
    assert 'Simple CLI for dealing with net configs' in result.output
    assert result.exit_code == 0
    help_result = runner.invoke(cli.btnetutils, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
