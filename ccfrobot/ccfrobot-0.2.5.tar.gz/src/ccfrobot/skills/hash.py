#!/bin/env python3
"""skill functions for hashing ccf objects
"""
import hashlib, os

def __hashDirectory( directory ):

    SHAhash = hashlib.md5()

    if not os.path.exists ( directory ):

        return -1

    try:
        for root, dirs, files in os.walk( directory ):

            for names in files:

                filepath = os.path.join(root,names)

                try:

                    f1 = open(filepath, 'rb')

                except:
                    # You can't open the file for some reason
                    f1.close()
                    continue

                while 1:
                    # Read file in as little chunks
                    buf = f1.read( 4096 )

                    if not buf : break

                    SHAhash.update( hashlib.md5( buf ).digest() )

                f1.close()

    except:
        import traceback
        # Print the stack traceback
        traceback.print_exc()
        return -2

    return SHAhash.hexdigest()



def __hashString( inp ):

    m = hashlib.sha512()

    m.update( inp )

    return m.hexdigest()[ :15 ]



def framework( data ):
    """
    """

    frameworkPath = os.path.abspath( data[ 'framework' ][ 'path' ] )

    data[ 'framework' ][ 'checksum' ] = __hashDirectory( frameworkPath )

    return data