from . import development_task_type
import logging

from sro_db.model.activity.models import Priority
logging.basicConfig(level=logging.INFO)

from jiraX import factories as factory
from pprint import pprint
from .base_entity import BaseEntity
from tqdm import tqdm

from sro_db.application import factories
from sro_db.model import factories as factories_model
from .conversor import factories as factories_conversor

from .team_member import team_member as etl_team_member
from .user_story import user_story as etl_user_story
from .sprint import sprint as etl_sprint
import datetime

""" Scrum performed development task """
class scrum_development_task(BaseEntity):
	"""
	Class responsible for retrieve tasks from jira and save them on database
	"""
	def create(self, data: dict, jira_issue: object = None, jira_project: object = None) -> tuple:
		"""Given an issue, creates Scrum Intended Development Task 
		and Scrum Performed Development Task (if is performed)

		Args:
			data (dict): Dict with jira issue information (issue_id = data['content']['all']['issue']['id'])
			jira_issue (object, optional): Issue from Jira
			jira_project (object, optional): Project from Jira

		Returns:
			object, object: Tuple with (scrum intended development task, scrum performed development task)
		"""
		try:
			logging.info("Creating Scrum Development Task")
			
			# print('test')
			if jira_issue is None:
				# check if exists
				issue_id = data['content']['all']['issue']['id']
				ScrumIntentedDevelopmentTask_application = factories.ScrumIntentedDevelopmentTaskFactory()
				ontology_ScrumIntentedDevelopmentTask = ScrumIntentedDevelopmentTask_application.retrive_by_external_uuid(issue_id)
				if (ontology_ScrumIntentedDevelopmentTask != None):
					logging.info("ScrumIntentedDevelopmentTask already exist in database")
					return
				else:
					issue_apl = factory.IssueFactory(user=self.user,apikey=self.key,server=self.url)
					jira_issue = issue_apl.find_by_id(issue_id)
			else:
				# check if exists
				issue_id = jira_issue.id
				ScrumIntentedDevelopmentTask_application = factories.ScrumIntentedDevelopmentTaskFactory()
				ontology_ScrumIntentedDevelopmentTask = ScrumIntentedDevelopmentTask_application.retrive_by_external_uuid(issue_id)
				if (ontology_ScrumIntentedDevelopmentTask != None):
					logging.info("ScrumIntentedDevelopmentTask already exist in database")
					return
			
			# print('test')
			if jira_project is None:
				project_id = data['content']['all']['issue']['fields']['project']['id']
				project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
				jira_project = project_apl.find_by_id(project_id)

			self.conversor = factories_conversor.ConversorTaskFactory(organization = self.organization, 
			data = self.data)
			scrum_intended_development_task, scrum_performed_development_task = self.conversor.convert(
				etl_team_member, etl_user_story, etl_sprint,
				jira_issue, jira_project,
			)

			# print('test')
			intended_task_application = factories.ScrumIntentedDevelopmentTaskFactory()
			scrum_intended_development_task = intended_task_application.create(scrum_intended_development_task)
			self.create_application_reference('issue', scrum_intended_development_task, jira_issue.id, jira_issue.self)

			# print('test')
			if(scrum_performed_development_task is not None):
				performed_task_application = factories.ScrumPerformedDevelopmentTaskFactory()
				scrum_performed_development_task.caused_by = scrum_intended_development_task.id
				performed_task_application.create(scrum_performed_development_task)
				self.create_application_reference('issue', scrum_performed_development_task, jira_issue.id, jira_issue.self)

			# print('AssociationDevelopmentTaskTeamMember')
			# Assignee association_development_task_team_member_table
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
				association = factories_model.AssociationDevelopmentTaskTeamMemberFactory()
				association.date = datetime.datetime.now()
				association.activate = True
				association.scrum_development_task_id = scrum_intended_development_task.id
				association.team_member_id = ontology_team_member.id

				ontology_association = factories.AssociationDevelopmentTaskTeamMemberFactory()
				ontology_association.create(association)

			# print('AssociationSprintScrumDevelopmentTask')
			# print('passou assignee')
			# Sprint association_sprint_scrum_development_task_table
			# sprints = jira_issue.raw.get("fields").get("customfield_10018") # wize
			sprint_name = jira_issue.raw.get("fields").get("customfield_10020")[0].get('name') # ledzepplin
			sprint_id = jira_issue.raw.get("fields").get("customfield_10020")[0].get('id') # ledzepplin
			if sprint_name != None:
				sprint_application = factories.SprintFactory()
				ontology_sprint = sprint_application.retrive_by_name_and_project_name(sprint_name, jira_project.name)
				# print(ontology_sprint.id)
				if ontology_sprint is None:
					sprint = etl_sprint()
					sprint.config(self.data, 'sprint')
					data_to_create = {'content':{'all':{'sprint':{'id': sprint_id}}}}
					ontology_sprint = sprint.create(data_to_create, None, jira_project)
				association = factories_model.AssociationSprintScrumDevelopmentTaskFactory()
				association.date = datetime.datetime.now()
				association.activate = True
				association.scrum_development_task_id = scrum_intended_development_task.id
				association.sprint_id = ontology_sprint.id

				ontology_association = factories.AssociationSprintScrumDevelopmentTaskFactory()
				ontology_association.create(association)

			# print('AssociationSprintBacklogScrumDevelopmentActivity')
			# print('passou o sprint')
			# Sprint_backlog association_sprint_backlog_scrum_development_activity_table
			if sprint_name != None:
				sprint_backlog_application = factories.SprintBacklogFactory()
				ontology_sprint_backlog = sprint_backlog_application.retrive_by_name_and_project_name(sprint_name, jira_project.name)
				if ontology_sprint_backlog is None:
					sprint = etl_sprint()
					sprint.config(self.data, 'sprint')
					data_to_create = {'content':{'all':{'sprint':{'id': sprint_id}}}}
					ontology_sprint_backlog = sprint.create(data_to_create, None, jira_project)
				association = factories_model.AssociationSprintBacklogScrumDevelopmentActivityFactory()
				association.date = datetime.datetime.now()
				association.activate = True
				association.scrum_development_task_id = scrum_intended_development_task.id
				association.sprint_backlog_id = ontology_sprint_backlog.id

				ontology_association = factories.AssociationSprintBacklogScrumDevelopmentActivityFactory()
				ontology_association.create(association)

			# print('passou o sprintBacklog')
			
			logging.info("Scrum Development Task created")

			self.insert_one_on_mongo_db(jira_issue.raw, 'issue')

			return scrum_intended_development_task, scrum_performed_development_task

		except Exception as e:
			pprint(e)
			logging.error("Failed to create Scrum Development Task")

	def update(self, data: dict, is_a_task: bool = False) -> tuple:
		"""Update a Scrum Development Task (intended or performed)

		Args:
			data (dict): Dict with jira issue information (issue_id = data['content']['all']['issue']['id'])
			is_a_task (bool, optional): If the jira's issue is of type Task, then True. Defaults to False.

		Returns:
			object, object: Tuple with (scrum intended development task, scrum performed development task)
		"""
		try:
			logging.info("Updating Scrum Development Task")

			issue_id = data['content']['all']['issue']['id']
			issue_apl = factory.IssueFactory(user=self.user,apikey=self.key,server=self.url)
			jira_issue = issue_apl.find_by_id(issue_id)
			
			if is_a_task:
				jira_issue.raw['fields']['parent'] = {'id': jira_issue.id}

			project_id = data['content']['all']['issue']['fields']['project']['id']
			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			jira_project = project_apl.find_by_id(project_id)
			
			intended_task_application = factories.ScrumIntentedDevelopmentTaskFactory()
			performed_task_application = factories.ScrumPerformedDevelopmentTaskFactory()
			ontology_scrum_intended_development_task = intended_task_application.retrive_by_external_uuid(jira_issue.id)
			ontology_scrum_performed_development_task = performed_task_application.retrive_by_external_uuid(jira_issue.id)

			self.conversor = factories_conversor.ConversorTaskFactory(organization = self.organization, data = self.data)
			scrum_intended_development_task, scrum_performed_development_task = self.conversor.convert(
				etl_team_member, etl_user_story, etl_sprint,
				jira_issue, jira_project, 
				ontology_scrum_intended_development_task, ontology_scrum_performed_development_task
			)

			intended_task_application.update(scrum_intended_development_task)
			print(f'Nome da task {scrum_intended_development_task.name}')

			

			if scrum_performed_development_task is not None:
				scrum_performed_development_task.caused_by = scrum_intended_development_task.id
				if ontology_scrum_performed_development_task is None:
					performed_task_application.create(scrum_performed_development_task)
					self.create_application_reference('issue', scrum_performed_development_task, jira_issue.id, jira_issue.self)
				else:
					performed_task_application.update(scrum_performed_development_task)
			
			logging.info("Scrum Development Task updated")

			self.find_one_and_update_on_mongo_db('issue', jira_issue.raw, 'id', jira_issue.raw['id'])

			return scrum_intended_development_task, scrum_performed_development_task

		except Exception as e:
			pprint(e)
			logging.error("Failed to update Scrum Development Task")

	def delete(self, data):
		pass

	def extract(self, data: dict) -> None:
		"""Retrieve all issues from all projects and save them on mongo

		Args:
			data (dict): With user, key and server to connect with jira
		"""
		try:
			logging.info("Scrum Development Task")

			self.config(data)
			self.delete_data_collection("issue")
			self.delete_data_collection("changelog")

			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			issue_apl = factory.IssueFactory(user=self.user,apikey=self.key,server=self.url)

			projects = project_apl.find_all()
			
			for project in tqdm(projects, desc='Issue'):
				issue_list = []	
				issues = issue_apl.find_by_project(project.key)
				
				for issue in issues:					
					issue_new = issue.raw
					
					#IDs do SRO
					issue_new['sro_db_project_id'] = 0
					issue_new['sro_db_development_team_id'] = 0
					issue_new['sro_db_product_backlog_id'] = 0
										
					issue_new['sro_db_reporter_id'] = 0
					issue_new['sro_db_creator_id'] = 0
					issue_new['sro_db_assignee_id'] = 0	

					issue_new['sro_db_activated_id'] = 0
					issue_new['sro_db_resolved_id'] = 0
					issue_new['sro_db_closed_id'] = 0	

					
					issue_new['sro_db_member_team_reporter_id'] = 0
					issue_new['sro_db_member_team_creator_id'] = 0
					issue_new['sro_db_member_team_assignee_id'] = 0	

					issue_new['sro_db_member_team_activated_id'] = 0
					issue_new['sro_db_member_team_resolved_id'] = 0
					issue_new['sro_db_member_team_closed_id'] = 0

					issue_new['sro_db_sprints'] = []
					issue_new['sro_db_sprint_backlogs'] = []

					#IDs do Jira
					issue_new['project_id'] = project.id
					issue_new['creator_id'] = 0
					issue_new['assignee_id'] = 0 
					issue_new['reporter_id'] = 0 
					issue_new['closed_id'] = 0
					issue_new['resolved_id'] = 0
					issue_new['activated_id'] = 0
					
					issue_new['activated_date'] = ""
					issue_new['resolved_date'] = ""
					issue_new['closed_date'] = ""
										
					issue_new['task_parent_id'] = ""
					issue_new['task_parent_type'] = ""
					
					issue_new['task_type_name'] = None
					issue_new['priority_name'] = None

					issue_new['create_performed_task'] = False
					#saber qual é a história de usuário ou epic
					issue_new['sro_db_task_parent_id'] = 0
					
					if issue.fields.status.statusCategory.id == 3 or issue.fields.status.statusCategory.id == 4:
						issue_new['create_performed_task'] = True
					
					if issue.fields.customfield_10018 is not None:
						for sprint_db in issue.fields.customfield_10018:
							
							issue_new['sprints_db_'+str(sprint_db.id)] = sprint_db.id						
					
					if 	issue.fields.creator is not None:
						issue_new['creator_id'] = issue.fields.creator.accountId
					
					if 	issue.fields.assignee is not None:
						issue_new['assignee_id'] = issue.fields.assignee.accountId
					
					if issue.fields.reporter is not None:
						issue_new['reporter_id'] = issue.fields.reporter.accountId
					
					if len(issue.fields.labels) >0:

						task_type_name = issue.fields.labels[0].lower()
						issue_new['task_type_name'] = task_type_name
						
					if issue.fields.priority is not None:
						priority_name = issue.fields.priority.name
						issue_new['priority_name'] = priority_name						
					
					if 'parent' in issue_new['fields']:
						if issue_new['fields']['parent']  is not None: 
							issue_new['task_parent_id'] = issue_new['fields']['parent']['id']
    				
					issue_list.append(issue_new)
									
				#Criando salvando os dados no mongo
				self.insert_many_on_mongo_db(issue_list,"issue")
			
			logging.info("Successfully done Scrum Development Task")

		except Exception as e:
			pprint(e)
			logging.error("Failed to do Scrum Development Task")

	def create_scrum_development_task(self, jira_development_task: list, priority_dict: dict, development_task_type_dict: dict) -> None:
		"""Retrieve all tasks from the projects and save them on sro db as 
		Scrum performed development task

		Args:
			jira_development_task (list): List of dicts, each dict is a issue saved on mongo
			priority_dict (dict): Dict of priorities, mapping name to id on sro db
			development_task_type_dict (dict): Dict of types, also mapping name to id on sro db
		"""
		try:
			logging.info("Scrum Development Task")

			scrum_intended_development_task_list = []
			scrum_performed_development_task_list = []

			#Processando os ontology_scrum_intended_development_task
			for jira_element in jira_development_task:
				
				ontology_scrum_intended_development_task = factories_model.ScrumIntentedDevelopmentTaskFactory()
				
				scrum_intended_development_task_list.append (ontology_scrum_intended_development_task)
				
				ontology_scrum_intended_development_task.created_by_sro = False

				self.fill_development_task(ontology_scrum_intended_development_task,jira_element)

				if jira_element['task_type_name'] is not None:
    					task_type_name = jira_element['task_type_name'].lower()
    					ontology_scrum_intended_development_task.type_activity = development_task_type_dict[task_type_name]

				if jira_element['priority_name'] is not None:
    				
					priority_name = jira_element['priority_name'].lower()	
					
					ontology_scrum_intended_development_task.priority = priority_dict[priority_name]
				
				### Se entrar, é necessário criar um performand e buscar uma intended com o mesmo id do jira_element_id
				if jira_element['create_performed_task'] is True: 
					
					ontology_scrum_performed_development_task = factories_model.ScrumPerformedDevelopmentTaskFactory()
					scrum_performed_development_task_list.append (ontology_scrum_performed_development_task)
										
					self.fill_development_task(ontology_scrum_performed_development_task,jira_element)
			
				
			#### Salvando no banco
			

			intended_task_application = factories.ScrumIntentedDevelopmentTaskFactory()
			performed_task_application = factories.ScrumPerformedDevelopmentTaskFactory()

			scrum_intended_development_task_list = intended_task_application.create_bulk(scrum_intended_development_task_list)

			#Vericando qual o id do jira está relacioado com o ID do SRO
			scrum_intented_development_task_dict = {}
			for scrum_intended_development_task in scrum_intended_development_task_list:
				jira_id = scrum_intended_development_task.jira_element['id']
				scrum_intented_development_task_dict [jira_id] = scrum_intended_development_task.id	

			# associando o Intented com Performed
			for scrum_performed_development_task in scrum_performed_development_task_list:
				jira_id = scrum_performed_development_task.jira_element['id']	
				scrum_performed_development_task.caused_by = scrum_intented_development_task_dict [jira_id]
			
			scrum_performed_development_task_list = performed_task_application.create_bulk(scrum_performed_development_task_list)
						
			self.create_application_reference_bulk(scrum_intended_development_task_list,'issue','id','self')
			self.create_application_reference_bulk(scrum_performed_development_task_list,'issue','id','self')
			

			#Salvando a relação entre team member e assigned da tarefa	
			self.create_development_task_teammember(scrum_intended_development_task_list,scrum_performed_development_task_list)

			#salvando a relação entre tarefa e o sprint	
			self.create_sprint_development_task(scrum_intended_development_task_list,scrum_performed_development_task_list)

			#salvando sprint_backlog e tarefa
			self.create_sprint_backlog_development_task(scrum_intended_development_task_list,scrum_performed_development_task_list)
			
			logging.info("Successfully done Scrum Development Task")
		
		except Exception as e:
			pprint(e)
			logging.error("Failed to do Scrum Development Task")
   		
	def do(self, data: dict) -> None:
		"""Retrieve all tasks from the projects and save them on db as 
		Scrum performed development task

		Args:
			data (dict): With user, key and server to connect with jira
		"""
		try:
			logging.info("Scrum Development Task")

			self.config(data)

			#Buscando os dados salvos no banco do mongo
			mongo_collection_name = self.mongo_db.get_collection('issue')

			#Buscando os priority do banco
			priority_application = factories.PriorityFactory()
			priority_dict = {}
			for priority in priority_application.get_all():
				priority_dict [priority.name.lower()] = priority.id
			
			
			#Buscando os scrum development type do banco
			development_task_type_application = factories.DevelopmentTaskTypeFactory()
			development_task_type_dict = {}

			for development_task_type in development_task_type_application.get_all():
				development_task_type_dict [development_task_type.name.lower()] = development_task_type.id

			jira_development_task = mongo_collection_name.find({"fields.issuetype.name":"Subtarefa"})

			self.create_scrum_development_task(jira_development_task,priority_dict,development_task_type_dict)
			
			#criando as tarefas que não são subtasks
			jira_development_task = mongo_collection_name.find({"fields.issuetype.name":"Tarefa"})
			
			self.create_scrum_development_task(jira_development_task,priority_dict,development_task_type_dict)

			logging.info("Successfully done Scrum Development Task")
		
		except Exception as e:
			pprint(e)
			logging.error("Failed to do Scrum Development Task")

	def update_by_time(self, data: dict, time: str) -> None:
		"""Retrieve subtasks from jira and save them on sro's database

		Args:
			data (dict): With user, key and server to connect with jira
			time (str): '1d' Will bring all epics created or updated on last 24h
		"""
		try:
			logging.info("Update Scrum Development Task by time")
			self.config(data)

			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			issue_apl = factory.IssueFactory(user=self.user,apikey=self.key,server=self.url)
			intended_task_application = factories.ScrumIntentedDevelopmentTaskFactory()
			performed_task_application = factories.ScrumPerformedDevelopmentTaskFactory()

			projects = project_apl.find_all()
			for project in tqdm(projects, desc='Scrum Development Task'):
				tasks = issue_apl.find_sub_task_by_project(project.key, time)
				for jira_task in tasks:
					ontology_scrum_intended_development_task = intended_task_application.retrive_by_external_uuid(jira_task.id)
					if ontology_scrum_intended_development_task is not None:
						ontology_scrum_performed_development_task = performed_task_application.retrive_by_external_uuid(jira_task.id)
						scrum_intended_development_task, scrum_performed_development_task = self.conversor.task(
							etl_team_member, etl_user_story, etl_sprint,
							jira_task, project, 
							ontology_scrum_intended_development_task, ontology_scrum_performed_development_task
						)
						intended_task_application.update(scrum_intended_development_task)
						if scrum_performed_development_task is not None:
							if ontology_scrum_performed_development_task is None:
								performed_task_application.create(scrum_performed_development_task)
								self.create_application_reference('issue', scrum_performed_development_task, jira_task.id, jira_task.self)
							else:
								performed_task_application.update(scrum_performed_development_task)
					else:
						self.create(None, jira_task, project)

			logging.info("Successfully updated Scrum Development Task by time")

		except Exception as e:
			pprint(e)
			logging.error("Failed to update Scrum Development Task by time")
