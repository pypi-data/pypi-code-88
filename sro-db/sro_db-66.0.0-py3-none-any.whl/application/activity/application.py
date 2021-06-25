from sro_db.service.activity.service import *
from sro_db.application.abstract_application import AbstractApplication

class ApplicationScrumIntentedDevelopmentTask(AbstractApplication):
    
    def __init__(self):
        super().__init__(ScrumIntentedDevelopmentTaskService())

    def update(self, object):
        # Atributos do filho
        instance = super().update(object)

        # Atributos do pai
        application_scrum_development_task = ApplicationScrumDevelopmentTask()
        application_scrum_development_task.update(object)
    
class ApplicationScrumPerformedDevelopmentTask(AbstractApplication):
    def __init__(self):
        super().__init__(ScrumPerformedDevelopmentTaskService())

    def update(self, object):
        # Atributos do filho
        instance = super().update(object)

        # Atributos do pai
        application_scrum_development_task = ApplicationScrumDevelopmentTask()
        application_scrum_development_task.update(object)
    
class ApplicationDevelopmentTaskType(AbstractApplication):

    def __init__(self):
        super().__init__(DevelopmentTaskTypeService())
    
    def retrive_by_name (self, name):
        return self.service.retrive_by_name(name)

class ApplicationPriority(AbstractApplication):

    def __init__(self):
        super().__init__(PriorityService())
    
    def retrive_by_name (self, name):
        return self.service.retrive_by_name(name)

class ApplicationRisk(AbstractApplication):

    def __init__(self):
        super().__init__(RiskService())
    
    def retrive_by_name (self, name):
        return self.service.retrive_by_name(name)

class ApplicationScrumDevelopmentTask(AbstractApplication):
    def __init__(self):
        super().__init__(ScrumDevelopmentTaskService())