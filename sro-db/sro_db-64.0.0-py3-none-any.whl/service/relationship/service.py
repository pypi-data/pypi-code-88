from sro_db.model.relationship.model import *
from sro_db.service.base_service import BaseService

class AssociationDevelopmentTaskTeamMemberService(BaseService):
    def __init__(self):
        super(AssociationDevelopmentTaskTeamMemberService,self).__init__(association_development_task_team_member_table)


class AssociationSprintScrumDevelopmentTaskService(BaseService):
    def __init__(self):
        super(AssociationSprintScrumDevelopmentTaskService,self).__init__(association_sprint_scrum_development_task_table)

class AssociationSprintBacklogScrumDevelopmentActivityService(BaseService):
    def __init__(self):
        super(AssociationSprintBacklogScrumDevelopmentActivityService,self).__init__(association_sprint_backlog_scrum_development_activity_table)


class AssociationAtomicUserStorySprintBacklogService(BaseService):
    def __init__(self):
        super(AssociationAtomicUserStorySprintBacklogService,self).__init__(association_atomic_user_story_sprint_backlog_table)

class AssociationUserStorySprintTeammemberService(BaseService):
    def __init__(self):
        super(AssociationUserStorySprintTeammemberService,self).__init__(association_user_story_sprint_team_member_table)

        