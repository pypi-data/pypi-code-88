"""
Match making tool.
"""
import random

from whist.core.session.userlist import UserList


# pylint: disable=too-few-public-methods
class RandomMatch:
    """
    Distributes the players randomly to teams.
    """
    _num_teams: int
    _team_size: int
    _users: UserList

    def __init__(self, num_teams: int, team_size: int, users: UserList):
        self._num_teams = num_teams
        self._team_size = team_size
        self._users = users

    def distribute(self) -> None:
        """
        For given parameter distributes the players to teams.
        :return: None
        :rtype: None
        """
        players = self._users.players
        teams: list = list(range(0, self._team_size)) * self._num_teams
        for player in players:
            team_id = random.choice(teams)
            self._users.change_team(player, team_id)
            teams.remove(team_id)
