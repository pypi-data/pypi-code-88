import copy
import datetime
import inspect
import json
from typing import Callable, Dict, Generator, Iterable, Set, Union, Any, List

from icecream import ic
import pysolr

from .utils.encoders_and_decoders import (
    ID_SEPARATOR,
    KEY_SEPARATOR,
    encode_id,
    encode_field_name,
)
from .utils.exceptions import PySolaarConfigurationError, PySolaarDocumentError
from .utils.meta_utils import (
    BaseMeta,
    ChildDocument,
    JsonChildDocument,
    DocumentFields,
    SplattedChildDocument,
)


def _splat_to_list(d):
    return_list = []
    for k, v in d.items():
        if isinstance(v, list):
            return_list += v
        elif isinstance(v, dict):
            return_list += _splat_to_list(v)
        elif v:
            return_list.append(v)
    return return_list


class BaseDocument:
    Meta: BaseMeta

    def __init__(self, **kwargs):
        """ Create a document of this type """
        self.__dict__["_values"] = kwargs

    def __getattr__(self, attr: str):
        """So that document attribtes are accessible as values,
        look them up first in self.__values, before returning
        normal class variables. This seem a bad idea?"""
        try:
            return self._values[attr]
        except:
            return self.__dict__[attr]

    def __setattr__(self, attr: str, value: Any) -> None:
        """ Likewise, throw error when setting values... """
        if attr in self._values:
            raise PySolaarDocumentError
        else:
            self.__dict__[attr] = value

    def doc_to_solr(self):
        # Start with the pysolaar_type

        doc = self._encode_key_values(self._values, self.Meta)
        doc["pysolaar_type"] = self.Meta.pysolaar_type
        return doc

    def doc_to_plain_json(self):
        doc = self._encode_key_values(
            self._values,
            self.EmbeddedMeta,
            encode_field_name=lambda meta, value: value,
            encode_id=lambda meta, value: value,
        )
        return doc

    def doc_to_nested_child(self, parent_pysolaar_type, parent_field_name):
        # Start with the pysolaar_type

        nested_encode_id = lambda child_type, id: encode_id(
            parent_pysolaar_type, encode_id(child_type, id)
        )

        nested_encode_field_name = lambda child_type, field_name: encode_field_name(
            parent_pysolaar_type, encode_field_name(parent_field_name, field_name)
        )

        doc = self._encode_key_values(
            self._values,
            self.EmbeddedMeta,
            encode_id=nested_encode_id,
            encode_field_name=nested_encode_field_name,
        )
        doc[
            "pysolaar_type_nested"
        ] = f"{parent_pysolaar_type}{ID_SEPARATOR}{self.Meta.pysolaar_type}{ID_SEPARATOR}{parent_field_name}"
        return doc

    def doc_to_splatted_child(self, field_name=""):
        self.EmbeddedMeta.splat = True
        # self.EmbeddedMeta.splatted_field_name =field_name
        doc = self._encode_key_values(
            self._values,
            self.EmbeddedMeta,
            encode_field_name=lambda meta, value: value,
            encode_id=lambda meta, value: value,
        )
        return doc

    @staticmethod
    def _unpack_meta(field_name: str, meta: BaseMeta) -> Set:
        return set(getattr(meta, field_name, []))

    @staticmethod
    def _encode_key_values(
        _values, meta, encode_id=encode_id, encode_field_name=encode_field_name
    ) -> Dict:

        """Make this a static method so we can inject whatever
        Meta dependencies we like from above functions, and test
        more easily.

        Also trying passing in the encode_id and encode_field_name functions so that
        we can modify them for nested docs."""

        # Unpack meta into sets for quicker access later
        fields_as_json = BaseDocument._unpack_meta("fields_as_json", meta)
        fields_as_child_docs = BaseDocument._unpack_meta("fields_as_child_docs", meta)
        fields_as_splatted_child_docs = BaseDocument._unpack_meta(
            "fields_as_splatted_child_docs", meta
        )

        # select_fields *include* all the fields specified
        select_fields = BaseDocument._unpack_meta("select_fields", meta)
        # exclude_fields *removes* specified fields from complete set
        # select_fields takes precedence

        if getattr(meta, "store_document_fields", []):

            fields_as_child_docs = set()
            select_fields = set()
            fields_as_splatted_child_docs = set()
            has_store_document_fields = True
            for field, value in meta.store_document_fields.items():
                if value:
                    select_fields.add(field)
                if isinstance(value, ChildDocument):
                    fields_as_child_docs.add(field)
                if isinstance(value, JsonChildDocument):
                    fields_as_json.add(field)
                if isinstance(value, SplattedChildDocument):
                    fields_as_splatted_child_docs.add(field)
        else:
            has_store_document_fields = False

        exclude_fields = (
            set([])
            if select_fields
            else BaseDocument._unpack_meta("exclude_fields", meta)
        )

        do_not_expand = BaseDocument._unpack_meta("do_not_expand", meta)
        # print(meta.pysolaar_type, "SELECTFIELDS", select_fields)
        doc = {}
        for key, value in _values.items():

            # print("-----", key, "-----")
            # print("DE", getattr(meta, "dict_embedding", False))
            # print("SF", select_fields)
            # Encode the id with a type prefix;
            # assume the content can't be any odd type
            if key == "id":
                doc["id"] = encode_id(meta.pysolaar_type, value)

            # n.b. the below filters should be placed AFTER key == "id" so that id
            # is always included

            # If select fields are set and the key is not in select fields, then skip
            elif (
                select_fields
                and key not in select_fields
                and not getattr(meta, "dict_embedding", False)
            ):
                continue

            # If it's not in select field and it's an embedded child, skip
            elif select_fields and key not in select_fields and callable(value):
                continue

            elif (
                getattr(meta, "splat", False)
                and select_fields
                and (
                    key not in select_fields and key.split("__")[0] not in select_fields
                )
            ):
                # print("excluding", key)
                continue

            # If exclude fields are set, and the key is in exclude fields, then skip
            elif exclude_fields and key in exclude_fields:
                continue

            # If field is a splat field, or inside a splat field, keep on splatting
            # the selected values down to a list!
            elif (
                key in fields_as_child_docs and key in fields_as_splatted_child_docs
            ) or (key in fields_as_child_docs and getattr(meta, "splat", False)):

                if has_store_document_fields:
                    this_keys_store_document_fields = meta.store_document_fields.get(
                        key, None
                    )
                else:
                    this_keys_store_document_fields = None
                field_name = encode_field_name(meta.pysolaar_type, key)

                with value(
                    document_structure=this_keys_store_document_fields
                ) as values:
                    doc[field_name] = []
                    for child_doc in values:
                        c = child_doc.doc_to_splatted_child(field_name=field_name)
                        doc[field_name] += _splat_to_list(c)
                doc[field_name] = list(set(doc[field_name]))

            elif key in fields_as_child_docs and key in fields_as_json:

                if has_store_document_fields:
                    this_keys_store_document_fields = meta.store_document_fields.get(
                        key, None
                    )
                else:
                    this_keys_store_document_fields = None

                with value(
                    document_structure=this_keys_store_document_fields
                ) as values:

                    try:
                        child_docs = [
                            child_doc.doc_to_plain_json() for child_doc in values
                        ]
                        if not child_docs:
                            continue
                        encoded_doc = json.dumps(
                            child_docs,
                            default=BaseDocument._encode_date_or_datetime,
                        )
                        doc[encode_field_name(meta.pysolaar_type, key)] = encoded_doc
                    except TypeError:

                        doc[encode_field_name(meta.pysolaar_type, key)] = values

            elif key in fields_as_child_docs:
                # PySolaar.items() now returns context manager, so that the
                # values can be safely extracted without hitting infinite recursion loops

                if has_store_document_fields:
                    this_keys_store_document_fields = meta.store_document_fields.get(
                        key, None
                    )
                else:
                    this_keys_store_document_fields = None

                with value(
                    document_structure=this_keys_store_document_fields
                ) as values:

                    # If we don't have "_doc" and also have some values to put in it
                    # then create it
                    if "_doc" not in doc and values:
                        doc["_doc"] = []

                    for child_doc in values:
                        doc["_doc"].append(
                            child_doc.doc_to_nested_child(meta.pysolaar_type, key)
                        )

            elif key in fields_as_json:
                # print("field as json^^")

                doc[key] = json.dumps(
                    value, default=BaseDocument._encode_date_or_datetime
                )

            elif isinstance(value, (list, tuple, set)):
                # print("is list, tuple, set")

                doc[encode_field_name(meta.pysolaar_type, key)] = [
                    BaseDocument._encode_value_types(v) for v in value
                ]

            # If it's a dict, recursively call this method
            # As long as it's dicts or values all the way down,
            # we're fine. Lists of dicts need to be tackled separately
            # somehow (nested docs???) (or not!!)
            elif isinstance(value, dict):
                # print("is_dict", key, value)
                d = {f"{key}__{k}": v for k, v in value.items()}

                # To do sub-dicts, we need a radically different Meta class
                # (so cloned the old one)
                # Easiest to just stick on a 'is dictionary' flag so that
                # the field gets included when we call this func again.
                new_meta = copy.deepcopy(meta)
                new_meta.dict_embedding = True

                r = BaseDocument._encode_key_values(
                    d, new_meta, encode_field_name=lambda m, f: f
                )
                # Encoded the field name #AFTER# we process the data inside...
                r = {encode_field_name(meta.pysolaar_type, k): v for k, v in r.items()}
                doc = {**doc, **r}

            else:
                # print("else_cond^^")
                doc[
                    encode_field_name(meta.pysolaar_type, key)
                ] = BaseDocument._encode_value_types(value)
            # print(doc)
        return doc

    @staticmethod
    def _encode_value_types(value: Any, meta=None) -> str:
        if isinstance(value, dict):
            # The only time this code should be called is when a list is tackled
            # (above) and the list-comp passes each value to this function.
            # Dicts not in lists are tackled in _encode_value_keys
            raise PySolaarDocumentError(
                "It is not possible to store a list of dicts."
                " Consider using a nested document or creating multiple fields."
            )
        if isinstance(value, (datetime.datetime, datetime.date)):
            return BaseDocument._encode_date_or_datetime(value)
        return value

    @staticmethod
    def _encode_date_or_datetime(value) -> str:
        """Given a datetime.datetime or datetime.date field, convert it
        to Solr's required format (odd format!!)

        TODO: Maybe move this function into utils, as will be useful for
        decoding."""
        if isinstance(value, datetime.datetime):
            return value.isoformat() + "Z"  # Needs timezone
        if isinstance(value, datetime.date):
            return value.isoformat() + "T00:00:00Z"
        return value
