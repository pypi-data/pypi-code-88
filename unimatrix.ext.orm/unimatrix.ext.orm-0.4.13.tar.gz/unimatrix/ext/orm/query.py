"""Declares :class:`NamedQuery`."""
import collections

import marshmallow.exceptions
from marshmallow.fields import *
from marshmallow import Schema
from sqlalchemy import exists
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import selectable
from sqlalchemy.sql.elements import BinaryExpression
from unimatrix.ext.model.exc import ValidationError


FORBIDDEN_ATTRS = ['build', 'execute', 'schema_context']


class NamedQueryParameter:

    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls=None):
        return obj._params[self.name]


class NamedQueryMeta(type):

    def __new__(cls, name, bases, attrs):
        super_new = super().__new__
        if name == 'NamedQuery':
            return super_new(cls, name, bases, attrs)

        # Construct a marshmallow.Schema class based on the fields found
        # on the NamedQuery subclass.
        fields = {}
        for attname in list(dict.keys(attrs)):
            if not isinstance(attrs[attname], Field):
                continue
            if attname in FORBIDDEN_ATTRS:
                raise ValueError("Field name '%s' is not allowed" % attname)
            fields[attname] = attrs.pop(attname)
            attrs[attname] = NamedQueryParameter(attname)

        attrs['schema_class'] = type("%sSchema" % name, (Schema,), fields)

        return super_new(cls, name, bases, attrs)


class NamedQuery(metaclass=NamedQueryMeta):
    """Represents a named database query."""
    columns = []
    declarative = False
    model = None
    predicate = []
    result_class = None

    supported_selectables = (
        selectable.Exists,
        selectable.Selectable,
    )

    supported_predicates = tuple([BinaryExpression])

    def __init__(self, *args, **kwargs):
        schema = self.schema_class()
        try:
            self._params = schema.load(kwargs)
        except marshmallow.exceptions.ValidationError as e:
            raise ValidationError(spec=e.normalized_messages())
        self._query = None

    def build(self):
        """Builds the query."""
        query = self.get_base_query()
        if self.predicate:
            if isinstance(self.predicate, collections.abc.Sequence):
                for p in self.predicate:
                    if callable(p):
                        p = p(self, query)
                    if isinstance(p, selectable.Select):
                        query = p
                    elif isinstance(p, self.supported_predicates):
                        query = query.where(p)
                    else:
                        raise NotImplementedError(
                            f"Unsupported predicate: {type(p).__name__}")
            elif isinstance(self.predicate, eq):
                query = query.where(self.predicate(self, query))
            else:
                raise NotImplementedError

        if query is None:
            raise NotImplementedError
        return query

    def get_base_query(self):
        relation = self.model or self.columns
        if relation:
            return self.query_factory(relation)
        raise NotImplementedError

    def get_result_class(self):
        return Result

    def process_result(self, result):
        """Hook to process the query results."""
        return result

    def query_factory(self, relation):
        return select(relation)

    def _build(self):
        self._query = self.build()
        return self._query

    def _process_result(self, result):
        return self.process_result(result)

    async def run(self, session):
        """Run the query."""
        cls = self.get_result_class()
        return cls(self, await self.execute(session))

    async def execute(self, session):
        """Executes the query and returns the result."""
        return self._process_result(await session.execute(self._build()))


class BaseDeclarativeQuery(NamedQuery):
    """A :class:`~unimatrix.ext.orm.query.Query` implementation that
    process the result as an SQLAlchemy declarative model.
    """

    def process_result(self, result):
        return result.scalars()


class DeclarativeCollectionQuery(BaseDeclarativeQuery):
    """Like :class:`BaseDeclarativeQuery`, but expects a collection."""

    def process_result(self, result):
        return result.scalars()


class DeclarativeQuery(BaseDeclarativeQuery):
    """Like :class:`BaseDeclarativeQuery`, but expects a single entity
    to be returned.
    """

    #: Indicates if the result may be ``None``.
    allow_none = False

    def process_result(self, result):
        result = super().process_result(result)
        return result.one() if not self.allow_none else result.first()


class Get(NamedQuery):
    """A :class:`Query` implementation that results a single row."""
    allow_none = False

    def process_result(self, result):
        result = result.fetchone()
        if result is None and not self.allow_none:
            raise NoResultFound
        return result


class Set(NamedQuery):
    """A :class:`NamedQuery` implementation that returns a result set
    constrained by the query predicate.
    """
    pass


class Exists(NamedQuery):

    def get_result_class(self):
        return lambda self, q: bool(q)

    def query_factory(self, relation):
        return exists(1)

    def _build(self, *args, **kwargs):
        q = super()._build(*args, **kwargs)
        assert isinstance(q, selectable.Exists) #nosec
        return select(q)

    def process_result(self, result):
        return result.scalar()


class Result:
    """The result of an executed :class:`Query`."""
    not_provided = object()

    def __init__(self, query, result):
        self.__query = query
        self.__result = result

    def __getattr__(self, attname):
        return getattr(self.__result, attname)

    def __iter__(self):
        return iter(self.__result)


Query = NamedQuery


class eq:

    def __init__(self, column, parameter):
        self.column = column
        self.parameter = parameter

    def __call__(self, params, query):
        return self.column == getattr(params, self.parameter)
