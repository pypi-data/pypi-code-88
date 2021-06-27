#!/bin/env python3
"""CLI API Subparsers
"""
import os, sys, argparse, glob, importlib, abc



class Subparser:

    @property
    @abc.abstractmethod
    def __args( self ):

        return NotImplemented


    @property
    @abc.abstractmethod
    def __kwargs( self ):

        return NotImplemented


    @abc.abstractmethod
    def __init__( self, parser ):

        assert( isinstance( parser, argparse.ArgumentParser ) )

        raise NotImplmentedError()


    def __call__( self ):

        return ( self.__args, self.__kwargs )



class NonTerminalSubparser( Subparser ):

    pass



class TerminalSubparser( Subparser ):


    @abc.abstractmethod
    def translate( self, args ):
        """translate a CLI request into an object model request data
        """

        return {}


    @abc.abstractmethod
    def callback( self, data ):
        """handle object model response data
        """

        print( NotImplemented )