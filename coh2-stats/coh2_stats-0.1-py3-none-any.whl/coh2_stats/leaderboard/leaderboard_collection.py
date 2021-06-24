from coh2_stats.utils.logger import Logger
from coh2_stats.leaderboard.leaderboard_constants import LeaderboardConstants
from coh2_stats.page_provider.leaderboard import LeaderboardPageProvider

class LeaderboardCollection:
    def __init__(self, leaderboards = []) -> None:
        self.leaderboards = leaderboards

    def add_elite_leaderboards(self, use_internet = True):
        for ladder_id in LeaderboardConstants.ladder_ids_4s_solo:
            leaderboard = LeaderboardPageProvider(ladder_id, 1, 400)
            leaderboard.load(use_internet)
            self.add_leaderboard(leaderboard)

        for ladder_id in LeaderboardConstants.ladder_ids_team:
            leaderboard = LeaderboardPageProvider(ladder_id, 1, 100)
            leaderboard.load(use_internet)
            self.add_leaderboard(leaderboard)

    def add_leaderboard(self, leaderboard: LeaderboardPageProvider):
        self.leaderboards.append(leaderboard)

    def get_player_id_list(self, eliminate_duplicates = True):
        player_id_list = []
        for leaderboard in self.leaderboards:
            player_id_list.extend(leaderboard.get_player_list())

        Logger(f"in all {len(player_id_list)} is recorded")
        if eliminate_duplicates:
            player_id_list = list(set(player_id_list))
            Logger(f"length of id_list is reduced to {len(player_id_list)} after duplicates being eliminated")
        return player_id_list
