from typing import Iterable, List, Type, Union

from .scopes import ScopeDomain, ScopeEnum, auto as auto_scopes


__all__ = (
    'Aggregate',
    'auto_aggregate',
    'AggregatesMeta',
    'BaseAggregates',
    'Aggregates',
)


AggregateValue = Union[ScopeDomain, ScopeEnum]


class Aggregate(set):
    """Set with 'name' attribute. Nothing more."""

    name: str

    def __init__(
        self,
        name: str,
        iterable: Iterable[AggregateValue] = ()
    ) -> None:
        super().__init__(iterable)
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<{self.name}: {super().__repr__()}>'


auto = auto_aggregate = Aggregate('auto')


class AggregatesMeta(type):
    AGGREGATE_ATTRIBUTE = '_Aggregate'
    VALUE_GENERATOR_ATTRIBUTE = '_generate_next_value_'

    def __new__(metacls, cls, bases, classdict):
        value_generator = metacls._resolve_cls_attribute(
            bases, classdict, metacls.VALUE_GENERATOR_ATTRIBUTE
        )
        names = []
        Class = metacls._resolve_cls_attribute(
            bases, classdict, metacls.AGGREGATE_ATTRIBUTE
        )

        if Class is None:
            raise TypeError(
                f'No attribute `{metacls.AGGREGATE_ATTRIBUTE}` defined '
                'in class or it\'s bases.'
            )

        for key, value in classdict.items():
            if value is auto or value is auto_scopes:
                assert value_generator is not None, (
                    f'Add `{metacls.VALUE_GENERATOR_ATTRIBUTE}` method to '
                    'a class `{cls}` to be able to use auto generation.'
                )

                value = classdict[key] = value_generator(cls=Class, key=key)

            if isinstance(value, Class):
                names.append(key)

        classdict['_item_names'] = names

        instance = super().__new__(
            metacls, cls, bases, classdict
        )

        return instance

    @classmethod
    def _resolve_cls_attribute(metacls, bases, classdict, attr: str):
        if attr in classdict:
            return classdict[attr]

        for chain in bases:
            for base in chain.__mro__:
                if hasattr(base, attr):
                    return getattr(base, attr)


class BaseAggregates(metaclass=AggregatesMeta):
    _Aggregate: Type[Aggregate] = Aggregate
    _item_names: List[str]


class Aggregates(BaseAggregates):
    """Special Enum-like class that can autogenerate aggregate attributes."""

    def _generate_next_value_(cls, key: str):
        return cls(key)
