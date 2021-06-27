#!/bin/env python3
"""skill functions for hashing ccf objects
"""
import  os, traceback, yaml


class Exception(BaseException):
    
    pass



class __CfSubYamlTag( yaml.YAMLObject ):

    yaml_tag = u'!Sub'


    def __init__(self, env_var):

        self.env_var = env_var


    def __repr__(self):

        return self.env_var


    @classmethod
    def from_yaml( cls, loader, node ):

        return globals()[ '__CfSubYamlTag' ]( node.value )



class SafeLoaderIgnoreUnknown(yaml.SafeLoader):

    def ignore_unknown(self, node):

        return None 

SafeLoaderIgnoreUnknown.add_constructor( None, SafeLoaderIgnoreUnknown.ignore_unknown )

SafeLoaderIgnoreUnknown.add_constructor( '!Sub', __CfSubYamlTag.from_yaml )



def __describeCf( data, absdirpath, objectsType ):

    env = {}

    try:

        with open( os.path.join( absdirpath, 'main.cf.aws.yml' ), 'r' ) as fh:

            env = yaml.load( fh, Loader=SafeLoaderIgnoreUnknown )

    except FileNotFoundError:

        print( traceback.format_exc() )

        import json

        with open( os.path.join( absdirpath, 'main.cf.aws.json' ), 'r' ) as fh:

            env = json.loads( fh.read() )

    if 'Parameters' in env.keys():

        data[ 'framework'][ 'environments' ][ 0 ][ 'parameters' ] = env[ 'Parameters' ]

    if 'Resources' in env.keys():

        for key in env[ 'Resources' ].keys() :

            if env[ 'Resources' ][ key ][ 'Type' ] == 'AWS::CloudFormation::Stack':

                templateUrl = env[ 'Resources' ][ key ][ 'Properties' ][ 'TemplateURL' ]

                entrypoint = {
                    'path' : data[ 'framework' ][ objectsType ][ 0 ][ 'path' ],
                    'name': key,
                    'reference': {
                        'path': templateUrl,
                        'parameters': env[ 'Resources' ][ key ][ 'Properties' ][ 'Parameters' ]
                    }
                }

                data[ 'framework' ][ 'entrypoints' ].insert( 0, entrypoint )

    return data



def __defaultDescribeMethodMap():

    return {
        'cf': __describeCf
    }



def environment( data ):
    """
    """

    fwpath = data[ 'framework'][ 'path' ]

    path = data[ 'framework'][ 'environments' ][ 0 ][ 'path' ]

    absdirpath = os.path.abspath( os.path.join( fwpath, path ) )

    func = __defaultDescribeMethodMap()[ data[ 'context' ][ 'interface' ] ]

    return func( data, absdirpath, 'environments' )



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

    data[ 'framework' ][ 'automations' ][ 0 ] = env
    data[ 'framework' ][ 'automations' ][ 0 ][ 'path' ] = epath

    return data