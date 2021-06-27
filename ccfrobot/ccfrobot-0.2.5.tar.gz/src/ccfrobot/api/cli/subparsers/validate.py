#!/bin/env python3
"""generate a validate (checksum) of a CCF environment object

"""
import argparse, pprint

import sys, os

parentPath = os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..' ) )
sys.path.insert( 1, parentPath )
import subparsers



TEMPLATE = {
    'help':        'generate a CCF {object} object validate',
    'description': """
Create SHA512 checksum of an entire CCF {object} as-code representation
"""
}



class Validate( subparsers.NonTerminalSubparser ):

    ARGS = [
        'validate'
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

        print( kwargs[ 'framework' ] )



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
                        'path': args[ 'path' ]
                    }
                ]
                
            }
        }


    def callback( kwargs ):

        print( kwargs[ 'framework' ][ 'environments'][ 0 ] )





class Automation( subparsers.TerminalSubparser ):

    ARGS = [
        'automation'
    ]
    KWARGS = {
        'help':        TEMPLATE[ 'help' ].format( object = 'environment' ),
        'description': TEMPLATE[ 'description' ].format( object = 'environment' )
    }


    def __init__( self, parser ):

        assert( isinstance( parser, argparse.ArgumentParser ) )

        parser.add_argument(
            'path',
            help='relative path to automation (may be a path to a directory, or a file)'
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

        print( kwargs[ 'framework' ][ 'automations'][ 0 ] )
