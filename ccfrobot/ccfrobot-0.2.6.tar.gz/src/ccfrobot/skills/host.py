#!/bin/env python3
"""skill functions for hosting ccf objects
"""
def api( data ):
    """
    """

    frameworkPath = os.path.abspath( data[ 'framework' ][ 'path' ] )

    data[ 'framework' ][ 'checksum' ] = __hashDirectory( frameworkPath )

    return data