#!/bin/env python3
"""skill functions for executing ccf object

"""
import os, asyncio, socket, json, warnings, random, string, queue, threading, sys, io, subprocess, traceback, pprint


STDOUT = sys.stdout


class Exception(BaseException):
    """
    """

    pass



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    GREY = '\033[90m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



class PropagatingThread( threading.Thread ):
    def run(self):
        self.exc = None
        try:
            if hasattr(self, '_Thread__target'):
                # Thread uses name mangling prior to Python 3.
                self.ret = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
            else:
                self.ret = self._target(*self._args, **self._kwargs)
        except BaseException as e:
            self.exc = e

    def join(self):
        super(PropagatingThread, self).join()
        if self.exc:
            raise self.exc
        return self.ret



class UnknownIpSocketTokenException( Exception ):
    """
    """

    pass



class ExceededIpSocketFaulToleranceException( Exception ):
    """
    """

    pass



class ForkProcessRaisedException( Exception ):
    """
    """

    pass



class __MultiplexIO( io.StringIO ):
    """Multiplexer for a file, and stdout stream (simultaneously)

    POSIX file-descriptor like class for multiplexing into a file, and 
    stdout stream simultaneously. This class' instantiation is equal to a 
    `open()`call. For more information refer to `open()`.
    """

    __filehandle = None

    def __init__( self, *args, **kwargs ):
        """
        """

        self.__filehandle = open( *args, **kwargs )


    def write( self, text ):
        """
        """

        STDOUT.write( '\033[90m' + text + '\033[0m' )

        self.__filehandle.write( text )


    def fileno( self ):
        """
        """

        return self.__filehandle.fileno()


    def __getattr__( self, name ):
        """
        """

        return getattr( self.__filehandle, name )



def __getLoopbackIpAddress():
    """
    """

    return '.'.join((
        str( 127 ),
        str( 0 ),
        str( 0 ),
        str( 1 )
    ))



def __getRandomNotWellKnownIpPort():
    """
    """

    return random.randrange( 1024, 65535 )



def __getRandomToken( size = 64 ):
    """
    """

    import random

    return ''.join( random.choices(
        string.ascii_lowercase + string.ascii_uppercase + string.digits,
        k = size
    ))



def __receiveFromSocket( rsock ):
    """
    :param rsock:
    :type rsock: socket.Socket
    """

    data = b''

    while True:
 
        buf = rsock.recv( 1024 ); data += buf

        if not buf: break

    rsock.close()

    return data



def __loadEnviron( token, data ):
    """load and validate a streamed environ data structure

    Validate a streamed environ data structure against an authentication token.
    Failed validations will raise an exception, successful validations will 
    return the environ data structure as a `dict`.

    :param data: data to be evaluated
    :type data: str

    :rtype: dict
    """

    obj = json.loads( data )

    if 'token' not in obj.keys() or obj[ 'token' ] != token:

        raise UnknownIpSocketTokenException( 'InvalidToken')

    if 'exception' in obj.keys():

        raise ForkProcessRaisedException( obj[ 'exception' ] )

    return obj



def __ipReceiveEnviron( faultTolerance = 50, **kwargs ):
    """receive environ data through an IP socket 

    Receive environ data through an IP socket, as part of the inter-process
    communication between a main and a forked process. The main process will
    wait for the forked process to finish. A finished state is, when the forked
    process has send data to the IP socket. The forked process identifies itself
    to the main process through an authentication token.

    :param faultTolerance: how many times an invalid data structure can be sent
        to the socket, before it will be closed.
    :param:

    :param laddr: an IP address for the local socket
    :type laddr: str

    :param lport: an IP port for the local socket
    :type lport: int

    :param token: a token to authenticate requests against
    :type token: str
    """

    assert( 'laddr' in kwargs.keys() )
    assert( 'lport' in kwargs.keys() )
    assert( 'token' in kwargs.keys() )

    lsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    lsock.bind( ( kwargs[ 'laddr' ], kwargs[ 'lport' ] ) )

    lsock.listen( 5 )

    fcount = 0

    while fcount < faultTolerance: 

        rsock, raddr = lsock.accept()

        data = __receiveFromSocket( rsock )

        lsock.close()

        try:

            return __loadEnviron( kwargs[ 'token' ], data )

        except UnknownIpSocketTokenException:

            fcount += 1

    raise ExceededIpSocketFaulToleranceException()



def __ipReceiveEnvironWorker( que, *args, **kwargs ):
    """queued __ipReceiveEnviron

    This will wait for __ipReceiveEnviron() and put it's result
    data into a queue.

    :param que: A queue to put result data into.
    :type que: queue.Queue
    """

    assert( isinstance( que, queue.Queue ) )

    que.put( __ipReceiveEnviron( *args, **kwargs ) )



def __ipSendEnviron( data = {}, **kwargs ):
    """send environ data through an IP socket

    send environ data structures through an IP socket, as part of the 
    inter-process communication between a main and a forked process. The forked
    process must call __ipSendEnviron() before it exits, otherwise the main 
    process has to apply a timeout to it's receive operation.

    :param raddr: an IP address for the remote socket
    :type laddr: str

    :param rport: an IP port for the remote socket
    :type rport: int

    :param token: a token to authenticate requests with
    :type token: str
    """

    import os, json

    assert( 'raddr' in kwargs.keys() )
    assert( 'rport' in kwargs.keys() )
    assert( 'token' in kwargs.keys() )

    lsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    lsock.connect( ( kwargs[ 'raddr' ], kwargs[ 'rport' ] ) )

    if data == {}:

        with open( os.environ[ 'CCF_INTERFACEBUFFER' ], 'r' ) as fh:

            data = json.loads( fh.read() )

    if 'exception' in kwargs.keys():

        dataout = json.dumps( {
        'token': kwargs[ 'token' ],
        'exception': traceback.format_exc(),
        'interface': data
    } )

    else:

        dataout = json.dumps( {
            'token': kwargs[ 'token' ],
            'environ': dict( os.environ ),
            'interface': data
        } )

    with open( os.environ[ 'CCF_INTERFACEBUFFER' ], 'w' ) as fh:

        fh.write( json.dumps( data, indent = 5, sort_keys = True ) )

    lsock.sendall( dataout.encode() )

    lsock.close()



def __executeShellScript( script, laddr, lport, token ):
    """execute a shell script

    :param script:
    :type script: str

    :param laddr:
    :type laddr: str

    :param lport:
    :type lport: int

    :param token:
    :type token: str
    """

    if 'CCF_INTERFACEBUFFER' not in os.environ.keys():

        warnings.warn( 'No interface buffer `CCF_INTERFACEBUFFER` specified.' )


    path = os.path.abspath( os.path.dirname( __file__ ) )

    afterScript = f'python3 -c "import sys; sys.path.insert( 0, \'{path}\' ); import execute; execute.__ipSendEnviron( raddr = \'{laddr}\', rport = {lport}, token = \'{token}\' )"'

    ph = subprocess.Popen( 
        '\n'.join([
            script,
            afterScript
        ]),
        stdout=subprocess.PIPE, 
        universal_newlines=True, 
        shell = True,
        env = os.environ
    )

    for line in iter( ph.stdout.readline, "" ): print( line )

    ph.stdout.close()

    err = ph.wait()

    if err: raise subprocess.CalledProcessError( err, script )



def __executePythonScript( script, laddr, lport, token ):
    """execute a python script

    :param script:
    :type script: str

    :param laddr:
    :type laddr: str

    :param lport:
    :type lport: int

    :param token:
    :type token: str
    """

    pkgpath = os.path.abspath( os.path.join( 
        os.path.dirname( __file__ ), 
        '..', 
        '..'
    ))

    sys.path.insert( 0, pkgpath )

    import ccfrobot

    environ = dict( os.environ )

    if 'CCF_INTERFACEBUFFER' in os.environ.keys():

        with open( os.environ[ 'CCF_INTERFACEBUFFER' ], 'r' ) as fh:

            interface = ccfrobot.loads( fh.read() )

    else:

        warnings.warn( 'No interface buffer `CCF_INTERFACEBUFFER` specified.' )

    exec( script )

    __ipSendEnviron( ccfrobot.dump( interface ), raddr = laddr, rport = lport, token = token )



def __executeRobotScript( script, laddr, lport, token ):
    """
    """

    pkgpath = os.path.abspath( os.path.join( 
        os.path.dirname( __file__ ), 
        '..', 
        '..'
    ))

    sys.path.insert( 1, pkgpath )

    import ccfrobot

    with open( os.environ[ 'CCF_INTERFACEBUFFER' ], 'r' ) as fh:

        interface = ccfrobot.loads( fh.read() )

    interface.robot = ccfrobot.Robot(
        skill = script
    )

    data = interface.robot.work( interface )

    __ipSendEnviron( data, raddr = laddr, rport = lport, token = token )



def __upgradeDict( master, slave ):
    """upgrade/merge/join a master with a slave map

    Upgrade a master with a slave map/dict, and slave values dominating over 
    existing master values.

    :param master: map to be upgraded
    :type master: dict

    :param slave: map to upgrade with
    :type slave: dict
    """

    if type( master ) is dict:

        mindexes = master.keys()
    else:

        mindexes = range( len( master ) )

    if type( slave ) is dict:

        sindexes = slave.keys()
    else:

        sindexes = range( len( slave ) )

    for x in mindexes:

        if type( master[ x ] ) is dict or type( master[ x ] ) is list:

            if x in sindexes:

                master[ x ] = __upgradeDict( master[ x ], slave[ x ] )

        elif x in sindexes:

            master[ x ] = slave[ x ]

    for x in sindexes:

        if x not in mindexes:

            master[ x ] = slave[ x ]

    return master



def __loadAutomationFromFile( path ):
    """load an automation as  a JSON or yaml formatted file
    """

    fh = open( path, 'r' )

    try: 

        data = json.loads( fh.read() )

    except:

        import yaml

        fh.seek( 0 )

        data = yaml.load( fh, yaml.CLoader )

    return data



def __upgradeAutomationData( data ):
    """
    """

    automation = data[ 'framework' ][ 'automations' ][ 0 ]

    frameworkPath = os.path.abspath( data[ 'framework' ][ 'path' ] )

    path = os.path.join( frameworkPath, automation[ 'path' ] )

    adata = __loadAutomationFromFile( path )

    automation = __upgradeDict( automation, adata )

    data[ 'framework' ][ 'automations' ][ 0 ] = automation

    fpath = data[ 'framework' ][ 'path' ]
    epath = data[ 'framework' ][ 'automations' ][ 0 ][ 'path' ]

    abspath = os.path.abspath( os.path.join( fpath, 'automations', epath ) )

    if os.path.isdir( abspath ):

        adata = __loadAutomationFromFile( path )

        automation = __upgradeDict( automation, adata )

    else:

        with open( os.path.join( abspath ), 'r' ):

            env = yaml.load( fh, Loader = SafeLoaderIgnoreUnknown )

    return data




def __formatStepHeader( stepno, stepcount, pid, ppid, type, summary ):

    return '%sSTEP %s/%s (pid:%s,ppid:%s,type:%s)%s - %s' % (
        '\033[95m',
        stepno, 
        stepcount,
        os.getpid(),
        os.environ[ 'CCF_MAINPID' ],
        type,
        '\033[0m',
        summary
    )



def __defaultExecuteScriptMap():

    return {
        'shell-script':  __executeShellScript,
        'python-script': __executePythonScript,
        'ccfrobot':      __executeRobotScript
    }



def automation( data ):
    """execute all automation steps of an automation

    This will always default to the first automation definition.

    :param data: ccf request object model
    :type data: dict

    :rtype: dict
    """

    environ = {}

    __upgradeDict( data[ 'framework' ][ 'automations' ][ 0 ][ 'environ' ], dict( os.environ ) )


    for index in range( len( data[ 'framework' ][ 'automations' ][ 0 ][ 'steps' ] ) ):

        if ( index == 0 ):

            data[ 'framework' ][ 'automations' ][ 0 ][ 'steps' ][ index ][ 'environ' ] = data[ 'framework' ][ 'automations' ][ 0 ][ 'environ' ]

            os.environ = data[ 'framework' ][ 'automations' ][ 0 ][ 'steps' ][ index ][ 'environ' ]

        else:

            data[ 'framework' ][ 'automations' ][ 0 ][ 'steps' ][ index ][ 'environ' ] = data[ 'framework' ][ 'automations' ][ 0 ][ 'steps' ][ index - 1 ][ 'environ' ]

            os.environ = data[ 'framework' ][ 'automations' ][ 0 ][ 'steps' ][ index - 1 ][ 'environ' ]

        data = automationStep( index, data, environ )

    return data



def automationStep( index, data, environ = {}, timeout = 600, aindex = 0, scriptmap={} ):
    """execute a single automation step

    returns the input `data` ccf interface with a modified `environ` attribute 
    of the executed step.

    a step's `script` is executed within a process fork and communicates with 
    the main process via a loopback IP socket on a random, not well known port. 
    The step is considered completed once the main process has received 
    JSON-encoded and `token`-authenticated environment data. The step is 
    considered to be in a failed state once the main process' receive operation 
    exceeds a `timeout`.

    a process fork's `stdout` is piped into a temporary file socket, whose path 
    can be referenced through the environment variable `CCF_STDOUTBUFFER`. In 
    addition, the output is also mirrored to the default shell `stdout` and 
    recolored. see class :class::`__MultiplexIO` for more information.

    :param index: index of automation step (framework.automations[?].steps[#]) 
        to be executed.
    :type index: int

    :param data: ccf interface dump
    :type data: dict

    :param aindex: index of parent automation (framework.automations[#])
    :type aindex: int, optional

    :param environ: dict representing a system environment variables map
    :type environ: dict, optional

    :param timeout: time (in seconds) for a step to be considered `FAIL`
    :type timeout: int, optional

    :rtype: dict

    """

    step = data[ 'framework' ][ 'automations' ][ aindex ][ 'steps' ][ index ]
    stepcount = len( data[ 'framework' ][ 'automations' ][ aindex ][ 'steps' ] )

    scriptmap = __defaultExecuteScriptMap() if scriptmap == {} else scriptmap
    laddr     = __getLoopbackIpAddress()
    lport     = __getRandomNotWellKnownIpPort()
    token     = __getRandomToken()
    que       = queue.Queue()
    thread    = PropagatingThread(
        target = __ipReceiveEnvironWorker,
        args   = [ que,  ],
        kwargs = {'laddr':laddr,'lport':lport,'token': token }
    )

    # this is still awkwardly positioned. The thread will also exist in any 
    # fork. It's problematic, while not being problematic. The thread creates
    # a UNIX socket, and even though this operation is done once, the fork 
    # process will still have a handle to the socket, and therefore is able to
    # accept data from the socket. If the fork process executes faster than the 
    # main process, we would lose our data, since it only exists outside of 
    # the main process's context. The main process thread runs with the same 
    # source (function) as the forked process. However, magically, the main 
    # process thread (until now) always executes before the forked process
    # thread. That's not good, because I don't know why... I'm not too well how 
    # process clock  time scheduling works in details (runtime environment, and 
    # kernel), that's why i want to come up with a solution that can be 
    # ignorant of that. For now, we'll also be checking the pid from within 
    # the thread, so that we can determine
    thread.start()

    os.environ[ 'CCF_MAINPID' ] = str( os.getpid() )

    for var in environ.keys():

        os.environ[ var ] = environ[ var ]

    pid = os.fork()

    if pid == 0:

        os.environ[ 'CCF_STDOUTBUFFER' ] = '%s.%s.stdout' % ( 
            os.getpid(), 
            os.environ[ 'CCF_MAINPID' ]
        )

        os.environ[ 'CCF_INTERFACEBUFFER' ] = '%s.%s.interface.json' % ( 
            os.getpid(), 
            os.environ[ 'CCF_MAINPID' ]
        )

        with open( os.environ[ 'CCF_INTERFACEBUFFER' ], 'w' ) as fh:

            fh.write( json.dumps( data, indent=5, sort_keys=True ) )

        os.environ[ 'CCF_CURRENTPID'] = str( os.getpid() )

        __stdout = sys.stdout

        sys.stdout = __MultiplexIO( os.environ[ 'CCF_STDOUTBUFFER' ], 'w+' )

        print( __formatStepHeader( 
            index + 1, 
            stepcount, 
            os.getpid(),
            os.environ[ 'CCF_MAINPID' ],
            step[ 'type' ],
            step[ 'script' ].splitlines()[ 0 ]
        ))

        func = scriptmap[ step[ 'type' ] ]

        try:

            func( step[ 'script' ], laddr, lport, token )

        except BaseException as e:

            __ipSendEnviron( data, raddr = laddr, rport = lport, token = token, exception=True )

            raise e

        sys.stdout = __stdout

        sys.exit()

    else:

        thread.join()

        data = que.get()

        interface = data[ 'interface' ]

        interface[ 'framework' ][ 'automations' ][ aindex ][ 'steps' ][ 0 ][ 'environ' ] = dict( os.environ )

        return interface