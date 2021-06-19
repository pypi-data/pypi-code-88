from __future__ import annotations

from collections.abc import Sequence
from functools import cache, partial, reduce
from itertools import groupby
from operator import add, attrgetter
from re import Pattern, compile
from typing import (  # noqa: N817
    ClassVar,
    Iterable,
    Literal,
    NamedTuple,
    NoReturn,
    Optional,
    Union as U,
)

from attr import asdict, field
from multidict import CIMultiDict

from .attr_cls import Attr, define
from .convert_json import convert

handlers = Literal[
    'acme_server',
    'authentication',
    'encode',
    'error',
    'file_server',
    'headers',
    'map',
    'metrics',
    'push',
    'request_body',
    'reverse_proxy',
    'rewrite',
    'subroute',
    'templates',
    'vars',
]


def convert_serializer(obj, attribute, value):
    return convert(value)


@convert.register
def convert_attr(obj: Attr):
    return asdict(obj, recurse=False, value_serializer=convert_serializer)


upper_pattern = compile('([A-Z])')


@define
class Handler:
    name: ClassVar[handlers]

    def __init_subclass__(cls, **kwargs):
        name = cls.__name__.removesuffix('Handler').lower()
        snake_case = upper_pattern.sub(r'_\1', name).lower()
        cls.name = snake_case


@convert.register
def convert_handler(obj: Handler):
    json = convert_attr(obj)
    cls = obj.__class__
    json['handler'] = cls.name
    return json


@define
class EncodeHandler(Handler):
    encodings: Sequence[Literal['gzip', 'ztsd']]


@define
class FileServerHandler(Handler):
    root: str = None
    hide: Sequence[str] = field(factory=list)
    index_names: Sequence[str] = field(factory=list)
    browse: U[dict, bool] = None
    canonical_uris: bool = None
    status_code: int = None
    pass_thru: bool = None
    precompressed: dict = field(factory=dict)
    precompressed_order: list[str] = field(factory=list)


@convert.register
def convert_file_server(obj: FileServerHandler):
    json = convert_attr(obj)

    if obj.root is None:
        del json['root']

    if not obj.hide:
        del json['hide']

    if not obj.index_names:
        del json['index_names']

    if obj.browse is None:
        del json['browse']

    if obj.status_code is None:
        del json['status_code']

    if obj.pass_thru is None:
        del json['pass_thru']

    if not obj.precompressed:
        del json['precompressed']

    if not obj.precompressed_order:
        del json['precompressed_order']

    if obj.canonical_uris is None:
        del json['canonical_uris']

    return json


@convert.register
def convert_encode(obj: EncodeHandler):
    cls = obj.__class__

    encodings = {
        encoding: {}
        for encoding in obj.encodings
    }

    return dict(
        handler=cls.name,
        encodings=encodings,
    )


class ReplaceHeader(NamedTuple):
    search: U[str, Pattern]
    replace: str


@convert.register
def convert_replace_header(obj: ReplaceHeader):
    result = dict(replace=obj.replace)

    if isinstance(obj.search, Pattern):
        result['search_regex'] = obj.search.pattern
    else:
        result['search'] = obj.search

    return result


class Header(CIMultiDict):
    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]

    def __getattr__(self, key):
        return self[key]


@convert.register
def convert_header(obj: Header):
    return {
        key: obj.getall(key)
        for key in obj
    }


@define
class CaddyHeader:
    add: Header = field(factory=Header)
    set: Header = field(factory=Header)  # noqa: A003
    replace: Header[ReplaceHeader] = field(factory=Header)
    delete: list[str] = field(factory=list)


@define
class Require:
    status_code: list[int] = field(factory=list)
    headers: Header = field(converter=Header, factory=list)

    def __bool__(self):
        return bool(self.status_code) and bool(self.headers)


@define
class ResponseHeader(CaddyHeader):
    require: Require = field(factory=Require)
    deferred: bool = False


@convert.register
def convert_response_header(obj: ResponseHeader):
    json = convert_attr(obj)
    if not obj.require:
        del json['require']

    return json


@define
class HeadersHandler(Handler):
    request: CaddyHeader = field(factory=CaddyHeader)
    response: ResponseHeader = field(factory=ResponseHeader)


@define
class ReverseProxyHeaders:
    request: CaddyHeader = field(factory=CaddyHeader)
    response: ResponseHeader = field(factory=ResponseHeader)


@define
class Upstream:
    dial: str = ''
    lookup_srv: str = ''
    max_requests: int = 0


def convert_to_upstream(val):
    if isinstance(val, Upstream):
        return val
    else:
        return Upstream(val)


class Pipe(tuple):
    def __new__(cls, *args):
        return super().__new__(cls, args)

    def __call__(self, arg):
        for func in self:
            arg = func(arg)

        return arg

    def __reversed__(self):
        return Pipe(*super().__reversed__())


upstream_convert = Pipe(partial(map, convert_to_upstream), list)


@define
class ReverseProxyHandler(Handler):
    upstreams: list[Upstream] = field(factory=list, converter=upstream_convert)
    headers: ReverseProxyHeaders = field(factory=ReverseProxyHeaders)
    flush_interval: int = 0
    buffer_requests: bool = False
    buffer_responses: bool = False
    max_buffer_size: int = 0


@define
class SubrouteHandler(Handler):
    routes: list[Route] = field(factory=list)
    errors: dict[str, list[Route]] = field(factory=dict)


class VarsHandler(Handler, dict):
    pass


@convert.register
def convert_vars_handler(obj: VarsHandler):
    # Convert to normal dict
    json = {} | obj
    json['handler'] = 'vars'

    return json


@define
class UriSubstring:
    find: str
    replace: str
    limit: int = 0


@define
class UriPathRegexp:
    find: U[Pattern, str]
    replace: str


@define
class RewriteHandler(Handler):
    method: str = None
    uri: str = None
    strip_path_prefix: str = None
    strip_path_suffix: str = None
    uri_substring: Sequence[UriSubstring] = field(factory=list)
    path_regexp: Sequence[UriPathRegexp] = field(factory=list)


@convert.register
def convert_rewrite_handler(obj: RewriteHandler):
    json = convert_attr(obj)

    if obj.method is None:
        del json['method']

    if obj.uri is None:
        del json['uri']

    if obj.strip_path_prefix is None:
        del json['strip_path_prefix']

    if obj.strip_path_suffix is None:
        del json['strip_path_suffix']

    if not obj.uri_substring:
        del json['uri_substring']

    if not obj.path_regexp:
        del json['path_regexp']

    return json


def no_and() -> NoReturn:
    raise TypeError(
        "MatcherList cannot be AND'ed.",
    )


class Matcher:
    name: ClassVar[str]
    matcher_classes: ClassVar[dict[str, type]] = {}

    def __new__(cls, name, *args, **kwargs):
        if cls is not Matcher:
            # When called from a subclass name is not name,
            # it is just the first arg to the subclass
            return super().__new__(cls, name, *args, **kwargs)
        elif name in cls.matcher_classes:
            new_cls = cls.matcher_classes[name]
            return new_cls.__new__(new_cls, *args, **kwargs)
        else:
            raise TypeError(f'{name} is not a registered matcher type')

    def __init_subclass__(cls, **kwargs):
        name = cls.__name__.removesuffix('Matcher').lower()
        cls.name = name
        cls.matcher_classes[name] = cls

    def __or__(self, other: U[Matcher, MatcherList, MatcherSet]):
        if isinstance(other, Matcher):
            return MatcherList(MatcherSet(self), MatcherSet(other))
        elif isinstance(other, MatcherSet):
            return MatcherList(other, MatcherSet(self))
        elif isinstance(other, MatcherList):
            return MatcherList(self, *other)
        else:
            return NotImplemented

    __ror__ = __or__

    def __and__(self, other: U[Matcher, MatcherSet]):
        if isinstance(other, Matcher):
            return MatcherSet(self, other)
        elif isinstance(other, MatcherSet):
            return MatcherSet(self, *other)
        elif isinstance(other, MatcherList):
            no_and()
        else:
            return NotImplemented

    __rand__ = __and__


class MatcherTuple(tuple):
    def __new__(cls, *args) -> MatcherTuple:
        if len(args) == 1 and isinstance(args[0], cls):
            return args[0]

        if hasattr(cls, '_coerce'):
            args = cls._coerce(args)

        return super().__new__(cls, args)

    __add__ = None
    __mul__ = None
    __rmul__ = None

    def __getnewargs__(self):
        return tuple(self)

    def __repr__(self):
        cls = self.__class__
        args = ', '.join(
            repr(item)
            for item in self
        )
        return f'{cls.__name__}({args})'


class HostMatcher(Matcher, MatcherTuple):
    def __add__(self, other: HostMatcher):
        if isinstance(other, HostMatcher):
            return HostMatcher(*self, *other)
        else:
            return NotImplemented


class PathMatcher(Matcher, MatcherTuple):
    def __add__(self, other: PathMatcher):
        if isinstance(other, PathMatcher):
            return PathMatcher(*self, *other)
        else:
            return NotImplemented


class VarsMatcher(Matcher, dict):
    def __add__(self, other: VarsMatcher):
        cls = self.__class__
        if isinstance(other, VarsMatcher):
            return cls(self.copy().update(other))
        else:
            return NotImplemented


get_name = attrgetter('name')


class MatcherSet(MatcherTuple):
    """Caddy will AND the matchers in the set."""

    def __new__(cls, *args: Matcher) -> MatcherSet:
        return super().__new__(cls, *(
            reduce(add, matchers)
            for name, matchers in groupby(
                sorted(args, key=get_name),
                key=get_name,
            )
        ))

    def __and__(self, other: U[MatcherSet, Matcher]) -> MatcherSet:
        cls = self.__class__
        if isinstance(other, MatcherSet):
            return cls(*self, *other)
        elif isinstance(other, MatcherList):
            no_and()
        elif isinstance(other, Matcher):
            return cls(*self, other)
        else:
            return NotImplemented

    __rand__ = __and__

    def __or__(self, other: any_matcher) -> MatcherList:
        cls = self.__class__
        if isinstance(other, MatcherList):
            other_cls = other.__class__
            return other_cls(self, *other)
        elif isinstance(other, Matcher):
            return MatcherList(self, cls(other))
        elif isinstance(other, MatcherSet):
            return MatcherList(self, other)
        else:
            return NotImplemented

    __ror__ = __or__


@convert.register
@cache
def convert_matcher_set(obj: MatcherSet):
    return {
        matcher.name: convert(matcher)
        for matcher in obj
    }


args_type = Iterable[U[Matcher, MatcherSet]]


class MatcherList(MatcherTuple):
    """Caddy will OR the matchers in the list."""

    @classmethod
    def _coerce(cls, args: args_type) -> Iterable[MatcherSet]:
        for arg in args:
            yield MatcherSet(arg)

    def __or__(self, other: any_matcher) -> MatcherList:
        cls = self.__class__
        if isinstance(other, MatcherList):
            return cls(*self, *other)
        elif isinstance(other, Matcher):
            return cls(*self, MatcherSet(other))
        elif isinstance(other, MatcherSet):
            return cls(*self, other)
        else:
            return NotImplemented

    __ror__ = __or__

    def __and__(self, other) -> NoReturn:
        if isinstance(other, (MatcherList, MatcherSet, Matcher)):
            no_and()
        else:
            return NotImplemented

    __rand__ = __and__


def to_handle(new_value):
    if isinstance(new_value, Handler):
        return [new_value]
    else:
        return new_value


handle_type = Sequence[Handler]

any_matcher = U[Matcher, MatcherSet, MatcherList]


@define
class Route:
    match: MatcherList
    handle: handle_type = field(factory=list, converter=to_handle)
    group: Optional[str] = ''
    terminal: bool = False


@define
class Site:
    name: str
    hostname: str
    port: int
    local_hostname: str
    extra_routes: Optional[list[dict]] = None


def add_standard_headers(headers):
    headers.response.delete += ('server', 'X-Powered-By')
    headers.response.deferred = True
    set_headers = headers.response.set
    set_headers['referrer-policy'] = 'no-referrer'
    set_headers['strict-transport-security'] = 'max-age=31536000;'
    set_headers['x-content-type-options'] = 'nosniff'
    set_headers['x-frame-options'] = 'DENY'
    set_headers['x-permitted-cross-domain-policies'] = 'none'
    add_headers = headers.response.add

    """
        "A man is not dead while his name is still spoken."
            - Going Postal, Chapter 4 prologue
    """
    add_headers.add('x-clacks-overhead', 'GNU Terry Pratchett')
    add_headers.add('x-clacks-overhead', 'GNU Eddie Patterson')
    add_headers.add('x-clacks-overhead', 'GNU Katelyn Barnes')


@convert.register
def convert_site(obj: Site):
    headers = HeadersHandler()
    add_standard_headers(headers)

    handlers = [
        EncodeHandler(encodings=('zstd', 'gzip')),
        headers,
        ReverseProxyHandler([f'{obj.local_hostname}:{obj.port}']),
    ]

    route = Route(
        match=MatcherList(HostMatcher(obj.hostname)),
        handle=handlers,
        terminal=True,
        group=obj.hostname,
    )

    if obj.extra_routes:
        all_routes = SubrouteHandler()
        all_routes.routes += obj.extra_routes
        all_routes.routes.append(route)
        route = Route(
            match=MatcherList(HostMatcher(obj.hostname)),
            handle=[all_routes],
            terminal=True,
        )

    return convert(route)
