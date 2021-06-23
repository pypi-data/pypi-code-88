import re
from typing import Dict

from pysolaar.utils.encoders_and_decoders import decode_field_name, decode_id
from pysolaar.utils.meta_utils import (
    AsDict,
    BaseMeta,
    ChildDocument,
    Transform,
    is_transform,
    _fields_from_meta_return_document_fields,
)


{
    "responseHeader": {
        "status": 0,
        "QTime": 0,
        "params": {"q": "pysolaar_type:Thing", "fl": "*,[child]", "wt": "json"},
    },
    "response": {
        "numFound": 1,
        "start": 0,
        "numFoundExact": True,
        "docs": [
            {
                "id": "Thing##########1",
                "pysolaar_type": ["Thing"],
                "_version_": 1694931063139205120,
            }
        ],
    },
}

IS_DICT_FIELD_REGEX = re.compile(r"[^_]__[^_]")


def _is_dict_field(key):
    """Checks whether a field is part of a flattened
    dictionary by checking for double underscores (flanked on
    either side by non-underscores!) in the name"""

    if IS_DICT_FIELD_REGEX.search(key):
        return True
    return False


class ResultDocBase(dict):
    pass


class PySolaarResultsBase:
    __slots__ = ("_response", "_input_docs", "_output_docs")

    def __init_subclass__(cls) -> None:
        # Create a result wrapper class
        cls.ResultWrapper = type(
            f"{cls.Meta.pysolaar_type}ReturnDocument",
            (ResultDocBase,),
            {"__slots__": tuple(cls.Meta.fields_and_types.keys())},
        )

    class Meta:
        pass

    def __init__(self, resp) -> None:
        self._response = resp["response"]
        # print(self._response)
        self._input_docs = self._response["docs"]
        # No need to set up the output until required
        self._output_docs = None

    def __len__(self):
        return len(self._input_docs)

    def __iter__(self):
        if not self._output_docs:
            self._convert_docs_for_output()
        yield from self._output_docs

    def count(self):
        return self._response["numFound"]

    def _convert_docs_for_output(self):
        return_docs = []

        for doc in self._input_docs:
            new_doc = _response_doc_to_return_values(
                doc,
                meta=self.Meta,
                transforms=self.Meta.transforms,
                fields_and_types=self.Meta.fields_and_types,
                child_fields_and_types=self.Meta.child_fields_and_types,
                child_transforms=self.Meta.child_transforms,
            )

            return_docs.append(self.ResultWrapper(new_doc))
        self._output_docs = return_docs
        return return_docs


def _response_doc_to_return_values(
    doc,
    meta=BaseMeta,
    fields_and_types={},
    transforms={},
    child_fields_and_types={},
    child_transforms={},
):
    return_doc: Dict = {}
    # print("fields_and_types", fields_and_types)
    for key, value in doc.items():

        # If key is not something we want -- also add to this possibly?
        # -- just skip over it
        if key in {"pysolaar_type", "_version_", "pysolaar_type_nested"}:
            continue

        # If it's an id, decode and then leave in case there are
        # any transformations on key/value
        if key == "id":
            value = decode_id(value)
        # Otherwise, decode hte fie
        else:
            key = decode_field_name(key)

        # Now that we've decoded the field names, check whether
        # a fields_and_types list has been provided, and if so,
        # whether the field name in question is in this dict
        if fields_and_types and key not in fields_and_types and key != "_doc":
            continue

        # Apply transforms
        if transforms is not None and key in transforms:
            key, value = transforms[key].transform_function(key, value)

        if key == "_doc":
            # print(value)
            return_doc = _unpack_child_docs(
                value,
                return_doc,
                child_fields_and_types,
                child_transforms,
                fields_and_types,
            )
        elif _is_dict_field(key):
            return_doc = _unpack_dict_field(key, value, return_doc)
        else:
            return_doc[key] = value

    return return_doc


def _unpack_child_docs(
    value, return_doc, child_fields_and_types, child_transforms, parent_fields_and_types
):
    """Unpacks "_doc" key, creating a list in return_doc for each parent
    field name, transforming the child doc as required, then appending to the
    correct list.


    The parent_fields_and_types list is passed in too, as we need to decided
    whether to include particular child types or not
    """

    # Optimisation: Check there's actually some transformations to do before we call
    # _apply_transforms_to_child_docs
    any_transforms = any(
        getattr(pfat, "transform_function", None)
        for k, pfat in parent_fields_and_types.items()
    )

    # If _doc is just a single item, i.e. a dict, return a list with a single
    # item in it ——
    ### CHANGED: used to return a dict, but behaviour is more consistent this
    # if we always return a list
    if type(value) is dict:
        child_doc = value
        parent_field_name = decode_id(child_doc["pysolaar_type_nested"][0])
        if parent_field_name not in parent_fields_and_types:
            return return_doc
        if parent_field_name not in return_doc:

            return_doc[parent_field_name] = [
                _response_doc_to_return_values(
                    child_doc,
                    fields_and_types=child_fields_and_types.get(parent_field_name),
                    transforms=child_transforms.get(parent_field_name),
                )
            ]
        if not any_transforms:
            return return_doc
        return _apply_transforms_to_child_docs(return_doc, parent_fields_and_types)

    # Otherwise, if _doc is *list* of child docs, iterate and tackle as appropriate
    for child_doc in value:

        parent_field_name = decode_id(child_doc["pysolaar_type_nested"][0])
        if parent_field_name not in parent_fields_and_types:
            continue

        if parent_field_name not in return_doc:
            return_doc[parent_field_name] = []
        return_doc[parent_field_name].append(
            _response_doc_to_return_values(
                child_doc,
                fields_and_types=child_fields_and_types.get(parent_field_name),
                transforms=child_transforms.get(parent_field_name),
            )
        )
    if not any_transforms:
        return return_doc
    return _apply_transforms_to_child_docs(return_doc, parent_fields_and_types)


def _apply_transforms_to_child_docs(return_doc, parent_fields_and_types):
    """If any of the parent_fields_and_types is a ChildDocument with a
    _transform_function method, iterate over all the fields in the return doc
    and apply those transforms; otherwise, just add back in that field."""

    new_return_doc = {}

    for k, v in return_doc.items():
        if k in parent_fields_and_types and getattr(
            parent_fields_and_types[k], "transform_function", None
        ):
            new_key, new_value = parent_fields_and_types[k].transform_function(k, v)
            new_return_doc[new_key] = new_value
        else:
            new_return_doc[k] = v
    return new_return_doc


def _unpack_dict_field(key, value, return_doc):
    """Builds required dicts to handle 'flattened' dicts
    in the form `field__something__somethingelse` by building
    out the dicts where necessary and sticking the value at the
    end point"""

    # Make a list of dict names by splitting on separator
    nested_dict_names = key.split("__")

    # Set the original dict as the starting point
    curr_dict_path: Dict = return_doc

    # For each item in the list except the last one (which is the
    # field name), create a dict if it doesn't exist, and
    # set the dict currently being operated on (curr_dict_path)
    # to this dict
    for i in nested_dict_names[:-1]:
        if i not in curr_dict_path:
            curr_dict_path[i] = {}
        curr_dict_path = curr_dict_path[i]
    curr_dict_path[nested_dict_names[-1]] = value
    return return_doc