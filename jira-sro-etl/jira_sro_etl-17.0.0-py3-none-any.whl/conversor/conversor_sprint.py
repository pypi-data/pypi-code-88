from datetime import datetime
from functools import lru_cache
from .conversor import Conversor

from jiraX import factories as factory
from sro_db.application import factories
from sro_db.model import factories as factories_model

class ConversorSprint(Conversor):
    """
    Class responsible for create a SRO's Sprint and Sprint Backlog from a Jira's Sprint
    """
    def __init__(self, organization, data):
        super().__init__(organization, data)

    def convert(self, etl_scrum_project: object, jira_sprint: object, jira_project: object, ontology_sprint: object = None, ontology_sprint_backlog: object = None):
        """Method responsible for converting

        Jira Sprint -> SRO Sprint and Sprint Backlog

        Args:
            etl_scrum_project (object): ETL scrum_project class
            jira_sprint (object): Sprint from Jira
            jira_project (object): Project from Jira
            ontology_sprint (object, optional): Sprint created by a sro_db's factory. Defaults to None.
            ontology_sprint_backlog (object, optional): SprintBacklog created by a sro_db's factory. Defaults to None.

        Returns:
            tuple[object, object]: Sprint, SprintBacklog
        """
        print("--------- Conversor sprint -----------")
        
        scrum_process_application = factories.ScrumProcessFactory()

        # Sprint
        if ontology_sprint is None:
            ontology_sprint = factories_model.SprintFactory()
            
        ontology_sprint.organization = self.organization
        ontology_sprint.name = jira_sprint.name

        # description
        if hasattr(jira_sprint, 'goal'):
            ontology_sprint.description = jira_sprint.goal
        else:
            ontology_sprint.description = ''
        
        # start date
        if hasattr(jira_sprint, 'startDate'):
            ontology_sprint.start_date = self.date_formater(jira_sprint.startDate)
        else:
            ontology_sprint.start_date = None
        
        # end date
        if hasattr(jira_sprint, 'endDate'):
            ontology_sprint.end_date = self.date_formater(jira_sprint.endDate)
        else:
            ontology_sprint.end_date = None
        
        #complete date ??
        if hasattr(jira_sprint, 'completeDate'):
            ontology_sprint.complete_date = self.date_formater(jira_sprint.completeDate)
        else: 
            ontology_sprint.complete_date = None

        # Scrum process id
        project_id = jira_project.id
        ontology_scrum_process = scrum_process_application.retrive_by_external_uuid(project_id)
        if ontology_scrum_process is None:
            scrum_project = etl_scrum_project()
            scrum_project.config(self.data)
            data_to_create = {'content': {'all': {'project': {'id': project_id}}}}
            _, scrum_process, _, _ = scrum_project.create(data_to_create)
            ontology_sprint.scrum_process_id = scrum_process.id
        else:
            ontology_sprint.scrum_process_id = ontology_scrum_process.id
            

        # Sprint Backlog
        if ontology_sprint_backlog is None:
            ontology_sprint_backlog = factories_model.SprintBacklogFactory()
        ontology_sprint_backlog.name = ontology_sprint.name
        # ontology_sprint_backlog.sprint = ontology_sprint.id

        print("--------- Conversor sprint end -----------")

        return ontology_sprint, ontology_sprint_backlog