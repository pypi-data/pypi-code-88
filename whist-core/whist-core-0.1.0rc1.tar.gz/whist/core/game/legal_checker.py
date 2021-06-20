"""Checks the legality of a move."""
from whist.core.cards.card import Card
from whist.core.cards.hand import Hand


# pylint: disable=too-few-public-methods
class LegalChecker:
    """
    Static legal checker.
    """

    @staticmethod
    def check_legal(hand: Hand, lead: Card) -> bool:
        """
        Checks if move is legal.
        :param hand: of the current player
        :type hand: Hand
        :param lead: the first played card
        :type lead: Card
        :return: True if legal else false
        :rtype: bool
        """
        first_card_played = lead is not None
        return not (first_card_played and hand.contain_suit(lead.suit))
