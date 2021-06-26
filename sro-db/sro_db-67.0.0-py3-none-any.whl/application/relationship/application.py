from sro_db.application.abstract_application import AbstractApplication
from sro_db.service.relationship.service import *


class AssociationDevelopmentTaskTeamMember(AbstractApplication):

    def __init__(self):
        super().__init__(AssociationDevelopmentTaskTeamMemberService())

class AssociationSprintScrumDevelopmentTask(AbstractApplication):
    
    def __init__(self):
        super().__init__(AssociationSprintScrumDevelopmentTaskService())

class AssociationSprintBacklogScrumDevelopmentActivity(AbstractApplication):
    
    def __init__(self):
        super().__init__(AssociationSprintBacklogScrumDevelopmentActivityService())

class AssociationAtomicUserStorySprintBacklog(AbstractApplication):
    
    def __init__(self):
        super().__init__(AssociationAtomicUserStorySprintBacklogService())

class AssociationUserStorySprintTeammember(AbstractApplication):
    
    def __init__(self):
        super().__init__(AssociationUserStorySprintTeammemberService())       