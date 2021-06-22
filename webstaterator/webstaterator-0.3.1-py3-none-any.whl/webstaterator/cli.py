"""
Module for command line interface features
"""

import argparse

DESCRIPTION = """A Python tool for generating static websites based on object models"""


def get_parser_options():
    """ Generate CLI options """
    parser = argparse.ArgumentParser(
        prog='webstaterator',
        description=DESCRIPTION
    )

    arg_website_short = '-w'
    arg_website_long = '--website'
    arg_website_desc = 'Website decription file'

    arg_output_short = '-o'
    arg_output_long = '--output'
    arg_output_desc = 'Output path'

    action_parser = parser.add_subparsers(
        title='Actions',
        description='Webstaterator actions',
        dest='action'
    )
    action_validate = action_parser.add_parser(
        'validate',
        help='Validates the provided website description file'
    )
    action_validate.add_argument(
        arg_website_short,
        arg_website_long,
        help=arg_website_desc,
        required = True
    )

    action_build = action_parser.add_parser(
        'build',
        help="""Builds a website in the given folder based
on the provided website description file"""
        )
    action_build.add_argument(
        arg_website_short,
        arg_website_long,
        help=arg_website_desc,
        required = True,
    )
    action_build.add_argument(
        arg_output_short,
        arg_output_long,
        help=arg_output_desc,
        required = True,
    )

    action_template = action_parser.add_parser(
        'template',
        help='Generates a blank website description file'
    )

    action_template.add_argument(
        arg_output_short,
        arg_output_long,
        help=arg_output_desc,
        required = True,
    )

    return parser
