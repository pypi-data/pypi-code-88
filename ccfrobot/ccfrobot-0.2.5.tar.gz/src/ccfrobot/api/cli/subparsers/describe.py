#!/bin/env python3
"""generate a describe (checksum) of a CCF environment object


:: python

    python3 -m ccfrobot \
        -d ../../ccfref-test \
        -p az \
        -i cf \
        -v 1 \
        describe environment  \
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
    'help':        'describe a CCF {object} object describe',
    'description': """
Describe an entire CCF {object} as-code representation
"""
}



class Describe( subparsers.NonTerminalSubparser ):

    ARGS = [
        'describe'
    ]
    KWARGS = {
        'help':        TEMPLATE[ 'help' ].format( object = '' ),
        'description': TEMPLATE[ 'description' ].format( object = '' )
    }


    def __init__( self, parser ):

        assert( isinstance( parser, argparse.ArgumentParser ) )



class Environment( subparsers.TerminalSubparser ):

    ARGS = [
        'environment'
    ]
    KWARGS = {
        'help':        TEMPLATE[ 'help' ].format( object = 'environment' ),
        'description': TEMPLATE[ 'description' ].format( object = 'environment' )
    }


    def __init__( self, parser ):

        assert( isinstance( parser, argparse.ArgumentParser ) )

        parser.add_argument(
            'path',
            help='name of environment'
        )


    @staticmethod
    def translate( args ):

        return {
            'framework': {
                'path': args[ 'dir' ],
                'environments': [
                    {
                        'path': args[ 'path' ],
                    }
                ]
            }
        }


    def callback( kwargs ):

        pprint.pprint( kwargs[ 'framework' ] )



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
            help='name of automation or absolute path to automation file'
        )


    @staticmethod
    def translate( args ):

        return {
            'framework': {
                'path': args[ 'dir' ],
                'automations': [
                    {
                        'path': args[ 'path' ],
                    }
                ]
            }
        }


    def callback( kwargs ):

        pprint.pprint( kwargs[ 'framework' ]['automations'] )
