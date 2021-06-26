from sro_db.application.abstract_application import AbstractApplication
from sro_db.service.artifact.service import UserStoryService, EpicService, AtomicUserStoryService, ProductBacklogService, SprintBacklogService


class ApplicationEpic(AbstractApplication):
    
    def __init__(self):
        super().__init__(EpicService())

    def update (self, object):
        # Atributos do filho
        instance = super().update(object)

        # Atributos do pai
        application_user_story = ApplicationUserStory()
        application_user_story.update(object)

class ApplicationUserStory(AbstractApplication):
    
    def __init__(self):
        super().__init__(UserStoryService())

class ApplicationAtomicUserStory(AbstractApplication):
    
    def __init__(self):
        super().__init__(AtomicUserStoryService())

    def update (self, object):
        # Atributos do filho
        instance = super().update(object)

        # Atributos do pai
        application_user_story = ApplicationUserStory()
        application_user_story.update(object)

class ApplicationProductBacklog(AbstractApplication):

    def __init__ (self):
        super().__init__(ProductBacklogService())
    
    def retrive_by_project_name(self, project_name):
        with self.create_session_connection() as session:
            return self.service.retrive_by_project_name(project_name)

class ApplicationSprintBacklog(AbstractApplication):

    def __init__ (self):
        super().__init__(SprintBacklogService())
        
    def retrive_by_name_and_project_name(self, sprint_name, project_name):
        with self.create_session_connection() as session:
            return self.service.retrive_by_name_and_project_name( sprint_name, project_name)
    
