#!/bin/env python3
"""CLI API facilities
"""
import os, sys, argparse
from . import subparsers



class TemporaryImportPath():
    """context manager class for temporarily extending $PATH

        with TemporaryImportPath( path ):

            mod = importlib.import_module( name )
    """

    def __init__( self, path ):

        self.path = path

    def __enter__( self ):

        sys.path.insert( 0, self.path )

    def __exit__( self, xType, xVal, xTraceback ):

        try:

            sys.path.remove( self.path )
        except ValueError:

            pass



class Exception( BaseException ):
    """api.cli base exception class
    """

    pass



def __getDefaultTopParser():
    """Generate a default ccfrobot :class:`argparse.ArgumentParser`, with only
    top parser.

    :rtype: argparse.ArgumentParser
    """

    importPath = os.path.abspath( os.path.join( __file__, '..', '..', '..' ) )

    with TemporaryImportPath( importPath ):

        import ccfrobot

    parser = argparse.ArgumentParser( 'ccfrobot', description="""
    Cloud Code Framework Robot

    The ccfrobot (Cloud Code Framework Robot) is a programmable automaton for 
    automating creative tasks that occur when working with the [Cloud Code 
    Framework (CCF)](). It implements all CCF models, as well as skills, that 
    are not destructive. In addition, it offers a CLI, as well as HTTP-REST 
    APIs.

    This is the CLI API.
    """ )

    parser.add_argument(
        '-d', '--dir',
        help='use paths relative to current working directory for path outputs',
        default='.',
    )

    parser.add_argument(
        '-p', '--platform',
        help='use paths relative to current working directory for path outputs',
        choices = ccfrobot.Context.PLATFORMS,
        required = True
    )

    parser.add_argument(
        '-i', '--interface',
        help='use paths relative to current working directory for path outputs',
        choices = ccfrobot.Context.INTERFACES
    )

    parser.add_argument(
        '-v', '--version',
        help='use paths relative to current working directory for path outputs',
        default = '1',
        choices = ccfrobot.Context.VERSIONS
    )

    return parser



def getDefaultParser():
    """Generate a default ccfrobot :class:`argparse.ArgumentParser` with command
    (predicate), and sub-command (object) parsers.

    This will return a tuple, with the second item being a map of subparsers 
    (groups).

    Both values are required for :meth:`handle`.

    :rtype: tuple( argparse.ArgumentParser, dict)
    """

    dirpath = os.path.abspath( os.path.join( os.path.dirname(__file__), 'subparsers' ) )

    parser = __getDefaultTopParser()

    groups = __upgradeParserRecursive( parser, dirpath )

    return parser, groups



def __getDefaultArgparseParser():
    """Generate a default ccfrobot :class:`argparse.ArgumentParser` with command
    (predicate), and sub-command (object) parsers.

    :rtype: argparse.ArgumentParser
    """

    parser, groups = getDefaultParser()

    return parser



def __getSubparsers( modname ):
    """get all `api.cli.subparsers.Subparser` classes within a module

    returns a tuple ( dict( terminals ), dict( nonTerminals ) ).

    :param modname: the name of the module to inspect
    :type modname: str

    :rtype: tuple( dict, dict )
    """

    import importlib, inspect

    module = importlib.import_module( modname )

    modmembers = dict( inspect.getmembers( module ) )

    nonTerminalName = None
    terminals = {}

    for key in modmembers.keys():

        if ( hasattr( modmembers[ key ], '__name__' ) and
             modmembers[ key ].__name__ == __makeGroupName( modname )
        ):

            nonTerminalName = key

            continue

        if (hasattr( modmembers[ key ], 'translate' ) and
           hasattr( modmembers[ key ], 'callback' )):

            terminals[ key ] = modmembers[ key ]

    if nonTerminalName is None: raise Exception( f"""
    in module ``{modname}`,` either none, or more than one 
    `api.cli.subparsers.NonTerminalSubparser` classes defined.
    """ )

    if len( terminals ) == 0: raise Exception( f"""
    in module ``{modname}`,` no `api.cli.subparsers.TerminalSubparser` classes 
    defined, requires at least 1.
    """ )

    return (
        {
            nonTerminalName: modmembers[ nonTerminalName ] 
        },
        terminals
    )


def __makeGroupName( text ):

    return text.capitalize()



def __getSubparserGroup( fpath ):
    """get all subparsers of a subparser group (module)

    returns a tuple ( str( groupname ), tuple( terminals, nonTerminals ) )

    :param fpath: path of subparser group module
    :type fpath: str

    :rtype: tuple( str, tuple )
    """

    groupname = '.'.join( os.path.basename( fpath ).split( '.' )[ :-1 ] )

    with TemporaryImportPath( os.path.dirname( fpath ) ):

        return __makeGroupName( groupname ), __getSubparsers( groupname )



def __getSubparserGroups( dirpath ):
    """get all subparser groups within a package directory

    :param dirpath: path of python package directory
    :type dirpath: str

    :rtype: dict
    """

    import glob

    groups = {}

    modules = [ fn for fn in glob.glob( f'{dirpath}/*.py' ) if (
        not os.path.basename( fn ).startswith( '__init__' ) and
        not os.path.basename( fn ).startswith( '__main__' ) 
    )]

    for modulePath in modules:

        groupname, group = __getSubparserGroup( modulePath )

        groups[ groupname ] = group

    return groups



def __upgradeParser( parser, obj ):
    """add a predicate-object api.cli.subparsers.Subparser` to an 
    `argparse.ArgumentParser`.

    ;param parser:
    :type parser: argparse.ArgumentParser

    :param obj: the module containing 
    :type obj: object

    :rtype: argparse.ArgumentParser
    """

    subparser = parser.add_parser( *obj.ARGS, **obj.KWARGS )

    obj( subparser )

    return subparser



def __upgradeParserRecursive( parser, dirpath ):
    """add a predicate-objects api.cli.subparsers.Subparser` to an 
    `argparse.ArgumentParser`.

    ;param parser:
    :type parser: argparse.ArgumentParser

    :param dirpath: the module containing 
    :type dirpath: str
    """

    assert( isinstance( parser, argparse.ArgumentParser ) )
    assert( isinstance( dirpath, str ) )

    groups = __getSubparserGroups( dirpath )

    pps = parser.add_subparsers( dest='predicate', required=True )

    for group in groups.items():

        nonterminalName = list(group[ 1 ][ 0 ].keys() )[ 0 ]

        nonterminal = group[ 1 ][ 0 ][ nonterminalName ]

        subparser = __upgradeParser( pps, nonterminal )

        ops = subparser.add_subparsers( dest='object', required=True )

        for terminal in group[ 1 ][ 1 ]:

            __upgradeParser( ops, group[ 1 ][ 1 ][ terminal ] )

    return groups



def __uniqueTypeInDictValues( haystack, needle ):
    """get the matching key of a dict value, whose type only occurs once within
    the entire dictionary.

    :param needle:
    :type needle: object

    :param haystack:
    :type haystack: dict
    """
    assert( isinstance( haystack, dict ) )
    assert( isinstance( needle, object ) )

    stor = None

    for key in haystack.keys():

        print( haystack[ key ].__class__ )

        if (isinstance( haystack[ key ], object ) and
           issubclass( haystack[ key ].__class__, needle )):


            if ( stor != None ): return None

            stor = key

    return stor



def __filterTypeFromDictValue( haystack, needle ):
    """retain only dict items with values of a certain type

    :param needle: 
    :type needle: object

    :param haystack:
    :type haystack: dict
    """
    assert( isinstance( haystack, dict ) )
    assert( isinstance( needle, object ) )

    result = {}

    for key in haystack.keys():

        if isinstance( haystack[ key ], needle ) == False : continue

        result[ key ] = haystack[ key ]

    return result



def handle( parser, groups, callback ):
    """
    """

    assert( isinstance( parser, argparse.ArgumentParser ) )

    args = vars( parser.parse_args( sys.argv[ 1: ] ) )

    predicatename = __makeGroupName( args[ 'predicate' ] )
    objectname    = __makeGroupName( args[ 'object' ] )

    obj = groups[ predicatename ][ 1 ][ objectname ]

    request = obj.translate( args )

    if 'framework' not in request.keys():

        request[ 'framework' ] = {}

        if 'path' not in request[ 'framework' ]:

            request[ 'framework' ][ 'path' ] = args[ 'path' ]

    request[ 'robot' ] = {
        'skill': '.'.join( [ args[ 'predicate' ], args[ 'object' ] ] )
    }

    request[ 'context' ] = {
        'platform':  args[ 'platform' ],
        'interface': args[ 'interface' ],
        'version':   args[ 'version' ]
    }

    response = callback( request )

    return obj.callback( response )