import logging
import datetime
logging.basicConfig(level=logging.INFO)

from jiraX import factories as factory
from pprint import pprint
from .base_entity import BaseEntity
from tqdm import tqdm

from sro_db.application import factories
from sro_db.model import factories as factories_model
from .conversor import factories as factories_conversor

from .scrum_project import scrum_project as etl_scrum_project

""" Sprint (Time box) """
class sprint(BaseEntity):
	"""
	Class responsible for retrieve sprints from jira
	"""
	def create(self, data: dict, jira_sprint: object = None, jira_project: object = None) -> tuple:
		"""Create a sprint and save it on database. Also save a sprint backlog

		Args:
			data (dict): Dict with jira sprint information (sprint_id = data['content']['all']['sprint']['id'])
			jira_sprint (object, optional): Sprint from Jira
			jira_project (object, optional): Project from Jira

		Returns:
			tuple[object, object]: Tuple with (sprint, sprint backlog)
		"""
		try:
			logging.info("Creating Sprint")


			if jira_sprint is None:
				# check if exists in database
				sprint_id = data['content']['all']['sprint']['id']
				Sprint_application = factories.SprintFactory()
				ontology_Sprint = Sprint_application.retrive_by_external_uuid(sprint_id)
				if (ontology_Sprint != None):
					logging.info("Sprint already exist in database")
					return
				else:
					sprint_apl = factory.SprintFactory(user=self.user,apikey=self.key,server=self.url)
					jira_sprint = sprint_apl.find_by_id(sprint_id)
			else:
				# check if exists in database
				sprint_id = jira_sprint.id
				Sprint_application = factories.SprintFactory()
				ontology_Sprint = Sprint_application.retrive_by_external_uuid(sprint_id)
				if (ontology_Sprint != None):
					logging.info("Sprint already exist in database")
					return

			if jira_project is None:
				board_id = data['content']['all']['sprint']['originBoardId']
				project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
				jira_project = project_apl.find_by_board_id(board_id)

			sprint_backlog_application = factories.SprintBacklogFactory()
			sprint_application = factories.SprintFactory()

			self.conversor = factories_conversor.ConversorSprintFactory(organization = self.organization, data = self.data)
			sprint, sprint_backlog = self.conversor.convert(
				etl_scrum_project,
				jira_sprint, jira_project)
			
			sprint = sprint_application.create(sprint)
			self.create_application_reference('sprint', sprint, jira_sprint.id, jira_sprint.self)
			sprint_backlog.sprint = sprint.id
			sprint_backlog = sprint_backlog_application.create(sprint_backlog)
			self.create_application_reference('sprint', sprint_backlog, jira_sprint.id, jira_sprint.self)

			logging.info("Sprint created")

			board_apl = factory.BoardFactory(user=self.user,apikey=self.key,server=self.url)
			project_id = jira_project.raw['id']
			board_id = jira_sprint.raw['originBoardId']

			board_new = board_apl.get_config(board_id)
			board_new['project_id'] = project_id
			columns_list = board_new['columnConfig']['columns']
			board_new['status_ids'] = [_dict['statuses'][0]['id'] for _dict in columns_list]

			sprint_new = jira_sprint.raw
			sprint_new['board_id'] = board_id
			sprint_new['project_id'] = project_id
			scrum_process_application = factories.ScrumProcessFactory()
			sro_scrum_process = scrum_process_application.retrive_by_external_uuid(project_id)
			sprint_new['sro_db_process_id'] = sro_scrum_process.id

			self.insert_one_on_mongo_db(sprint_new, 'sprint')
			self.insert_one_on_mongo_db(board_new, 'board')

			return sprint, sprint_backlog
			
		except Exception as e:
			pprint(e)
			logging.error("Failed to create Sprint")

	def update (self, data: dict) -> tuple:
		"""Update a sprint and sprint backlog on sro db

		Args:
			data (dict): Dict with jira sprint information (sprint_id = data['content']['all']['sprint']['id'])
			and board information (board_id = data['content']['all']['sprint']['originBoardId'])

		Returns:
			tuple[object, object]: Tuple with (sprint, sprint backlog)
		"""
		try:
			logging.info("Updating Sprint")

			sprint_application = factories.SprintFactory()
			sprint_backlog_application = factories.SprintBacklogFactory()

			sprint_id = data['content']['all']['sprint']['id']
			sprint_apl = factory.SprintFactory(user=self.user,apikey=self.key,server=self.url)
			jira_sprint = sprint_apl.find_by_id(sprint_id)

			board_id = data['content']['all']['sprint']['originBoardId']
			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			jira_project = project_apl.find_by_board_id(board_id)

			#Update
			ontology_sprint = sprint_application.retrive_by_external_uuid(jira_sprint.id)
			ontology_sprint_backlog = sprint_backlog_application.retrive_by_external_uuid(jira_sprint.id)
			
			self.conversor = factories_conversor.ConversorSprintFactory(organization = self.organization, data = self.data)
			sprint, sprint_backlog = self.conversor.convert(
				etl_scrum_project,
				jira_sprint, jira_project, 
				ontology_sprint, ontology_sprint_backlog)
			sprint_application.update(sprint)
			sprint_backlog.sprint = sprint.id
			sprint_backlog_application.update(sprint_backlog)

			logging.info("Sprint updated")

			self.find_one_and_update_on_mongo_db('sprint', jira_sprint.raw, 'id', jira_sprint.raw['id'])
			
			return sprint, sprint_backlog

		except Exception as e:
			pprint(e)
			logging.error("Failed to update Sprint")

	def delete (self, data):
		pass

	def extract(self, data: dict) -> None:
		"""Retrive all sprints and boards from Jira API and save them on mongo db

		Args:
			data (dict): With user, key and server to connect with jira

		Returns:
			dict: Key is the project's key and value is a list with all sprints of this project
		"""
		try:
			logging.info("Sprint")
			self.config(data)
			self.delete_data_collection("sprint")
			self.delete_data_collection("board")
			
			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			board_apl = factory.BoardFactory(user=self.user,apikey=self.key,server=self.url)
			sprint_apl = factory.SprintFactory(user=self.user,apikey=self.key,server=self.url)
		
			board_list = []
			new_sprints = []
			projects = project_apl.find_all()
			for project in tqdm(projects, desc='Sprint'):
				try:
					boards = board_apl.find_by_project(project.key)
					if(boards != None):
						for board in boards:
							try:
								# Buscando a configuração dos board
								board_new = board_apl.get_config(board.id)
								board_new ['project_id'] = project.id
								columns_list = board_new['columnConfig']['columns']
								board_new['status_ids'] = [_dict['statuses'][0]['id'] for _dict in columns_list] 
								board_list.append (board_new)
								
								sprints = sprint_apl.find_by_board(board.id)
								
								for sprint in sprints:
									sprint_new = sprint.raw
									sprint_new['board_id'] = board.id
									sprint_new['project_id'] = project.id
									sprint_new['sro_db_process_id'] = 0
									new_sprints.append(sprint_new)
									
							except Exception as e:
								pprint (e)
								logging.info("O quadro não aceita sprints")
				except Exception as e:
					pprint (e)
					logging.info("O quadro não aceita sprints")
			self.insert_many_on_mongo_db(new_sprints,"sprint")																
			self.insert_many_on_mongo_db(board_list,"board")

			logging.info("Successfully done Sprint")
			return new_sprints
			
		except Exception as e:
			pprint(e)
			logging.error("Failed to do Sprint")
			pass
	
	def do(self, data: dict) -> None:
		"""Retrieve all sprints from mongo and save them on sro db

		Args:
			data (dict): With user, key and server to connect with jira

		Returns:
			dict: Key is the project's key and value is a list with all sprints of this project
		"""
		try:
			logging.info("Sprint")
			pprint ("sprint")
			
			self.config(data)
			
			#Buscando os dados salvos no banco do mongo
			mongo_collection_name = self.mongo_db.get_collection('sprint')
		
			sprints = mongo_collection_name.find({},{ "id": 1, "project_id": 1, "name": 1,'goal':1, "startDate":1,"endDate":1, "completeDate":1 , "self": 1, "sro_db_process_id": 1 })
			
			sprints_list = []

			for jira_element in sprints:
				
				ontology_sprint = factories_model.SprintFactory()
				
				ontology_sprint.organization_id = self.organization.id
				
				if 'name' in jira_element:
					ontology_sprint.name = jira_element['name']				
				
				if 'goal' in jira_element:
					ontology_sprint.description = jira_element['goal']
				
				if 'startDate' in jira_element:
					ontology_sprint.start_date = self.date_formater(jira_element['startDate'])
				
				if 'endDate' in jira_element:
					ontology_sprint.end_date = self.date_formater(jira_element['endDate'])
				
				if "completeDate" in jira_element:
					ontology_sprint.complete_date = self.date_formater(jira_element['completeDate'])
				
				ontology_sprint.jira_element = jira_element
				ontology_sprint.jira_project_id = jira_element['project_id']
				ontology_sprint.jira_sprint_id = jira_element['id']	

				ontology_sprint.scrum_process_id = jira_element['sro_db_process_id']
				sprints_list.append (ontology_sprint)
			
			
			sprint_application = factories.SprintFactory()
			sprints_list = sprint_application.create_bulk (sprints_list)
			self.create_application_reference_bulk(sprints_list,'sprint','id','self')

			sprint_backlog_list = []
			sprint_backlog_application = factories.SprintBacklogFactory()

			for sprint in sprints_list:
				ontology_sprint_backlog = factories_model.SprintBacklogFactory()
				ontology_sprint_backlog.sprint = sprint.id
				ontology_sprint_backlog.name = sprint.name
				ontology_sprint_backlog.sro_sprint = sprint
				sprint_backlog_list.append(ontology_sprint_backlog)
			
			#Criando o sprint_backlog
			sprint_backlog_list = sprint_backlog_application.create_bulk(sprint_backlog_list)

			#atualizando o sprint com o ID do projeto
			for ontology_sprint_backlog in sprint_backlog_list:
    		
				index_value = ontology_sprint_backlog.sro_sprint.jira_sprint_id
				index_value_project_id = ontology_sprint_backlog.sro_sprint.jira_project_id

				field_value = ontology_sprint_backlog.sro_sprint.id
				filed_value_ontology_sprint_backlog = ontology_sprint_backlog.id

				self.update_one_query_array("issue", "sprints_db_"+str(index_value), index_value, "project_id", str(index_value_project_id),"sro_db_sprints",field_value)
				self.update_one_query_array("issue", "sprints_db_"+str(index_value), index_value, "project_id", str(index_value_project_id),"sro_db_sprint_backlogs",filed_value_ontology_sprint_backlog)
				
			
			pprint ("Successfully done Sprint")
		except Exception as e:
			pprint(e)
			logging.error("Failed to do Sprint")
			pass

