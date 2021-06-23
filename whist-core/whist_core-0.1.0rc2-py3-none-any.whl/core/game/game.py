"""One Game of whist"""
from typing import Optional

from whist.core.game.hand import Hand
from whist.core.game.play_order import PlayOrder
from whist.core.scoring.score_card import ScoreCard
from whist.core.scoring.team import Team


class Game:
    """
    One Game of whist.
    """

    def __init__(self, teams: list[Team]):
        super().__init__()
        self.teams: list[Team] = teams
        self.win_score: int = 3
        self.score_card: ScoreCard = ScoreCard()
        self._current_hand: Optional[Hand] = None

    def next_hand(self) -> Hand:
        """
        Checks if the current hand is done and if so will return the next hand. If not it will
        return the current hand.
        :rtype: Hand
        """
        if self._current_hand is None:
            self._current_hand = Hand(PlayOrder(self.teams))
        elif self._current_hand.done:
            next_order = self._current_hand.next_play_order
            self._current_hand = Hand(next_order)
        return self._current_hand

    @property
    def done(self):
        """
        Check if game is done.
        :return: True if done else false
        :rtype: bool
        """
        return self.win_score <= self.score_card.max
