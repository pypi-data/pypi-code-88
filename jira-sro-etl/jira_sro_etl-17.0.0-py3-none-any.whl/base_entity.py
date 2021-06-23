from pprint import pprint
from typing import Any
from jiraX import factories as factory
from pymongo.results import InsertManyResult, InsertOneResult
import logging
logging.basicConfig(level=logging.INFO)

from sro_db.application import factories
from sro_db.model import factories as factories_model

from .mongo_db.sro_mongo_db import Mongo_DB

from datetime import datetime
from .conversor.conversor import Conversor
from .conversor.conversor_developmentTeam import ConversorDevelopmentTeam
from .conversor.conversor_epic import ConversorEpic
from .conversor.conversor_project import ConversorProject
from .conversor.conversor_sprint import ConversorSprint
from .conversor.conversor_task import ConversorTask
from .conversor.conversor_team import ConversorTeam
from .conversor.conversor_teamMember import ConversorTeamMember
from .conversor.conversor_user import ConversorUser
from .conversor.conversor_userStory import ConversorUserStory
from .conversor import factories as factories_conversor

class BaseEntity():
    """ 
    Class responsible to connect with jira and make default tasks with database
    """
    def __init__(self):
        self.mongo_db = Mongo_DB()      
    
    def delete_data_collection(self, collection_name: str) -> None:
        """Delete a collection on mongo db

        Args:
            collection_name (str): The of collection to delete
        """
        self.mongo_db.delete_data_collection(collection_name)

    def config(self, data: dict) -> None:
        """Responsible to configure connection parameters

        Args:
            data (dict): Dictionary with user, key, url, organization_id and configuration_id to connect with jira and also get organization and configuration from database
        """
        self.data = data

        self.user = self.data['user']
        self.key = self.data['key']
        self.url = self.data['url']

        uuid = data['organization_id']
        organization_application = factories.OrganizationFactory()
        self.organization = organization_application.get_by_uuid(uuid)
        
        uuid_configuration = data['configuration_id']
        configuration_application = factories.ConfigurationFactory()
        self.configuration = configuration_application.get_by_uuid(uuid_configuration)

        self.conversor = None

    def create_application_reference_bulk(self, list_element: list, external_type_entity: str, external_id_index: str, external_url_index: str=None) -> None:
        """Create application reference for multiple elements at once

        Args:
            list_element (list): Elements list
            external_type_entity (str): Entity name on jira 
            external_id_index (str): Key to id on jira_element
            external_url_index (str, optional): Key to url on jira_element
        """
        application_reference_application = factories.ApplicationReferenceFactory()
        application_reference_list = []
        
        #criando o application reference
        for element in list_element:
            jira_element = element.jira_element
            application_reference = self.create_application_reference_without_save(external_type_entity, element, jira_element[external_id_index], jira_element[external_url_index])
            application_reference_list.append(application_reference)

        application_reference_application.create_bulk(application_reference_list)

    def create_application_reference(self, external_type_entity: str, internal_entity: object, external_id: str, external_url: str = None):
        """Responsible to save application reference on database

        Args:
            external_type_entity (str): Entity name on jira 
            internal_entity (obj): Object created by a sro_db's factory
            external_id (str): Unique identifier of object on jira
            external_url (str, optional): Url from jira object
        """
        application_reference_application = factories.ApplicationReferenceFactory()
        application_reference = self.create_application_reference_without_save(external_type_entity, internal_entity, external_id, external_url)
        application_reference_application.create(application_reference)

    def create_application_reference_without_save(self, external_type_entity: str, internal_entity: str, external_id: str, external_url: str = None) -> object:
        """Responsible to save application reference on database

        Args:
            external_type_entity (str): Entity name on jira 
            internal_entity (obj): Object created by a sro_db's factory
            external_id (str): Unique identifier of object on jira
            external_url (str, optional): Url from jira object
        """
        application_reference = factories_model.ApplicationReferenceFactory()
        application_reference.external_id = external_id
        # print('------- External id ' + application_reference.external_id + '------')
        application_reference.external_url = external_url
        application_reference.configuration = self.configuration.id
        application_reference.external_type_entity = external_type_entity
        application_reference.internal_uuid = internal_entity.uuid
        application_reference.entity_name = internal_entity.__tablename__
        
        return application_reference

    def date_formater(self, date_string: str) -> datetime:
        """Receive date in YYYY-MM-DD and return datetime

        Can receive date with more details like hour, minute and second, but all info
        after day is ignored

		Args:
			date_string (str/NoneType): string YYYY-MM-DD or None

		Returns:
			datetime/NoneType: Formated date or None if param was None
		"""
        if date_string:
            return datetime.strptime(date_string[:10], "%Y-%m-%d")
        return None
    
    def date_formater_2(self, date_string: str) -> datetime:
        """Receive date in YYYY-MM-DDTH:M:S and return datetime

		Args:
			date_string (str/NoneType): string YYYY-MM-DDTH:M:S or None

		Returns:
			datetime/NoneType: Formated date or None if param was None
		"""
        if date_string:
            return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z")
        return None

    def insert_many_on_mongo_db(self, list_entities: list, collection_name: str):
        """Insert many entities on a mongo collection at once

        Args:
            list_entities (list): List of entities
            collection_name (str): Collection's name

        Returns:
            InsertManyResult: Return of insert_many
        """
        return self.mongo_db.insert_many(list_entities, collection_name)

    def insert_one_on_mongo_db(self, entity: dict, collection_name: str):
        """Insert one entity on a mongo collection at once

        Args:
            entity (dict): Entity data
            collection_name (str): Collection's name

        Returns:
            InsertOneResult: Return of insert_one
        """
        return self.mongo_db.insert_one(entity, collection_name)

    def find_one_and_update_on_mongo_db(self, collection_name: str, entity: dict, index_name: str, index_value):
        """Find one entity and update it

        Args:
            collection_name (str): Collection's name
            entity (dict): New entity data
            index_name (str): Field to search/filter
            index_value (any): Value to use on search/filter
        """
        return self.mongo_db.find_one_and_update(collection_name, index_name, index_value, entity)

    def update_one_query(self, collection_name: str, index_name: str, index_value, field_name: str, field_value):
        """Update a field to certain entities of a collection

        Args:
            collection_name (str): Collection's name
            index_name (str): Field to search/filter
            index_value (any): Value to use on search/filter
            field_name (str): Field to be updated
            field_value ([type]): Value to use on update

        Returns:
            UpdateResult: Return of update_many
        """
        return self.mongo_db.update_one_query(collection_name, index_name, index_value, field_name,field_value) 

    def update_two_query(self, collection_name: str, index_name: str, index_value, index_name_2: str, index_value_2, field_name: str, field_value):
        """Update a field to certain entities of a collection

        Args:
            collection_name (str): Collection's name
            index_name (str): First field to search/filter
            index_value (any): Value to use on first search/filter
            index_name_2 (str): Second field to search/filter
            index_value_2 (any): Value to use on second search/filter field
            field_name (str): Field to be updated
            field_value (any): Value to use on update

        Returns:
            UpdateResult: Return of update_many
        """
        return self.mongo_db.update_two_query(collection_name, index_name, index_value, index_name_2, index_value_2, field_name, field_value)

    def update_one_query_array(self, collection_name: str, index_name: str, index_value, index_name_2: str, index_value_2, array_search_name, field_value):
        """[summary]

        Args:
            collection_name (str): Collection's name
            index_name (str): First field to search/filter
            index_value (any): Value to use on first search/filter
            index_name_2 (str): Second field to search/filter
            index_value_2 (any): Value to use on second search/filter field
            array_search_name ([type]): [description]
            field_value ([type]): [description]

        Returns:
            UpdateResult: Return of update_many
        """
        return self.mongo_db.update_one_query_array(collection_name, index_name, index_value, index_name_2, index_value_2, array_search_name, field_value)

    def update_many_on_mongo_db(self, list_entities: list, collection_name: str, field_name: str) -> None:
        """Update a collection field to the value of this field in entity (do it for all entities on the list)

        Args:
            list_entities (list): List of entities
            collection_name (str): Collection's name
            field_name (str): Collection's field that will be updated to the value of entity[field_name]
        """
        for entity in list_entities:
            self.mongo_db.update_one(collection_name,entity,field_name)

    def fill_development_task(self, development_task: object, jira_element: dict) -> None:
        """Fill attributes of SRO class derived from ScrumDevelopmentTask

        Args:
            development_task (object): Object created by a sro_db's factory
            jira_element (dict): Dictionary returned by jira's Api
        """
        development_task.jira_element = jira_element

        development_task.index = jira_element['key']

        # Risk
        development_task.risk = None
				
        if 'fields' in jira_element:
            fields = jira_element['fields']

            if 'summary' in fields:
                development_task.name = fields['summary']	
            if 'description' in fields:			
                development_task.description = fields['description']
            if 'customfield_10020' in fields:
                development_task.story_points = fields['customfield_10020']
            if 'created' in fields:
               development_task.created_date = self.date_formater(fields['created'])

            if 'timeoriginalestimate' in fields:
               development_task.time_estimate = fields['timeoriginalestimate']
            
            if 'timespent' in fields:
               development_task.time_spent = fields['timespent']
         	
        if jira_element['sro_db_member_team_creator_id'] > 0:
            development_task.created_by = jira_element['sro_db_member_team_creator_id']
				
        if jira_element['sro_db_member_team_reporter_id'] > 0:
            development_task.reported_by = jira_element['sro_db_member_team_reporter_id']

        if jira_element['sro_db_member_team_activated_id'] > 0:
           development_task.activated_by = jira_element['sro_db_member_team_activated_id']
				
        if jira_element['sro_db_member_team_resolved_id'] > 0:
           development_task.resolved_by = jira_element['sro_db_member_team_resolved_id']

        if jira_element['sro_db_member_team_closed_id'] > 0:
           development_task.closed_by = jira_element['sro_db_member_team_closed_id']
      
        development_task.activated_date = jira_element['activated_date']
        
        development_task.closed_date = jira_element['closed_date']
        
        development_task.resolved_date = jira_element['resolved_date']
        
        if jira_element["sro_db_task_parent_id"] > 0: 
            #Há tarefas ligadas em epic o que fazer?
            development_task.atomic_user_story = jira_element["sro_db_task_parent_id"]
    
    def create_sprint_backlog_development_task(self, scrum_intended_development_task_list: list,  scrum_performed_development_task_list: list) -> None:
        """[summary]

        Args:
            scrum_intended_development_task_list (list): List of objects created by a sro_db's factory
            scrum_performed_development_task_list (list): List of objects created by a sro_db's factory
        """
        association_sprint_backlog_development_activity_application = factories.AssociationSprintBacklogScrumDevelopmentActivityFactory()
		
        association_sprint_backlog_development_activity_list = self.create_association_sprint_backlog_development_task(scrum_intended_development_task_list)
        association_sprint_backlog_development_activity_application.create_bulk (association_sprint_backlog_development_activity_list)

        association_sprint_backlog_development_activity_list = self.create_association_sprint_backlog_development_task(scrum_performed_development_task_list)
        association_sprint_backlog_development_activity_application.create_bulk (association_sprint_backlog_development_activity_list)

    def create_association_sprint_backlog_development_task(self, scrum_development_task_list: list) -> list:
        """[summary]

        Args:
            scrum_development_task_list (list): List of objects created by a sro_db's factory

        Returns:
            list: List of objects created by a sro_db's factory
        """
        association_sprint_backlog_development_task_list = []
		
        for scrum_development_task in scrum_development_task_list:
           jira_element = scrum_development_task.jira_element 
           for sprint_backlog_id in jira_element['sro_db_sprint_backlogs']:
                association_sprint_backlog_development_task = factories_model.AssociationSprintBacklogScrumDevelopmentActivityFactory()
                association_sprint_backlog_development_task.date = datetime.datetime.now()
                association_sprint_backlog_development_task.activate = True
                association_sprint_backlog_development_task.scrum_development_task_id = scrum_development_task.id
                association_sprint_backlog_development_task.sprint_backlog_id = sprint_backlog_id
                association_sprint_backlog_development_task_list.append (association_sprint_backlog_development_task)
		
        return association_sprint_backlog_development_task_list

    def create_sprint_development_task(self, scrum_intended_development_task_list: list, scrum_performed_development_task_list: list) -> None:
        """[summary]

        Args:
            scrum_intended_development_task_list (list): List of objects created by a sro_db's factory
            scrum_performed_development_task_list (list): List of objects created by a sro_db's factory
        """
        association_sprint_development_task_application = factories.AssociationSprintScrumDevelopmentTaskFactory()
		
        association_sprintscrum_developmenttask_list = self.create_association_sprint_development_task(scrum_intended_development_task_list)
        association_sprint_development_task_application.create_bulk (association_sprintscrum_developmenttask_list)

        association_sprintscrum_developmenttask_list = self.create_association_sprint_development_task(scrum_performed_development_task_list)
        association_sprint_development_task_application.create_bulk (association_sprintscrum_developmenttask_list)

    def create_association_sprint_development_task(self, scrum_development_task_list: list) -> list:
        """[summary]

        Args:
            scrum_development_task_list (list): List of objects created by a sro_db's factory

        Returns:
            list: List of objects created by a sro_db's factory
        """
        association_sprint_scrum_developmenttask_list = []
        for scrum_development_task in scrum_development_task_list:
            
            jira_element = scrum_development_task.jira_element 

            for sprint_id in jira_element['sro_db_sprints']:
                association_sprint_development_task = factories_model.AssociationSprintScrumDevelopmentTaskFactory()
                association_sprint_development_task.date = datetime.datetime.now()
                association_sprint_development_task.activate = True
                association_sprint_development_task.scrum_development_task_id = scrum_development_task.id
                association_sprint_development_task.sprint_id = sprint_id
                association_sprint_scrum_developmenttask_list.append (association_sprint_development_task)

        return association_sprint_scrum_developmenttask_list

    def create_user_story_team_member (self, user_story_list: list) -> None:
        """[summary]

        Args:
            user_story_list (list): List of objects created by a sro_db's factory
        """
        association_userstory_teammember_application = factories.AssociationUserStorySprintTeammemberFactory()
        association_userstory_teammember_list = []
        
        for user_story in user_story_list:
           jira_element = user_story.jira_element 
           if jira_element['sro_db_member_team_assignee_id'] > 0:
                association_development_task= factories_model.AssociationUserStorySprintTeammemberFactory()
                association_development_task.date = datetime.datetime.now()
                association_development_task.activate = True
                association_development_task.user_story_id = user_story.id
                association_development_task.team_member_id = jira_element['sro_db_member_team_assignee_id']
                association_userstory_teammember_list.append (association_development_task)
		
        association_userstory_teammember_application.create_bulk(association_userstory_teammember_list)

    def create_development_task_teammember(self, scrum_intended_development_task_list: list, scrum_performed_development_task_list: list) -> None:
        """[summary]

        Args:
            scrum_intended_development_task_list (list): List of objects created by a sro_db's factory
            scrum_performed_development_task_list (list): List of objects created by a sro_db's factory
        """
        association_development_application = factories.AssociationDevelopmentTaskTeamMemberFactory()
        association_development_task_list = self.create_association_development_task_teammember(scrum_intended_development_task_list)
        association_development_application.create_bulk(association_development_task_list)

        association_development_task_list = self.create_association_development_task_teammember(scrum_performed_development_task_list)
        association_development_application.create_bulk(association_development_task_list)

    def create_association_development_task_teammember(self, scrum_development_task_list: list) -> list:
        """[summary]

        Args:
            scrum_development_task_list (list): [description]

        Returns:
            list: List of objects created by a sro_db's factory
        """
        association_development_task_list = []
		
        for scrum_development_task in scrum_development_task_list:
           jira_element = scrum_development_task.jira_element 
           if jira_element['sro_db_member_team_assignee_id'] > 0:
                association_development_task= factories_model.AssociationDevelopmentTaskTeamMemberFactory()
                association_development_task.date = datetime.datetime.now()
                association_development_task.activate = True
                association_development_task.scrum_development_task_id = scrum_development_task.id
                association_development_task.team_member_id = jira_element['sro_db_member_team_assignee_id']
                association_development_task_list.append (association_development_task)
		
        return association_development_task_list
     
    def create_user_story_spring_backlog(self, user_story_list: list) -> None:
        """[summary]

        Args:
            user_story_list (list): List of objects created by a sro_db's factory
        """
        association_atomic_user_story_sprint_backlog_factory_application = factories.AssociationAtomicUserStorySprintBacklogFactory()
        association_sprint_backlog_development_task_list = []
		
        for user_story in user_story_list:
            jira_element = user_story.jira_element
            for sprint_backlog_id in jira_element['sro_db_sprint_backlogs']:
                association_atomic_user_story_sprint_backlog = factories_model.AssociationAtomicUserStorySprintBacklogFactory()
                association_atomic_user_story_sprint_backlog.date = datetime.datetime.now()
                association_atomic_user_story_sprint_backlog.activate = True
                association_atomic_user_story_sprint_backlog.user_story_id = user_story.id
                association_atomic_user_story_sprint_backlog.sprint_backlog_id = sprint_backlog_id
                association_sprint_backlog_development_task_list.append(association_atomic_user_story_sprint_backlog)
		
        association_atomic_user_story_sprint_backlog_factory_application.create_bulk(association_sprint_backlog_development_task_list)
