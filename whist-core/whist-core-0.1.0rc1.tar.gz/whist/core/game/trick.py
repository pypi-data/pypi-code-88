"""Trick implementation"""
from whist.core.cards.card import Card, Suit
from whist.core.cards.stack import Stack
from whist.core.game.errors import NotPlayersTurnError, TrickDoneError
from whist.core.game.legal_checker import LegalChecker
from whist.core.game.player_at_table import PlayerAtTable
from whist.core.game.warnings import TrickNotDoneWarning, ServSuitFirstWarning


class Trick:
    """
    One round of where every player plays one card.
    """

    def __init__(self, play_order: list[PlayerAtTable], trump: Suit):
        self._play_order: list[PlayerAtTable] = play_order
        self._stack: Stack = Stack()
        self._trump = trump

    @property
    def done(self) -> bool:
        """
        Is the trick done.
        :return: True if trick is done else false.
        :rtype: bool
        """
        return len(self._stack) == len(self._play_order)

    @property
    def winner(self) -> PlayerAtTable:
        """
        Player how won the trick.
        :return: Player instance of the winner if the trick is done.
        Else raises TrickNotDoneWarning
        :rtype: Player
        """
        if not self.done:
            raise TrickNotDoneWarning()
        winner_card = self._stack.winner_card(self._trump)
        return self._play_order[self._stack.get_turn(winner_card)]

    def play_card(self, player: PlayerAtTable, card: Card) -> None:
        """
        One player plays one card. Which is put on top of the stack.
        :param player: Player who wants to play a card.
        :type player: Player
        :param card: Card which the player wants to play.
        :type card: Card
        :return: None if successful, else raises TrickDoneError if every player already played a
        card.
        Or NotPlayersTurnError if a player attempts to play card although it is not they turn.
        :rtype: None
        """
        turn = len(self._stack)
        if turn == len(self._play_order):
            raise TrickDoneError()
        if player != self._play_order[turn]:
            raise NotPlayersTurnError(player.player, self._play_order[turn].player)
        if not LegalChecker.check_legal(player.hand, self._stack.lead):
            raise ServSuitFirstWarning()

        self._stack.add(card)
