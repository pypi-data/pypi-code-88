"""Collection of cards"""
from typing import Optional

from whist.core.cards.card import Card, Suit


class Stack:
    """An ordered collection of cards"""

    def __init__(self):
        self.__cards: list[Card] = []

    def __len__(self):
        return len(self.__cards)

    @property
    def lead(self) -> Optional[Card]:
        """
        Returns the first card played.
        :return: The first card played if it exists. Else none.
        :rtype: Card or None
        """
        if len(self.__cards) == 0:
            return None
        return self.__cards[0]

    def add(self, card: Card) -> None:
        """
        Put card on top of stack
        :param card: a Card placed on top of the stack
        """
        if card in self.__cards:
            raise KeyError(f'{card} already in deck')
        self.__cards.append(card)

    def winner_card(self, trump: Suit) -> Card:
        """
        Returns the highest trump card or the highest card of the suit played first.
        :param trump: suit of trump
        :type trump: Suit
        :return: the winning card
        :rtype: Card
        """
        winner_suit_cards: list[Card] = self._card_of_suit(trump)
        if len(winner_suit_cards) == 0:
            winner_suit_cards: list[Card] = self._card_of_suit(self.__cards[0].suit)
        return max(winner_suit_cards, key=lambda x: x.rank)

    def get_turn(self, card: Card) -> int:
        """
        Gets the turn of a card played.
        :param card: for which the turn number shall be found
        :type card: Card
        :return: the index of the card in the stack. 0 is the first the card played
        :rtype: int
        """
        if card not in self.__cards:
            raise KeyError(f'{card} is not in stack.')
        return self.__cards.index(card)

    def _card_of_suit(self, trump):
        return [card for card in self.__cards if card.suit == trump]
