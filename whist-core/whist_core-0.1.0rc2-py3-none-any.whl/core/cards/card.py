"""Card related classes"""

from dataclasses import dataclass
from enum import Enum, unique
from typing import final, Any


class _OrderedEnum(Enum):
    def __new__(cls, *args) -> '_OrderedEnum':
        if len(args) == 1:
            value = args[0]
        else:
            value = args

        obj = object.__new__(cls)
        obj._value_ = value
        # pylint: disable=protected-access
        obj.__ordinal = len(cls.__members__)
        return obj

    @classmethod
    def by_ordinal(cls, ordinal: int) -> '_OrderedEnum':
        """
        Get enum constant by ordinal.

        :param ordinal: ordinal
        :return: enum constant
        """
        return list(cls.__members__.values())[ordinal]

    @property
    def ordinal(self) -> int:
        """
        Get the ordinal.

        :return: ordinal
        """
        return self.__ordinal

    def __ge__(self, other: Any) -> bool:
        if self.__class__ is other.__class__:
            return self.ordinal >= other.ordinal
        return NotImplemented

    def __gt__(self, other: Any) -> bool:
        if self.__class__ is other.__class__:
            return self.ordinal > other.ordinal
        return NotImplemented

    def __le__(self, other: Any) -> bool:
        if self.__class__ is other.__class__:
            return self.ordinal <= other.ordinal
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if self.__class__ is other.__class__:
            return self.ordinal < other.ordinal
        return NotImplemented


@unique
@final
class Suit(_OrderedEnum):
    """Suits in a playing card deck"""

    CLUBS = ('♣', 'clubs')
    DIAMONDS = ('♦', 'diamonds')
    HEARTS = ('♥', 'hearts')
    SPADES = ('♠', 'spades')

    @classmethod
    def by_label(cls, label: str, search_symbols: bool = False) -> 'Suit':
        """
        Get suit by label.

        :param label: label
        :param search_symbols: True if the suit symbols should be searched as well
        :return: suit
        """
        for _, value in cls.__members__.items():
            if label == value.label:
                return value
            if search_symbols and label == value.symbol:
                return value
        raise KeyError

    @property
    def symbol(self) -> str:
        """
        Get the suit symbol.

        :return: suit symbol
        """
        # pylint: disable=unsubscriptable-object
        return self.value[0]

    @property
    def label(self) -> str:
        """
        Get the suit label.

        :return: suit label
        """
        # pylint: disable=unsubscriptable-object
        return self.value[1]

    def __str__(self) -> str:
        return self.label


@unique
@final
class Rank(_OrderedEnum):
    """Ranks in a playing card deck"""

    NUM_2 = '2'
    NUM_3 = '3'
    NUM_4 = '4'
    NUM_5 = '5'
    NUM_6 = '6'
    NUM_7 = '7'
    NUM_8 = '8'
    NUM_9 = '9'
    NUM_10 = '10'
    J = ('J', 'jack')
    Q = ('Q', 'queen')
    K = ('K', 'king')
    A = ('A', 'ace')

    @classmethod
    def by_label(cls, label: str, search_short_labels: bool = False) -> 'Rank':
        """
        Get rank by label.

        :param label: rank
        :param search_short_labels: True if the rank short labels should be searched as well
        :return: label
        """
        for _, value in cls.__members__.items():
            if label == value.label:
                return value
            if search_short_labels and label == value.short_label:
                return value
        raise KeyError

    @property
    def short_label(self) -> str:
        """
        Get the short version of the rank label.

        :return: short version of rank label
        """
        # pylint: disable=unsubscriptable-object
        return self.value if isinstance(self.value, str) else self.value[0]

    @property
    def label(self) -> str:
        """
        Get the rank label.

        :return: rank label
        """
        # pylint: disable=unsubscriptable-object
        return self.value if isinstance(self.value, str) else self.value[1]

    def __str__(self) -> str:
        return self.label


@final
@dataclass(frozen=True)
class Card:
    """A playing card"""
    suit: Suit
    rank: Rank

    @property
    def short_name(self) -> str:
        """
        Get the short name of this card.

        :return: short name
        """
        return f'{self.suit.symbol}{self.rank.short_label}'

    @property
    def name(self) -> str:
        """
        Get the name of this card.

        :return: name
        """
        return f'{self.rank} of {self.suit}'

    def __str__(self) -> str:
        return self.name
