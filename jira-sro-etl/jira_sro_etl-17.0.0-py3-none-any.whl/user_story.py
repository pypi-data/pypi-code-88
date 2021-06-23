import logging

from pymongo.message import _EMPTY, update
from pymongo.results import UpdateResult
logging.basicConfig(level=logging.INFO)

from jiraX import factories as factory
from pprint import pprint
from .base_entity import BaseEntity
from tqdm import tqdm

from sro_db.application import factories
from sro_db.model import factories as factories_model
from .conversor import factories as factories_conversor

from .scrum_project import scrum_project as etl_scrum_project
from .team_member import team_member as etl_team_member
from .sprint import sprint as etl_sprint
import datetime


""" User story """
class user_story(BaseEntity):
	"""
	Class responsible for retrieve user storys from jira
	"""
	def create(self, data: dict, jira_issue: object = None, jira_project: object = None) -> object:
		"""Create an Atomic User Story on Sro's database (if this atomic user story already exists, do nothing)

		Args:
			data (dict): Dict with jira issue information (issue_id = data['content']['all']['issue']['id'])
			and project information (project_id = data['content']['all']['issue']['fields']['project']['id'])
			jira_issue (object, optional): Issue from Jira
			jira_project (object, optional): Project from Jira

		Returns:
			object: AtomicUserStory created by a sro_db's factory
		"""
		try:
			logging.info("Creating Atomic User Story")

			if jira_issue is None:
				# Check if exisits in the bd
				issue_id = data['content']['all']['issue']['id']
				atomic_user_story_application = factories.AtomicUserStoryFactory()
				ontology_atomic_user = atomic_user_story_application.retrive_by_external_uuid(issue_id)
				if ontology_atomic_user != None:
					logging.info("User Story already exist in database")
					return
				else:
					issue_apl = factory.IssueFactory(user=self.user,apikey=self.key,server=self.url)
					jira_issue = issue_apl.find_by_id(issue_id)
			else:
				# Check if exisits in the bd
				issue_id = jira_issue.id
				atomic_user_story_application = factories.AtomicUserStoryFactory()
				ontology_atomic_user = atomic_user_story_application.retrive_by_external_uuid(issue_id)
				if ontology_atomic_user != None:
					logging.info("User Story already exist in database")
					return

			
			if jira_project is None:
				project_id = data['content']['all']['issue']['fields']['project']['id']
				project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
				jira_project = project_apl.find_by_id(project_id)
			# print('-----------project id = '+ jira_project.id +' ----------')
			
			self.conversor = factories_conversor.ConversorUserStoryFactory(organization = self.organization, 
			data = self.data)
			atomic_user_story = self.conversor.convert(
				etl_scrum_project, etl_team_member, etl_sprint,
				jira_issue, jira_project)

			atomic_user_story = atomic_user_story_application.create(atomic_user_story)

			# Assignee
			assignee = jira_issue.raw.get("fields").get("assignee")
			if assignee != None:
				assignee_id = assignee.get('accountId')
				team_member_application = factories.TeamMemberFactory()
				ontology_team_member = team_member_application.retrive_by_external_id_and_project_name(assignee_id, 
				jira_project.name)
				if ontology_team_member is None:
					team_member = etl_team_member()
					team_member.config(self.data)
					data_to_create = {'accountId': assignee_id}
					ontology_team_member = team_member.create(data_to_create, None, jira_project)
				association_development_task = factories_model.AssociationUserStorySprintTeammemberFactory()
				association_development_task.date = datetime.datetime.now()
				association_development_task.activate = True
				association_development_task.user_story_id = atomic_user_story.id
				association_development_task.team_member_id = ontology_team_member.id

				ontology_association_development_task_application = factories.AssociationUserStorySprintTeammemberFactory()
				ontology_association_development_task_application.create(association_development_task)


			# print('Atomic_user_story_sprint_backlog')
			# print('passou o sprint')
			# Sprint_backlog association_sprint_backlog_scrum_development_activity_table
			# sprints = jira_issue.raw.get("fields").get("customfield_10018") # wize
			sprint_name = jira_issue.raw.get("fields").get("customfield_10020")[0].get('name') # ledzepplin
			sprint_id = jira_issue.raw.get("fields").get("customfield_10020")[0].get('id') # ledzepplin
			if sprint_name != None:
				sprint_backlog_application = factories.SprintBacklogFactory()
				ontology_sprint_backlog = sprint_backlog_application.retrive_by_name_and_project_name(sprint_name, jira_project.name)
				if ontology_sprint_backlog is None:
					sprint = etl_sprint()
					sprint.config(self.data, 'sprint')
					data_to_create = {'content':{'all':{'sprint':{'id': sprint_id}}}}
					ontology_sprint_backlog = sprint.create(data_to_create, None, jira_project)
				association = factories_model.AssociationAtomicUserStorySprintBacklogFactory()
				association_development_task.date = datetime.datetime.now()
				association_development_task.activate = True
				association.user_story_id = atomic_user_story.id
				association.sprint_backlog_id = ontology_sprint_backlog.id

				ontology_association = factories.AssociationAtomicUserStorySprintBacklogFactory()
				ontology_association.create(association)
			
			self.create_application_reference('issue', atomic_user_story, jira_issue.id, jira_issue.self)
			
			logging.info("Atomic User Story created")

			self.insert_one_on_mongo_db(jira_issue.raw, 'issue')

			return atomic_user_story

		except Exception as e:
			pprint(e)
			logging.error("Failed to create Atomic User Story")

	def update(self, data: dict, is_a_task: bool = False) -> object:
		"""Update an Atomic User Story on Sro's database 

		Args:
			data (dict): Dict with jira issue information (issue_id = data['content']['all']['issue']['id'])
			and project information (project_id = data['content']['all']['issue']['fields']['project']['id'])
			is_a_task (bool, optional): True if issue is a Task on jira, otherwise False. Defaults to False.

		Returns:
			object: AtomicUserStory created by a sro_db's factory
		"""
		try:
			logging.info("Updating Atomic User Story")

			issue_id = data['content']['all']['issue']['id']
			issue_apl = factory.IssueFactory(user=self.user,apikey=self.key,server=self.url)
			jira_issue = issue_apl.find_by_id(issue_id)

			if is_a_task:
				jira_issue.is_a_task = True
			
			project_id = data['content']['all']['issue']['fields']['project']['id']
			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			jira_project = project_apl.find_by_id(project_id)
			
			atomic_user_story_application = factories.AtomicUserStoryFactory()
			ontology_user_story = atomic_user_story_application.retrive_by_external_uuid(jira_issue.id)
			print('entra conversor')
			self.conversor = factories_conversor.ConversorUserStoryFactory(organization = self.organization, data = self.data)
			atomic_user_story = self.conversor.convert(
				etl_scrum_project, etl_team_member, etl_sprint,
				jira_issue, jira_project, 
				ontology_user_story)
			print('saiu conversor')
			atomic_user_story_application.update(atomic_user_story)
			
			logging.info("Atomic User Story updated")

			self.find_one_and_update_on_mongo_db('issue', jira_issue.raw, 'id', jira_issue.raw['id'])

			return atomic_user_story

		except Exception as e:
			pprint(e)
			logging.error("Failed to update Atomic User Story")

	def delete(self, data):
		pass

	def extract(self,data):
		pass

	def do(self, data: dict) -> None:
		"""Retrieve all issues from mongo and save those with fields.issuetype.name = "História", "Tarefa"
		on sro db

		Args:
			data (dict): With user, key and server to connect with jira

		Returns:
			dict: Key is the project's key and value is a list with all user stories of this project
		"""
		try:
			logging.info("User Story")
					
			self.config(data)
			
			#Buscando os dados salvos no banco do mongo
			mongo_collection_name = self.mongo_db.get_collection('issue')

			#Salvando as histórias de usuário quando são histórias
			jira_user_stories = mongo_collection_name.find({"fields.issuetype.name":"História"})
			self.create_atomic_user_story(jira_user_stories, created_by_sro = False)

			#criando as histórias de usuário quando há epic relacionados as histórias de usuário
			pprint ("criando histórias de usuários baaseado em EPIC para as tarefas")
			jira_user_stories = mongo_collection_name.find({"fields.issuetype.name":"Tarefa", "task_parent_type": "epic"})
			user_stories_list = self.create_atomic_user_story(jira_user_stories, created_by_sro = True, update = False)

			pprint ("update: criando histórias de usuários baaseado em EPIC para as tarefas" )
			self.update_user_story_created_by_sro(user_stories_list)

			pprint ("criando histórias de usuários baaseado em tarefas sem EPIC e US")
			jira_user_stories = mongo_collection_name.find({"fields.issuetype.name":"Tarefa", "task_parent_type": ""})
			user_stories_list = self.create_atomic_user_story(jira_user_stories, created_by_sro = True, update = False)
			
			pprint ("UPDATE: criando histórias de usuários baaseado em tarefas sem EPIC e US")
			self.update_user_story_created_by_sro(user_stories_list)
			
			logging.info("Successfully done Atomic User Story")

		except Exception as e:
			pprint(e)
			logging.error("Failed to do Atomic User Story")

	def update_user_story_created_by_sro(self, user_stories_list: list) -> None:
		"""Update user stories on the list on mongo db

		Args:
			user_stories_list (list): list of user stories (are objects)
		"""
		for user_story in user_stories_list:
			index_value = user_story.jira_element['id']
			field_value = user_story.id
			self.update_one_query("issue", "id", str(index_value), "sro_db_task_parent_id",field_value)
			self.update_one_query("issue", "id", str(index_value), "task_parent_type","atomic_user_story")	

	def create_atomic_user_story(self, jira_user_stories: list, created_by_sro: bool, update: bool = True) -> list:
		"""Create Atomic user stories on sro db

		Args:
			jira_user_stories (list): list of dicts
			created_by_sro (bool): True if issue was not a SubTask on jira
			update (bool, optional): If true, update all epic ids. Defaults to True.

		Returns:
			list: list of AtomicUserStory
		"""
		user_stories_list = self.create_ontology_atomic_user_story(jira_user_stories, created_by_sro)		

		atomic_user_story_application = factories.AtomicUserStoryFactory()
		user_stories_list = atomic_user_story_application.create_bulk(user_stories_list)
		self.create_application_reference_bulk(user_stories_list,'issue','id','self')

		#salvando sprint_backlog e epic
		self.create_user_story_spring_backlog(user_stories_list)

		#Salvando a relação entre team member e assigned da tarefa	e epic
		self.create_user_story_team_member(user_stories_list)

		#atualizando todos os IDs de epic
		if update:
			for user_story in user_stories_list:
				index_value = user_story.jira_element['id']
				field_value = user_story.id
				self.update_one_query("issue", "task_parent_id", str(index_value), "sro_db_task_parent_id",field_value)
				self.update_one_query("issue", "task_parent_id", str(index_value), "task_parent_type","atomic_user_story")
			
		return user_stories_list
				
	def create_ontology_atomic_user_story(self, jira_user_stories: list, created_by_sro: bool = False) -> list:
		"""Given a list of dicts with Jira's user story informations, create a list with AtomicUserStory (sro's db model)

		Args:
			jira_user_stories (list): list of dicts
			created_by_sro (bool): True if issue was not a SubTask on jira. Defaults to False.

		Returns:
			list: list of AtomicUserStory
		"""
		user_stories_list = []
			
		for jira_element in jira_user_stories:
				
			ontology_atomic_user_story = factories_model.AtomicUserStoryFactory()
				
			ontology_atomic_user_story.jira_element = jira_element

			ontology_atomic_user_story.index = jira_element['key']

			if jira_element["sro_db_task_parent_id"] > 0 and jira_element['task_parent_type'] == "epic": 
					
				ontology_atomic_user_story.epic = jira_element["sro_db_task_parent_id"]
			
			if jira_element["task_parent_type"] == "":
				ontology_atomic_user_story.epic = None

			ontology_atomic_user_story.created_by_sro = created_by_sro
				
			if 'fields' in jira_element:
				fields = jira_element['fields']
				if 'summary' in fields:
					ontology_atomic_user_story.name = fields['summary']	
				if 'description' in fields:			
					ontology_atomic_user_story.description = fields['description']
				if 'customfield_10020' in fields:
					ontology_atomic_user_story.story_points = fields['customfield_10020']
				if 'created' in fields:
					ontology_atomic_user_story.created_date = self.date_formater(fields['created'])
					
			ontology_atomic_user_story.product_backlog_id = jira_element['sro_db_product_backlog_id']

			if jira_element['sro_db_member_team_creator_id'] > 0:
				ontology_atomic_user_story.created_by = jira_element['sro_db_member_team_creator_id']
					
			if jira_element['sro_db_member_team_reporter_id'] > 0:
				ontology_atomic_user_story.reported_by = jira_element['sro_db_member_team_reporter_id']

			if jira_element['sro_db_member_team_activated_id'] > 0:
				ontology_atomic_user_story.activated_by = jira_element['sro_db_member_team_activated_id']
					
			if jira_element['sro_db_member_team_resolved_id'] > 0:
				ontology_atomic_user_story.resolved_by = jira_element['sro_db_member_team_resolved_id']

			if jira_element['sro_db_member_team_closed_id'] > 0:
				ontology_atomic_user_story.closed_by = jira_element['sro_db_member_team_closed_id']
		
			ontology_atomic_user_story.activated_date = jira_element['activated_date']
			
			ontology_atomic_user_story.closed_date = jira_element['closed_date']
			
			ontology_atomic_user_story.resolved_date = jira_element['resolved_date']

			user_stories_list.append(ontology_atomic_user_story)

		return 	user_stories_list	

	def update_by_time(self, data: dict, time: str):
		"""Retrieve stories from jira and save them on sro's database

		Args:
			data (dict): With user, key and server to connect with jira
			time (str): '1d' Will bring all stories created or updated on last 24h
		"""
		try:
			logging.info("Update User Story by time")
			self.config(data)

			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			issue_apl = factory.IssueFactory(user=self.user,apikey=self.key,server=self.url)
			atomic_user_story_application = factories.AtomicUserStoryFactory()

			projects = project_apl.find_all()
			for project in tqdm(projects, desc='User Story'):
				stories = issue_apl.find_story_by_project(project.key, time)
				for jira_story in stories:
					ontology_user_story = atomic_user_story_application.retrive_by_external_uuid(jira_story.id)
					if ontology_user_story is not None:
						atomic_user_story = self.conversor.user_story(
							etl_scrum_project, etl_team_member, etl_sprint,
							jira_story, project,
							ontology_user_story)
						atomic_user_story_application.update(atomic_user_story)
					else:
						self.create(None, jira_story, project)

			logging.info("Successfully updated User Story by time")

		except Exception as e:
			pprint(e)
			logging.error("Failed to update User Story by time")

