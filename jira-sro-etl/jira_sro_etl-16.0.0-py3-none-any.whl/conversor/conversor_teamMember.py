from datetime import datetime
from functools import lru_cache
from .conversor import Conversor

from jiraX import factories as factory
from sro_db.application import factories
from sro_db.model import factories as factories_model

class ConversorTeamMember(Conversor):
    """
    Class responsible for create a SRO's Developer from a Jira's User
    """
    def __init__(self, organization, data):
        super().__init__(organization, data)

    def convert(self, etl_user: object, etl_scrum_development_team: object,
        jira_user: object, jira_project: object,
        ontology_team_member: object = None) -> object:
        """Method responsible for converting

        Jira User -> SRO Developer

        Args:
            etl_user (object): ETL user class
            etl_scrum_development_team (object): ETL scrum_development_team class
            jira_user (object): User from Jira
            jira_project (object): Project from Jira
            ontology_team_member (object, optional): Developer created by a sro_db's factory. Defaults to None.

        Returns:
            object: Developer created by a sro_db's factory
        """
        print("--------- Conversor team_member -----------")

        person_application = factories.PersonFactory()
        scrum_development_team_application = factories.DevelopmentTeamFactory()

        if ontology_team_member is None:
            ontology_team_member = factories_model.DeveloperFactory()
        ontology_team_member.team_role = 'developer'
        
        # Ontology_team_member.person
        user_id = jira_user.accountId
        ontology_person = person_application.retrive_by_external_uuid(user_id)
        if ontology_person is None:
            user = etl_user()
            user.config(self.data)
            data_to_create = {'content': {'all': {'user': {'accountId': user_id}}}}
            ontology_team_member.person_id = user.create(data_to_create).id
        else:
            ontology_team_member.person_id = ontology_person.id
        
        # Ontology_team_member
        team_id = jira_project.id
        ontology_development_team = scrum_development_team_application.retrive_by_external_uuid(team_id)
        if ontology_team_member.team_id is None:
            scrum_development_team = etl_scrum_development_team()
            scrum_development_team.config(self.data)
            data_to_create = {'content': {'all': {'project': {'id': team_id}}}}
            print(data_to_create)
            ontology_team_member.team_id = scrum_development_team.create(data_to_create).id
        else:
            ontology_team_member.team_id = ontology_development_team.id

        print(f'Team role {ontology_team_member.team_role}')
        print(f'Person id {ontology_team_member.person_id}')
        print(f'Team id {ontology_team_member.team_id}')

        print("--------- Conversor team_member end -----------")

        return ontology_team_member