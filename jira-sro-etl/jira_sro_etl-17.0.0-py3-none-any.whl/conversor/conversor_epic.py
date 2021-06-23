from datetime import datetime
from functools import lru_cache
from .conversor import Conversor

from jiraX import factories as factory
from sro_db.application import factories
from sro_db.model import factories as factories_model

class ConversorEpic(Conversor):
    """
    Class responsible for create a SRO's Epic from a Jira's Issue
    """
    def __init__(self, organization, data):
        super().__init__(organization, data)

    def convert(self, etl_scrum_project: object, etl_team_member: object,
    jira_issue: object, jira_project: object,
    ontology_epic: object = None) -> object:
        """Method responsible for converting

        Jira Issue -> SRO Epic

        Args:
            etl_scrum_project (object): ETL scrum_project class
            etl_team_member (object): ETL team_member class
            jira_issue (object): Issue from Jira
            jira_project (object): Project from Jira
            ontology_epic (object, optional): Epic created by a sro_db's factory. Defaults to None.

        Returns:
            object: Epic created by a sro_db's factory
        """
        print("--------- Conversor epic -----------")

        team_member_application = factories.TeamMemberFactory()
        product_backlog_application = factories.ProductBacklogFactory()

        if ontology_epic is None:
            ontology_epic = factories_model.EpicFactory()
        ontology_epic.name = jira_issue.raw['fields']['summary']
        ontology_epic.index = jira_issue.key

        (activated_date, activated_id), (resolved_date, resolved_id), (closed_date, closed_id) = self.find_activated_resolved_closed(jira_issue)

        # Product Backlog
        ontology_product_backlog = product_backlog_application.retrive_by_external_uuid(jira_project.id)
        print(f"Project id: {jira_project.id}")
        if ontology_product_backlog == None:
            scrum_project = etl_scrum_project()
            scrum_project.config(self.data)
            data_to_create = {'content': {'all': {'project': {'id': jira_project.id}}}}
            _, _, _, product_backlog = scrum_project.create(data_to_create)
            ontology_epic.product_backlog_id = product_backlog.id
            print(f"Product backlog: {product_backlog.id}")
        else:
            print(f"Product backlog: {ontology_product_backlog.id}")
            ontology_epic.product_backlog_id = ontology_product_backlog.id
            
        # Creator
        creator_id = jira_issue.raw['fields']['creator']['accountId']
        ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(creator_id, jira_project.name)
        if ontology_team_member == None:
            team_member = etl_team_member()
            team_member.config(self.data)
            data_to_create = {'accountId': creator_id}
            ontology_epic.created_by = team_member.create(data_to_create, None, jira_project).id
        else:
            ontology_epic.created_by = ontology_team_member.id

        # Activated
        if activated_id is None:
            ontology_epic.activated_by = None
            ontology_epic.activated_date = None
        else:
            ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(activated_id, jira_project.name)
            if ontology_team_member == None:
                team_member = etl_team_member()
                team_member.config(self.data)
                data_to_create = {'accountId': activated_id}
                ontology_team_member = team_member.create(data_to_create, None, jira_project)
                ontology_epic.activated_by = ontology_team_member.id
            else:
                ontology_epic.activated_by = ontology_team_member.id
            ontology_epic.activated_date = activated_date           

        # Resolved
        if resolved_id is None:
            ontology_epic.resolved_by = None
            ontology_epic.resolved_date = None    
        else:
            ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(resolved_id, jira_project.name)
            if ontology_team_member == None:
                team_member = etl_team_member()
                team_member.config(self.data)
                data_to_create = {'accountId': resolved_id}
                team_member_ = team_member.create(data_to_create, None, jira_project)
                ontology_epic.resolved_by = team_member_.id
            else:
                ontology_epic.resolved_by = ontology_team_member.id
            ontology_epic.resolved_date = resolved_date

        # Closed 
        if closed_id is None:
            ontology_epic.closed_by = None
            ontology_epic.closed_date = None
        else:
            ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(closed_id, jira_project.name)
            if ontology_team_member == None:
                team_member = etl_team_member()
                team_member.config(self.data)
                data_to_create = {'accountId': closed_id}
                ontology_team_member = team_member.create(data_to_create, None, jira_project)
                ontology_epic.closed_by = ontology_team_member.id
                ontology_epic.closed_date = closed_date
            else:
                ontology_epic.closed_by = ontology_team_member.id
                ontology_epic.closed_date = closed_date

        ontology_epic.story_points = jira_issue.raw.get("fields").get("customfield_10016") # ledZepplin
        ontology_epic.created_date = self.date_formater(jira_issue.raw.get("fields").get("created"))

        print("--------- Conversor epic end -----------")

        return ontology_epic