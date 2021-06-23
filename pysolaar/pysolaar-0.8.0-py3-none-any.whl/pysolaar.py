from collections.abc import Iterable
from contextlib import contextmanager
from functools import wraps
import itertools
import sys
from types import FunctionType
from typing import (
    Callable,
    Dict,
    Generator,
    Iterable,
    Set,
    Sized,
    Tuple,
    Union,
    Any,
    List,
)

import warnings

from icecream import ic
import pysolr

from pysolaar.document import BaseDocument
from pysolaar.utils.meta_utils import (
    BaseMeta,
    ChildDocument,
    DocumentFields,
    SplattedChildDocument,
)
from pysolaar.queryset import PySolaarQuerySetBase, Q
from pysolaar.result import PySolaarResultsBase
from pysolaar.utils.chunks import chunks
from pysolaar.utils.exceptions import PySolaarConfigurationError, PySolaarDocumentError


class CachedGenerator(list):
    pass


class PySolaarConfigurationWarning(UserWarning):
    pass


class PySolaarMeta(type):
    """Calling __len__ and __iter__ on a class is presumably
    utter batshit. But why not. Finally found a use for metaclasses.
    """

    def __len__(cls):
        return cls.proxy_len()

    def __iter__(cls):
        return cls.proxy_iter()


class PySolaar(metaclass=PySolaarMeta):
    __subclasses: Dict = {}
    _solr: Union[pysolr.Solr, None] = None
    CLASS_EMBEDDING_DEPTH: int

    @classmethod
    def configure_pysolr(cls, url: str = "None", pysolr_object=None, **kwargs):

        if cls.__name__ != "PySolaar":
            raise PySolaarConfigurationError(
                "`configure_pysolr` can only be called from the main PySolaar class."
            )
        if pysolr_object:
            cls._solr = pysolr_object
        else:
            cls._solr = pysolr.Solr(
                url,
                always_commit=kwargs.pop("always_commit")
                if "always_commit" in kwargs
                else True,
                **kwargs,
            )

    @classmethod
    def get_subclass(cls, name):
        return cls.__subclasses[name]

    @classmethod
    def _RESET(cls) -> None:
        """Method used by pytest fixture to reset the listed
        subclasses between each test.
        """
        cls.__subclasses = {}
        cls._solr = None
        cls._DOCUMENT_CACHE = {}

    class Meta:
        """ Set Meta variables for this PySolaar class. """

        # I guess the default-of-defaults could be set elsewhere by modifiying this
        # class?
        pass

    class Document:
        """ Create a document of this type. """

        """ This is here as a placeholder so typechecking tools don't complain about
        such a thing not existing when it's used in a base class. It's overwritten dynamically
        at runtime.
        
        FAKE is here to identify this version, so our override doesn't from it, but can inherit from 
        a Document class created by user. """
        __FAKE = True

        def __new__(cls, id="ID", *args, **kwargs):
            raise PySolaarConfigurationError(
                "Only subclasses of PySolaar have an associated Document type."
            )

    def __init_subclass__(cls) -> None:
        """On the **declaration** of a subclass — i.e. the moment PySolaar is subclasses, not init'd -
        do the following:
            -   Check whether the subclass implements "build_document_set" and "build_document" and
                converts them into a classmethod
            -   Replace the un-implemented Document class above with a subclass of BaseDocument,
                replacing the default 'meta' field with a dict of variables from the subclass's Meta
                class.
        """

        if cls.__name__ in cls.__subclasses:
            raise PySolaarConfigurationError(
                f"PySolaar class {cls.__name__} has already been created."
            )

        ######################################################################
        # Replace cls.Meta with a new class of Meta, inheriting from BaseMeta
        # (as if we just subclasses BaseMeta on declaration, but that's now not necessary)
        # and also stick the "pysolaar_type" in there as well for good measure
        cls.Meta = type(
            "Meta",
            (cls.Meta, BaseMeta, object),
            {"pysolaar_type": cls.__name__},
        )  # type: ignore
        ######################################################################

        ######################################################################
        # Create a subclass's Result type!
        cls.Results = type(
            f"{cls.__name__}Results",
            (PySolaarResultsBase,),
            {
                "pysolaar_type": cls.__name__,
                "Meta": cls.Meta,
                "_solr": cls._solr,
            },
        )
        #
        ######################################################################

        ######################################################################
        # Create a subclass's QuerySet type!
        cls.QuerySet = type(
            f"{cls.__name__}QuerySet",
            (PySolaarQuerySetBase,),
            {
                "pysolaar_type": cls.__name__,
                "Meta": cls.Meta,
                "_solr": cls._solr,
                "_results_class": cls.Results,
            },
        )
        #
        ######################################################################

        ######################################################################
        # Also create a Document type for this subclass, inheriting from BaseDocument and from
        # any user-defined Document class that has been confirmed to be not the one above with
        # __FAKE attribute.
        # print(cls.__bases__[0].__name__)
        inherited_from = BaseDocument
        for c in cls.__mro__:
            if hasattr(c, "Document") and not hasattr(c.Document, "_Document__FAKE"):
                inherited_from = c.Document
                break

        doc_class_inherits: Tuple = (
            (
                inherited_from,
                BaseDocument,
            )
            if inherited_from is not BaseDocument
            else (BaseDocument,)
        )
        cls.Document = type(f"{cls.__name__}Document", doc_class_inherits, {"Meta": cls.Meta})  # type: ignore

        if hasattr(cls, "build_document_set") and getattr(cls, "build_document_set"):
            cls.build_document_set = classmethod(getattr(cls, "build_document_set"))  # type: ignore
        elif not hasattr(cls, "build_document_set"):
            warnings.warn(
                (
                    f"PySolaar subclass {cls.__name__} has no `build_document_set` method.\n"
                    "Explicitly set `build_document_set = None` in the subclass to silence this warning."
                ),
                PySolaarConfigurationWarning,
            )
        """
        # CHANGE: No longer raise an error if `build_document_set` is not provided.
                  Obviously, this stops the class being automatically called (or called at all?)
                  by Pysolaar.update()
        ## CHANGE: now should raise a warning!
        
        else:
            raise PySolaarConfigurationError(
                f"PySolaar subclass <{cls.__name__}> must implement a 'build_document_set' method."
            )
        """
        ######################################################################

        ## Here we make sure cls.build_document is appropriately handled.

        ## The user will declare the method in their implemented subclass,
        ## as a normal instance method, so we get it and wrap it with classmethod decorator
        if "build_document" in cls.__dict__ and hasattr(cls, "build_document"):
            # This is the class implementing
            cls.build_document: Union[Iterable[BaseDocument], BaseDocument] = classmethod(cls._wrap_build_document_in_cache(getattr(cls, "build_document")))  # type: ignore

        ## If a subclass has been inheritted from another subclass, and does not implement its
        ## own 'build_document' method, it can obviously leech off the parent for functionality
        ## but we need to take those results and change their classes into the child class's
        ## document type!
        elif hasattr(cls, "build_document"):

            def wrapping_build_document(build_document_func):
                def inner(self, identifier):

                    built_docs = build_document_func(identifier)
                    if isinstance(built_docs, BaseDocument):
                        doc = cls.Document(**built_docs._values)
                        doc.Meta = cls.Meta
                        return doc
                    elif isinstance(built_docs, Iterable) and not isinstance(
                        built_docs, str
                    ):

                        def do_building(built_doc):
                            if not isinstance(built_doc, BaseDocument):
                                raise PySolaarDocumentError(
                                    f"{cls.__name__}.build_document should return either "
                                    "a single Document instance, or an iterable of Document instances, not a"
                                    f" iterable of {type(built_doc).__name__}s."
                                )
                            doc = cls.Document(**built_doc._values)
                            doc.Meta = cls.Meta
                            return doc

                        docs = (do_building(built_doc) for built_doc in built_docs)

                        # If it's an iterable, return it in the same type we were given
                        # or if generator, return a generator object
                        try:
                            return type(built_docs)(docs)
                        except TypeError:
                            return docs
                    else:
                        raise PySolaarDocumentError(
                            f"{cls.__name__}.build_document should return either "
                            "a single Document instance, or an iterable of Document instances."
                        )

                return inner

            cls.build_document = classmethod(
                cls._wrap_build_document_in_cache(
                    wrapping_build_document(getattr(cls, "build_document"))
                )
            )  # type: ignore
        else:
            raise PySolaarConfigurationError(
                f"PySolaar subclass <{cls.__name__}> must implement a 'build_document' method."
            )

        # Stores the subclass in Pysolaar._subclasses, with whatever information required
        cls.__subclasses[cls.__name__] = {
            "class": cls,
        }

        cls.CLASS_EMBEDDING_DEPTH = 0
        cls._DOCUMENT_CACHE = {}

    @classmethod
    def _wrap_build_document_in_cache(cls, build_doc_func):
        """ Wrapper for build_document to cache results after first call"""

        def inner(cls, identifier):
            if identifier in cls._DOCUMENT_CACHE:
                res = cls._DOCUMENT_CACHE[identifier]
                if type(res).__name__ in {"CachedGenerator"}:
                    # If the type is a CachedGenerator (i.e. 'list')
                    # return it as a generator object, as this is
                    # presumably expected if not cached...
                    return (d for d in res)
                else:
                    return res
            else:
                res = build_doc_func(cls, identifier)
                if type(res).__name__ == "generator":
                    # As we're going to call the generator anyway, we
                    # might as well cache the results ...
                    cls._DOCUMENT_CACHE[identifier] = CachedGenerator()

                    # Create a function to both add the doc to the cache
                    # and return it...
                    def get_and_append(d):
                        cls._DOCUMENT_CACHE[identifier].append(d)
                        return d

                    # So that we can return in this generator object
                    return (get_and_append(d) for d in res)
                else:
                    cls._DOCUMENT_CACHE[identifier] = res
                    return res

        return inner

    @classmethod
    def _decr_csd(cls):
        cls.CLASS_EMBEDDING_DEPTH -= 1

    @classmethod
    def _incr_csd(cls):
        cls.CLASS_EMBEDDING_DEPTH += 1

    @classmethod
    def items(
        cls,
        identifiers,
        *,
        call=None,
        meta=None,
        select_fields=None,
        exclude_fields=None,
        fields_as_json=[],
        do_not_expand=None,
    ) -> FunctionType:

        """ Prepare a list of documents from an iterable of identifiers """
        # TODO: here, we might want to pack several other fields
        embedded_meta: BaseMeta = meta or type(
            "EmbeddedMeta", (cls.Meta,), {"is_embedded": True}
        )
        embedded_meta.is_embedded = True

        for k, v in {
            "select_fields": select_fields,
            "exclude_fields": exclude_fields,
            "fields_as_json": set(fields_as_json),
            "do_not_expand": do_not_expand,
        }.items():
            if v:
                setattr(embedded_meta, k, v)

        # HERE, check whether we have a single identifier or an iterable,
        # and make into a list if not

        # TODO: tuple should not be accepted - should be treated as single value!!!!
        if not isinstance(identifiers, (list, tuple, set, Generator)):
            identifiers = [identifiers]

        """ 
        Here, we do so many things your head might bleed.

        General idea is to return a list of documents to be nested (remember here we're setting the value
        of a particular field inside another class), which is then handled by Document._encode_key_value
         -- BUT:

        To prevent endless (mutual) recursion of mutually embedded documents (or docs whose embedding forms a loop)
        we do a number of things:
            - find out which class's build_document method this particular .items() method is embedded in 
                (i.e. not *THIS* class, cls) by using sys._getframe, and look up that particular class
                in the PySolaar subclasses (this may not be necessary, but seems to stop references being confused 🤷)
            - each subclass has a CLASS_EMBEDDING_DEPTH variable, which keeps count of what 'depth' of embedding of a particular
                class, and when it exceeds e.g. 1 for the calling_class, we replace the calling_class's .items method with
                a function that does nothing (out)
            - once we're done with a particular level of nesting, decrement the CLASS_EMBEDDING_DEPTH, and restore the original
            .items method.
                This roundabout bull is required for a few reasons. Can't just turn off .items once it's been used once, as there
                may be multiple calls to .items from the same document (so not triggering any recursion); essentially, we
                need to turn off .items at higher levels of embedded, not just after multiple calls.

        
        Instead of returning the results directly, they're embedded in a context manager which:
            - defers execution of cls.build_document until we know it's needed (i.e. not in 'exclude_field' etc.)
            - probably safer??

        """

        ## Whatever else, do not move this sys._getframe call, otherwise it won't be the same frame!!
        ## Also, when testing, need to mock this sys._getframe() call to something stable!

        ## Previous versions just looked in sys._getframe(1), which ignored possibility of
        ## PySolaar.items() calls being passed by functions (or functions returning functions, etc.)
        ## into the Document constructor --- so to fix this, we just work our way backwards through frames
        ## until we find something that can be found and is a PySolaar subclass...
        ## Tested by: tests/test_pysolaar_config.py::test_complex_setup_too

        i = 1
        calling_class_name = None
        while i < 10:
            try:
                calling_class_name = sys._getframe(i).f_locals["self"].__name__
                PySolaar.get_subclass(calling_class_name)
                break
            except:
                i += 1

        # calling_class_name = sys._getframe(1).f_locals["self"].__name__
        calling_class = PySolaar.get_subclass(calling_class_name)["class"]
        CALLING_CLASS_ITEMS_BACKUP = calling_class.items

        def null_items(*args, **kwargs):
            @contextmanager
            def get_null_items(field_name=None, document_structure=None):
                ic("Calling end from ", calling_class, "in", cls.__name__)
                yield []  # lambda: []

            return get_null_items

        @contextmanager
        def doc_context(
            field_name=None, document_structure=None
        ) -> Generator[Iterable[BaseDocument], Iterable[BaseDocument], None]:

            """
            Dealing with store_document_fields...

            First time we hit an .items() call in a nesting, i.e. the first level nest,
            then document_structure should be None... it has nothing so far.

            """
            # If we're dealing with an embedding, we shouldn't be using its
            # own store_document_fields, should we? Or we'd be going mad...
            # So nuke it!
            embedded_meta.store_document_fields = []
            if document_structure:
                # print(">        document_structure:", document_structure)
                embedded_meta.store_document_fields = document_structure
                embedded_meta.fields_as_json = {
                    field
                    for field, value in document_structure.items()
                    if isinstance(value, ChildDocument)
                    and not isinstance(value, SplattedChildDocument)
                }
            elif hasattr(embedded_meta, "fields_as_child_docs"):
                if not hasattr(embedded_meta, "fields_as_json"):
                    embedded_meta.fields_as_json = embedded_meta.fields_as_child_docs
                else:
                    embedded_meta.fields_as_json = set(embedded_meta.fields_as_json)
                    for f in embedded_meta.fields_as_child_docs:

                        embedded_meta.fields_as_json.add(f)

            calling_class = PySolaar.get_subclass(calling_class_name)["class"]
            # ic(cls.__name__, calling_class.CLASS_EMBEDDING_DEPTH, calling_class)
            calling_class._incr_csd()
            if calling_class.CLASS_EMBEDDING_DEPTH > 1:
                calling_class.items = null_items

            docs = []
            for identifier in identifiers:

                built_docs = cls.build_document(identifier)  # type: ignore

                if isinstance(built_docs, BaseDocument):
                    built_docs.EmbeddedMeta = embedded_meta
                    built_docs.Meta.is_embedded = True
                    docs.append(built_docs)
                elif isinstance(built_docs, Iterable) and not isinstance(
                    built_docs, str
                ):
                    for built_doc in built_docs:
                        if not isinstance(built_doc, (BaseDocument)):
                            raise PySolaarDocumentError(
                                f"{cls.__name__}.build_document should return either "
                                "a single Document instance, or an iterable of Document instances, not a"
                                f" iterable of {type(built_doc).__name__}s."
                            )

                        built_doc.EmbeddedMeta = embedded_meta
                        built_doc.Meta.is_embedded = True
                        docs.append(built_doc)

            yield docs

            calling_class = PySolaar.get_subclass(calling_class_name)["class"]
            calling_class._decr_csd()
            if calling_class.CLASS_EMBEDDING_DEPTH <= 1:
                calling_class.items = CALLING_CLASS_ITEMS_BACKUP

        return doc_context

    @classmethod
    def _get_documents_to_index(cls) -> Generator[BaseDocument, BaseDocument, None]:
        for name, c_dict in cls.__subclasses.items():
            subclass = c_dict["class"]
            if (
                not hasattr(subclass, "build_document_set")
                or subclass.build_document_set is None
            ):
                continue
            try:
                yield from subclass.build_document_set()
            except TypeError:
                print(subclass.build_document_set)
                print("type error when yielding from subclass", subclass)
                pass
            
    

    @classmethod
    def _yield_solr_prepared_documents(cls):
        for d in cls._get_documents_to_index():
            doc = d.doc_to_solr()
            try:
                # Pre-push nested documents so that Solr accepts that they're real!
                yield from doc["_doc"]
            except:
                pass
            yield doc

    @classmethod
    def update(cls, max_chunk_size=1000):
        for data in chunks(cls._yield_solr_prepared_documents(), size=max_chunk_size):
            docs = list(data)
            # print("DOC>>", docs)
            cls._solr.add(docs)

        # And reset all the document caches...
        for name, c_dict in cls.__subclasses.items():
            subclass = c_dict["class"]
            subclass._DOCUMENT_CACHE = {}
                


    ###########################################################################
    # When querying, we want to start a new query like this:
    #        Thing.filter(something="what")
    # which should return a QuerySet instance. To avoid duplicating all the
    # method definitions, we use the _proxy_to_new_queryset method, which
    # takes the name of a QuerySet method, initialises a query set and
    # dynamically calls named method. Using functools.wraps should ensure
    # that the method signatures are the same.
    #
    def _proxy_to_new_queryset(method_name):
        """Define a method on PySolaar that creates a new QuerySet
        and calls the named method on that QuerySet (returning a new
        queryset)"""

        @classmethod
        @wraps(getattr(PySolaarQuerySetBase, method_name))
        def inner(cls, *args, **kwargs):
            query_set = cls.QuerySet()
            query_set_method = getattr(query_set, method_name, None)
            return query_set_method(*args, **kwargs)

        return inner

    #
    #   And here we proxy the methods:
    #
    all = _proxy_to_new_queryset("all")
    first = _proxy_to_new_queryset("first")
    last = _proxy_to_new_queryset("last")
    filter = _proxy_to_new_queryset("filter")
    filter_by_distinct_child = _proxy_to_new_queryset(
        "filter_by_distinct_child",
    )
    count = _proxy_to_new_queryset("count")
    order_by = _proxy_to_new_queryset("order_by")
    paginate = _proxy_to_new_queryset("paginate")
    # These two here are utterly ridiculous, and require the introduction
    # of a metaclass, pointing to these proxied methods.
    proxy_len = _proxy_to_new_queryset("__len__")
    proxy_iter = _proxy_to_new_queryset("__iter__")
    #
    ###########################################################################