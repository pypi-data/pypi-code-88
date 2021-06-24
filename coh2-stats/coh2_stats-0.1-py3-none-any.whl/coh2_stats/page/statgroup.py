class StatGroup:
    def __init__(self, json_data) -> None:
        self.id = json_data['id']
        self.members = [Member(member) for member in json_data['members']]
        self.team_member_count = len(self.members)

class Member:
    def __init__(self, json_data):
        self.profile_id = json_data['profile_id']
        self.alias = json_data['alias']
        self.personal_statgroup_id = json_data['personal_statgroup_id']