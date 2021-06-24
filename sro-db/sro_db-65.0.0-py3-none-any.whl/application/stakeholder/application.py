from sro_db.model.stakeholder.models import Person, Developer, ScrumMaster
from sro_db.service.stakeholder.service import PersonService, DeveloperService, ScrumMasterService, TeamMemberService
from sro_db.application.core.application import ApplicationApplicationReference
from sro_db.application.abstract_application import AbstractApplication
from pprint import pprint

class ApplicationPerson(AbstractApplication):
    
    def __init__(self):
        super().__init__(PersonService())
    
    def get_all(self, organization_uuid):
        return self.service.get_all(organization_uuid)
    def get_by_email(self, email):
        return self.service.get_by_email(email)
        
class ApplicationTeamMember(AbstractApplication):
    
    def __init__(self):
        super().__init__(TeamMemberService())
        
    def retrive_by_external_id_and_project_name(self, external_id, project_name):
        application_person = ApplicationPerson()
        print(external_id)
        person = application_person.retrive_by_external_uuid(external_id)
        
        if person is None:
            print("Pessoa n existe no banco")
            return None
        print("Pessoa existe no banco")
        # print( )
        result = self.service.retrive_by_external_id_and_project_name(person,project_name)
        print(person.id)
        print(project_name)
        print(result.id)
        print('aqui')
        # exit()
        return result
        
class ApplicationDeveloper(AbstractApplication):

    def __init__(self):
        super().__init__(DeveloperService())
    
    def create_with_project_name(self, external_id, project_name):
        application_person = ApplicationPerson()
        person = application_person.retrive_by_external_uuid(external_id)
        if person is not None:
            return self.service.create_with_project_name(person, project_name)
        return None        
        
class ApplicationScrumMaster(AbstractApplication):
    
    def __init__(self):
        super().__init__(ScrumMasterService())
        
    