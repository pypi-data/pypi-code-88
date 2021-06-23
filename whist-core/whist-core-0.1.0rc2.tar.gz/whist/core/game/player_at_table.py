"""Player instance during the game phase."""
from whist.core.cards.hand import Hand
from whist.core.user.player import Player


class PlayerAtTable:
    """
    Wraps the current hand and player instance.
    """

    def __init__(self, player: Player, hand: Hand):
        self._player = player
        self._hand = hand

    def __eq__(self, other):
        if not isinstance(other, PlayerAtTable):
            return False
        return self._player == other._player

    def __repr__(self):
        return f'PlayerAtTable: {self._player}'

    @property
    def player(self):
        """
        Getter player instance.
        :return: player instance
        :rtype: Player
        """

        return self._player

    @property
    def hand(self) -> Hand:
        """
        Hand of the player
        :return: hand of the player
        :rtype: Hand
        """
        return self._hand
