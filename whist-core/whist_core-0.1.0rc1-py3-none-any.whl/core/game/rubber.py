"""Rubber of whist"""
from pydantic import BaseModel

from whist.core.game.game import Game
from whist.core.scoring.team import Team


class Rubber(BaseModel):
    """
    Implementation of a rubber.
    """
    max_games: int = 3
    games: list[Game] = []
    teams: list[Team]

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Configuration class for base model to allow fields which are not pydantic models.
        """
        arbitrary_types_allowed = True

    @property
    def games_played(self) -> int:
        """
        Amounts of games played already.
        :rtype: int
        """
        return len(self.games)

    @property
    def done(self) -> bool:
        """
        Checks if the rubber is done.
        :return: True if done else False
        :rtype: bool
        """
        return self.games_played == self.max_games

    def next_game(self) -> Game:
        """
        Creates a new game if the previous is done. Else returns the current game.
        :rtype: Game
        """
        if len(self.games) == 0 or self.games[-1].done:
            self.games.append(Game(self.teams))
        return self.games[-1]
