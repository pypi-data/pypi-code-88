#!/bin/env python3
"""generate a hash (checksum) of a CCF framework object

"""
import argparse, pprint

import sys, os

parentPath = os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..' ) )
sys.path.insert( 1, parentPath )
import subparsers



TEMPLATE = {
    'help':        'execute a CCF {object} object',
    'description': """
Execute a CCF {object} as-code representation
"""
}



class Execute( subparsers.NonTerminalSubparser ):

    ARGS = [
        'execute'
    ]
    KWARGS = {
        'help':        TEMPLATE[ 'help' ].format( object = '' ),
        'description': TEMPLATE[ 'description' ].format( object = '' )
    }


    def __init__( self, parser ):

        assert( isinstance( parser, argparse.ArgumentParser ) )



class Automation( subparsers.TerminalSubparser ):

    ARGS = [
        'automation'
    ]
    KWARGS = {
        'help':        TEMPLATE[ 'help' ].format( object = 'automation' ),
        'description': TEMPLATE[ 'description' ].format( object = 'automation' )
    }


    def __init__( self, parser ):

        assert( isinstance( parser, argparse.ArgumentParser ) )

        parser.add_argument(
            'path',
            help='path to a CCF automation as-code representation (file in yaml, or json format).',
        )


    @staticmethod
    def translate( args ):

        return {
            'framework': {
                'path': args[ 'dir' ],
                'automations': [
                    {
                        'path': args[ 'path' ]
                    }
                ]
            }
        }


    def callback( kwargs ):

        pass
