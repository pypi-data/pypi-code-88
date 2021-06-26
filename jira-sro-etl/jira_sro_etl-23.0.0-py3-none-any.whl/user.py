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

""" User """
class user(BaseEntity):
	"""
	Class responsible for retrieve users from jira and sabe them on database
	"""
	def create(self, data: dict, jira_user: object = None) -> object:
		"""Create a Person on Sro's database (if this person already exists, do nothing)

		Args:
			data (dict): Dict with jira user information (user_id = data['content']['all']['user']['accountId'])
			jira_user (object, optional): User from Jira. Defaults to None.

		Returns:
			object: Person created by a sro_db's factory
		"""
		try:
			logging.info("Creating User")

			if jira_user is None:
				# Check if exists in the database
				user_id = data['content']['all']['user']['accountId']
				person_application = factories.PersonFactory()
				ontology_scrum_project = person_application.retrive_by_external_uuid(user_id)
				if (ontology_scrum_project != None):
					logging.info("User already exist in database")
					return
				else:
					user_apl = factory.UserFactory(user=self.user,apikey=self.key,server=self.url)
					jira_user = user_apl.find_by_id(user_id)
			else:
				# Check if exists in the database
				user_id = jira_user.id
				person_application = factories.PersonFactory()
				ontology_scrum_project = person_application.retrive_by_external_uuid(user_id)
				if (ontology_scrum_project != None):
					logging.info("User already exist in database")
					return

			self.conversor = factories_conversor.ConversorUserFactory(organization = self.organization, data = self.data)
			person = self.conversor.convert(jira_user)
			
			person_application = factories.PersonFactory()
			person = person_application.create(person)
			self.create_application_reference('user', person, jira_user.accountId, jira_user.self)

			logging.info("User created")

			self.insert_one_on_mongo_db(jira_user.raw,"user")

			return person

		except Exception as e:
			pprint(e)
			logging.error("Failed to create User")

	def update(self, data: dict) -> object:
		"""Update a Person on Sro's database 

		Args:
			data (dict): Dict with jira user information (user_id = data['content']['all']['user']['accountId'])

		Returns:
			object: Person created by a sro_db's factory
		"""
		try:
			logging.info("Updating User")
			user_id = data['content']['all']['user']['accountId']
			user_apl = factory.UserFactory(user=self.user,apikey=self.key,server=self.url)
			jira_user = user_apl.find_by_id(user_id)

			person_application = factories.PersonFactory()
			ontology_user = person_application.retrive_by_external_uuid(jira_user.accountId)
			
			self.conversor = factories_conversor.ConversorUserFactory(organization = self.organization, data = self.data)
			person = self.conversor.convert(jira_user, ontology_user)
			person_application.update(person)

			logging.info("User updated")

			self.find_one_and_update_on_mongo_db('user', jira_user.raw, 'accountId', jira_user.raw['accountId'])

			return person

		except Exception as e:
			pprint(e)
			logging.error("Failed to update User")

	def delete(self, data):
		pass
	
	def extract(self, data: dict):
		"""Retrieve all users from jira api and save them on mongo db

		Args:
			data (dict): With user, key and server to connect with jira

		Returns:
			InsertManyResult: Return of insert_many
		"""
		try:
			logging.info("User")
			
			self.config(data)
			self.delete_data_collection("user")
			
			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			user_apl = factory.UserFactory(user=self.user,apikey=self.key,server=self.url)
			members = list({str(member.accountId): member.raw 
				for project in project_apl.find_all() 
				for member in user_apl.find_by_project(project.key)}.values())
			
			pprint ("USER: extract ")

			return self.insert_many_on_mongo_db(members,"user")
						
			logging.info("Successfully done User")

		except Exception as e:
			pprint(e)
			logging.error("Failed to do User")

	def do(self, data: dict) -> None:
		"""Retrieve all users from mongo db and save on database.
		Also fill issue fields related to user with their id

		Args:
			data (dict): With user, key and server to connect with jira
		"""
		try:
			self.config(data)

			#Buscando os dados salvos no banco do mongo
			mongo_collection_name = self.mongo_db.get_collection('user')
			
			result = mongo_collection_name.find({},{ "accountId": 1, "displayName": 1, "emailAddress": 1, 'self': 1 })			
			
			people = []
			application_reference_list = []

			for jira_user in  tqdm(result, desc='User - SRO_DB'):
    				
				ontology_user = factories_model.PersonFactory()        
				ontology_user.organization_id = self.organization.id
				
				ontology_user.name = jira_user['displayName']
				if jira_user['emailAddress'] != '':
					ontology_user.email = jira_user['emailAddress']
				
				# Adicionando o elemento do jira na classe da ontologia
				ontology_user.jira_element = jira_user
				
				people.append (ontology_user)
			
			person_application = factories.PersonFactory()
			#Salvando todos de uma só vez
			people = person_application.create_bulk(people)
			
			#criando o application reference
			self.create_application_reference_bulk(people,'user','accountId','self')

			#atualizando o user story com o ID do update team_member
			for person in people:
				index_value = person.jira_element['accountId']
				field_value = person.id
				
				self.update_one_query("issue", "creator_id", index_value, "sro_db_creator_id",field_value)
				self.update_one_query("issue", "assignee_id", index_value, "sro_db_assignee_id",field_value)
				self.update_one_query("issue", "reporter_id", index_value, "sro_db_reporter_id",field_value)

				self.update_one_query("issue", "activated_id", index_value, "sro_db_activated_id",field_value)
				self.update_one_query("issue", "resolved_id", index_value, "sro_db_resolved_id",field_value)
				self.update_one_query("issue", "closed_id", index_value, "sro_db_closed_id",field_value)
			

			logging.info("Successfully done User")

		except Exception as e:
			pprint(e)
			logging.error("Failed to do User")


