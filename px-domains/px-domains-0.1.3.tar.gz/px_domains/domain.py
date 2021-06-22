from typing import Optional, List, Union


__all__ = 'DOMAIN_DELIMITER', 'Domain',

DOMAIN_DELIMITER = '::'
DomainDefinition = List[str]


def sublist(lst1, lst2):
    len1 = len(lst1)
    diff = len(lst2) - len1

    if diff < 0:
        return -1

    for i in range(diff + 1):
        if lst1[0] == lst2[i] and lst1 == lst2[i:i + len1]:
            return i

    return -1


class Domain(str):
    """Basement for domain keys description.

    Based on `str` class implementation with additional methods for
    better subdomains chaining.

    Additionally re-implements `in` magic mehtod.
    """

    _delimiter: str = DOMAIN_DELIMITER
    _definition: DomainDefinition = []
    _basement: DomainDefinition = []

    def __new__(
        cls, name: str = '',
        basement: Optional[DomainDefinition] = None,
        delimiter: Optional[str] = None
    ):
        delimiter = str(delimiter or cls._delimiter)
        basement = list(basement or [])
        definition = basement + name.split(delimiter)
        basement = definition[:-1]

        self = super().__new__(cls, delimiter.join(definition))
        self._delimiter = delimiter
        self._definition = definition
        self._basement = basement

        return self

    def __contains__(self, basement: 'Domain') -> bool:
        return sublist(basement._definition, self._definition) != -1

    def __or__(self, other: Union['Domain', str]) -> 'Domain':
        if isinstance(other, Domain):
            return self.combine(other)
        elif isinstance(other, str):
            return self.nest(other)
        else:
            raise TypeError(
                'unsupported operand type(s) for |: '
                f'"{type(self)}" and "{type(other)}"'
            )

    def nest(self, name: str) -> 'Domain':
        """Creates subdomain based on the current one.

        Args:
            name (str): Subdomain name.

        Returns:
            Domain: New chained domain.
        """
        return self.__class__(
            name, basement=self._definition, delimiter=self._delimiter
        )

    def combine(self, domain: 'Domain') -> 'Domain':
        return self.__class__.from_definition(
            self._definition + domain._definition, delimiter=self._delimiter
        )

    def get_path(self):
        path = []

        for i in range(len(self._definition)):
            path.append(self.__class__.from_definition(
                self._definition[:i + 1], delimiter=self._delimiter
            ))

        return path

    def get_basement(self) -> Optional['Domain']:
        """Returns higher tier domain(base).

        Returns:
            Optional[Domain]: Domain or None if domain is the 1st level domain.
        """
        if not len(self._basement):
            return None

        return self.__class__.from_definition(
            self._basement, delimiter=self._delimiter
        )

    @classmethod
    def parse(
        cls,
        value: str = '',
        delimiter: Optional[str] = None
    ) -> 'Domain':
        """Parses formatted string and creates new domain definition.

        Returns:
            Domain: New domain definition.
        """
        delimiter = delimiter or cls._delimiter
        definition = value.split(delimiter)

        return cls.from_definition(definition, delimiter=delimiter)

    @classmethod
    def from_definition(cls, definition, **kwargs):
        return cls(
            definition[-1], basement=definition[:-1], **kwargs
        )

    def __repr__(self):
        return f'<{self.__class__.__name__} domain: {str(self)}>'
