"""
Implements the Web Service Transition Language (WeSTL), which is specified at https://github.com/RWCBook/wstl-spec.
This module provides functions for managing state transitions specified in WeSTL. HEA follows the WeSTL spec with the
following exceptions:
* Data objects: data objects may contain one level of nested objects, and property names may not contain periods.
"""

import copy
import functools
import logging
import pkgutil
import json
import jsonmerge  # type: ignore
from collections import abc
from aiohttp.web import Request, Response
from typing import Optional, Callable, Dict, Any, Coroutine, List, Union
from . import appproperty, requestproperty, jsonschemavalidator
from yarl import URL

DEFAULT_DESIGN_TIME_WSTL = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'wstl': {
        "actions": []
    }
}

ACTION_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'description': {'type': 'string'},
        'type': {
            'type': 'string',
            'enum': ['safe', 'unsafe']
        },
        'action': {
            'type': 'string',
            'enum': ['read', 'append', 'update', 'remove', 'diff']
        },
        'target': {'type': 'string'},
        'prompt': {'type': 'string'},
        'href': {'type': 'string'},
        'rel': {
            'type': 'array',
            'items': {'type': 'string'}
        },
        'inputs': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'prompt': {'type': 'string'},
                    'value': {'type': 'string'},
                    'readOnly': {
                        'type': 'boolean',
                        'enum': [True, False]
                    },
                    'required': {
                        'type': 'boolean',
                        'enum': [True, False]
                    },
                    'pattern': {'type': 'string'},
                    'type': {
                        'type': 'string',
                        'enum': ['textarea', 'select']
                    },
                    'suggest': {
                        'anyOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'related': {'type': 'string'},
                                    'value': {'type': 'string'},
                                    'text': {'type': 'string'}
                                },
                                'required': ['related', 'value', 'text']
                            },
                            {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'value': {'type': 'string'},
                                        'text': {'type': 'string'}
                                    },
                                    'required': ['value']
                                },
                                'minItems': 1
                            },
                            {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'value': {'type': 'string'},
                                        'text': {'type': 'string'}
                                    },
                                    'required': ['text']
                                }
                            }
                        ]
                    }
                },
                'required': ['name']
            }
        }
    },
    'required': ['name']
}

_ACTION_SCHEMA_VALIDATOR = jsonschemavalidator.compile(ACTION_SCHEMA)

WSTL_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'wstl': {
            'type': 'object',
            'properties': {
                'title': {'type': 'string'},
                'hci': {
                    'type': 'object',
                    'properties': {
                        'href': {'type': 'string'}
                    }
                },
                'actions': {
                    'type': 'array',
                    'items': ACTION_SCHEMA,
                    'mergeStrategy': 'append'
                },
                'content': {
                    'type': 'object',
                    'properties': {
                        'type': {
                            'type': 'string',
                            'enum': ['html', 'markdown', 'text']
                        },
                        'text': {'type': 'string'}
                    }
                },
                'data': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'patternProperties': {
                            '.*': {'not': {'type': 'object'}},
                        },
                        'additionalProperties': False
                    },
                    'mergeStrategy': 'append'
                },
                'related': {
                    'type': 'object',
                    'additionalProperties': {'type': 'array'},
                    'minProperties': 1
                }
            }
        }
    },
    'required': ['wstl']
}

_WSTL_SCHEMA_VALIDATOR = jsonschemavalidator.compile(WSTL_SCHEMA)


class RuntimeWeSTLDocumentBuilder:
    """
    A run-time WeSTL document builder. Call instance of this class to produce a run-time WeSTL document.
    """

    def __init__(self, design_time_wstl: Optional[Dict[str, Any]] = None, href: Optional[Union[str, URL]]=None) -> None:
        """
        Constructs a run-time WeSTL document with a design-time WeSTL document.

        :param design_time_wstl: a dict representing a design-time WeSTL document. If omitted, the
        DEFAULT_DESIGN_TIME_WSTL design-time WeSTL document will be used. Assumes that the design-time WeSTL document
        is valid.
        :param href: The URL associated with the resource (optional).
        """
        _logger = logging.getLogger(__name__)
        self.__orig_design_time_wstl = copy.deepcopy(design_time_wstl if design_time_wstl else DEFAULT_DESIGN_TIME_WSTL)
        self.__design_time_wstl = copy.deepcopy(self.__orig_design_time_wstl)
        _logger.debug('Design-time WeSTL document is %s', self.__design_time_wstl)
        self.__run_time_wstl = copy.deepcopy(self.__design_time_wstl)
        self.__run_time_wstl['wstl']['actions'] = []
        self.__actions = {action_['name']: action_ for action_ in self.__design_time_wstl['wstl'].get('actions', [])}
        self.__run_time_actions: Dict[str, Any] = {}
        if href is not None:
            self.__run_time_wstl['wstl'].setdefault('hci', {})['href'] = str(href)

    def clear(self):
        _logger = logging.getLogger(__name__)
        self.__design_time_wstl = copy.deepcopy(self.__orig_design_time_wstl)
        self.__run_time_wstl = copy.deepcopy(self.__design_time_wstl)
        self.__run_time_wstl['wstl']['actions'] = []
        self.__actions = {action_['name']: action_ for action_ in self.__design_time_wstl['wstl'].get('actions', [])}
        self.__run_time_actions: Dict[str, Any] = {}
        _logger.debug('Cleared run-time WeSTL document builder')

    def find_action(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Low level finder of actions in the design-time WeSTL document.

        :param name: the name of the action of interest.
        :return: The first action found with the given name, or None if not found.
        """
        a = self.__actions.get(name)
        if a:
            return copy.deepcopy(a)
        else:
            return None

    def has_run_time_action(self, name: str):
        return name in self.__run_time_actions

    def add_run_time_action(self, name: str,
                            path: Optional[str] = None,
                            rel: Optional[Union[str, List[str]]] = None,
                            root: Optional[str] = None) -> None:
        """
        Append an action from the design-time WeSTL document to the run-time WeSTL document.

        :param name: the action's name. Required.
        :param path: the path of the action, plus any fragment and query string.
        :param rel: a list of HTML rel attribute values, or the list as a space-delimited string.
        :param root: the root of the action URL (everything except the path above).
        """
        _logger = logging.getLogger(__name__)
        if rel is not None and not isinstance(rel, list):
            rel_ = [rel]
        else:
            rel_ = rel
        if name in self.__run_time_actions:
            raise ValueError(f'Duplicate run-time action {name}')
        tran = self.__make(name, path=path, rel=rel_, root=root)
        _logger.debug('Adding base action %s', tran)
        self.__run_time_wstl['wstl']['actions'].append(tran)
        self.__run_time_actions[name] = tran

    def has_design_time_action(self, name: str):
        return name in self.__actions

    def add_design_time_action(self, action_: Dict[str, Any]) -> None:
        """
        Append an action to the design-time WeSTL document.

        :param action_: a WeSTL action object dict. Required.
        """
        if not action_:
            raise ValueError('action_ cannot be None')
        try:
            _ACTION_SCHEMA_VALIDATOR.validate(action_)
            actions = self.__design_time_wstl['wstl']['actions']
            if action_['name'] not in self.__actions:
                action__ = copy.deepcopy(action_)
                actions.append(action__)
                self.__actions[action_['name']] = action__
            else:
                raise ValueError(f'Existing action with name {action_["name"]} found in the design-time document')
        except jsonschemavalidator.ValidationError as e:
            raise ValueError from e

    @property
    def href(self) -> Optional[str]:
        wstl = self.__run_time_wstl['wstl']
        return wstl['hci'].get('href') if 'hci' in wstl else None

    @href.setter
    def href(self, href: Optional[str]) -> None:
        """
        The href of the data in the run-time WeSTL document.
        """
        self.__run_time_wstl['wstl'].setdefault('hci', {})['href'] = str(href)

    @href.deleter
    def href(self) -> None:
        wstl = self.__run_time_wstl['wstl']
        if 'hci' in wstl:
            wstl['hci'].pop('href', None)

    @property
    def data(self) -> list:
        return self.__run_time_wstl['wstl'].get('data', None)

    @data.setter
    def data(self, data) -> None:
        """
        The data object of the run-time WeSTL document.
        """
        if isinstance(data, abc.Mapping):
            self.__run_time_wstl['wstl']['data'] = [data]
        elif not all(isinstance(elt, abc.Mapping) for elt in data):
            raise TypeError(f'List data must be a list of dicts but instead was {data}')
        elif data:
            self.__run_time_wstl['wstl']['data'] = data
        else:
            self.__run_time_wstl['wstl'].pop('data', None)

    @data.deleter
    def data(self) -> None:
        self.__run_time_wstl['wstl'].pop('data', None)

    def find_by_target(self, val: str):
        return [tran for tran in self.__run_time_wstl['wstl']['actions'] if 'target' in tran and val in tran['target']]

    @property
    def design_time_document(self) -> Dict[str, Any]:
        """
        Returns a copy of the design-time WeSTL document.

        :return: a dict representing the design-time WeSTL document.
        """
        return copy.deepcopy(self.__design_time_wstl)

    def __call__(self) -> Dict[str, Any]:
        """
        Returns a copy of the run-time WeSTL document.

        :return: a dict representing the run-time WeSTL document.
        """
        return copy.deepcopy(self.__run_time_wstl)

    def __make(self, name: str, path: Optional[str]=None, rel: Optional[List[str]] = None, root: Optional[str] = None) -> Dict[str, Any]:
        """
        Make a base transition.

        :param name: the transition's name. Required.
        :param path: the path and fragment parts of the action URL.
        :param rel: a list of strings.
        :param root: the root of the action URL (everything except the path above).
        :return: the created base transition, or None if the passed in dict does not have a name key.
        """
        if not name:
            raise ValueError('name cannot be None')
        else:
            root_ = '' if root is None else root
            path_ = '' if path is None else path
            rel_ = rel if rel is not None else []
            tran = self.find_action(name)
            if tran is not None:
                rtn = tran
                rtn['href'] = root_ + path_
                rtn['rel'] = rel_
            else:
                raise ValueError(f'No action with name {name}')
        return rtn


def action(name: str,
           path='#',
           rel: Optional[Union[str, List[str]]] = None,
           include_root=False) -> Callable[[Callable[[Request], Coroutine[Any, Any, Response]]],
                                           Callable[[Request], Coroutine[Any, Any, Response]]]:
    """
    Decorator factory for appending a WeSTL action to a run-time WeSTL document in a HTTP request.

    :param name: the action's name. Required.
    :param path: the action's path. Required. The path may contain variables in curly braces that will be substituted
    in the runtime WeSTL document by corresponding data values. Nested JSON objects may be referred to using a period
    syntax like in object-oriented programming.
    :param rel: a list of HTML rel attribute values, or the list as a space-delimited string.
    :param include_root: whether to include the root of the service's URL in the action href. False by default. Should
    always be False except in services that are accessible publicly.
    :return: the decorated callable.
    """

    def wrap(f: Callable[[Request], Coroutine[Any, Any, Response]]) -> Callable[
        [Request], Coroutine[Any, Any, Response]]:
        @functools.wraps(f)
        def wrapped_f(request: Request) -> Coroutine[Any, Any, Response]:
            wstl_ = request[requestproperty.HEA_WSTL_BUILDER]
            wstl_.add_run_time_action(name, path=path, rel=rel,
                                      root=(request.app[appproperty.HEA_COMPONENT] if include_root else None))
            return f(request)

        return wrapped_f

    return wrap


def builder_factory(package: Optional[str] = None, resource='wstl/all.json', href: Optional[Union[str, URL]]=None, loads=json.loads) -> Callable[
    [], RuntimeWeSTLDocumentBuilder]:
    """
    Returns a zero-argument callable that will load a design-time WeSTL document and get a RuntimeWeSTLDocumentBuilder
    instance. It caches the design-time WeSTL document.

    :param package: the name of the package that the provided resource is in, in standard module format (foo.bar).
    Must be an absolute package name. If resource is set to None, then this argument will be ignored and may be omitted.
    :param resource: a relative path to a design-time WeSTL document. Expects / as the path separator. The parent
    directory (..) is not allowed, nor is a rooted name (starting with /). The default value is 'wstl/all.json'. If
    set to None, the DEFAULT_DESIGN_TIME_WSTL design-time WeSTL document will be used.
    :param href: The URL associated with the resource
    :param loads: any callable that accepts str and returns dict with parsed JSON (json.loads() by default).
    :return: a zero-argument callable for creating a WSTLDocument object. The same document instance will be
    returned every time.
    :raises FileNotFoundException: no such resource exists.
    :raises ValueError: if a non-existent package is specified, or the provided package name does not support the
    get_data API.
    """

    if resource:
        if package is None:
            raise ValueError('package cannot be None when a resource is given')
        data_ = pkgutil.get_data(package, resource)
        if not data_:
            raise ValueError('No package named ' + package +
                             ', or the package uses a loader that does not support get_data')
        data = loads(data_)
        _validate(data)
    else:
        data = DEFAULT_DESIGN_TIME_WSTL

    def builder_factory_() -> RuntimeWeSTLDocumentBuilder:
        """
        Reads a JSON document in design-time Web Service Transition Language (WeSTL) format from a file within a package.
        The specification of the WeSTL format is available from https://rwcbook.github.io/wstl-spec/.

        :return: a RuntimeWeSTLDocumentBuilder instance for creating a run-time WeSTL document.
        """
        return RuntimeWeSTLDocumentBuilder(data, href)

    return builder_factory_


def builder(package: str, resource='wstl/all.json', href: Optional[Union[str, URL]]=None, loads=json.loads) -> RuntimeWeSTLDocumentBuilder:
    """
    Returns a RuntimeWeSTLDocumentBuilder instance.

    :param package: the name of a package, in standard module format (foo.bar).
    :param resource: a relative path to a design-time WeSTL ocument. Expects / as the path separator. The parent
    directory (..) is not allowed, nor is a rooted name (starting with /). The default value is 'wstl/all.json'. If
    set to None, the DEFAULT_DESIGN_TIME_WSTL design-time WeSTL document will be used.
    :param href: the URL associated with the resource.
    :param loads: any callable that accepts str and returns dict with parsed JSON (json.loads() by default).
    :return: a zero-argument callable for creating a WSTLDocument object. The same document instance will be
    returned every time.
    :raises FileNotFoundException: no such resource exists.
    :raises ValueError: if a non-existent package is specified, or the provided package name does not support the
    get_data API.
    """
    return builder_factory(package, resource=resource, href=href, loads=loads)()


_merger = jsonmerge.Merger(WSTL_SCHEMA)


def merge(base: Dict[str, Any], head: Dict[str, Any]):
    return _merger.merge(base, head)


def _check_duplicates(itr):
    s = set()
    for item in itr:
        if item in s:
            return True
        else:
            s.add(item)
    return False


def _validate(wstl_doc):
    try:
        _WSTL_SCHEMA_VALIDATOR.validate(wstl_doc)
    except jsonschemavalidator.ValidationError as e:
        raise ValueError from e
    if _check_duplicates(obj['name'] for obj in wstl_doc['wstl'].get('actions', [])):
        raise ValueError('Invalid WeSTL document')
