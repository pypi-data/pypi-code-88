from coh2_stats.page.statgroup import StatGroup, Member
from coh2_stats.page.page import PageStatGroups, PagePerformances

class PerformancePage(PageStatGroups, PagePerformances):
    def __init__(self, json_page):
        super().__init__(json_page)

        self.team_statgroups = self.get_team_statgroups()
        self.performances = self.get_player_performances()

    def get_members_from_id(self, statgroup_id, statgroups: list[StatGroup])-> list[Member]:
        for statgroup in statgroups:
            if statgroup.id == statgroup_id:
                return statgroup.members

    def get_statgroup_member_from_personal_id(self, personal_id, statgroups):
        for statgroup in statgroups:
            for member in statgroup.members:
                if member.personal_statgroup_id == personal_id:
                    return member

        return None
        
