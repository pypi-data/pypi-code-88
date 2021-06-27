#!/bin/env python3
"""skill functions for hosting ccf objects
"""
import os

class Exception( BaseException ):

    pass

def framework( data ):
    """
    """

    frameworkPath = os.path.abspath( data[ 'framework' ][ 'path' ] )

    if os.path.isdir( frameworkPath ) and os.path.exists( frameworkPath ):

        contents = os.listdir( frameworkPath )

        if '.ccf' in contents:

            raise Exception('not an empty directory.')

    for x in [
        'environments',
        'automations',
        'resource-groups',
        '.ccf'
    ]:
        path = os.path.join( frameworkPath, x )

        print( 'mkdirs: %s' % ( path ) )

        os.makedirs( path ) 

    if data[ 'context' ][ 'interface' ] == 'tf':

        open( os.path.join( frameworkPath, 'main.tf' ), 'w' ).close()
        open( os.path.join( frameworkPath, 'outputs.tf' ), 'w' ).close()
        open( os.path.join( frameworkPath, 'variables.tf' ), 'w' ).close()

    if data[ 'context' ][ 'interface' ] == 'cf':

        open( os.path.join( frameworkPath, 'main.cf.aws.yaml' ), 'w' ).close()

    return data



def entrypoint( data ):

    return data



def resourceGroup( data ):

    return data