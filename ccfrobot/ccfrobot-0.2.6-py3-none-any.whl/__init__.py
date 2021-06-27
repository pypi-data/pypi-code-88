#!/usr/bin/env python3
"""ccfrobot module
====================================

.. uml::

    abstract CcfObject {
        +{abstract} void    __init__( **kwargs )
        +{abstract} object  load( data )
        +{abstract} dict    dump( self )
    }

    class Interface {
        +str framework
        +str context
        +str robot
        +void   __init__( **kwargs )
        +object load( data )
        +dict   dump( self )
    }

    class Framework {
        +str  path           
        +str  checksum       
        +list entrypoints    
        +list environments   
        +list resource_groups
        +list automations    

        +void __init__( **kwargs )
        +object load( data )
        +dict dump( self )
        +{abstract}{static} void   create( self )
        +{abstract} void   eval( self )
    }

    class Context {
        +{static} list PLATFORMS
        +{static} list INTERFACES
        +{static} list VERSIONS
        +str platform
        +str interface
        +str version

        +void __init__( **kwargs )
        +object load( data )
        +dict dump( self )
        +{abstract}{static} void   create( self )
        +{abstract} void   eval( self )
    }

    class Robot {
        +str skill
        +str status
        +str status_message

        +void __init__( **kwargs )
        +object load( data )
        +dict dump( self )
        +object work( self, interface )
    }

    class Entrypoint {
        +{static} list BASENAMETAILS
        +str path
        +str name
        +str checksum
        +object reference

        +void __init__( **kwargs )
        +object load( data )
        +dict dump( self )
        +object create( path, name, reference )
        +object eval( path, name, reference)
    }

    class Reference {
        +str path
        +str checksum
        +str parameters
        +object reference

        +void __init__( **kwargs )
        +object load( data )
        +dict dump( self )
    }

    class Environment {
        +{static}list PATHPREFIXES
        +str path
        +str checksum

        +void __init__( **kwargs )
        +object load( data )
        +dict dump( self )
        +{abstract}void create( path, platform, interface, instance = None )
        +{abstract}void eval( path, platform, interface, instance = None )
    }

    class ResourceGroup {
        +{static}list PATHPREFIXES
        +str path
        +str checksum

        +void __init__( **kwargs )
        +object load( data )
        +dict dump( self )
        +{abstract}void create( path, platform, interface, instance = None )
        +{abstract}void eval( path, platform, interface, instance = None )
    }

    class Automation {
        +{static}list PATHPREFIXES
        +str path
        +str checksum

        +void __init__( **kwargs )
        +object load( data )
        +dict dump( self )
        +{abstract}void create( path, platform, interface, instance = None )
        +{abstract}void eval( path, platform, interface, instance = None )
    }

    class AutomationStep {
        +{static}list PATHPREFIXES
        +str path
        +str checksum

        +void __init__( **kwargs )
        +object load( data )
        +dict dump( self )
        +{abstract}void create( path, platform, interface, instance = None )
        +{abstract}void eval( path, platform, interface, instance = None )
    }

    CcfObject --|> Interface : "parent of"

    CcfObject --|> Framework : "parent of"

    CcfObject --|> Context : "parent of"

    CcfObject --|> Entrypoint : "parent of"

    Entrypoint ---> Reference : "depends on"

    CcfObject --|> Robot : "parent of"

    CcfObject --|> Reference : "parent of"

    CcfObject --|> Environment : "parent of"

    CcfObject --|> ResourceGroup : "parent of"
"""
import os, abc, importlib, warnings, sys, glob, traceback


class Exception( BaseException ):

    pass



def load( data ):
    """translate dict into ccf interface object

    :param data: a python dictionary object with `json.dumps` passing a \
    `common.schema.json` validation
    :type inst: dict

    :rtype: ccfrobot.Interface
    """

    assert( isinstance( data, dict ) )

    return Interface.load( data )



def loads( data ):
    """translate json string into ccf interface object

    :param data: a python dictionary object with `json.dumps` passing a \
    `common.schema.json` validation
    :type inst: dict

    :rtype: ccfrobot.Interface
    """

    assert( isinstance( data, str ) )

    import json

    return load( json.loads( data ) )



def handle( interface ):

    assert( isinstance( interface, Interface ) )

    if interface.robot is None:

        warnings.warn( "`robot` not configured. Nothing to do.", UserWarning )

        return interface

    return interface.robot.work( interface )



def dump( interface ):
    """translate interface object into dict (same as `Interface.dump()`)

    :param inst: ccfrobot (request) instance object
    :type inst: ccfrobot.Interface

    :return: returns a dict object representing an instance
    :rtype: dict
    """

    assert( isinstance( interface, Interface ) )

    return interface.dump()



def dumps( interface ):
    """translate interface object into json string

    :return: json string
    :rtype: str
    """

    import json

    return json.dumps( interface.dump() )



def jsoneval( dictObj, schema = 'interface.ccf.schema.json' ):
    """evaluate a `dict` against a json interface schema 
    """

    import jsonschema
    pass



def strToCamelCase( text ):

    out = ''.join( word.capitalize() for word in text.split( '-' )  )

    return out



class CcfObject( abc.ABC ):
    """abstract class for ccf object implementations of ccfrobot

    .. uml::

        abstract CcfObject {
            +{abstract} void    __init__( **kwargs )
            +{abstract} object  load( data )
            +{abstract} dict    dump( self )
        }
    """

    @abc.abstractmethod
    def __init__( self, **kwargs ):
        """translate dict into object
        """

        return NotImplemented


    @staticmethod
    @abc.abstractmethod
    def load( data ):
        """translate dict into object
        """

        return NotImplemented


    @abc.abstractmethod
    def dump( self ):
        """translate object into dict
        """

        dump = NotImplemented

        return dump



class Interface( CcfObject ):
    """ccf Interface

    .. uml::

        class Interface {
            +str framework
            +str context
            +str robot
            +void   __init__( **kwargs )
            +object load( data )
            +dict   dump( self )
        }

    :param framework: ccfrobot Framework Object
    :type framework: ccfrobot.Framework

    :param context: ccfrobot Context Object
    :type context: ccfrobot.Context

    :param robot: ccfrobot Robot Object
    :type robot: ccfrobot.Robot, optional
    """
    framework = None
    context   = None
    robot     = None


    def __init__( self, **kwargs ):

        if len( kwargs ) == 0:

            self.framework = Framework()
            self.context   = Context()
            self.robot     = Robot()

            return

        assert( isinstance( kwargs[ 'framework' ], Framework ) )
        assert( isinstance( kwargs[ 'context' ], Context ) )

        self.framework = kwargs[ 'framework' ]
        self.context   = kwargs[ 'context' ]

        if ( 'robot' in kwargs.keys() and kwargs[ 'robot'] is not Interface.robot ):

            assert( isinstance( kwargs[ 'robot' ], Robot ) )

            self.robot     = kwargs[ 'robot' ]


    @staticmethod
    def load( data ):

        robot = Interface.robot
        if 'robot' in data.keys():

            robot = Robot.load( data[ 'robot' ] )

        return Interface(
            framework = Framework.load( data[ 'framework' ] ),
            context   = Context.load( data[ 'context' ] ),
            robot     = robot
        )


    def dump( self ):

        dump = {
            'framework': self.framework.dump(),
            'context': self.context.dump()
        }

        if self.robot is not Interface.robot:

            dump[ 'robot' ] = self.robot.dump()

        return dump


    def handle( self ):
        """handle a ccfrobot selfance as a request

        :param self: ccfrobot (request) selfance object
        :type self: ccfrobot.Interface

        :return: returns a new ccfrobot (response) selfance object
        :rtype: ccfrobot.Interface
        """

        return self.robot.work( self )



class Framework( CcfObject ):
    """ccf Framework

    .. uml::

        class Framework {
            +str  path           
            +str  checksum       
            +list entrypoints    
            +list environments   
            +list resource_groups
            +list automations    

            +void __init__( **kwargs )
            +object load( data )
            +dict dump( self )
            +{abstract}{static} void   create( self )
            +{abstract} void   eval( self )
        }

    :param path: directory path to ccf framework as-code representation
    :type path: str

    :param checksum: checksum of the ccf framework as-code representation
    :type checksum: str, optional

    :param entrypoints: list of :class:`ccfrobot.Entrypoint` objects
    :type entrypoints: list, optional

    :param environments: list of :class:`ccfrobot.Environment` objects
    :type environments: list, optional

    :param resource_groups: list of :class:`ccfrobot.ResourceGroup` objects
    :type resource_groups: list, optional

    :param automations: list of :class:`ccfrobot.Automation` objects
    :type automations: list, optional
    """
    path            = ''
    checksum        = ''
    entrypoints     = []
    environments    = []
    resource_groups = []
    automations     = []


    def __init__( self, **kwargs ):

        if len( kwargs ) == 0: return

        assert( isinstance( kwargs[ 'path' ], type( Framework.path ) ) )

        self.path = kwargs[ 'path' ]

        if 'checksum' in kwargs.keys():

            assert( isinstance( kwargs[ 'checksum' ], type( Framework.checksum ) ) )

            self.checksum = kwargs[ 'checksum' ]

        if 'entrypoints' in kwargs.keys():

            self.entrypoints = []

            obj = None
            for obj in kwargs[ 'entrypoints' ]:

                assert( isinstance( obj, Entrypoint ) )

                self.entrypoints.append( obj )

        if 'environments' in kwargs.keys():

            self.environments = []

            obj = None
            for obj in kwargs[ 'environments' ]:

                assert( isinstance( obj, Environment ) )

                self.environments.append( obj )

        if 'resource_groups' in kwargs.keys():

            self.resource_groups = []

            obj = None
            for obj in kwargs[ 'resource_groups' ]:

                assert( isinstance( obj, ResourceGroup ) )

                self.resource_groups.append( obj )

        if 'automations' in kwargs.keys():

            self.automations = []

            obj = None
            for obj in kwargs[ 'automations' ]:

                assert( isinstance( obj, Automation ) )

                self.automations.append( obj )


    @staticmethod
    def load( data ):

        checksum        = Framework.checksum
        entrypoints     = Framework.entrypoints
        environments    = Framework.environments
        resource_groups = Framework.resource_groups
        automations     = Framework.automations


        if 'checksum' in data.keys():

            checksum = data[ 'checksum' ]

        if 'entrypoints' in data.keys():

            entrypoints = []

            for _data in data[ 'entrypoints' ]:

                entrypoints.append( Entrypoint.load( _data ) )

        if 'resource-groups' in data.keys():

            resource_groups = []

            for _data in data[ 'resource-groups' ]:

                resource_groups.append( ResourceGroup.load( _data ) )

        if 'environments' in data.keys():

            environments = []

            for _data in data[ 'environments' ]:

                environments.append( Environment.load( _data ) )

        if 'automations' in data.keys():

            automations = []

            for _data in data[ 'automations' ]:

                automations.append( Automation.load( _data ) )

        return Framework( 
            path            = data[ 'path' ],
            checksum        = checksum,
            entrypoints     = entrypoints,
            environments    = environments,
            resource_groups = resource_groups,
            automations     = automations
         )


    def dump( self ):

        dump = {
            'path': self.path
        }

        if self.checksum is not Framework.checksum:

            dump[ 'checksum' ] = self.checksum

        if self.entrypoints is not Framework.entrypoints:

            dump[ 'entrypoints' ] = []

            for entrypoint in self.entrypoints:

                dump[ 'entrypoints' ].append( entrypoint.dump() )

        if self.environments is not Framework.environments:

            dump[ 'environments' ] = []

            for environment in self.environments:

                dump[ 'environments' ].append( environment.dump() )

        if self.resource_groups is not Framework.resource_groups:

            dump[ 'resource_groups' ] = []

            for resource_group in self.resource_groups:

                dump[ 'resource_groups' ].append( resource_group.dump() )

        if self.automations is not Framework.automations:

            dump[ 'automations' ] = []

            for automation in self.automations:

                dump[ 'automations' ].append( automation.dump() )

        return dump


    @staticmethod
    def hash( interface ):
        """
        """

        import skills.hash

        return skills.hash.framework( interface.dump() )


    @staticmethod
    def create( interface ):
        """
        """

        import skills.create

        return skills.create.framework( interface.dump() )


    @staticmethod
    def validate( interface ):
        """
        """

        import skills.validate

        return skills.validate.framework( interface.dump() )



class Context( CcfObject ):
    """ccf Context

    .. uml::

        class Context {
            +{static} list PLATFORMS
            +{static} list INTERFACES
            +{static} list VERSIONS
            +str platform
            +str interface
            +str version

            +void __init__( **kwargs )
            +object load( data )
            +dict dump( self )
            +{abstract}{static} void   create( self )
            +{abstract} void   eval( self )
        }

    :param PLATFORMS: list of available platforms (str)
    :type PLATFORMS: list

    :param INTERFACES: list of available platform interfaces (str)
    :type INTERFACES: list

    :param VERSIONS: list of available ccf versions (str)
    :type VERSIONS: list

    :param platform: abbreviated name of current platform, must be any of 
        (str) in `PLATFORMS`.
    :type platform: str

    :param interface: abbreviated name of current platform interface, must be 
        any of (str) in `INTERFACES`.
    :type interface: str

    :param version: version of ccf
    :type version: str
    """
    PLATFORMS       = [ 'az', 'aws', 'gcloud' ]
    INTERFACES      = [ 'tf', 'cf', 'arm', 'cdm' ]
    VERSIONS        = [ '1' ]
    platform        = ''
    interface       = ''
    version         = ''


    def __init__( self, **kwargs ):

        if len( kwargs ) == 0: return

        assert( kwargs[ 'interface' ] in self.INTERFACES )
        assert( kwargs[ 'platform' ] in self.PLATFORMS )
        assert( kwargs[ 'version' ] in self.VERSIONS )

        self.interface = kwargs[ 'interface' ]
        self.platform  = kwargs[ 'platform' ]
        self.version   = kwargs[ 'version' ]


    @staticmethod
    def load( data ):

        return Context( 
            interface = data[ 'interface' ],
            platform  = data[ 'platform' ],
            version   = data[ 'version' ]
        )


    def dump( self, reduce=False ):

        return {
            'platform':   self.platform,
            'interface':  self.interface,
            'version':    self.version,
            'INTERFACES': self.INTERFACES,
            'PLATFORMS':  self.PLATFORMS,
            'VERSIONS':   self.VERSIONS
        }



class Robot( CcfObject ):
    """ccf Robot

    .. uml::

        class Robot {
            +str skill
            +str status
            +str status_message

            +void __init__( **kwargs )
            +object load( data )
            +dict dump( self )
            +object work( self, interface )
        }

    :param skill: active ccf skill
    :type skill: str
    """
    skill          = ''
    status         = ''
    status_message = ''
    advanced_skill = ''
    object_index   = 0

    def __init__( self, **kwargs ):

        if len( kwargs ) == 0: return

        assert( isinstance( kwargs[ 'skill' ], type( Robot.skill ) ) )

        self.skill = kwargs[ 'skill' ]

        if 'status' in kwargs.keys():

            assert( isinstance( kwargs[ 'status' ], type( Robot.status ) ) )

            self.status = kwargs[ 'status' ]

        if 'status_message' in kwargs.keys():

            assert( isinstance( kwargs[ 'status_message' ], type( Robot.status_message ) ) )

            self.status_message = kwargs[ 'status_message' ]

        if 'advanced_skill' in kwargs.keys():

            assert( isinstance( kwargs[ 'advanced_skill' ], type( Robot.advanced_skill ) ) )

            self.advanced_skill = kwargs[ 'advanced_skill' ]

        if 'object_index' in kwargs.keys():

            assert( isinstance( kwargs[ 'object_index' ], type( Robot.object_index ) ) )

            self.object_index = kwargs[ 'object_index' ]

    @staticmethod
    def load( data ):

        status         = Robot.status
        status_message = Robot.status_message
        advanced_skill = Robot.advanced_skill
        object_index   = Robot.object_index

        if 'status' in data.keys():

            status = data[ 'status' ]

        if 'status-message' in data.keys():

            status_message = data[ 'status-message' ]

        if 'advanced-skill' in data.keys():

            advanced_skill = data[ 'advanced-skill' ]

        if 'object-index' in data.keys():

            object_index = data[ 'object-index' ]

        return Robot(
            skill          = data[ 'skill' ],
            status         = status,
            status_message = status_message,
            advanced_skill = advanced_skill,
            object_index   = object_index
        )


    def dump( self ):

        dump = {
            'skill': self.skill,
            'object-index': self.object_index
        }

        if self.status is not Robot.status:

            dump[ 'status' ] = self.status

        if self.status_message is not Robot.status_message:

            dump[ 'status-message' ] = self.status_message

        if self.advanced_skill is not Robot.advanced_skill:

            dump[ 'advanced-skill' ] = self.advanced_skill

        return dump


    def work( self, interface ):
        """
        """

        assert( isinstance( interface, Interface ) )

        predicate, object = tuple( interface.robot.skill.split( '.' ) )

        obj = getattr( sys.modules[ __name__ ], strToCamelCase( object ) )

        mod = getattr( obj, predicate )

        data = mod( interface )

        return data



class Entrypoint( CcfObject ):
    """ccf Entrypoint

    .. uml::

        class Entrypoint {
            +{static} list BASENAMETAILS
            +str path
            +str name
            +str checksum
            +object reference

            +void __init__( **kwargs )
            +object load( data )
            +dict dump( self )
            +{abstract}object create( path, name, reference, interface = None)
            +{abstract}object eval( path, name, reference, interface = None)
        }

        CcfObject ---> Entrypoint : "parent of"

        Entrypoint ---> Reference : "(object) reference"

    :param BASENAMETAILS: list of allowed entrypoint file base name tails
    :type BASENAMETAILS: list

    :param PATHPREFIXES: list of allowed entrypoint file base name tails
    :type PATHPREFIXES: list

    :param path: path to environment directory
    :type path: str

    :param name: name of entrypoint
    :type name: str

    :param checksum: checksum of entrypoint file
    :type checksum: str, optional

    :param reference: checksum of entrypoint file
    :type reference: str, optional
    """
    BASENAMETAILS = [ 'tf', 'cf.aws.yml', 'cf.aws.json', 'arm.az.json' ]
    path          = ''
    name          = ''
    checksum      = ''
    reference     = None


    def __init__( self, **kwargs ):

        if len( kwargs ) == 0: return

        assert( isinstance( kwargs[ 'path' ], type( Entrypoint.path ) ) )
        assert( isinstance( kwargs[ 'name' ], type( Entrypoint.name ) ) )

        self.path = kwargs[ 'path' ]
        self.name = kwargs[ 'name' ]

        if 'checksum' in kwargs.keys():

            assert( isinstance( 
                kwargs[ 'checksum' ],
                type( Entrypoint.checksum )
            ))

            self.checksum = kwargs[ 'checksum' ]

        if 'reference' in kwargs.keys():

            assert( isinstance( kwargs[ 'reference' ], Reference ) )

            self.reference = kwargs[ 'reference' ]


    @staticmethod
    def load( data ):

        checksum  = Entrypoint.checksum
        reference = Entrypoint.reference

        if 'checksum' in data.keys():

            checksum = data[ 'checksum' ]

        if 'reference' in data.keys():

            reference = Reference.load( data[ 'reference' ] )

        return Entrypoint(
            path      = data[ 'path' ],
            name      = data[ 'name' ],
            checksum  = checksum,
            reference = reference
        )


    def dump( self ):

        dump = {
            'path': self.path,
            'name': self.name
        }

        if self.checksum is not Entrypoint.checksum:

            dump[ 'checksum' ] = self.checksum

        if self.reference is not Entrypoint.reference:

            dump[ 'reference' ] = self.reference.dump()

        return dump


    @staticmethod
    def create( interface ):

        import skills.create

        return skills.create.entrypoint( interface.dump() )



class Reference( CcfObject ):
    """ccf Reference

    .. uml::

        class Reference {
            +str path
            +str checksum
            +str parameters
            +object reference

            +void __init__( **kwargs )
            +object load( data )
            +dict dump( self )
        }

    :param path: path to environment directory
    :type path: str

    :param parameters: path to environment directory
    :type parameters: str
    """
    path         = ''
    checksum     = ''
    parameters   = {}


    def __init__( self, **kwargs ):

        if len( kwargs ) == 0: return

        assert( isinstance( kwargs[ 'path' ], type( Reference.path ) ) )

        self.path = kwargs[ 'path' ]

        if 'checksum' in kwargs.keys():

            assert( isinstance( 
                kwargs[ 'checksum' ],
                type( Reference.checksum )
            ))

            self.checksum = kwargs[ 'checksum' ]

        if 'parameters' in kwargs.keys():

            assert( isinstance( 
                kwargs[ 'parameters' ],
                type( Reference.parameters )
            ))

            self.parameters = kwargs[ 'parameters' ]


    @staticmethod
    def load( data ):

        checksum   = Reference.checksum
        parameters = Reference.parameters

        if 'checksum' in data.keys():

            checksum = data[ 'checksum' ]

        if 'parameters' in data.keys():

            parameters = data[ 'parameters' ]

        return Reference(
            path       = data[ 'path' ],
            checksum   = checksum,
            parameters = parameters
        )


    def dump( self ):

        dump = {
            'path': self.path
        }

        if self.checksum is not Reference.checksum:

            dump[ 'checksum' ] = self.checksum

        if self.parameters is not Reference.parameters:

            dump[ 'parameters' ] = self.parameters

        return dump



class Environment( CcfObject ):
    """ccf Environment

    .. uml::

        class Environment {
            +{static}list PATHPREFIXES
            +str path
            +str checksum

            +void __init__( **kwargs )
            +object load( data )
            +dict dump( self )
            +{abstract}void create( path, platform, interface, instance = None )
            +{abstract}void eval( path, platform, interface, instance = None )
        }

    :param PATHPREFIXES: list of allowed entrypoint file base name tails
    :type PATHPREFIXES: list

    :param path: path to environment directory
    :type path: str

    :param checksum: checksum of environment directory
    :type checksum: str, optional
    """
    PATHPREFIXES = [ 'environments' ]
    path         = ''
    checksum     = ''


    def __init__( self, **kwargs ):

        if len( kwargs ) == 0: return

        assert( isinstance( kwargs[ 'path' ], type( Environment.path ) ) )

        self.path = kwargs[ 'path' ]

        if 'checksum' in kwargs.keys():

            assert( isinstance( 
                kwargs[ 'checksum' ],
                type( Environment.checksum )
            ))

            self.checksum = kwargs[ 'checksum' ]


    @staticmethod
    def load( data ):

        checksum  = Environment.checksum

        if 'checksum' in data.keys():

            kwargs[ 'checksum' ] = data[ 'checksum' ]

        return Environment(
            path     = data[ 'path' ],
            checksum = checksum
        )


    def dump( self ):

        dump = {
            'path': self.path
        }

        if self.checksum is not Environment.checksum:

            dump[ 'checksum' ] = self.checksum

        return dump


    @staticmethod
    def validate( interface ):

        import skills.validate

        return skills.validate.environment( interface.dump() )


    @staticmethod
    def describe( interface ):

        import skills.describe

        Environment.validate( interface )

        return skills.describe.environment( interface.dump() )


    @staticmethod
    def list( interface ):

        import skills.list, skills.validate

        fpath = interface.framework.path
        epath = Environment.PATHPREFIXES[ 0 ]

        abspath = os.path.abspath( os.path.join( fpath, epath ) )

        interface.framework.environments = []

        for path in glob.glob( os.path.join( abspath, '*', '*' ), recursive = True ):

            environment = Environment( path = path )

            interface.framework.environments.insert( 0, environment )

            try:

                Environment.validate( interface )

            except:

                del interface.framework.environments[ 0 ]

                warnings.warn( traceback.format_exc() )

        return skills.list.environment( interface.dump() )



class ResourceGroup( CcfObject ):
    """ccf Resource Group

    .. uml::

        class ResourceGroup {
            +{static}list PATHPREFIXES
            +str path
            +str checksum

            +void __init__( **kwargs )
            +object load( data )
            +dict dump( self )
            +{abstract}void create( path, platform, interface, instance = None )
            +{abstract}void eval( path, platform, interface, instance = None )
        }

    :param PATHPREFIXES: list of allowed entrypoint file base name tails
    :type PATHPREFIXES: list

    :param path: path to environment directory
    :type path: str

    :param checksum: checksum of environment directory
    :type checksum: str, optional
    """
    PATHPREFIXES = [ 'resource-groups' ]
    path         = ''
    checksum     = ''


    def __init__( self, **kwargs ):

        if len( kwargs ) == 0: return

        assert( isinstance( kwargs[ 'path' ], type( ResourceGroup.path ) ) )

        self.path = kwargs[ 'path' ]

        if 'checksum' in kwargs.keys():

            assert( isinstance( 
                kwargs[ 'checksum' ],
                type( ResourceGroup.checksum )
            ))

            self.checksum = kwargs[ 'checksum' ]


    @staticmethod
    def load( data ):

        checksum  = ResourceGroup.checksum

        if 'checksum' in data.keys():

            kwargs[ 'checksum' ] = data[ 'checksum' ]

        return ResourceGroup(
            path     = data[ 'path' ],
            checksum = checksum
        )


    def dump( self ):

        dump = {
            'path': self.path
        }

        if self.checksum is not ResourceGroup.checksum:

            dump[ 'checksum' ] = self.checksum

        return dump



    @staticmethod
    def create( interface ):
        """
        """

        import skills.create

        return skills.create.resourceGroup( interface.dump() )



class Automation( CcfObject ):
    """ccf Automation

    .. uml::

        class Automation {
            +{static}list PATHPREFIXES
            +str path
            +str checksum
            +list steps

            +void __init__( **kwargs )
            +object load( data )
            +dict dump( self )
            +{abstract}void create( path, platform, interface, instance = None )
            +{abstract}void eval( path, platform, interface, instance = None )
        }

        CcfObject ---> Automation

        Automation ---> AutomationStep : "depends on"

    :param checksum: checksum of automation file
    :type checksum: str, optional

    :param path: path to automation file
    :type path: str

    :param name: name of ccfrobot automation
    :type name: str, optional

    :param steps: list of :class:`ccfrobot.AutomationStep` objects
    :type steps: list
    """
    PATHPREFIXES = [ 'automations' ]
    path     = ''
    steps    = []
    checksum = ''
    auto_in  = {}


    def __init__( self, **kwargs ):

        if len( kwargs ) == 0: return

        assert( ( 'path' in kwargs.keys() ) or ( 'steps' in kwargs.keys() ) )

        if 'path' in kwargs.keys():

            assert( isinstance( 
                kwargs[ 'path' ],
                type( Automation.path )
            ))

            self.path = kwargs[ 'path' ]

        if 'checksum' in kwargs.keys():

            assert( isinstance( 
                kwargs[ 'checksum' ],
                type( Automation.checksum )
            ))

            self.checksum = kwargs[ 'checksum' ]

        if 'steps' in kwargs.keys():

            assert( isinstance( 
                kwargs[ 'steps' ],
                type( Automation.steps )
            ))

            self.steps = kwargs[ 'steps' ]


    @staticmethod
    def load( data ):

        checksum = Automation.checksum
        auto_in  = Automation.auto_in
        path     = Automation.path
        steps    = Automation.steps

        if 'steps' in data.keys():

            steps = data[ 'steps' ]

        if 'path' in data.keys():

            path = data[ 'path' ]

        if 'checksum' in data.keys():

            checksum = data[ 'checksum' ]

        if 'auto_in' in data.keys():

            auto_in = data[ 'auto_in' ]

        return Automation(
            path     = path,
            steps    = steps,
            checksum = checksum,
            auto_in  = auto_in
        )


    def dump( self ):

        dump = {
            'PATHPREFIXES': self.PATHPREFIXES
        }

        if self.path is not Automation.steps:

            dump[ 'path' ] = self.path

        if self.steps is not Automation.steps:

            dump[ 'steps' ] = self.steps

        if self.checksum is not Automation.checksum:

            dump[ 'checksum' ] = self.checksum

        return dump


    @staticmethod
    def execute( interface ):

        import skills.execute

        Automation.describe( interface )

        data = skills.execute.automation( Automation.describe( interface ) )

        return data


    @staticmethod
    def validate( interface ):

        import skills.validate

        data = skills.validate.automation( interface.dump() )

        return data


    @staticmethod
    def describe( interface ):

        import skills.describe

        Automation.validate( interface )

        return skills.describe.automation( interface.dump() )



class AutomationStep( CcfObject ):
    """ccf Automation Step

    .. uml::

        class AutomationStep {
            +{static}list PATHPREFIXES
            +str path
            +str checksum

            +void __init__( **kwargs )
            +object load( data )
            +dict dump( self )
            +{abstract}void create( path, platform, interface, instance = None )
            +{abstract}void eval( path, platform, interface, instance = None )
        }

    :param command: a command to execute
    :type command: str

    :param context: a CCF context
    :type context: Interface, optional
    """
    TYPES     = [ 'shell', 'ccfrobot', 'python3-script' ]
    type      = ''
    input     = None
    output    = None
    interface = None

    @abc.abstractmethod
    def __init__( self ):

        pass


    @staticmethod
    @abc.abstractmethod
    def load( data ):

        return NotImplemented


    @abc.abstractmethod
    def dump( self ):

        return NotImplemented



class Api( CcfObject ):

    TYPES         = [ 'http-html', 'http-rest' ]
    type          = ''
    configuration = {}