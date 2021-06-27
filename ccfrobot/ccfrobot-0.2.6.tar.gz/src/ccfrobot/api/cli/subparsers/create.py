#!/bin/env python3
"""generate a create (checksum) of a CCF entrypoint object


:: python

    python3 -m ccfrobot \
        -d ../../ccfref-test \
        -p az \
        -i cf \
        -v 1 \
        create entrypoint  \
        --with-name "customer" \
        --inside-of "environments/sample-environment" \
        --referencing "resource-groups/sample-resource-group" \
        --with-parameter "test:value1"
"""
import argparse, pprint

import sys, os

parentPath = os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..' ) )
sys.path.insert( 1, parentPath )
import subparsers



TEMPLATE = {
    'help':        'create a CCF {object} object create',
    'description': """
Create an entire CCF {object} as-code representation
"""
}



class Create( subparsers.NonTerminalSubparser ):

    ARGS = [
        'create'
    ]
    KWARGS = {
        'help':        TEMPLATE[ 'help' ].format( object = '' ),
        'description': TEMPLATE[ 'description' ].format( object = '' )
    }


    def __init__( self, parser ):

        assert( isinstance( parser, argparse.ArgumentParser ) )



class Entrypoint( subparsers.TerminalSubparser ):

    ARGS = [
        'entrypoint'
    ]
    KWARGS = {
        'help':        TEMPLATE[ 'help' ].format( object = 'entrypoint' ),
        'description': TEMPLATE[ 'description' ].format( object = 'entrypoint' )
    }


    def __init__( self, parser ):

        assert( isinstance( parser, argparse.ArgumentParser ) )

        parser.add_argument(
            '-n', '--with-name',
            help='name of entrypoint',
            required=True
        )

        parser.add_argument(
            '--inside-of',
            help='path to object containing entrypoints (e.g. environments )',
            required=True
        )

        parser.add_argument(
            '-r', '--referencing',
            help='path to an object acting as a reference.',
            required=True
        )

        parser.add_argument(
            '-p', '--with-parameter',
            help='path to an object acting as a reference.',
            nargs='*'
        )


    @staticmethod
    def translate( args ):

        parameters = {}

        for parameter in args[ 'with_parameter' ]:

            key, value = tuple( parameter.split( ':', 2 ) )

            parameters[ key ] = value

        return {
            'framework': {
                'path': args[ 'dir' ],
                'entrypoints': [
                    {
                        'name': args[ 'with_name' ],
                        'path': args[ 'inside_of' ],
                        'reference': {
                            'path': args[ 'referencing' ],
                            'parameters': parameters
                        }
                    }
                ]
            }
        }


    def callback( kwargs ):

        pprint.pprint( kwargs[ 'framework' ] )
