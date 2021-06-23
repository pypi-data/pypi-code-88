# -*- coding: utf-8 -*-
"""
Bapy Package.

>>> assert N['MODULE'] == '__module__'
>>> assert N['fail_on_purpose'] == 'fail_on_purpose'
>>> assert N.MODULE.name == 'MODULE'
>>> assert N.MODULE.has(dict) == True
>>> assert N.MODULE.getter({'__module__': 'test'}) == 'test'
>>> from copy import deepcopy
>>> import environs
>>>
>>> deepcopy(environs.Env()) # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
RecursionError: maximum recursion depth exceeded

"""
__all__ = (
    # Std Lib - Imports
    'ByteString',
    'Callable',
    'Container',
    'Generator',
    'Iterable',
    'Iterator',
    'KeysView',
    'Mapping',
    'MutableMapping',
    'MutableSequence',
    'MutableSet',
    'Sequence',
    'Sized',
    'ValuesView',
    'Simple',

    # Vars
    '__version__',
    'NEWLINE',

    # Defaults
    'CMS_INSTALL_POST_DEFAULT',
    'FILE_DEFAULT',
    'FRAME_INDEX',
    'GIT_VERSIONS',
    'STDOUT_DEFAULT',
    'SUDO_DEFAULT',

    # Vars
    'APP_CONTEXT',
    'CURLYBRACKETS',
    'INIT_PY',
    'USERLOCAL',
    'LOCALBIN',
    'WITHSUDO',

    # StdLib - Protected
    'Alias',
    'cancel_all_tasks',
    'CRLock',
    'current_frames',
    'getframe',
    'inspect_empty',
    'RunningLoop',
    'ThreadLock',

    # Aliases
    'LockClass',
    'ModuleSpec',
    'datafield',

    # Typing
    'AsyncsUnion',
    'BaseTypesUnion',
    'DefsUnion',
    'DictStrAny',
    'ExceptionUnion',
    'Frames',
    'FunctionTypesUnion',
    'IteratorTypes',
    'LST',
    'OpenIO',
    'PrimitiveTypesUnion',
    'SeqNoStr',
    'SeqTuple',
    'SeqUnion',
    'TupleStr',
    'TupleType',

    # Functions
    'aioclosed',
    'aiocmd',
    'aioloop',
    'aioloopid',
    'aiorunning',
    'allin',
    'annotations',
    'annotations_init',
    'anyin',
    'cache',
    'cmd',
    'cmdname',
    'current_task_name',
    'delete',
    'delete_list',
    'dict_sort',
    'effect',
    'enumvalue',
    'filterm',
    'firstfound',
    'flatten',
    'framesimple',
    'fromiter',
    'funcdispatch',
    'get',
    'getcls',
    'getf',
    'getm',
    'getnostr',
    'getprops',
    'getset',
    'getsetstate',
    'has',
    'hasget',
    'hasgetany',
    'importname',
    'indict',
    'indictr',
    'initimps',
    'iseven',
    'istype',
    'join_newline',
    'localbin',
    'map_reduce_even',
    'map_with_args',
    'missing',
    'newprop',
    'noexc',
    'notmissing',
    'notstart',
    'objname',
    'prefixed',
    'pretty_install',
    'pypifree',
    'reprcls',
    'reprkw',
    'sourcepath',
    'sourcevars',
    'splitsep',
    'to_camel',
    'toiter',
    'tomodules',
    'traceback_install',
    'varname',
    'yield_if',
    'yield_last',

    # EnumBase
    'EnumBase',
    'EnumBaseAlias',
    'EnumBaseMeta',

    # Classes
    'Access',
    'AccessEnumMembers',
    'AllAttr',
    'Annotation',
    'AnnotationsAttr',
    'AsDictMethod',
    'AsDictProperty',
    'Attribute',
    'BaseState',
    'BoxKeys',
    'ChainRV',
    'Chain',
    'ClassBase',
    'Class',
    'CmdError',
    'CmdAioError',
    'DataClass',
    'dd',
    'dictsort',
    'Executor',
    'FindUp',
    'Frame',
    'FrameIdBase',
    'FrameId',
    'FrameSimple',
    'GetItem',
    'GetMethod',
    'getter',
    'GitTop',
    'IntervalBase',
    'IntervalType',
    'Is',
    'Kind',
    'MatchError',
    'Missing',
    'MISSING',
    'DictStrMissingAny',
    'ModuleBase',
    'Module',
    'nstr',
    'N',
    'NameAttr',
    'Namedtuple',
    'NamedTupleTyping',
    'NParser',
    'ObjBase',
    'Obj',
    'PIs',
    'PMode',
    'POption',
    'POutput',
    'PSuffixBase',
    'PSuffix',
    'Path',
    'PathInstallScript',
    'Re',
    'Real',
    'ReposNamesBase',
    'ReposNames',
    'SlotsType',
    'SourceVars',
    'SourceBase',
    'Source',
    'Stack',
    'StateEnv',
    'UserActual',
    'UserProcess',
    'User',
    'VarsType',

    # Dependant
    'PathLikeStr',
    'PathInternal',
    'path_internal',
    'SYSCONFIG_PATHS_EXCLUDE',
    'PATHS_EXCL',
    'Types',
    'TypesType',

    # Echo
    'black',
    'blue',
    'cyan',
    'green',
    'magenta',
    'red',
    'white',
    'yellow',
    'bblack',
    'bblue',
    'bcyan',
    'bgreen',
    'bmagenta',
    'bred',
    'bwhite',
    'byellow',

    # Vars: Instances
    'alocks',
    'locks',
    'reposnames',
    'user',
    'init_stack',
)

import abc
import ast
import asyncio.events
import atexit
import collections
import concurrent.futures
import contextlib
import copy
import dataclasses
import datetime
import enum
import functools
# noinspection PyCompatibility
import grp
import importlib
import importlib.machinery
import importlib.util
import inspect
import io
import ipaddress
import json
import logging

import click
import marshmallow.fields
import marshmallow.validate
import os
import pathlib
import pickle
import platform
# noinspection PyCompatibility
import pwd
import re
import shelve
import shlex
import shutil
import site
import socket
import subprocess
import sys
import sysconfig
import tempfile
import textwrap
import threading
import time
import tokenize
import types
import typing
import urllib.error
import warnings
from collections.abc import ByteString as ByteString
from collections.abc import Callable as Callable
from collections.abc import Container as Container
from collections.abc import Generator as Generator
from collections.abc import Iterable as Iterable
from collections.abc import Iterator as Iterator
from collections.abc import KeysView as KeysView
from collections.abc import Mapping as Mapping
from collections.abc import MutableMapping as MutableMapping
from collections.abc import MutableSequence as MutableSequence
from collections.abc import MutableSet as MutableSet
from collections.abc import Sequence as Sequence
from collections.abc import Sized as Sized
from collections.abc import ValuesView as ValuesView
from types import SimpleNamespace as Simple

import box
import colorama
import decorator
import devtools
import distro
import environs
import furl
import git
import icecream
import inflect
import intervaltree
import jinja2
import jsonpickle
import marshmallow
import more_itertools
import nested_lookup
import paramiko
import pymongo.errors
import requests
import rich.console
import rich.pretty
import rich.traceback
import semver
import setuptools.command.install
import structlog
import typer
import urllib3
from nested_lookup.nested_lookup import _nested_lookup

__version__ = '1.0.34'

# Defaults
CMS_INSTALL_POST_DEFAULT = False
FILE_DEFAULT = True
FRAME_INDEX = 1
GIT_VERSIONS = 50
STDOUT_DEFAULT = True
SUDO_DEFAULT = True

# Vars
Alias = typing._alias
ALL_PORTS = range(0, 65535)
APP_CONTEXT = dict(help_option_names=['-h', '--help'], color=True)
app = typer.Typer(context_settings=APP_CONTEXT)
AsyncsUnion = typing.Union[ast.AsyncFor, ast.AsyncWith, ast.Await]
BASE_EXEC_PREFIX = sys.base_exec_prefix
BASE_EXECUTABLE = sys._base_executable
BASE_PREFIX = sys.base_prefix
# noinspection PyAnnotations
BaseTypesUnion = typing.Union[int, float, list, dict, set, tuple, object, bytes]
BASE_TYPES = set(typing.get_args(BaseTypesUnion))
Bool = bool
BUILTIN = (__i if isinstance(__i := globals()['__builtins__'], dict) else vars(__i)).copy()
BUILTIN_CLASS = tuple(filter(lambda x: isinstance(x, type), BUILTIN.values()))
BUILTIN_CLASS_NO_EXCEPTION = tuple(filter(lambda x: not issubclass(x, BaseException), BUILTIN_CLASS))
BUILTIN_CLASS_DICT = (classmethod, staticmethod, type, importlib._bootstrap.BuiltinImporter,)
BUILTIN_CLASS_NO_DICT = tuple(set(BUILTIN_CLASS_NO_EXCEPTION).difference(BUILTIN_CLASS_DICT))
BUILTIN_FUNCTION = tuple(filter(lambda x: isinstance(x, (types.BuiltinFunctionType, types.FunctionType,)),
                                BUILTIN.values()))
BUILTIN_MODULE_NAMES = sys.builtin_module_names
cancel_all_tasks = asyncio.runners._cancel_all_tasks
console = rich.console.Console(color_system='256')
cp = console.print
CRLock = threading._CRLock
current_frames = sys._current_frames
CURLYBRACKETS = '{}'
datafield = dataclasses.field
DATA_MISSING = dataclasses.MISSING
DbfilenameShelf = shelve.DbfilenameShelf
debug = devtools.Debug(highlight=True)
DEFAULT_FACTORY = dataclasses._HAS_DEFAULT_FACTORY
DefsUnion = typing.Union[ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda]
Dict = dict
DictStrAny = dict[str, typing.Any]
DISTRO = distro.LinuxDistribution()
EXEC_PREFIX = sys.exec_prefix
ExceptionUnion = typing.Union[tuple[typing.Type[Exception]], typing.Type[Exception]]
EXECUTABLE = pathlib.Path(sys.executable)
EXECUTABLE_SITE = pathlib.Path(EXECUTABLE).resolve()
FIELD = dataclasses._FIELD
FIELD_BASE = dataclasses._FIELD_BASE
FIELD_CLASSVAR = dataclasses._FIELD_CLASSVAR
FIELD_INITVAR = dataclasses._FIELD_INITVAR
FlagsType = typing.Union[int, re.RegexFlag]
fmic = icecream.IceCreamDebugger(prefix=str()).format
fmicc = icecream.IceCreamDebugger(prefix=str(), includeContext=True).format
FQDN = socket.getfqdn()
FRAME = sys._getframe(0)
Frames = typing.Union[inspect.FrameInfo, types.FrameType, types.TracebackType]
FUNCTION_MODULE = '<module>'
FunctionTypesUnion = typing.Union[types.FunctionType, types.MethodType, types.LambdaType, types.BuiltinFunctionType,
                                  types.BuiltinMethodType]
FUNCTION_TYPES = set(typing.get_args(FunctionTypesUnion))
getframe = sys._getframe
GitCommandWrapperType = git.Repo.GitCommandWrapperType
HOSTNAME = platform.node().split('.')[0]
HTTP_EXCEPTIONS = (urllib.error.HTTPError, json.JSONDecodeError,)
ic = icecream.IceCreamDebugger(prefix=str())
icc = icecream.IceCreamDebugger(prefix=str(), includeContext=True)
ID_RSA_PUB = 'id_rsa.pub'
INIT_PY = '__init__.py'
inspect_empty = inspect._empty
IPv = typing.Union[ipaddress.IPv4Address, ipaddress.IPv6Address]
IMPORTLIB_BOOTSTRAP = importlib._bootstrap.__name__
IMPORTLIB_BOOTSTRAP_EXTERNAL = importlib._bootstrap_external.__name__
IMPORTLIB_PYCACHE = importlib._bootstrap_external._PYCACHE
IteratorTypes = (type(iter('')),)
KALI = DISTRO.id() == 'kali'
LINUX = platform.system() == 'Linux'
List = list
USERLOCAL = pathlib.Path('/usr/local')
LOCALBIN = USERLOCAL / 'bin'
LOCALHOST = socket.gethostbyname('localhost')
LST = typing.Union[list, set, tuple]
LST_TYPES = typing.get_args(LST)
MACOS = platform.system() == 'Darwin'
MACHINE = platform.machine()
MANIFEST = 'MANIFEST.in'
MatchAnyStr = typing.Match[typing.AnyStr]
MatchCallable = typing.Callable[[MatchAnyStr], typing.AnyStr]
MatchCallableUnion = typing.Union[typing.Callable[[MatchAnyStr], typing.AnyStr], typing.AnyStr]
MatchIterator = typing.Iterator[MatchAnyStr]
MatchOptional = typing.Optional[MatchAnyStr]
META_PATH = sys.meta_path
ModuleSpec = importlib._bootstrap.ModuleSpec
MONGO_CONF = '.mongo.toml'
MONGO_EXCEPTIONS = (socket.gaierror, pymongo.errors.ConnectionFailure, pymongo.errors.AutoReconnect,
                    pymongo.errors.ServerSelectionTimeoutError, pymongo.errors.ConfigurationError,)
NEWLINE = '\n'
NODE = platform.node()
OpenIO = typing.Union[io.BufferedRandom, io.BufferedReader, io.BufferedWriter, io.FileIO, io.TextIOWrapper]
PATH_HOOKS = sys.path_hooks
PATHLIBDIR = sys.platlibdir
PLATFORM = platform.platform()
PatternUnion = typing.Union[typing.AnyStr, typing.Pattern[typing.AnyStr]]
plural = inflect.engine().plural
PrimitiveTypesUnion = typing.Union[str, bool, type(None), int, float]
PRIMITIVE_TYPES = set(typing.get_args(PrimitiveTypesUnion))
NON_REDUCTIBLE_TYPES = BASE_TYPES | FUNCTION_TYPES | PRIMITIVE_TYPES
print_exception = console.print_exception
PROCESSOR = platform.processor()
PYTHON_IMPLEMENTATION = platform.python_implementation()
PYTHON_VERSION = platform.python_version()
PYTHON_VERSIONS = (semver.VersionInfo(3, 9), semver.VersionInfo(3, 10),)
PYTHON_VERSION_TUPLE = platform.python_version_tuple()
RELEASE = platform.release()
RunningLoop = asyncio.events._RunningLoop
SeqTuple = typing.Union[MutableSequence, MutableSet, tuple]
SYSCONFIG_PATHS = {__k: pathlib.Path(__v) for __k, __v in sysconfig.get_paths().items()}
SCRIPTS = SYSCONFIG_PATHS['scripts']
Simple = types.SimpleNamespace
SOCKET_VERSION = {4: dict(af=socket.AF_INET), 6: dict(af=socket.AF_INET6)}
SPECIAL_CHARACTERS = '"' + "'" + '!#$%^&*(){}-+?_=,<>/\\'
SSH_CONFIG = dict(AddressFamily='inet', BatchMode='yes', CheckHostIP='no', ControlMaster='auto',
                  ControlPath='/tmp/ssh-%h-%r-%p', ControlPersist='20m', IdentitiesOnly='yes',
                  LogLevel='QUIET', StrictHostKeyChecking='no', UserKnownHostsFile='/dev/null')
SSH_CONFIG_TEXT = ' '.join([f'-o {key}={value}' for key, value in SSH_CONFIG.items()])
Str = str
SUDO_USER = os.getenv('SUDO_USER')
SUDO = bool(SUDO_USER)
SYSPATH = sys.path
SYSPREFIX = sys.prefix
TEMPDIR = pathlib.Path('/') / tempfile.gettempprefix()
ThreadLock = threading.Lock
LockClass = type(ThreadLock())
Tuple = tuple
TupleStr = tuple[str, ...]
TupleType = tuple[typing.Type, ...]
UBUNTU = DISTRO.id() == 'ubuntu'
SeqNoStr = typing.Union[Iterator, KeysView, MutableSequence, MutableSet, Sequence, tuple, ValuesView]
SeqUnion = typing.Union[bytes, ByteString, SeqNoStr, str]
VENV = BASE_PREFIX != SYSPREFIX
WITHSUDO = '' if MACOS else 'sudo '


# Functions
def aioclosed() -> bool: return asyncio.get_event_loop().is_closed()


async def aiocmd(command, decode=True, utf8=False, lines=False):
    """
    Asyncio run cmd.

    Args:
        command: command.
        decode: decode and strip output.
        utf8: utf8 decode.
        lines: split lines.

    Returns:
        CompletedProcess.
    """
    proc = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE,
                                                 stderr=asyncio.subprocess.PIPE, loop=asyncio.get_running_loop())
    stdout, stderr = await proc.communicate()
    if decode:
        stdout = stdout.decode().rstrip('.\n')
        stderr = stderr.decode().rstrip('.\n')
    elif utf8:
        stdout = stdout.decode('utf8').strip()
        stderr = stderr.decode('utf8').strip()

    out = stdout.splitlines() if lines else stdout

    return subprocess.CompletedProcess(command, proc.returncode, out, typing.cast(typing.Any, stderr))


def aioloop(): return noexc(RuntimeError, asyncio.get_running_loop)


def aioloopid():
    try:
        return asyncio.get_running_loop()._selector
    except RuntimeError:
        return None


def aiorunning(): return asyncio.get_event_loop().is_running()


def allin(origin, destination):
    """
    Checks all items in origin are in destination iterable.

    Examples:
        >>> class Int(int):
        ...     pass
        >>> allin(tuple.__mro__, BUILTIN_CLASS)
        True
        >>> allin(Int.__mro__, BUILTIN_CLASS)
        False
        >>> allin('tuple int', 'bool dict int')
        False
        >>> allin('bool int', ['bool', 'dict', 'int'])
        True
        >>> allin(['bool', 'int'], ['bool', 'dict', 'int'])
        True

    Args:
        origin: origin iterable.
        destination: destination iterable to check if origin items are in.

    Returns:
        True if all items in origin are in destination.
    """
    origin = toiter(origin)
    destination = toiter(destination)
    return all(map(lambda x: x in destination, origin))


def annotations(data, index=1):
    """
    Formats obj annotations.

    Examples:
        >>> from typing import Optional, Final, Any, ClassVar, Union, Literal
        >>> from bapy import Is
        >>> import bapy.data.cls
        >>> ann = annotations(bapy.data.cls.DataAnnotations)
        >>> assert (ann['any'].any, ann['any'].cls, ann['any'].default) == (True, Any, None)
        >>> assert (ann['classvar'].classvar, ann['classvar'].cls, ann['classvar'].default) == (True, str, '')
        >>> assert (ann['classvar_optional'].classvar, ann['classvar_optional'].cls, \
        ann['classvar_optional'].default) == (True, str, '')
        >>> assert (ann['classvar_optional_union'].classvar, ann['classvar_optional_union'].cls, \
        ann['classvar_optional_union'].default) == (True, str, '')
        >>> assert (ann['classvar_union'].classvar, ann['classvar_union'].cls, \
        ann['classvar_union'].default) == (True, str, '')
        >>> assert (ann['final'].final, ann['final'].cls, ann['final'].default) == \
        (True, Final, None)  # TODO: 'final'
        >>> assert (ann['final_str'].final, ann['final_str'].cls, ann['final_str'].default) == \
        (True, str, '')  # TODO: 'final_str'
        >>> assert (ann['integer'].cls, ann['integer'].default) == (int, 0)
        >>> assert (ann['initvar'].initvar, ann['initvar'].cls, ann['initvar'].default) == (True, str, '')
        >>> assert (ann['initvar_optional'].initvar, ann['initvar_optional'].cls, \
        ann['initvar_optional'].default) == (True, str, '')
        >>> assert (ann['literal'].literal, ann['literal'].cls, ann['literal'].default) == (True, str, 'literal')
        >>> assert (ann['literal_optional'].literal, ann['literal_optional'].cls, \
        ann['literal_optional'].default) == (True, str, 'literal_optional')
        >>> assert (ann['optional'].optional, ann['optional'].cls, ann['optional'].default) == (True, str, '')
        >>> assert (ann['union'].union, ann['union'].cls, ann['union'].default) == (True, str, '')
        >>> assert (ann['optional_union'].optional, ann['optional_union'].union, ann['optional_union'].cls, \
        ann['optional_union'].default) == (True, True, str, '')

    Args:
        data: instance or class.
        index: stack index.

    Returns:
        Annotation: obj annotations. Default are filled with annotation not with class default.
    """

    def value(_cls):
        # TODO: 1) default from annotations, 2) value from kwargs or class defaults.
        return noexc(_cls)

    def inner(_hint):
        cls = _hint
        default = None
        args = list(typing.get_args(_hint))
        _annotations = list()
        origin = typing.get_origin(_hint)
        literal = origin == typing.Literal
        final = origin == typing.Final or _hint == typing.Final
        _any = _hint == typing.Any
        union = origin == typing.Union
        classvar = origin == typing.ClassVar
        # TODO: Look because origin must be InitVar and then  ...
        initvar = isinstance(cls, dataclasses.InitVar)
        optional = type(None) in args
        if initvar:
            if isinstance(_hint.type, type):
                cls = _hint.type
                default = value(cls)
            else:
                _hint = _hint.type
                _a = inner(_hint)
                _annotations.append(_a)
                default = _a.default
                cls = _a.cls
        elif origin is None:
            cls = _hint
            # TODO: final (now: None) -> default: 'final'  # hint == Final and origin is None
            default = None if _any or final else value(cls)
        elif literal and args:
            default = args[0]  # TODO: o default or kwarg or None if Optional(?)
            cls = type(default)
        elif final and args:  # origin == Final
            cls = args[0]
            # TODO: final (now: '') -> default: 'final_str'
            default = cls()
        elif args:
            literal = typing.Literal._name in repr(_hint)
            for arg in args:
                if isinstance(arg, type(None)):
                    _annotations.append(None)
                else:
                    _a = inner(arg)
                    _annotations.append(_a)
            obj = _annotations[1] if _annotations[0] is None else _annotations[0]
            default = obj.default
            cls = obj.cls
        return Annotation(any=_any, args=_annotations or args, classvar=classvar, cls=cls, default=default,
                          final=final, hint=_hint, initvar=initvar, literal=literal, name=name,
                          optional=optional, origin=origin, union=union)

    frame = inspect.stack()[index].frame
    globs, locs = frame.f_globals, frame.f_locals
    rv = {}
    try:
        if a := typing.get_type_hints(data, globalns=globs, localns=locs):
            for name in a:
                rv |= {name: inner(a.get(name))}
    except TypeError:
        rv = {}
    return rv


def annotations_init(data, index=2, optional=True, **kwargs):
    """
    Init class with defaults or kwargs a class.

    Examples:
        >>> from typing import NamedTuple, Optional
        >>> from pathlib import Path
        >>> NoInitValue = NamedTuple('NoInitValue', var=str)
        >>> A = NamedTuple('A', module=str, path=Optional[Path], test=Optional[NoInitValue])
        >>> assert annotations_init(A, optional=False) == A(module='', path=None, test=None)
        >>> assert annotations_init(A) == A(module='', path=Path('.'), test=None)
        >>> assert annotations_init(A, test=NoInitValue('test')) == \
        A(module='', path=Path('.'), test=NoInitValue(var='test'))
        >>> assert annotations_init(A, optional=False, test=NoInitValue('test')) == \
        A(module='', path=None, test=NoInitValue(var='test'))

    Args:
        data: instance or class.
        index: stack index.
        optional: True to use args[0] instead of None as default for Optional fallback to None if exception.
        **kwargs:

    Returns:
        cls: cls instance with default values.
    """
    values = dict()
    for name, a in annotations(data=data, index=index).items():
        if v := kwargs.get(name):
            value = v
        elif a.origin == typing.Union and not optional:
            value = None
        else:
            value = a.default
        values[name] = value
    with contextlib.suppress(Exception):
        return Is(data)()(**values)


def anyin(origin, destination):
    """
    Checks any item in origin are in destination iterable and return the first found.

    Examples:
        >>> class Int(int):
        ...     pass
        >>> anyin(tuple.__mro__, BUILTIN_CLASS)
        <class 'tuple'>
        >>> assert anyin('tuple int', BUILTIN_CLASS) is None
        >>> anyin('tuple int', 'bool dict int')
        'int'
        >>> anyin('tuple int', ['bool', 'dict', 'int'])
        'int'
        >>> anyin(['tuple', 'int'], ['bool', 'dict', 'int'])
        'int'

    Args:
        origin: origin iterable.
        destination: destination iterable to check if any of origin items are in.

    Returns:
        First found if any item in origin are in destination.
    """
    origin = toiter(origin)
    destination = toiter(destination)
    for item in toiter(origin):
        if item in destination:
            return item


def cache(func):
    """
    Caches previous calls to the function if object can be encoded.

    Examples:
        >>> import asyncio
        >>> from environs import Env as Environs
        >>> from collections import namedtuple
        >>> from bapy import cache
        >>>
        >>> @cache
        ... def test(a):
        ...     print(True)
        ...     return a
        >>>
        >>> @cache
        ... async def test_async(a):
        ...     print(True)
        ...     return a
        >>>
        >>> test({})
        True
        {}
        >>> test({})
        {}
        >>> asyncio.run(test_async({}))
        True
        {}
        >>> asyncio.run(test_async({}))
        {}
        >>> test(Environs())
        True
        <Env {}>
        >>> test(Environs())
        <Env {}>
        >>> asyncio.run(test_async(Environs()))
        True
        <Env {}>
        >>> asyncio.run(test_async(Environs()))
        <Env {}>
        >>>
        >>> @cache
        ... class Test:
        ...     def __init__(self, a):
        ...         print(True)
        ...         self.a = a
        ...
        ...     @property
        ...     @cache
        ...     def prop(self):
        ...         print(True)
        ...         return self
        >>>
        >>> Test({})  # doctest: +ELLIPSIS
        True
        <....Test object at 0x...>
        >>> Test({})  # doctest: +ELLIPSIS
        <....Test object at 0x...>
        >>> Test({}).a
        {}
        >>> Test(Environs()).a
        True
        <Env {}>
        >>> Test(Environs()).prop  # doctest: +ELLIPSIS
        True
        <....Test object at 0x...>
        >>> Test(Environs()).prop  # doctest: +ELLIPSIS
        <....Test object at 0x...>
        >>>
        >>> Test = namedtuple('Test', 'a')
        >>> @cache
        ... class TestNamed(Test):
        ...     __slots__ = ()
        ...     def __new__(cls, *args, **kwargs):
        ...         print(True)
        ...         return super().__new__(cls, *args, **kwargs)
        >>>
        >>> TestNamed({})
        True
        TestNamed(a={})
        >>> TestNamed({})
        TestNamed(a={})
        >>> @cache
        ... class TestNamed(Test):
        ...     __slots__ = ()
        ...     def __new__(cls, *args, **kwargs): return super().__new__(cls, *args, **kwargs)
        ...     def __init__(self): super().__init__()
        >>> TestNamed({}) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError: __init__() takes 1 positional argument but 2 were given
    """
    memo = {}
    log = structlog.get_logger()
    structlog.configure(logger_factory=structlog.stdlib.LoggerFactory())
    coro = inspect.iscoroutinefunction(func)
    if coro:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            """Async Cache Wrapper."""
            key = None
            save = True
            try:
                key = jsonpickle.encode((args, kwargs))
                if key in memo:
                    return memo[key]
            except Exception as exception:
                log.warning('Not cached', func=func, args=args, kwargs=kwargs, exception=exception)
                save = False
            value = await func(*args, **kwargs)
            if key and save:
                memo[key] = value
            return value
    else:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Cache Wrapper."""
            key = None
            save = True
            try:
                key = jsonpickle.encode((args, kwargs))
                if key in memo:
                    return memo[key]
            except Exception as exception:
                log.warning('Not cached', func=func, args=args, kwargs=kwargs, exception=exception)
                save = False
            value = func(*args, **kwargs)
            if key and save:
                memo[key] = value
            return value
    return wrapper


def cmd(command, exc=False, lines=True, shell=True, py=False, pysite=True):
    """
    Runs a cmd.

    Examples:
        >>> cmd('ls a')
        CompletedProcess(args='ls a', returncode=1, stdout=[], stderr=['ls: a: No such file or directory'])
        >>> assert 'Requirement already satisfied' in cmd('pip install pip', py=True).stdout[0]
        >>> cmd('ls a', shell=False, lines=False)  # Extra '\' added to avoid docstring error.
        CompletedProcess(args=['ls', 'a'], returncode=1, stdout='', stderr='ls: a: No such file or directory\\n')
        >>> cmd('echo a', lines=False)  # Extra '\' added to avoid docstring error.
        CompletedProcess(args='echo a', returncode=0, stdout='a\\n', stderr='')

    Args:
        command: command.
        exc: raise exception.
        lines: split lines so ``\\n`` is removed from all lines (extra '\' added to avoid docstring error).
        py: runs with python executable.
        shell: expands shell variables and one line (shell True expands variables in shell).
        pysite: run on site python if running on a VENV.

    Returns:
        Union[CompletedProcess, int, list, str]: Completed process output.

    Raises:
        CmdError:
   """
    if py:
        m = '-m'
        if isinstance(command, str) and command.startswith('/'):
            m = str()
        command = f'{str(EXECUTABLE_SITE) if pysite else str(EXECUTABLE)} {m} {command}'
    elif not shell:
        command = toiter(command)

    if lines:
        text = False
    else:
        text = True

    proc = subprocess.run(command, shell=shell, capture_output=True, text=text)

    def std(out=True):
        if out:
            if lines:
                return proc.stdout.decode("utf-8").splitlines()
            else:
                # return proc.stdout.rstrip('.\n')
                return proc.stdout
        else:
            if lines:
                return proc.stderr.decode("utf-8").splitlines()
            else:
                # return proc.stderr.decode("utf-8").rstrip('.\n')
                return proc.stderr

    rv = subprocess.CompletedProcess(proc.args, proc.returncode, std(), std(False))
    if rv.returncode != 0 and exc:
        raise CmdError(rv)
    return rv


def cmdname(func, sep='_'): return func.__name__.split(**splitsep(sep))[0]


def current_task_name(): return asyncio.current_task().get_name() if aioloop() else str()


@functools.singledispatch
def delete(data: MutableMapping, key=('self', 'cls',)):
    """
    Deletes item in dict based on key.

    Args:
        data: MutableMapping.
        key: key.

    Returns:
        data: dict with key deleted or the same if key not found.
    """
    key = toiter(key)
    for item in key:
        with contextlib.suppress(KeyError):
            del data[item]
    return data


@delete.register
def delete_list(data: list, key=('self', 'cls',)):
    """
    Deletes value in list.

    Args:
        data: MutableMapping.
        key: key.

    Returns:
        data: list with value deleted or the same if key not found.
    """
    key = toiter(key)
    for item in key:
        with contextlib.suppress(ValueError):
            data.remove(item)
    return data


def dict_sort(data, ordered=False, reverse=False):
    """
    Order a dict based on keys.

    Args:
        data: dict to be ordered.
        ordered: OrderedDict.
        reverse: reverse.

    Returns:
        Union[dict, collections.OrderedDict]: Dict sorted
    """
    rv = {key: data[key] for key in sorted(data.keys(), reverse=reverse)}
    if ordered:
        return collections.OrderedDict(rv)
    return rv.copy()


def effect(apply, *args):
    """
    Perform function on iterable.

    Examples:
        >>> simple = Simple()
        >>> effect(lambda x: simple.__setattr__(x, dict()), 'a b', 'c')
        >>> assert simple.a == {}
        >>> assert simple.b == {}
        >>> assert simple.c == {}

    Args:
        apply: Function to apply.
        *args: Iterable to perform function.

    Returns:
        No Return.
    """
    for arg in toiter(args):
        for item in arg:
            apply(item)


def enumvalue(data):
    """
    Returns Enum Value if Enum Instance or Data.

    Examples:
        >>> enumvalue(N.ANNOTATIONS)
        '__annotations__'
        >>> enumvalue(None)

    Args:
        data: object.

    Returns:
        Enum Value or Data.
    """
    return data() if Is(data).enum else data


def filterm(d, k=lambda x: True, v=lambda x: True):
    # noinspection PyUnresolvedReferences
    """
    Filter Mutable Mapping.

    >>> assert filterm({'d':1}) == {'d': 1}
    >>> assert filterm({'d':1}, lambda x: x.startswith('_')) == {}
    >>> assert filterm({'d': 1, '_a': 2}, lambda x: x.startswith('_'), lambda x: isinstance(x, int)) == {'_a': 2}

    Returns:
        Filtered dict with
    """
    return d.__class__({x: y for x, y in d.items() if k(x) and v(y)})


def firstfound(data, apply):
    """
    Returns first value in data if apply is True.

    >>> assert firstfound([1, 2, 3], lambda x: x == 2) == 2
    >>> assert firstfound([1, 2, 3], lambda x: x == 4) is None

    Args:
        data: iterable.
        apply: function to apply.

    Returns:
        Value if found.
    """
    for i in data:
        if apply(i):
            return i


def flatten(data, recurse=False, unique=False, sort=True):
    """
    Flattens an Iterable

    >>> assert flatten([1, 2, 3, [1, 5, 7, [2, 4, 1, ], 7, 6, ]]) == [1, 2, 3, 1, 5, 7, [2, 4, 1], 7, 6]
    >>> assert flatten([1, 2, 3, [1, 5, 7, [2, 4, 1, ], 7, 6, ]], recurse=True) == [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 7]
    >>> assert flatten((1, 2, 3, [1, 5, 7, [2, 4, 1, ], 7, 6, ]), unique=True) == (1, 2, 3, 4, 5, 6, 7)

    Args:
        data: iterable
        recurse: recurse
        unique: when recurse
        sort: sort

    Returns:
        Union[list, Iterable]:
    """
    if unique:
        recurse = True

    cls = data.__class__

    flat = []
    _ = [flat.extend(flatten(item, recurse, unique) if recurse else item)
         if isinstance(item, list) else flat.append(item) for item in data if item]
    value = set(flat) if unique else flat
    if sort:
        try:
            value = cls(sorted(value))
        except TypeError:
            value = cls(value)
    return value


def framesimple(data):
    """
    :class:`rc.FrameSimple`.

    Examples:
        >>> frameinfo = inspect.stack()[0]
        >>> finfo = framesimple(frameinfo)
        >>> ftype = framesimple(frameinfo.frame)
        >>> assert frameinfo.frame.f_code == finfo.code
        >>> assert frameinfo.frame == finfo.frame
        >>> assert frameinfo.filename == str(finfo.path)
        >>> assert frameinfo.lineno == finfo.lineno
        >>> fields_frame = list(FrameSimple._fields)
        >>> fields_frame.remove('vars')
        >>> for attr in fields_frame:
        ...     assert getattr(finfo, attr) == getattr(ftype, attr)

    Returns:
        :class:`rc.FrameSimple`.
    """
    i = Is(data)
    if not any([i.frameinfo, i.frametype, i.tracebacktype]):
        return
    if i.frameinfo:
        frame = data.frame
        back = frame.f_back
        lineno = data.lineno
    elif i.frametype:
        frame = data
        back = data.f_back
        lineno = data.f_lineno
    else:
        frame = data.tb_frame
        back = data.tb_next
        lineno = data.tb_lineno

    code = frame.f_code
    f_globals = frame.f_globals
    f_locals = frame.f_locals
    function = code.co_name
    v = f_globals | f_locals
    name = v.get(N.NAME) or function
    return FrameSimple(back=back, code=code, frame=frame, function=function, globals=f_globals, lineno=lineno,
                       locals=f_locals, name=name, package=v.get(N.PACKAGE) or name.split('.')[0],
                       path=sourcepath(data), vars=v)


def fromiter(data, *args):
    """
    Gets attributes from Iterable of objects and returns dict with

    >>> assert fromiter([Simple(a=1), Simple(b=1), Simple(a=2)], 'a', 'b', 'c') == {'a': [1, 2], 'b': [1]}
    >>> assert fromiter([Simple(a=1), Simple(b=1), Simple(a=2)], ('a', 'b', ), 'c') == {'a': [1, 2], 'b': [1]}
    >>> assert fromiter([Simple(a=1), Simple(b=1), Simple(a=2)], 'a b c') == {'a': [1, 2], 'b': [1]}

    Args:
        data: object.
        *args: attributes.

    Returns:
        Tuple
    """
    value = {k: [getattr(C, k) for C in data if N[k].has(C)] for i in args for k in toiter(i)}
    return {k: v for k, v in value.items() if v}


def funcdispatch(func):
    """
    Decorator for adding dispatch functionality for functions.

    Similar to :py:func:`functools.singledispatch`, but for functions. This
    decorator allows for a single function name to be used for two different implementations.

    Args:
        func: Synchronous function to create a dispatch with.

    Example:

        .. code-block:: python

            from bapy import funcdispatch
            import asyncio

            @funcdispatch(
            def func():
                return True

            @func.register
            async def _():
                return False

            async def main():
                print(func())          # >>> True
                print(await func())    # >>> False

            asyncio.run(main())
    """
    funcs = {True: lambda x: x, False: lambda x: x}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # _ = wrapper.__qualname__  # To have __qualname__ in LOG:
        c = Stack()
        # ic(c.context)
        # ic(Call(index=1).function, func, c.sync, c.file, c.fileframe, c.code, c.line, c.filesys, c.func, c.id,
        #    c.function, c.child)
        # print()
        return funcs[not c[1].coro](*args, **kwargs)

    def register(f: Callable) -> None:
        funcs[not Is(f).coro] = f

    wrapper.register = register
    wrapper.register(func)
    return wrapper


def get(data, *args, default=None, one=True, recursive=False, with_keys=False):
    """
    Get value of name in Mutabble Mapping/GetType or object

    Examples:
        >>> get(dict(a=1), 'a')
        1
        >>> get(dict(a=1), 'b')
        >>> get(dict(a=1), 'b', default=2)
        2
        >>> get(dict, '__module__')
        'builtins'
        >>> get(dict, '__file__')

    Args:
        data: MutabbleMapping/GetType to get value.
        *args: keys (default: ('name')).
        default: default value (default: None).
        with_keys: return dict names and values or values (default: False).
        one: return [0] if len == 1 and one instead of list (default: True).
        recursive: recursivily for MutableMapping (default: False).

    Returns:
        Value for key.
    """

    def rv(items):
        if recursive and with_keys:
            items = {key: value[0] if len(value) == 1 and one else value for key, value in items}
        if with_keys:
            return items
        return list(r)[0] if len(r := items.values()) == 1 and one else list(r)

    args = args or ('name',)
    es = Is(data)
    if recursive and not es.mm:
        # TODO: to_vars() empty
        # data = to_vars()
        pass
    if es.mm and recursive:
        return rv(collections.defaultdict(
            list, {k: v for arg in args for k, v in _nested_lookup(arg, data, with_keys=with_keys)}))
    elif es.mm:
        return rv({arg: data.get(arg, default) for arg in args})

    return rv({attr: getattr(data, attr, default) for attr in args})


def getcls(data): return data if istype(data) else data.__class__


def getf(data, name, default=None):
    """
    Get value from: FrameInfo, FrameType, MutableMapping, TracebackType and object.

    Use :class:`rc.Es.get` for real names.

    Args:
        data: object.
        name: attribute or key name.
        default: default.

    Returns:
        Value.
    """
    name = enumvalue(name)
    i = Is(data)
    if name in [N.FILE, N.filename]:
        return sourcepath(data)
    if i.frameinfo:
        if name in [N.NAME, N.co_name, N.function]:
            return data.function
        if name in [N.lineno, N.f_lineno, N.tb_lineno]:
            return data.lineno
        if name in [N.f_globals, N.globals]:
            return data.frame.f_globals
        if name in [N.f_locals, N.locals]:
            return data.frame.f_locals
        if name in [N.frame, N.tb_frame]:
            return data.frame
        if name == N.vars:
            return data.frame.f_globals | data.frame.f_locals
        if name in [N.CODE, N.f_code]:
            return data.frame.f_code
        if name in [N.f_back, N.tb_next]:
            return data.frame.f_back
        if name == N.index:
            return data.index
        if name == N.code_context:
            return data.code_context
        if name in [N.FILE, N.filename]:
            return sourcepath(data)
        return getf(data.frame.f_globals | data.frame.f_locals, name=name, default=default)
    elif i.frametype:
        if name in [N.NAME, N.co_name, N.function]:
            return data.f_code.co_name
        if name in [N.lineno, N.f_lineno, N.tb_lineno]:
            return data.f_lineno
        if name in [N.f_globals, N.globals]:
            return data.f_globals
        if name in [N.f_locals, N.locals]:
            return data.f_locals
        if name in [N.frame, N.tb_frame]:
            return data
        if name == N.vars:
            return data.f_globals | data.f_locals
        if name in [N.CODE, N.f_code]:
            return data.f_code
        if name in [N.f_back, N.tb_next]:
            return data.f_back
        if name in [N.FILE, N.filename]:
            return sourcepath(data)
        return getf(data.f_globals | data.f_locals, name=name, default=default)
    elif i.tracebacktype:
        if name in [N.NAME, N.co_name, N.function]:
            return data.tb_frame.f_code.co_name
        if name in [N.lineno, N.f_lineno, N.tb_lineno]:
            return data.tb_lineno
        if name in [N.f_globals, N.globals]:
            return data.tb_frame.f_globals
        if name in [N.f_locals, N.locals]:
            return data.tb_frame.f_locals
        if name in [N.frame, N.tb_frame]:
            return data.tb_frame
        if name == N.vars:
            return data.tb_frame.f_globals | data.tb_frame.f_locals
        if name in [N.CODE, N.f_code]:
            return data.tb_frame.f_code
        if name in [N.f_back, N.tb_next]:
            return data.tb_next
        if name in [N.FILE, N.filename]:
            return sourcepath(data)
        return getf(data.tb_frame.f_globals | data.tb_frame.f_locals, name=name, default=default)
    # MutableMapping and object
    return hasget(data=data, name=name, default=default)


def getm(data, name='name'):
    if isinstance(data, MutableMapping):
        return data.get(name, MISSING)
    return data.__getattribute__(name) if hasattr(data, name) else MISSING


def getnostr(data, attr='value'):
    """
    Get attr if data is not str.

    Examples:
        >>> simple = Simple(value=1)
        >>> assert getnostr(simple) == 1
        >>> assert getnostr(simple, None) == simple
        >>> assert getnostr('test') == 'test'

    Args:
        data: object.
        attr: attribute name (default: 'value').

    Returns:
        Attr value if not str.
    """
    return (data if isinstance(data, str) else getattr(data, attr)) if attr else data


def getprops(data):
    is_type = isinstance(data, type)
    cls = data if is_type else data.__class__
    return {i: obj if is_type else getattr(data, i, Missing)
            for i in dir(cls) if (obj := isinstance(getattr(cls, i), property)) and not iscoro(obj)}


def getset(data, name, default=None, setvalue=True):
    """
    Sets attribute with default if it does not exists and returns value.

    Examples:
        >>> class D: pass
        >>> class Slots: __slots__ = ('a', )
        >>>
        >>> d = D()
        >>> s = Slots()
        >>> getset(d, 'a')
        >>> # noinspection PyUnresolvedReferences
        >>> d.a
        >>> getset(s, 'a')
        >>> s.a
        >>>
        >>> d = D()
        >>> s = Slots()
        >>> getset(d, 'a', 2)
        2
        >>> # noinspection PyUnresolvedReferences
        >>> d.a
        2
        >>> getset(s, 'a', 2)
        2
        >>> s.a
        2
        >>>
        >>> class D: a = 1
        >>> class Slots:
        ...     __slots__ = ('a', )
        ...     def __init__(self):
        ...         self.a = 1
        >>> d = D()
        >>> s = Slots()
        >>> getset(d, 'a')
        1
        >>> getset(s, 'a')
        1
        >>> getset(d, 'a', 2)
        1
        >>> getset(s, 'a', 2)
        1

    Args:
        data: object.
        name: attr name.
        default: default value (default: None)
        setvalue: setattr in object if AttributeError (default: True).

    Returns:
        Attribute value or sets default value and returns.
    """
    try:
        return object.__getattribute__(data, name)
    except AttributeError:
        if setvalue:
            object.__setattr__(data, name, default)
            return object.__getattribute__(data, name)
        return default


def getsetstate(data, state=None):
    """
    Values for :class:`rc.BaseState` methods:
        - :meth:`rc.BaseState.__getstate__`: (pickle) when state=None.
        - :meth:`rc.BaseState.__setstate__`: (unpickle) when state.

    Examples:
        >>> from bapy import MISSING
        >>> class Test:
        ...     __slots__ = ('attribute', )
        ...     __ignore_state__ = ()
        >>>
        >>> test = Test()
        >>> e = Obj(test)
        >>> status = getsetstate(test)
        >>> status
        {'attribute': <MISSING>}
        >>> reconstruct = getsetstate(test, status)
        >>> reconstruct  # doctest: +ELLIPSIS
        <....Test object at 0x...>
        >>> reconstruct == getsetstate(test, status)
        True
        >>>
        >>> test.attribute = 1
        >>> new = Is(test)
        >>> status = getsetstate(test)
        >>> status
        {'attribute': 1}
        >>> reconstruct == getsetstate(test, status)
        True
        >>> reconstruct.attribute
        1

    Args:
        data: object.
        state: dict to restore object.

    Returns:
        State dict (pickle) or restored object from state dict (unpickle).
    """
    if state is None:
        return Obj(data).state()
    for key, value in state.items():
        data.__setattr__(key, value)
    return data


def has(data, name):
    """
    Name in Data.

    Args:
        data: object.
        name: attribute name.

    Returns:
        True if Name in Data.
    """
    return name in data if isinstance(data, Container) else hasattr(data, name)


def hasget(data, name, default=None):
    """
    Return Attribute Value if Has Attribute.

    Args:
        data: object.
        name: attribute name.
        default: fallback (default: None)

    Returns:
        Attribute Value.
    """
    if isinstance(data, (MutableMapping, types.MappingProxyType)):
        if name in data:
            return data[name]
        return default
    if hasattr(data, name):
        return getattr(data, name)
    return default


def hasgetany(data, name, default=None):
    """
    Return Attribute Value if Has Attribute in instance or class.

    Args:
        data: object.
        name: attribute name.
        default: fallback (default: None)

    Returns:
        Attribute Value.
    """
    if hasattr(data, name):
        return getattr(data, name)
    if not isinstance(data, type):
        if hasattr(data.__class__, name):
            return getattr(data.__class__, name)
    return default


def importname(data):
    """
    >>> test = dict()
    >>> assert importname(test) == 'bapy.__init__.test'
    >>> assert importname(type(25)) == 'builtins.int'
    >>> assert importname(type(None)) == 'builtins.NoneType'
    >>> assert importname(False.__class__) == 'builtins.bool'
    >>> assert importname(AttributeError) == 'builtins.AttributeError'
    """
    i = Is(data)
    if i.moduletype:
        return i.__name__
    cls = i.cls

    def rv(m, n): return f'{m}.{n}'

    if i.type:
        return rv(cls.__module__, cls.__qualname__)
    elif (module := hasget(data, N.MODULE)) and (name := hasget(data, N.QUALNAME, hasget(data, N.NAME))):
        return rv(module, name)
    s = inspect.stack()[1]
    module = Path(s.frame.f_globals.get(N.FILE)).to_modules()
    name = objname(stack=s)
    return rv(module, name)


def indict(data, items=None, **kwargs):
    """
    All item/kwargs pairs in flat dict.

    >>> assert indict(BUILTIN, {'iter': iter}, credits=credits) is True
    >>> assert indict(BUILTIN, {'iter': 'fake'}) is False
    >>> assert indict(BUILTIN, {'iter': iter}, credits='fake') is False
    >>> assert indict(BUILTIN, credits='fake') is False

    Args:
        data: dict to search.
        items: key/value pairs.
        **kwargs: key/value pairs.

    Returns:
        True if all pairs in dict.
    """
    return all(map(lambda x: x[0] in data and x[1] == data[x[0]], ((items if items else {}) | kwargs).items()))


def indictr(data, items=None, **kwargs):
    """
    Is Item in Dict?.

    Examples:
        >>> from bapy import indictr, N
        >>> indictr(globals(), {'True': True, 'False': False})
        True
        >>> indictr(globals()['__builtins__'], {'True': True, 'False': False}, __name__='builtins')
        True
        >>> indictr(globals(), {'True': True, 'False': False}, __name__='builtins')
        True
        >>> Is(dict(__name__='builtins')).builtin
        True

    Args:
        data: Dict
        items: Dict with key and values for not str keys (default: None)
        **kwargs: keys and values.

    Raises:
        TypeError: item must be a MutabbleMapping.

    Returns:
        True if items in Dict.
    """
    if isinstance(data, MutableMapping):
        if items and not isinstance(items, MutableMapping):
            raise TypeError(f'{items=} must be a MutabbleMapping')
        if d := (items if items else dict()) | kwargs:
            for key, value in d.items():
                values = nested_lookup.nested_lookup(key, data)
                if not values or value not in values:
                    return False
            return True
    return False


def initimps(path=__file__, relative=True):
    """
    Creates __init__.py and __init__.pyi for a package.

    Args:
        path: file or dir.
        relative: use relative imports in __init__.py

    Returns:
        None.
    """
    relative = '.' if relative else ''
    path = Path.to_parent(path)
    modules = tuple(p.to_module for p in iter(path.glob(PSuffix.PY())) if p != INIT_PY)
    parent = Path(__file__).parent
    a = ",\n".join(sorted([f"    '{item}'" for module in modules for item in module.__all__]))
    header = f'#!/usr/bin/env python3.9\n# -*- coding: utf-8 -*-\n"""{path.name.capitalize()} Package."""\n'
    alls = f'__all__ = (\n{a}\n)\n'
    imps = '\n'.join(sorted(
        [f'from {relative}{module.__name__} import {item} as {item}' for module in modules for item in module.__all__]))
    close = '__all__: tuple[str, ...] = ...'
    init = '__init__.py'
    initi = f'{init}i'
    py = header + '\n' + alls + '\n' + imps + '\n'
    pyi = imps + '\n' + close + '\n'
    (parent / init).write_text(py)
    (parent / initi).write_text(pyi)
    return modules, py, pyi


def iscoro(data): return any([inspect.isasyncgen(data), inspect.isasyncgenfunction(data),
                              asyncio.iscoroutine(data), inspect.iscoroutinefunction(data)])


def iseven(number): return Is(number).even


def istype(data): return isinstance(data, type)


def join_newline(data): return NEWLINE.join(data)


@app.command()
def localbin(path=__file__):
    """
    Copy files in directory/path to /usr/local/bin (except __init__.py).

    Args:
        path: source directory or file.

    Returns:
        None
    """
    path = pathlib.Path(path)
    path = (path.parent / N.scripts) if path.is_file() else path

    subprocess.run(f'find {pathlib.Path(path)} -mindepth 1 -maxdepth 1 -type f ! -name ".*" ! -name "{INIT_PY}" '
                   f'! -name "_init.py" -exec {WITHSUDO} chmod +x "{CURLYBRACKETS}" \; -print | '
                   f'xargs -I {CURLYBRACKETS} {WITHSUDO} cp "{CURLYBRACKETS}" {LOCALBIN}', shell=True, check=True)


def map_reduce_even(iterable): return more_itertools.map_reduce(iterable, keyfunc=iseven)


def map_with_args(data, func, /, *args, pred=lambda x: True if x else False, split=' ', **kwargs):
    """
    Apply pred/filter to data and map with args and kwargs.

    Examples:
        >>> # noinspection PyUnresolvedReferences
        >>> def f(i, *ar, **kw):
        ...     return f'{i}: {[a(i) for a in ar]}, {", ".join([f"{k}: {v(i)}" for k, v in kw.items()])}'
        >>> map_with_args('0.1.2', f, int, list, pred=lambda x: x != '0', split='.', int=int, str=str)
        ["1: [1, ['1']], int: 1, str: 1", "2: [2, ['2']], int: 2, str: 2"]

    Args:
        data: data.
        func: final function to map.
        *args: args to final map function.
        pred: pred to filter data before map.
        split: split for data str.
        **kwargs: kwargs to final map function.

    Returns:
        List with results.
    """
    return [func(item, *args, **kwargs) for item in yield_if(data, pred=pred, split=split)]


def missing(data): return data == MISSING


def newprop(name=None, default=None):
    """
    Get a new property with getter, setter and deleter.

    Examples:
        >>> class Test:
        ...     prop = newprop()
        ...     callable = newprop(default=str)
        >>>
        >>> test = Test()
        >>> '_prop' not in vars(test)
        True
        >>> test.prop
        >>> '_prop' in vars(test)
        True
        >>> test.prop
        >>> test.prop = 2
        >>> test.prop
        2
        >>> del test.prop
        >>> '_prop' in vars(test)
        False
        >>> test.prop
        >>> '_callable' not in vars(test)
        True
        >>> test.callable  # doctest: +ELLIPSIS
        '....Test object at 0x...>'
        >>> '_callable' in vars(test)
        True
        >>> test.callable  # doctest: +ELLIPSIS
        '....Test object at 0x...>'
        >>> test.callable = 2
        >>> test.callable
        2
        >>> del test.callable
        >>> '_callable' in vars(test)
        False
        >>> test.callable  # doctest: +ELLIPSIS
        '....Test object at 0x...>'

    Args:
        name: property name (attribute name: _name). :func:' varname`is used if no name (default: varname())
        default: default for getter if attribute is not defined.
            Could be a callable/partial that will be called with self (default: None)

    Returns:
        Property.
    """
    name = f'_{name if name else varname()}'
    return property(
        lambda self:
        getset(self, name, default=default(self) if Is(default).instance(Callable, functools.partial) else default),
        lambda self, value: self.__setattr__(name, value),
        lambda self: self.__delattr__(name)
    )


def noexc(func, *args, default_=None, exc_=Exception, **kwargs):
    """
    Execute function suppressing exceptions.

    Examples:
        >>> noexc(dict(a=1).pop, 'b', default_=2, exc_=KeyError)
        2

    Args:
        func: callable.
        *args: args.
        default_: default value if exception is raised.
        exc_: exception or exceptions.
        **kwargs: kwargs.

    Returns:
        Any: Function return.
    """
    try:
        return func(*args, **kwargs)
    except exc_:
        return default_


def notmissing(data): return not (data == MISSING)


def notstart(name: str, start='__'): return not name.startswith(start)


# noinspection PyUnusedLocal
def objname(data=None, stack=1):
    """
    Object name.

    >>> a = dict()
    >>> assert objname(a) == 'a'
    >>> def middle(var): return objname(stack=inspect.stack()[1])
    >>> assert middle(a) == 'a'

    Args:
        data: object.
        stack: stack index or FrameInfo.

    Returns:
        Object name.
    """
    finfo = Is(stack).frameinfo
    s = inspect.stack()[1]
    stack = stack if finfo else s
    function = s.function if finfo else objname.__name__
    return re.sub('(\)|,\)).*$', '', re.sub(f'^.*{function}\(', '', textwrap.dedent(
        stack.code_context[0]).replace('\n', ')')).removesuffix('\)'))


def prefixed(name: str) -> str:
    try:
        return f'{name.upper()}_'
    except AttributeError:
        pass


def pretty_install(cons=console, expand=True): return rich.pretty.install(cons, expand_all=expand)


def pypifree(name, stdout=False):
    """
    Pypi name available.

    Examples:
        >>> assert pypifree('common') is False
        >>> assert pypifree('sdsdsdsd') is True

    Args:
        name: package.
        stdout: stdout.

    Returns:
        bool: True if available.
    """
    r = requests.get(f'https://pypi.org/pypi/{name}/json')

    if r:
        if stdout:
            print(False)
        return False
    else:
        if stdout:
            print(True)
        return True


def reprcls(data=None, attrs=(), kw=True, line=False, module=False, sort=False, **kwargs):
    """
    Add Module and Class to Repr.

    Examples:
        >>> s = Simple(); s.a = 1
        >>> assert reprcls(s, 'a') == 'SimpleNamespace(a=1)'
        >>> assert reprcls(Simple(a=1, b=2)) == 'SimpleNamespace(a=1, b=2)'


    Args:
        data: data or kwargs.
        attrs: attributes to getattr from data or repr/kw
        kw: call reprkw or use attrs string.
        line: newline after each pair.
        module: include module name.
        sort: sort keys.
        **kwargs: data or kwargs.

    Returns:
        Repr.
    """
    new = NEWLINE if line else ''
    mod = f'{data.__class__.__module__}.' if data.__class__.__module__ and module else ''
    rep = reprkw(data=data, attrs=attrs, line=line, sort=sort, **kwargs) if kw else attrs
    return f'{mod}{data.__class__.__name__}({new}{rep}{new})'


def reprkw(data=None, attrs=(), line=False, sort=False, **kwargs):
    """
    Render ``data`` or ``kwargs`` or data ``attrs`` as a list of ``Key=repr(Value), `` pairs.

    Examples:
        >>> rv1 = reprkw(b=1, a='a')
        >>> rv2 = reprkw(line=True, b=1, a='a')
        >>> rv3 = reprkw(sort=True, b=1, a='a')
        >>> rv4 = reprkw(line=True, sort=True, b=1, a='a')
        >>> rv1, rv2, rv3, rv4
        ("b=1, a='a'", "    b=1,\\n    a='a'", "a='a', b=1", "    a='a',\\n    b=1")
        >>> assert reprkw(dict(b=1, a='a'), attrs='b a') == 'b=<MISSING>, a=<MISSING>'
        >>> assert reprkw(Simple(b=1, a='a'), attrs='b a') == rv1
        >>> assert reprkw(Simple(b=1, a='a'), attrs='b a', line=True) == rv2
        >>> assert reprkw(Simple(b=1, a='a'), attrs='b a', sort=True) == rv3
        >>> assert reprkw(Simple(b=1, a='a'), attrs='b a', line=True, sort=True) == rv4
        >>> s = Simple(); s.a = 1
        >>> assert reprkw(s, 'a') == 'a=1'
        >>> assert reprkw(s, ('a', )) == 'a=1'
        >>>
        >>> assert reprkw(Simple(a=1, b=2)) == 'a=1, b=2'

    Args:
        data: data or kwargs.
        attrs: attributes to getattr from data.
        line: newline and 4 spaces after each pair.
        sort: sort keys.
        **kwargs: data or kwargs.

    Returns:
        Repr ``Key=repr(Value)`` pairs
    """
    if not (attrs or kwargs):
        kwargs = Obj(data).repr()
    elif not kwargs and attrs:
        attrs = toiter(attrs)

    data = kwargs or {i: getattr(data, i, MISSING) for i in attrs}
    return f',{NEWLINE if line else " "}'.join(f'{"    " if line else ""}{k}='
                                               f'{repr(v)}' for k, v in (dict_sort(data) if sort else data).items())


@decorator.decorator
def runwarning(func, *args, **kwargs):
    with warnings.catch_warnings(record=False):
        warnings.filterwarnings('ignore', category=RuntimeWarning)
        warnings.showwarning = lambda *_args, **_kwargs: None
        rv = func(*args, **kwargs)
        return rv


def sourcepath(data):
    """
    Get path of object.

    Examples:
        >>> import asyncio
        >>> import bapy.__init__
        >>>
        >>> frameinfo = inspect.stack()[0]
        >>> globs_locs = (frameinfo.frame.f_globals | frameinfo.frame.f_locals).copy()
        >>> assert sourcepath(sourcepath) == Path(bapy.__init__.__file__)
        >>> assert sourcepath(asyncio.__file__) == Path(asyncio.__file__)
        >>> assert sourcepath(allin) == Path(bapy.__init__.__file__)
        >>> assert sourcepath(dict(a=1)) == Path("{'a': 1}")

    Returns:
        Path.
    """
    i = Is(data)
    if i.mm:
        f = data.get(N.FILE)
    elif i.frameinfo:
        f = data.filename
    else:
        try:
            f = inspect.getsourcefile(data) or inspect.getfile(data)
        except TypeError:
            f = None
    return Path(f or str(data))


def sourcevars():
    rv = {re.sub('_', '', i).lower(): i for i in (N.FILE, N.NAME, N.PACKAGE, N.PYPI, N.REPO, N.SPEC, N.SOURCE,)}
    return {i: rv[i] for i in sorted(rv)}


def splitsep(sep='_'): return dict(sep=sep) if sep else dict()


def to_camel(text, replace=True):
    """
    Convert to Camel

    Examples:
        >>> to_camel(N.IGNORE_ATTR)
        'IgnoreAttr'
        >>> to_camel(N.IGNORE_ATTR, replace=False)
        '__Ignore_Attr__'

    Args:
        text: text to convert.
        replace: remove '_'  (default: True)

    Returns:
        Camel text.
    """
    rv = ''.join(map(str.title, toiter(text, '_')))
    return rv.replace('_', '') if replace else rv


def toiter(data, always=False, split=' '):
    """
    To iter.

    Examples:
        >>> assert toiter('test1') == ['test1']
        >>> assert toiter('test1 test2') == ['test1', 'test2']
        >>> assert toiter({'a': 1}) == {'a': 1}
        >>> assert toiter({'a': 1}, always=True) == [{'a': 1}]
        >>> assert toiter('test1.test2') == ['test1.test2']
        >>> assert toiter('test1.test2', split='.') == ['test1', 'test2']

    Args:
        data: data.
        always: return any iterable into a list.
        split: split for str.

    Returns:
        Iterable.
    """
    if isinstance(data, str):
        data = data.split(split)
    elif not isinstance(data, Iterable) or always:
        data = [data]
    return data


def tomodules(data, suffix=True):
    """
    Converts Iterable to A.B.C

    >>> assert tomodules('a b c') == 'a.b.c'
    >>> assert tomodules('a b c.py') == 'a.b.c'
    >>> assert tomodules('a/b/c.py') == 'a.b.c'
    >>> assert tomodules(['a', 'b', 'c.py']) == 'a.b.c'
    >>> assert tomodules('a/b/c.py', suffix=False) == 'a.b.c.py'
    >>> assert tomodules(['a', 'b', 'c.py'], suffix=False) == 'a.b.c.py'

    Args:
        data: iterable.
        suffix: remove suffix.

    Returns:
        String A.B.C
    """
    split = '/' if Is(data).str and '/' in data else ' '
    return '.'.join(i.removesuffix(Path(i).suffix if suffix else '') for i in toiter(data, split=split))


def traceback_install(cons=console, extra=5, locs=True): return rich.traceback.install(
    console=cons, extra_lines=extra, show_locals=locs)


def varname(index=2, lower=True, prefix=None, sep='_'):
    """
    Caller var name.

    Examples:
        >>> from dataclasses import dataclass
        >>> def function() -> str:
        ...     return varname()
        >>>
        >>> class ClassTest:
        ...     def __init__(self):
        ...         self.name = varname()
        ...
        ...     @property
        ...     def prop(self):
        ...         return varname()
        ...
        ...     # noinspection PyMethodMayBeStatic
        ...     def method(self):
        ...         return varname()
        >>>
        >>> @dataclass
        ... class DataClassTest:
        ...     def __post_init__(self):
        ...         self.name = varname()
        >>>
        >>> name = varname(1)
        >>> Function = function()
        >>> classtest = ClassTest()
        >>> method = classtest.method()
        >>> prop = classtest.prop
        >>> dataclasstest = DataClassTest()
        >>>
        >>> def test_var():
        ...     assert name == 'name'
        >>>
        >>> def test_function():
        ...     assert Function == function.__name__.lower()
        >>>
        >>> def test_class():
        ...     assert classtest.name == ClassTest.__name__.lower()
        >>>
        >>> def test_method():
        ...     assert classtest.method() == ClassTest.__name__.lower()
        ...     assert method == 'method'
        >>> def test_property():
        ...     assert classtest.prop == ClassTest.__name__.lower()
        ...     assert prop == 'prop'
        >>> def test_dataclass():
        ...     assert dataclasstest.name == DataClassTest.__name__.lower()

        .. code-block:: python

            class A:

                def __init__(self):

                    self.instance = varname()

            a = A()

            var = varname(1)


    Args:
        index: index.
        lower: lower.
        prefix: prefix to add.
        sep: split.

    Returns:
        Optional[str]: Var name.
    """
    with contextlib.suppress(IndexError, KeyError):
        _stack = inspect.stack()
        func = _stack[index - 1].function
        index = index + 1 if func == N.POST_INIT else index
        if line := textwrap.dedent(_stack[index].code_context[0]):
            if var := re.sub(f'(.| ){func}.*', str(), line.split(' = ')[0].replace('assert ', str()).split(' ')[0]):
                return (prefix if prefix else '') + (var.lower() if lower else var).split(**splitsep(sep))[0]


@app.command(name='version')
def _version():
    """Version"""
    print(__version__)


def yield_if(data, pred=lambda x: True if x else False, split=' ', apply=None):
    """
    Yield value if condition is met and apply function if predicate.

    Examples:
        >>> assert list(yield_if([True, None])) == [True]
        >>> assert list(yield_if('test1.test2', pred=lambda x: x.endswith('2'), split='.')) == ['test2']
        >>> assert list(yield_if('test1.test2', pred=lambda x: x.endswith('2'), split='.', \
        apply=lambda x: x.removeprefix('test'))) == ['2']
        >>> assert list(yield_if('test1.test2', pred=lambda x: x.endswith('2'), split='.', \
        apply=(lambda x: x.removeprefix('test'), lambda x: int(x)))) == [2]


    Args:
        data: data
        pred: predicate (default: if value)
        split: split char for str.
        apply: functions to apply if predicate is met.

    Returns:
        Yield values if condition is met and apply functions if provided.
    """
    for item in toiter(data, split=split):
        if pred(item):
            if apply:
                for func in toiter(apply):
                    item = func(item)
            yield item


def yield_last(data, split=' '):
    """
    Yield value if condition is met and apply function if predicate.

    Examples:
        >>> assert list(yield_last([True, None])) == [(False, True, None), (True, None, None)]
        >>> assert list(yield_last('first last')) == [(False, 'first', None), (True, 'last', None)]
        >>> assert list(yield_last('first.last', split='.')) == [(False, 'first', None), (True, 'last', None)]
        >>> assert list(yield_last(dict(first=1, last=2))) == [(False, 'first', 1), (True, 'last', 2)]


    Args:
        data: data.
        split: split char for str.

    Returns:
        Yield value and True when is the last item on iterable
    """
    data = toiter(data, split=split)
    mm = Is(data).mm
    total = len(data)
    count = 0
    for i in data:
        count += 1
        yield count == total, *(i, data.get(i) if mm else None,)


# EnumBase
@functools.total_ordering
class EnumBase(enum.Enum):
    """Enum Base Class."""

    def __call__(self):
        """Returns Value."""
        return self.value

    def __eq__(self, other):
        """
        Equal Using Enum Key and Enum Instance.

        Examples:
            >>> assert Access['field'] == Access.PUBLIC
            >>> assert Access['field'] is Access.PUBLIC
            >>> assert Access['field'] != '_field'
            >>> assert Access['_field'] == '_field'
            >>> assert Access['_field'] is not '_field'

        Returns:
            True if Enum Key or Enum Instance are equal to self.
        """
        try:
            rv = type(self)[other]
            return self._name_ == rv._name_ and self._value_ == rv._value_
        except KeyError:
            return False

    def __gt__(self, other):
        """
        Greater Than Using Enum Key and Enum Instance.

        Examples:
            >>> assert Access['field'] == Access.PUBLIC
            >>> assert Access['field'] > '_field'
            >>> assert Access['field'] > Access.ALL
            >>> assert Access['field'] >= 'field'
            >>> assert Access['field'] >= Access.PUBLIC
            >>> assert (Access['field'] < Access.ALL) is False
            >>> assert Access.PROTECTED >= Access.ALL
            >>> assert Access['field'] >= Access.ALL
            >>> assert Access['field'] >= '_field'

        Raises:
            TypeError: '>' not supported between instances of '{type(self)}' and '{type(rv)}'.

        Returns:
            True self (index/int) is greater than other Enum Key or Enum Instance.
        """
        try:
            rv = type(self)[other]
            if isinstance(rv, typing.SupportsInt):
                return self.__int__() > rv.__int__()
            raise TypeError(f"'>' not supported between instances of '{type(self)}' and '{type(rv)}'")
        except KeyError:
            raise TypeError(f"'>' not supported between instances of '{type(self)}' and '{type(other)}'")

    def __hash__(self): return hash(self._name_)

    def __int__(self):
        """
        int based on index to compare.

        Examples:
            >>> assert int(Access.PROTECTED) == 2

        Returns:
            Index.
        """
        return list(Access.__members__.values()).index(self)

    def _generate_next_value_(self, start, count, last_values): return self.lower() if isinstance(self, str) else self

    @classmethod
    def asdict(cls): return {key: value._value_ for key, value in cls.__members__.items()}

    @classmethod
    def attrs(cls): return list(cls.__members__)

    @classmethod
    def default(cls): return cls._member_map_[cls._member_names_[0]]

    @classmethod
    def default_attr(cls): return cls.attrs()[0]

    @classmethod
    def default_dict(cls): return {cls.default_attr(): cls.default_value()}

    @classmethod
    def default_value(cls): return cls[cls.default_attr()]

    @property
    def describe(self):
        """
        Returns:
            tuple:
        """
        # self is the member here
        return self.name, self()

    lower = property(lambda self: self.name.lower())

    @classmethod
    def values(cls): return list(cls.asdict().values())


EnumBaseAlias = Alias(EnumBase, 0, name=EnumBase.__name__)


class EnumBaseMeta(enum.EnumMeta):
    def __getitem__(cls, item):
        """
        Access Instance Value:
            - If str and is enum key: returns value.
            - If str and not enum key: returns value base on re.compile.
            - If Access Instance: returns item.

        Examples:
            >>> assert (Access[str()], Access[Access.PROTECTED], Access['__name__'], Access['_name__'], \
            Access['name__'], ) == (None, Access.PROTECTED, Access.PRIVATE, Access.PROTECTED, Access.PUBLIC)
            >>> assert Access['PROTECTED'] == Access.PROTECTED
            >>> Access[dict()] # doctest: +IGNORE_EXCEPTION_DETAIL, +ELLIPSIS
            Traceback (most recent call last):
            KeyError: "{} not in ...

        Raises:
            KeyError: item not in cls.__members__.

        Args:
            item: Access key, string to run re.compile or Access Instance.

        Returns:
            Access Instance.
        """
        if isinstance(item, str):
            if item == '':
                return
            if item in cls._member_map_:
                return cls._member_map_[item]
            for key in list(cls._member_map_.keys())[1:]:
                value = cls._member_map_[key]
                v = value()
                if N.search.has(v) and bool(v.search(item)):
                    return value
            raise KeyError(f'{item} not in {cls._member_map_}')
        elif isinstance(item, enum.Enum):
            return item
        else:
            for value in cls._member_map_.values():
                if value() == item:
                    return item
        raise KeyError(f'{item} not in {cls._member_map_}')

    __class_getitem__ = __getitem__


# Classes
class Access(EnumBase, metaclass=EnumBaseMeta):
    """Access Attributes Enum Class."""
    ALL = re.compile('.')
    PRIVATE = re.compile('^__.*')
    PROTECTED = re.compile('^_(?!_).*$')
    PUBLIC = re.compile('^(?!_)..*$')

    @classmethod
    def classify(cls, *args, keys=False, **kwargs):
        """
        Classify args or kwargs based on data access.

        Examples:
            >>> import bapy.data.cls
            >>> a = \
                Access.classify(**dict(map(lambda x: (x.name, x, ), \
                inspect.classify_class_attrs(bapy.data.cls.MroAsync))))
            >>> n = '__class__'
            >>> assert n in a.all and n in a.private and n not in a.protected and n not in a.public
            >>> n = bapy.data.cls.MroAsync._staticmethod
            >>> assert n in a.all and n not in a.private and n in a.protected and n not in a.public
            >>> n = bapy.data.cls.MroAsync.staticmethod.__name__
            >>> assert n in a.all and n not in a.private and n not in a.protected and n in a.public
            >>>
            >>> a = Access.classify(\
                **dict(map(lambda x: (x.name, x, ), inspect.classify_class_attrs(bapy.data.cls.MroAsync))), keys=True)
            >>> n = '__class__'
            >>> assert n in a.all and n in a.private and n not in a.protected and n not in a.public
            >>> assert a.private[n].name == n
            >>> n = bapy.data.cls.MroAsync._staticmethod
            >>> assert n in a.all and n not in a.private and n in a.protected and n not in a.public
            >>> assert a.protected[n].name == n
            >>> n = bapy.data.cls.MroAsync.staticmethod.__name__
            >>> assert n in a.all and n not in a.private and n not in a.protected and n in a.public
            >>> assert a.public[n].name == n

        Args:
            *args: str iterable.
            keys: include keys if kwargs so return dict or list with kwargs.values().
            **kwargs: dict with keys to check and values

        Raises:
            TypeError('args or kwargs not both')

        Returns:
            AccessEnumMembers.
        """
        if args and kwargs:
            raise TypeError('args or kwargs not both')
        rv: collections.defaultdict[Access, typing.Union[dict, list]] = \
            collections.defaultdict(dict if keys and kwargs else list, dict())
        for name in args or kwargs:
            if value := cls[name]:
                rv[value].update({name: kwargs.get(name)}) if keys and kwargs else rv[value].append(name)
                rv[cls.ALL].update({name: kwargs.get(name)}) if keys and kwargs else rv[cls.ALL].append(name)
        return AccessEnumMembers(all=rv[cls.ALL], private=rv[cls.PRIVATE], protected=rv[cls.PROTECTED],
                                 public=rv[cls.PUBLIC])

    def include(self, name):
        """
        Include Key.

        Examples:
            >>> assert (Access.ALL.include(str()), Access.PRIVATE.include(str()), Access.PROTECTED.include(str()), \
            Access.PUBLIC.include(str())) == (None, None, None, None)
            >>> assert (Access.ALL.include('__name__'), Access.PRIVATE.include('__name__'), \
            Access.PROTECTED.include('__name__'), Access.PUBLIC.include('__name__')) == (True, True, False, False)
            >>> assert (Access.ALL.include('_name__'), Access.PRIVATE.include('_name__'), \
            Access.PROTECTED.include('_name__'), Access.PUBLIC.include('_name__')) == (True, True, True, False)
            >>> assert (Access.ALL.include('name__'), Access.PRIVATE.include('name__'), \
            Access.PROTECTED.include('name__'), Access.PUBLIC.include('name__')) == (True, True, True, True)

        Args:
            name: name.

        Returns:
            True if key to be included.
        """
        if name:
            return type(self)[name] >= self


AccessEnumMembers = collections.namedtuple('AccessEnumMembers', 'all private protected public')


class AllAttr(metaclass=abc.ABCMeta):
    """ __all__ Type. """
    __slots__ = ()
    __all__ = TupleStr

    @classmethod
    def __subclasshook__(cls, C):
        if cls is AllAttr:
            return N.ALL.has(C)
        return NotImplemented


Annotation = collections.namedtuple('Annotation', 'any args classvar cls default final hint initvar literal '
                                                  'name optional origin union')


class AnnotationsAttr(metaclass=abc.ABCMeta):
    """
    Annotations Type.

    Examples:
        >>> named = collections.namedtuple('named', 'a', defaults=('a', ))
        >>> from typing import NamedTuple
        >>> Named = NamedTuple('Named', a=str)
        >>>
        >>> assert Is(named).annotationsattr == False
        >>> assert Is(named()).annotationsattr == False
        >>>
        >>> assert Is(Named).annotationsattr == True
        >>> assert Is(Named(a='a')).annotationsattr == True
    """
    __slots__ = ()
    __annotations__ = dict()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is AnnotationsAttr:
            return N.ANNOTATIONS.has(C)
        return NotImplemented


class AsDictMethod(metaclass=abc.ABCMeta):
    """
    AsDict Method Support (Class, Static and Method).

    Examples:
        >>> class AsDictClass: asdict = classmethod(lambda cls, *args, **kwargs: dict())
        >>> class AsDictM: asdict = lambda self, *args, **kwargs: dict()
        >>> class AsDictP: asdict = property(lambda self: dict())
        >>> class AsDictStatic: asdict = staticmethod(lambda cls, *args, **kwargs: dict())
        >>>
        >>> c = AsDictClass()
        >>> m = AsDictM()
        >>> p = AsDictP()
        >>> s = AsDictStatic()
        >>>
        >>> assert Is(AsDictClass).asdictmethod == True
        >>> assert Is(c).asdictmethod == True
        >>>
        >>> assert Is(AsDictM).asdictmethod == True
        >>> assert Is(m).asdictmethod == True
        >>>
        >>> assert Is(AsDictP).asdictmethod == False
        >>> assert Is(p).asdictmethod == False
        >>>
        >>> assert Is(AsDictStatic).asdictmethod == True
        >>> assert Is(s).asdictmethod == True
    """

    @abc.abstractmethod
    def asdict(self, *args, **kwargs): pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is AsDictMethod:
            return callable(N.asdict.hasget(C))
        return NotImplemented


class AsDictProperty(metaclass=abc.ABCMeta):
    """
    AsDict Property Type.

    Examples:
        >>> class AsDictClass: asdict = classmethod(lambda cls, *args, **kwargs: dict())
        >>> class AsDictM: asdict = lambda self, *args, **kwargs: dict()
        >>> class AsDictP: asdict = property(lambda self: dict())
        >>> class AsDictStatic: asdict = staticmethod(lambda cls, *args, **kwargs: dict())
        >>>
        >>> c = AsDictClass()
        >>> m = AsDictM()
        >>> p = AsDictP()
        >>> s = AsDictStatic()
        >>>
        >>> assert Is(AsDictClass).asdictproperty == False
        >>> assert Is(c).asdictproperty == False
        >>>
        >>> assert Is(AsDictM).asdictproperty == False
        >>> assert Is(m).asdictproperty == False
        >>>
        >>> assert Is(AsDictP).asdictproperty == True
        >>> assert Is(p).asdictproperty == True
        >>>
        >>> assert Is(AsDictStatic).asdictproperty == False
        >>> assert Is(s).asdictproperty == False
    """

    @property
    @abc.abstractmethod
    def asdict(self):
        return dict()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is AsDictProperty:
            return isinstance(N.asdict.hasget(C), property)
        return NotImplemented


Attribute = collections.namedtuple('Attribute', 'defining i kind object qualname')


class BaseState:
    """
    Deepcopy and Pickle State Base Class.

    Examples:
        >>> from copy import deepcopy
        >>>
        >>> class Test(BaseState):
        ...     __slots__ = ('attribute', )
        ...     __state__ = ('attribute', )
        ...     def __init__(self): self.attribute = dict(a=1)
        >>>
        >>> test = Test()
        >>> test_copy = test
        >>> test_deepcopy = deepcopy(test)
        >>> assert id(test) == id(test_copy)
        >>> assert id(test) != id(test_deepcopy)
        >>> test.attribute['a'] = 2
        >>> assert id(test.attribute) == id(test_copy.attribute)
        >>> assert id(test.attribute) != id(test_deepcopy.attribute)
        >>> assert test_copy.attribute['a'] == 2
        >>> assert test_deepcopy.attribute['a'] == 1
    """
    __slots__ = ()
    __ignore_state__ = ()

    def __getstate__(self): return getsetstate(self)

    def __setstate__(self, state): getsetstate(self, state)


class BoxKeys(box.Box):
    """
    Creates a Box with values from keys.
    """

    def __init__(self, keys, value='lower'):
        """
        Creates Box instance.

        Examples:
            >>> from bapy import BoxKeys
            >>>
            >>> BoxKeys('a b', value=None)
            <Box: {'a': 'a', 'b': 'b'}>
            >>> BoxKeys('A B')
            <Box: {'A': 'a', 'B': 'b'}>
            >>> BoxKeys('A B', value=list)
            <Box: {'A': [], 'B': []}>

        Args:
            keys: keys to use for keys and values.
            value: Type or function to use to init the Box.

        Returns:
            Initialize box from keys.
        """
        es = Is(value)
        super().__init__({item: getattr(item, value)() if es.str else item if es.none else value()
                          for item in toiter(keys)})


class ChainRV(EnumBase, metaclass=EnumBaseMeta):
    ALL = enum.auto()
    FIRST = enum.auto()
    UNIQUE = enum.auto()


class Chain(collections.ChainMap):
    # noinspection PyUnresolvedReferences
    """
        Variant of chain that allows direct updates to inner scopes and returns more than one value,
        not the first one.

        >>> class Test3:
        ...     a = 2
        >>>
        >>> class Test4:
        ...     a = 2
        >>>
        >>> Test1 = collections.namedtuple('Test1', 'a b')
        >>> Test2 = collections.namedtuple('Test2', 'a d')
        >>> test1 = Test1(1, 2)
        >>> test2 = Test2(3, 5)
        >>> test3 = Test3()
        >>> test4 = Test4()
        >>>
        >>> maps = [dict(a=1, b=2), dict(a=2, c=3), dict(a=3, d=4), dict(a=dict(z=1)), dict(a=dict(z=1)), \
        dict(a=dict(z=2))]
        >>> chain = Chain(*maps)
        >>> assert chain['a'] == [1, 2, 3, {'z': 1}, {'z': 2}]
        >>> chain = Chain(*maps, rv=ChainRV.FIRST)
        >>> assert chain['a'] == 1
        >>> chain = Chain(*maps, rv=ChainRV.ALL)
        >>> assert chain['a'] == [1, 2, 3, {'z': 1}, {'z': 1}, {'z': 2}]
        >>>
        >>> maps = [dict(a=1, b=2), dict(a=2, c=3), dict(a=3, d=4), dict(a=dict(z=1)), dict(a=dict(z=1)),\
        dict(a=dict(z=2)), test1, test2]
        >>> chain = Chain(*maps)
        >>> assert chain['a'] == [1, 2, 3, {'z': 1}, {'z': 2}]
        >>> chain = Chain(*maps, rv=ChainRV.FIRST)
        >>> assert chain['a'] == 1
        >>> chain = Chain(*maps, rv=ChainRV.ALL)
        >>> assert chain['a'] == [1, 2, 3, {'z': 1}, {'z': 1}, {'z': 2}, 1, 3]
        >>>
        >>> maps = [dict(a=1, b=2), dict(a=2, c=3), dict(a=3, d=4), dict(a=dict(z=1)), dict(a=dict(z=1)), \
        dict(a=dict(z=2)), test1, test2]
        >>> chain = Chain(*maps)
        >>> del chain['a']
        >>> assert chain == Chain({'b': 2}, {'c': 3}, {'d': 4}, test1, test2)
        >>> assert chain['a'] == [1, 3]
        >>>
        >>> maps = [dict(a=1, b=2), dict(a=2, c=3), dict(a=3, d=4), dict(a=dict(z=1)), dict(a=dict(z=1)), \
        dict(a=dict(z=2)), test1, test2]
        >>> chain = Chain(*maps)
        >>> assert chain.delete('a') == Chain({'b': 2}, {'c': 3}, {'d': 4}, test1, test2)
        >>> assert chain.delete('a')['a'] == [1, 3]
        >>>
        >>> maps = [dict(a=1, b=2), dict(a=2, c=3), dict(a=3, d=4), dict(a=dict(z=1)), dict(a=dict(z=1)), \
        dict(a=dict(z=2)), test1, test2]
        >>> chain = Chain(*maps, rv=ChainRV.FIRST)
        >>> del chain['a']
        >>> del maps[0]['a'] # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        KeyError:
        >>>
        >>> assert chain['a'] == 2
        >>>
        >>> maps = [dict(a=1, b=2), dict(a=2, c=3), dict(a=3, d=4), dict(a=dict(z=1)), dict(a=dict(z=1)), \
        dict(a=dict(z=2)), test1, test2]
        >>> chain = Chain(*maps, rv=ChainRV.FIRST)
        >>> new = chain.delete('a')
        >>> del maps[0]['a'] # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        KeyError:
        >>> assert new.delete('a')
        >>> del maps[1]['a'] # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        KeyError:
        >>>
        >>> assert new['a'] == 3
        >>>
        >>> maps = [dict(a=1, b=2), dict(a=2, c=3), dict(a=3, d=4), dict(a=dict(z=1)), dict(a=dict(z=1)), \
        dict(a=dict(z=2)), test1, test3]
        >>> chain = Chain(*maps)
        >>> del chain['a']
        >>> assert chain[4] == []
        >>> assert not hasattr(test3, 'a')
        >>> assert chain.set('a', 9)
        >>> assert chain['a'] == [9, 1]
        >>>
        >>> maps = [dict(a=1, b=2), dict(a=2, c=3), dict(a=3, d=4), dict(a=dict(z=1)), dict(a=dict(z=1)), \
        dict(a=dict(z=2)), test1, test4]
        >>> chain = Chain(*maps)
        >>> chain.set('j', 9)  # doctest: +ELLIPSIS
        Chain({'a': 1, 'b': 2, 'j': 9}, {'a': 2, 'c': 3}, {'a': 3, 'd': 4}, {'a': {'z': 1}}, {'a': {'z': 1}}, \
{'a': {'z': 2}}, Test1(a=1, b=2), <....Test4 object at 0x...>)
        >>> assert [maps[0]['j']] == chain['j'] == [9]
        >>> chain.set('a', 10)  # doctest: +ELLIPSIS
        Chain({'a': 10, 'b': 2, 'j': 9}, {'a': 10, 'c': 3}, {'a': 10, 'd': 4}, {'a': 10}, {'a': 10}, {'a': 10}, \
Test1(a=1, b=2), <....Test4 object at 0x...>)
        >>> # noinspection PyUnresolvedReferences
        >>> assert [maps[0]['a'], 1] == chain['a'] == [maps[7].a, 1] == [10, 1]  # 1 from namedtuple
        >>>
        >>> maps = [dict(a=1, b=2), dict(a=2, c=3), dict(a=3, d=4), dict(a=dict(z=1)), dict(a=dict(z=1)), \
        dict(a=dict(z=2)), test1, test4]
        >>> chain = Chain(*maps, rv=ChainRV.FIRST)
        >>> chain.set('a', 9)  # doctest: +ELLIPSIS
        Chain({'a': 9, 'b': 2}, {'a': 2, 'c': 3}, {'a': 3, 'd': 4}, {'a': {'z': 1}}, {'a': {'z': 1}}, \
{'a': {'z': 2}}, Test1(a=1, b=2), <....Test4 object at 0x...>)
        >>> assert maps[0]['a'] == chain['a'] == 9
        >>> assert maps[1]['a'] == 2
        """
    rv = ChainRV.UNIQUE
    default = None
    maps = list()

    def __init__(self, *maps, rv=ChainRV.UNIQUE, default=None):
        super().__init__(*maps)
        self.rv = rv
        self.default = default

    def __getitem__(self, key):
        rv = []
        for mapping in self.maps:
            if Is(mapping).namedtuple:
                mapping = mapping._asdict()
            elif hasattr(mapping, 'asdict'):
                to_dict = getattr(mapping.__class__, 'asdict')
                if isinstance(to_dict, property):
                    mapping = mapping.asdict
                elif callable(to_dict):
                    mapping = mapping.asdict()
            if hasattr(mapping, '__getitem__'):
                try:
                    value = mapping[key]
                    if self.rv is ChainRV.FIRST:
                        return value
                    if (self.rv is ChainRV.UNIQUE and value not in rv) or self.rv is ChainRV.ALL:
                        rv.append(value)
                except KeyError:
                    pass
            elif hasattr(mapping, '__getattribute__') and isinstance(key, str) and \
                    not isinstance(mapping, (tuple, bool, int, str, bytes)):
                try:
                    value = getattr(mapping, key)
                    if self.rv is ChainRV.FIRST:
                        return value
                    if (self.rv is ChainRV.UNIQUE and value not in rv) or self.rv is ChainRV.ALL:
                        rv.append(value)
                except AttributeError:
                    pass
        return self.default if self.rv is ChainRV.FIRST else rv

    def __delitem__(self, key):
        index = 0
        deleted = []
        found = False
        for mapping in self.maps:
            if mapping:
                if not isinstance(mapping, (tuple, bool, int, str, bytes)):
                    if hasattr(mapping, '__delitem__'):
                        if key in mapping:
                            del mapping[key]
                            if self.rv is ChainRV.FIRST:
                                found = True
                    elif hasattr(mapping, '__delattr__') and hasattr(mapping, key) and isinstance(key, str):
                        delattr(mapping.__class__, key) if key in dir(mapping.__class__) else delattr(mapping, key)
                        if self.rv is ChainRV.FIRST:
                            found = True
                if not mapping:
                    deleted.append(index)
                if found:
                    break
            index += 1
        for index in reversed(deleted):
            del self.maps[index]
        return self

    def delete(self, key):
        del self[key]
        return self

    def __setitem__(self, key, value):
        found = False
        for mapping in self.maps:
            if mapping:
                if not isinstance(mapping, (tuple, bool, int, str, bytes)):
                    if hasattr(mapping, '__setitem__'):
                        if key in mapping:
                            mapping[key] = value
                            if self.rv is ChainRV.FIRST:
                                found = True
                    elif hasattr(mapping, '__setattr__') and hasattr(mapping, key) and isinstance(key, str):
                        setattr(mapping, key, value)
                        if self.rv is ChainRV.FIRST:
                            found = True
                if found:
                    break
        if not found and not isinstance(self.maps[0], (tuple, bool, int, str, bytes)):
            if hasattr(self.maps[0], '__setitem__'):
                self.maps[0][key] = value
            elif hasattr(self.maps[0], '__setattr__') and isinstance(key, str):
                setattr(self.maps[0], key, value)
        return self

    def set(self, key, value):
        return self.__setitem__(key, value)


ClassBase = collections.namedtuple('Class', 'annotation attribute cls coro data importable i init module '
                                            'mro mroitems property qualname routine '
                                            'signature slot', )


class Class(ClassBase):
    """
    Class Info

    >>> import bapy.data.cls

    >>> a, d = Class(bapy.data.cls.MroAsync), Class(bapy.data.cls.MroDataDictSlotMix)

    # coro
    >>> assert sorted(a.coro) == ['async_classmethod', 'async_method', 'async_prop', 'async_staticmethod']

    # attribute
    >>> assert sorted(set(d.attribute).difference(dir(bapy.data.cls.MroDataDictSlotMix))) == \
    ['_MroData__dataclass_default_factory', '_MroData__dataclass_default_factory_init', 'args', \
    'dataclass_default_factory', 'dataclass_default_factory_init', 'kwargs', 'slot_initvar', 'slot_property_initvar']

    # defaults
    >>> assert d.data['dataclass_default_factory'] == {}
    >>> assert d.data['dataclass_default_factory_init'] == {}
    >>> assert d.filter(name='data') == {'_MroData__data': '__data', \
                                           '_MroData__dataclass_classvar': '__dataclass_classvar', \
                                           '_MroData__dataclass_default_factory': {}, \
                                           '_MroData__dataclass_default_factory_init': {}, \
                                           'args': MISSING, 'dataclass_classvar': 'dataclass_classvar', \
                                           'dataclass_default': 'dataclass_default', \
                                           'dataclass_default_factory': {}, 'dataclass_default_factory_init': {}, \
                                           'dataclass_default_init': 'dataclass_default_init', \
                                           'dataclass_initvar': 'dataclass_initvar', \
                                           'dataclass_str': 'dataclass_integer', \
                                           'kwargs': MISSING, \
                                           'slot_initvar': 'slot_initvar', \
                                           'slot_property_initvar': 'slot_property_initvar', \
                                           'subclass_annotated_str': 'subclass_annotated_str', \
                                           'subclass_classvar': 'subclass_classvar', 'subclass_str': 'subclass_str'}

    # sigs
    >>> assert d.signature[bapy.data.cls.MroDataDictSlotMix] == dd(dict, {'args': MISSING, 'kwargs': MISSING, \
                                                            'dataclass_initvar': MISSING, \
                                                            'slot_property_initvar': 'slot_property_initvar', \
                                                            'slot_initvar': 'slot_initvar'})
    >>> assert d.signature[bapy.data.cls.MroDataDictMix] == dd(dict, {'args': MISSING, 'kwargs': MISSING, \
                                                        'dataclass_initvar': MISSING, \
                                                        'subclass_dynamic': 'subclass_dynamic'})
    >>> assert d.signature[bapy.data.cls.MroData] == dd(dict, {'args': MISSING, 'kwargs': MISSING, \
                                                 '_MroData__dataclass_default_factory_init': DEFAULT_FACTORY, \
                                                 'dataclass_default_factory_init': DEFAULT_FACTORY, \
                                                 'dataclass_default_init': 'dataclass_default_init', \
                                                 'dataclass_initvar': MISSING, 'dataclass_str': 'dataclass_integer'})
    >>> assert d.signature[object] == dd(dict, {'args': MISSING, 'kwargs': MISSING})
    """
    cache = {}
    __slots__ = ()

    def __new__(cls, C):
        i, C = (C, C()) if isinstance(C, Is) else (Is(C), C)
        if C in Class.cache:
            return Class.cache[C]
        cached_properties, fields = [], C.__dataclass_fields__ if i.dataclass else {}
        named = cls._fields if i.namedtuple else {}
        kw = dict(annotation=annotations(C, index=2), attribute={}, cls=C, coro=set(), data={}, i=i,
                  importable=f'{C.__module__}.{C.__qualname__}', init={}, module=C.__qualname__,
                  mro=C.__mro__, mroitems=collections.defaultdict(set, {}), property=set(), qualname=C.__qualname__,
                  routine=set(), signature={}, slot=set())
        for base in C.__mro__:
            kw['signature'][base] = typing.cast(typing.Any, dd(dict, {}))
            for name, exclude in N.SIGNATURES().items():
                if v := name.hasget(base):
                    kw['signature'][base].update({k: v for k, v in Is(v).signature.items() if k not in exclude})
            for key, value in N.MROITEMS().items():
                kw['mroitems'][key].update(key.hasget(base, default=set()))
                kw['mroitems'][key].update(value)
        init_and_state = kw['mroitems'][N.IGNORE_INIT] | kw['mroitems'][N.IGNORE_STATE]
        for item in inspect.classify_class_attrs(C):
            name = qualname = item.name
            i, kind = Is(item.object), Kind(item.kind)
            if kind is Kind.DATA:
                if i.memberdescriptortype:
                    kw['slot'].add(name)
                else:
                    f = getm(fields, name)
                    if name in named:
                        kw['data'][name] = kw['init'][name] = getm(cls._field_defaults, named)
                    elif f != MISSING:
                        kw['data'][name] = MISSING if f.default is DATA_MISSING else f.default
                        if f.init and name not in init_and_state:
                            kw['init'][name] = kw['data'][name]
                    else:
                        kw['data'][name] = typing.cast(typing.Any, item.object)
                        if name in kw['signature'][C]:
                            kw['init'][name] = kw['data'][name]
            else:
                if i.cached_property:
                    kind = Kind.PROPERTY
                    cached_properties.append(name)
                kw['routine'].add(name)
                qualname = N.QUALNAME.hasget(i.func, name)
                if kind is Kind.PROPERTY:
                    kw['property'].add(name)
                if i.coro:
                    kw['coro'].add(name)
            kw['attribute'][name] = typing.cast(typing.Any, Attribute(defining=item.defining_class, i=i, kind=kind,
                                                                      object=item.object, qualname=qualname))
        for name in cached_properties:
            kw['attribute'].pop(name)

        for name, f in fields.items():
            if name not in kw['attribute']:
                defining = C
                for base in reversed(C.__mro__):
                    if N.DATACLASS_FIELDS.has(base) and name in base.__dataclass_fields__:
                        defining = base
                        break
                if f.default_factory is not DATA_MISSING:
                    kind = Kind.FACTORY
                    data = f.default_factory()
                elif isinstance(f.type, dataclasses.InitVar):
                    kind = Kind.INITVAR
                    data = f.default if f.default is not DATA_MISSING else MISSING
                else:
                    kind = Kind.UNKNOWN
                    data = MISSING
                kw['data'][name] = data
                if f.init and name not in init_and_state:
                    kw['init'][name] = kw['data'][name]
                kw['attribute'][name] = typing.cast(typing.Any, Attribute(defining=defining, i=Is(kw['data'][name]),
                                                                          kind=kind, object=data, qualname=name))
        # noinspection PyUnresolvedReferences
        for name, df in kw['signature'][C].items():
            if name not in kw['init']:
                kw['data'][name] = df if df != MISSING else getm(kw['annotation'], name)
                kw['init'][name] = kw['data'][name]
                kw['attribute'][name] = typing.cast(typing.Any, Attribute(defining=C, i=Is(kw['data'][name]),
                                                                          kind=Kind.INITVAR, object=kw['data'][name],
                                                                          qualname=name))
        Class.cache[C] = value = super().__new__(cls, **kw)
        return value

    def __iter__(self):
        """
        Iter: Class Attributes.

        Returns:
            Class Attributes.
        """
        for i in sorted(self.attribute):
            yield i

    def filter(self, name, access=Access.PROTECTED):
        if (value := getattr(self, name)) and isinstance(value, dict):
            return {i: value[i] for i in sorted(value) if i >= access}
        return tuple(i for i in sorted(value) if i >= access)

    @classmethod
    def from_obj(cls, data): return cls(Is(data))

    @classmethod
    def vars(cls, data, access=Access.PROTECTED, both=False, ignore=lambda x, y: False, prop=True, state=False):
        """
        Data Attributes for Class, Instance or Class & Instance (both).

        >>> import bapy.data.cls
        >>> from bapy import Class, MISSING
        >>> a, m = Class.vars(bapy.data.cls.MroAsync()), Class.vars(bapy.data.cls.MroDataDictSlotMix())
        >>> assert a == { \
            '_async_classmethod': '_async_classmethod', \
            '_async_method': '_async_method', \
            '_async_prop': '_async_prop', \
            '_async_staticmethod': '_async_staticmethod', \
            '_classmethod': '_classmethod', \
            '_method': '_method', \
            '_staticmethod': '_staticmethod', \
            'args': MISSING, \
            'cprop': '_cprop', \
            'kwargs': MISSING, \
            'prop': '_prop' \
        }
        >>> assert m == {'_MroData__dataclass_default_factory': {}, '_MroData__dataclass_default_factory_init': {}, \
                         'dataclass_default_factory': {}, 'dataclass_default_factory_init': {}, \
                         'dataclass_default_init': 'dataclass_default_init', 'dataclass_str': 'dataclass_integer', \
                         'slot': 'slot_initvar', 'slot_property': 'slot_property_initvar', \
                         'subclass_dynamic': 'subclass_dynamic'}

        Args:
            data: instance or class.
            access: include prefix.
            both: when instance both includes classvars.
            ignore: predicate to ignore key/value.
            prop: include properties when instance.
            state: do not include class even if not init method.

        Returns:
            Dict with Data Attributes for Class, Instance or Class & Instance (both).
        """
        c = cls.from_obj(data)
        if c.i.type:
            d = c.data
        else:
            if not state and not N.INIT(c.i().__dict__):  # If not init then include class.
                both = True
            d = (c.data if both else {}) | {i: getm(data, i) for i in c.slot} | \
                (data.__dict__ if N.DICT(data) else {})
            if prop:
                for i in c.property:
                    if ((protected := f'_{i}') in d) and (i not in c.coro):
                        d.pop(protected)
                        d[i] = getm(data, i)
        return dict_sort({k: v for k, v in d.items() if Access[k] >= access and not ignore(k, v)})


class CmdError(Exception):
    """Thrown if execution of cmd command fails with non-zero status code."""

    def __init__(self, rv):
        command = rv.args
        rc = rv.returncode
        stderr = rv.stderr
        stdout = rv.stdout
        super().__init__(f'{command=}', f'{rc=}', f'{stderr=}', f'{stdout=}')


class CmdAioError(CmdError):
    """Thrown if execution of aiocmd command fails with non-zero status code."""

    def __init__(self, rv):
        super().__init__(rv)


class DataClass(metaclass=abc.ABCMeta):
    """
    Supports Data Class.

    Examples:
        >>> from dataclasses import make_dataclass
        >>>
        >>> DataC = make_dataclass('C', [('a', int, datafield(default=1))])
        >>> class D: a = 1
        >>>
        >>> data = DataC()
        >>> d = D()
        >>>
        >>> assert Is(DataC).dataclass == True
        >>> assert Is(data).dataclass == True
        >>>
        >>> assert Is(Dict).dataclass == False
        >>> assert Is(d).dataclass == False
    """
    __annotations__ = dict()
    __dataclass_fields__ = dict()

    @abc.abstractmethod
    def __repr__(self) -> str:
        return str(self)

    @classmethod
    def __subclasshook__(cls, C):
        if cls is DataClass:
            return N.DATACLASS_FIELDS.has(C)
        return NotImplemented


class dd(collections.defaultdict):
    """
    Default Dict Helper Class.

    Examples:
        >>> d = dd()
        >>> d
        dd(None, {})
        >>> d[1]
        >>> d.get(1)
        >>>
        >>> d = dd({})
        >>> d
        dd(None, {})
        >>> d[1]
        >>> d.get(1)
        >>>
        >>> d = dd({}, a=1)
        >>> d
        dd(None, {'a': 1})
        >>> d[1]
        >>> d.get(1)
        >>>
        >>> d = dd(dict)
        >>> d
        dd(<class 'dict'>, {})
        >>> d.get(1)
        >>> d
        dd(<class 'dict'>, {})
        >>> d[1]
        {}
        >>> d
        dd(<class 'dict'>, {1: {}})
        >>> d = dd(tuple)
        >>> d
        dd(<class 'tuple'>, {})
        >>> d[1]
        ()
        >>> d.get(1)
        ()
        >>>
        >>> d = dd(True)
        >>> d
        dd(True, {})
        >>> d[1]
        True
        >>> d.get(1)
        True
        >>>
        >>> d = dd({1: 1}, a=1)
        >>> d
        dd(None, {1: 1, 'a': 1})
        >>> d[1]
        1
        >>> d.get(1)
        1
        >>>
        >>> d = dd(list, {1: 1}, a=1)
        >>> d
        dd(<class 'list'>, {1: 1, 'a': 1})
        >>> d[2]
        []
        >>> d
        dd(<class 'list'>, {1: 1, 'a': 1, 2: []})
        >>>
        >>> d = dd(True, {1: 1}, a=1)
        >>> d
        dd(True, {1: 1, 'a': 1})
        >>> d.get('c')
        >>> d['c']
        True
    """
    __slots__ = ('__factory__',)

    def __init__(self, factory=None, *args, **kwargs):
        def dd_factory(value): return lambda: value() if callable(value) else value

        iterable = isinstance(factory, Iterable)
        self.__factory__ = None if iterable else factory
        super().__init__(dd_factory(self.__factory__), *(args + (factory,) if iterable else args), **kwargs)

    def __repr__(self): return f'{self.__class__.__name__}({self.__factory__}, {dict(self)})'

    __class_getitem__ = classmethod(types.GenericAlias)


class dictsort(dict, MutableMapping):
    __slots__ = ()

    def __init__(self, *args, **kwargs): super().__init__(*args, **kwargs)

    def sort(self): return self.__class__({item: self[item] for item in sorted(self)})


class Executor(EnumBase, metaclass=EnumBaseMeta):
    PROCESS = concurrent.futures.ProcessPoolExecutor
    THREAD = concurrent.futures.ThreadPoolExecutor
    NONE = None

    async def run(self, func, *args, **kwargs):
        """
        Run in :lib:func:`loop.run_in_executor` with :class:`concurrent.futures.ThreadPoolExecutor`,
            :class:`concurrent.futures.ProcessPoolExecutor` or
            :lib:func:`asyncio.get_running_loop().loop.run_in_executor` or not poll.

        Args:
            func: func
            *args: args
            **kwargs: kwargs

        Raises:
            ValueError: ValueError

        Returns:
            Awaitable:
        """
        loop = asyncio.get_running_loop()
        call = functools.partial(func, *args, **kwargs)
        if not func:
            raise ValueError

        if self():
            with self()() as p:
                return await loop.run_in_executor(p, call)
        return await loop.run_in_executor(self(), call)


FindUp = collections.namedtuple('FindUp', 'path previous')


class Frame:
    """
    Frame Class.

    >>> import bapy.__init__
    >>> from bapy import Stack, Frame, Path
    >>> init = Stack.init()
    >>> assert Path(bapy.__init__.__file__) in Frame.cache
    >>> main = Stack.main()
    >>> frame = Stack()

    """
    cache = {}

    __slots__ = ('_args', '_vars', 'cls', 'code', 'context', 'coro', 'decorator', 'external', 'file', 'frame',
                 'function', 'functions', 'include',
                 'internal', 'lineno', 'lines', 'module', 'node', 'qualname', 'real', 'source')

    def __init__(self, frame):
        self._args, self._vars = None, None
        self.code, self.file, self.frame = frame.f_code, Path(frame.f_code.co_filename), frame
        self.function, self.lineno = frame.f_code.co_name, frame.f_lineno
        self.internal = path_internal.file.parent and self.file.is_relative_to(path_internal.file.parent)
        self.decorator, self.lines, self.module = [], {}, self.function == FUNCTION_MODULE
        self.external, self.functions, self.lines = False, intervaltree.IntervalTree(), {}
        self.cls, self.context, self.coro, self.node, self.qualname, self.real, self.source = (None,) * 7
        # TODO: No entiendo por que no funciona el '/Applications/PyCharm.app/Contents/plugins' lineno 32
        self.include = self.file.resolved.exists() and not any(map(self.file.is_relative_to, PATHS_EXCL))
        if self.include:
            if self.file in Frame.cache:
                c = Frame.cache[self.file]
                self.source = c.source
                self.node = c.node
                self.external = c.external
                self.functions = c.functions
                self.lines = c.lines
                self.context = c.context
                self.cls = c.cls
                self.decorator = c.decorator
                self.qualname = c.qualname
                self.coro = c.coro
                self.real = c.real
                return
            self.source = self.file.source
            self.node = ast.parse(self.source, self.file.text)
            for node in self:
                if (isinstance(node, ast.Import) and any([path_internal.package == n.name.split('.')[0]
                                                          for n in node.names])) \
                        or (isinstance(node, ast.ImportFrom) and node.level == 0
                            and node.module.split('.')[0] == path_internal.package):
                    self.external = True
                else:  # Add: LINES & FUNCTIONS
                    if (defs := (self + node)) is not None:
                        start = node.lineno
                        end = node.lineno
                        for n in ast.walk(node):
                            if (self + n) is not None:
                                start = min(start, n.lineno)
                                end = max(end, n.lineno)
                        if defs and ((end - start) > 1):
                            self.functions[start:end] = node

            # LINES
            if (line := self.lines.get(self.lineno)) is None:
                raise MatchError(file=self.file, lineno=self.lineno)
            for n in line['nodes']:
                code = ast.unparse(n)
                if isinstance(n, (ast.AsyncFor, ast.AsyncWith, ast.Await)) or \
                        (any([i.__name__ in code for i in [asyncio.as_completed, asyncio.create_task,
                                                           asyncio.ensure_future, asyncio.gather, asyncio]])
                         and asyncio.to_thread.__name__ not in code):
                    self.lines[self.lineno]['coro']['line'] = True
                    break
            self.lines[self.lineno]['code'] = str(max({ast.get_source_segment(self.source, n) for n in line['nodes']},
                                                      key=len)).split('\n')
            self.context = self.lines[self.lineno]['code']
            self.lines = dict_sort(self.lines)

            # FUNCTIONS
            if not self.module:  # TODO: No tengo claro lo de self.module
                if not (routines := self.functions[self.lineno]):
                    raise MatchError(file=self.file, lineno=self.lineno, function=self.function)
                distance = {self.lineno - item.begin: item.data for item in routines}
                distance = intervaltree.Interval(min(distance.keys()), max(distance.keys()), distance)
                distance_min = distance.data[distance.begin]
                if distance_min.name != self.function:
                    raise MatchError(file=self.file, lineno=self.lineno, name=distance_min.name, function=self.function)
                self.cls = distance.data[distance.end].name
                self.decorator = [item.id for item in distance_min.decorator_list if N.id(item)]
                self.lines[self.lineno]['coro']['func'] = isinstance(distance_min, ast.AsyncFunctionDef)
                self.qualname = '.'.join([distance.data[item].name for item in sorted(distance.data, reverse=True)])

            # CORO
            rv = None
            for i in FrameId:
                if i is FrameId.IMPORTLIB and self.lineno == 228:
                    ic(i.value.function, self.function, i.value.function == self.function,
                       self.module, self.module is False,
                       self.file.exists, self.file.exists is False,
                       i.value.parts, self.file.path, self.file.path().text, self.file.path().has(i.value.parts))
                if i.value.function == self.function and \
                        any([(i.value.parts in self.file.path()),
                             (self.module is False and self.file.exists is False and isinstance(i.value.parts, str) and
                              self.file.path().has(i.value.parts))]):
                    rv = i
                    break
            self.coro = rv.value.ASYNC if rv else \
                self.lines[self.lineno]['coro']['line'] or self.lines[self.lineno]['coro']['func']
            self.real = rv.value.real if rv else int() if self.include else None
            Frame.cache[self.file] = self

    def __add__(self, node):
        if N.lineno(node):
            if node.lineno not in self.lines:
                self.lines[node.lineno] = {'coro': {'func': False, 'line': False}, 'nodes': [], 'source': ''}
            if node not in self.lines[node.lineno]['nodes']:
                self.lines[node.lineno]['nodes'].append(node)
            return Is(node).defs

    def __hash__(self): return hash(self.frame)

    def __iter__(self):
        if self.node:
            for i in ast.walk(self.node):
                yield i

    def __reduce__(self): return self.__class__, (self.frame,)

    def __repr__(self): return reprcls(self, ('file', 'function', 'lineno', 'module', 'coro',
                                              'include', 'internal', 'external', 'qualname', 'context', 'real'))

    @property
    def args(self):
        try:
            return self._args
        except AttributeError:
            self._args = value = {}
            locs = self.vars.locs
            if locs:
                arg, varargs, keywords = inspect.getargs(self.code)
                value = delete({name: locs[name] for name in arg} | ({varargs: val} if (
                    val := locs.get(varargs)) else dict()) | (kw if (kw := locs.get(keywords)) else dict()))
            return value

    @property
    def vars(self):
        try:
            return self._vars
        except AttributeError:
            self._vars = value = SourceVars(self.frame)
            return value

    __class_getitem__ = classmethod(types.GenericAlias)


FrameIdBase = collections.namedtuple('FrameIdBase', 'code decorator function parts real coro')


class FrameId(EnumBase, metaclass=EnumBaseMeta):
    ASYNCCONTEXTMANAGER = FrameIdBase(code=str(), decorator=str(),
                                      function='__aenter__', parts='contextlib.py', real=1, coro=True)
    IMPORTLIB = FrameIdBase(code=str(), decorator=str(),
                            function='_call_with_frames_removed', parts=f'<frozen {importlib._bootstrap.__name__}>',
                            real=5, coro=False)
    RUN = FrameIdBase(code=str(), decorator=str(),
                      function='_run', parts='asyncio events.py', real=5, coro=True)
    TO_THREAD = FrameIdBase(code=str(), decorator=str(),
                            function='run', parts='concurrent futures thread.py', real=None, coro=False)
    # FUNCDISPATCH = ('return funcs[Call().ASYNC]', 'wrapper bapy', 'core', 1)


FrameSimple = collections.namedtuple('FrameSimple', 'back code frame function globals lineno locals name '
                                                    'package path vars')


@typing.runtime_checkable
class GetItem(typing.Protocol):
    """Supports __getitem__."""
    __slots__ = tuple()

    @abc.abstractmethod
    def __getitem__(self, index): return self[index]


@typing.runtime_checkable
class GetMethod(typing.Protocol):
    """
    Get Method.

    Examples:
        >>> class D: a = 1
        >>> class G: a = 1; get = lambda self, item: self.__getattribute__(item)
        >>> class Slots: a = 1; __slots__ = tuple()
        >>>
        >>> d = D()
        >>> dct = dict(a=1)
        >>> g = G()
        >>>
        >>> assert dct.get('a') == 1
        >>> assert g.get('a') == 1
        >>>
        >>> assert Is(D).getmethod == False
        >>> assert Is(d).getmethod == False
        >>>
        >>> assert Is(G).getmethod == True
        >>> assert Is(g).getmethod == True
        >>>
        >>> assert Is(dict).getmethod == True
        >>> assert Is(dct).getmethod == True
    """
    __slots__ = tuple()

    @abc.abstractmethod
    def get(self, name, default=None): pass


class getter:
    """
    Return a callable object that fetches the given attribute(s)/item(s) from its operand.

    >>> from types import SimpleNamespace
    >>> from pickle import dumps, loads
    >>> from copy import deepcopy
    >>>
    >>> test = SimpleNamespace(a='a', b='b')
    >>> assert getter('a b')(test) == (test.a, test.b)
    >>> assert getter('a c')(test) == (test.a, None)
    >>> dicts = getter('a c d', default={})(test)
    >>> assert dicts == (test.a, {}, {})
    >>> assert id(dicts[1]) != id(dicts[2])
    >>> assert getter('a')(test) == test.a
    >>> assert getter('a b', 'c')(test) == (test.a, test.b, None)
    >>> assert getter(['a', 'b'], 'c')(test) == (test.a, test.b, None)
    >>> assert getter(['a', 'b'])(test) == (test.a, test.b)
    >>>
    >>> test = dict(a='a', b='b')
    >>> assert getter('a b')(test) == (test['a'], test['b'])
    >>> assert getter('a c')(test) == (test['a'], None)
    >>> dicts = getter('a c d', default={})(test)
    >>> assert dicts == (test['a'], {}, {})
    >>> assert id(dicts[1]) != id(dicts[2])
    >>> assert getter('a')(test) == test['a']
    >>> assert getter('a b', 'c')(test) == (test['a'], test['b'], None)
    >>> assert getter(['a', 'b'], 'c')(test) == (test['a'], test['b'], None)
    >>> assert getter(['a', 'b'])(test) == (test['a'], test['b'])
    >>>
    >>> test = SimpleNamespace(a='a', b='b')
    >>> test1 = SimpleNamespace(d='d', test=test)
    >>> assert getter('d test.a test.a.c test.c test.m.j.k')(test1) == (test1.d, test1.test.a, None, None, None)
    >>> assert getter('a c')(test1) == (None, None)
    >>> dicts = getter('a c d test.a', 'test.b', default={})(test1)
    >>> assert dicts == ({}, {}, test1.d, test1.test.a, test1.test.b)
    >>> assert id(dicts[1]) != id(dicts[2])
    >>> assert getter('a')(test1) is None
    >>> assert getter('test.b')(test1) == test1.test.b
    >>> assert getter(['a', 'test.b'], 'c')(test1) == (None, test1.test.b, None)
    >>> assert getter(['a', 'a.b.c'])(test1) == (None, None)
    >>>
    >>> test = dict(a='a', b='b')
    >>> test1_dict = dict(d='d', test=test)
    >>> assert getter('d test.a test.a.c test.c test.m.j.k')(test1_dict) == \
    getter('d test.a test.a.c test.c test.m.j.k')(test1)
    >>> assert getter('d test.a test.a.c test.c test.m.j.k')(test1_dict) == (test1_dict['d'], test1_dict['test']['a'], \
    None, None, None)
    >>> assert getter('a c')(test1_dict) == (None, None)
    >>> dicts = getter('a c d test.a', 'test.b', default={})(test1_dict)
    >>> assert dicts == ({}, {}, test1_dict['d'], test1_dict['test']['a'], test1_dict['test']['b'])
    >>> assert id(dicts[1]) != id(dicts[2])
    >>> assert getter('a')(test1_dict) is None
    >>> assert getter('test.b')(test1_dict) == test1_dict['test']['b']
    >>> assert getter(['a', 'test.b'], 'c')(test1_dict) == (None, test1_dict['test']['b'], None)
    >>> assert getter(['a', 'a.b.c'])(test1_dict) == (None, None)
    >>>
    >>> encode = dumps(test1_dict)
    >>> test1_dict_decode = loads(encode)
    >>> assert id(test1_dict) != id(test1_dict_decode)
    >>> test1_dict_copy = deepcopy(test1_dict)
    >>> assert id(test1_dict) != id(test1_dict_copy)
    >>>
    >>> assert getter('d test.a test.a.c test.c test.m.j.k')(test1_dict_decode) == \
    (test1_dict_decode['d'], test1_dict_decode['test']['a'], None, None, None)
    >>> assert getter('a c')(test1_dict_decode) == (None, None)
    >>> dicts = getter('a c d test.a', 'test.b', default={})(test1_dict_decode)
    >>> assert dicts == ({}, {}, test1_dict_decode['d'], test1_dict['test']['a'], test1_dict_decode['test']['b'])
    >>> assert id(dicts[1]) != id(dicts[2])
    >>> assert getter('a')(test1_dict_decode) is None
    >>> assert getter('test.b')(test1_dict_decode) == test1_dict_decode['test']['b']
    >>> assert getter(['a', 'test.b'], 'c')(test1_dict_decode) == (None, test1_dict_decode['test']['b'], None)
    >>> assert getter(['a', 'a.b.c'])(test1_dict_decode) == (None, None)

    The call returns:
        - getter('name')(r): r.name/r['name'].
        - getter('name', 'date')(r): (r.name, r.date)/(r['name'], r['date']).
        - getter('name.first', 'name.last')(r):(r.name.first, r.name.last)/(r['name.first'], r['name.last']).
    """
    __slots__ = ('_attrs', '_call', '_copy', '_default', '_mm')

    def __init__(self, attr, *attrs, default=None):
        self._copy = True if 'copy' in dir(type(default)) else False
        self._default = default
        _attrs = toiter(attr)
        attr = _attrs[0]
        attrs = (tuple(_attrs[1:]) if len(_attrs) > 1 else ()) + attrs
        if not attrs:
            if not isinstance(attr, str):
                raise TypeError('attribute name must be a string')
            self._attrs = (attr,)
            names = attr.split('.')

            def func(obj):
                mm = isinstance(obj, MutableMapping)
                count = 0
                total = len(names)
                for name in names:
                    # TODO: estaba con el type de las constantes.
                    #   Estaba con la cache.
                    #   Estaba Con Class.
                    count += 1
                    _default = self._default.copy() if self._copy else self._default
                    if mm:
                        try:
                            obj = obj[name]
                            if not isinstance(obj, MutableMapping) and count < total:
                                obj = None
                                break
                        except KeyError:
                            obj = _default
                            break
                    else:
                        obj = getattr(obj, name, _default)
                return obj

            self._call = func
        else:
            self._attrs = (attr,) + attrs
            callers = tuple(self.__class__(item, default=self._default) for item in self._attrs)

            def func(obj):
                return tuple(call(obj) for call in callers)

            self._call = func

    def __call__(self, obj): return self._call(obj)

    def __reduce__(self): return self.__class__, self._attrs

    def __repr__(self): return reprcls(data=self, attrs=self._attrs)


class GitScheme(EnumBase, metaclass=EnumBaseMeta):
    HOST = enum.auto()
    HTTPS = enum.auto()
    PIP = enum.auto()
    SSH = enum.auto()


GitTop = collections.namedtuple('GitTop', 'name origin path')

IntervalBase = collections.namedtuple('IntervalBase', 'begin end data')
IntervalType = intervaltree.Interval[IntervalBase]


class Is:
    """
    Is Instance/Subclass Helper Class.

    Examples:
        >>> import bapy.data.cls
        >>> assert Is(2).int is True
        >>> assert Is(2).bool is False
        >>> assert Is(2).instance(dict, tuple) is False
        >>> assert Is(2).instance(dict, tuple) is False
        >>> def func(): pass
        >>> assert Is(func).coro is False
        >>> async def async_func(): pass
        >>> i = Is(async_func)
        >>> assert (i.coro, i.coroutinefunction, i.asyncgen, i.asyncgenfunction, i.awaitable, i.coroutine) ==  \
        (True, True, False, False, False, False)
        >>> rv = dict(map(lambda x: (x.name, Is(x.object)), inspect.classify_class_attrs(bapy.data.cls.MroAsync)))
        >>> assert (rv['async_classmethod'].coro, rv['async_classmethod'].coroutinefunction, \
        rv['async_classmethod'].asyncgen, rv['async_classmethod'].asyncgenfunction, \
        rv['async_classmethod'].awaitable, rv['async_classmethod'].coroutine) == \
        (True, True, False, False, False, False)
        >>> assert (rv['async_method'].coro, rv['async_method'].coroutinefunction, \
        rv['async_method'].asyncgen, rv['async_method'].asyncgenfunction, \
        rv['async_method'].awaitable, rv['async_method'].coroutine) == (True, True, False, False, False, False)
        >>> assert (rv['async_prop'].coro, rv['async_prop'].coroutinefunction, \
        rv['async_prop'].asyncgen, rv['async_prop'].asyncgenfunction, \
        rv['async_prop'].awaitable, rv['async_prop'].coroutine) == (True, True, False, False, False, False)
        >>> assert (rv['async_staticmethod'].coro, rv['async_staticmethod'].coroutinefunction, \
        rv['async_staticmethod'].asyncgen, rv['async_staticmethod'].asyncgenfunction, \
        rv['async_staticmethod'].awaitable, rv['async_staticmethod'].coroutine) == \
        (True, True, False, False, False, False)
        >>> assert rv['classmethod'].coro == False
        >>> assert rv['cprop'].coro == False
        >>> assert rv['method'].coro == False
        >>> assert rv['prop'].coro == False
        >>> assert rv['staticmethod'].coro == False

    Attributes:
    -----------
        data: Any
            object to provide information (default: None)
    """
    __slots__ = ('_func', '_varstype', 'data',)

    def __init__(self, data=None): self.data = data; self._func = self._varstype = None

    def __call__(self):
        """
        Returns data type or type if class`.

        Examples:
            >>> assert Is(dict)() == dict
            >>> assert Is(dict())() == dict

        Returns:
            Class.
        """
        return self.cls

    def __getstate__(self): return dict(data=self.data)

    def __hash__(self):
        """
        Hash

        >>> from environs import Env
        >>> assert hash(Is(dict()))
        >>> assert hash(Is(list()))
        >>> assert hash(Is(Env()))

        Returns:
            Hash
        """
        try:
            return hash(self.data)
        except TypeError:
            if isinstance((data := self.data), MutableMapping) or (
                    not isinstance(self.data, type) and (data := N.DICT.hasget(self.data))):
                return hash(tuple(data.items()))
            return hash(pickle.dumps(self.data))

    def __iter__(self):
        """
        Iter: self.data.

        Returns:
            Iterable self.data.
        """
        if self.iterable:
            for i in self.data:
                yield i
        else:
            yield

    def __reduce__(self): return self.__class__, (self.data,)

    def __repr__(self): return f'{self.__class__.__name__}({self.data})'

    def __setstate__(self, state): self.data = state['data']

    def __str__(self): return str(self.data)

    allattr = property(lambda self: self.supports(AllAttr))
    annotationsattr = property(lambda self: self.supports(AnnotationsAttr))
    asdictmethod = property(lambda self: self.supports(AsDictMethod))
    asdictproperty = property(lambda self: self.supports(AsDictProperty))
    ast = property(lambda self: isinstance(self.data, ast.AST))
    asyncfor = property(lambda self: isinstance(self.func, ast.AsyncFor))
    asyncfunctiondef = property(lambda self: isinstance(self.func, ast.AsyncFunctionDef))
    asyncgen = property(lambda self: isinstance(self.func, types.AsyncGeneratorType))
    asyncgenfunction = property(lambda self: inspect.isasyncgenfunction(self.func))
    asyncs = property(lambda self: isinstance(self.data, typing.get_args(AsyncsUnion)))
    asyncwith = property(lambda self: isinstance(self.func, ast.AsyncWith))
    await_ast = property(lambda self: isinstance(self.func, ast.Await))
    awaitable = property(lambda self: inspect.isawaitable(self.func))
    bool = property(lambda self: isinstance(self.data, int) and isinstance(self.data, bool))
    builtin = property(
        lambda self: self.builtinclass or self.builtinfunction or (indict(BUILTIN, self.data) if self.mm else False))
    builtinclass = property(lambda self: self.data in BUILTIN_CLASS if self.type else False)
    builtinclassnodict = property(lambda self: self.data in BUILTIN_CLASS_NO_DICT if self.type else False)
    builtinfunction = property(lambda self: self.data in BUILTIN_FUNCTION)
    builtinfunctiontype = property(lambda self: isinstance(self.data, types.BuiltinFunctionType))
    bytesio = property(lambda self: isinstance(self.data, io.BytesIO))  # :class:`typing.BinaryIO`
    cached = property(lambda self: self.cls in self.cache)
    cached_property = property(lambda self: isinstance(self.data, functools.cached_property))
    callable = property(lambda self: isinstance(self.data, Callable))
    chain = property(lambda self: isinstance(self.data, Chain))
    chainmap = property(lambda self: isinstance(self.data, collections.ChainMap))
    classdef = property(lambda self: isinstance(self.data, ast.ClassDef))
    classvar = property(lambda self: (self.datafield and self.data._field_type is FIELD_CLASSVAR) or typing.get_origin(
        self.data) == typing.ClassVar)
    classvar_or_initvar = property(lambda self: self.classvar or self.initvar)
    cls = property(lambda self: self.data if self.type else self.data.__class__)
    clsmethod = property(lambda self: isinstance(self.data, (classmethod, types.ClassMethodDescriptorType)))
    codetype = property(lambda self: isinstance(self.data, types.CodeType))
    collections = property(lambda self: N.MODULE.has(self.cls) and self.cls.__module__ == collections.__name__)
    container = property(lambda self: isinstance(self.data, Container))
    coro = property(lambda self: any(
        self.asyncs or self.defs if self.ast else [self.asyncgen, self.asyncgenfunction, self.awaitable,
                                                   self.coroutine, self.coroutinefunction]))
    coroutine = property(lambda self: asyncio.iscoroutine(self.func) or isinstance(self.func, types.CoroutineType))
    coroutinefunction = property(lambda self: inspect.iscoroutinefunction(self.func))
    dataclass = property(lambda self: self.supports(DataClass))
    datafield = property(lambda self: isinstance(self.data, dataclasses.Field))
    datamissing = property(
        lambda self: (self.datafield and self.data.default is DATA_MISSING) or self.data is DATA_MISSING)
    defaultdict = property(lambda self: isinstance(self.data, collections.defaultdict))
    defs = property(lambda self: isinstance(self.data, typing.get_args(DefsUnion)))
    deleter = property(lambda self: self.property_any and self.data.fdel is not None)
    dict = property(lambda self: isinstance(self.data, dict))
    dynamicclassattribute = property(lambda self: isinstance(self.data, types.DynamicClassAttribute))
    dlst = property(lambda self: isinstance(self.data, (dict, list, set, tuple)))
    enum = property(lambda self: isinstance(self.data, enum.Enum))
    enum_sub = property(lambda self: isinstance(self.data, type) and issubclass(self.data, enum.Enum))
    enumbase = property(lambda self: isinstance(self.data, EnumBase))
    enumbase_sub = property(lambda self: isinstance(self.data, type) and issubclass(self.data, EnumBase))
    even = property(lambda self: not self.data % 2 if isinstance(self.data, int) else NotImplemented)
    factory = property(lambda self: (self.datafield and self.data.default_factory is not DATA_MISSING))
    fileio = property(lambda self: isinstance(self.data, io.FileIO))
    float = property(lambda self: isinstance(self.data, float))
    frameinfo = property(lambda self: isinstance(self.data, inspect.FrameInfo))
    frametype = property(lambda self: isinstance(self.data, types.FrameType))

    @property
    def func(self):
        if self._func is None:
            self._func = self.data.fget if self.prop else self.data.__func__ \
                if (v := N.FUNC.hasget(self.data)) and callable(v) else self.data
        return self._func

    functiondef = property(lambda self: isinstance(self.data, ast.FunctionDef))
    functiontype = property(lambda self: isinstance(self.data, types.FunctionType))
    generator = property(lambda self: isinstance(self.data, Generator))
    generatortype = property(lambda self: isinstance(self.data, types.GeneratorType))
    genericalias = property(lambda self: isinstance(self.data, types.GenericAlias))
    getitem = property(lambda self: self.supports(GetItem))
    getmethod = property(lambda self: self.supports(GetMethod))
    getsetdescriptortype = property(lambda self: isinstance(self.data, types.GetSetDescriptorType))
    hashable = property(lambda self: bool(noexc(hash, self.data)))
    import_ast = property(lambda self: isinstance(self.data, ast.Import))

    @property
    def importname(self): return importname(self.data)

    importfrom = property(lambda self: isinstance(self.data, ast.ImportFrom))
    initvar = property(
        lambda self: (self.datafield and self.data._field_type is FIELD_INITVAR) or isinstance(
            self.data, dataclasses.InitVar))

    @property
    def installed(self):
        """
        Tests to see if ``module`` is available on the sys.path

        >>> assert Is('sys').installed is True
        >>> assert Is('fake').installed is False

        Returns:
            True if installed.
        """
        if self.str or hasattr(self.data, N.MODULE):
            try:
                __import__(self.data if self.str else self.data.__module__)
                return True
            except ImportError:
                return False
        return NotImplemented

    def instance(self, *args): return isinstance(self.data, args)

    int = property(lambda self: isinstance(self.data, int))
    io = property(lambda self: self.bytesio and self.stringio)  # :class:`typing.IO`
    iterable = property(lambda self: isinstance(self.data, Iterable))
    iterator = property(lambda self: isinstance(self.data, Iterator))
    lambda_ast = property(lambda self: isinstance(self.data, ast.Lambda))
    lambdatype = property(lambda self: isinstance(self.data, types.LambdaType))
    list = property(lambda self: isinstance(self.data, list))
    list_like = property(lambda self: N.GETITEM.has(self.data) and N.append.has(self.data))
    lst = property(lambda self: isinstance(self.data, (list, set, tuple)))
    mappingproxytype = property(lambda self: isinstance(self.data, types.MappingProxyType))
    mappingproxytype_sub = property(
        lambda self: isinstance(self.data, type) and issubclass(self.data, types.MappingProxyType))
    memberdescriptortype = property(lambda self: isinstance(self.data, types.MemberDescriptorType))
    method = property(
        lambda self: (self.methodtype or self.routine) and not any([self.classmethod, self.prop, self.static]))
    methoddescriptor = property(lambda self: inspect.ismethoddescriptor(self.data))
    methoddescriptortype = property(lambda self: isinstance(self.data, types.MethodDescriptorType))
    methodtype = property(lambda self: isinstance(self.data, types.MethodType))  # True if it is an instance method!.
    methodwrappertype = property(lambda self: isinstance(self.data, types.MethodWrapperType))
    methodwrappertype_sub = property(
        lambda self: isinstance(self.data, type) and issubclass(self.data, types.MethodWrapperType))
    missing = property(lambda self: isinstance(self.data, Missing))
    missing_or_factory = property(lambda self: self.datamissing or self.factory)
    mlst = property(lambda self: isinstance(self.data, (MutableMapping, list, set, tuple)))
    mm = property(lambda self: isinstance(self.data, MutableMapping))
    moduletype = property(lambda self: isinstance(self.data, (types.ModuleType, ast.Module)))
    namedtuple = property(lambda self: self.supports(Namedtuple))
    namedtupletyping = property(lambda self: self.supports(NamedTupleTyping))

    @property
    def noncomplex(self):
        """
        Returns True if *obj* is a special (weird) class, that is more complex
            than primitive data types, but is not a full object.
        Including:
            * :class:`~time.struct_time`
        """
        if self.cls is time.struct_time:
            return True
        return False

    none = property(lambda self: isinstance(self.data, type(None)))

    @property
    def object(self):
        """
        Returns True is obj is a reference to an object instance.

        >>> assert Is(1).object is True
        >>> assert Is(object()).object is True
        >>> assert Is(lambda x: 1).object is False

        Returns:
            True is obj is a reference to an object instance.
        """
        return isinstance(self.data, object) and not isinstance(self.data,
                                                                (type, types.FunctionType, types.BuiltinFunctionType))

    pathlib = property(lambda self: isinstance(self.data, pathlib.Path))
    picklable = property(lambda self: bool(noexc(pickle.dumps, self.data)))

    @property
    def primitive(self):
        """
        Helper method to see if the object is a basic data type. Unicode strings,
        integers, longs, floats, booleans, and None are considered primitive
        and will return True when passed into *is_primitive()*

        >>> assert Is(3).primitive is True
        >>> assert Is([4,4]).primitive is False

        """
        return self.cls in {str, bool, type(None), int, float}

    prop = property(lambda self: isinstance(self.data, property))
    propany = property(lambda self: self.prop or self.cached_property)

    def readonly(self, name='__readonly__'):
        """
        Is readonly object?

        Examples:
            >>> from bapy import Is
            >>>
            >>> class First:
            ...     __slots__ = ('_data', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_id', )
            >>>
            >>> assert isinstance(Is(Test()).readonly(), AttributeError)

        Returns:
            True if readonly.
        """
        name = nstr(name)
        value = None
        try:
            if name.has(self.data):
                value = getattr(self.data, name)
            setattr(self.data, name, value)
        except Exception as exception:
            return exception
        if value is not None:
            delattr(self.data, name)
        return False

    @property
    def reducible(self):
        """
        Returns false if of a type which have special casing,
        and should not have their __reduce__ methods used
        """
        # defaultdict may contain functions which we cannot serialise
        if not self.defaultdict:
            return True
        # sets are slightly slower in this case
        if self.cls in NON_REDUCTIBLE_TYPES:
            return False
        elif self.data is object:
            return False
        elif self.list_like:
            return False
        elif self.moduletype:
            return False
        elif self.reducible_sequence_subclass:
            return False
        elif isinstance(getattr(self.data, N.SLOTS, None), typing.get_args(IteratorTypes)):
            return False
        elif self.type and self.data.__module__ == datetime.__name__:
            return False
        return True

    reducible_sequence_subclass = property(lambda self: N.CLASS.has(self.data) and issubclass(self.cls, LST_TYPES))
    routine = property(lambda self: inspect.isroutine(self.data))
    sequence = property(lambda self: isinstance(self.data, Sequence))
    sequence_sub = property(lambda self: isinstance(self.data, type) and issubclass(self.data, Sequence))
    settype = property(lambda self: isinstance(self.data, set))
    setter = property(lambda self: isinstance(self.data, property) and self.data.fset is not None)

    @property
    def signature(self):
        """
        Function Signature.

        >>> import bapy.data.cls
        >>> from bapy import Is, MISSING
        >>> assert Is(bapy.data.cls.MroDataDictSlotMix.__init__).signature == \
        {'self': MISSING, 'dataclass_initvar': 'dataclass_initvar_2', \
        'slot_property_initvar': 'slot_property_initvar', 'slot_initvar': 'slot_initvar'}

        Returns:
          Function Signature.
        """
        sig = noexc(inspect.signature, self.data, default_=inspect.Signature())
        return {k: MISSING if v.default is inspect_empty else v.default for k, v in sig.parameters.items()}

    simple = property(lambda self: isinstance(self.data, Simple))
    sized = property(lambda self: isinstance(self.data, Sized))
    slotstype = property(lambda self: N.SLOTS.has(self.data))
    static = property(lambda self: isinstance(self.data, (staticmethod, types.BuiltinMethodType)))
    str = property(lambda self: isinstance(self.data, str))
    stringio = property(lambda self: isinstance(self.data, io.StringIO))  # :class:`typing.TextIO`

    def subclass(self, *args): return issubclass(self.cls, args)

    def supports(self, *args): return isinstance(self.data, args) or issubclass(self.cls, args)

    tracebacktype = property(lambda self: isinstance(self.data, types.TracebackType))
    tuple = property(lambda self: isinstance(self.data, tuple))
    type = property(lambda self: isinstance(self.data, type))

    @property
    def varstype(self):
        if self._varstype is None:
            self._varstype = False
            if not self.type and N.DICT.has(self.data):
                self._varstype = True
            else:
                for C in self.cls.__mro__:
                    if not self.__class__(C).builtinclassnodict and N.SLOTS not in C.__dict__:
                        self._varstype = True
        return self._varstype

    wrapperdescriptortype = property(lambda self: isinstance(self.data, types.WrapperDescriptorType))

    def writeable(self, name):
        # noinspection PyUnresolvedReferences
        """
        Checks if an attr is writeable in object.

        Examples:
            >>> from bapy import Is
            >>>
            >>> class First:
            ...     __slots__ = ('_data', )
            >>>
            >>> class Test(First):
            ...     __slots__ = ('_id', )
            >>>
            >>> test = Test()
            >>> es = Is(test)
            >>> assert es.writeable('_id') == True
            >>> assert es.writeable('test') == False
            >>> assert Is(test.__class__).writeable('test') == True
            >>> test.__class__.test = 2
            >>> assert test.test == 2
            >>> assert Is(test.__class__).writeable('cls') == True
            >>> object.__setattr__(test.__class__, 'cls', 2) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            TypeError: can't apply this __setattr__ to type object

        Args:
            name: attribute name.

        Returns:
            True if can be written.
        """
        return not self.readonly(name)


class Kind(EnumBase, metaclass=EnumBaseMeta):
    CLASSMETHOD = 'class method'
    CLASSVAR = enum.auto()
    DATA = enum.auto()
    FACTORY = enum.auto()
    INITVAR = enum.auto()
    METHOD = enum.auto()
    PROPERTY = property.__name__
    STATICMETHOD = 'static method'
    UNKNOWN = enum.auto()


class MatchError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__('No match', *[f'{key}: {value}' for key, value in kwargs.items()], *args)


class Missing:
    name = 'MISSING'
    __slots__ = ()

    def __hash__(self): return hash((self.__class__, self.name,))

    def __reduce__(self): return self.__class__, (self.name,)

    def __repr__(self): return f'<{self.name}>'


MISSING = Missing()
DictStrMissingAny = dict[str, typing.Union[Missing, typing.Any]]


class ModuleBase(EnumBase, metaclass=EnumBaseMeta):
    get = property(lambda self: globals().get(self()))
    load = property(lambda self: importlib.import_module(self()))


class Module(ModuleBase):
    """Module Enum Class."""
    FUNCTOOLS = enum.auto()
    TYPING = enum.auto()


class nstr(str):
    """Value Str Class."""
    __slots__ = ('name',)

    def __new__(cls, value='', *args, **kwargs):
        v = value
        value = super().__new__(cls, value)
        value = cls(f'__{cls.lower(value)}__') if cls.isupper(value) else value
        value.name = v
        return value

    def __call__(self, data=None): return self in data if isinstance(data, Container) else hasattr(data, self)

    # noinspection PyUnusedLocal
    def __init__(self, value=''): super().__init__()

    def get(self, obj, default=None):
        """
        Get key/attr value.

        Args:
            obj: object.
            default: default value (default: None).

        Returns:
            Value.
        """
        return hasget(obj, name=self, default=default)

    def getset(self, obj, default=None, setvalue=True):
        """
        Get key/attr value and sets if does not exists.

        Args:
            obj: object.
            default: default value (default: None).
            setvalue: setattr in object if AttributeError (default: True).

        Returns:
            Value.
        """
        return getset(obj, name=self, default=default, setvalue=setvalue)

    def has(self, obj):
        """
        Checks if object/dict has attr/key.

        >>> class Test:
        ...     __repr_newline__ = True
        >>>
        >>> assert N.REPR_NEWLINE.has(Test()) is True
        >>> assert N.REPR_EXCLUDE.has(Test()) is False
        >>> assert N.MODULE.has(tuple) is True
        >>> assert N.NAME.has(tuple) is True
        >>> assert N.FILE.has(tuple) is False
        >>> assert N.FILE.has(asyncio) is True
        >>> assert N.name.has({'name': ''}) is True
        >>> assert N.name.has({1: 1}) is False

        Args:
            obj: object.

        Returns:
            True if object/dict has attr/key.
        """
        return has(obj, self)

    def hasget(self, obj, default=None): return hasget(obj, self, default=default)

    def hasgetany(self, obj, default=None): return hasgetany(obj, self, default=default)

    @property
    def getter(self):
        """
        Value Getter.

        >>> assert N.MODULE.getter(tuple) == 'builtins'
        >>> assert N.NAME.getter(tuple) == 'tuple'
        >>> assert 'asyncio/__init__.py' in N.FILE.getter(asyncio)

        Returns:
            getter(str)
        """
        return getter(self)

    def parse(self): return NParser(self())


N = type('N', (object,), {
    __i: nstr(__i) for __i in (
        'ABOUT', 'ABSTRACTMETHODS', 'AUTHOR', 'ADAPT', 'ALL', 'ALLOC', 'ANNOTATIONS',
        'ARGS', 'ASDICT', 'ATTRIBUTES', 'BASE', 'BASICSIZE', 'BUILD_CLASS', 'BUILTINS',
        'CACHE_CLEAR', 'CACHE_INFO', 'CACHED', 'CLASS', 'CODE', 'CONFORM', 'CONTAINS',
        'CREDITS', 'COPY', 'COPYRIGHT', 'CVSID', 'DATACLASS_FIELDS', 'DATACLASS_PARAMS',
        'DATE', 'DECIMAL_CONTEXT', 'DEEPCOPY', 'DELATTR', 'DICT', 'DICTOFFSET',
        'DIR', 'DOC', 'DOCFORMAT', 'EMAIL', 'EQ', 'EXCEPTION', 'FILE', 'FLAGS', 'FUNC', 'GET',
        'GETATTRIBUTE', 'GETFORMAT', 'GETINITARGS', 'GETITEM', 'GETNEWARGS', 'GETSTATE',
        'HASH', 'HASH_EXCLUDE', 'IGNORE_ATTR', 'IGNORE_COPY', 'IGNORE_HASH', 'IGNORE_INIT',
        'IGNORE_KWARG', 'IGNORE_REPR', 'IGNORE_STATE', 'IGNORE_STR', 'IMPORT', 'INIT', 'INIT_SUBCLASS',
        'INITIALIZING', 'ISABSTRACTMETHOD', 'ITEMSIZE', 'LEN', 'LIBMPDEC_VERSION', 'LOADER',
        'LTRACE', 'MAIN', 'MEMBERS', 'METHODS', 'MODULE', 'MP_MAIN', 'MRO', 'NAME', 'NEW', 'NEW_MEMBER',
        'NEW_OBJ', 'NEW_OBJ_EX', 'OBJ_CLASS', 'OBJCLASS', 'PACKAGE', 'POST_INIT', 'PREPARE',
        'QUALNAME', 'REDUCE', 'REDUCE_EX', 'REPR', 'REPR_EXCLUDE', 'REPR_NEWLINE',
        'REPR_PPROPERTY', 'RETURN', 'SELF_CLASS', 'SETATTR', 'SETFORMAT', 'SETSTATE',
        'SIGNATURE', 'SIZEOF', 'SLOTNAMES', 'SLOTS', 'SPEC', 'STATE', 'STATUS', 'STR',
        'SUBCLASSHOOK', 'TEST', 'TEXT_SIGNATURE', 'THIS_CLASS', 'TRUNC', 'VERSION', 'WARNING_REGISTRY',
        'WEAKREF', 'WEAKREFOFFSET', 'WRAPPED', '_asdict', '_cls', '_copy', '_count', '_data',
        '_extend', '_external', '_field_defaults', '_field_type', '_fields', '_file', '_filename',
        '_frame', '_func', '_function', '_get', '_globals', '_id', '_index', '_ip', '_item',
        '_items', '_key', '_keys', '_kind', '_locals', '_name', '_node', '_origin', '_obj', '_object',
        '_path', '_repo', '_RV', '_rv', '_pypi', '_remove', '_reverse', '_sort', '_source', '_update',
        '_value', '_values', '_vars', 'add', 'append', 'args', 'asdict', 'attr', 'attrs',
        'authorized_keys', 'backup', 'cls', 'clear', 'cli', 'co_name', 'code_context', 'compare',
        'copy', 'copyright', 'count', 'credits', 'data', 'default', 'default_factory',
        'defaults', 'docs', 'endswith', 'exit', 'extend', 'external', 'f_back', 'f_code',
        'f_globals', 'f_lineno', 'f_locals', 'file', 'filename', 'frame', 'func', 'function',
        'get', 'globals', 'hash', 'help', 'id', 'id_rsa', 'ignore', 'index', 'init', 'ip', 'item', 'items',
        'kali', 'key', 'keys', 'kind', 'kwarg', 'kwargs', 'kwargs_dict', 'license', 'lineno',
        'locals', 'metadata', 'name', 'node', 'obj', 'object', 'origin', 'path', 'pop', 'popitem',
        'public', 'pypi', 'PYPI', 'quit', 'remove', 'repo', 'REPO', 'repr', 'rv', 'reverse',
        'search', 'scripts', 'self', 'sort', 'source', 'SOURCE', 'startswith', 'templates', 'test',
        'tests', 'tb_frame', 'tb_lineno', 'tb_next', 'tmp', 'type', 'ubuntu', 'update', 'value',
        'values', 'values_dict', 'vars', 'venv',
    )
} | dict(os.environ) | {
             '__slots__': (),
             '__repr__': lambda self: reprcls(data=self, line=True, **self._dict_),
             '_dict_': classmethod(lambda cls: {k: v for k, v in cls.__dict__.items() if notstart(k)}),
             'BUILTIN_OTHER': classmethod(lambda cls: tuple(
                 map(BUILTIN.get, (cls.DOC, cls.IMPORT, cls.SPEC, cls.copyright, cls.credits, cls.exit,
                                   cls.help, cls.license, cls.quit,))
             )),
             'MROITEMS': classmethod(lambda cls: {
                 cls.IGNORE_HASH: (cls.args, cls.kwargs), cls.IGNORE_INIT: (),
                 cls.IGNORE_REPR: (cls.args, cls.kwargs),
                 cls.IGNORE_STATE: (cls.ALLOC, cls.ANNOTATIONS, cls.ARGS, cls.BUILD_CLASS, cls.BUILTINS, cls.CLASS,
                                    cls.DATACLASS_FIELDS, cls.DATACLASS_PARAMS, cls.DICT, cls.DOC, cls.HASH,
                                    cls.MODULE,
                                    cls.SLOTS, cls.SLOTNAMES, cls.WEAKREF, cls._fields, cls._field_defaults),
                 N.SLOTS: (),
             }),
             'SIGNATURES': classmethod(lambda cls: {cls.NEW: cls.cls, cls.INIT: cls.self, cls.POST_INIT: cls.self}),
             '__class_getitem__': lambda x, y: x.__dict__[y] if y in x.__dict__ and y not in {
                 *{'__slots__', '_dict_', '__repr__', '__class_getitem__'}, *dir(type)
             } else nstr(y),
         })


class NameAttr(metaclass=abc.ABCMeta):
    """Supports name attribute."""
    __slots__ = tuple()

    @property
    @abc.abstractmethod
    def name(self): return

    @classmethod
    def __subclasshook__(cls, C):
        if cls is NameAttr:
            n = N.name.hasget(C)
            return n and not callable(n) and not issubclass(C, MutableMapping)
        return NotImplemented


class Namedtuple(metaclass=abc.ABCMeta):
    """
    namedtupl.

    Examples:
        >>> named = collections.namedtuple('named', 'a', defaults=('a', ))
        >>>
        >>> assert Is(named()).namedtuple == True
        >>> assert Is(named).namedtuple == True
        >>>
        >>> assert Is(named()).tuple == True
        >>> assert issubclass(named, tuple) == True
    """
    _fields = tuple()
    _field_defaults = dict()

    @abc.abstractmethod
    def _asdict(self):
        return dict()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Namedtuple:
            return callable(N._asdict.hasget(C)) and issubclass(C, tuple) and N._fields.has(
                C) and N._field_defaults.has(C)
        return NotImplemented


class NamedTupleTyping(metaclass=abc.ABCMeta):
    """
    NamedTuple.

    Examples:
        >>> named = collections.namedtuple('named', 'a', defaults=('a', ))
        >>> from typing import NamedTuple
        >>> Named = NamedTuple('Named', a=str)
        >>>
        >>> assert Is(named()).namedtupletyping == False
        >>> assert Is(named).namedtupletyping == False
        >>>
        >>> assert Is(Named('a')).namedtupletyping == True
        >>> assert Is(Named).namedtupletyping == True
        >>>
        >>> assert Is(named()).tuple == True
        >>> assert issubclass(named, tuple) == True
    """
    __annotations__ = dict()
    _fields = tuple()
    _field_defaults = dict()

    @abc.abstractmethod
    def _asdict(self):
        return dict()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is NamedTupleTyping:
            return issubclass(C, Namedtuple) and issubclass(C, AnnotationsAttr)
        return NotImplemented


class NParser:
    __slots__ = ('data', 'default', )
    def __init__(self, data='', default=None): self.data, self.default = data, default
    def __repr__(self): return f'{self.__class__.__name__}({self.asdict()})'
    def asdict(self): return getprops(self)

    @property
    def domain(self):
        if self.data:
            if noexc(socket.gethostbyname, self.data):
                return furl.furl(host=self.data)
        return self.default

    @property
    def email(self):
        if self.data:
            if rv := noexc(marshmallow.validate.Email(), self.data, default_=self.default):
                value = rv.split('@')
                return furl.furl(host=value[1], username=value[0])
        return self.default

    @property
    def environ(self):
        if self.true is not None:
            return self.true
        if self.integer is not None:
            return self.integer
        if self.email is not None:
            return self.email
        if self.domain is not None:
            return self.domain
        if self.url is not None:
            return self.url
        if self.ip is not None:
            return self.ip
        if self.path is not None:
            return self.path
        return self.data

    @property
    def integer(self):
        if self.data:
            return noexc(marshmallow.fields.Integer().deserialize, self.data, default_=self.default)
        return self.default

    @property
    def ip(self):
        if self.data:
            return noexc(ipaddress.ip_address, self.data, default_=self.default)
        return self.default

    @property
    def log_level(self):
        if self.data:
            rv = self.data.upper()
            if hasattr(logging, rv):
                return rv
        return self.default

    @property
    def log_value(self):
        if self.data:
            if rv := self.log_level:
                return getattr(logging, rv, self.default)
            elif self.integer:
                level = self.data.upper()
                if hasattr(logging, self.data) and isinstance(getattr(logging, level), int):
                    return getattr(logging, level)
        return self.default

    @property
    def path(self):
        if self.data:
            if any([self.domain, self.email, self.integer, self.ip, self.true, self.url]):
                return self.default
            if NEWLINE not in self.data and '*' not in self.data and '$' not in self.data and '/' in self.data:
                return pathlib.Path(self.data)
        return self.default

    @property
    def true(self):
        if self.data:
            return noexc(marshmallow.fields.Boolean().deserialize, self.data, default_=self.default)
        return self.default

    @property
    def url(self):
        if self.data:
            if rv := noexc(marshmallow.validate.URL(), self.data):
                return furl.furl(rv)
        return self.default


ObjBase = collections.namedtuple('ObjBase', 'c data')


class Obj(ObjBase):
    """Obj Info."""
    cache = {}
    __slots__ = ()

    def __new__(cls, data):
        kw = dict(c=Class.from_obj(data), data=data)
        return super().__new__(cls, **kw)

    def __iter__(self):
        """
        Iter: Class & data and Attributes names.

        Returns:
            Iter: Class & data and Attributes names.
        """
        for i in sorted({*self.c.attribute, *(self.data.__dict__ if N.DICT(self.data) else {})}):
            yield i

    @property
    def deepcopy(self):
        """
        Deep copy object

        Tries again after calling :class:`rc.Es.state_methods` in case of PicklingError RecursionError.

        Examples:
            >>> from copy import deepcopy
            >>> from environs import Env as Environs
            >>> from bapy import Is, Obj
            >>>
            >>> deepcopy(Environs()) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            RecursionError: maximum recursion depth exceeded
            >>> env = Environs()
            >>> term = env('TERM')
            >>> env
            <Env {'TERM': 'xterm-256color'}>
            >>> env_copy = env
            >>> assert id(env_copy) == id(env)
            >>> env_deepcopy = Obj(env).deepcopy
            >>> env_deepcopy
            <Env {'TERM': 'xterm-256color'}>
            >>> assert id(env_deepcopy) != id(env)
            >>> assert id(env_deepcopy._values) != id(env._values)

        Returns:
            Deep copied object.
        """
        try:
            return copy.deepcopy(self.data)
        except (pickle.PicklingError, RecursionError):
            return copy.deepcopy(self.state_methods)

    def hash(self, access=Access.PROTECTED, prop=True):
        """
        Hash Dict.

        >>> import bapy.data.cls
        >>> from bapy import Obj, MISSING
        >>> a = Obj(bapy.data.cls.MroAsync()).hash(prop=False)
        >>> assert a == { \
            '_async_classmethod': '_async_classmethod', \
            '_async_method': '_async_method', \
            '_async_prop': '_async_prop', \
            '_async_staticmethod': '_async_staticmethod', \
            '_classmethod': '_classmethod', \
            '_cprop': '_cprop', \
            '_method': '_method', \
            '_prop': '_prop', \
            '_staticmethod': '_staticmethod', \
        }
        >>> a, m = Obj(bapy.data.cls.MroAsync()).hash(), Obj(bapy.data.cls.MroDataDictSlotMix()).hash()
        >>> assert a == { \
            '_async_classmethod': '_async_classmethod', \
            '_async_method': '_async_method', \
            '_async_prop': '_async_prop', \
            '_async_staticmethod': '_async_staticmethod', \
            '_classmethod': '_classmethod', \
            '_method': '_method', \
            '_staticmethod': '_staticmethod', \
            'cprop': '_cprop', \
            'prop': '_prop' \
        }
        >>> assert m == {'_MroData__dataclass_default_factory': {}, '_MroData__dataclass_default_factory_init': {}, \
                         'dataclass_default_factory': {}, 'dataclass_default_factory_init': {}, \
                         'dataclass_default_init': 'dataclass_default_init', 'dataclass_str': 'dataclass_integer', \
                         'slot': 'slot_initvar', 'slot_property': 'slot_property_initvar', \
                         'subclass_dynamic': 'subclass_dynamic'}
        >>> assert Obj(bapy.data.cls.MroValuesSub(1)).hash() == {'_hash': MISSING, '_slot': MISSING, 'attr': MISSING, \
            'init': 1, 'init_ignore': 'init_ignore', 'missing': MISSING, 'test': MISSING, }

        Args:
            access: include prefix.
            prop: include properties when instance.

        Returns:
            Hash Dict.
        """
        return self.vars(access=access, ignore=lambda x, y: x in self.c.mroitems[N.IGNORE_HASH], prop=prop)

    def init(self, access=Access.PROTECTED):
        """
        Init Dict.

        >>> import bapy.data.cls
        >>> from bapy import Obj, MISSING
        >>> a, m = Obj(bapy.data.cls.MroAsync()).init(), Obj(bapy.data.cls.MroDataDictSlotMix()).init()
        >>> assert a == {}
        >>> assert m == {'_MroData__dataclass_classvar': '__dataclass_classvar', \
                         '_MroData__dataclass_default_factory_init': {}, \
                         'dataclass_classvar': 'dataclass_classvar', 'dataclass_default_factory_init': {}, \
                         'dataclass_default_init': 'dataclass_default_init', 'dataclass_initvar': 'dataclass_initvar', \
                         'dataclass_str': 'dataclass_integer', \
                         'slot_initvar': 'slot_initvar', 'slot_property_initvar': 'slot_property_initvar'}
        >>> assert Obj(bapy.data.cls.MroValuesSub(1)).init() == {}

        Args:
            access: include prefix.

        Returns:
            Init Dict.
        """
        return dict_sort({k: v for k, v in self.c.init.items()
                          if Access[k] >= access and v != MISSING and k not in self.c.mroitems[N.IGNORE_INIT]})

    @property
    def pickles(self):
        """
        Pickles object (dumps).

        Tries again after calling :class:`rc.Es.state_methods` in case of PicklingError RecursionError.

        Returns:
            Pickle object (bytes) or None if methods added to self.data so it can be called again.
        """
        try:
            return pickle.dumps(self.data)
        except (pickle.PicklingError, RecursionError):
            return pickle.dumps(self.state_methods)

    def repr(self, access=Access.PROTECTED, both=False, prop=True):
        """
        Repr Dict.

        >>> import bapy.data.cls
        >>> from bapy import Obj, MISSING
        >>> a = Obj(bapy.data.cls.MroAsync()).repr(prop=False)
        >>> assert a == { \
            '_async_classmethod': '_async_classmethod', \
            '_async_method': '_async_method', \
            '_async_prop': '_async_prop', \
            '_async_staticmethod': '_async_staticmethod', \
            '_classmethod': '_classmethod', \
            '_cprop': '_cprop', \
            '_method': '_method', \
            '_prop': '_prop', \
            '_staticmethod': '_staticmethod', \
        }
        >>> a, m = Obj(bapy.data.cls.MroAsync()).repr(), Obj(bapy.data.cls.MroDataDictSlotMix()).repr()
        >>> assert a == { \
            '_async_classmethod': '_async_classmethod', \
            '_async_method': '_async_method', \
            '_async_prop': '_async_prop', \
            '_async_staticmethod': '_async_staticmethod', \
            '_classmethod': '_classmethod', \
            '_method': '_method', \
            '_staticmethod': '_staticmethod', \
            'cprop': '_cprop', \
            'prop': '_prop' \
        }
        >>> assert m == {'_MroData__dataclass_default_factory': {}, '_MroData__dataclass_default_factory_init': {}, \
                         'dataclass_default_factory': {}, 'dataclass_default_factory_init': {}, \
                         'dataclass_default_init': 'dataclass_default_init', 'dataclass_str': 'dataclass_integer', \
                         'slot': 'slot_initvar', 'slot_property': 'slot_property_initvar', \
                         'subclass_dynamic': 'subclass_dynamic'}
        >>> assert Obj(bapy.data.cls.MroValuesSub(1)).repr() == {'_prop': MISSING, '_repr': MISSING, '_slot': MISSING, \
            'init': 1, 'init_ignore': 'init_ignore', 'missing': MISSING}

        Args:
            access: include prefix.
            both: when instance both includes classvars.
            prop: include properties when instance.

        Returns:
            Repr Dict.
        """
        v = self.vars(access=access, both=both, ignore=lambda x, y: x in self.c.mroitems[N.IGNORE_REPR], prop=prop)
        return v

    def state(self):
        """
        State Dict.

        >>> import bapy.data.cls
        >>> from bapy import Obj, MISSING
        >>> a, m = Obj(bapy.data.cls.MroAsync()).state(), Obj(bapy.data.cls.MroDataDictSlotMix()).state()
        >>> assert a == {}
        >>> assert m == {'_MroData__dataclass_default_factory': {}, '_MroData__dataclass_default_factory_init': {}, \
                         '_slot_property': 'slot_property_initvar', \
                         'dataclass_default_factory': {}, 'dataclass_default_factory_init': {}, \
                         'dataclass_default_init': 'dataclass_default_init', 'dataclass_str': 'dataclass_integer', \
                         'slot': 'slot_initvar', \
                         'subclass_dynamic': 'subclass_dynamic'}
        >>> assert Obj(bapy.data.cls.MroValuesSub(1)).state() == {'_prop': MISSING, '_repr': MISSING, \
            '_slot': MISSING, 'init': 1, '_test': MISSING, 'init_ignore': 'init_ignore', 'missing': MISSING}

        Returns:
            State Dict.
        """
        return self.vars(access=Access.PRIVATE, ignore=lambda x, y: x in self.c.mroitems[N.IGNORE_STATE], state=True,
                         prop=False)

    @property
    def state_methods(self):
        """
        Add :class:`rc.BaseState` methods to object if PicklingError or RecursionError if class in mro is
        in :data `rc.STATE_ATTRS`:
            - :meth:`rc.BaseState.__getstate__`: (pickle) when state=None.
            - :meth:`rc.BaseState.__setstate__`: (unpickle) when state.

        Raises:
            PicklingError: Object has one or both state methods.
            AttributeError: Read-only.
            NotImplementedError: No mro items in STATE_ATTRS.

        Returns:
            Object with __getstate__ and __setstate__ methods added.
        """

        def _state(*args):
            if args and len(args) == 1:
                return getsetstate(args[0])
            elif args and len(args) == 2:
                return getsetstate(args[0], args[1])

        setstate = None
        if (getstate := hasattr(self.data, N.GETSTATE)) or (setstate := hasattr(self.data, N.SETSTATE)):
            raise pickle.PicklingError(f'Object {self.data}, has one or both state methods: {getstate=}, {setstate=}')
        found = False
        for C in self.c.mro:
            cache_key = C, self.__class__.state_methods.fget
            if cache_key not in Obj.cache:
                Obj.cache[cache_key] = self.state()
            if cache_key in Obj.cache:
                for attr in (N.GETSTATE, N.SETSTATE,):
                    es = Is(self.data.__class__)
                    if not es.writeable(attr):
                        exc = es.readonly(attr)
                        raise AttributeError(f'Read-only: {self.data=}') from exc
                self.data.__class__.__getstate__ = _state
                self.data.__class__.__setstate__ = _state
                found = True
        if found:
            return self.data
        else:
            raise NotImplementedError(f'No mro: {self.c.mro} found for: {self.data=}')

    @property
    def unpickles(self):
        """Unpickles object (loads)."""
        return pickle.loads(self.data)

    def vars(self, access=Access.PROTECTED, both=False, ignore=lambda x, y: False, prop=True, state=False):
        """
        Data Attributes for Class, Instance or Class & Instance (both).

        >>> import bapy.data.cls
        >>> from bapy import Obj, MISSING
        >>> a, m = Obj(bapy.data.cls.MroAsync()).vars(), Obj(bapy.data.cls.MroDataDictSlotMix()).vars()
        >>> assert a == { \
            '_async_classmethod': '_async_classmethod', \
            '_async_method': '_async_method', \
            '_async_prop': '_async_prop', \
            '_async_staticmethod': '_async_staticmethod', \
            '_classmethod': '_classmethod', \
            '_method': '_method', \
            '_staticmethod': '_staticmethod', \
            'args': MISSING, \
            'cprop': '_cprop', \
            'kwargs': MISSING, \
            'prop': '_prop' \
        }
        >>> assert m == {'_MroData__dataclass_default_factory': {}, '_MroData__dataclass_default_factory_init': {}, \
                         'dataclass_default_factory': {}, 'dataclass_default_factory_init': {}, \
                         'dataclass_default_init': 'dataclass_default_init', 'dataclass_str': 'dataclass_integer', \
                         'slot': 'slot_initvar', 'slot_property': 'slot_property_initvar', \
                         'subclass_dynamic': 'subclass_dynamic'}

        Args:
            access: include prefix.
            both: when instance both includes classvars.
            ignore: predicate to ignore key/value.
            prop: include properties when instance.
            state: do not include class even if not init method.

        Returns:
            Dict with Data Attributes for Class, Instance or Class & Instance (both).
        """
        return self.c.vars(data=self.data, access=access, both=both, ignore=ignore, prop=prop, state=state)


class PIs(EnumBase, metaclass=EnumBaseMeta):
    DIR = 'is_dir'
    FILE = 'is_file'


class PMode(EnumBase, metaclass=EnumBaseMeta):
    DIR = 0o666
    FILE = 0o777
    X = 0o755


class POption(EnumBase, metaclass=EnumBaseMeta):
    BOTH = enum.auto()
    DIRS = enum.auto()
    FILES = enum.auto()


class POutput(EnumBase, metaclass=EnumBaseMeta):
    BOTH = enum.auto()
    DICT = dict
    LIST = list
    NAMED = collections.namedtuple
    TUPLE = tuple


class PSuffixBase(EnumBase, metaclass=EnumBaseMeta):
    """NBase Base Enum Class."""

    def _generate_next_value_(self, *args): return self if self == 'NO' else f'.{self.lower()}'


class PSuffix(PSuffixBase):
    NO = str()
    BASH = enum.auto()
    ENV = enum.auto()
    GIT = enum.auto()
    GITCONFIG = enum.auto()
    INI = enum.auto()
    J2 = enum.auto()
    JINJA2 = enum.auto()
    LOG = enum.auto()
    MONGO = enum.auto()
    OUT = enum.auto()
    PY = enum.auto()
    RLOG = enum.auto()
    SH = enum.auto()
    SHELVE = enum.auto()
    SSH = enum.auto()
    TOML = enum.auto()
    YAML = enum.auto()
    YML = enum.auto()


class Path(pathlib.Path, pathlib.PurePosixPath):
    """Path Helper Class."""
    __slots__ = ('_previous', '_rv',)

    def __call__(self, name=None, file=not FILE_DEFAULT, group=None, mode=None, su=not SUDO_DEFAULT, u=None):
        # noinspection PyArgumentList
        return (self.touch if file else self.mkdir)(name=name, group=group, mode=mode, su=su, u=u)

    def __contains__(self, value): return all([i in self.resolved.parts for i in toiter(value)])

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._cparts == other._cparts

    def __hash__(self): return self._hash if hasattr(self, '_hash') else hash(tuple(self._cparts))

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._cparts < other._cparts

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._cparts <= other._cparts

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._cparts > other._cparts

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._cparts >= other._cparts

    def _is_file(self):
        p = self.resolved
        while True:
            if p.is_file():
                return p.text
            p = p.parent
            if p == Path('/'):
                return None

    def append_text(self, data, encoding=None, errors=None):
        """Open the file in text mode, append to it, and close the file."""
        if not isinstance(data, str):
            raise TypeError(f'data must be str, not {data.__class__.__name__}')
        with self.open(mode='a', encoding=encoding, errors=errors) as f:
            return f.write(data)

    def c_(self, p='-'):
        """
        Change working dir, returns post_init Path and stores previous.

        Examples:
            >>> path = Path()
            >>> local = path.c_('/usr/local')
            >>> usr = local.parent
            >>> assert usr.text == usr.str == str(usr.resolved)
            >>> assert Path.cwd() == usr.cwd()
            >>> assert 'local' in local
            >>> assert local.has('usr local')
            >>> assert not local.has('usr root')
            >>> assert local.c_() == path.resolved

        Args:
            p: path

        Returns:
            Path: P
        """
        if not hasattr(self, '_previous'):
            # noinspection PyAttributeOutsideInit
            self._previous = self.cwd()
        # noinspection PyArgumentList
        p = type(self)(self._previous if p == '-' else p)
        previous = self.cwd()
        p.chdir()
        p = self.cwd()
        p._previous = previous
        return p

    @property
    @contextlib.contextmanager
    def cd(self):
        """
        Change dir context manger to self and comes back to Path.cwd() when finished.

        Examples:
            >>> new = Path('/usr/local').resolved
            >>> p = Path.cwd()
            >>> with new.cd as prev:
            ...     assert new == Path.cwd()
            ...     assert prev == p
            >>> assert p == Path.cwd()

        Returns:
            CWD when invoked.
        """
        cwd = self.cwd()
        try:
            self.parent.chdir() if self.is_file() else self().chdir()
            yield cwd
        finally:
            cwd.chdir()

    def chdir(self): os.chdir(self.text)

    def chmod(self, mode=None):
        os.system(f'{user.sudo("chmod", SUDO_DEFAULT)} {mode or (755 if self.resolved.is_dir() else 644)} '
                  f'{shlex.quote(self.resolved.text)}')
        return self

    def chown(self, group=None, u=None):
        os.system(f'{user.sudo("chown", SUDO_DEFAULT)} {u or user.name}:{group or user.gname} '
                  f'{shlex.quote(self.resolved.text)}')
        return self

    endseparator = property(lambda self: self.text + os.sep)

    def fd(self, *args, **kwargs):
        return os.open(self.text, *args, **kwargs)

    @property
    def find_packages(self):
        try:
            with self.cd:
                packages = setuptools.find_packages()
        except FileNotFoundError:
            packages = list()
        return packages

    def find_up(self, file=PIs.FILE, name=PSuffix.ENV, uppermost=False):
        """
        Find file or dir up.

        >>> import email.mime.application
        >>> from bapy import Path
        >>> email_path = Path(email.mime.application.__file__)
        >>> email_path.find_up(name=INIT_PY).path  # doctest: +ELLIPSIS
        Path('.../lib/python.../email/mime/__init__.py')
        >>> email_path.find_up(name=INIT_PY, uppermost=True).path  # doctest: +ELLIPSIS
        Path('.../lib/python.../email/__init__.py')

        Args:
            file: file.
            name: name.
            uppermost: uppermost found.

        Returns:
            Optional[Union[tuple[Optional[Path], Optional[Path]]], Path]:
        """
        name = name if isinstance(name, str) else name()
        start = self.resolved if self.is_dir() else self.parent.resolved
        before = self.resolved
        latest = None
        while True:
            find = start / name
            if getattr(find, file())():
                if not uppermost:
                    return FindUp(find, before)
                latest = find
            before = start
            start = start.parent
            if start == Path('/'):
                return FindUp(latest, before)

    #
    # @classmethod
    # def git(cls, path=None):
    #     url = cls.giturl(path)
    #     path = cls.gitpath(path)
    #     return GitTop(str(url.path).rpartition('/')[2].split('.')[0] if url else path.name if
    #     path else None, url, path)
    #
    # # noinspection PyArgumentList
    # @classmethod
    # def gitpath(cls, path=None):
    #     rv = None
    #     if (path and ((path := cls(path).resolve()).exists() or (path := cls.cwd() / path).resolve().exists())) \
    #             or (path := cls.cwd().resolve()):
    #         with cls(path).cd:
    #             if path := run('git rev-parse --show-toplevel', shell=True, capture_output=True,
    #                            text=True).stdout.removesuffix('\n'):
    #                 return cls(path)
    #     return rv
    #
    # @classmethod
    # def giturl(cls, path=None):
    #     rv = None
    #     if (path and ((path := cls(path).resolve()).exists() or (path := cls.cwd() / path).resolve().exists())) \
    #             or (path := cls.cwd().resolve()):
    #         with cls(path).cd:
    #             if path := run('git config --get remote.origin.url', shell=True, capture_output=True,
    #                            text=True).stdout.removesuffix('\n'):
    #                 return cls(path)
    #             # rv = furl(stdout[0]) if (stdout := cmd('git config --get remote.origin.url').stdout) else None
    #     return rv

    @classmethod
    def from_obj(cls, obj):
        """
        Get Path from object or str(obj.

        Args:
            obj: object.

        Returns:
            Path.
        """
        pass

    def has(self, value: str):
        """
        Only checks text and not resolved as __contains__.

        Args:
            value:

        Returns:
            bool
        """

        return all([item in self.text for item in toiter(value)])

    @classmethod
    def home(cls, name: str = None, file: bool = not FILE_DEFAULT):
        """
        Returns home if not name or creates file or dir.

        Args:
            name: name.
            file: file.

        Returns:
            Path:
        """
        return cls(user.home)(name, file)

    # # noinspection PyArgumentList
    # @classmethod
    # @cache
    # def importer(cls, modname: str, s=None):
    #     for frame in s or inspect.stack():
    #         if all([frame.function == N._MODULE, frame.index == 0, 'PyCharm' not in frame.filename,
    #                 cls(frame.filename).suffix,
    #                 False if 'setup.py' in frame.filename and setuptools.__name__ in frame.frame.f_globals else True,
    #                 (c[0].startswith(f'from {modname} import') or
    #                  c[0].startswith(f'import {modname}'))
    #                 if (c := frame.code_context) else False, not cls(frame.filename).installedbin]):
    #             return cls(frame.filename), frame.frame

    @property
    def installed(self):
        # noinspection PyCompatibility
        """
        Relative path to site/user packages or scripts dir.

        Examples:
            >>> import pip, bapy
            >>> from shutil import which
            >>> assert Path(pip.__file__).installed == Path('pip/__init__.py')
            >>> assert Path(which(pip.__name__)).installed == Path('pip')
            >>> assert Path(bapy.__file__).installed is None

        Returns:
            Relative path to install lib/dir if file in self is installed.
        """
        return self.installedpy or self.installedbin

    @property
    def installedbin(self):
        """
        Relative path to scripts dir.

        Returns:
            Optional[Path]:
        """
        return self.resolve().relative(SCRIPTS)

    @property
    def installedpy(self):
        """
        Relative path to site/user packages.

        Returns:
            Optional[Path]:
        """
        for s in site.getsitepackages() + toiter(site.USER_SITE) if site.USER_SITE else []:
            if p := self.relative(s):
                return p

    @classmethod
    def internal(cls):
        file = cls(__file__)
        path = file.path()
        return PathInternal(file=file, path=path, package=path.name)

    def j2(self, dest=None, stream=True, variables=None):
        f = inspect.stack()[1]
        variables = variables if variables else f.frame.f_globals.copy() | f.frame.f_locals.copy()
        return [v(variables).dump(Path(dest / k).text) for k, v in self.templates(stream=stream).items()] \
            if dest and stream else {k: v(variables) for k, v in self.templates(stream=stream).items()}

    def mkdir(self, name=None, group=None, mode=755, su=not SUDO_DEFAULT, u=None):
        """
        Add directory, make directory and return post_init Path.

        Args:
            name: name
            group: group
            mode: mode
            su: su
            u: user

        Returns:
            Path:
        """
        file = None
        if not (p := (self / (name or str())).resolved).is_dir() and not (file := p._is_file()):
            os.system(f'{user.sudo("mkdir", su)} -p -m {mode or 755} {shlex.quote(p.text)}')
        if file:
            raise NotADirectoryError(f'{file=} is file and not dir', f'{(self / (name or str())).resolved}')
        p.chown(group=group, u=u)
        return p

    def open(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None, token=False):
        """
        Open the file pointed by this path and return a file object, as
        the built-in open() function does.
        """
        if token:
            return tokenize.open(self.text) if self.is_file() else None
        return super().open(mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline)

    def path(self, uppermost=True):
        """
        Package path.

        >>> import email.mime.application
        >>> from bapy import Path
        >>> email_path = Path(email.mime.application.__file__)
        >>> email_path.path(uppermost=False)  # doctest: +ELLIPSIS
        Path('.../lib/python.../email/mime')
        >>> email_path.path()  # doctest: +ELLIPSIS
        Path('.../lib/python.../email')
        >>> assert Path('/X/Y/Z/test.py').path(uppermost=False) == Path('/X/Y/Z')
        >>> assert Path('/X/Y/Z/test.py').path() == Path('/X/Y/Z')

        Args:
            uppermost: uppermost package ('__init__.py')

        Returns:
            Package path.
        """
        found = None
        if path := self.find_up(name=INIT_PY, uppermost=uppermost).path:
            found = True
        elif not ((path := self.find_up(PIs.DIR, PSuffix.GIT).path) and (path / 'HEAD').exists()):
            path = self
        parent = path.parent
        parent._rv = found
        return parent

    pwd = property(lambda self: self.cwd().resolved)

    def read(self, encoding=None, errors=None, lnum=False, token=False):
        """Tuple with lnum 1 if lnum"""
        rv = self.read_text(encoding=encoding, errors=errors, token=token)
        if lnum and rv:
            return [rv, 1]
        return rv

    def read_text(self, encoding=None, errors=None, token=False):
        """Open the file in text mode, read it, and close the file."""
        with self.open(encoding=encoding, errors=errors, token=token) as f:
            if token and not f:
                return f
            return f.read()

    def relative(self, p):
        p = Path(p).resolved
        return self.relative_to(p) if self.resolved.is_relative_to(p) else None

    resolved = property(lambda self: self.resolve())

    def rm(self, missing_ok=True):
        """
        Delete a folder/file (even if the folder is not empty)

        Examples:
            >>> with Path.tmp() as tmp:
            ...     name = 'dir'
            ...     p = tmp(name)
            ...     assert p.is_dir()
            ...     p.rm()
            ...     assert not p.is_dir()
            ...     name = 'file'
            ...     p = tmp(name, FILE_DEFAULT)
            ...     assert p.is_file()
            ...     p.rm()
            ...     assert not p.is_file()
            ...     assert Path('/tmp/a/a/a/a')().is_dir()

        Args:
            missing_ok: missing_ok
        """
        if not missing_ok and not self.exists():
            raise
        if self.exists():
            # It exists, so we have to delete it
            if self.is_dir():  # If false, then it is a file because it exists
                shutil.rmtree(self)
            else:
                self.unlink()

    def root(self, uppermost=True):
        """
        Root of Package path:
            -   path.parent if __init__.py or .git found.
            -   path if not found

        >>> import email.mime.application
        >>> from bapy import Path
        >>> email_path = Path(email.mime.application.__file__)
        >>> email_path.root(uppermost=False)  # doctest: +ELLIPSIS
        Path('.../lib/python.../email')
        >>> email_path.root()  # doctest: +ELLIPSIS
        Path('.../lib/python...')
        >>> assert Path('/X/Y/Z/test.py').root(uppermost=False) == Path('/X/Y/Z')
        >>> assert Path('/X/Y/Z/test.py').root() == Path('/X/Y/Z')

        Args:
            uppermost: uppermost package parent ('__init__.py').

        Returns:
            Package Root.
        """
        rv = self.path(uppermost=uppermost)
        return rv.parent if rv._rv else rv

    def rv(self, default=None):
        if N._rv.has(self):
            return self._rv
        return default

    def scan(self, option=POption.FILES, output=POutput.DICT, suffix=PSuffix.NO, level=False, hidden=False):
        """
        Scan Path.

        Args:
            option: what to scan in path.
            output: scan return type.
            suffix: suffix to scan.
            level: scan files two levels from path.
            hidden: include hidden files and dirs.

        Returns:
            Union[Box, dict, list]: list [paths] or dict {name: path}.
        """

        def scan_level():
            b = {}
            for level1 in self.iterdir():
                if not level1.stem.startswith('.') or hidden:
                    if level1.is_file():
                        if option is POption.FILES:
                            b[level1.stem] = level1
                    else:
                        b[level1.stem] = {}
                        for level2 in level1.iterdir():
                            if not level2.stem.startswith('.') or hidden:
                                if level2.is_file():
                                    if option is POption.FILES:
                                        b[level1.stem][level2.stem] = level2
                                else:
                                    b[level1.stem][level2.stem] = {}
                                    for level3 in level2.iterdir():
                                        if not level3.stem.startswith('.') or hidden:
                                            if level3.is_file():
                                                if option is POption.FILES:
                                                    b[level1.stem][level2.stem][level3.stem] = level3
                                            else:
                                                b[level1.stem][level2.stem][level3.stem] = {}
                                                for level4 in level3.iterdir():
                                                    if not level3.stem.startswith('.') or hidden:
                                                        if level4.is_file():
                                                            if option is POption.FILES:
                                                                b[level1.stem][level2.stem][level3.stem][level4.stem] \
                                                                    = level4
                                                if not b[level1.stem][level2.stem][level3.stem]:
                                                    b[level1.stem][level2.stem][level3.stem] = level3
                                    if not b[level1.stem][level2.stem]:
                                        b[level1.stem][level2.stem] = level2
                        if not b[level1.stem]:
                            b[level1.stem] = level1
            return b

        def scan_dir():
            both = {Path(item).stem: Path(item) for item in self.glob(f'*{suffix.dot}')
                    if not item.stem.startswith('.') or hidden}
            if option is POption.BOTH:
                return both
            if option is POption.FILES:
                return {key: value for key, value in both.items() if value.is_file()}
            if option is POption.DIRS:
                return {key: value for key, value in both.items() if value.is_dir()}

        rv = scan_level() if level else scan_dir()
        if output is POutput.LIST:
            return list(rv.values())
        return rv

    @classmethod
    def shelve(cls, path=__file__, pathonly=False, register=True, rm=False):
        """
        Shelve Sync with `atexit.register`.

        Examples:
            >>> import atexit
            >>> ncallbacks = atexit._ncallbacks()
            >>> mdb = Path.shelve(f'doctest/{Path.shelve.__name__}', rm=True)
            >>> file = Path.shelve(f'doctest/{Path.shelve.__name__}', pathonly=True)
            >>> assert locks[file].locked() is True
            >>> assert atexit._ncallbacks() == ncallbacks + 2
            >>> mdb[atexit.__name__] = atexit.__name__
            >>> assert mdb[atexit.__name__] == atexit.__name__
            >>> assert file.exists() is True

        Arguments:
            path: path to be added to for user.shelve
            pathonly: return only path of shelve.
            register: register atexit functions for ctx since they can not be unregistered.
            rm: remove shelve.

        Returns:
            shelve.
        """
        p = cls(path)
        path = (cls(user.shelve) / p.parent.name).mkdir() / f'{p.stem}.dbm'
        if pathonly:
            value = path
        else:
            lock = locks[path]
            while lock.locked():
                time.sleep(1)
            lock.acquire()
            if rm:
                path.rm()
            value = shelve.open(path.text, writeback=True)
            if register:
                atexit.register(value.close)
                atexit.register(lock.release)
        return value

    @classmethod
    @contextlib.contextmanager
    def shelvectx(cls, path=__file__, rm=False):
        """
        Shelve context manager.

        Examples:
            >>> import atexit
            >>> ncallbacks = atexit._ncallbacks()
            >>> f = Path.shelve(f'doctest/{Path.shelvectx.__name__}', pathonly=True)
            >>> assert locks[f].locked() is False
            >>>
            >>> with Path.shelvectx(f'doctest/{Path.shelvectx.__name__}') as d:
            ...     assert locks[f].locked() is True
            ...     assert d.get('atexit') in [None, 'atexit']
            ...     d['a'] = 1
            >>> assert locks[f].locked() is False
            >>>
            >>> with Path.shelvectx(f'doctest/{Path.shelvectx.__name__}') as d:
            ...     assert d['a'] == 1
            >>>
            >>> with Path.shelvectx(f'doctest/{Path.shelvectx.__name__}', rm=True) as d:
            ...     assert d.get('a') is None

        Arguments:
            path: path to be added to for user.shelve
            rm: remove shelve.

        Returns:
            shelve.
        """
        db = cls.shelve(path=path, register=False, rm=rm)
        file = cls.shelve(path=path, pathonly=True)
        try:
            yield db
        finally:
            db.close()
            locks[file].release()

    @property
    def source(self):
        with tokenize.open(self.text) as f:
            return f.read()

    stemfull = property(lambda self: type(self)(self.text.removesuffix(self.suffix)))

    # def _setup(self):
    #     self.init = self.file.initpy.path.resolved
    #     self.path = self.init.parent
    #     self.package = '.'.join(self.file.relative(self.path.parent).stemfull.parts)
    #     self.prefix = f'{self.path.name.upper()}_'
    #     log_dir = self.home(PSuffix.LOG.dot)
    #     self.logconf = ConfLogPath(log_dir, log_dir / f'{PSuffix.LOG.lower}{PSuffix.ENV.dot}',
    #                                log_dir / f'{self.path.name}{PSuffix.LOG.dot}',
    #                                log_dir / f'{self.path.name}{PSuffix.RLOG.dot}')
    #     self.env = Env(prefix=self.prefix, file=self.logconf.env, test=self.path.name is TESTS_DIR)
    #     self.env.call()
    #     self.ic = deepcopy(ic)
    #     self.ic.enabled = self.env.debug.ic
    #     self.icc = deepcopy(icc)
    #     self.icc.enabled = self.env.debug.ic
    #     self.log = Log.get(*[self.package, self.logconf.file, *self.env.log._asdict().values(),
    #                          bool(self.file.installed and self.file.installedbin)])
    #     self.kill = Kill(command=self.path.name, log=self.log)
    #     self.sem = Sem(**self.env.sem | cast(Mapping, dict(log=self.log)))
    #     self.semfull = SemFull(**self.env.semfull | cast(Mapping, dict(log=self.log)))
    #     self.work = self.home(f'.{self.path.name}')
    #
    # # noinspection PyArgumentList
    # @property
    # def _setup_file(self) -> Optional[Path]:
    #     for frame in STACK:
    #         if all([frame.function == N._MODULE, frame.index == 0, 'PyCharm' not in frame.filename,
    #                 type(self)(frame.filename).suffix,
    #                 False if 'setup.py' in frame.filename and setuptools.__name__ in frame.frame.f_globals else True,
    #                 (c[0].startswith(f'from {self.bapy.path.name} import') or
    #                  c[0].startswith(f'import {self.bapy.path.name}'))
    #                 if (c := frame.code_context) else False, not type(self)(frame.filename).installedbin]):
    #             self._frame = frame.frame
    #             return type(self)(frame.filename).resolved
    #
    # # noinspection PyArgumentList
    # @classmethod
    # def setup(cls, file: Union[Path, PathLib, str] = None) -> Path:
    #     b = cls(__file__).resolved
    #
    #     obj = cls().resolved
    #     obj.bapy = cls().resolved
    #     obj.bapy._file = Path(__file__).resolved
    #     obj.bapy._frame = STACK[0]
    #     obj.bapy._setup()
    #
    #     obj._file = Path(file).resolved if file else f if (f := obj._setup_file) else Path(__file__).resolved
    #     if obj.file == obj.bapy.file:
    #         obj._frame = obj.bapy._frame
    #     obj = obj._setup
    #     return obj
    #
    # def setuptools(self) -> dict:
    #     # self.git = Git(fallback=self.path.name, file=self.file, frame=self._frame, module=self.importlib_module)
    #     top = Git.top(self.file)
    #     if top.path:
    #         self.repo = top.name
    #         color = Line.GREEN
    #     elif repo := getvar(REPO_VAR, self._frame, self.importlib_module):
    #         self.repo = repo
    #         color = Line.BYELLOW
    #     else:
    #         self.repo = self.path.name
    #         color = Line.BRED
    #     self.project = top.path if top.path else (self.home / self.repo)
    #     Line.echo(data={'repo': None, self.repo: color, 'path': None, self.project: color})
    #     self.git = None
    #     with suppress(git.NoSuchPathError):
    #         self.git = Git(_name=self.repo, _origin=top.origin, _path=self.project)
    #     self.tests = self.project / TESTS_DIR
    #     if self.git:
    #         (self.project / MANIFEST).write_text('\n'.join([f'include {l}' for l in self.git.ls]))
    #
    #     self.setup_kwargs = dict(
    #         author=user.gecos, author_email=Url.email(), description=self.description,
    #         entry_points=dict(console_scripts=[f'{p} = {p}:{CLI}' for p in self.packages_upload]),
    #         include_package_data=True, install_requires=self.requirements.get('requirements', list()), name=self.repo,
    #         package_data={
    #             self.repo: [f'{p}/{d}/*' for p in self.packages_upload
    #                         for d in (self.project / p).scan(POption.DIRS)
    #                         if d not in self.exclude_dirs + tuple(self.packages + [DOCS])]
    #         },
    #         packages=self.packages_upload, python_requires=f'>={PYTHON_VERSIONS[0]}, <={PYTHON_VERSIONS[1]}',
    #         scripts=self.scripts_relative, setup_requires=self.requirements.get('requirements_setup', list()),
    #         tests_require=self.requirements.get('requirements_test', list()),
    #         url=Url.lumenbiomics(http=True, repo=self.repo).url,
    #         version=__version__, zip_safe=False
    #     )
    #     return self.setup_kwargs

    str = property(lambda self: self.text)

    @classmethod
    def sys(cls): return cls(sys.argv[0]).resolved

    def templates(self, stream=True):
        """
        Iter dir for templates and create dict with name and dump func.

        Examples:
            >>> from bapy import *
            >>>
            >>> with Path.tmp() as tmp:
            ...     p = tmp('templates')
            ...     filename = 'sudoers'
            ...     f = p(f'{filename}{PSuffix.J2()}', FILE_DEFAULT)
            ...     name = User().name
            ...     template = 'Defaults: {{ name }} !logfile, !syslog'
            ...     value = f'Defaults: {name} !logfile, !syslog'
            ...     null_1 = f.write_text(template)
            ...     assert value == p.j2(stream=False)[filename]
            ...     null_2 = p.j2(dest=p)
            ...     assert value == p(filename, FILE_DEFAULT).read_text()
            ...     p(filename, FILE_DEFAULT).read_text()  # doctest: +ELLIPSIS
            'Defaults: ...

        Returns:
            dict
        """
        if self.name != 'templates':
            # noinspection PyMethodFirstArgAssignment
            self /= 'templates'
        if self.is_dir():
            return {i.stem: getattr(jinja2.Template(Path(i).read_text(), autoescape=True),
                                    'stream' if stream else 'render') for i in self.glob(f'*{PSuffix.J2()}')}
        return dict()

    text = property(lambda self: str(self))

    @classmethod
    @contextlib.contextmanager
    def tmp(cls):
        cwd = cls.cwd()
        tmp = tempfile.TemporaryDirectory()
        with tmp as cd:
            try:
                # noinspection PyArgumentList
                yield cls(cd)
            finally:
                cwd.chdir()

    @property
    def to_modname(self):
        if self.exists():
            return inspect.getmodulename(self.text)

    @property
    def to_module(self):
        if self.is_file() and self.text != __file__:
            with contextlib.suppress(ModuleNotFoundError):
                spec = importlib.util.spec_from_file_location(self.name, self.text)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module

    def to_modules(self, suffix=True, uppermost=True):
        """
        Converts relative path to rel or root/path of package (A.B.C)

        >>> import asyncio.events
        >>> assert Path(asyncio.events.__file__).to_modules() == asyncio.events.__name__
        >>> assert Path('/X/Y/Z/test.py').to_modules() == 'test'
        >>> import email.mime.application
        >>> email_path = Path(email.mime.application.__file__)
        >>> email_path.to_modules(uppermost=False)  # doctest: +ELLIPSIS
        'mime.application'
        >>> email_path.to_modules()  # doctest: +ELLIPSIS
        'email.mime.application'
        >>> assert Path('/X/Y/Z/test.py').to_modules(uppermost=False) == 'test'
        >>> assert Path('/X/Y/Z/test.py').to_modules() == 'test'

        Args:
            suffix: remove suffix.
            uppermost: uppermost package parent ('__init__.py').

        Returns:
            String A.B.C
        """
        return tomodules(self.relative_to(self.root(uppermost=uppermost)).parts, suffix=suffix)

    @classmethod
    def to_parent(cls, path=__file__):
        """Return Parent Path if File"""
        path = cls(path)
        return path.parent if path.is_file() and path.exists() else path

    def touch(self, name=None, group=None, mode=644, su=not SUDO_DEFAULT, u=None):
        """
        Add file, touch and return post_init Path.

        Parent paths are created.

        Args:
            name: name
            group: group
            mode: mode
            su: sudo
            u: user

        Returns:
            Path:
        """
        file = None
        if not (p := (self / (name or str())).resolved).is_file() and not p.is_dir() \
                and not (file := p.parent._is_file()):
            if not p.parent:
                p.parent.mkdir(name=name, group=group or user.gname, mode=mode, su=su, u=u or user.name)

            os.system(f'{user.sudo("touch", su)} {shlex.quote(p.text)}')
        if file:
            raise NotADirectoryError(f'{file=} is file and not dir', f'{(self / (name or str())).resolved}')
        p.chmod(mode=mode)
        p.chown(group=group, u=u)
        return p


class PathGit(EnumBase, metaclass=EnumBaseMeta):
    PATH = 'git rev-parse --show-toplevel'
    ORIGIN = 'git config --get remote.origin.url'
    ORGANIZATION = f'git config --get remote.{N.GITHUB_ORGANIZATION}.url'

    def cmd(self, path=None):
        rv = None
        if (path and ((path := Path(path).resolved).exists() or (path := Path.cwd() / path).resolve().exists())) \
                or (path := Path.cwd().resolved):
            with Path(path).cd:
                if path := subprocess.run(shlex.split(
                        self.value), capture_output=True, text=True).stdout.removesuffix(typing.cast(bytes, '\n')):
                    return Path(typing.cast(str, path)) if self is PathGit.PATH else furl.furl(path)
        return rv

    @classmethod
    def top(cls, path=None):
        """
        Get Git Top Path, ORIGIN and name.

        Examples:
            >>> p = Path(__file__).parent.parent
            >>> top = PathGit.top()
            >>> assert top.path == p
            >>> assert top.name == p.name
            >>> assert top.origin is not None
            >>> with Path('/tmp').cd:
            ...     print(PathGit.top())
            GitTop(name=None, origin=None, path=None)

        Args:
            path: path (default: Path.cwd()

        Returns:
            GitTop: Name, Path and Url,
        """
        path = cls.PATH.cmd(path)
        url = cls.ORIGIN.cmd(path)
        return GitTop(str(url.path).rpartition('/')[2].split('.')[0] if url else path.name if path else None, url, path)


class PathInstallScript(setuptools.command.install.install):
    def run(self):
        # does not call install.run() by design
        # noinspection PyUnresolvedReferences
        self.distribution.install_scripts = self.install_scripts

    @classmethod
    def path(cls):
        dist = setuptools.Distribution({'cmdclass': {'install': cls}})
        dist.dry_run = True  # not sure if necessary, but to be safe
        dist.parse_config_files()
        command = dist.get_command_obj('install')
        command.ensure_finalized()
        command.run()
        return dist.install_scripts


class Re(EnumBase, metaclass=EnumBaseMeta):
    """
    >>> import re
    >>> re.search(Re.MODULE_IDENTIFIER(), 'a.b.c')
    <re.Match object; span=(0, 3), match='a.b'>
    >>> re.match(Re.MODULE_IDENTIFIER(), 'a.b.c')
    <re.Match object; span=(0, 3), match='a.b'>
    """
    ASYNCDEF = re.compile(r'^(\s*async\s+def\s)')
    BLOCK = re.compile(r'^(\s*def\s)|(\s*async\s+def\s)|(.*(?<!\w)lambda(:|\s))|^(\s*@)')
    DEF = re.compile(r'^(\s*def\s)')
    DECORATOR = re.compile(r'^(\s*@)')
    ENVVAR = re.compile(r'(\$({\s?)?[a-zA-Z_]\w*(}\s?)?|%\s?[a-zA-Z_]\w*\s?%)')
    HEXSHA_ONLY = re.compile('^[0-9A-Fa-f]{40}$')
    HEXSHA_SHORTENED = re.compile('^[0-9A-Fa-f]{4,40}$')
    LAMBDA = re.compile(r'^(.*(?<!\w)lambda(:|\s))')
    LETTERS = re.compile(r'^[A-Za-z]*$')
    LETTERS_NUMBERS = re.compile(r'^[A-Za-z0-9]*$')  # Letters and numbers
    MODULE_IDENTIFIER = re.compile(r'^(?:\s*(\w+)\s*\.)?\s*(\w+)')
    NUMBERS = re.compile(r'^[0-9]*$')
    TAB_FULL_LINE = re.compile(r'^\t(.*)$')
    UNDERSCORES_PREFIX = re.compile(r'^_*')  # re.search( , ___prefix_suffix__) -> ___
    UNDERSCORES_SUFFIX = re.compile(r'(^!_)*_*$')  # re.search( , ___prefix_suffix__) -> __
    VAR = re.compile(r'^[A-Za-z0-9_]*$')  # Letters, numbers and _
    VAR_DASH = re.compile(r'^[A-Za-z0-9_-]*$')  # Letters, numbers, _ and -
    WHITESPACE = re.compile(r'\s+')
    ALL = Access.ALL()
    PRIVATE = Access.PRIVATE()
    PROTECTED = Access.PROTECTED()
    PUBLIC = Access.PUBLIC()


Real = collections.namedtuple('Var', 'caller real')


class ReposNamesBase:
    """Repo Base Class."""
    __slots__ = ('name', 'script',)

    def __init__(self, name=None, script=None):
        self.name = name if name else varname()
        self.script = script if script else self.name

    def __hash__(self): return hash((self.name, self.script,))

    def __reduce__(self): return self.__class__, (self.name, self.script,)

    def __repr__(self): return reprcls(data=self, attrs=self.__slots__)


class ReposNames(dictsort):
    """
    Repos Class

    >>> r = ReposNames()
    >>> r.rcdev.name
    'rcdev'
    >>> from pickle import dumps, loads
    >>> from copy import deepcopy
    >>>
    >>> encode = dumps(r)
    >>> assert id(r) != id(loads(encode))
    >>> assert id(r) != id(deepcopy(r))
    >>> assert hash(r)
    >>>
    >>> encode = dumps(r.rcdev)
    >>> assert id(r.rcdev) != id(loads(encode))
    >>> assert id(r.rcdev) != id(deepcopy(r.rcdev))
    >>> assert hash(r.rcdev)
    """
    __slots__ = ('rcdev', 'rclib',)

    def __init__(self):
        super().__init__({k: v for k, v in self.__class__.__dict__.items() if not k.startswith('_')})
        effect(lambda x: setattr(self, x, ReposNamesBase(x)), self.__slots__)

    def __hash__(self): return hash(tuple(self.values()))

    def __repr__(self): return reprcls(data=self, line=True, **self)

    __class_getitem__ = classmethod(types.GenericAlias)


class SlotsType(metaclass=abc.ABCMeta):
    """
    Slots Type.

    >>> import bapy.data.cls
    >>> class D: a = 1
    >>> class Slots: a = 1; __slots__ = tuple()
    >>>
    >>> d = D()
    >>> s = Slots()
    >>>
    >>> assert Is(Dict).slotstype is False and not issubclass(Dict, SlotsType)
    >>> assert Is(d).slotstype is False and not isinstance(d, SlotsType)
    >>>
    >>> assert Is(Slots).slotstype and issubclass(Slots, SlotsType)
    >>> assert Is(s).slotstype and isinstance(s, SlotsType)
    >>>
    >>> assert issubclass(bapy.data.cls.MroDataDictSlotMix, SlotsType) and \
        isinstance(bapy.data.cls.MroDataDictSlotMix(), SlotsType)
    >>> assert Is(bapy.data.cls.MroDataDictSlotMix).slotstype and \
        Is(bapy.data.cls.MroDataDictSlotMix()).slotstype
    >>> assert issubclass(bapy.data.cls.MroDataDictMix, SlotsType) is False and \
        isinstance(bapy.data.cls.MroDataDictMix(), SlotsType) is False
    >>> assert Is(bapy.data.cls.MroDataDictMix).slotstype is False and \
        Is(bapy.data.cls.MroDataDictMix()).slotstype is False
    """
    __slots__ = ()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is SlotsType:
            return N.SLOTS.has(C)
        return NotImplemented


class SourceVars:
    """
    Frame Source Vars

    Examples:
        >>> from copy import deepcopy
        >>> s = SourceVars(getframe(0))
        >>> s # doctest: +ELLIPSIS
        SourceVars(file='....py', name='...', package='', pypi=None, repo=None, source=None, spec=ModuleSpec(name=...
        >>> s['sys']
        <module 'sys' (built-in)>
        >>> s = SourceVars()
        >>> s
        SourceVars(file=None, name=None, package=None, pypi=None, repo=None, source=None, spec=None)
        >>> s.globs, s.locs, s.vars
        ({}, {}, {})
    """
    __sourcevars__ = sourcevars()
    __slots__ = tuple(__sourcevars__) + ('globs', 'locs', 'vars',)

    def __init__(self, frame=None):
        if frame:
            self.globs = dd(frame.f_globals.copy())
            self.locs = dd(frame.f_locals.copy())
            self.vars = self.globs | self.locs
            effect(lambda x: self.__setattr__(x[0], self.get(x[1])), self.__sourcevars__.items())
        else:
            effect(lambda x: self.__setattr__(x, None), self.__sourcevars__)
            effect(lambda x: self.__setattr__(x, {}), ('globs', 'locs', 'vars',))

    def __eq__(self, other): return self.vars == self.vars if isinstance(other, type(self)) else NotImplemented

    def __getitem__(self, item): return self.vars.get(item)

    def __repr__(self): return reprcls(self, self.__sourcevars__)

    def get(self, item, default=None): return self.vars.get(item, default)


SourceBase = collections.namedtuple('SourceBase', 'code data exists file function include internal lineno '
                                                  'module node source vars',
                                    defaults=(None, None, False, None, str(), False, False, int(), False, ast.AST(),
                                              str(), SourceVars()))


class Source(SourceBase):
    """Source Class."""
    EXCLUDE_DIRS = (IMPORTLIB_PYCACHE, N.backup, N.venv, importlib.machinery.BYTECODE_SUFFIXES, '.pyo')
    __slots__ = ()

    def __new__(cls, data, full=False, lnum=False, **kwargs):
        """
        :class:`rc.Source`.

        Args:
            data: Object.
            full: Complete source/node for file (always for module and frame corresponding to module)
                or object node (default=False).
            lnum: Line of source with source.

        Returns:
            :class:`rc.Source`.

        Examples:
            >>> from inspect import FrameInfo
            >>> frameinfo = inspect.stack()[0]
            >>> ftype = Source(frameinfo.frame)
            >>>
            >>> finfo = Source(frameinfo, full=True)
            >>> finfo.source
            'frameinfo = inspect.stack()[0]\\n'
            >>>
            >>> # finfo = Source(frameinfo, lnum=True)
            >>> # assert finfo.source == ('frameinfo = inspect.stack()[0]\\n', 0)
            >>>
            >>> # finfo = Source(frameinfo, full=True, lnum=True)
            >>> # assert finfo.source == ('frameinfo = inspect.stack()[0]\\n', 0)
            >>>
            >>> finfo = Source(frameinfo)
            >>> assert finfo.source == 'frameinfo = inspect.stack()[0]\\n'

            >>> assert finfo.source == ftype.source
        """

        def setitem(frame, lineno):
            kwargs['code'], file, function = frame.f_code, Path(frame.f_code.co_filename), frame.f_code.co_name
            kwargs['file'], kwargs['function'], kwargs['lineno'] = file, function, lineno
            kwargs['exists'], kwargs['module'] = file.resolved.exists, function == FUNCTION_MODULE
            kwargs['include'] = not (any(map(file.is_relative_to, PATHS_EXCL)) or not file.suffix)
            kwargs['internal'] = file.parent == file.parent and file.is_relative_to(
                path_internal.file.parent)
            kwargs['data'], kwargs['vars'] = frame, SourceVars(frame)

        kwargs = SourceBase._field_defaults
        i = Is(data)

        if i.frametype:
            setitem(data, data.f_lineno)
        elif i.frameinfo:
            setitem(data.frame, data.lineno)
        elif i.tracebacktype:
            setitem(data.tb_frame, data.tb_lineno)
        else:
            kwargs['data'] = data
            kwargs['file'] = data.__file__ if i.moduletype else noexc(Path, data)
            kwargs['module'] = i.moduletype

        if (kwargs['module'] or full) and kwargs['file'] and kwargs['file'].is_file():
            kwargs['source'] = kwargs['file'].read(lnum=lnum, token=True)
        if not kwargs['source']:
            try:
                kwargs['source'] = inspect.getsourcelines(kwargs['data']) if lnum else inspect.getsource(kwargs['data'])
                if lnum:
                    kwargs['source'] = ''.join(kwargs['source'][0]), kwargs['source'][1]
            except (OSError, TypeError):
                kwargs['source'] = [str(data), 1] if lnum else str(data)
        kwargs['node'] = ast.parse(kwargs['source'][0]
                                   if isinstance(kwargs['source'], tuple) or lnum else kwargs['source'])

        return super().__new__(cls, **kwargs)

    @property
    def args(self):
        locs = self.vars.locs
        if locs:
            arg, varargs, keywords = inspect.getargs(self.code)
            return delete({name: locs[name] for name in arg} | ({varargs: val} if (
                val := locs.get(varargs)) else dict()) | (kw if (kw := locs.get(keywords)) else dict()))
        return {}

    __class_getitem__ = classmethod(types.GenericAlias)


class Stack(tuple[Frame]):
    real = None

    def __new__(cls, init=False):
        fs = list()
        frame = FRAME if init else getframe(FRAME_INDEX)
        while frame:
            fs.append(Frame(frame))
            frame = frame.f_back
        return tuple.__new__(Stack, fs)

    def __call__(self, index=FRAME_INDEX, real=False):
        caller = self[index]
        rv = None
        if real:
            with contextlib.suppress(IndexError):
                rv = self[index + (caller.real or bool(None))]
        return Real(caller=caller, real=rv) if real else caller

    def __repr__(self):
        msg = f',{NEWLINE}'.join([f'[{self.index(item)}]: {self[self.index(item)]}' for item in self])
        return f'{self.__class__.__name__}({NEWLINE}{msg}{NEWLINE})'

    @classmethod
    def init(cls):
        return cls(init=True)

    @classmethod
    def main(cls):
        return cls.init()[0]

    @classmethod
    def package(cls):
        for item in cls.init():
            if item.external:
                return item


class StateEnv(environs.Env, BaseState):
    """
    Env Class with Deepcopy and Pickle.

    Examples:
        >>> from copy import deepcopy
        >>> from bapy import StateEnv
        >>> import environs
        >>>
        >>> env = StateEnv()
        >>> term = env('TERM')
        >>> env
        <StateEnv {'TERM': 'xterm-256color'}>
        >>> state = env.__getstate__()
        >>> env_deepcopy = deepcopy(env)
        >>> env_deepcopy
        <StateEnv {'TERM': 'xterm-256color'}>
        >>> assert id(env_deepcopy) != id(env)
        >>> assert id(env_deepcopy._values) != id(env._values)
    """

    def __init__(self, *, eager=True, expand_vars=False):
        super().__init__(eager=eager, expand_vars=expand_vars)


class UserActual:
    """User Actual Class."""
    ROOT = None
    SUDO = None
    SUDO_USER = None

    def __init__(self):
        try:
            self.name = pathlib.Path('/dev/console').owner() if MACOS else os.getlogin()
        except OSError:
            self.name = pathlib.Path('/proc/self/loginuid').owner()
        try:
            self.passwd = pwd.getpwnam(self.name)
        except KeyError:
            raise KeyError(f'Invalid user: {self.name=}')
        else:
            self.gecos = self.passwd.pw_gecos
            self.gid = self.passwd.pw_gid
            self.gname = grp.getgrgid(self.gid).gr_name
            self.home = pathlib.Path(self.passwd.pw_dir).resolve()
            self.id = self.passwd.pw_uid
            self.shell = pathlib.Path(self.passwd.pw_shell).resolve()
            self.ssh = self.home / PSuffix.SSH()
            self.auth_keys = self.ssh / N.authorized_keys
            self.id_rsa = self.ssh / N.id_rsa
            self.id_rsa_pub = self.ssh / ID_RSA_PUB
            self.git_config_path = self.home / PSuffix.GITCONFIG()


class UserProcess:
    """User Process Class."""
    id = os.getuid()
    gecos = pwd.getpwuid(id).pw_gecos
    gid = os.getgid()
    gname = grp.getgrgid(gid).gr_name
    home = pathlib.Path(pwd.getpwuid(id).pw_dir).resolve()
    name = pwd.getpwuid(id).pw_name
    passwd: pwd.struct_passwd = pwd.getpwuid(id)
    ROOT = not id
    shell = pathlib.Path(pwd.getpwuid(id).pw_shell).resolve()
    ssh = home / PSuffix.SSH()
    SUDO = SUDO
    SUDO_USER = SUDO_USER
    auth_keys = ssh / N.authorized_keys
    id_rsa = ssh / N.id_rsa
    id_rsa_pub = ssh / ID_RSA_PUB
    git_config_path = home / PSuffix.GITCONFIG()
    git_config = git.GitConfigParser(str(git_config_path))
    github_username = git_config.get_value(section='user', option='username', default=str())


class User:
    """User Class."""
    actual: UserActual = UserActual()
    process: UserProcess = UserProcess()
    SUDO = UserProcess.SUDO
    SUDO_USER = UserProcess.SUDO_USER
    gecos = process.gecos if SUDO else actual.gecos
    gid = process.gid if SUDO else actual.gid
    gname = process.gname if SUDO else actual.gname
    home = process.home if SUDO else actual.home
    id = process.id if SUDO else actual.id
    name = process.name if SUDO else actual.name
    passwd: pwd.struct_passwd = process.passwd if SUDO else actual.passwd
    ROOT = UserProcess.ROOT
    shell = process.shell if SUDO else actual.shell
    ssh = process.ssh if SUDO else actual.ssh
    auth_keys = process.auth_keys if SUDO else actual.auth_keys
    id_rsa = process.id_rsa if SUDO else actual.id_rsa
    id_rsa_pub = process.id_rsa_pub if SUDO else actual.id_rsa_pub
    git_config_path = process.git_config_path if SUDO else actual.git_config_path
    git_config = git.GitConfigParser(str(git_config_path))
    github_username = git_config.get_value(section='user', option='username', default=str())
    shelve = home / PSuffix.SHELVE()
    shelve.mkdir(parents=True, exist_ok=True)
    GIT_SSH_COMMAND = f'ssh -i {str(id_rsa)} {SSH_CONFIG_TEXT}'
    os.environ['GIT_SSH_COMMAND'] = GIT_SSH_COMMAND
    __contains__ = lambda self, item: item in self.name
    __eq__ = lambda self, other: self.name == other.name
    __hash__ = lambda self: hash(self.name)
    sudo = staticmethod(lambda command, su=False: command if UserProcess.SUDO or not su else f'sudo {command}')


class VarsType(metaclass=abc.ABCMeta):
    """
    Vars (__dict__) Type.

    >>> import bapy.data.cls
    >>> class D: a = 1
    >>> class Slots: a = 1; __slots__ = tuple()
    >>>
    >>> d = D()
    >>> s = Slots()
    >>>
    >>> assert Is(Slots).varstype is False and not issubclass(Slots, VarsType)
    >>> assert Is(s).varstype is False and not isinstance(s, VarsType)
    >>>
    >>> assert Is(D).varstype and issubclass(D, VarsType)
    >>> assert Is(d).varstype and isinstance(d, VarsType)
    >>>
    >>> assert issubclass(bapy.data.cls.MroDataDictSlotMix, VarsType) and \
        isinstance(bapy.data.cls.MroDataDictSlotMix(), VarsType)
    >>> assert Is(bapy.data.cls.MroDataDictSlotMix).varstype and Is(bapy.data.cls.MroDataDictSlotMix()).varstype
    >>> assert issubclass(bapy.data.cls.MroDataDictMix, VarsType) and \
        isinstance(bapy.data.cls.MroDataDictMix(), VarsType)
    >>> assert Is(bapy.data.cls.MroDataDictMix).varstype and Is(bapy.data.cls.MroDataDictMix()).varstype
    """
    __dict__ = {}

    @classmethod
    def __subclasshook__(cls, C):
        if cls is VarsType:
            return Is(C).varstype
        return NotImplemented


# Dependant
PathLikeStr = typing.Union[pathlib.Path, Path, str]
PathInternal = collections.namedtuple('PathInternal', 'file path package')
path_internal = Path.internal()
SYSCONFIG_PATHS_EXCLUDE = tuple(SYSCONFIG_PATHS[_i] for _i in
                                ['stdlib', 'purelib', 'include', 'platinclude', 'scripts'])
PATHS_EXCL = SYSCONFIG_PATHS_EXCLUDE + ((_i,) if
                                        (_i := Path(os.getenv('PYCHARM_PLUGINS', '<None>'))).resolved.exists() else (

)) \
             + ('/Applications/PyCharm.app',)

Types = typing.Union[AllAttr, AnnotationsAttr, AsDictMethod, AsDictProperty, DataClass,
                     GetItem, GetMethod,
                     NameAttr, Namedtuple, NamedTupleTyping, VarsType, SlotsType]
TypesType = typing.Union[typing.Type[typing.Any], typing.Type[AllAttr], typing.Type[AnnotationsAttr],
                         typing.Type[AsDictMethod], typing.Type[AsDictProperty],
                         typing.Type[DataClass],
                         typing.Type[GetItem], typing.Type[GetMethod],
                         typing.Type[NameAttr], typing.Type[Namedtuple], typing.Type[NamedTupleTyping],
                         typing.Type[VarsType], typing.Type[SlotsType]]


# Echo
def black(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Black.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='black',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


def blue(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Blue.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(
        f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True,
        fg='blue', err=err, reset=reset,
    )
    if rc is not None:
        typer.Exit(rc)


def cyan(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Cyan.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='cyan',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


def green(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Green.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='green', err=err,
                reset=reset)
    if rc is not None:
        typer.Exit(rc)


def magenta(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Magenta.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='magenta', err=err,
                reset=reset)
    if rc is not None:
        typer.Exit(rc)


def red(msg, bold=False, nl=True, underline=False, blink=False, err=True, reset=True, rc=None) -> None:
    """
    Red.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='red', err=err,
                reset=reset)
    if rc is not None:
        typer.Exit(rc)


def white(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    White.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='white', err=err,
                reset=reset)
    if rc is not None:
        typer.Exit(rc)


def yellow(msg, bold=False, nl=True, underline=False, blink=False, err=True, reset=True, rc=None) -> None:
    """
    Yellow.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='yellow',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


def bblack(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Black.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_black',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


def bblue(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bblue.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_blue',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


def bcyan(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bcyan.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_cyan',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


def bgreen(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bgreen.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_green',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


def bmagenta(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bmagenta.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_magenta',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


def bred(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bred.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_red',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


def bwhite(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Bwhite.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_white',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


def byellow(msg, bold=False, nl=True, underline=False, blink=False, err=False, reset=True, rc=None) -> None:
    """
    Byellow.

    Args:
        msg: msg
        bold: bold
        nl: nl
        underline: underline
        blink: blink
        err: err
        reset: reset
        rc: rc
    """
    click.secho(f'{msg}', bold=bold, nl=nl, underline=underline, blink=blink, color=True, fg='bright_yellow',
                err=err, reset=reset)
    if rc is not None:
        typer.Exit(rc)


# Instances
alocks = dd(asyncio.Lock, {})
locks = dd(threading.Lock, {})
reposnames = ReposNames()
shelves = {}
user = User()

# Init
colorama.init()
init_stack = inspect.stack()
logging.getLogger(paramiko.__name__).setLevel(logging.NOTSET)
pretty_install()
os.environ['PYTHONWARNINGS'] = N.ignore
structlog.configure(logger_factory=structlog.stdlib.LoggerFactory())
urllib3.disable_warnings()


if __name__ == '__main__':
    try:
        typer.Exit(app())
    except KeyError:
        pass
