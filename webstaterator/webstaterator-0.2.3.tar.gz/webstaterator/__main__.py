"""
Webstaterator

A Python tool for generating static websites based on object models

Documentation: https://gitlab.com/Jon.Keatley.Folio/webstaterator
Gitlab: https://gitlab.com/Jon.Keatley.Folio/webstaterator
PyPi: https://pypi.org/project/webstaterator/

Created by Jon Keatley (http://jon-keatley.com)
Named by Sasha Siegel. It is her fault!

Copyright Jon Keatley 2021

"""

import sys

from webstaterator.cli import get_parser_options
from webstaterator.webstaterator import Webstaterator


def run(args):
    """ Execute webstaterators CLI """
    pargs = get_parser_options().parse_args(args)

    if pargs.action is None:
        get_parser_options().parse_args(["-h"])
        sys.exit(0)

    ws_obj = Webstaterator()

    if pargs.action == 'validate':
        ws_obj.validate(pargs.website)
    elif pargs.action == 'build':
        ws_obj.build(pargs.website, pargs.output)
    elif pargs.action == 'template':
        ws_obj.template(pargs.output)

def execute():
    """ wrapper method that calls run with sys.argv[1:] """
    run(sys.argv[1:])

if __name__ == '__main__':
    execute()
