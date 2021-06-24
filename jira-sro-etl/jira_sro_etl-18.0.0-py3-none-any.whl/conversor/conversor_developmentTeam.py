from datetime import datetime
from functools import lru_cache
from .conversor import Conversor

from jiraX import factories as factory
from sro_db.application import factories
from sro_db.model import factories as factories_model

class ConversorDevelopmentTeam(Conversor):
    """
    Class responsible for create a SRO's Development Team from a Jira's Project
    """
    def __init__(self, organization, data):
        super().__init__(organization, data)

    def convert(self, etl_scrum_project_team: object,
        jira_project: object,
        ontology_scrum_development_team: object = None) -> object:
        """Method responsible for converting

        Jira Project -> SRO Development Team

        Args:
            etl_scrum_project_team (object): ETL scrum_project_team class
            jira_project (object): Project from Jira
            ontology_scrum_development_team (object, optional): DevelopmentTeam created by a sro_db's factory. Defaults to None.

        Returns:
            object: DevelopmentTeam created by a sro_db's factory
        """
        print("--------- Conversor development team -----------")

        scrum_team_application = factories.ScrumTeamFactory()

        # Organization and name
        if ontology_scrum_development_team is None:
            ontology_scrum_development_team = factories_model.DevelopmentTeamFactory()
        ontology_scrum_development_team.organization = self.organization
        ontology_scrum_development_team.name = f"{jira_project.key}_scrum_development_team"
        
        # Scrum team id
        project_id = jira_project.id
        ontology_scrum_team = scrum_team_application.retrive_by_external_uuid(jira_project.id)
        if ontology_scrum_team == None:
            scrum_project_team = etl_scrum_project_team()
            scrum_project_team.config(self.data)
            data_to_create = {'content': {'all': {'project': {'id': project_id}}}}
            ontology_scrum_development_team.scrum_team_id = scrum_project_team.create(data_to_create).id
        else:
            ontology_scrum_development_team.scrum_team_id = ontology_scrum_team.id
            

        print("--------- Conversor development team end -----------")

        return ontology_scrum_development_team

            