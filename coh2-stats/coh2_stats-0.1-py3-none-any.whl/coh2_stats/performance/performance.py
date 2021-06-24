from coh2_stats.leaderboard.leaderboard_constants import LeaderboardConstants

class Performance:
    def __init__(self, performance_data) -> None:
        self.statgroup_id = performance_data['statgroup_id']
        self.ladder_id = performance_data['leaderboard_id']
        self.wins = performance_data['wins']
        self.losses = performance_data['losses']

        total_games = self.wins + self.losses
        self.rank = performance_data['rank']

        self.ladder_name = self.get_ladder_name(self.ladder_id)

        if total_games == 0:
            self.win_rate = -1
            pass
            #print("wtf")
        else:
            self.win_rate = round(self.wins / (self.wins + self.losses), 2)

        self.is_4s_solo = self.ladder_id in LeaderboardConstants.ladder_ids_4s_solo
        self.is_team = self.ladder_id in LeaderboardConstants.ladder_ids_team

        self.count = 1
        if self.is_team:
            self.count = int(self.ladder_name[-1])

        #if self.is_team:
            #Performance.add_to_team_database(self)

    def is_qualified(self):
        if self.rank == -1:
            return False
        return True

    def get_ladder_name(self, ladder_id):
        if ladder_id in LeaderboardConstants.ladder_ids:
            ladder_name = LeaderboardConstants.id_to_ladder_name[self.ladder_id]
        else:
            ladder_name = "NULL"
        return ladder_name

    def __repr__(self) -> str:
        self.info = f'{self.ladder_name} rank:{self.rank} wins:{self.wins} {self.losses} {self.win_rate}' + \
                f' sg_id:{self.statgroup_id}'
        return self.info