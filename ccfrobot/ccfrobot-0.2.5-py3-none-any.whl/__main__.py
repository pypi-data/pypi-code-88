#!/usr/bin/env python3
"""ccfrobot main scope module (CLI)

ccfrobot running in the main scope by executing the module as a script via 
`python3 -m ccfrobot`. This provides a shell CLI. For more information on 
available commands, execute `python3 -m ccfrobot --help`, or consider the 
ccfrobot.api.cli documentation.

.. Rubric:: CLI

.. argparse::
    :module: ccfrobot.api.cli
    :func: __getDefaultArgparseParser
"""



def __callback( data ):
    """handle a CCF request object model

    :param data: ccf request object model
    :type data: dict

    :rtype: dict
    """

    request = ccfrobot.load( data )

    response = ccfrobot.handle( request )

    return response



if __name__ == '__main__':

    import sys, os

    # path to import itself (package) as a module (__init__)
    # also, we are tidy people let's keep index 0 clean.
    sys.path.insert( 1, os.path.abspath( os.path.join( __file__, '..' ) ) )

    import ccfrobot
    import ccfrobot.api.cli

    parser, subparserGroups = ccfrobot.api.cli.getDefaultParser()

    ccfrobot.api.cli.handle( parser, subparserGroups, __callback )
