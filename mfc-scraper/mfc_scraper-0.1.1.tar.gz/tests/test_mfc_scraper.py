#!/usr/bin/env python

"""Tests for `mfc_scraper` package."""

import pytest

from click.testing import CliRunner

from mfc_scraper import scraper
from mfc_scraper import __main__


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(__main__.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help' in help_result.output
