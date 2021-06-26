import logging
logging.basicConfig(level=logging.INFO)
from .base_entity import BaseEntity
from jiraX import factories as factory
from pprint import pprint
from tqdm import tqdm

from sro_db.application import factories
from sro_db.model import factories as factories_model
from .conversor import factories as factories_conversor

from .scrum_project import scrum_project as etl_scrum_project

""" Scrum development team """
class scrum_project_team(BaseEntity):
	"""
	Class responsible for retrieve teams from jira
	"""

	def create(self, data: dict, jira_project: object = None) -> object:
		"""Create a scrum project team and save it on database.

		Args:
			data (dict): Dict with jira project information (project_id = data['content']['all']['project']['id'])
			jira_project (object, optional): Project from Jira

		Returns:
			object: ScrumTeam created by a sro_db's factory
		"""
		try:
			logging.info("Creating Scrum Project Team")

			scrum_team_application = factories.ScrumTeamFactory()
			ontology = scrum_team_application

			if jira_project is None:
				project_id = data['content']['all']['project']['id']
				project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
				jira_project = project_apl.find_by_id(project_id)
			
			self.conversor = factories_conversor.ConversorTeamFactory(organization = self.organization, data = self.data)
			scrum_team = self.conversor.convert(
				etl_scrum_project,
				jira_project)

			scrum_team = scrum_team_application.create(scrum_team)
			self.create_application_reference('project', scrum_team, jira_project.id)
			
			logging.info("Scrum Project Team created")

			return scrum_team

		except Exception as e:
			pprint(e)
			logging.error("Failed to create Scrum Project Team")

	def update(self, data):
		pass

	def delete(self, data: dict) -> None:
		"""Delete a development team on database.

		Args:
			data (dict): [description]
		"""
		try:
			logging.info("Creating Scrum Project Team")

			scrum_team_application = factories.ScrumTeamFactory()

			content = data['content']
			project = content['all']['project']

			scrum_team = scrum_team_application.retrive_by_external_uuid(project['id'])
			scrum_team_application.delete(scrum_team)

			logging.info("Scrum project Team deleted")

		except Exception as e:
			pprint(e)
			logging.error("Failed to delete Scrum Project Team")

	def do (self, data: dict) -> list:
		"""With data saved on mongo, create and save all scrum teams on sro db

		Args:
			data (dict): With user, key and server to connect with jira

		Returns:
			list: List of all scrum teams
		"""
		try:
			logging.info("Scrum Project Team")

			self.config(data)

			mongo_collection_name = self.mongo_db.get_collection('project')
			
			projects = mongo_collection_name.find({},{ "id": 1, "name": 1, "key": 1, 'self': 1, 'sro_db_project_id': 1 })

			scrum_team_application = factories.ScrumTeamFactory()
			
			scrum_team_list = []

			for jira_project in tqdm(projects, desc='Scrum Project Team'):
				scrum_team = factories_model.ScrumTeamFactory()
				scrum_team.name = jira_project['name']+"_scrum_team"
				scrum_team.organization_id = self.organization.id
				scrum_team.jira_element = jira_project
				scrum_team.scrum_project_id = jira_project['sro_db_project_id']
				scrum_team_list.append (scrum_team)

			scrum_team_list = scrum_team_application.create_bulk(scrum_team_list)
			self.create_application_reference_bulk(scrum_team_list,'project','id','self')
			
			update_mongo = []

			for scrum_team in scrum_team_list:
				jira_element = scrum_team.jira_element
				jira_element['sro_db_scrum_team_id'] = scrum_team.id
				update_mongo.append (jira_element)	
			
			self.update_many_on_mongo_db(update_mongo,'project','sro_db_scrum_team_id')
			
			return scrum_team_list
			
		except Exception as e:
			pprint (e)
