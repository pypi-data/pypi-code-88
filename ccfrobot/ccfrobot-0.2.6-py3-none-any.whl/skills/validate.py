#!/bin/env python3
"""skill functions for hashing ccf objects
"""
import  os, yaml, glob, traceback, warnings


class Exception(BaseException):
    
    pass



class SafeLoaderIgnoreUnknown( yaml.SafeLoader ):

    def ignore_unknown( self, node ):

        return None 



SafeLoaderIgnoreUnknown.add_constructor(
    None,
    SafeLoaderIgnoreUnknown.ignore_unknown
)



def __validateArm( data, absdirpath, *args ):
    """validate a Microsoft Azure Resource Manager CCF object
    """

    assert data[ 'context' ][ 'interface' ] == 'arm'

    import json

    with open( os.path.join( absdirpath, 'azuredeploy.json' ), 'r' ) as fh:

        env = json.loads( fh.read() )

    if 'parameters' in env.keys():

        assert isinstance( env[ 'parameters' ], dict )

    try:

        with open( os.path.join( absdirpath, 'parameters.azuredeploy.json' ), 'r' ) as fh:

            env = json.loads( fh.read() )

            assert isinstance( env, dict )

    except:

        warnings.warn( traceback.format_exc() )



def __validateCf( data, absdirpath, name = 'main' ):
    """validate an AWS Cloudformation CCF object
    """

    assert data[ 'context' ][ 'interface' ] == 'cf'

    try:

        with open( os.path.join( absdirpath, f'{name}.cf.aws.yml' ), 'r' ) as fh:

            env = yaml.load( fh, Loader = SafeLoaderIgnoreUnknown )

    except:

        warnings.warn( traceback.format_exc() )

        import json

        with open( os.path.join( absdirpath, 'main.cf.aws.json' ), 'r' ) as fh:

            env = json.loads( fh.read() )

    if 'Parameters' in env.keys():

        assert isinstance( env[ 'Parameters' ], dict )



def __validateTf( data, absdirpath, *args ):
    """validate a Terraform CCF object
    """

    assert data[ 'context' ][ 'interface' ] == 'tf'

    import hcl

    found = False

    for path in glob.glob( os.path.join( absdirpath, '*.tf' ) ):

        if not os.path.isfile( os.path.join( absdirpath, path ) ): continue

        try:

            with open( os.path.join( absdirpath, path ), 'r' ) as fh:

                env = hcl.load( fh )

                found = True

                break

        except ValueError as e:

            warnings.warn( traceback.format_exc() )

    if not found:

        raise FileNotFoundError( ( os.path.join( absdirpath, '*.tf' ) ) )



def __validateCdm( data, absdirpath, name = 'main' ):
    """validate a Google Cloud Deployment Manager CCF object
    """

    assert data[ 'context' ][ 'interface' ] == 'cdm'

    with open( os.path.join( absdirpath, f'{name}.cdm.gcloud.yml' ), 'r' ) as fh:

        env = yaml.load( fh, Loader = SafeLoaderIgnoreUnknown )



def __defaultValidateMethodMap():

    return {
        'cf': __validateCf,
        'tf': __validateTf,
        'arm': __validateArm,
        'cdm': __validateCdm
    }



def environment( data ):

    fpath = data[ 'framework' ][ 'path' ]
    epath = data[ 'framework' ][ 'environments' ][ 0 ][ 'path' ]

    absdirpath = os.path.abspath( os.path.join( fpath, epath ) )

    assert os.path.isdir( absdirpath ), absdirpath

    func = __defaultValidateMethodMap()[ data[ 'context' ][ 'interface' ] ]

    func( data, absdirpath )

    return data



def resourceGroup( data ):

    fpath = data[ 'framework' ][ 'path' ]
    epath = data[ 'framework' ][ 'resource-groups' ][ 0 ][ 'path' ]

    absdirpath = os.path.abspath( os.path.join( fpath, epath ) )

    assert os.path.isdir( absdirpath ), absdirpath

    func = __defaultValidateMethodMap()[ data[ 'context' ][ 'interface' ] ]

    func( data, absdirpath )

    return data



def framework( data ):
    """
    """

    fpath = data[ 'framework' ][ 'path' ]
    epath = '.ccf'

    absdirpath = os.path.abspath( fpath )

    absdirpaths = [
        os.path.join( absdirpath, path )
        for path in [
            '.ccf',
            'environments',
            'automations',
            'resource-groups'
        ]
    ]

    assert os.path.isdir( absdirpaths[ 0 ] ), absdirpaths[ 0 ]
    assert os.path.isdir( absdirpaths[ 1 ] ), absdirpaths[ 1 ]
    assert os.path.isdir( absdirpaths[ 2 ] ), absdirpaths[ 2 ]
    assert os.path.isdir( absdirpaths[ 3 ] ), absdirpaths[ 3 ]

    func = __defaultValidateMethodMap()[ data[ 'context' ][ 'interface' ] ]
    func( data, absdirpaths[ 0 ] )

    return data



def automation( data ):

    fpath = data[ 'framework' ][ 'path' ]
    epath = data[ 'framework' ][ 'automations' ][ 0 ][ 'path' ]

    abspath = os.path.abspath( os.path.join( fpath, 'automations', epath ) )

    if os.path.isdir( abspath ):

        platform = data[ 'context' ][ 'platform' ]

        with open( os.path.join( abspath, f'main.{platform}.yml' ), 'r' ) as fh:

            env = yaml.load( fh, Loader = SafeLoaderIgnoreUnknown )

    else:

        with open( os.path.join( abspath ), 'r' ):

            env = yaml.load( fh, Loader = SafeLoaderIgnoreUnknown )

    return data