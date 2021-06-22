""" pytest module to hold tests for webstaterator/cli.py and webstaterator/__main__.py """

import os
import shutil
import argparse

import pytest


from webstaterator.webstaterator import Webstaterator
from webstaterator.cli import get_parser_options
from webstaterator.__main__ import *

EXPECTED_HELP_OUTPUT = """usage: webstaterator [-h] {validate,build,template} ...

A Python tool for generating static websites based on object models

optional arguments:
  -h, --help            show this help message and exit

Actions:
  Webstaterator actions

  {validate,build,template}
    validate            Validates the provided website description file
    build               Builds a website in the given folder based on the
                        provided website description file
    template            Generates a blank website description file
"""

def test_get_parser_returns_an_argument_parser():
    assert type(get_parser_options()) == argparse.ArgumentParser

def test_build_commands():
    pargs = get_parser_options().parse_args(
        ["build", "--website=test.json","--output=test/"]
    )

    assert pargs.action == "build"
    assert pargs.website == "test.json"
    assert pargs.output == "test/"

def test_validate_commands():
    pargs = get_parser_options().parse_args(
        ["validate", "--website=test.json"]
    )

    assert pargs.action == "validate"
    assert pargs.website == "test.json"

def test_template_commands():
    pargs = get_parser_options().parse_args(
        ["template", "--output=test/"]
    )

    assert pargs.action == "template"
    assert pargs.output == "test/"

def helper_cli_run_with_args(args, expected_output, capsys):
    run(args)
    out, err = capsys.readouterr()
    assert out == expected_output

def helper_cli_run_with_args_and_exit(args, expected_output, capsys):
    with pytest.raises(SystemExit):
        helper_cli_run_with_args(args, expected_output, capsys)

def test_cli_run_without_args(capsys):
    helper_cli_run_with_args_and_exit(
        [],
        EXPECTED_HELP_OUTPUT,
        capsys
    )

def test_cli_run_with_build(capsys,tmpdir):
    website_path = os.path.join(tmpdir, "test_website")
    ws_obj = Webstaterator()
    ws_obj.template(website_path)
    build_path = os.path.join(tmpdir,"build_output")
    website_json = os.path.join(website_path,"website.json")
    helper_cli_run_with_args(
        ["build", f"--output={build_path}", f"--website={website_json}"],
        """Building template
Built
Loading ...
copying assets
Building website
Built!
""",
        capsys
    )
