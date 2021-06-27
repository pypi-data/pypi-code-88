#!/bin/env python3
"""generate a list (checksum) of a CCF environment object

"""
import argparse, pprint

import sys, os

parentPath = os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..' ) )
sys.path.insert( 1, parentPath )
import subparsers



TEMPLATE = {
    'help':        'generate a CCF {object} object list',
    'description': """
Create SHA512 checksum of an entire CCF {object} as-code representation
"""
}



class List( subparsers.NonTerminalSubparser ):

    ARGS = [
        'list'
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


    @staticmethod
    def translate( args ):

        return {
            'framework': {
                'path': args[ 'dir' ]
            }
        }


    def callback( kwargs ):

        pprint.pprint( kwargs[ 'framework' ][ 'environments'] )