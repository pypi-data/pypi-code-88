"""Hand held by player."""
from typing import final, Iterable, Any, Iterator

from whist.core.cards.card import Suit, Card


@final
class Hand:
    """
    Hand of player during a game.
    """

    def __init__(self, *args: (tuple[Iterable[Card]], tuple[Card, ...])) -> None:
        """
        Constructor

        :param args: multiple cards or one card iterable
        """
        if len(args) == 1 and not isinstance(args[0], Card):
            self.__cards = {*args[0]}
        else:
            self.__cards = {*args}

    def __contains__(self, card: Card) -> bool:
        return card in self.__cards

    def __len__(self):
        return len(self.__cards)

    def __iter__(self) -> Iterator[Card]:
        return iter(self.__cards)

    def __str__(self) -> str:
        return str(self.__cards)

    def __repr__(self) -> str:
        return f'Hand(cards={self.__cards!r})'

    def __eq__(self, other: Any) -> bool:
        if self.__class__ is other.__class__:
            # pylint: disable=protected-access
            return self.__cards == other.__cards
        return NotImplemented

    def add(self, card: Card) -> None:
        """
        Add a card to this deck.

        :param card: card to add
        """
        if card in self.__cards:
            raise KeyError(f'{card} already in deck')
        self.__cards.add(card)

    def remove(self, card: Card) -> None:
        """
        Remove a card from this deck.

        :param card: card to remove
        """
        self.__cards.remove(card)

    @staticmethod
    def empty():
        """
        Creates a empty hand.
        :return: empty hand
        :rtype: Hand
        """
        return Hand()

    def contain_suit(self, suit: Suit) -> bool:
        """
        Checks if a card of a suit is still in the hand.
        :param suit: which should be checked
        :type suit: Suit
        :return: True if contains this suit else False
        :rtype: bool
        """
        if len(self.__cards) == 0:
            return False
        return any((card for card in self.__cards if card.suit == suit))
