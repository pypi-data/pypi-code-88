"""
jsonref with YAML reading added

copied directly from jsonref v0.2, with added routines _yaml_load
and _yaml_loads replacing json.load and json.loads
Added/modified lines are marked "# WCC"
"""
import functools
import os
import json
import yaml # WCC
import operator
import re
import sys
import warnings
import copy
from pathlib import Path

from ..misc.remoteGitLab import gitLabFile

from ..misc.discoveryfiles import Datapath

try:
    from collections.abc import Mapping, MutableMapping, Sequence
except ImportError:
    from collections import Mapping, MutableMapping, Sequence

PY3 = sys.version_info[0] >= 3

from urllib import parse as urlparse
from urllib.parse import unquote
from urllib.request import urlopen

unicode = str
basestring = str
iteritems = operator.methodcaller("items")

try:
    # If requests >=1.0 is available, we will use it
    import requests

    if not callable(requests.Response.json):
        requests = None
except ImportError:
    requests = None

from proxytypes import LazyProxy, Proxy

__version__ = "0.2"


class JsonRefError(Exception):
    def __init__(self, message, reference, uri="", base_uri="", path=(), cause=None):
        self.message = message
        self.reference = reference
        self.uri = uri
        self.base_uri = base_uri #TODO: check base_uri
        self.path = list(path)
        self.cause = self.__cause__ = cause

    def __repr__(self):
        return "<%s: %r>" % (self.__class__.__name__, self.message)

    def __str__(self):
        return str(self.message)


class JsonRef(LazyProxy):
    """
    A lazy loading proxy to the dereferenced data pointed to by a JSON
    Reference object.

    """

    __notproxied__ = ("__reference__",)

    @classmethod
    def replace_refs(cls, obj, _recursive=False, **kwargs):
        """
        Returns a deep copy of `obj` with all contained JSON reference objects
        replaced with :class:`JsonRef` instances.

        :param obj: If this is a JSON reference object, a :class:`JsonRef`
            instance will be created. If `obj` is not a JSON reference object,
            a deep copy of it will be created with all contained JSON
            reference objects replaced by :class:`JsonRef` instances
        :param base_uri: URI to resolve relative references against
        :param loader: Callable that takes a URI and returns the parsed JSON
            (defaults to global ``jsonloader``, a :class:`JsonLoader` instance)
        :param jsonschema: Flag to turn on `JSON Schema mode
            <http://json-schema.org/latest/json-schema-core.html#anchor25>`_.
            'id' keyword changes the `base_uri` for references contained within
            the object
        :param load_on_repr: If set to ``False``, :func:`repr` call on a
            :class:`JsonRef` object will not cause the reference to be loaded
            if it hasn't already. (defaults to ``True``)

        """
        
        
       
        store = kwargs.setdefault("_store", _URIDict())
        base_uri, frag = urlparse.urldefrag(kwargs.get("base_uri", "")) #TODO: check base_uri
        
        store_uri = None  # If this does not get set, we won't store the result
        if not frag and not _recursive:
            store_uri = base_uri
        try:
            if kwargs.get("jsonschema") and isinstance(obj["id"], basestring): # It's a schema
                kwargs["base_uri"] = urlparse.urljoin( #TODO: check base_uri
                    kwargs.get("base_uri", ""), obj["id"]
                )
                store_uri = kwargs["base_uri"]
        except (TypeError, LookupError):
            pass

        try:
            if not isinstance(obj["$ref"], basestring): #It's a $ref but not a string
                raise TypeError
        except (TypeError, LookupError):
            pass
        else:
            return cls(obj, **kwargs) #__init__ and Return JsonRef object (content of $ref) if a string

        # If our obj was not a json reference object, iterate through it,
        # replacing children with JsonRefs
        kwargs["_recursive"] = True
        path = list(kwargs.pop("_path", ()))
        if isinstance(obj, Mapping):
            obj = type(obj)( #Calls __init__ for the relevant object type
                (k, cls.replace_refs(v, _path=path + [k], **kwargs))
                for k, v in iteritems(obj)
            )
        elif isinstance(obj, Sequence) and not isinstance(obj, basestring):
            obj = type(obj)( #Calls __init__ for the relevant object type
                cls.replace_refs(v, _path=path + [i], **kwargs)
                for i, v in enumerate(obj)
            )
        #else obj is a "leaf" object (not a list, not a directory) and thus not replaceable, we simply return it
        
        if store_uri is not None:
            store[store_uri] = obj
            
        return obj

    def __init__(
        self,
        refobj,
        base_uri="",
        loader=None,
        jsonschema=False,
        load_on_repr=True,
        _path=(),
        _store=None,
        datapath=None,
    ):
        if not isinstance(refobj.get("$ref"), basestring):
            raise ValueError("Not a valid json reference object: %s" % refobj)

        self.__reference__ = refobj
        self.base_uri = base_uri #TODO: check base_uri
        self.loader = loader or jsonloader
        self.jsonschema = jsonschema
        self.load_on_repr = load_on_repr
        self.path = list(_path)
        self.store = _store  # Use the same object to be shared with children
        self.datapath = datapath
        if self.store is None:
            self.store = _URIDict()

    @property
    def _ref_kwargs(self):
        return dict(
            base_uri=self.base_uri,
            loader=self.loader,
            jsonschema=self.jsonschema,
            load_on_repr=self.load_on_repr,
            _path=self.path,
            _store=self.store,
            datapath = self.datapath,
        )

    @property
    def full_uri(self):
        kwargs = self._ref_kwargs
        dp = kwargs["datapath"]
        
        if not dp:
            print(f'Error in datapath in full_uri, reference: {self.__reference__["$ref"]}')
            raise ValueError
        
        base_uri = Path(dp.build_datapath(self.__reference__["$ref"]))
        
        self.base_uri = unquote(urlparse.urlsplit(str(base_uri)).path if gitLabFile.isRemote(str(base_uri)) \
                                  else base_uri.as_uri())
        return(self.base_uri) 
        #return urlparse.urljoin(str(self.base_uri), self.__reference__["$ref"]) #TODO: check base_uri

    def callback(self):
        uri, fragment = urlparse.urldefrag(self.full_uri)
        # If we already looked this up, return a reference to the same object
        if uri in self.store:
            result = self.resolve_pointer(self.store[uri], fragment)
        else:
            # Remote ref
            try:              
                base_doc = self.loader(uri)
            except Exception as e:
                # self._error("%s: %s" % (e.__class__.__name__, unicode(e)), cause=e)
                # WCC
                print(e)
                return None
                

            kwargs = self._ref_kwargs
            kwargs["base_uri"] = uri #TODO: check if base_uri is OK here
            base_doc = JsonRef.replace_refs(base_doc, **kwargs)
            result = self.resolve_pointer(base_doc, fragment)
            
        if hasattr(result, "__subject__"):
            # TODO: Circular ref detection
            result = result.__subject__
        return result

    def resolve_pointer(self, document, pointer):
        """
        Resolve a json pointer ``pointer`` within the referenced ``document``.

        :argument document: the referent document
        :argument str pointer: a json pointer URI fragment to resolve within it

        """
        # Do only split at single forward slashes which are not prefixed by a caret
        parts = re.split(r"(?<!\^)/", unquote(pointer.lstrip("/"))) if pointer else []

        for part in parts:
            # Restore escaped slashes and carets
            replacements = {r"^/": r"/", r"^^": r"^"}
            part = re.sub(
                "|".join(re.escape(key) for key in replacements.keys()),
                lambda k: replacements[k.group(0)],
                part,
            )
            if isinstance(document, Sequence):
                # Try to turn an array index to an int
                try:
                    part = int(part)
                except ValueError:
                    pass
            try:
                document = document[part]
            except (TypeError, LookupError) as e:
                self._error("Unresolvable JSON pointer: %r" % pointer, cause=e)
        return document

    def _error(self, message, cause=None):
        raise JsonRefError(
            message,
            self.__reference__,
            uri=self.full_uri,
            base_uri=self.base_uri, #TODO: check base_uri
            path=self.path,
            cause=cause,
        )

    def __repr__(self):
        if hasattr(self, "cache") or self.load_on_repr:
            return repr(self.__subject__)
        return "JsonRef(%r)" % self.__reference__


class _URIDict(MutableMapping):
    """
    Dictionary which uses normalized URIs as keys.

    """

    def normalize(self, uri):
        return urlparse.urlsplit(uri).geturl()

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.store.update(*args, **kwargs)

    def __getitem__(self, uri):
        return self.store[self.normalize(uri)]

    def __setitem__(self, uri, value):
        self.store[self.normalize(uri)] = value

    def __delitem__(self, uri):
        del self.store[self.normalize(uri)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __repr__(self):
        return repr(self.store)


class JsonLoader(object):
    """
    Provides a callable which takes a URI, and returns the loaded JSON referred
    to by that URI. Uses :mod:`requests` if available for HTTP URIs, and falls
    back to :mod:`urllib`. By default it keeps a cache of previously loaded
    documents.

    :param store: A pre-populated dictionary matching URIs to loaded JSON
        documents
    :param cache_results: If this is set to false, the internal cache of
        loaded JSON documents is not used

    """

    def __init__(self, store=(), cache_results=True):
        self.store = _URIDict(store)
        self.cache_results = cache_results

    def __call__(self, uri, **kwargs):
        """
        Return the loaded JSON referred to by `uri`

        :param uri: The URI of the JSON document to load
        :param kwargs: Keyword arguments passed to :func:`json.loads`

        """
        if uri in self.store:
            return self.store[uri]
        else:
            result = self.get_remote_json(uri, **kwargs)
            if self.cache_results:
                self.store[uri] = result
            return result

    def get_remote_json(self, uri, **kwargs):
        scheme = urlparse.urlsplit(uri).scheme
        path = urlparse.urlsplit(uri).path

        # Open locally or remotely according to scheme     
        result = _yaml_loads(urlopen(uri).read().decode("utf-8") if scheme == 'file' \
                                  else gitLabFile.get_gitlab_file(path), 
                             **kwargs)   # WCC
        
        return result


jsonloader = JsonLoader()
# jsonloader = YAMLLoader() # WCC


def load(fp, base_uri="", loader=None, jsonschema=False, load_on_repr=True, datapath=None,
         **kwargs):
    """
    Drop in replacement for :func:`json.load`, where JSON references are
    proxied to their referent data.

    :param fp: File-like object containing JSON document
    :param kwargs: This function takes any of the keyword arguments from
        :meth:`JsonRef.replace_refs`. Any other keyword arguments will be
        passed to :func:`json.load`

    """
    if loader is None:
        loader = functools.partial(jsonloader, **kwargs)
        
    #base_uri = "file:///home/susana/obsinfo-0.109/obsinfo/_examples/Information_Files/network/"
    # Convert encoded characters
    base_uri = unquote(base_uri)
    
    return JsonRef.replace_refs(
        _yaml_load(fp, **kwargs), # WCC
        base_uri=base_uri, #TODO: check base_uri
        loader=loader,
        jsonschema=jsonschema,
        load_on_repr=load_on_repr,
        datapath=datapath, #LFA. Datapath is the list of paths where files can potentialy be found
    )


def loads(s, base_uri="", loader=None, jsonschema=False, 
          load_on_repr=True, datapath=None, recursive=True, **kwargs):
    """
    Drop in replacement for :func:`json.loads`, where JSON references are
    proxied to their referent data.

    :param s: String containing JSON document
    :param kwargs: This function takes any of the keyword arguments from
        :meth:`JsonRef.replace_refs`. Any other keyword arguments will be passed to
        :func:`json.loads`

    """
    
    if loader is None:
        loader = functools.partial(jsonloader, **kwargs)
    
    dic = _yaml_loads(s, **kwargs) if isinstance(s, str) else s
        
    if recursive:
        return JsonRef.replace_refs(
            dic,  # WCC et LFA
            base_uri=base_uri, #TODO: check base_uri
            loader=loader,
            jsonschema=jsonschema,
            load_on_repr=load_on_repr,
            datapath=datapath,
        )
    else:
        return dic


def load_uri(uri, base_uri=None, loader=None, jsonschema=False, load_on_repr=True):
    """
    Load JSON data from ``uri`` with JSON references proxied to their referent
    data.

    :param uri: URI to fetch the JSON from
    :param kwargs: This function takes any of the keyword arguments from
        :meth:`JsonRef.replace_refs`

    """

    if loader is None:
        loader = jsonloader
    if base_uri is None: 
        base_uri = uri #LFA #TODO: check if OK

    return JsonRef.replace_refs(
        loader(uri),
        base_uri=base_uri,
        loader=loader,
        jsonschema=jsonschema,
        load_on_repr=load_on_repr,
        datapath=datapath,
    )

# WCC ADDED BEGIN
# Method read_json_yaml_ref  in ObsMetadata uses load, not loads. Load loads a file.
def _yaml_load(fp, **kwargs):
    """ Call {yaml,json}.load according to file type """
    try:
        return json.load(fp, **kwargs)
    # except JSONDecodeError:
    except:
        fp.seek(0)
        try:
            return yaml.safe_load(fp)
        # except ScannerError:
        except:
            warnings.warn(f'file {fp.name} is neither JSON nor YAML')
            raise
    return None

# Method validate in ObsMetadata uses loads, not load. loads loads a string, not a file.
def _yaml_loads(s, **kwargs):
    """ Call {yaml,json}.loads according to file type """
    a = None
    
    kw = copy.deepcopy(kwargs) #copy to make sure you don alter the original kwargs
    kw.pop('base_uri', None)
    kw.pop('datapath', None)
    
    if s[:3] == '---':
        try:
            a = yaml.safe_load(s, **kw)
        except:
            try:
                a = json.loads(s, **kwargs)
            except:
                warnings.warn(f'string is neither JSON nor YAML:\n{s}')
                raise
    else:
        try:
            a = json.loads(s, **kwargs)
        except:
            try:
                a = yaml.safe_load(s, **kwargs)
            except:
                warnings.warn('string is neither JSON nor YAML')
                raise
            
    return a
# WCC ADDED END

def dump(obj, fp, **kwargs):
    """
    Serialize `obj`, which may contain :class:`JsonRef` objects, as a JSON
    formatted stream to file-like `fp`. `JsonRef` objects will be dumped as the
    original reference object they were created from.

    :param obj: Object to serialize
    :param fp: File-like to output JSON string
    :param kwargs: Keyword arguments are the same as to :func:`json.dump`

    """
    # Strangely, json.dumps does not use the custom serialization from our
    # encoder on python 2.7+. Instead just write json.dumps output to a file.
    fp.write(dumps(obj, **kwargs))


def dumps(obj, **kwargs):
    """
    Serialize `obj`, which may contain :class:`JsonRef` objects, to a JSON
    formatted string. `JsonRef` objects will be dumped as the original
    reference object they were created from.

    :param obj: Object to serialize
    :param kwargs: Keyword arguments are the same as to :func:`json.dumps`

    """
    kwargs["cls"] = _ref_encoder_factory(kwargs.get("cls", json.JSONEncoder))
    return json.dumps(obj, **kwargs)


def _ref_encoder_factory(cls):
    class JSONRefEncoder(cls):
        def default(self, o):
            if hasattr(o, "__reference__"):
                return o.__reference__
            return super(JSONRefEncoder, cls).default(o)

        # Python 2.6 doesn't work with the default method
        def _iterencode(self, o, *args, **kwargs):
            if hasattr(o, "__reference__"):
                o = o.__reference__
            return super(JSONRefEncoder, self)._iterencode(o, *args, **kwargs)

        # Pypy doesn't work with either of the other methods
        def _encode(self, o, *args, **kwargs):
            if hasattr(o, "__reference__"):
                o = o.__reference__
            return super(JSONRefEncoder, self)._encode(o, *args, **kwargs)

    return JSONRefEncoder
