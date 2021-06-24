from coh2_stats.performance.performance import Performance
from coh2_stats.page.statgroup import StatGroup
import json

class Page:
    def __init__(self, page_json) -> None:
        if page_json is None:
            self.page = []
        else:
            self.page = json.loads(page_json)

class PageStatGroups(Page):
    def __init__(self, page) -> None:
        super().__init__(page)

    def get_team_statgroups(self):
        data = self.page['statGroups']
        return [ StatGroup(datum) for datum in data]

class PagePerformances(Page):
    def __init__(self, page) -> None:
        super().__init__(page)

    def get_player_performances(self):
        data = self.page['leaderboardStats']
        return [ Performance(datum) for datum in data if Performance(datum).is_qualified()]


from coh2_stats.match.match_statistics import MatchStatistics

class PageMatchHistoryStats(Page):
    def __init__(self, page) -> None:
        super().__init__(page)

    def get_match_list(self):
        if self.page == []:
            return []

        match_list = self.page['matchHistoryStats']

        match_stats_list = []
        for match_data in match_list:
            ms = MatchStatistics(match_data)
            match_stats_list.append(ms)

        return match_stats_list
