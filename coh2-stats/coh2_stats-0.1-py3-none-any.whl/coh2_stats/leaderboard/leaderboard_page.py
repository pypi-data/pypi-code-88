from coh2_stats.page.page import PageStatGroups, PagePerformances
import json

class LeaderboardPage(PageStatGroups, PagePerformances):
    def __init__(self, page) -> None:
        super().__init__(page)

    def get_player_ids(self):
        ids = []
        statgroups = self.get_team_statgroups()
        for statgroup in statgroups:
            member = statgroup.members[0]
            ids.append(member.profile_id)
        return ids


