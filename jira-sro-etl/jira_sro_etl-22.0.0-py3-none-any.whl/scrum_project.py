import logging
from pymongo.results import InsertManyResult
logging.basicConfig(level=logging.INFO)
from tqdm import tqdm

from jiraX import factories as factory
from pprint import pprint
from .base_entity import BaseEntity

from sro_db.application import factories
from sro_db.model import factories as factories_model
from .conversor import factories as factories_conversor

""" Scrum project """
class scrum_project(BaseEntity):
	"""
	Class responsible for retrieve projects from jira and save them on database
	"""

	def create(self, data: dict, jira_project: object = None) -> tuple:
		"""Create a project and save it on database. Also save a scrum process,
		product backlog definition and product_backlog for the project

		Args:
			data (dict): Dict with jira project information (project_id = data['content']['all']['project']['id'])
			jira_project (object, optional): Project from Jira

		Returns:
			object, object: Tuple with (scrum project, scrum process, product backlog definition, product backlog)
		"""
		try:
			logging.info("Creating Scrum Project")

			scrum_project_application = factories.ScrumAtomicProjectFactory()
			scrum_process_application = factories.ScrumProcessFactory()
			product_backlog_definition_application = factories.ProductBacklogDefinitionFactory()
			product_backlog_application = factories.ProductBacklogFactory()
			
			
			if jira_project is None:
				# Check if exists in the database
				project_id = data['content']['all']['project']['id']
				scrum_project_application = factories.ScrumAtomicProjectFactory()
				ontology_scrum_project = scrum_project_application.retrive_by_external_uuid(project_id)
				if (ontology_scrum_project != None):
					logging.info("Scrum Project already exist in database")
					return
				else:
					project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
					jira_project = project_apl.find_by_id(project_id)
			else:
				# Check if exists in the database
				project_id = jira_project.id
				scrum_project_application = factories.ScrumAtomicProjectFactory()
				ontology_scrum_project = scrum_project_application.retrive_by_external_uuid(project_id)
				if (ontology_scrum_project != None):
					logging.info("Scrum Project already exist in database")
					return

			self.conversor = factories_conversor.ConversorProjectFactory(organization = self.organization, data = self.data)
			scrum_project, scrum_process, product_backlog_definition, product_backlog = self.conversor.convert(jira_project)
			

			scrum_project =	scrum_project_application.create(scrum_project)
			self.create_application_reference('project', scrum_project, jira_project.id, jira_project.self)
			
			scrum_process.scrum_project_id = scrum_project.id
			scrum_process = scrum_process_application.create(scrum_process)
			self.create_application_reference('project', scrum_process, jira_project.id, jira_project.self)
			
			product_backlog_definition.scrum_process_id = scrum_process.id
			product_backlog_definition = product_backlog_definition_application.create(product_backlog_definition)
			self.create_application_reference('project', product_backlog_definition, jira_project.id, jira_project.self)
			
			product_backlog.product_backlog_definition_id = product_backlog_definition.id
			product_backlog = product_backlog_application.create(product_backlog)
			self.create_application_reference('project', product_backlog, jira_project.id, jira_project.self)

			logging.info("Scrum Project created")
			
			self.insert_one_on_mongo_db(jira_project.raw,"project")

			return scrum_project, scrum_process, product_backlog_definition, product_backlog

		except Exception as e:
			pprint(e)
			logging.error("Failed to create Scrum Project")

	def update(self, data: dict) -> tuple:
		"""Update a scrum project, scrum process, product backlog definition and 
		product backlog on sro db

		Args:
			data (dict): Dict with jira project information (project_id = data['content']['all']['project']['id'])
		
		Returns:
			object, object, object, object: Tuple with (scrum project, scrum process, product backlog definition, product backlog)
		"""
		try:
			logging.info("Updating Scrum Project")

			scrum_project_application = factories.ScrumAtomicProjectFactory()
			scrum_process_application = factories.ScrumProcessFactory()
			product_backlog_definition_application = factories.ProductBacklogDefinitionFactory()
			product_backlog_application = factories.ProductBacklogFactory()

			content = data['content']
			project = content['all']['project']
			project_id = project['id']
			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			jira_project = project_apl.find_by_id(project_id)

			self.conversor = factories_conversor.ConversorProjectFactory(organization = self.organization, data = self.data)
			scrum_project, scrum_process, product_backlog_definition, product_backlog = self.conversor.convert(
				jira_project,
				scrum_project_application.retrive_by_external_uuid(jira_project.id),
				scrum_process_application.retrive_by_external_uuid(jira_project.id),
				product_backlog_definition_application.retrive_by_external_uuid(jira_project.id),
				product_backlog_application.retrive_by_external_uuid(jira_project.id)
			)
			
			print(f'----- Projeto {scrum_project.name} -----')

			# print('Scrum project')
			scrum_project_application.update(scrum_project)
			# print('Scrum process')
			scrum_process_application.update(scrum_process)
			product_backlog_definition_application.update(product_backlog_definition)
			product_backlog.product_backlog_definition = product_backlog_definition.id
			# print('Scrum product_backlog')
			product_backlog_application.update(product_backlog)
			product_backlog_application.update(product_backlog)
			# exit()

			logging.info("Scrum Project updated")

			self.find_one_and_update_on_mongo_db('project', jira_project.raw, 'id', jira_project.raw['id'])

			return scrum_project, scrum_process, product_backlog_definition, product_backlog

		except Exception as e:
			pprint(e)
			logging.error("Failed to update Scrum Project")

	def delete(self, data):
		pass

	def extract(self, data: dict):
		"""Retrieve all projects from jira API and save them on mongo db

		Args:
			data (dict): With user, key and server to connect with jira

		Returns:
    		InsertManyResult: Return of insert_many
		"""
		try:
			logging.info("Scrum Project")
			self.config(data)
			self.delete_data_collection("project")

			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			projects = project_apl.find_all()

			new_project = []
			for project in tqdm(projects, desc='Scrum Project'):
				project_x = project.raw
				project_x['sro_db_project_id'] = 0
				project_x['sro_db_scrum_team_id'] = 0
				project_x['sro_db_scrum_development_team_id'] = 0
				new_project.append(project.raw)
			
			logging.info("Successfully done Scrum Project")
			pprint ("PROJECT: extract ")
			return self.insert_many_on_mongo_db(new_project,"project")

		except Exception as e:
			pprint(e)
			logging.error("Failed to do Scrum Project")

	def do(self, data: dict) -> None:
		"""Retrieve all projects from mongo and save them on sro db

		Args:
			data (dict): With user, key and server to connect with jira
		"""
		try:
			logging.info("Scrum Project")
			
			self.config(data)
			
			#Buscando os dados salvos no banco do mongo
			mongo_collection_name = self.mongo_db.get_collection('project')
			
			#Select name, key, id, self from Project .. só que no mongo
			projects = mongo_collection_name.find({},{ "id": 1, "name": 1, "key": 1, 'self': 1 })

			scrum_atomic_project_application = factories.ScrumAtomicProjectFactory()
			scrum_process_application = factories.ScrumProcessFactory()
			product_backlog_definition_application = factories.ProductBacklogDefinitionFactory()
			product_backlog_application = factories.ProductBacklogFactory()
			
			scrum_atomic_project_list = []
			ontology_scrum_process_list = []
			ontology_product_backlog_definition_list = []
			ontology_product_backlog_list = []
			
			update_mongo = []
			
			for jira_project in projects:
				
				ontology_scrum_atomic_project = factories_model.ScrumAtomicProjectFactory()
				ontology_scrum_atomic_project.organization_id = self.organization.id
				ontology_scrum_atomic_project.name = jira_project['name']
				ontology_scrum_atomic_project.index = jira_project['key']
				ontology_scrum_atomic_project.jira_element = jira_project

				scrum_atomic_project_list.append (ontology_scrum_atomic_project)
							
			#Salvando todos de uma só vez --> Salvando no Postgres
			scrum_atomic_project_list = scrum_atomic_project_application.create_bulk(scrum_atomic_project_list)

			self.create_application_reference_bulk(scrum_atomic_project_list,'project','id','self')

			for scrum_atomic_project in scrum_atomic_project_list:
				
				ontology_scrum_process = factories_model.ScrumProcessFactory()
				ontology_scrum_process.name = scrum_atomic_project.name
				ontology_scrum_process.scrum_project_id = scrum_atomic_project.id
				ontology_scrum_process.jira_project_id = scrum_atomic_project.jira_element['id']
				ontology_scrum_process_list.append (ontology_scrum_process)	

				jira_element = scrum_atomic_project.jira_element
				jira_element['sro_db_project_id'] = scrum_atomic_project.id
			
				update_mongo.append (jira_element)

				#Aproveitando o loop para atualizar o issue
				index_value = scrum_atomic_project.jira_element['id']
				field_value = scrum_atomic_project.id
				self.update_one_query("issue", "project_id", str(index_value), "sro_db_project_id",field_value)

			ontology_scrum_process_list = scrum_process_application.create_bulk(ontology_scrum_process_list)

			for ontology_scrum_process in ontology_scrum_process_list:
    				
				ontology_product_backlog_definition = factories_model.ProductBacklogDefinitionFactory()
				ontology_product_backlog_definition.name = ontology_scrum_process.name
				ontology_product_backlog_definition.scrum_process_id = ontology_scrum_process.id
				ontology_product_backlog_definition.jira_project_id = ontology_scrum_process.jira_project_id
				ontology_product_backlog_definition_list.append (ontology_product_backlog_definition)

			ontology_product_backlog_definition_list = product_backlog_definition_application.create_bulk(ontology_product_backlog_definition_list)		

			for ontology_product_backlog_definition in ontology_product_backlog_definition_list:
				ontology_product_backlog = factories_model.ProductBacklogFactory()
				ontology_product_backlog.name = ontology_product_backlog_definition.name
				ontology_product_backlog.product_backlog_definition_id = ontology_product_backlog_definition.id
				
				ontology_product_backlog.jira_project_id = ontology_product_backlog_definition.jira_project_id
				ontology_product_backlog_list.append (ontology_product_backlog)

			ontology_product_backlog_list = product_backlog_application.create_bulk(ontology_product_backlog_list)	
			
			#atualuizando o mongo
			self.update_many_on_mongo_db(update_mongo,'project','sro_db_project_id')
			

			#atualizando o sprint com o ID do projeto
			for ontology_scrum_process in ontology_scrum_process_list:
				index_value = ontology_scrum_process.jira_project_id
				field_value = ontology_scrum_process.id
				self.update_one_query("sprint", "project_id", str(index_value), "sro_db_process_id",field_value)

			#atualizando o user story com o ID do product backlog
			for product_backlog in ontology_product_backlog_list:
				index_value = product_backlog.jira_project_id
				field_value = product_backlog.id
				self.update_one_query("issue", "project_id", str(index_value), "sro_db_product_backlog_id",field_value)
			

			logging.info("Successfully done Scrum Project")
			pprint ("Successfully done Scrum Project")

		except Exception as e:
			pprint(e)
			logging.error("Failed to do Scrum Project")

