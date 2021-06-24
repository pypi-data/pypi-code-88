from datetime import datetime
from functools import lru_cache
from .conversor import Conversor

from jiraX import factories as factory
from sro_db.application import factories
from sro_db.model import factories as factories_model

class ConversorTask(Conversor):
    """
    Class responsible for create a SRO's Scrum Indended Development Task and Scrum Performed Development Task from a Jira's Issue
    """
    def __init__(self, organization, data):
        super().__init__(organization, data)

    def convert(self, etl_team_member: object, etl_user_story: object, etl_sprint: object,
        jira_issue: object, jira_project: object,
        ontology_scrum_intended_development_task: object = None, ontology_scrum_performed_development_task: object = None):
        """Method responsible for converting

        Jira Issue -> SRO Scrum Indended Development Task and Scrum Performed Development Task

        Args:
            etl_team_member (object): ETL team_member class
            etl_user_story (object): ETL user_story class
            etl_sprint (object): ETL sprint class
            jira_issue (object): Issue from Jira
            jira_project (object): Project from Jira
            ontology_scrum_intended_development_task (object, optional): ScrumIntentedDevelopmentTask created by a sro_db's factory. Defaults to None.
            ontology_scrum_performed_development_task (object, optional): ScrumPerformedDevelopmentTask created by a sro_db's factory. Defaults to None.

        Returns:
            tuple[object, object]: ScrumIntentedDevelopmentTask and ScrumPerformedDevelopmentTask
        """
        print("--------- Conversor task -----------")

        # Ontology scrum intended development task
        team_member_application = factories.TeamMemberFactory()
        priority_application = factories.PriorityFactory()
        atomic_user_story_application = factories.AtomicUserStoryFactory()
        sprint_application = factories.SprintFactory()
        sprint_backlog_application = factories.SprintBacklogFactory()
        development_task_type_application = factories.DevelopmentTaskTypeFactory()
        priority_dict = {'1': 'high', '2': 'high', '3': 'medium', '4': 'normal', '5': 'normal'}

        (activated_date, activated_id), (resolved_date, resolved_id), (closed_date, closed_id) = self.find_activated_resolved_closed(jira_issue)

        def _scrum_development_task(scrum_dev_task):
            scrum_dev_task.name = jira_issue.raw['fields']['summary']
            scrum_dev_task.description = jira_issue.raw['fields'].get('description')
            scrum_dev_task.index = jira_issue.key

            # Created date
            scrum_dev_task.created_date = self.date_formater(jira_issue.raw['fields']['created'])

            # Created by
            creator_id = jira_issue.raw['fields']['creator']['accountId']
            print("Created by")
            print(f"Creator id {creator_id}")
            print(f"Jira project name {jira_project.name}")
            ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(creator_id, jira_project.name)
            print('test')
            # print(ontology_team_member.id)
            # exit()
            if ontology_team_member is None:
                print('test')
                team_member = etl_team_member()
                team_member.config(self.data)
                data_to_create = {'accountId': creator_id}
                created_by = team_member.create(data_to_create, None, jira_project)
                scrum_dev_task.created_by = created_by.id
            else:
                print('test')
                scrum_dev_task.created_by = ontology_team_member.id
            
            # Assigned by
            print('Assigned by')
            # assignee_id = jira_issue.raw['fields']['assignee']['accountId']
            # scrum_dev_task.assigned_by = [team_member_application.retrive_by_external_id_and_project_name(assignee_id, jira_project.name)]
            # if scrum_dev_task.assigned_by == [None]:
            #     team_member = etl_team_member()
            #     team_member.config(self.data)
            #     data_to_create = {'accountId': assignee_id}
            #     scrum_dev_task.assigned_by = [team_member.create(data_to_create, None, jira_project)]
            

            # Story Points
            print('Story points')
            # scrum_dev_task.story_points = jira_issue.raw.get("fields").get("customfield_10020") #wize
            scrum_dev_task.story_points = jira_issue.raw.get("fields").get("customfield_10016") #ledzepplin

            # # Sprints & Sprint Backlogs
            # print('Sprint e Sprint Backlogs')
            # sprints_list = []
            # backlogs_list = []
            
            # # sprints = scrum_dev_task.story_points = jira_issue.raw.get("fields").get("customfield_10018") #wize
            # sprints = scrum_dev_task.story_points = jira_issue.raw.get("fields").get("customfield_10020") #ledzepplin
            # print(sprints)
            # sprints.sort(key=lambda x: self.date_formater(x['startDate']))
            # if not sprints: # Check if is None or []
            #     scrum_dev_task.sprints = []
            #     scrum_dev_task.sprint_backlogs = []
            # else:
            #     for sprint in sprints:
            #         sprint_id = sprint['id']
            #         board_id = sprint['boardId']
            #         ontology_sprint = sprint_application.retrive_by_external_uuid(sprint_id)
            #         ontology_sprint_backlog = sprint_backlog_application.retrive_by_external_uuid(sprint_id)
            #         if ontology_sprint is None: # Se não existe sprint, tbm não existe sprint_backlog
            #             sprint_backlog = etl_sprint()
            #             sprint_backlog.config(self.data)
            #             data_to_create = {'content': {'all': {'sprint': {'id': sprint_id, 'originBoardId': board_id}}}}
            #             ontology_sprint, ontology_sprint_backlog = sprint_backlog.create(data_to_create)
            #         if(closed_date is not None):
            #             try:
            #                 if(ontology_sprint.start_date <= closed_date <= ontology_sprint.complete_date):
            #                     sprints_list.append(ontology_sprint)
            #                     backlogs_list.append(ontology_sprint_backlog)
            #                     break
            #             except Exception as e:
            #                 pass
            #         sprints_list.append(ontology_sprint)
            #         backlogs_list.append(ontology_sprint_backlog)
            #     scrum_dev_task.sprints = sprints_list
            #     scrum_dev_task.sprint_backlogs = backlogs_list

            # Atomic User Story
            print('Atomic User Story')
            parent_id = jira_issue.raw['fields']['parent']['id']
            ontology_atomic_user_story = atomic_user_story_application.retrive_by_external_uuid(parent_id)
            if ontology_atomic_user_story is None:
                atomic_user_story = etl_user_story()
                atomic_user_story.config(self.data)
                data_to_create = {"content": {"all": {"issue": {"id": parent_id } } } }
                scrum_dev_task.atomic_user_story = atomic_user_story.create(data_to_create, None, jira_project).id
            else:
                scrum_dev_task.atomic_user_story = ontology_atomic_user_story.id
            
        
        if ontology_scrum_intended_development_task is None:
            ontology_scrum_intended_development_task = factories_model.ScrumIntentedDevelopmentTaskFactory()
        
        _scrum_development_task(ontology_scrum_intended_development_task)
        
        # Type Activity
        print('\n\n\n\nType Activity')
        task_type = jira_issue.raw['fields'].get('labels')
        if task_type != []:
            task_type = jira_issue.raw['fields']['labels'][0].lower() #wize
            # task_type = jira_issue.raw['fields']['issuetype']['name'].lower() # ledzepplin
            print(task_type)
            ontology_development_task_type = development_task_type_application.retrive_by_name(task_type)
            if ontology_development_task_type is None:
                ontology_development_task_type = factories_model.DevelopmentTaskTypeFactory()
                ontology_development_task_type.name = task_type
                ontology_development_task_type.description = task_type
                ontology_development_task_type  = development_task_type_application.create(ontology_development_task_type)
            ontology_scrum_intended_development_task.type_activity = ontology_development_task_type.id
        else:
            ontology_scrum_intended_development_task.type_activity = None
            

        

        # Priority
        print('Priority')
        ontology_priority = priority_application.retrive_by_name(priority_dict[jira_issue.raw.get("fields").get("priority").get("id")])
        print('test')
        if ontology_priority == None:
            ontology_scrum_intended_development_task.priority = None
        else:
            ontology_scrum_intended_development_task.priority = ontology_priority.id
            
        # Risk
        ontology_scrum_intended_development_task.risk = None

        # Time estimate
        ontology_scrum_intended_development_task.time_estimate = jira_issue.raw['fields']['timeoriginalestimate']

        # --------------------------

        # Performed
        if (jira_issue.raw['fields']['status']['statusCategory']['id'] == 3 # Itens concluídos
        or jira_issue.raw['fields']['status']['statusCategory']['id'] == 4): # Em andamento
            
            # Ontology scrum performed development task
            if ontology_scrum_performed_development_task is None:
                ontology_scrum_performed_development_task = factories_model.ScrumPerformedDevelopmentTaskFactory()
            
            _scrum_development_task(ontology_scrum_performed_development_task)

            # Closed Date & Closed By
            print('Closed Date & Closed By')
            if closed_id is None:
                ontology_scrum_performed_development_task.closed_by = None
                ontology_scrum_performed_development_task.closed_date = None
            else:
                ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(closed_id, jira_project.name)
                if ontology_team_member == None:
                    team_member = etl_team_member()
                    team_member.config(self.data)
                    data_to_create = {'accountId': closed_id}
                    ontology_team_member = team_member.create(data_to_create, None, jira_project)
                    ontology_scrum_performed_development_task.closed_by = ontology_team_member.id
                    ontology_scrum_performed_development_task.closed_date = closed_date
                else:
                    ontology_scrum_performed_development_task.closed_by = ontology_team_member.id
                    ontology_scrum_performed_development_task.closed_date = closed_date
                
            # Activated Date & Activated By
            print('Activated Date & Activated By')
            if activated_id is None:
                ontology_scrum_performed_development_task.activated_by = None
                ontology_scrum_performed_development_task.activated_date = None
            else: 
                ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(activated_id, jira_project.name)
                if ontology_team_member == None:
                    team_member = etl_team_member()
                    team_member.config(self.data)
                    data_to_create = {'accountId': activated_id}
                    ontology_team_member = team_member.create(data_to_create, None, jira_project)
                    ontology_scrum_performed_development_task.activated_by = ontology_team_member.id
                    ontology_scrum_performed_development_task.activated_date = activated_date
                else:
                    ontology_scrum_performed_development_task.activated_by = ontology_team_member.id
                    ontology_scrum_performed_development_task.activated_date = activated_date
               
            # Resolved Date & Resolved By
            print('Resolved Date & Resolved By')
            if resolved_id is None:
                ontology_scrum_performed_development_task.resolved_by = None
                ontology_scrum_performed_development_task.resolved_date = None
            else:
                ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(resolved_id, jira_project.name)
                if ontology_team_member == None:
                    ontology_scrum_performed_development_task.resolved_by = ontology_team_member.id
                    ontology_scrum_performed_development_task.resolved_date = resolved_date
                else:
                    team_member = etl_team_member()
                    team_member.config(self.data)
                    data_to_create = {'accountId': resolved_id}
                    ontology_team_member = team_member.create(data_to_create, None, jira_project)
                    ontology_scrum_performed_development_task.resolved_by = ontology_team_member.id
                    ontology_scrum_performed_development_task.resolved_date = resolved_date

            # Caused By (É feito fora do conversor, porque depende do intended)
            # ontology_scrum_performed_development_task.caused_by = ontology_scrum_intended_development_task.id

            # Time Spent
            print('Time Spent')
            ontology_scrum_performed_development_task.time_spent = jira_issue.raw['fields']['timespent']
            
            print("--------- Conversor task end -----------")

            # exit()

            return ontology_scrum_intended_development_task, ontology_scrum_performed_development_task
        
        print("--------- Conversor task end -----------")

        # exit()
        return ontology_scrum_intended_development_task, None