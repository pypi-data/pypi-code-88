from __future__ import annotations

import datetime
from functools import wraps
from pysolaar.utils.exceptions import PySolaarConfigurationError
import re
from typing import Any, Dict, Union

from icecream import ic


from solrq import Q as SolrQ, Value as SolrqValue
import solrq


from pysolaar.utils.encoders_and_decoders import (
    encode_field_name,
    PySolaarException,
    ID_SEPARATOR,
    KEY_SEPARATOR,
    encode_id,
)
from pysolaar.utils.meta_utils import ChildDocument


class PySolaarQueryError(PySolaarException):
    pass


END_MODIFIED_FIELD_REGEX = re.compile(r"(.*[a-zA-Z0-9]+)__([a-zA-Z0-9]+)$")


class PatchedValue(SolrqValue):
    def __init__(self, raw, safe=False):
        """Initialize Value object and process it's raw value.
        If ``datetime`` or ``timedelta`` is passed as ``raw`` then immediately
        convert it to format that can be parsed by Solr.
        """
        if isinstance(raw, datetime.datetime) and not safe:
            # Note: solr speaks ISO, wrap it with quotes to avoid further
            # escaping
            self.raw = '"{dt}Z"'.format(
                dt=(
                    raw.strftime("%Y-%m-%dT%H:%M:%S.%f")
                    if raw.tzinfo
                    else raw.isoformat()
                )
            )
            # since we translated value we can safely mark it safe
            self.safe = True

        ################################################################
        ### Added this elif clause here to tackle datetime.date values,
        ### which are allowed in PySolaar. So modified whole function
        ### and patched this variant back in later

        elif isinstance(raw, datetime.date) and not safe:
            self.raw = f'"{str(raw) + """T00:00:00Z"""}"'
            self.safe = True
        ###
        ###
        ################################################################

        elif isinstance(raw, datetime.timedelta) and not safe:
            # Make representation compatibile with Solr Date Math Syntax
            # Note: at first look this can look weird since it can produce
            # strings with mixed singn for negative deltas e.g:
            #
            #     >>> Value(-timedelta(days=2, hours=2))
            #     <Value: NOW-3DAYS+79200SECONDS+0MILLISECONDS>
            #
            #  but this is a valid representation and Solr can handle it
            self.raw = (
                self.TIMEDELTA_FORMAT.format(
                    days=raw.days, secs=raw.seconds, mills=int(raw.microseconds / 1000)
                )
                if not raw == datetime.timedelta()
                else "NOW"
            )
            # since we translated value we can safely mark it safe
            self.safe = True
        else:
            self.raw = raw
            self.safe = safe


class Q(SolrQ):
    def compile(self, extra_parenthesis=True, class_name=None, nested=False):
        """Compile :class:`Q` object into query string.
        Args:
            extra_parenthesis (bool): add extra parenthesis to children query.
        Returns:
            str: compiled query string.
        Examples:
            >>> (Q(type="animal") & Q(name="cat")).compile()
            'type:animal AND name:cat'
            >>> (Q(type="animal") & Q(name="cat")).compile(True)
            '(type:animal AND name:cat)'
        """

        # Modification from solrq: take a class_name, and encode the field using it
        try:
            if self.field == "id":
                field = self.field
            elif class_name:
                field = encode_field_name(class_name, self.field)
            else:
                field = self.field

            # Check whether the field ends with a __gt, __gte, etc. or a
            # #dict subfield modifier
            # Regex.match returns two groups, the field name and the modifier
            end_modified_match = END_MODIFIED_FIELD_REGEX.match(field)
            if end_modified_match:
                field_name, modifier = end_modified_match.groups()
                field, query = self._encode_end_modifier_query(
                    field_name, modifier, self.query
                )
            elif field == "id":
                if nested:
                    query = f"*{self.query}"
                else:
                    query = encode_id(class_name, self.query)

            else:
                query = self.query
        except AttributeError:
            pass

        if not self._children:
            query_string = "{field}:{qs}".format(field=field, qs=query)
        else:
            query_string = self._operator(
                # Modified call to child.compile to pass class_name variable
                [
                    child.compile(extra_parenthesis=True, class_name=class_name)
                    for child in self._children
                ]
            )

            if extra_parenthesis:
                query_string = "({qs})".format(qs=query_string)

        return query_string

    @staticmethod
    def _encode_end_modifier_query(field_name, modifier, query_value):
        """Encodes Django-style modifiers into Solr range queries,
        or just returns a field__subfield=value type query
        """
        if modifier == "lt":
            return field_name, f"[* TO {query_value}}}"
        if modifier == "lte":
            return field_name, f"[* TO {query_value}]"
        if modifier == "gt":
            return field_name, f"{{{query_value} TO *]"
        if modifier == "gte":
            return field_name, f"[{query_value} TO *]"
        return f"{field_name}__{modifier}", query_value


##############################################################################
### Monkey-patch solrq's Value and Q classes with the one adjusted above

solrq.Value = PatchedValue
solrq.Q = Q

### Patching it like this ought to be sufficient, as we're only accessing
### Value via our own Q object, rather than loading the class directly in
### way that might skip the patching.
##############################################################################


class PySolaarQuerySetBase:
    _results = None

    def __init_subclass__(cls) -> None:
        # Unpack the fields_and_types variables from Meta into
        # default return fields

        # n.b. this has been moved from __init__ as it only
        # needs to happen on the creation of the QuerySet subclass,
        # not every time there's a new queryset initialised...
        try:
            cls.default_return_fields = [
                encode_field_name(cls.pysolaar_type, key)
                for key, v in cls.Meta.fields_and_types.items()
                if key != "id" and type(v) is not ChildDocument
            ]
        except AttributeError:
            cls.default_return_fields = []

        # and we need all the child fields as well...
        try:
            for parent_key, parent_fields in cls.Meta.child_fields_and_types.items():
                for field in parent_fields:
                    if field != "id":
                        child_field = encode_field_name(
                            encode_field_name(cls.pysolaar_type, parent_key), field
                        )
                        cls.default_return_fields.append(child_field)
        except AttributeError:
            pass

    def __init__(self, q_object=None, child_qs={}, **kwargs):
        """ Create a queryset """

        """
        Here, we could allow passing queries directly to __init__, but it
        seems a lot more effort to just handle same logic cases... much easier
        I guess to have a redundant in-between class... so a Pysolaar object
        would initialise its queryset class with a call like:

        Thing.filter(some_shit="whatever")

        and then the PySolaar class can implement .filter with the same signature
        as the queryset, just returning a queryset lazily via...

        return ThingQueryset().filter()...

        ^^ N.B. This is exactly how we do it, and PySolaar class has 
        _proxy_to_new_queryset method that creates methods dynamically

        """

        self.q_object = q_object
        self.child_qs = child_qs
        self.kwargs = kwargs
        self._results = None

    def _set_results_class(self):
        try:
            self._solr.results_cls = self._results_class
        except AttributeError:
            raise PySolaarConfigurationError(
                "No pysolr configuration found. Be sure to call `PySolaar.configure_pysolr`"
            )

    def filter(self, input_q: Union[None, Q] = None, **kwargs) -> PySolaarQuerySetBase:
        """To filter, either pass in a Q object or kwargs.
        Kwargs will automatically be splatted to a q-object anyway"""

        if input_q and kwargs:
            raise PySolaarQueryError(
                "The `filter` method takes a Q object or key-word arguments, not both."
            )

        elif not self.q_object and input_q:  # set to None by __init__
            q_object = input_q

        elif self.q_object and input_q:
            q_object = self.q_object & input_q

        elif kwargs:
            q_object = self.q_object
            for key, value in kwargs.items():
                if q_object:
                    q_object = q_object & Q(**{key: value})
                else:
                    q_object = Q(**{key: value})

        return self.__class__(q_object=q_object, child_qs=self.child_qs)

    def filter_by_distinct_child(self, q=None, field_name=None, **kwargs):
        """To filter, either pass in a Q object or kwargs.
        Kwargs will automatically be splatted to a q-object anyway"""

        # TODO: FOR SOME REASON, id field is being missed out of query!

        q_object = None
        if not field_name:
            raise PySolaarQueryError(
                "You `filter_by_distinct_child` method must specify the "
                "parent field with the `field_name` key-word argument."
            )
        elif q and kwargs:
            raise PySolaarQueryError(
                "The `filter_by_distinct_child` method takes a Q object "
                "or key-word arguments, not both."
            )
        elif q:
            q_object = q

        elif kwargs:
            for key, value in kwargs.items():
                if q_object:
                    q_object = q_object & Q(**{key: value})
                else:
                    q_object = Q(**{key: value})

        compiled_q = q_object.compile(
            extra_parenthesis=True,
            class_name=encode_field_name(
                self.pysolaar_type,
                field_name,
            ),
            nested=True,
        )

        child_qs = [*self.child_qs, (field_name, compiled_q)]

        return self.__class__(
            q_object=self.q_object,
            child_qs=child_qs,
            **self.kwargs,
        )


    def _build_sort_statement(self, classname, order_field, order):

        order_field = (
            encode_field_name(classname, order_field) if order_field != "id" else order_field
        )
        return f"{order_field} {order}"

    def order_by(self, *args, accumulate=False):
        """ Orders results by field name. Takes as many arguments are required, as 
        strings containing field name with optional 'asc' or 'desc' —— e.g. "id asc".
        
        `accumulate=True` to keep previously set order, adding new order as the first
        ordering option
        """
    
        orderings = self.kwargs.pop("sort", "")
  

        if len(args) == 0:
            raise PySolaarQueryError("order_by requires an argument in the form 'field_name asc'")

        orderings_list = []
        for ordering_string in args:
            try:
                # If we have a field and order, split
                order_field, order = ordering_string.split(" ")
            except ValueError:
                # Otherwise, it's just a field
                order_field = ordering_string
                # and set a default
                order = "asc"
            orderings_list.append(self._build_sort_statement(self.pysolaar_type, order_field, order))

        if orderings and accumulate:
            orderings_list =  orderings_list + [orderings]
        
        orderings = ",".join(orderings_list)
        
            

        
        return self.__class__(q_object=self.q_object, child_qs=self.child_qs, sort=orderings, **self.kwargs)



    def paginate(self, start=None, page_number=None, page_size=10):
        """Return a paginated QuerySet.

        Provide either a page_number and page_size,
        or a start and page size."""

        ## PROBLEM!!!!
        ## Can't IF on a zero!!

        kwargs = {**self.kwargs}
        try:
            kwargs.pop("start")
            kwargs.pop("rows")
        except KeyError:
            pass

        if type(page_number) is int:
            calculated_start = page_number * page_size
        else:
            calculated_start = start

        if type(calculated_start) is not int:
            raise PySolaarQueryError(
                "To paginate, a start point or a page number must be provided."
            )

        return self.__class__(
            q_object=self.q_object,
            child_qs=self.child_qs,
            start=calculated_start,
            rows=page_size,
            **self.kwargs,
        )

    def _prepare_qs(self):
        if self.q_object:
            parent_query = self.q_object.compile(class_name=self.pysolaar_type)
            pq = f" +({parent_query})"
            query = f"pysolaar_type:{self.pysolaar_type} AND {parent_query}"
        else:
            query = f"pysolaar_type:{self.pysolaar_type}"

        return query

    def _child_qs_to_fqs(self):
        prepared_child_qs = []
        for field_name, compiled_q in self.child_qs:
            q = f'{{!parent which="*:* -_nest_path_:* +pysolaar_type:{self.pysolaar_type}"}}(+_nest_path_:\\/_doc +pysolaar_type_nested:*{field_name} +pysolaar_type_nested:{self.pysolaar_type}* +({compiled_q}))'
            prepared_child_qs.append(q)
        return prepared_child_qs

    def _get_results(self, rows=100000, start=0, *args, **kwargs):
        # print(rows, start, args, kwargs)
        # So, we have a *single* PySolr class, which means we need to change the
        # results class just before each query... which is fine?
        rows = self.kwargs.get("rows", rows)
        start = self.kwargs.get("start", start)
        sort = self.kwargs.get("sort", "")

        return_fields = self.default_return_fields
        fls = ",".join(
            ["id", "pysolaar_type"]
            + return_fields
            + ["_doc", "pysolaar_type_nested", "[child limit=1000000]"]
        )
        # TODO: add child filter on child field types to make sure we
        # only fetch the required ones, instead of filtering out afterwards!!!
        self._set_results_class()
        query = self._prepare_qs()
        fqs = self._child_qs_to_fqs()
        print("Solr Query:", query)
        print("Solr Fqs", fqs)

        results = self._solr.search(
            query,
            fq=fqs,
            fl=fls,
            rows=rows,
            start=start,
            sort=sort,
        )

        return results

    def _with_results(method: Callable) -> Callable:  # type: ignore
        """Decorates a PySolaarQuerySetBase method to get results before
        calling the method (*not* the same as @_proxy_to_results, which points to the
        relevant method on the results class itself)"""

        @wraps(method)
        def inner(self, *args, **kwargs):
            if not self._results:
                self._results = self._get_results()
            return method(self, *args, **kwargs)

        return inner

    def _proxy_to_results(*args, **kwargs):  # type: ignore
        """Proxies usual functions by passing in a result object, which it looks
        up in advance.

        Pass kwargs to pass to `_get_results` method. Also pass `incomplete=True`
        if the result is partial (e.g. getting first item only) and should not
        therefore be saved."""

        def _wrapper(func):
            @wraps(func)
            def inner(self, *inner_args, **inner_kwargs):
                if not self._results:

                    try:
                        incomplete = kwargs.pop("incomplete")
                    except KeyError:
                        incomplete = False
                    results = self._get_results(*args[1:], **kwargs)
                    if not incomplete:
                        self._results = results
                    return func(results, *inner_args, **inner_kwargs)
                else:
                    return func(self._results, *inner_args, **inner_kwargs)

            return inner

        if len(args) == 1 and callable(args[0]):
            return _wrapper(args[0])
        else:
            return _wrapper

    __iter__ = _proxy_to_results(iter)

    @_proxy_to_results
    def __len__(results):
        return len(results)

    @_proxy_to_results(rows=0, incomplete=True)
    def count(results):
        return results.count()

    @_proxy_to_results(rows=1, incomplete=True)
    def first(results):
        try:
            return list(results)[0]
        except IndexError:
            return None

    @_proxy_to_results
    def last(results):
        try:
            return results[-1]
        except IndexError:
            return None

    @_proxy_to_results
    def all(results):
        return results

    @_with_results
    def results_set(self):
        return self._results
