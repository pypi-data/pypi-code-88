from datetime import datetime
from functools import lru_cache
from .conversor import Conversor

from jiraX import factories as factory
from sro_db.application import factories
from sro_db.model import factories as factories_model

class ConversorUserStory(Conversor):
    """
    Class responsible for create a SRO's Atomic User Story from a Jira's Issue
    """
    def __init__(self, organization, data):
        super().__init__(organization, data)
    
    def convert(self, etl_scrum_project: object, etl_team_member: object, etl_sprint: object,
        jira_issue: object, jira_project: object,
        ontology_atomic_user_story: object = None) -> object:
        """Method responsible for converting

        Jira Issue -> SRO Atomic User Story

        Args:
            etl_scrum_project (object): ETL scrum_project class
            etl_team_member (object): ETL team_member class
            etl_sprint (object): ETL sprint class
            jira_issue (object): Issue from Jira
            jira_project (object): Project from Jira
            ontology_atomic_user_story (object, optional): AtomicUserStory created by a sro_db's factory. Defaults to None.

        Returns:
            object: AtomicUserStory created by a sro_db's factory
        """
        print("--------- Conversor user_story -----------")

        product_backlog_application = factories.ProductBacklogFactory()
        team_member_application = factories.TeamMemberFactory()
        sprint_backlog_application = factories.SprintBacklogFactory()

        if ontology_atomic_user_story is None:
            ontology_atomic_user_story = factories_model.AtomicUserStoryFactory()
        ontology_atomic_user_story.name = jira_issue.raw['fields']['summary']
        ontology_atomic_user_story.description = jira_issue.raw['fields'].get('description') # wize
        # ontology_atomic_user_story.description = jira_issue.raw['fields']['description']
        ontology_atomic_user_story.index = jira_issue.key

        (activated_date, activated_id), (resolved_date, resolved_id), (closed_date, closed_id) = self.find_activated_resolved_closed(jira_issue)

        # Product Backlog
        print('product backlog')
        project_id = jira_project.id
        ontology_product_backlog = product_backlog_application.retrive_by_external_uuid(jira_project.id)
        if ontology_product_backlog == None:
            ontology_atomic_user_story.product_backlog_id = None
        else:
            ontology_atomic_user_story.product_backlog_id = ontology_product_backlog.id
        if ontology_atomic_user_story.product_backlog_id is None:
            scrum_project = etl_scrum_project()
            scrum_project.config(self.data)
            data_to_create = {'content': {'all': {'project': {'id': project_id}}}}
            _, _, _, product_backlog = scrum_project.create(data_to_create)
            ontology_atomic_user_story.product_backlog_id = product_backlog.id            

        print('creator')
        # Creator
        creator_id = jira_issue.raw['fields']['creator']['accountId']
        # print(f'Creator id {creator_id}')
        # print(jira_project.name)
        ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(creator_id, jira_project.name)
        # print(dir(ontology_team_member))
        if ontology_team_member == None:
            ontology_atomic_user_story.created_by = None
        else:
            ontology_atomic_user_story.created_by = ontology_team_member.id
        print('Criou ontology team memeber')
        if ontology_atomic_user_story.created_by is None:
            print('mas era None')
            team_member = etl_team_member()
            team_member.config(self.data)
            data_to_create = {'accountId': creator_id}
            print(data_to_create)
            team_member = team_member.create(data_to_create, None, jira_project)
            print("errado")
            ontology_atomic_user_story.created_by = team_member.id

        # TODO passar a usar create_user_story_team_member
        print('Assignee')
        # ontology_atomic_user_story.assigned_by = None
        # Assignee
        # assignee = jira_issue.raw.get("fields").get("assignee")
        # if assignee == None:
        #     ontology_atomic_user_story.assigned_by = [None]
        # else:
        #     assignee_id = assignee.get('accountId')
        #     self.create_user_story_team_member([assignee])
        #     ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(assignee_id, jira_project.name)
        #     if ontology_team_member == None:
        #         ontology_atomic_user_story.assigned_by = [None]
        #     else:
        #         ontology_atomic_user_story.assigned_by = [team_member_application.retrive_by_external_id_and_project_name(assignee_id, jira_project.name)]
        #     # print('test')
        # if ontology_atomic_user_story.assigned_by == [None]:
        #     team_member = etl_team_member()
        #     team_member.config(self.data)
        #     data_to_create = {'accountId': assignee_id}
        #     ontology_atomic_user_story.assigned_by = [team_member.create(data_to_create, None, jira_project)]

        print('Activated')
        # Activated
        if activated_id is None:
            ontology_atomic_user_story.activated_by = None
            ontology_atomic_user_story.activated_date = None
        else:    
            team_member_ = team_member_application.retrive_by_external_id_and_project_name(activated_id, jira_project.name)
            if team_member_ == None:
                ontology_atomic_user_story.activated_by = None
            else:
                ontology_atomic_user_story.activated_by = team_member_.id
            ontology_atomic_user_story.activated_date = activated_date
            if ontology_atomic_user_story.activated_by is None:
                team_member = etl_team_member()
                team_member.config(self.data)
                data_to_create = {'accountId': activated_id}
                team_member_ = team_member.create(data_to_create, None, jira_project)
                ontology_atomic_user_story.activated_by = team_member_.id
                ontology_atomic_user_story.activated_date = activated_date
            
        # exit()
        # Resolved
        if resolved_id is None:
            ontology_atomic_user_story.resolved_by = None
            ontology_atomic_user_story.resolved_date = None
        else:
            team_member_ = team_member_application.retrive_by_external_id_and_project_name(resolved_id, jira_project.name)
            if team_member_ == None:
                ontology_atomic_user_story.resolved_by = None
            else:
                ontology_atomic_user_story.resolved_by = team_member_.id
            ontology_atomic_user_story.resolved_date = resolved_date
            if ontology_atomic_user_story.resolved_by is None:
                team_member = etl_team_member()
                team_member.config(self.data)
                data_to_create = {'accountId': resolved_id}
                team_member_ = team_member.create(data_to_create, None, jira_project)
                ontology_atomic_user_story.resolved_by = team_member_.id
                ontology_atomic_user_story.resolved_date = resolved_date

        # Closed 
        if closed_id is None:
            ontology_atomic_user_story.closed_by = None
            ontology_atomic_user_story.closed_date = None
        else:
            team_member_ = team_member_application.retrive_by_external_id_and_project_name(closed_id, jira_project.name)
            if team_member_ == None:
                ontology_atomic_user_story.closed_by = None
            else:
                ontology_atomic_user_story.closed_by = team_member_.id
            ontology_atomic_user_story.closed_date = closed_date
            if ontology_atomic_user_story.closed_by is None:
                team_member = etl_team_member()
                team_member.config(self.data)
                data_to_create = {'accountId': closed_id}
                team_member_ = team_member.create(data_to_create, None, jira_project)
                ontology_atomic_user_story.closed_by = team_member_.id
                ontology_atomic_user_story.closed_date = closed_date
        
    
        # ontology_atomic_user_story.story_points = jira_issue.raw.get("fields").get("customfield_10020") # wize
        ontology_atomic_user_story.story_points = jira_issue.raw.get("fields").get("customfield_10016") # ledZepplin
        ontology_atomic_user_story.created_date = self.date_formater(jira_issue.raw.get("fields").get("created"))

        # Sprint backlogs
        # sprints = jira_issue.raw.get("fields").get("customfield_10018") # wize
        sprints = jira_issue.raw.get("fields").get("customfield_10020") # ledzepplin
        if not sprints: # Check if is None or []
            ontology_atomic_user_story.sprint_backlogs = []
        else:
            backlogs_list = []
            for sprint in sprints:
                sprint_id = sprint['id']
                board_id = sprint['boardId']
                ontology_sprint_backlog = sprint_backlog_application.retrive_by_external_uuid(sprint_id)
                if ontology_sprint_backlog is None:
                    sprint_backlog = etl_sprint()
                    sprint_backlog.config(self.data)
                    data_to_create = {'content': {'all': {'sprint': {'id': sprint_id, 'originBoardId': board_id}}}}
                    _, ontology_sprint_backlog = sprint_backlog.create(data_to_create)
                backlogs_list.append(ontology_sprint_backlog)
            ontology_atomic_user_story.sprint_backlogs = backlogs_list

        try:
            ontology_atomic_user_story.created_by_sro = jira_issue.is_a_task
        except Exception as e:
            ontology_atomic_user_story.created_by_sro = False
        
        print("--------- Conversor user_story end -----------")
        print(f'Name {ontology_atomic_user_story.name}')
        print(f'Description {ontology_atomic_user_story.description}')
        print(f'Index {ontology_atomic_user_story.index}')
        print()
        print(f'product_backlog_id {ontology_atomic_user_story.product_backlog_id}')
        print()
        print(f'created_by {ontology_atomic_user_story.created_by}')
        print(f'activated_by {ontology_atomic_user_story.activated_by}')
        print(f'closed_by {ontology_atomic_user_story.closed_by}') 
        print(f'resolved_by {ontology_atomic_user_story.resolved_by}') 
        # print(f'assigned_by {ontology_atomic_user_story.assigned_by}') 
        print()
        print(f'story_points {ontology_atomic_user_story.story_points}')
        print()
        print(f'created_date {ontology_atomic_user_story.created_date}') 
        print(f'activated_date {ontology_atomic_user_story.activated_date}') 
        print(f'closed_date {ontology_atomic_user_story.closed_date}') 
        print(f'resolved_date {ontology_atomic_user_story.resolved_date}')  

        # exit()

        return ontology_atomic_user_story