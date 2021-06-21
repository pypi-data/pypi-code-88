import logging
logging.basicConfig(level=logging.INFO)

from jiraX import factories as factory
from pprint import pprint
from .base_entity import BaseEntity

from sro_db.application import factories
from sro_db.model import factories as factories_model
from .conversor import factories as factories_conversor

from .user import user as etl_user
from .scrum_development_team import scrum_development_team as etl_scrum_development_team
import json 

""" Team member of a project """
class team_member(BaseEntity):
	"""
	Class responsible for retrieve team members from jira and save on database
	"""
	def create(self, data: dict, jira_user: object = None, jira_project: object = None) -> object:
		"""Create a Team Member on Sro's database (if this team member already exists, do nothing)

		Args:
			data (dict): Dict with jira project information (project_id = data['project_id']) 
			and user information (user_accountId = data['accountId'])
			jira_user (object, optional): User from Jira
			jira_project (object, optional): Project from Jira
		
		Returns:
			object: TeamMember created by a sro_db's factory
		"""
		try:
			logging.info("Creating Team Member")
			# print(data)
			print('test')


			if jira_project is None:
				project_id = data['project_id']

				# check if exists in the database
				team_member_application = factories.TeamMemberFactory()
				ontology_team_member = team_member_application.retrive_by_external_uuid(project_id)
				if (ontology_team_member != None):
					logging.info("Team Member already exist in database")
					return
				else:
					project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
					jira_project = project_apl.find_by_id(project_id)

			else:
				# check if exists in the database
				project_id = jira_project.id
				team_member_application = factories.TeamMemberFactory()
				ontology_team_member = team_member_application.retrive_by_external_uuid(project_id)
				if (ontology_team_member != None):
					logging.info("Team Member already exist in database")
					return
			# print("criou projeto")


			if jira_user is None:
				user_accountId = data['accountId']
				user_apl = factory.UserFactory(user=self.user,apikey=self.key,server=self.url)
				jira_user = user_apl.find_by_project_key_and_accountId(jira_project.key, user_accountId)
			# print("criou user")


			self.conversor = factories_conversor.ConversorTeamMemberFactory(organization = self.organization, data = self.data)
			team_member = self.conversor.convert(
				etl_user, etl_scrum_development_team, 
				jira_user, jira_project)
			developer_application = factories.DeveloperFactory()
			team_member = developer_application.create(team_member)
			print(team_member)
			#Essa classe não tem application reference

			logging.info("Team Member created")

			return team_member

		except Exception as e:
			pprint(e)
			logging.error("Failed to create Team Member")

	def update(self, data: dict) -> object:
		"""Update a Team Member on Sro's database

		Args:
			data (dict): With user information (account_id = data['accountId']) and 
			project information (project_id = data['project_id'])

		Returns:
			object: TeamMember created by a sro_db's factory
		"""
		try:
			logging.info("Updating Team Member")

			user_accountId = data['accountId']
			project_id = data['project_id']

			developer_application = factories.DeveloperFactory()
			team_member_application = factories.TeamMemberFactory()

			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			user_apl = factory.UserFactory(user=self.user,apikey=self.key,server=self.url)
			project = project_apl.find_by_id(project_id)
			user = user_apl.find_by_project_key_and_accountId(project.key, user_accountId)

			self.conversor = factories_conversor.ConversorUserFactory(organization = self.organization, data = self.data)
			team_member = self.conversor.convert(
				user,
				project,
				team_member_application.retrive_by_external_id_and_project_name(user.accountId, project.name)
			)
			developer_application.update(team_member)

			logging.info("Team Member updated")

			return team_member

		except Exception as e:
			pprint(e)
			logging.error("Failed to update Team Member")

	def delete(self, data):
		pass

	def extract (self, data):
		pass

	def __create_developer(self, person_id: int, team_id: int) -> object:
		"""Create a sro Developer

		Args:
			person_id (int): id to Person on sro db
			team_id (int): id to Team on sro db

		Returns:
			object: Developer created by a sro_db's factory
		"""
		ontology_team_member = factories_model.DeveloperFactory()
		ontology_team_member.team_role = 'developer'
		ontology_team_member.person_id = person_id
		ontology_team_member.team_id = team_id 
		return ontology_team_member

	def __create_team_member(self, people: list, sro_db_development_teams_dict: dict, project_person_dict: dict) -> tuple:
		"""[summary]

		Args:
			people (list): List of person (are dicts)
			sro_db_development_teams_dict (dict): Keys are project ids and values are team ids
			project_person_dict (dict): Keys are project ids and values are lists with person ids

		Returns:
			tuple[list, dict]: Tuple with (list of Developers, project_person_dict)
		"""
		ontology_team_member_list = []
			
		for person in people:
    				
			project_id = person['_id']
			sro_db_team_member_ids = person['people']

			if project_id not in project_person_dict:
				project_person_dict [project_id] = []

			# lista de elementos que já foram salvos no banco de dados de um projeto e de um equipe
			project_person_list	= project_person_dict [project_id]			
			
			#removendo elementos que já foram salvos no banco para inserior apenas novos
			sro_db_team_member_ids = set(sro_db_team_member_ids) - set(project_person_list) 

			for person_id in sro_db_team_member_ids:
				#removendo o usuários não encontrados
			 
				if person_id != 0:
					team_id = sro_db_development_teams_dict [project_id] 
					ontology_team_member = self.__create_developer(person_id,team_id)
					ontology_team_member.jira_project_id = project_id
					ontology_team_member_list.append(ontology_team_member)
					list_member = project_person_dict [project_id]
					list_member.append(person_id)
		
		return ontology_team_member_list, project_person_dict

	def do(self, data: dict) -> None:
		"""Retrieve members from mongo and save them on sro's database.
		Also set the id of created team members on sro_db_member_team_* fields on mongo issue collection

		Args:
			data (dict): With user, key and server to connect with jira
		"""
		try:
			logging.info("Team Member")

			self.config(data)

			mongo_collection_name = self.mongo_db.get_collection('issue')
			
			#Buscando todos os developments teams de um projeto
			sro_db_development_teams = mongo_collection_name.aggregate([ {"$group" : {"_id" : "$project_id", "development_team" : {"$addToSet" : "$sro_db_development_team_id"}}}])
			
			sro_db_development_teams_dict = {}

			#Criando um dicionario de dados relacionando o projeto com o development teams criados
			for sro_db_development_team in sro_db_development_teams:
				
				project_id = sro_db_development_team['_id']
				sro_db_development_team_id = sro_db_development_team['development_team'][0]
				sro_db_development_teams_dict[project_id] = sro_db_development_team_id


			people_strings = ["$sro_db_creator_id", "$sro_db_reporter_id", "$sro_db_assignee_id", "$sro_db_activated_id", "$sro_db_resolved_id", "$sro_db_closed_id"]	
			
			project_person_dict = {}
			
			developer_application = factories.DeveloperFactory()
			
			ontology_team_member_all_list = []
			
			for person_string in people_strings:
    				
				#Buscando as pessoas que foram criadores
				people = mongo_collection_name.aggregate([ {"$group" : {"_id" : "$project_id", "people" : {"$addToSet" : person_string}}}])
				
				#Criando o team member com os ids das pessoas que foram creator
				ontology_team_member_list, project_person_dict  = self.__create_team_member(people,sro_db_development_teams_dict, project_person_dict)
				
				#Salvando no banco
				ontology_team_member_list  = developer_application.create_bulk(ontology_team_member_list)

				ontology_team_member_all_list = ontology_team_member_all_list + ontology_team_member_list
				
			#Atualizando os campos sro_db_member com os valores gerados
			for ontology_team_member in ontology_team_member_all_list:
			
				index_value = ontology_team_member.jira_project_id
				index_value_2 = ontology_team_member.person_id
				field_value = ontology_team_member.id

				self.update_two_query("issue", "project_id", str(index_value), "sro_db_creator_id", index_value_2, "sro_db_member_team_creator_id", field_value)
				self.update_two_query("issue", "project_id", str(index_value), "sro_db_reporter_id", index_value_2, "sro_db_member_team_reporter_id", field_value)
				self.update_two_query("issue", "project_id", str(index_value), "sro_db_assignee_id", index_value_2, "sro_db_member_team_assignee_id", field_value)

				self.update_two_query("issue", "project_id", str(index_value), "sro_db_activated_id", index_value_2, "sro_db_member_team_activated_id", field_value)
				self.update_two_query("issue", "project_id", str(index_value), "sro_db_resolved_id", index_value_2, "sro_db_member_team_resolved_id", field_value)
				self.update_two_query("issue", "project_id", str(index_value), "sro_db_closed_id", index_value_2, "sro_db_member_team_closed_id", field_value)
			

			logging.info("Successfully done Team Member")

		except Exception as e:
			pprint(e)
			logging.error("Failed to do Team Member")

