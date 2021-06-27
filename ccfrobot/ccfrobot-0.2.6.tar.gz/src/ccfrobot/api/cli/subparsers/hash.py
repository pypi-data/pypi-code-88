#!/bin/env python3
"""generate a hash (checksum) of a CCF framework object

"""
import argparse, pprint

import sys, os

parentPath = os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..' ) )
sys.path.insert( 1, parentPath )
import subparsers



TEMPLATE = {
    'help':        'generate a CCF {object} object hash',
    'description': """
Create SHA512 checksum of an entire CCF {object} as-code representation
"""
}



class Hash( subparsers.NonTerminalSubparser ):

    ARGS = [
        'hash'
    ]
    KWARGS = {
        'help':        TEMPLATE[ 'help' ].format( object = '' ),
        'description': TEMPLATE[ 'description' ].format( object = '' )
    }


    def __init__( self, parser ):

        assert( isinstance( parser, argparse.ArgumentParser ) )



class Framework( subparsers.TerminalSubparser ):

    ARGS = [
        'framework'
    ]
    KWARGS = {
        'help':        TEMPLATE[ 'help' ].format( object = 'framework' ),
        'description': TEMPLATE[ 'description' ].format( object = 'framework' )
    }


    def __init__( self, parser ):

        assert( isinstance( parser, argparse.ArgumentParser ) )

        #parser.add_argument()


    @staticmethod
    def translate( args ):

        return {
            'framework': {
                'path': args[ 'dir' ]
            }
        }


    def callback( kwargs ):

        print( kwargs[ 'framework' ][ 'checksum' ] )
