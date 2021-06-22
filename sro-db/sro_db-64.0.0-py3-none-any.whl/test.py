from pprint import pprint
from application import factories as application_factory
from model import factories as factories_model
from service.base_service import BaseService
from model.relationship.model import association_user_story_sprint_team_member_table
import datetime

class Test(BaseService):
    def find_all_by_userStoryId(self, user_story):
        print('entrou')
        with self.create_session_connection() as session:   
            results = session.query(self.object).filter(self.object.user_story_id == user_story.id)
            return results
    
    def update_assignee(self, user_story, team_member):
        print('entrou na update assignee')
        with self.create_session_connectio() as session:
            session.query(self.object).filter(self.object.user_story_id == user_story.id).update({"team_member_id": team_member.id})

    # def change_assignee(self, team_members_list)

apl_user_story = application_factory.AtomicUserStoryFactory()
user_story = apl_user_story.retrive_by_external_uuid('10275')

# apl_team_member = application_factory.TeamMemberFactory()
# team_member = apl_team_member.retrive_by_external_uuid('5b157fa264666649ccb90fc7')

# print(user_story)
# a = Test(association_user_story_sprint_team_member_table).find_all(user_story)
# pprint(a[0].user_story_id)

association_development_task = factories_model.AssociationUserStorySprintTeammemberFactory()
pprint(dir(association_development_task))
association_development_task.date = datetime.datetime.now()
association_development_task.activate = True
association_development_task.user_story_id = '1'
association_development_task.team_member_id = '1'
